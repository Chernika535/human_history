"""Import attributed CC BY-SA encyclopedia leads. Cached retrieval; no runtime external API.
Usage: python scripts/import-encyclopedia.py /absolute/cache
Wikipedia text retains its own CC BY-SA license; code licensing is separate.
"""
import gzip,base64,json,pathlib,urllib.request,urllib.parse,concurrent.futures,time,sys,re
root=pathlib.Path(__file__).resolve().parents[1];cache=pathlib.Path(sys.argv[1]);cache.mkdir(parents=True,exist_ok=True)
catalog=json.load(open(root/'dist/data/cliopatria/catalog.json'))
def request(lang,params):
 if '--offline' in sys.argv:return {}
 url=f'https://{lang}.wikipedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',format='json',formatversion=2,redirects=1,**params))
 for attempt in range(3):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ChronosHistoryAtlas/0.11 (educational atlas; https://github.com/Chernika535/human_history)'}),timeout=40) as r:j=json.load(r)
   if 'error' in j:raise ValueError(j['error'])
   return j
  except Exception as e:
   if attempt==2:print('request failed',lang,str(e)[:70],flush=True);return {}
   time.sleep(2+attempt*3)
extras={'culture:auth-athens':'Classical Athens','culture:auth-sparta':'Sparta','religion:christianity':'Christianity','religion:islam':'Islam','religion:buddhism':'Buddhism','religion:hindu':'Hinduism','religion:judaism':'Judaism','religion:jain':'Jainism','religion:shinto':'Shinto','religion:daoism':'Taoism','religion:confucian':'Confucianism','religion:zoroastrian':'Zoroastrianism','religion:classical':'Religion in ancient Greece','religion:egyptian':'Ancient Egyptian religion','religion:mesopotamian':'Ancient Mesopotamian religion','religion:ritual':'Prehistoric religion','religion:ancestral':'Ancestor veneration','religion:mesoamerican':'Mesoamerican religion','religion:andean':'Inca religion'}
auth={'foragers-africa':'Prehistory of Africa','foragers-eurasia':'Paleolithic','kakadu':'Kakadu National Park','jomon':'Jōmon period','wheat':'Neolithic Revolution','gobekli':'Göbekli Tepe','catal':'Çatalhöyük','kuk':'Kuk Swamp','uruk':'Uruk','liangzhu':'Liangzhu culture','sumer':'Sumer','caral':'Caral–Supe civilization','egypt-old':'Old Kingdom of Egypt','indus':'Indus Valley Civilisation','shang':'Shang dynasty','zhou':'Zhou dynasty','persia':'Achaemenid Empire','buddhist-india':'History of Buddhism in India','han-west':'Han dynasty','rome':'Principate','han-east':'Han dynasty','sasan':'Sasanian Empire','jewish-diaspora':'Jewish diaspora','byz-early':'Byzantine Empire','early-islam':'Early history of Islam','abbasid':'Abbasid Caliphate','cahokia':'Cahokia','angkor':'Angkor','kilwa':'Kilwa Kisiwani','zimbabwe':'Great Zimbabwe','novgorod':'Novgorod Republic','lubeck':'Hanseatic League','mongol':'Mongol Empire','byz-late':'Byzantine Empire under the Palaiologos dynasty','ottoman':'Ottoman Empire','aztec':'Tenochtitlan','ming':'Ming dynasty','inca':'Inca Empire','spain':'Spanish Empire','goree':'Gorée','mughal':'Mughal Empire','potosi':'Potosí','eic-india':'Company rule in India','britain':'British Empire','china-opium':'Opium Wars','un-world':'United Nations','decolon':'Decolonisation','celts':'Celts','deep-mehrgarh':'Mehrgarh','deep-halaf':'Halaf culture','deep-ubaid':'Ubaid period','deep-longshan':'Longshan culture','deep-erlitou':'Erlitou culture','deep-elam':'Elam','deep-akkad':'Akkadian Empire','deep-uriii':'Third Dynasty of Ur','deep-mari':'Mari, Syria','deep-babylon':'First Babylonian Empire','ashur-trade':'Old Assyrian period','deep-hittites':'Hittites','deep-kerma':'Kerma culture','deep-egypt-middle':'Middle Kingdom of Egypt','egypt-new':'New Kingdom of Egypt','deep-kush':'Kingdom of Kush','deep-aksum':'Kingdom of Aksum','deep-minoan':'Minoan civilization','deep-mycenaean':'Mycenaean Greece','deep-phoenicia':'Phoenicia','deep-olmec':'Olmecs','deep-chavin':'Chavín culture','deep-moche':'Moche culture','deep-teotihuacan':'Teotihuacan','deep-tikal':'Tikal','deep-tiwanaku':'Tiwanaku','deep-lapita':'Lapita culture','deep-nabataea':'Nabataean Kingdom','deep-gandhara':'Gandhara','deep-jericho':'Tell es-Sultan','deep-natufian':'Natufian culture'}
extras.update({'culture:'+k:v for k,v in auth.items()});extras.update({'region:'+k:v for k,v in {'antarctica':'History of Antarctica','arctic':'Circumpolar peoples','greenland':'History of Greenland','svalbard':'History of Svalbard','iceland':'History of Iceland','europe':'History of Europe','north-africa':'History of North Africa','west-africa':'History of West Africa','central-africa':'History of Central Africa','east-africa':'History of East Africa','southern-africa':'History of Southern Africa','madagascar':'History of Madagascar','nile':'History of Egypt','west-asia':'History of West Asia','south-asia':'History of South Asia','east-asia':'History of East Asia','southeast-asia':'History of Southeast Asia','steppe':'Eurasian Steppe','siberia':'History of Siberia','north-america':'History of North America','caribbean':'History of the Caribbean','mesoamerica':'Mesoamerican chronology','andes':'Andean civilizations','amazon':'History of Amazonia','southern-america':'History of South America','australia':'History of Indigenous Australians','new-guinea':'History of Papua New Guinea','pacific':'History of Oceania','nz':'History of New Zealand','hawaii':'History of Hawaii'}.items()});mapping={e['id']:e['wikipedia'] for e in catalog};mapping.update(extras)
titles=sorted(set(mapping.values()));english={};russian={}
def load_batches(lang,titles):
 seeded={}
 for cp in cache.glob('*.json'):
  try:
   cached=json.load(open(cp));
   query=cached.get('query',{});old={p['title']:p for p in query.get('pages',[]) if p.get('fullurl','').startswith('https://'+lang+'.wikipedia.org/')};
   for title,page in old.items():
    page['_truncated']=bool(cached.get('warnings'))
    previous=seeded.get(title)
    if previous is None or (previous.get('_truncated',False) and not page['_truncated']) or (previous.get('_truncated',False)==page['_truncated'] and len(page.get('extract',''))>len(previous.get('extract',''))):seeded[title]=page
   normal={p['from']:p['to'] for p in query.get('normalized',[])+query.get('redirects',[])}
   for alias in normal:
    dest=alias;seen=set()
    while dest in normal and dest not in seen:seen.add(dest);dest=normal[dest]
    if dest in seeded:seeded[alias]=seeded[dest]
  except (ValueError,KeyError):pass
 allpages={t:seeded[t] for t in titles if t in seeded};titles=[t for t in titles if t not in seeded];batches=[titles[i:i+15] for i in range(0,len(titles),15)]
 def one(titles):
  if all(t in seeded for t in titles):return {'query':{'pages':list({p['title']:p for t in titles for p in [seeded[t]]}.values()),'redirects':[{'from':t,'to':seeded[t]['title']} for t in titles if t!=seeded[t]['title']]}}
  key=__import__('hashlib').sha256((lang+'full-intro-v2'+'|'.join(titles)).encode()).hexdigest();p=cache/(key+'.json')
  if p.exists():return json.load(open(p))
  j=request(lang,dict(prop='extracts|langlinks|pageprops|info',inprop='url',exintro=1,explaintext=1,exlimit=20,lllang='ru',lllimit=500,titles='|'.join(titles)))
  if j:p.write_text(json.dumps(j,ensure_ascii=False))
  return j
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  for i,j in enumerate(pool.map(one,batches)):
   query=j.get('query',{});pages={p['title']:p for p in query.get('pages',[])};normal={p['from']:p['to'] for p in query.get('normalized',[])+query.get('redirects',[])}
   for batchtitle in batches[i]:
    title=batchtitle;seen=set()
    while title in normal and title not in seen:seen.add(title);title=normal[title]
    if title in pages:allpages[batchtitle]=pages[title]
   if i%10==0:print(lang,'batches',i+1,'/',len(batches),flush=True)
 return allpages
english=load_batches('en',titles);rtitles=sorted({ll['title'] for p in english.values() for ll in p.get('langlinks',[]) if ll['lang']=='ru'});russian=load_batches('ru',rtitles)
def clean(text):return re.sub(r'\s*\[\d+\]\s*',' ',text).strip()
def paragraphs(text):
 ps=[clean(p) for p in text.split('\n') if len(clean(p))>=80 and not p.lstrip().startswith('==')]
 # Preserve prose; split a single long lead at sentence boundaries rather than pad it.
 if len(ps)==1 and len(ps[0])>650:
  sentences=re.split(r'(?<=[.!?])\s+(?=[А-ЯA-Z«])',ps[0]);cut=len(sentences)//2
  if cut and len(' '.join(sentences[:cut]))>200 and len(' '.join(sentences[cut:]))>200:ps=[' '.join(sentences[:cut]),' '.join(sentences[cut:])]
 return ps[:3]
# Short leads are enriched from the article's historical prose, not padded with regional templates.
def enrich_short(lang,pages):
 candidates={p['title']:p for p in pages.values() if p.get('extract') and len(paragraphs(p['extract']))<2 and 'disambiguation' not in p.get('pageprops',{})}
 def one(item):
  title,page=item;key=__import__('hashlib').sha256((lang+'full-untruncated'+title).encode()).hexdigest();p=cache/(key+'.json')
  if p.exists():j=json.load(open(p))
  else:
   j=request(lang,dict(prop='extracts',explaintext=1,exlimit=1,exsectionformat='wiki',titles=title))
   if j:p.write_text(json.dumps(j,ensure_ascii=False))
  full=next(iter(j.get('query',{}).get('pages',[])),{}).get('extract','')
  if full:
   # Prefer the history section when present; retain the article's own introductory paragraph.
   sections=re.split(r'(?m)^==+\s*(.*?)\s*==+\s*$',full)
   lead=paragraphs(sections[0]);history=[]
   for i in range(1,len(sections)-1,2):
    if re.search(r'истори|history|основан|origin|decline',sections[i],re.I):history.extend(paragraphs(sections[i+1]))
   chosen=lead[:1]+(history[:1]+history[-1:] if len(history)>1 else history)
   if len(chosen)<2:chosen=paragraphs(full)
   chosen=list(dict.fromkeys(chosen))[:3]
   if len(chosen)>1:page['_paragraphs']=chosen
  return title
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for i,_ in enumerate(pool.map(one,candidates.items())):
   if i%50==0:print(lang,'expanded',i+1,'/',len(candidates),flush=True)
enrich_short('ru',russian)
# English is retained for the English edition, including entries without a Russian article.
enrich_short('en',english)
articles={}
for key,title in mapping.items():
 p=english.get(title,{});ll=next((x['title'] for x in p.get('langlinks',[]) if x['lang']=='ru'),None);r=russian.get(ll,{})
 langs={}
 for lang,page in [('ru',r),('en',p)]:
  text=page.get('extract','')
  if page.get('_truncated') and re.search(r'(?:\.{3}|…)\s*$',text):
   clipped=re.sub(r'(?:\.{3}|…)\s*$','',text);matches=list(re.finditer(r'[.!?](?=\s+[А-ЯA-Z«]|$)',clipped));text=clipped[:matches[-1].end()] if matches else clipped
  ps=page.get('_paragraphs') or paragraphs(text)
  if ps:langs[lang]=dict(title=page.get('title'),paragraphs=ps,url=page.get('fullurl') or f'https://{lang}.wikipedia.org/wiki/'+urllib.parse.quote(page.get('title','').replace(' ','_')),pageId=page.get('pageid'),revision=page.get('lastrevid'),qid=page.get('pageprops',{}).get('wikibase_item'),short=len(ps)<2)
 if langs:articles[key]=langs
out={'license':'CC-BY-SA-4.0','licenseUrl':'https://creativecommons.org/licenses/by-sa/4.0/','retrieved':'2026-10-24','articles':articles}
folder=root/'dist/data/accounts';folder.mkdir(exist_ok=True);buckets={};entries={}
for key,value in articles.items():
 bucket=__import__('hashlib').sha256(key.encode()).hexdigest()[:2];file=bucket+'.json';buckets.setdefault(file,{})[key]=value;entries[key]={'file':file,'titles':{lang:x['title'] for lang,x in value.items()},'paragraphs':{lang:len(x['paragraphs']) for lang,x in value.items()}}
for file,value in buckets.items():(folder/file).write_text(json.dumps({'encoding':'gzip-base64','data':base64.b64encode(gzip.compress(json.dumps(value,ensure_ascii=False,separators=(',',':')).encode(),mtime=0)).decode()},separators=(',',':'))+'\n')
out.pop('articles');out['directory']='accounts';out['entries']=entries;(folder/'index.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n');print('articles',len(articles),'ru',sum('ru'in x for x in articles.values()),'2ru',sum(len(x.get('ru',{}).get('paragraphs',[]))>=2 for x in articles.values()),flush=True)
