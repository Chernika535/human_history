import fs from 'node:fs';
const names=new Set(fs.readdirSync('dist/data/territories').filter(p=>p.endsWith('.geojson')).flatMap(p=>JSON.parse(fs.readFileSync('dist/data/territories/'+p)).features.map(f=>f.properties.name)));
const explicit=Object.fromEntries(`
Eastern Roman Empire|Восточная Римская империя
Western Roman Empire|Западная Римская империя
Byzantine Empire|Византийская империя
Roman Empire|Римская империя
Roman Republic|Римская республика
Rome|Рим
Holy Roman Empire|Священная Римская империя
Russian Empire|Российская империя
Tsardom of Muscovy|Русское царство
USSR|СССР
Austrian Empire|Австрийская империя
Austria Hungary|Австро-Венгрия
Austro-Hungarian Empire|Австро-Венгрия
Prussia|Пруссия
Poland-Lithuania|Польско-Литовское государство
Polish–Lithuanian Commonwealth|Речь Посполитая
United States|США
United States of America|Соединённые Штаты Америки
United Kingdom|Великобритания
United Kingdom of Great Britain and Ireland|Соединённое Королевство Великобритании и Ирландии
West Germany|ФРГ
East Germany|ГДР
Yugoslavia|Югославия
Czechoslovakia|Чехословакия
Persia|Персия
Persian Empire|Персидская держава
Achaemenid Empire|Ахеменидская держава
Sasanian Empire|Сасанидская держава
Sasanian dependencies|Зависимые земли Сасанидов
Parthia|Парфия
Parthian Empire|Парфянское царство
Media|Мидия
Elam|Элам
Babylonia|Вавилония
Assyria|Ассирия
Urartu|Урарту
Ur|Ур
Sumer|Шумер
Akkad|Аккад
Ubaid|Убейдская культура
Oxus|Бактрийско-Маргианский комплекс
Bactria|Бактрия
Sogdiana|Согдиана
Khwarezm|Хорезм
Khwarazmian Empire|Держава Хорезмшахов
Seleucid Kingdom|Государство Селевкидов
Ptolemaic Kingdom|Птолемеевский Египет
Macedonia|Македония
Alexander's Empire|Держава Александра Македонского
Greek city-states|Греческие полисы
city-states|Города-государства
Phoenicia|Финикия
Carthage|Карфаген
Nabatean Kingdom|Набатейское царство
Hittites|Хетты
Hittite Empire|Хеттское царство
Phrygians|Фригийцы
Lydia|Лидия
Lycia|Ликия
Thrace|Фракия
Odrysian Kingdom|Одрисское царство
Pergamon|Пергамское царство
Pontus|Понтийское царство
Arameans|Арамеи
state societies and Aramaean kingdoms|Государства и арамейские царства
Arabs|Арабские общества
Arabia|Аравия
Arabian pastoral nomads|Кочевые скотоводы Аравии
Saba|Сабейское царство
Hadramaut|Хадрамаут
Himyar|Химьяр
Qataban|Катабан
Abyssinia|Абиссиния
Axum|Аксум
Meroe|Мероитское царство
Kush|Куш
Nobatia|Нобатия
Makkura|Макурия
Alwa|Алва
Blemmyes|Блеммии
Numidia|Нумидия
Mauretania|Мавретания
Guanches|Гуанчи
Khoisan|Койсанские народы
Bantu|Бантуязычные общества
Bantu peoples|Бантуязычные народы
Mossi States|Государства моси
Hausa States|Государства хауса
Oyo|Ойо
Asante|Ашанти
Kanem-Bornu|Канем-Борну
Songhai|Сонгай
Merina Kingdom|Королевство Мерина
Luba|Луба
Lunda|Лунда
Kongo|Королевство Конго
Mwenemutapa|Мономотапа
Great Zimbabwe|Большой Зимбабве
Sokoto Caliphate|Халифат Сокото
Zulu|Зулусы
Zululand|Зулуленд
Almohad Caliphate|Халифат Альмохадов
Almoravid dynasty|Держава Альморавидов
Fatimid Caliphate|Фатимидский халифат
Abbasid Caliphate|Аббасидский халифат
Umayyad Caliphate|Омейядский халифат
Rashidun Caliphate|Праведный халифат
Seljuk Empire|Сельджукская держава
Seljuk Caliphate|Сельджукская держава
Ottoman Empire|Османская империя
Ottoman Sultanate|Османский султанат
Safavid Empire|Сефевидская держава
Samanid Empire|Саманидская держава
Saffarids|Саффариды
Mamluks|Мамлюкский султанат
Ayyubids|Айюбиды
Mongol Empire|Монгольская империя
Mongols|Монголы
Golden Horde|Золотая Орда
White Horde|Белая Орда
Nogai Horde|Ногайская Орда
Crimean Khanate|Крымское ханство
Astrakhan Khanate|Астраханское ханство
Kazan Khanate|Казанское ханство
Quazaq Khanate|Казахское ханство
Timurid Empire|Держава Тимуридов
Timurid Emirates|Тимуридские эмираты
central Asian khanates|Среднеазиатские ханства
Western Gokturk Khaganate|Западно-Тюркский каганат
Gokturk Khaganate|Тюркский каганат
Turcik tribes|Тюркские племена
Turks|Тюрки
Oghuz|Огузы
Oghuz Turks|Огузские тюрки
Uyghurs|Уйгуры
Avars|Авары
Alans|Аланы
Huns|Гунны
Pechenegs|Печенеги
Khazars|Хазары
Scythians|Скифы
Sarmates|Сарматы
Proto-Scythian culture|Протоскифские культуры
Saka Kingdom|Сакское царство
Xiongnu|Хунну
Southern Xiongnu|Южные хунну
Xia|Ся
Shang|Шан
Zhou states|Государства эпохи Чжоу
Zhoa|Чжао
Qin|Цинь
Han|Хань
Western Han|Западная Хань
Eastern Han|Восточная Хань
Three Kingdoms|Троецарствие
Sixteen Kingdoms|Шестнадцать царств
Northern Liang|Северная Лян
Toba Wei|Северная Вэй
Sui Empire|Империя Суй
Tang Empire|Империя Тан
Song Empire|Империя Сун
Qing Empire|Империя Цин
Manchu Empire|Цинская империя
Ming|Империя Мин
Post-Ming Warlords|Региональные режимы после падения Мин
Wu|У
Yue|Юэ
Nan-Yue|Наньюэ
Nan Chao|Наньчжао
Nan-Zhao|Наньчжао
Xixia|Западное Ся
Tibet|Тибет
Tibetan Empire|Тибетская империя
Tufan Empire|Тибетская империя
Tibetans|Тибетцы
Tibeto-Burmanese|Тибето-бирманские народы
Korea|Корея
Koguryo|Когурё
Paekche|Пэкче
Silla|Силла
Balhae|Бохай
Parhae|Бохай
Yamato|Ямато
Tokugawa shogunate|Сёгунат Токугава
Shogun Japan (Kamakura)|Камакурский сёгунат
Ainu|Айны
Ainus|Айны
Jōmon|Дзёмон
Yayoi|Яёй
Indus valley civilization|Индская цивилизация
Maurya Empire|Империя Маурьев
Gupta Empire|Империя Гуптов
Mughal Empire|Империя Великих Моголов
British Raj|Британская Индия
Sultanate of Delhi|Делийский султанат
Hindu kingdoms|Индийские царства
minor Hindu kingdoms|Малые индийские царства
minor Hindu and Buddhist states|Малые индуистские и буддийские государства
minor Hindu and Buddhist kingdoms|Малые индуистские и буддийские царства
minor states|Малые государства
minor states under Indian influence|Малые государства индийской культурной сферы
Dravidians|Дравидоязычные общества
Vedic Aryans|Общества ведийской традиции
Palas|Держава Палов
Chola|Чола
Pallava|Паллавы
Pallava state|Государство Паллавов
Pallavas|Паллавы
Pandyas|Пандья
Pandya state|Государство Пандья
Satavahanihara|Держава Сатаваханов
Vakataka|Вакатаки
Vijayanagara|Виджаянагара
Rashtrakuta|Раштракуты
Rashtrakuta state|Государство Раштракутов
Pratiharas|Пратихары
Western Chalukyas|Западные Чалукьи
Western Gangas|Западные Ганги
Rajput kingdoms|Раджпутские царства
Rajput Clans and Small States|Раджпутские кланы и малые государства
Rajputana|Раджпутана
Rajputs|Раджпуты
Punjab|Пенджаб
Sind|Синд
Sindh|Синд
Orissa|Орисса
Simhala|Сингальское царство
Sinhalese kingdom|Сингальское царство
Sinhalese kingdoms|Сингальские царства
Ceylon|Цейлон
Sikhs|Сикхские общества
Khmer Empire|Кхмерская империя
Champa|Тямпа
Đại Việt|Дайвьет
Siam|Сиам
Ayutthaya|Аюттхая
Sukhothai|Сукхотай
Rattanakosin Kingdom|Королевство Раттанакосин
Bagan|Паган
Pagan|Паган
Arakan|Аракан
Burma|Бирма
Mon States|Государства монов
Mon state|Государство монов
Shan states|Шанские княжества
Srivijaya Empire|Шривиджая
Majapahit|Маджапахит
Aceh|Ачех
Malaya|Малайя
Minang|Минангкабау
Papuans|Папуасы
Papuan|Папуасские общества
Papuan neolithic farmers|Ранние земледельцы Новой Гвинеи
Austronesians|Австронезийские народы
Polynesians|Полинезийцы
Māori|Маори
Maori|Маори
Tuʻi Tonga Empire|Морская держава Тонга
Rapa Nui|Рапануи
Celts|Кельтские общества островов
Celtic kingdoms|Кельтские королевства
Celtiberians|Кельтиберы
Hallstatt culture|Гальштатская культура
La Tène culture|Латенская культура
Boii|Бойи
Galatians|Галаты
Galatia|Галатия
Picts|Пикты
Scots|Скотты
Welsh|Валлийцы
Gauls|Галлы
Gaul|Галлия
Germans|Германские народы
Germanic tribes|Германские племена
Franks|Франки
Francia|Франкское государство
West Francia|Западно-Франкское королевство
East Francia|Восточно-Франкское королевство
Anglo-Saxons|Англосаксы
Saxons|Саксы
Visigoths|Вестготы
Visigothic Kingdom|Вестготское королевство
Ostrogoths|Остготы
Vandals|Вандалы
Suebi|Свевы
Lombards|Лангобарды
Norsemen|Скандинавы
Northmen|Скандинавы
Northumbria|Нортумбрия
Wessex|Уэссекс
Neustria|Нейстрия
Burgundy|Бургундия
Britany|Бретань
Armorica|Арморика
Angevin Empire|Анжуйская держава
Slavs|Славяне
Slavic tribes|Славянские племена
Slavonic tribes|Славянские племена
Proto-Slavs|Протославянские общества
Balts|Балты
Baltic tribes|Балтийские племена
Curonians|Курши
Prussians|Пруссы
Finno-Ugric taiga hunter-gatherers|Финно-угорские сообщества тайги
Saami|Саамы
Sami|Саамы
Samis|Саамы
Sámi|Саамы
Suomi|Суоми
Veps|Вепсы
Mordvinians|Мордва
Permians|Пермские народы
Nenets|Ненцы
Nganasan|Нганасаны
Yukagir|Юкагиры
Tungus|Тунгусские народы
Tungusic Tribes|Тунгусские общества
Siberians|Народы Сибири
Kyivan Rus|Киевская Русь
Kievan Rus|Киевская Русь
Rus' Khaganate|Русский каганат
Other Rus Principalities|Другие русские княжества
Principality of Kyiv|Киевское княжество
Principality of Novgorod|Новгородская земля
Novgorod|Новгород
Pskov|Псков
Ryazan|Рязанское княжество
Principality of Galicia-Volhynia|Галицко-Волынское княжество
Principality of Polotsk|Полоцкое княжество
Principality of Vladimir-Suzdal|Владимиро-Суздальское княжество
Principality of Wallachia|Валахия
Volga Bulgars|Волжская Булгария
Papal States|Папская область
Teutonic Knights|Тевтонский орден
Swiss Confederation|Швейцарский союз
Denmark-Norway|Датско-норвежская уния
Sweden–Norway|Шведско-норвежская уния
Venice|Венецианская республика
Venetia|Венеция
Tuscany|Тоскана
Savoy|Савойя
Sardinia|Сардиния
Sardinia-Piedmont|Сардинское королевство
Sicily|Сицилия
Naples|Неаполитанское королевство
Navarre|Наварра
Aragón|Арагон
Castile|Кастилия
Scotland|Шотландия
Ireland|Ирландия
England|Англия
Wales|Уэльс
Aztec Empire|Ацтекская держава
Inca Empire|Инкская держава
Toltec Empire|Толтекская держава
Zapotec Empire|Сапотекские государства
Maya|Майя
Maya city-states|Города-государства майя
Maya chiefdoms and states|Вождества и государства майя
Olmec|Ольмекские общества
Zapotec|Сапотеки
Teotihuacan|Теотиуакан
Monte Albán|Монте-Альбан
Norte Chico|Норте-Чико
Chavin|Чавин
Moche|Моче
Nazca|Наска
Wari|Уари
Tiahuanaco Empire|Тиуанако
Chorrera|Чоррера
Valdivia|Вальдивия
Paracas|Паракас
Anasazi|Древние пуэбло
Pueblos|Пуэбло
Adena|Адена
Adena Culture|Культура Адена
Hopewell|Хоупвелл
Dorset|Дорсетская культура
Thule|Культура Туле
Paleo-Inuit|Палеоинуитские общества
Arawaks|Араваки
Taino|Таино
Caribs|Карибы
Innu|Инну
Inuit|Инуиты
Athabascan|Атабаскские народы
Athabaskan|Атабаскские народы
Apache|Апачи
Navajo|Навахо
Navaho|Навахо
Shuar|Шуар
Mapuche|Мапуче
Aymara|Аймара
Aymara kingdoms|Государства аймара
Quechua|Кечуа
Muisca|Муиски
Guarani|Гуарани
Tupis|Тупи
Australian aboriginal hunter-gatherers|Коренные общества Австралии
Aboriginal Tasmanians|Коренные народы Тасмании
Aboriginal tribes|Коренные сообщества
Tasmanian hunter-gatherers|Охотники и собиратели Тасмании
Pampas cultures|Культуры Пампы
Patagonian shellfish and marine mammal hunters|Прибрежные охотники и собиратели Патагонии
Subarctic forest hunter-gatherers|Охотники и собиратели субарктических лесов
Amazon hunter-gatherers|Лесные сообщества Амазонии
Savanna hunter-gatherers|Охотники и собиратели саванн
Andean hunter-gatherers|Охотники и собиратели Анд
Caribbean hunter-gatherers|Ранние сообщества Карибских островов
Plateau fichers and hunter gatherers|Рыболовы и охотники плато
West African cereal farmers|Земледельческие общества Западной Африки
Plain bison hunters|Охотничьи общества Великих равнин
Desert hunter-gatherers|Охотники и собиратели пустынь
North American Pacific foraging, hunting and fishing peoples|Прибрежные общества североамериканского Тихоокеанья
Arctic marine mammal hunters|Арктические морские охотники
Paleo-Siberian hunter-gatherers|Палеосибирские сообщества
Eastern North American hunter-gatherers|Охотники и собиратели востока Северной Америки
Saharan pastoral nomads|Скотоводческие общества Сахары
Saharan Nomadic Tribes|Кочевые общества Сахары
Shellfish gatherers|Прибрежные собиратели
Manioc farmers|Общества земледельцев, выращивающих маниок
Neolithic Farmers|Неолитические земледельцы
Neanderthal|Неандертальские сообщества
Alluvial Lowland Mesolithic Hunter-Foragers|Мезолитические сообщества речных низменностей
Steppe Mesolithic Hunter-Foragers|Мезолитические сообщества степей
Archaic Amerindian hunter-gatherers|Ранние охотничьи общества Америки
Andean states and chiefdoms|Государства и вождества Анд
Proto-Altaic pastoralists|Ранние скотоводческие общества Алтая
Austro-Asiatic rice cultures|Рисоводческие культуры Юго-Восточной Азии
Afanasevo|Афанасьевская культура
Andronovo|Андроновская общность
Yamnaya culture|Ямная культура
Sintashta|Синташтинская культура
Urnfield cultures|Культуры полей погребальных урн
Únětice|Унетицкая культура
Milograd culture|Милоградская культура
Narva|Нарвская культура
Brushed Pottery culture|Культура штрихованной керамики
Plain-Pottery culture|Культуры гладкостенной керамики
Okhotsk culture|Охотская культура
Pomeranian culture |Поморская культура
Sambian-Nothangian culture|Самбийско-натангийская культура
Western Masurian culture|Западномазурская культура
Eastern Masurian culture|Восточномазурская культура
Bell-shaped burials culture|Культура подклёшевых погребений
Stentinello culture|Культура Стентинелло
Poverty point culture|Культура Поверти-Пойнт
Swift Creek Culture|Культура Свифт-Крик
Caloosahatchee culture|Культура Калусахатчи
Glades Culture|Культура Глейдс
Point Peninsula|Культура Пойнт-Пенинсула
Portuguese Guinea|Португальская Гвинея
Portuguese East Africa|Португальская Восточная Африка
Portuguese Brazil|Португальская Бразилия
Spanish Guinea|Испанская Гвинея
Spanish Morocco|Испанское Марокко
Spanish Sahara|Испанская Сахара
Western Sahara|Западная Сахара
French Guiana|Французская Гвиана
Dutch East Indies|Нидерландская Ост-Индия
Netherlands Indies|Нидерландская Ост-Индия
Netherlands Antilles|Нидерландские Антильские острова
New France|Новая Франция
New Amsterdam|Новый Амстердам
New Hebrides|Новые Гебриды
New South Wales|Новый Южный Уэльс
Northern Rhodesia|Северная Родезия
Southern Rhodesia|Южная Родезия
Rhodesia|Родезия
Nyasaland|Ньясаленд
Cape Colony|Капская колония
Union of South Africa|Южно-Африканский Союз
Transvaal|Трансвааль
Orange Free State|Оранжевое Свободное Государство
Anglo-Egyptian Sudan|Англо-Египетский Судан
Cochin China|Кохинхина
Annam|Аннам
Tonkin|Тонкин
Trucial Oman|Договорный Оман
Muscat|Маскат
Muscat and Oman|Маскат и Оман
Zaire|Заир
Gambia, The|Гамбия
Ivory Coast|Кот-д’Ивуар
Hong Kong|Гонконг
Hainan|Хайнань
Republic of Turkey|Турецкая Республика
Turkish Cypriot-administered area|Территория под управлением турок-киприотов
Viceroyalty of New Spain|Вице-королевство Новая Испания
Viceroyalty of New Granada|Вице-королевство Новая Гранада
Viceroyalty of Peru|Вице-королевство Перу
Viceroyalty of the Río de la Plata|Вице-королевство Рио-де-ла-Плата
Viceroyalty of Brazil|Вице-королевство Бразилия
United Provinces of the Río de la Plata|Объединённые провинции Рио-де-ла-Платы
Tanzania, United Republic of|Танзания
Saint Barthelemy|Сен-Бартелеми
Saint Martin|Сен-Мартен
United States Virgin Islands|Американские Виргинские острова
Virgin Islands (UK)|Британские Виргинские острова
Virgin Islands (Danemark)|Датские Виргинские острова
Wallis and Futuna Islands|Уоллис и Футуна
Turks and Caicos Islands|Теркс и Кайкос
Saar Protectorate|Протекторат Саар
Rupert's Land|Земля Руперта
Islamic city-states|Мусульманские города-государства
Africa|Африка
Antarctica|Антарктида
? |Местные сообщества
`.trim().split('\n').map(s=>s.split('|')));
const en=new Intl.DisplayNames('en',{type:'region'}),ru=new Intl.DisplayNames('ru',{type:'region'});
for(let a=65;a<=90;a++)for(let b=65;b<=90;b++){const code=String.fromCharCode(a,b),name=en.of(code);if(name!==code&&!explicit[name])explicit[name]=ru.of(code);}
Object.assign(explicit,Object.fromEntries(`
Aghlabid Emirate|Аглабидский эмират
Ayyubid Sultanate|Султанат Айюбидов
Bokhara Khanate|Бухарское ханство
Bukara Khanate|Бухарское ханство
Bosporan Kingdom|Боспорское царство
Bosporian Kingdom|Боспорское царство
Bulgar Khanate|Болгарское ханство
Chagatai Khanate|Чагатайский улус
Carolingian Empire|Империя Каролингов
Carthaginian Empire|Карфагенская держава
Cuman Khanates|Половецкие объединения
Chola Empire|Держава Чола
Chalukya Empire|Держава Чалукьев
Chimú Empire|Государство Чимор
Dendi Kingdom|Денди
Emirate of Córdoba|Кордобский эмират
Caliphate of Córdoba|Кордобский халифат
Emirate of Sicily|Сицилийский эмират
Emirate of Tiflis|Тбилисский эмират
Empire of Alexander|Держава Александра Македонского
Empire of Ghana|Государство Гана
Empire of Japan|Японская империя
Frankish Kingdom|Франкское королевство
Fulani Empire|Держава фульбе
Georgian Kingdom|Грузинское царство
Ghaznavid Emirate|Держава Газневидов
Grand Duchy of Moscow|Великое княжество Московское
Great Khanate|Великий ханский улус
Han Empire|Империя Хань
Himyarite Kingdom|Химьяритское царство
Hindu kingdoms and republics|Индийские царства и республики
Hindu states|Индийские государства
Huari Empire|Держава Уари
Hunnic Empire|Держава гуннов
Hurrian Kingdoms|Хурритские царства
Hunters-gatherers|Охотники и собиратели
Imperial Japan (Fujiwara)|Япония эпохи Фудзивара
Khitan Empire|Империя Ляо
Kingdom of France|Французское королевство
Kingdom of Italy|Итальянское королевство
Kingdom of Hungary|Венгерское королевство
Kingdom of Kush|Кушитское царство
Kingdom of Nepal|Непальское королевство
Kingdom of Sicily|Сицилийское королевство
Kingdom of Sardinia|Сардинское королевство
Kingdom of Jerusalem|Иерусалимское королевство
Kingdom of Makuria|Макурия
Liao Empire|Империя Ляо
Majapahit Empire|Маджапахит
Mauryan Empire|Империя Маурьев
Mauryan Kingdom|Государство Маурьев
Gupta Kingdom|Держава Гуптов
Kingdom of Kongo|Королевство Конго
Ghurid Empire|Держава Гуридов
Nabatean kingdom|Набатейское царство
Oirat Confederation|Ойратская конфедерация
Rashtrakuta Empire|Держава Раштракутов
Soomra Emirate|Эмират Сумра
Sultanate of Zanzibar|Занзибарский султанат
Sultinate of Zanzibar|Занзибарский султанат
Suren Kingdom|Царство Суренов
Wadai Empire|Держава Вадаи
Wassoulou Empire|Держава Васулу
Zhangzhung Kingdom|Шангшунг
British American colonies|Британские колонии Северной Америки
British East Africa|Британская Восточная Африка
British East India Company|Британская Ост-Индская компания
British Guiana|Британская Гвиана
British Protectorate|Британский протекторат
British Somaliland|Британское Сомали
French Cameroons|Французский Камерун
French Equatorial Africa|Французская Экваториальная Африка
French Indo-China|Французский Индокитай
French Indochina|Французский Индокитай
French Somaliland|Французское Сомали
French West Africa|Французская Западная Африка
German Empire|Германская империя
German South-West Africa|Германская Юго-Западная Африка
German E. Africa (Tanganyika)|Германская Восточная Африка · Танганьика
Dutch Brazil|Нидерландская Бразилия
Dutch Formosa|Нидерландская Формоза
Dutch Guiana|Нидерландская Гвиана
Dutch Guinea|Нидерландская Гвинея
Dutch Republic|Республика Соединённых провинций
Dutch settlements|Нидерландские поселения
Ceylon (Dutch)|Нидерландский Цейлон
Germany (Soviet)|Германия · советская зона оккупации
Germany (USA)|Германия · американская зона оккупации
Czech Republic|Чехия
Bosnia and Herzegovina|Босния и Герцеговина
Antigua and Barbuda|Антигуа и Барбуда
Saint Kitts and Nevis|Сент-Китс и Невис
Saint Vincent and the Grenadines|Сент-Винсент и Гренадины
Republic of Kraków|Краковская республика
Helvetic Republic|Гельветическая республика
Batavian Republic|Батавская республика
Rome (Constantinus)|Рим · Константин
Rome (Diocletianus)|Рим · Диоклетиан
Rome (Galerius)|Рим · Галерий
Rome (Maximian)|Рим · Максимиан
Duchy of Swabia|Герцогство Швабия
Duchy of Benevento|Герцогство Беневенто
Grand Duchy of Hesse|Великое герцогство Гессен
Dominion of Newfoundland|Доминион Ньюфаундленд
Acadian Peninsula (UK)|Акадский полуостров · британское владение
Cyraneica (UK Lybia)|Киренаика · британская администрация
Tripolitana (UK Lybia)|Триполитания · британская администрация
Fezzan (Frech Lybia)|Феццан · французская администрация
Ethiopian highland farmers|Земледельцы Эфиопского нагорья
Coastal and Woodland Mesolithic Hunter-Foragers|Мезолитические сообщества побережий и лесов
Iranian pastoralists|Иранские скотоводческие общества
Catacomb culture|Катакомбная культурная общность
Chernoles culture|Чернолесская культура
Chinchorro culture|Культура Чинчорро
Gandhara grave culture|Гандхарская культура погребений
Dapenkeng culture|Культура Дапэнькэн
Dakapeng culture|Культура Дапэнькэн
Champa City States|Города-государства Тямпы
Beylik of Aydin|Айдынский бейлик
Buyid Emirate|Держава Буидов
Buwayhid Emirates|Эмираты Буидов
Bahmani Kingdom|Бахманийский султанат
Arapaho|Арапахо
Cherokee|Чероки
Cheyenne|Шайенны
Choctaw|Чокто
Chickasaw|Чикасо
Comanche|Команчи
Creek|Крики
Crow|Кроу
Haudenosaunee|Хауденосауни
Iroquois|Ирокезы
Blackfoot|Черноногие
Kiowa|Кайова
Cree|Кри
Plains Cree|Равнинные кри
Plains|Равнинные
Mapuche|Мапуче
Ojibwe|Оджибве
Mohawk|Мохоки
Seneca|Сенека
Cayuga|Кайюга
Oneida|Онейда
Onondaga|Онондага
Seminole|Семинолы
Shawnee|Шауни
Osage|Осейджи
Pawnee|Пауни
Potawatomi|Потаватоми
Nez Perce|Нез-персе
Nisga'a|Нисгаа
Tlingit|Тлинкиты
Tsimshian|Цимшиан
Haida|Хайда
Hopi|Хопи
Zuni|Зуньи
Miwok|Мивок
Ohlone|Олони
Yurok|Юрок
Yupik|Юпики
Yup’ik/Cup’ik|Юпики и чупики
Yup'ik & Cup'ik|Юпики и чупики
Inupiat|Инупиаты
Chukchi|Чукчи
Aleut|Алеуты
Arawak|Араваки
Yanomami|Яномами
Kayapo|Каяпо
Tupinambá|Тупинамба
Shipibo-Konibo|Шипибо-конибо
Ashaninka|Ашанинка
Asheninka|Ашенинка
Warlpiri|Варлпири
Pitjantjatjara|Питянтятяра
Arrernte|Аррернте
Yolngu|Йолнгу
Noongar|Нунгар
Wiradjuri|Вираджури
Gurindji|Гуринджи
Bohemia|Богемия
Hungary|Венгрия
`.trim().split('\n').map(s=>s.split('|'))));
const words={'Empire':'империя','Emirate':'эмират','Emirates':'эмираты','Duchy':'герцогство','Grand':'Великое','Kingdoms':'царства','Khanates':'ханства','Kingdom':'королевство','Republic':'республика','Confederation':'конфедерация','Confederacy':'конфедерация','Caliphate':'халифат','Sultanate':'султанат','Khanate':'ханство','Principality':'княжество','Protectorate':'протекторат','States':'государства','state':'государство','states':'государства','tribes':'племена','Tribes':'племена','culture':'культура','Culture':'культура','cultures':'культуры','First':'коренные','Confederated':'объединённые','Villages':'поселения','Council':'совет','Tribe':'народ','Indians':'индейские народы','Settlement':'поселение','settlements':'поселения','territory':'территория','peoples':'народы','people':'народ','North':'Северный','Northern':'Северный','South':'Южный','Southern':'Южный','East':'Восточный','Eastern':'Восточный','West':'Западный','Western':'Западный','Central':'Центральный','Upper':'Верхний','Lower':'Нижний','Mountain':'Горный','River':'река','Island':'остров','Islands':'острова','Indian':'индийское','Community':'община','Nation':'народ','Metis':'метисы','Métis':'метисы','and':'и','of':'','the':'','UK':'Британия','RU':'Россия','FR':'Франция','BC':'Британская Колумбия','Reservation':'резервация','princely':'княжеское','under':'под','influence':'влиянием','hunters':'охотники','gatherers':'собиратели'};
const letter={a:'а',b:'б',c:'к',d:'д',e:'е',f:'ф',g:'г',h:'х',i:'и',j:'дж',k:'к',l:'л',m:'м',n:'н',o:'о',p:'п',q:'к',r:'р',s:'с',t:'т',u:'у',v:'в',w:'в',x:'кс',y:'й',z:'з',æ:'э',œ:'ё',ø:'ё',ł:'л',ð:'д',þ:'т',ŋ:'нг',ə:'э',ʉ:'у',Ɂ:'',ʔ:'',ʷ:'в',ʌ:'а',ɫ:'л',ƛ:'тл',ɬ:'л',ɔ:'о',ʊ:'у',β:'в',θ:'т',ώ:'о',ʰ:'х',ʲ:'ь',ʕ:'',ɩ:'и',ʔ:'',ᖹ:'',ᐟ:'',ᒧ:'',ᐧ:'',ᨑ:'',ʦ:'ц'};
function transliterate(input){return input.normalize('NFD').replace(/\p{M}/gu,'').replace(/[\p{L}]+/gu,w=>{if(explicit[w])return explicit[w];if(w in words)return words[w];let s=w.toLowerCase().replace(/tch/g,'ч').replace(/sh/g,'ш').replace(/ch/g,'ч').replace(/zh/g,'ж').replace(/th/g,'т').replace(/ph/g,'ф').replace(/kh/g,'х').replace(/ng/g,'нг').replace(/oo/g,'у').replace(/ee/g,'и');s=[...s].map(c=>letter[c]??c).join('');return w[0]===w[0].toUpperCase()?s[0]?.toUpperCase()+s.slice(1):s;}).replace(/\p{Script=Latin}/gu,'').replace(/[^\p{Script=Cyrillic}\p{Number}\p{Punctuation}\p{Separator}]/gu,'').replace(/\s+/g,' ').trim();}
const result={},approx=[];
for(const n of [...names].sort()){if(!n.trim()||/^\?\s*$/.test(n)){result[n]='Местные сообщества';continue;}result[n]=explicit[n]||transliterate(n)||'Местные сообщества';if(!explicit[n])approx.push(n);}
fs.writeFileSync('dist/area-names.js','// Generated by scripts/localize-names.mjs. Established exonyms + Cyrillic renderings of other autonyms.\nexport const namesRu='+JSON.stringify(result,null,1)+';\nexport const transcribedNames=new Set('+JSON.stringify(approx)+');\n');
console.log({total:names.size,exonyms:names.size-approx.length,transcriptions:approx.length});
