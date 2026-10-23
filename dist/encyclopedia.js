import {unpackBundle} from './polities.js?v=0.11.1';
// Independently licensed, attributed historical prose is loaded only when a card opens.
export class EncyclopediaStore {
 constructor(index,fetcher=url=>fetch(url)){this.index=index;this.fetcher=fetcher;this.cache=new Map();this.pending=new Map();}
 peek(key){const file=this.index.entries[key]?.file;return file?this.cache.get(file)?.[key]:null;}
 async load(key){const file=this.index.entries[key]?.file;if(!file)return null;if(!this.cache.has(file)){let p=this.pending.get(file);if(!p){p=this.fetcher('data/'+(this.index.directory||'encyclopedia')+'/'+file).then(r=>{if(!r.ok)throw Error('Historical account unavailable');return r.json();}).then(async d=>d.encoding?unpackBundle(d):d).then(d=>{this.cache.set(file,d);return d;}).finally(()=>this.pending.delete(file));this.pending.set(file,p);}await p;}return this.peek(key);}
}
export function accountFor(record,language){return record?.[language]||record?.ru||record?.en||null;}
