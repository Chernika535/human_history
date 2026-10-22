# Compile selected CC0 Wikidata statements; never project undated rulers into the past.
import json,pathlib,re,datetime,sys
root=pathlib.Path(__file__).resolve().parents[1];cache=pathlib.Path(sys.argv[1]);data=json.load(open(cache/'wikidata-cache.json'));labels=json.load(open(cache/'wikidata-labels.json'))
props={'P31':['Тип общества','Entity type'],'P36':['Столица','Capital'],'P37':['Язык','Language'],'P122':['Форма правления','Government'],'P38':['Денежная единица','Currency'],'P140':['Религиозная традиция','Religious tradition'],'P35':['Правитель','Ruler'],'P6':['Глава правительства','Head of government']}
def date(s):
 v=s.get('datavalue',{}).get('value',{});t=v.get('time','') if isinstance(v,dict) else '';m=re.match('([+-]\\d+)-',t)
 return int(m[1]) if m and int(m[1]) else None
out={}
for q,e in data.items():
 facts=[]
 for prop,titles in props.items():
  for st in e.get('claims',{}).get(prop,[]):
   if st.get('rank')=='deprecated':continue
   v=st.get('mainsnak',{}).get('datavalue',{}).get('value',{});target=v.get('id') if isinstance(v,dict) else None
   if not target or target not in labels or not labels[target].get('en'):continue
   qual=st.get('qualifiers',{});start=next((date(s) for s in qual.get('P580',[]) if date(s) is not None),None);end=next((date(s) for s in qual.get('P582',[]) if date(s) is not None),None);point=next((date(s) for s in qual.get('P585',[]) if date(s) is not None),None)
   if point is not None and start is None and end is None:start=end=point
   if prop in ['P35','P6'] and (start is None or end is None):continue
   f={'property':prop,'title':{'ru':titles[0],'en':titles[1]},'value':labels[target],'qid':target,'scope':'dated' if start is not None or end is not None else 'general'}
   if start is not None:f['from']=start
   if end is not None:f['to']=end
   if start is not None and end is not None and start>end:continue
   if f not in facts:facts.append(f)
 out[q]={'qid':q,'labels':e['labels'],'description':e['descriptions'],'facts':facts,'source':'https://www.wikidata.org/wiki/'+q}
(root/'dist/data/cliopatria/profiles.json').write_text(json.dumps({'license':'CC0-1.0','retrieved':'2026-10-22','entities':out},ensure_ascii=False,separators=(',',':'))+'\n');print('profiles',len(out),'facts',sum(len(v['facts']) for v in out.values()))
