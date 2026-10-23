import {contextAt} from './regional-history.js?v=0.11.1';
import {landscapeFeatures} from './landscapes.js?v=0.11.1';
const source=(title,url)=>({title,url});
export const beliefSources={
 ritual:source('Погребения и символические практики · Смитсоновский институт','https://humanorigins.si.edu/evidence/behavior/burial'),
 mesopotamian:source('Божества Месопотамии · Метрополитен-музей','https://www.metmuseum.org/essays/mesopotamian-deities'),
 classical:source('Греческие боги и религиозные практики · Метрополитен-музей','https://www.metmuseum.org/essays/greek-gods-and-religious-practices'),
 asia:source('Древние религии Азии · Музей азиатских цивилизаций','https://www.nhb.gov.sg/acm/galleries/faith-and-belief/ancient-religions'),
 roads:source('Распространение религий по Шёлковым путям · ЮНЕСКО','https://www.unesco.org/en/silk-roads/about-silk-roads'),
 shinto:source('Синто · Метрополитен-музей','https://www.metmuseum.org/essays/shinto'),
 african:source('Предки и духи земли в Центральной Африке · Метрополитен-музей','https://www.metmuseum.org/fr/met-publications/eternal-ancestors-the-art-of-the-central-african-reliquary'),
 american:source('Разнообразие коренных культур · Национальный музей американских индейцев','https://americanindian.si.edu/nk360/about/essential-understandings'),
 australian:source('Земля, церемонии и тотемические связи · Австралийский музей','https://australian.museum/about/history/exhibitions/body-art/paint-up-aboriginal-dance/'),
 totem:source('Тотем и ответственность за морскую страну · народ воппабурра','https://australian.museum/learn/cultures/first-nations-collections/woppaburra-people-of-the-keppel-islands/'),
 newguinea:source('Растения, ритуал и духовные существа Новой Гвинеи · Австралийский музей','https://australian.museum/visit/audio-tours/200-treasures/tour_stop/10/')
};
beliefSources.pacific=source('Верования маори · Те Ара','https://teara.govt.nz/en/traditional-maori-religion-nga-karakia-a-te-maori');
beliefSources.siberian=source('Шаманские традиции Сибири · Российский этнографический музей / Музей Иллинойса','https://museum.state.il.us/exhibits/changing/journey/shamanism.html');
const extra={
 'local-african':{name:'Местные африканские традиции',color:'#f09bc0',origin:'Множество самостоятельных историй; общего основателя и единой даты нет',summary:'Почитание предков, духов земли и священных мест принимает разные формы у разных народов. Это не единая африканская религия. Местные практики продолжаются и во взаимодействии с исламом и христианством.',sources:['african'],facets:['animism','ancestor']},
 'local-american':{name:'Коренные традиции Северной Америки',color:'#86cfa8',origin:'Разные традиции народов; конкретные системы известны не для всех древних периодов',summary:'Церемонии, отношения с землёй и нечеловеческими существами, предки и священные повествования различаются между народами. Единой религии коренных американцев нет; позднюю этнографию нельзя механически переносить на древние поселения.',sources:['american'],facets:['animism','ancestor']},
 'local-amazonian':{name:'Коренные традиции Амазонии',color:'#62ccb1',origin:'Самостоятельные локальные истории; точные даты возникновения не установлены',summary:'У разных народов существуют собственные представления о людях, животных, духах и преобразованиях живых существ. Шаманские и обрядовые практики неодинаковы. Современные описания не доказывают неизменности верований на протяжении тысячелетий.',sources:['american'],facets:['animism']},
 'local-australian':{name:'Коренные традиции Австралии',color:'#efb56d',origin:'Множество традиций, связанных с конкретными странами и общинами',summary:'Земля, предки, церемонии и тотемические связи имеют большое значение во многих коренных обществах. Например, у воппабурра тотемическая связь с горбатым китом предполагает ответственность за него и морскую среду. Этот пример не описывает всех жителей Австралии или её древнейшие эпохи.',sources:['australian','totem'],facets:['animism','totemism','ancestor']},
 'local-siberian':{name:'Локальные традиции Сибири и Арктики',color:'#9ccce9',origin:'Разные коренные общества, без единой даты основания',summary:'Отношения с животными и духами, обряды специалистов и представления о предках известны в разных формах. Понятие «шаманизм» объединяет исследовательские сравнения, а не единую церковь или одинаковую религию всех северных народов.',sources:['siberian'],facets:['animism','ancestor']},
 'local-pacific':{name:'Океанийские традиции предков и священных мест',color:'#80cdd4',origin:'Формируются в разных обществах после заселения конкретных островов',summary:'Генеалогия, предки, божества и священные места связывают сообщества с островами и морем. У маори, гавайцев и других народов собственные истории. Общий цвет показывает семейство региональных обзоров, а не одинаковые пантеоны.',sources:['pacific'],facets:['polytheism','ancestor']},
 'local-newguinea':{name:'Локальные традиции Новой Гвинеи',color:'#a8d27d',origin:'Множество местных традиций; общей даты возникновения нет',summary:'Ритуалы, представления о духовных существах и отношения с землёй различаются между обществами острова. Предметы, связанные с производством пищи, могут иметь церемониальное значение. Это не единый паностровной культ.',sources:['newguinea'],facets:['animism','ancestor']},
 'european-local':{name:'Местные политеистические традиции Европы',color:'#c4a1ed',origin:'Разные культы бронзового и железного веков; единой даты основания нет',summary:'Погребения, святилища и посвящения показывают разнообразную обрядовую жизнь. Кельтские, германские, славянские и балтийские традиции различались. Слово «язычество» не означает единой религии; поздние имена богов нельзя автоматически приписывать более ранним памятникам.',sources:['ritual','classical'],facets:['polytheism','ancestor']},
 'chinese-local':{name:'Китайские культы предков и местных божеств',color:'#e6bb6d',origin:'Надписи Шан II тысячелетия до н. э. и последующие самостоятельные традиции',summary:'Предки, гадания, местные божества и государственные обряды имеют разную историю. Позднее они взаимодействуют с конфуцианскими, даосскими и буддийскими традициями; участие в одних обрядах не исключает другие.',sources:['roads'],facets:['polytheism','ancestor']},
 shinto:{name:'Синто и культы ками',color:'#f29a91',origin:'Постепенное формирование в Японии; единого основателя нет',summary:'Ками связывают со священными местами, силами природы и предками. Святилища и обряды менялись со временем. После распространения буддизма обе традиции длительно взаимодействовали; жёсткое разделение на две взаимоисключающие религии искажает эту историю.',sources:['shinto'],facets:['polytheism','ancestor']},
 jain:{name:'Джайнизм',color:'#b7da91',origin:'Южная Азия; традиция тиртханкаров, историческое оформление в I тысячелетии до н. э.',summary:'Освобождение от перерождений, ненасилие и аскетическая дисциплина занимают центральное место. Джайнские общины сосуществуют с другими религиями Южной Азии; их присутствие не означает регионального большинства.',sources:['asia'],facets:[]}
};
export const beliefFacets={animism:'Анимистические представления',totemism:'Тотемические связи',polytheism:'Многобожие',ancestor:'Почитание предков'};
export function beliefCatalog(history){const out={...history.religions,...extra};out.andean={...out.andean,summary:'Разные общества Анд создавали собственные священные центры, обряды и представления о мире. Культы инков относятся к позднему доиспанскому времени и не описывают все более ранние андские культуры.'};out.mesoamerican={...out.mesoamerican,summary:'Многочисленные традиции Мезоамерики связывают божеств, предков, земледелие и календарные циклы. Майя, сапотеки и позднейшие мешика имеют разные пантеоны и политические истории; единой неизменной религии региона нет.'};delete out.na;for(const id of ['egyptian','mesopotamian','classical'])out[id]={...out[id],facets:['polytheism']};out.ancestral={...out.ancestral,facets:['ancestor']};for(const [id,p] of Object.entries(out))out[id]={...p,id,sources:(p.sources||[]).map(s=>beliefSources[s]||history.sources[s]).filter(Boolean)};return out;}
const localFor={europe:'european-local','north-africa':'local-african','west-africa':'local-african','central-africa':'local-african','east-africa':'local-african','southern-africa':'local-african',madagascar:'local-african','north-america':'local-american',caribbean:'local-american',mesoamerica:'mesoamerican',andes:'andean',amazon:'local-amazonian','southern-america':'local-american',australia:'local-australian','new-guinea':'local-newguinea',pacific:'local-pacific',nz:'local-pacific',hawaii:'local-pacific',siberia:'local-siberian',arctic:'local-siberian',greenland:'local-siberian',steppe:'local-siberian'};
// Dates below are display intervals for regional evidence, not founding dates.
function traditions(id,year){let a=[];const add=(key,from,to=2025)=>{if(year>=from&&year<=to)a.push(key);};
 if(localFor[id])add(localFor[id],['europe','mesoamerica','andes'].includes(id)?-1500:0);
 if(id==='nile'){add('egyptian',-4000,500);add('christianity',300);add('islam',650);}
 if(id==='west-asia'){add('ritual',-10000);add('christianity',100);add('islam',650);}
 if(id==='south-asia'){add('hindu',-1500);add('buddhism',-500);add('jain',-500);add('islam',1200);}
 if(id==='east-asia'){add('chinese-local',-1600);add('confucian',-400);add('daoism',100);add('buddhism',100);}
 if(id==='southeast-asia'){add('ritual',-3000);add('hindu',100);add('buddhism',100);add('islam',1200);}
 if(id==='europe')add('christianity',300);
 if(id==='iceland'){add('european-local',800,1100);add('christianity',1000);}
 if(id==='north-africa'){add('ritual',-3000);add('christianity',200);add('islam',700);}
 if(id==='west-africa')add('islam',900);
 if(id==='east-africa'){add('christianity',400);add('islam',800);}
 if(id==='steppe'){add('buddhism',100);add('islam',900);}
 if(['north-america','mesoamerica','caribbean','andes','amazon','southern-america'].includes(id))add('christianity',1500);
 if(['central-africa','southern-africa','madagascar','new-guinea','australia','pacific','nz','hawaii','siberia','arctic','greenland'].includes(id))add('christianity',1800);
 return a.length?a:['unknown'];}
// Localized overlays avoid moving a region's traditions to all of its neighbours.
const overlays=[
 {id:'japan',name:'Японские острова',box:[129,30,146,46],from:300,traditions:y=>y>=600?['shinto','buddhism']:['shinto']},
 {id:'mesopotamia',name:'Месопотамия',box:[39,29,49,37],from:-3500,to:300,traditions:()=>['mesopotamian']},
 {id:'iran',name:'Иранское нагорье',box:[46,25,62,39],from:-500,traditions:y=>y<650?['zoroastrian']:['zoroastrian','islam']},
 {id:'italy',name:'Италийский полуостров',box:[8,37,18,46],from:-700,to:399,traditions:()=>['classical']},
 {id:'greece',name:'Эгеида и юг Балкан',box:[19,34,29,42],from:-800,to:299,traditions:()=>['classical']},
 {id:'baltic',name:'Балтийские земли',box:[20,53,30,60],from:-500,to:1399,traditions:y=>y<1100?['european-local']:['european-local','christianity']},
 {id:'scandinavia',name:'Скандинавия',box:[5,55,29,70],from:-500,to:1299,traditions:y=>y<900?['european-local']:['european-local','christianity']},
 {id:'tibet',name:'Тибет',box:[78,28,98,36],from:700,traditions:()=>['buddhism','ritual']},
 {id:'levante',name:'Левант',box:[34,29,37,34],from:-500,traditions:y=>y<100?['judaism','ritual']:y<650?['judaism','christianity']:['judaism','christianity','islam']}
];
const polygon=([w,s,e,n])=>({type:'Polygon',coordinates:[[[w,s],[w,n],[e,n],[e,s],[w,s]]]});
export function worldReligionFeatures(regions,year,catalog,filter='all'){
 const items=landscapeFeatures(regions,year).filter(f=>!['antarctica','svalbard'].includes(f.properties.regionId)).map(f=>{const c=contextAt(f.properties.anchor,year);return {...f,id:'belief:'+f.properties.regionId,properties:{...f.properties,summary:c.beliefs,keys:traditions(f.properties.regionId,year)}};});
 for(const o of overlays)if(year>=o.from&&year<=(o.to??2025))items.push({type:'Feature',id:'belief:'+o.id,geometry:polygon(o.box),properties:{name:o.name,title:o.name,anchor:[(o.box[0]+o.box[2])/2,(o.box[1]+o.box[3])/2],keys:o.traditions(year),summary:null,background:false}});
 return items.map(f=>{const keys=f.properties.keys.filter(id=>catalog[id]&&(filter==='all'||id===filter||(catalog[id].facets?.includes(filter)&&(!['animism','totemism'].includes(filter)||year>=1500))));if(!keys.length)return null;const ts=keys.map(id=>catalog[id]);return {...f,properties:{...f.properties,mode:'religions',snapshot:year,basis:ts.length>1?'mixed':'regional',precision:0,religion:keys.length===1?keys[0]:'multiple',traditions:ts,color:ts[0].color,colors:ts.map(t=>t.color),name:f.properties.name,title:f.properties.title,summary:f.properties.summary||ts.map(t=>t.summary).join(' '),note:'Региональный обзор присутствия традиций, а не перепись верующих. Полосы показывают сосуществование, их ширина не передаёт численность. Исторические даты появления общин различаются внутри ареала.'}};}).filter(Boolean);
}
