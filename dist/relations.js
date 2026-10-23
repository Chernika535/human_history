// One visual key shared by globe, filters and relationship cards.
export const relationStyles={trade:{color:'#59d8e8',dash:[],label:'Торговля и обмен'},colonial:{color:'#ff9b82',dash:[7,5],label:'Колониальная зависимость'}};
export function relationStyle(type){return relationStyles[type]||{color:'#b9a5ff',dash:[3,3],label:'Связь'};}
// A search selects connected relationships; keep both endpoints visible.
export function relationNetwork(cultures,relations,seedIds){const byId=new Map(cultures.map(c=>[c.id,c]));const links=relations.filter(r=>byId.has(r.from)&&byId.has(r.to)&&(!seedIds||seedIds.has(r.from)||seedIds.has(r.to)));const ids=new Set(links.flatMap(r=>[r.from,r.to]));return {links,nodes:cultures.filter(c=>ids.has(c.id))};}
export function relationNodeColor(id,links){const types=new Set(links.filter(r=>r.from===id||r.to===id).map(r=>r.type));return types.size===1?relationStyle([...types][0]).color:'#f2f6ff';}
export function segmentDistance(p,a,b){const dx=b[0]-a[0],dy=b[1]-a[1],length=dx*dx+dy*dy;const t=length?Math.max(0,Math.min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/length)):0;return Math.hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dy);}
