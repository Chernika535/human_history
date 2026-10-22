import json,pathlib,urllib.request,urllib.parse,urllib.error,concurrent.futures,time,datetime,sys,re
root=pathlib.Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=True);src=json.load(open(sys.argv[1]))['features'];ids=sorted({f['properties'].get('Wikidata') for f in src if re.fullmatch(r'Q[1-9][0-9]*',f['properties'].get('Wikidata',''))});del src
wanted=['P31','P36','P37','P122','P38','P140','P571','P576','P35','P6'];cache=root/'wikidata-cache.json';data=json.load(open(cache)) if cache.exists() else {}
def get(batch,props):
 url='https://www.wikidata.org/w/api.php?'+urllib.parse.urlencode({'action':'wbgetentities','ids':'|'.join(batch),'props':props,'languages':'ru|en','format':'json','maxlag':'5'})
 for attempt in range(3):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ChronosHistoryAtlas/0.5 (educational historical atlas; github.com/Chernika535/human_history)'}),timeout=45) as r:j=json.load(r)
   if 'error' in j:raise ValueError(str(j['error']))
   return j['entities']
  except Exception as e:
   if attempt==2:print('failed batch',batch[0],type(e).__name__,flush=True);return {}
   time.sleep(min(60,int(e.headers.get('Retry-After','10'))) if isinstance(e,urllib.error.HTTPError) and e.code in [429,503] else 2+attempt*3)
def prune(e):
 return {'id':e['id'],'labels':{l:v['value'] for l,v in e.get('labels',{}).items()},'descriptions':{l:v['value'] for l,v in e.get('descriptions',{}).items()},'claims':{p:e.get('claims',{}).get(p,[]) for p in wanted if p in e.get('claims',{})}}
missing=[i for i in ids if i not in data];batches=[missing[i:i+30] for i in range(0,len(missing),30)]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for idx,result in enumerate(pool.map(lambda b:get(b,'labels|descriptions|claims'),batches)):
  for k,v in result.items():
   if 'missing' not in v:data[k]=prune(v)
  cache.write_text(json.dumps(data,ensure_ascii=False));print('entities',len(data),'/',len(ids),flush=True)
related=set()
for e in data.values():
 for statements in e.get('claims',{}).values():
  for st in statements:
   v=st.get('mainsnak',{}).get('datavalue',{}).get('value',{});
   if isinstance(v,dict) and v.get('id','').startswith('Q'):related.add(v['id'])
labels={k:e['labels'] for k,e in data.items()};missing=sorted(related-set(labels));batches=[missing[i:i+50] for i in range(0,len(missing),50)]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for result in pool.map(lambda b:get(b,'labels'),batches):
  for k,v in result.items():labels[k]={l:x['value'] for l,x in v.get('labels',{}).items()}
(root/'wikidata-labels.json').write_text(json.dumps(labels,ensure_ascii=False));print('done',len(data),'entities',len(labels),'labels',flush=True)
