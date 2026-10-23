import json,pathlib,re
root=pathlib.Path(__file__).resolve().parents[1];path=root/'dist/locales/en.json';values=json.loads(path.read_text());overrides={}
for line in '''
ХРОНОС|CHRONOS
Хронос — Земля. Человек. Время.|Chronos — Earth. People. Time.
Хронос — атлас человечества|Chronos — Atlas of Humanity
АТЛАС ЧЕЛОВЕЧЕСТВА|ATLAS OF HUMANITY
Земля. Человек.|Earth. People.
Время.|Time.
Атлас|Atlas
Путешествия|Journeys
Об атласе|About the atlas
Поиск|Search
Культуры|Cultures
Религии|Religions
Связи|Connections
Истории|Stories
Легенда|Legend
Люди и места|People and places
Язык сайта|Site language
Язык названий на карте|Map label language
Названия на карте|Map labels
Русские названия|Russian names
Исходные названия|Original names
Поиск культур|Find a culture
Поиск и список культур|Search and culture list
Культура, место, народ…|Culture, place, people…
НАЙТИ СВОЮ ИСТОРИЮ|FIND YOUR HISTORY
Страны и культуры|States and cultures
Культуры и общества|Cultures and societies
Религии и верования|Religions and beliefs
Торговля и отношения|Trade and relationships
Все части света|All regions
Все связи|All connections
Все добавленные традиции|All available traditions
Сбросить|Reset
Сбросить фильтры|Reset filters
Ввести год|Enter a year
Перейти|Go
Год|Year
Эра|Era
Выбрать год|Choose a year
Выбрать эпоху|Choose a period
КОГДА ВЫ ХОТИТЕ ОКАЗАТЬСЯ?|WHEN WOULD YOU LIKE TO GO?
ВЫБЕРИТЕ ТОЧКУ ОТПРАВЛЕНИЯ|CHOOSE YOUR STARTING POINT
В ВЫБРАННОМ ГОДУ|IN THE SELECTED YEAR
РЕЗУЛЬТАТЫ ВО ВСЕХ ЭПОХАХ|RESULTS ACROSS ALL PERIODS
ГОСУДАРСТВА ВО ВСЕХ ЭПОХАХ|STATES ACROSS ALL PERIODS
ТЕРРИТОРИИ НА КАРТЕ|TERRITORIES ON THE MAP
РЕЛИГИОЗНЫЕ АРЕАЛЫ|RELIGIOUS AREAS
КАК ЧИТАТЬ КАРТУ|READING THE MAP
История этого места|History of this place
История места|Place history
История выбранного места|History of the selected place
ЗЕМЛИ И НАРОДЫ|LANDS AND PEOPLES
КУЛЬТУРЫ И ОБЩЕСТВА|CULTURES AND SOCIETIES
РЕЛИГИИ И ВЕРОВАНИЯ|RELIGIONS AND BELIEFS
ИСТОРИЯ МЕСТА|PLACE HISTORY
Региональный обзор|Regional overview
Региональный контекст|Regional context
Историческое общество|Historical society
Религиозная традиция|Religious tradition
Устройство государства|Government and society
Как было устроено общество|How society worked
Люди и образ жизни|People and daily life
Люди и повседневность|People and daily life
Чем жили и что производили|Livelihoods and production
Хозяйство и обмен|Economy and exchange
ХОЗЯЙСТВО|ECONOMY
УСТРОЙСТВО ОБЩЕСТВА|SOCIAL ORGANIZATION
ВЕРОВАНИЯ|BELIEFS
Власть|Government
Во что верили|Beliefs
Верования и ритуалы|Beliefs and rituals
Возникновение и особенности|Origins and characteristics
Формирование|Formation
События к выбранному году|Events up to the selected year
Источники и оговорки|Sources and qualifications
Источники и точность|Sources and uncertainty
Источники|Sources
Покрытие карты|Map coverage
Что ещё неизвестно|What remains unknown
История людей и государств.|A history of people and states.
Атрибуция и обработка геоданных ↗|Attribution and data processing ↗
В проверенной базе пока не указан|Not recorded in the verified dataset
Верования не восстановлены.|The beliefs have not been reconstructed.
Верования неизвестны.|The beliefs are unknown.
Точное устройство управления не установлено|The precise organization of government is unknown
Устройство ранних общин восстановлено неполно|The organization of early communities is only partly reconstructed
Культуры и общества этого региона|Cultures and societies in this region
Сравнить с современниками|Compare contemporaries
А что в это время в Америке?|What was happening in the Americas?
Открыть историю|Explore the story
Открыть другую сторону|Explore the other side
Во что верили|What people believed
Что отправляли|Outgoing goods
Встречный поток и контроль|Return flows and control
Выгоды и издержки|Benefits and costs
Торговля и обмен|Trade and exchange
Торговля и обмен →|Trade and exchange →
ТОРГОВЛЯ И ОБМЕН|TRADE AND EXCHANGE
Колониальная зависимость|Colonial rule
Колониальная зависимость ⇢|Colonial rule ⇢
КОЛОНИАЛЬНАЯ ЗАВИСИМОСТЬ|COLONIAL RULE
Тип отношений|Relationship type
Первая культура|First society
Вторая культура|Second society
Охотники и собиратели|Hunters and gatherers
Первые земледельцы|Early farmers
Первые города|The first cities
Бронзовый век|Bronze Age
Железный век|Iron Age
Античность|Antiquity
Раннее Средневековье|Early Middle Ages
Средневековье|Middle Ages
Раннее Новое время|Early Modern Period
Индустриальная эпоха|Industrial Age
XX–XXI века|20th–21st centuries
01 / БРОНЗОВЫЙ ВЕК|01 / BRONZE AGE
02 / СРЕДНЕВЕКОВЬЕ|02 / MIDDLE AGES
03 / РАННЕЕ НОВОЕ ВРЕМЯ|03 / EARLY MODERN PERIOD
Америка|Americas
Африка|Africa
Европа|Europe
Азия|Asia
Океания|Oceania
Срез не загрузился · повторить|Map could not load · retry
Загружаем территории…|Loading territories…
Загружаем территориальный срез…|Loading the historical map…
Проявляем очертания мира…|Revealing the world…
Границы|Borders
Ареалы|Areas
: срез|: map for
Нет ареалов для выбранного года / фильтра|No mapped areas for this year or filter
Площадь территории: ≈|Territory area: ≈
км²|km²
· общий профиль|· general profile
общий профиль|general profile
в выбранном году|in the selected year
перейти к|go to
· перейти|· go to
мест|places
место|place
н. э.|CE
до н. э.|BCE
ок.|c.
с. ш.|N
ю. ш.|S
в. д.|E
з. д.|W
Поделиться|Share
Ссылка на этот момент скопирована.|Link to this moment copied.
Вернуть управление|Show controls
Вернуть исходный вид|Reset view
Исходный вид|Reset view
Включить режим погружения|Enter immersion mode
Выключить режим погружения|Leave immersion mode
Режим погружения|Immersion mode
Приблизить|Zoom in
Отдалить|Zoom out
Приблизить планету|Zoom in on the globe
Отдалить планету|Zoom out from the globe
Включить плавное вращение|Start slow rotation
Остановить плавное вращение|Stop rotation
Плавное вращение|Slow rotation
Закрыть справку|Close details
Закрыть поиск|Close search
Закрыть легенду|Close legend
Закрыть окно|Close dialog
Закрыть ввод года|Close year input
Как путешествовать|How to explore
Как управлять атласом|Atlas controls
Показать города и памятники|Show cities and sites
Религиозный слой|Religious layer
Методология и источники ↗|Methods and sources ↗
Исследовательский атлас|Research atlas
100 тысяч лет истории|100,000 years of history
У каждой точки — своя история.|Every place has a history.
Один палец — вращать · Два — приближать|One finger to rotate · Two to zoom
Потяните Землю · Колесо — ближе|Drag to rotate · Scroll to zoom
В регионе известны поселения|Settlement is documented in the region
Заселение не подтверждено|Settlement is not confirmed
Постоянное заселение не подтверждено|Permanent settlement is not confirmed
Местное заселение не установлено|Local settlement is not established
Раннее заселение не подтверждено|Early settlement is not confirmed
Местная датировка неизвестна|Local dates are unknown
Ранняя хронология обсуждается|The early chronology is debated
Раннее заселение; местная датировка неизвестна|Early settlement; local dates unknown
Период раннего заселения|Early settlement period
Заселение зависит от острова|Settlement dates vary by island
Заселение неоднородно|Settlement was uneven
Экспедиционное присутствие|Expeditionary presence
Экспедиции и промысловое присутствие|Expeditions and resource exploitation
Штриховка: смешанное / институты|Hatching: mixed traditions / institutions
Пунктир: приблизительная граница|Dashed line: approximate border
Цвет сохраняется для одной области|An area retains its color
Заливка: территории и культурные ареалы|Fill: territories and cultural areas
Запустить путешествие во времени|Start the timeline
Остановить путешествие|Pause the timeline
Правитель в|Ruler in
ОНЛАЙН|ONLINE
ПУТЕШЕСТВИЕ СКВОЗЬ ТЫСЯЧЕЛЕТИЯ|A JOURNEY THROUGH MILLENNIA
СЛЕДЫ ОДНОЙ ЭПОХИ|TRACES OF AN AGE
МИР, СОЕДИНЁННЫЙ СВЯЗЯМИ|A CONNECTED WORLD
КАК ЧЕЛОВЕК ОБЪЯСНЯЛ МИР|HOW PEOPLE EXPLAINED THE WORLD
НЕБОЛЬШОЙ КОМПАС ДЛЯ БОЛЬШОГО МИРА|A SMALL COMPASS FOR A VAST WORLD
ТРИ ВОПРОСА К ИСТОРИИ ЧЕЛОВЕКА|THREE QUESTIONS ABOUT HUMAN HISTORY
ОДНОВРЕМЕННО НА ЗЕМЛЕ|AT THE SAME TIME ON EARTH
ПРОСТРАНСТВО И ВРЕМЯ|SPACE AND TIME
Управление временем|Timeline controls
'''.strip().splitlines():
 k,v=line.split('|',1);overrides[k]=v
names={
'foragers-africa':'African hunter-gatherers','foragers-eurasia':'Eurasian hunter-gatherers','kakadu':'Kakadu cultural landscape','jomon':'Jōmon · northern Japan','wheat':'Early farming in Southwest Asia','gobekli':'Göbekli Tepe','catal':'Çatalhöyük','kuk':'Kuk · early agriculture','uruk':'Uruk and the first cities','liangzhu':'Liangzhu','sumer':'Sumerian cities','caral':'Caral-Supe','egypt-old':'Egypt · Old Kingdom','indus':'Indus Valley Civilization','shang':'Shang','zhou':'Zhou · bronze traditions','persia':'Achaemenid Empire','buddhist-india':'Buddhist centers in South Asia','han-west':'Western Han','rome':'Roman Empire · Principate','han-east':'Eastern Han','sasan':'Sasanian Empire','jewish-diaspora':'Jewish communities in Late Antiquity','byz-early':'Eastern Roman Empire','early-islam':'The early Muslim community','abbasid':'Abbasid Caliphate','cahokia':'Cahokia','angkor':'Angkor','kilwa':'Kilwa Kisiwani','zimbabwe':'Great Zimbabwe','novgorod':'Novgorod Republic','lubeck':'Lübeck and the Hanseatic network','mongol':'Mongol Empire','byz-late':'Byzantium · Palaiologan period','ottoman':'Ottoman Empire','aztec':'Mexica · Tenochtitlan','ming':'China · Ming dynasty','inca':'Inca Empire','spain':'Spanish colonial monarchy','goree':'Gorée · the Atlantic slave trade','mughal':'Mughal Empire','potosi':'Potosí · Spanish colonial rule','eic-india':'East India Company in India','britain':'Britain · colonial connections','china-opium':'Qing China · the opium trade','un-world':'United Nations · the postwar world','decolon':'Decolonization · Africa and Asia','celts':'Celtic cultural areas'}
for c in json.loads((root/'dist/data/history.json').read_text())['cultures']:overrides[c['name']]=names[c['id']]
overrides.update({'Восточное христианство · земли Руси':'Eastern Christianity · lands of Rus’','Гавайские острова':'Hawaiian Islands','Шпицберген':'Svalbard','У-ди':'Emperor Wu','СОЛНЕЧНЫЙ КУЛЬТ':'SOLAR CULT','Древнеегипетские культы':'Ancient Egyptian religious traditions','Реконструкция ограничена':'Limited reconstruction','Местные ритуальные традиции':'Local ritual traditions','Межгосударственная организация':'Intergovernmental organization','Система управления':'System of government'})
for k,v in values.items():
 if 'двор' in k.lower():v=v.replace('Courtyard','Court').replace('courtyard','court')
 if 'хозяйств' in k.lower():v=re.sub(r'\bHousing\b','Economy',v);v=re.sub(r'\bhousing\b','economy',v)
 if re.search(r'карт[аыуе]\b',k.lower()):v=re.sub(r'\bCard\b','Map',v);v=re.sub(r'\bcard\b','map',v)
 if 'верован' in k.lower() and 'восстанов' in k.lower():v=v.replace('restored','reconstructed')
 if 'Горе' in k:v=v.replace('Woe','Gorée').replace('Gore Island','Gorée Island')
 v=re.sub(r'\bMaori\b','Māori',v);v=v.replace('Early New Time','Early Modern Period').replace('Early NEW TIME','EARLY MODERN PERIOD')
 if '↗' in k:v=v.replace('⁇','↗')
 if '↔' in k:v=v.replace('⁇','↔')
 values[k]=v
overrides.update({'Перемещение материалов':'Movement of materials','ФРГ · послевоенное восстановление':'West Germany · postwar reconstruction','Каниш · Кюльтепе':'Kanesh · Kültepe','Дильмун · Бахрейн':'Dilmun · Bahrain','Маган · Оманский полуостров':'Magan · Oman Peninsula','Материал и находки':'Material and finds','Что можно заключить':'What the evidence supports','Что известно о передаче':'What is known about transfer'})
values.update(overrides);path.write_text(json.dumps(values,ensure_ascii=False,indent=1)+'\n');(root/'dist/locales/en-overrides.json').write_text(json.dumps(overrides,ensure_ascii=False,indent=1)+'\n');print('reviewed overrides',len(overrides),'total',len(values))
