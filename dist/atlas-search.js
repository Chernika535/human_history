// Search is independent of the displayed year and layer. All navigation targets are dated.
export const normalizeSearch=s=>String(s||'').normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase('ru').replace(/ё/g,'е').replace(/[·—–,()[\]]/g,' ').replace(/\s+/g,' ').trim();
export function targetYear(periods,year){return periods.reduce((best,[a,b])=>{const y=Math.max(a,Math.min(b,year));return best===null||Math.abs(y-year)<Math.abs(best-year)?y:best;},null);}
export function searchAtlas(entries,query,year,limit=60){const q=normalizeSearch(query);if(!q)return [];const tokens=q.split(' ');return entries.map(e=>{const names=e.names.map(normalizeSearch),exact=names.some(n=>n===q),prefix=names.some(n=>n.startsWith(q)),matched=names.some(n=>tokens.every(t=>n.includes(t)));return matched?{...e,target:targetYear(e.periods,year),score:exact?0:prefix?1:2}:null;}).filter(Boolean).sort((a,b)=>a.score-b.score||Math.abs(a.target-year)-Math.abs(b.target-year)||a.label.localeCompare(b.label,'ru')).slice(0,limit);}
export function namedBorderNeighbours(feature,features){
 if(!feature?.geometry||feature.properties.background)return [];
 const rings=g=>g.type==='Polygon'?g.coordinates:g.type==='MultiPolygon'?g.coordinates.flat():[];
 const point=([x,y])=>x.toFixed(3)+','+y.toFixed(3),edge=(a,b)=>[point(a),point(b)].sort().join('|'),edges=new Set();
 for(const r of rings(feature.geometry))for(let i=1;i<r.length;i++)if(point(r[i])!==point(r[i-1]))edges.add(edge(r[i],r[i-1]));
 // Both polygons must actually contain the same segment, not just its two endpoints.
 const touching=g=>rings(g).some(r=>r.some((p,i)=>i>0&&point(p)!==point(r[i-1])&&edges.has(edge(p,r[i-1]))));
 return features.filter(f=>f.id!==feature.id&&!f.properties.background&&f.properties.name!==feature.properties.name&&touching(f.geometry));
}
