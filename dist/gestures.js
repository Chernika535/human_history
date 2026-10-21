// Pointer gesture state is independent of the DOM so multi-touch transitions are testable.
export const clampZoom=z=>Math.max(.7,Math.min(4.5,z));
const latitude=y=>Math.max(-85,Math.min(85,y));
const longitude=x=>((x+180)%360+360)%360-180;
const point=p=>({x:p.clientX,y:p.clientY});
export class GlobeGesture {
 constructor(read,apply,tap){this.read=read;this.apply=apply;this.tap=tap;this.pointers=new Map();this.suppressTap=false;this.anchor=null;}
 rebase(){const ps=[...this.pointers.values()];if(!ps.length){this.anchor=null;return;}const state=this.read();const mid=ps.length>=2?{x:(ps[0].x+ps[1].x)/2,y:(ps[0].y+ps[1].y)/2}:ps[0];this.anchor={...state,rotation:[...state.rotation],mid:{...mid},distance:ps.length>=2?Math.hypot(ps[0].x-ps[1].x,ps[0].y-ps[1].y):0};}
 down(e){if(!this.pointers.size)this.suppressTap=false;this.pointers.set(e.pointerId,point(e));if(this.pointers.size>1)this.suppressTap=true;this.rebase();}
 move(e){if(!this.pointers.has(e.pointerId))return false;this.pointers.set(e.pointerId,point(e));const ps=[...this.pointers.values()],a=this.anchor;if(!a)return false;const mid=ps.length>=2?{x:(ps[0].x+ps[1].x)/2,y:(ps[0].y+ps[1].y)/2}:ps[0];const dx=mid.x-a.mid.x,dy=mid.y-a.mid.y;if(Math.hypot(dx,dy)>5)this.suppressTap=true;let zoom=a.zoom;if(ps.length>=2&&a.distance>0)zoom=clampZoom(a.zoom*Math.hypot(ps[0].x-ps[1].x,ps[0].y-ps[1].y)/a.distance);this.apply({zoom,rotation:[longitude(a.rotation[0]+dx*.23/a.zoom),latitude(a.rotation[1]-dy*.23/a.zoom),0]});return true;}
 up(e,cancelled=false){if(!this.pointers.has(e.pointerId))return;const canTap=!cancelled&&!this.suppressTap&&this.pointers.size===1;this.pointers.delete(e.pointerId);if(canTap)this.tap(e);this.rebase();if(!this.pointers.size)this.suppressTap=false;}
}
