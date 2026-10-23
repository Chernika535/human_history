"""Extend authored atlas with audited affiliations and dated treaty participation.
Run after build-relations-atlas.py. Optional argv[1]: pinned Cliopatria properties.
No proximity edges or Cartesian products. Organization hubs denote membership,
not bilateral routes. Annual precision: start/end years include partial years.
"""
import json,pathlib,re,hashlib,sys
root=pathlib.Path(__file__).resolve().parents[1];path=root/'dist/data/relation-atlas.json';a=json.loads(path.read_text());base=json.loads((root/'dist/data/history.json').read_text());nodes={n['id']:n for n in base['cultures']+a['nodes']};translations={}
def T(ru,en):translations[ru]=en;return ru
def S(id,title,url):a['sources'][id]={'title':title,'url':url}
def N(id,ru,en,x,y,start,end,region,summary,summaryEn,source):
 if id not in nodes:
  n=dict(id=id,name=T(ru,en),coordinates=[x,y],start=start,end=end,region=region,summary=T(summary,summaryEn),sources=[source],kind='Узел исторической сети',relationOnly=True);a['nodes'].append(n);nodes[id]=n
 else:nodes[id]['start']=min(nodes[id]['start'],start);nodes[id]['end']=max(nodes[id]['end'],end)
def R(id,f,t,start,end,title,titleEn,goods,goodsEn,returns,returnsEn,impact,impactEn,source,kind='trade',direct='network',note=None):
 if any(r['id']==id for r in a['relations']):return
 assert start<=end and f!=t
 for n in [f,t]:assert nodes[n]['start']<=start<=end<=nodes[n]['end'],(id,n,start,end,nodes[n]['start'],nodes[n]['end'])
 note=note or T('Обзорный интервал свидетельств; линия показывает связь узлов сети, а не точный маршрут или ежегодный объём перевозок.','An overview interval of evidence; the line connects network nodes, not an exact itinerary or annual volume.')
 a['relations'].append(dict(id=id,**{'from':f,'to':t},start=start,end=end,title=T(title,titleEn),goods=T(goods,goodsEn),returns=T(returns,returnsEn),impact=T(impact,impactEn),sources=[source],type=kind,evidence=T('Датированные исторические сведения и исследования','Dated historical evidence and research'),directness=direct,periodNote=note,approximate=start<1500))
# Explicit MemberOf entries only. Geographic and chronological groupings such as
# Mahajanapadas, Anglo-Saxon England, Warring States are deliberately excluded.
if True:
 raw=json.loads(pathlib.Path(sys.argv[1]).read_text()) if len(sys.argv)>1 else [dict(Name=x['child'],MemberOf=x['parent'],Type='POLITY',FromYear=lo,ToYear=hi) for x in json.loads((root/'scripts/affiliation-intervals.json').read_text()) for lo,hi in x['periods']];catalog={n['name']:n for n in json.loads((root/'dist/data/cliopatria/catalog.json').read_text())};names=json.loads((root/'dist/area-names.js').read_text().split('export const namesRu=')[1].split(';\n')[0]);S('ra-clio-members','Cliopatria · датированные политические объединения','https://github.com/Seshat-Global-History-Databank/cliopatria/tree/5f433377139a6eeaeacbdc894b70f8805b72c8b5')
 parents={'(Holy Roman Empire)':('Священная Римская империя','Holy Roman Empire',8.57,50.11),'(Kingdom of France)':('Французская корона','French Crown',2.35,48.86),'(British Empire)':('Британская имперская система','British imperial system',-.12,51.5),'(Portuguese Empire)':('Португальская имперская система','Portuguese imperial system',-9.14,38.72),'(Carolingian Empire)':('Каролингская империя','Carolingian Empire',6.08,50.78),'(Habsburg Monarchy)':('Габсбургская монархия','Habsburg Monarchy',16.37,48.21),'(Kalmar Union)':('Кальмарская уния','Kalmar Union',16.36,56.66)}
 groups={}
 for p in raw:
  if p['Type']!='POLITY':continue
  for parent in p.get('MemberOf','').split(';'):
   if parent not in parents:continue
   child=p['Name']
   if child.strip('()')==parent.strip('()') or child not in catalog:continue
   # Skip umbrella records, dynasties without a distinct territorial node,
   # and imperial cores whose relation is constitutional rather than external.
   if child.startswith('House of ') or child in ['Kingdom of Great Britain','British Colonial Empire','Kingdom of Portugal','Holy Roman Empire Minor States']:continue
   groups.setdefault((parent,child),[]).append([p['FromYear'],p['ToYear']])
 snapshot=[]
 for (parent,child),periods in sorted(groups.items()):
  merged=[]
  for lo,hi in sorted(periods):
   if merged and lo<=merged[-1][1]+1:merged[-1][1]=max(hi,merged[-1][1])
   else:merged.append([lo,hi])
  ru,en,x,y=parents[parent];f='affiliation:'+hashlib.sha1(parent.encode()).hexdigest()[:12];t='affiliation:'+hashlib.sha1(child.encode()).hexdigest()[:12];name=names.get(child,child).strip('()');cx,cy=catalog[child]['anchor'];lo=min(p[0] for p in merged);hi=max(p[1] for p in merged)
  N(f,ru,en,x,y,lo,hi,'Европа',ru+' объединяет земли с разными институтами, правами и степенью самостоятельности.',en+' encompasses territories with different institutions, rights and degrees of autonomy.','ra-clio-members')
  N(t,name,child,cx,cy,lo,hi,'Африка' if cy<15 and -20<cx<50 else 'Азия' if cx>45 else 'Америка' if cx<-25 else 'Европа',name+': участник датированной политической связи с объединением «'+ru+'».',child+': a participant in a dated political relationship with '+en+'.','ra-clio-members')
  for i,(lo,hi) in enumerate(merged):
   R(f'{f}:{t}:{i}',t,f,lo,hi,name+' → '+ru,child+' → '+en,'Политическая принадлежность и отношения с центром','Political affiliation and relations with the centre','Местные учреждения и степень автономии различались','Local institutions and degrees of autonomy varied','Связь отражает политическую структуру периода; сама по себе она не устанавливает торговые потоки или единообразие управления.','The relationship represents a political structure, without implying trade flows or uniform government.','ra-clio-members','political','documented',T('Даты — интервалы исторической реконструкции Cliopatria. Точки условные; формы подчинения и полномочия менялись внутри периода.','Dates follow Cliopatria reconstruction intervals. Points are schematic; forms of dependence and powers changed within each period.'))
  snapshot.append({'parent':parent,'child':child,'periods':merged})
 (root/'scripts/affiliation-intervals.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=1)+'\n')
else:
 # Rebuild without the large original GeoJSON from the committed audit snapshot.
 snapshot_path=root/'scripts/affiliation-intervals.json'
 if snapshot_path.exists():
  raise SystemExit('Provide pinned source properties to rebuild political affiliations (see README).')
# Modern cooperation: hubs are institutions, never invented pairwise treaties.
S('ra-eu-members','Совет ЕС · даты вступления стран','https://www.consilium.europa.eu/en/policies/how-enlargement-works/timeline-accession-eu-member-states/')
S('ra-asean-members','АСЕАН · государства-участники','https://asean.org/member-states/')
S('ra-cptpp','МИД Австралии · даты действия CPTPP','https://www.dfat.gov.au/trade/agreements/in-force/cptpp/comprehensive-and-progressive-agreement-for-trans-pacific-partnership')
S('ra-rcep','МИД Австралии · участники RCEP','https://www.dfat.gov.au/trade/agreements/in-force/rcep')
# country key | RU | EN | capital lon lat | continent. Points represent capitals.
country_data='''be|Бельгия|Belgium|4.35|50.85|Европа
fr|Франция|France|2.35|48.86|Европа
de|ФРГ|Federal Republic of Germany|13.4|52.52|Европа
it|Италия|Italy|12.5|41.9|Европа
lu|Люксембург|Luxembourg|6.13|49.61|Европа
nl|Нидерланды|Netherlands|4.9|52.37|Европа
dk|Дания|Denmark|12.57|55.68|Европа
ie|Ирландия|Ireland|-6.26|53.35|Европа
uk|Великобритания|United Kingdom|-.12|51.5|Европа
gr|Греция|Greece|23.73|37.98|Европа
pt|Португалия|Portugal|-9.14|38.72|Европа
es|Испания|Spain|-3.7|40.42|Европа
at|Австрия|Austria|16.37|48.21|Европа
fi|Финляндия|Finland|24.94|60.17|Европа
se|Швеция|Sweden|18.07|59.33|Европа
cy|Кипр|Cyprus|33.38|35.19|Европа
cz|Чехия|Czechia|14.42|50.08|Европа
ee|Эстония|Estonia|24.75|59.44|Европа
hu|Венгрия|Hungary|19.04|47.5|Европа
lv|Латвия|Latvia|24.11|56.95|Европа
lt|Литва|Lithuania|25.28|54.69|Европа
mt|Мальта|Malta|14.51|35.9|Европа
pl|Польша|Poland|21.01|52.23|Европа
sk|Словакия|Slovakia|17.11|48.15|Европа
si|Словения|Slovenia|14.51|46.06|Европа
bg|Болгария|Bulgaria|23.32|42.7|Европа
ro|Румыния|Romania|26.1|44.43|Европа
hr|Хорватия|Croatia|15.98|45.81|Европа
us|США|United States|-77.04|38.91|Америка
ca|Канада|Canada|-75.7|45.42|Америка
is|Исландия|Iceland|-21.94|64.15|Европа
no|Норвегия|Norway|10.75|59.91|Европа
tr|Турция|Türkiye|32.86|39.93|Азия
al|Албания|Albania|19.82|41.33|Европа
me|Черногория|Montenegro|19.26|42.43|Европа
mk|Северная Македония|North Macedonia|21.43|42|Европа
id|Индонезия|Indonesia|106.85|-6.21|Азия
my|Малайзия|Malaysia|101.69|3.14|Азия
ph|Филиппины|Philippines|120.98|14.6|Азия
sg|Сингапур|Singapore|103.82|1.35|Азия
th|Таиланд|Thailand|100.5|13.76|Азия
bn|Бруней|Brunei|114.94|4.89|Азия
vn|Вьетнам|Vietnam|105.83|21.03|Азия
la|Лаос|Laos|102.63|17.97|Азия
mm|Мьянма|Myanmar|96.13|19.76|Азия
kh|Камбоджа|Cambodia|104.92|11.56|Азия
tl|Восточный Тимор|Timor-Leste|125.58|-8.56|Азия
au|Австралия|Australia|149.13|-35.28|Океания
nz|Новая Зеландия|New Zealand|174.78|-41.29|Океания
jp|Япония|Japan|139.69|35.69|Азия
mx|Мексика|Mexico|-99.13|19.43|Америка
pe|Перу|Peru|-77.04|-12.05|Америка
cl|Чили|Chile|-70.67|-33.45|Америка
cn|КНР|People’s Republic of China|116.4|39.9|Азия
kr|Республика Корея|Republic of Korea|126.98|37.57|Азия'''
countries={}
for row in country_data.splitlines():
 k,ru,en,x,y,reg=row.split('|');countries[k]=(ru,en,float(x),float(y),reg)
def member(org,k,start,end=2025,kind='diplomatic'):
 ru,en,x,y,reg=countries[k];source=org['source'];N('member:'+k,ru,en,x,y,start,end,reg,ru+' участвует в международных договорах и объединениях. Точка показывает столицу; откройте связь для условий участия.',en+' participates in international agreements and organizations. The point represents the capital; open a connection for its terms.',source)
 R(org['id']+':'+k,'member:'+k,org['id'],start,end,ru+' ↔ '+org['ru'],en+' ↔ '+org['en'],org['goods'],org['goodsEn'],org['returns'],org['returnsEn'],org['impact'],org['impactEn'],source,kind,'documented',T('Линия ведёт к условному узлу объединения и означает участие в нём. Это не отдельный двусторонний договор или физический путь перевозки. В год вступления или выхода показана часть года.','The line leads to a schematic organization hub and indicates participation, not a separate bilateral treaty or physical transport route. Accession and withdrawal years include partial years.'))
def org(id,ru,en,x,y,start,source,goods,goodsEn,returns,returnsEn,impact,impactEn):
 N(id,ru,en,x,y,start,2025,'Европа' if x<40 and y>35 else 'Азия',goods+' '+impact+' '+T('Условный узел объединения; положение точки не обозначает штаб-квартиру.','Schematic organization hub; the point does not identify its headquarters.'),goodsEn+' '+impactEn+' Schematic organization hub; the point does not identify its headquarters.',source)
 return dict(id=id,ru=ru,en=en,source=source,goods=goods,goodsEn=goodsEn,returns=returns,returnsEn=returnsEn,impact=impact,impactEn=impactEn)
eu=org('org:eec-eu','ЕЭС / Европейский союз','EEC / European Union',3.5,54,1958,'ra-eu-members','Общий рынок и согласование экономических правил','A common market and coordination of economic rules','Общие институты и договорные обязательства участников','Shared institutions and treaty obligations of members','ЕЭС действует с 1958 года; Европейский союз — с 1993 года. Политика и состав менялись.','The EEC began in 1958 and the EU in 1993; policies and membership evolved.')
for start,keys in [(1958,'be fr de it lu nl'),(1973,'dk ie uk'),(1981,'gr'),(1986,'pt es'),(1995,'at fi se'),(2004,'cy cz ee hu lv lt mt pl sk si'),(2007,'bg ro'),(2013,'hr')]:
 for k in keys.split():member(eu,k,start,2020 if k=='uk' else 2025,'political')
nato=org('org:nato','НАТО','NATO',6,54,1949,'ra-nato-members','Коллективная оборона по Североатлантическому договору','Collective defence under the North Atlantic Treaty','Консультации и обязательства по статьям договора','Consultation and obligations under the treaty articles','Гарантии коллективной обороны не означают участия всех стран в каждой военной операции.','Collective defence commitments do not imply that every member participates in every military operation.')
for start,keys in [(1949,'be ca dk fr is it lu nl no pt uk us'),(1952,'gr tr'),(1955,'de'),(1982,'es'),(1999,'cz hu pl'),(2004,'bg ee lv lt ro sk si'),(2009,'al hr'),(2017,'me'),(2020,'mk'),(2023,'fi'),(2024,'se')]:
 for k in keys.split():member(nato,k,start)
asean=org('org:asean','АСЕАН','ASEAN',110,0,1967,'ra-asean-members','Региональные переговоры, сотрудничество и экономическая интеграция','Regional dialogue, cooperation and economic integration','Согласование решений при сохранении суверенитета участников','Coordination of decisions while members retain sovereignty','Объединение не является единым государством; членство не означает автоматического согласия по каждому вопросу.','The association is not a single state; membership does not imply automatic agreement on every issue.')
for start,keys in [(1967,'id my ph sg th'),(1984,'bn'),(1995,'vn'),(1997,'la mm'),(1999,'kh'),(2025,'tl')]:
 for k in keys.split():member(asean,k,start,2025,'political')
cptpp=org('org:cptpp','Транстихоокеанское партнёрство · CPTPP','Trans-Pacific partnership · CPTPP',175,-34,2018,'ra-cptpp','Преференциальные тарифы и правила торговли товарами и услугами','Preferential tariffs and rules for trade in goods and services','Обязательства по происхождению товаров, доступу на рынки и инвестициям','Commitments on rules of origin, market access and investment','Торговое соглашение не создаёт единого государства или единой валюты; сроки снижения пошлин различаются.','The trade agreement creates neither a single state nor a currency; tariff reduction schedules vary.')
for start,keys in [(2018,'au ca jp mx nz sg'),(2019,'vn'),(2021,'pe'),(2022,'my'),(2023,'cl bn'),(2024,'uk')]:
 for k in keys.split():member(cptpp,k,start,kind='trade')
rcep=org('org:rcep','Всеобъемлющее региональное партнёрство · RCEP','Regional Comprehensive Economic Partnership · RCEP',108,-5,2022,'ra-rcep','Региональные правила происхождения и постепенное снижение торговых барьеров','Regional rules of origin and gradual reduction of trade barriers','Тарифные графики и обязательства участников по соглашению','Tariff schedules and commitments of participating parties','Вступление в силу различалось по странам; линия не означает беспошлинность всех товаров с первого дня.','Entry into force differed by country; the line does not mean all goods became duty free on day one.')
for start,keys in [(2022,'au bn kh cn jp la nz sg th vn kr my'),(2023,'id ph')]:
 for k in keys.split():member(rcep,k,start,kind='trade')
# Historical networks: distinct intermediate ports and oases, not modern states.
S('ra-zarafshan','ЮНЕСКО · коридор Зарафшан — Каракумы','https://whc.unesco.org/en/list/1675/')
S('ra-kilwa','ЮНЕСКО · Килва и Сонго-Мнара','https://whc.unesco.org/en/list/144/')
S('ra-zimbabwe','ЮНЕСКО · Большой Зимбабве','https://whc.unesco.org/en/list/364/')
S('ra-berenike','С. Сайдботэм · торговля римской Береникой','https://doi.org/10.1525/california/9780520244306.003.0012')
new_nodes=[('bukhara','Бухара','Bukhara',64.42,39.77,-200,1500,'Азия','Оазисный город связывал земледельческие районы Зарафшана с караванными путями.','An oasis city linking the farming districts of the Zarafshan with caravan routes.','ra-zarafshan'),('merv','Мерв','Merv',62.19,37.66,-200,1500,'Азия','Оазис у Каракумов был узлом караванного движения между Ираном и Центральной Азией.','An oasis near the Karakum and a caravan hub between Iran and Central Asia.','ra-zarafshan'),('penjikent','Пенджикент','Penjikent',67.61,39.49,500,750,'Азия','Согдийский город в долине Зарафшана с ремеслом, торговлей и настенной живописью.','A Sogdian city in the Zarafshan valley with crafts, trade and wall painting.','ra-zarafshan'),('kilwa-port','Килва-Кисивани','Kilwa Kisiwani',39.52,-8.96,1200,1500,'Африка','Суахилийский порт участвовал в обмене золотом и привозной керамикой Индийского океана.','A Swahili port participating in Indian Ocean exchange in gold and imported ceramics.','ra-kilwa'),('zimbabwe-trade','Большой Зимбабве','Great Zimbabwe',30.93,-20.27,1100,1450,'Африка','Каменный город обществ шона связывал внутренние районы с восточноафриканскими торговыми сетями.','A stone-built city of Shona societies linking the interior to East African exchange networks.','ra-zimbabwe'),('sofala','Софала','Sofala',34.72,-20.18,1200,1500,'Африка','Прибрежный торговый район на выходе путей из золотоносных внутренних земель.','A coastal trading district connected to routes from the gold-bearing interior.','ra-kilwa'),('berenike','Береника','Berenike',35.48,23.91,1,300,'Африка','Красноморский порт римского Египта; здесь найдены индийский перец и другие привозные продукты.','A Red Sea port of Roman Egypt with finds of Indian pepper and other imported products.','ra-berenike'),('muziris','Музирис · Малабарский берег','Muziris · Malabar coast',76.2,10.18,1,300,'Азия','Портовый район юго-западной Индии участвовал в обмене перцем и другими товарами через Индийский океан.','A port district of southwestern India participating in Indian Ocean exchange in pepper and other goods.','ra-berenike'),('blue-ridge-mica','Аппалачи · слюда','Appalachians · mica',-82,36,-100,400,'Америка','Район происхождения слюды, обнаруженной в комплексах Хоупвелл в долине Огайо.','Source region of mica found in Hopewell assemblages in the Ohio valley.','ra-hopewell-materials')]
for args in new_nodes:N(*args)
# title is explicit about indirect networks; commodities pertain to the network.
for f,t,lo,hi,src,goods,enGoods,returns,enReturns in [
 ('bukhara','merv',-200,1500,'ra-zarafshan','Караванные товары между оазисами','Caravan goods moving between oases','Постоялые дворы, рынки и встречные поставки','Caravanserais, markets and return consignments'),
 ('bukhara','sogdiana',200,750,'ra-zarafshan','Ремесленные изделия и транзитные товары','Craft products and transit goods','Рыночный обмен в долине Зарафшана','Market exchange in the Zarafshan valley'),
 ('penjikent','sogdiana',500,750,'ra-zarafshan','Ремесленные изделия согдийских городов','Craft goods of Sogdian cities','Торговые и семейные сети купцов','Merchant trading and family networks'),
 ('merv','baghdad',800,1200,'ra-ocean','Товары и купцы караванных путей','Goods and merchants of caravan routes','Иракские рынки и посредничество','Iraqi markets and intermediation'),
 ('kilwa-port','sofala',1200,1500,'ra-kilwa','Золото и товары восточноафриканских берегов','Gold and goods of the East African coast','Керамика, ткани и другие морские товары','Ceramics, textiles and other maritime goods'),
 ('zimbabwe-trade','sofala',1200,1450,'ra-zimbabwe','Золото и товары внутренних районов','Gold and products of the interior','Привозные бусы, керамика и посредничество','Imported beads, ceramics and intermediation'),
 ('kilwa-port','aden',1200,1500,'ra-kilwa','Золото и другие товары суахилийского побережья','Gold and other goods of the Swahili coast','Аравийские товары и дальнейшее морское посредничество','Arabian goods and further maritime intermediation'),
 ('kilwa-port','india-ports',1200,1500,'ra-kilwa','Восточноафриканские товары в морских сетях','East African goods in maritime networks','Ткани и ремесленные изделия индийских портов','Textiles and craft goods of Indian ports'),
 ('berenike','muziris',1,300,'ra-berenike','Перец и другие индийские продукты','Pepper and other Indian products','Средиземноморские товары и денежные расчёты','Mediterranean goods and monetary payments'),
 ('blue-ridge-mica','hopewell',-100,400,'ra-hopewell-materials','Слюда из Аппалачей в комплексах Огайо','Appalachian mica in Ohio assemblages','Передача и поездки не равны доказанному рынку','Transfer and travel do not establish a market')]:
 name=nodes[f]['name']+' ↔ '+nodes[t]['name'];enName=translations.get(nodes[f]['name'],json.loads((root/'dist/locales/en.json').read_text()).get(nodes[f]['name'],nodes[f]['name']))+' ↔ '+translations.get(nodes[t]['name'],json.loads((root/'dist/locales/en.json').read_text()).get(nodes[t]['name'],nodes[t]['name']))
 R('expanded:'+f+':'+t,f,t,lo,hi,name,enName,goods,enGoods,returns,enReturns,'Узлы соединяла сеть посредников; линия не означает единственного прямого рейса.','A network of intermediaries connected these nodes; the line does not imply a single direct voyage.',src,'material' if f=='blue-ridge-mica' else 'trade')
# AU membership is not backdated to OAU, and suspension of participation is not
# confused with withdrawal. Morocco joins only in 2017; South Sudan in 2011.
S('ra-au','Африканский союз · государства-участники','https://amo.au.int/en/member-states')
africa='''dz|Алжир|Algeria|3.05|36.75
an|Ангола|Angola|13.23|-8.84
bj|Бенин|Benin|2.63|6.5
bw|Ботсвана|Botswana|25.91|-24.65
bf|Буркина-Фасо|Burkina Faso|-1.52|12.37
bi|Бурунди|Burundi|29.92|-3.43
cv|Кабо-Верде|Cabo Verde|-23.51|14.92
cm|Камерун|Cameroon|11.52|3.87
cf|ЦАР|Central African Republic|18.56|4.37
td|Чад|Chad|15.05|12.13
km|Коморы|Comoros|43.26|-11.7
cg|Республика Конго|Republic of the Congo|15.28|-4.27
ci|Кот-д’Ивуар|Côte d’Ivoire|-5.28|6.82
cd|ДР Конго|Democratic Republic of the Congo|15.27|-4.33
dj|Джибути|Djibouti|43.15|11.57
eg|Египет|Egypt|31.24|30.04
gq|Экваториальная Гвинея|Equatorial Guinea|8.78|3.75
er|Эритрея|Eritrea|38.93|15.32
et|Эфиопия|Ethiopia|38.76|9.03
ga|Габон|Gabon|9.45|.39
gm|Гамбия|The Gambia|-16.58|13.45
gh|Гана|Ghana|-.19|5.56
gn|Гвинея|Guinea|-13.71|9.64
gw|Гвинея-Бисау|Guinea-Bissau|-15.6|11.86
ke|Кения|Kenya|36.82|-1.29
ls|Лесото|Lesotho|27.48|-29.31
lr|Либерия|Liberia|-10.8|6.32
ly|Ливия|Libya|13.19|32.89
mg|Мадагаскар|Madagascar|47.51|-18.88
mw|Малави|Malawi|33.79|-13.96
ml|Мали|Mali|-8|12.64
mr|Мавритания|Mauritania|-15.96|18.07
mu|Маврикий|Mauritius|57.5|-20.16
ma|Марокко|Morocco|-6.84|34.02
mz|Мозамбик|Mozambique|32.58|-25.97
na|Намибия|Namibia|17.08|-22.56
ne|Нигер|Niger|2.11|13.51
ng|Нигерия|Nigeria|7.49|9.06
rw|Руанда|Rwanda|30.06|-1.94
eh|САДР · член Африканского союза|SADR · African Union member|-8.14|27.67
st|Сан-Томе и Принсипи|São Tomé and Príncipe|6.73|.34
sn|Сенегал|Senegal|-17.45|14.69
sc|Сейшелы|Seychelles|55.45|-4.62
sl|Сьерра-Леоне|Sierra Leone|-13.23|8.48
so|Сомали|Somalia|45.34|2.05
za|ЮАР|South Africa|28.23|-25.75
ss|Южный Судан|South Sudan|31.6|4.85
sd|Судан|Sudan|32.56|15.5
sz|Эсватини|Eswatini|31.14|-26.31
tg|Того|Togo|1.22|6.13
tn|Тунис|Tunisia|10.18|36.81
ug|Уганда|Uganda|32.58|.35
tz|Танзания|Tanzania|35.74|-6.16
zm|Замбия|Zambia|28.28|-15.42
zw|Зимбабве|Zimbabwe|31.05|-17.83'''
au=org('org:au','Африканский союз','African Union',35,6,2002,'ra-au','Континентальные институты, переговоры о мире и региональной интеграции','Continental institutions, peace negotiations and regional integration','Участие государств в органах и программах союза','State participation in the institutions and programmes of the union','Членство сохраняется при некоторых приостановках участия. Союз действует с 2002 года и не является единым государством.','Membership can continue during suspensions of participation. The union began in 2002 and is not a single state.')
nodes['org:au']['region']='Африка'
for row in africa.splitlines():
 k,ru,en,x,y=row.split('|');countries[k]=(ru,en,float(x),float(y),'Африка');member(au,k,2017 if k=='ma' else 2011 if k=='ss' else 2002,2025,'political')
# Additional maritime networks in the early modern and industrial periods.
S('ra-portuguese','ЮНЕСКО · морские пути и португальские порты','https://www.unesco.org/en/silk-roads/about-silk-roads')
S('ra-voc','Национальный архив Нидерландов · Ост-Индская компания','https://www.nationaalarchief.nl/en/explore/the-world-of-the-dutch-east-india-company')
S('ra-eic','Королевские музеи Гринвича · Ост-Индская компания','https://www.rmg.co.uk/national-maritime-museum/attractions/traders-east-india-company-asia')
maritime=[('lisbon-trade','Лиссабон · океанские сети','Lisbon · ocean networks',-9.14,38.72,1500,1850,'Европа','ra-portuguese'),('goa-trade','Гоа · портовые сети','Goa · port networks',73.83,15.5,1510,1850,'Азия','ra-portuguese'),('moz-island','Остров Мозамбик · морской узел','Island of Mozambique · maritime hub',40.73,-15.03,1500,1850,'Африка','ra-portuguese'),('hormuz-trade','Ормуз · торговый пролив','Hormuz · trading strait',56.45,27.06,1500,1622,'Азия','ra-portuguese'),('cape-voc','Капская станция · снабжение судов','Cape station · ship provisioning',18.42,-33.92,1652,1795,'Африка','ra-voc'),('ceylon-voc','Цейлон · нидерландские порты','Ceylon · Dutch ports',79.86,6.93,1658,1796,'Азия','ra-voc'),('london-eic','Лондон · Ост-Индская компания','London · East India Company',-.12,51.5,1600,1833,'Европа','ra-eic'),('bengal-eic','Бенгалия · текстильные и колониальные сети','Bengal · textile and colonial networks',88.36,22.57,1650,1833,'Азия','ra-eic'),('bombay-eic','Бомбей · морские сети','Bombay · maritime networks',72.88,19.08,1668,1833,'Азия','ra-eic')]
for id,ru,en,x,y,lo,hi,reg,src in maritime:
 N(id,ru,en,x,y,lo,hi,reg,ru+': порт, торговые посредники, склады и снабжение океанских судов. Состав власти и условия обмена менялись.',en+': a port, trading intermediaries, warehouses and provisioning for ocean-going ships. Political control and terms of exchange changed.',src)
sea_links=[('lisbon-trade','goa-trade',1510,1750,'ra-portuguese','Пряности, ткани и товары азиатских рынков','Spices, textiles and Asian market goods','Металлы, расчёты и океанское посредничество','Metals, payments and oceanic intermediation'),('moz-island','goa-trade',1510,1750,'ra-portuguese','Восточноафриканские товары и снабжение рейсов','East African goods and supplies for voyages','Индийские ткани и транзитные товары','Indian textiles and transit goods'),('lisbon-trade','moz-island',1500,1750,'ra-portuguese','Товары, экипажи и снабжение на пути в Индию','Goods, crews and supplies on the India route','Портовые услуги и африканские товары','Port services and African goods'),('goa-trade','malacca',1511,1641,'ra-portuguese','Индийские ткани и транзитные товары','Indian textiles and transit goods','Пряности и товары проливных рынков','Spices and goods from straits markets'),('goa-trade','hormuz-trade',1515,1622,'ra-portuguese','Товары индийских портов','Goods of Indian ports','Персидские и аравийские товары через пролив','Persian and Arabian goods through the strait'),('netherlands-network','cape-voc',1652,1795,'ra-voc','Суда, оборудование и люди компании','Company ships, equipment and people','Снабжение водой и продовольствием на океанском пути','Water and food supplies on the ocean route'),('cape-voc','batavia',1652,1795,'ra-voc','Снабжение и промежуточная остановка судов','Supplies and an intermediate stop for ships','Рейсы с азиатскими товарами в Европу','Voyages carrying Asian goods to Europe'),('batavia','ceylon-voc',1658,1796,'ra-voc','Межпортовые поставки и ресурсы компании','Inter-port shipments and company resources','Коричные и другие цейлонские товары','Cinnamon and other Ceylonese goods'),('ceylon-voc','netherlands-network',1658,1796,'ra-voc','Корица и другие товары Цейлона','Cinnamon and other goods of Ceylon','Европейские расчёты и морское снабжение','European payments and maritime supplies'),('london-eic','bengal-eic',1650,1833,'ra-eic','Бенгальские ткани, шёлк и другие товары','Bengali textiles, silk and other goods','Серебро, расчёты и позднее колониальные доходы','Silver, payments and later colonial revenues'),('london-eic','bombay-eic',1668,1833,'ra-eic','Индийские товары и морские услуги','Indian goods and maritime services','Капитал, суда и контроль торговых операций','Capital, ships and control of trading operations'),('london-eic','guangzhou',1700,1833,'ra-eic','Чай, шёлк и фарфор из Китая','Tea, silk and porcelain from China','Серебро и товары через азиатских посредников','Silver and goods through Asian intermediaries'),('bombay-eic','guangzhou',1750,1833,'ra-eic','Хлопок и опиум в торговых сетях','Cotton and opium in trading networks','Платежи и доходы, связанные с китайской торговлей','Payments and revenues linked to China trade')]
for f,t,lo,hi,src,g,ge,ret,rete in sea_links:
 ru=nodes[f]['name']+' ↔ '+nodes[t]['name'];en=translations.get(nodes[f]['name'],json.loads((root/'dist/locales/en.json').read_text()).get(nodes[f]['name'],nodes[f]['name']))+' ↔ '+translations.get(nodes[t]['name'],json.loads((root/'dist/locales/en.json').read_text()).get(nodes[t]['name'],nodes[t]['name']))
 R('maritime:'+f+':'+t,f,t,lo,hi,ru,en,g,ge,ret,rete,'Морская торговля сочеталась с монополиями, военной силой и неравными условиями для местных обществ.','Maritime commerce combined monopolies, military power and unequal conditions for local societies.',src)

# Validation across both atlas layers.
for r in a['relations']:
 for id in [r['from'],r['to']]:assert nodes[id]['start']<=r['start']<=r['end']<=nodes[id]['end'],r['id']
assert len({r['id'] for r in a['relations']})==len(a['relations'])
path.write_text(json.dumps(a,ensure_ascii=False,indent=1)+'\n')
# New text is authored bilingually; never overwrite reviewed legacy translations.
en_path=root/'dist/locales/en.json';en=json.loads(en_path.read_text());en.update(translations)
for k,v in [('Политические объединения','Political affiliations'),('Структура отношений','Structure of the relationship'),('Условия участия','Terms of participation'),('Светлая тема','Light theme'),('Тёмная тема','Dark theme')]:en[k]=v
for src in a['sources'].values():
 if src['title'] not in en or src['title'] in [a['sources'][k]['title'] for k in ['ra-clio-members','ra-eu-members','ra-asean-members','ra-cptpp','ra-rcep','ra-zarafshan','ra-kilwa','ra-zimbabwe','ra-berenike','ra-au','ra-portuguese','ra-voc','ra-eic']]:en[src['title']]={'ra-clio-members':'Cliopatria · dated political affiliations','ra-eu-members':'Council of the EU · accession dates','ra-asean-members':'ASEAN · member states','ra-cptpp':'Australian DFAT · CPTPP entry into force','ra-rcep':'Australian DFAT · RCEP parties','ra-zarafshan':'UNESCO · Zarafshan–Karakum corridor','ra-kilwa':'UNESCO · Kilwa and Songo Mnara','ra-zimbabwe':'UNESCO · Great Zimbabwe','ra-berenike':'S. Sidebotham · trade in Roman Berenike','ra-au':'African Union · member states','ra-portuguese':'UNESCO · maritime routes and Portuguese ports','ra-voc':'National Archives of the Netherlands · Dutch East India Company','ra-eic':'Royal Museums Greenwich · East India Company'}.get(next((k for k,v in a['sources'].items() if v is src),''),'Historical bibliography')
en_path.write_text(json.dumps(en,ensure_ascii=False,indent=1)+'\n')
print(len(a['relations'])+len(base['relations']),'relations;',len(a['nodes']),'network nodes')
