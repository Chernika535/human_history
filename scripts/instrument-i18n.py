# Wrap DOM rendering boundaries; source strings stay Russian and state keys stay unchanged.
from tree_sitter import Parser,Language
import tree_sitter_javascript as js
from pathlib import Path
root=Path(__file__).resolve().parents[1];parser=Parser(Language(js.language()))
for name in ['app.js','globe.js']:
 p=root/'dist'/name;src=p.read_bytes();tree=parser.parse(src);edits=[]
 def visit(n):
  if n.type=='assignment_expression':
   left=n.child_by_field_name('left');right=n.child_by_field_name('right')
   if left and right and left.type=='member_expression':
    prop=left.child_by_field_name('property');key=src[prop.start_byte:prop.end_byte].decode() if prop else ''
    fn='html' if key=='innerHTML' else 'tx' if key=='textContent' else None
    val=src[right.start_byte:right.end_byte].decode()
    if fn and not val.startswith(fn+'('):edits.append((right.start_byte,right.end_byte,(fn+'('+val+')').encode()))
  if n.type=='call_expression':
   f=n.child_by_field_name('function');args=n.child_by_field_name('arguments')
   if f and args and f.type=='member_expression':
    prop=f.child_by_field_name('property');key=src[prop.start_byte:prop.end_byte].decode() if prop else ''
    values=args.named_children
    if key=='setAttribute' and len(values)>=2:
     attr=src[values[0].start_byte:values[0].end_byte].decode().strip('"\'')
     if attr in ['aria-label','title','aria-valuetext','placeholder']:
      v=values[1];text=src[v.start_byte:v.end_byte].decode()
      if not text.startswith('tx('):edits.append((v.start_byte,v.end_byte,('tx('+text+')').encode()))
  for c in n.children:visit(c)
 visit(tree.root_node)
 # All targeted render values are independent; reject overlap rather than damaging source.
 edits.sort()
 for a,b in zip(edits,edits[1:]):
  if a[1]>b[0]:raise RuntimeError('Nested render edits: '+str((a,b)))
 for a,b,text in reversed(edits):src=src[:a]+text+src[b:]
 p.write_bytes(src);print(name,len(edits))
