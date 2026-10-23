// Names are tied to a named polity and historical interval, never projected onto ancient cultures.
export const endonyms={
 'Japan':{from:1947,to:2025,names:['日本','Nihon','Nippon','日本国','Нихон','Ниппон'],url:'https://www.auswaertiges-amt.de/de/service/laender/japan-node/japan-213030'},
 'Third Hellenic Republic':{from:1974,to:2025,names:['Ελλάδα','Ελληνική Δημοκρατία','Elláda','Ellinikí Dimokratía','Эллада'],url:'https://www.auswaertiges-amt.de/de/service/laender/griechenland-node/griechenland-211520'},
 'Republic of India':{from:1950,to:2025,names:['भारत','Bhārat','Бхарат','भारत गणराज्य','Bhārat Gaṇarājya'],text:{ru:'Индия также называет себя Бхарат (भारत, Bhārat). В статье 1 Конституции закреплены оба названия — India и Bharat. На хинди название республики — भारत गणराज्य (Bhārat Gaṇarājya); Индия многоязычна, и это не единственный местный вариант.',en:'India also calls itself Bharat (भारत, Bhārat). Article 1 of the Constitution recognizes both India and Bharat. The Hindi name of the republic is भारत गणराज्य (Bhārat Gaṇarājya); India is multilingual and this is not its only local-language name.'},url:'https://www.legislative.gov.in/static/uploads/2025/07/359f70a69695affb9d72f8393102bd2e.pdf'},
 'Federated Republic of Germany':{from:1949,to:2025,names:['Deutschland','Bundesrepublik Deutschland','Дойчланд'],url:'https://en.wikipedia.org/wiki/Germany'},
 'Republic of Finland':{from:1917,to:2025,names:['Suomi','Suomen tasavalta','Finland','Republiken Finland','Суоми'],url:'https://en.wikipedia.org/wiki/Finland'},
 'Hungarian Republic':{from:1989,to:2025,names:['Magyarország','Мадьярорсаг'],url:'https://en.wikipedia.org/wiki/Hungary'},
 'Republic of Austria':{from:1945,to:2025,names:['Österreich','Republik Österreich','Эстеррайх'],url:'https://en.wikipedia.org/wiki/Austria'},
 'Republic of Turkey':{from:1923,to:2025,names:['Türkiye','Türkiye Cumhuriyeti','Тюркие'],url:'https://en.wikipedia.org/wiki/Turkey'},
 'People\'s Republic of China':{from:1949,to:2025,names:['中国','中华人民共和国','Zhōngguó','Zhōnghuá Rénmín Gònghéguó','Чжунго'],url:'https://en.wikipedia.org/wiki/China'},
 'Kingdom of Spain':{from:1978,to:2025,names:['España','Reino de España','Эспанья'],url:'https://en.wikipedia.org/wiki/Spain'},
 'Republic of Italy':{from:1946,to:2025,names:['Italia','Repubblica Italiana','Италия'],url:'https://en.wikipedia.org/wiki/Italy'},
 'Italian Republic':{from:1946,to:2025,names:['Italia','Repubblica Italiana','Италия'],url:'https://en.wikipedia.org/wiki/Italy'},
 'Kingdom of Belgium':{from:1830,to:2025,names:['België','Belgique','Belgien','Koninkrijk België','Royaume de Belgique','Königreich Belgien'],url:'https://en.wikipedia.org/wiki/Belgium'},
 'Netherlands':{from:1815,to:2025,names:['Nederland','Koninkrijk der Nederlanden','Нидерланд'],url:'https://en.wikipedia.org/wiki/Netherlands'},
 'Swiss Confederation':{from:1848,to:2025,names:['Schweiz','Suisse','Svizzera','Svizra','Confoederatio Helvetica'],url:'https://en.wikipedia.org/wiki/Switzerland'},
 'Portugal':{from:1910,to:2025,names:['Portugal','República Portuguesa','Португал'],url:'https://en.wikipedia.org/wiki/Portugal'},
 'Islamic Republic of Iran':{from:1979,to:2025,names:['ایران','جمهوری اسلامی ایران','Īrān','Jomhuri-ye Eslāmi-ye Irān'],url:'https://en.wikipedia.org/wiki/Iran'},
 'Arab Republic of Egypt':{from:1971,to:2025,names:['مصر','Miṣr','جمهورية مصر العربية','Jumhūriyyat Miṣr al-ʿArabiyya','Миср'],url:'https://en.wikipedia.org/wiki/Egypt'}
};
export function endonymFor(name,year){const n=endonyms[name];return n&&n.from<=year&&year<=n.to?n:null;}
