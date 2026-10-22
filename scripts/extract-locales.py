import pathlib,json,re,html
from html.parser import HTMLParser
from tree_sitter import Language,Parser
import tree_sitter_javascript as js
root=pathlib.Path(__file__).resolve().parents[1];strings=set()
def add(s):
 s=html.unescape(s).strip();s=re.sub(r'^[\"\'>]+','',s);s=re.sub(r'\s+',' ',s)
 if re.search('[А-Яа-яЁё]',s) and not any(v in s for v in ['=>','function ','properties.','document.']):strings.add(s)
class Texts(HTMLParser):
 def handle_data(self,s):add(s)
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if v and k in ['title','aria-label','placeholder','data-tip','alt']:add(v)
def markup(s):
 try:Texts().feed(s)
 except Exception:pass
 # Literal fragments adjoining a template expression still need a translation.
 if '<' not in s and '>' not in s:add(s)
def descend(j):
 if isinstance(j,str):add(j)
 elif isinstance(j,list):
  for v in j:descend(v)
 elif isinstance(j,dict):
  for v in j.values():descend(v)
for p in [root/'dist/data/history.json',root/'dist/data/editorial-areas.geojson']:descend(json.loads(p.read_text()))
markup((root/'dist/index.html').read_text())
parser=Parser(Language(js.language()))
for name in ['app.js','core.js','globe.js','regional-history.js','area-history.js','landscapes.js','world-beliefs.js']:
 source=(root/'dist'/name).read_bytes();tree=parser.parse(source)
 def visit(n):
  if n.type=='string':
   v=source[n.start_byte+1:n.end_byte-1].decode();v=re.sub(r'\\([\\\'"`])',r'\1',v).replace('\\n','\n');markup(v);return
  if n.type=='string_fragment' and n.parent.type=='template_string':markup(source[n.start_byte:n.end_byte].decode())
  for c in n.children:visit(c)
 visit(tree.root_node)
(root/'dist/locales').mkdir(exist_ok=True)
(root/'dist/locales/ru-source.json').write_text(json.dumps(sorted(strings),ensure_ascii=False,indent=2)+'\n')
print('translation strings',len(strings))
