import {getLanguage,englishText} from './i18n.js?v=0.11.1';
export const MIN_YEAR=-100000, MAX_YEAR=2025;
export const epochs=[{name:'Охотники и собиратели',year:-40000},{name:'Первые земледельцы',year:-8500},{name:'Первые города',year:-3500},{name:'Бронзовый век',year:-2560},{name:'Железный век',year:-1200},{name:'Античность',year:100},{name:'Раннее Средневековье',year:750},{name:'Средневековье',year:1250},{name:'Раннее Новое время',year:1600},{name:'Индустриальная эпоха',year:1850},{name:'XX–XXI века',year:1960}];
export const anchors=[-100000,-40000,-12000,-8000,-4000,-2000,-1000,1,500,1000,1500,1800,1900,2025];
// Period names are navigation conventions, not synchronous global stages.
const epochStarts=[-100000,-12000,-4500,-3300,-1200,-800,476,1000,1453,1750,1900];
epochs.forEach((epoch,i)=>{epoch.start=epochStarts[i];});
export function formatYear(y){return `${Math.abs(y).toLocaleString(getLanguage()==='en'?'en-US':'ru-RU')} ${getLanguage()==='en'?(y<0?'BCE':'CE'):(y<0?'до н. э.':'н. э.')}`;}
export function activeAt(records,year){return records.filter(r=>r.start<=year&&year<=r.end);}
export function yearToPosition(y){let i=anchors.findIndex((a,j)=>j<anchors.length-1&&y>=a&&y<=anchors[j+1]);if(i<0)return y<=MIN_YEAR?0:1000;return (i+(y-anchors[i])/(anchors[i+1]-anchors[i]))/(anchors.length-1)*1000;}
export function positionToYear(p){const v=Math.min(1000,Math.max(0,p))/1000*(anchors.length-1),i=Math.min(anchors.length-2,Math.floor(v));let y=Math.round(anchors[i]+(anchors[i+1]-anchors[i])*(v-i));return y===0?1:y;}
export function parseYear(value,era='ce'){const n=Number(String(value).trim());if(!String(value).trim()||!Number.isInteger(n)||n===0)return null;const y=n<0?n:era==='bce'?-n:n;return y>=MIN_YEAR&&y<=MAX_YEAR?y:null;}
export function matches(r,q){return `${r.name} ${r.region} ${r.summary} ${r.aliases||''} ${englishText(r.name)} ${englishText(r.summary)}`.toLocaleLowerCase('ru').includes(q.toLocaleLowerCase('ru').trim());}
export function activeRelations(data,year,type='all'){return activeAt(data.relations,year).filter(r=>type==='all'||r.type===type).filter(r=>data.cultures.some(c=>c.id===r.from&&c.start<=year&&c.end>=year)&&data.cultures.some(c=>c.id===r.to&&c.start<=year&&c.end>=year));}
