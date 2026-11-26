"""Epic Tales Daily drawing kit: characters, props, backdrops and card layouts.

Every episode is drawn with this kit so the look never changes. See CLAUDE.md.
"""
import textwrap, subprocess, random, math, json, sys, importlib.util, pathlib
W,H=1080,1350
FONT="Inter, DejaVu Sans, sans-serif"
SERIES="EPIC TALES DAILY"
INK="#3b2414"

def T(x,y,lines,size=20,fill=INK,weight="400",anchor="start",lh=1.3):
    o=f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">'
    for i,l in enumerate(lines): o+=f'<tspan x="{x}" dy="{0 if i==0 else size*lh}">{l}</tspan>'
    return o+'</text>'

def person(x,y,s=1,robe="#1f618d",skin="#c68642",trim="#f1c40f",hair="#2b1b12",crown=False,beard=None,beardlen=30,mood="smile",topknot=False,female=False,drape=None,arms="down",tiara=False,flip=False,eyes=True):
    g=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    def arm(x1,y1,x2,y2): return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{robe}" stroke-width="15" stroke-linecap="round"/><circle cx="{x2}" cy="{y2}" r="9" fill="{skin}"/>'
    if female: g+=f'<path d="M-36,-44 Q-46,10 -28,26 L28,26 Q46,10 36,-44 Z" fill="{hair}"/>'
    if arms=="down": g+=arm(-27,12,-47,66)+arm(27,12,47,66)
    if arms=="raise": g+=arm(-27,12,-47,66)+arm(27,14,60,-22)
    if arms=="up2": g+=arm(-27,14,-62,-30)+arm(27,14,62,-30)
    g+=f'<path d="M-30,0 Q0,-14 30,0 L46,120 L-46,120 Z" fill="{robe}"/>'
    if drape: g+=f'<polygon points="-30,0 -6,-9 46,100 46,120 18,120" fill="{drape}"/>'
    g+=f'<path d="M-46,120 L46,120 L44,106 L-44,106 Z" fill="{trim}"/>'
    g+=f'<path d="M-30,0 Q0,-14 30,0 L27,14 Q0,2 -27,14 Z" fill="{trim}"/>'
    if arms=="hold": g+=arm(-27,14,-13,52)+arm(27,14,13,52)
    if topknot: g+=f'<circle cx="0" cy="-78" r="13" fill="{hair}"/>'
    g+=f'<circle cx="0" cy="-38" r="34" fill="{skin}"/>'
    if hair: g+=f'<path d="M-34,-42 A34,34 0 0 1 34,-42 Q0,-60 -34,-42 Z" fill="{hair}"/>'
    if beard: g+=f'<path d="M-30,-28 Q0,{beardlen} 30,-28 Q0,-8 -30,-28 Z" fill="{beard}"/>'
    if crown: g+='<polygon points="-27,-62 -27,-92 -13,-78 0,-100 13,-78 27,-92 27,-62" fill="#f1c40f" stroke="#b7950b" stroke-width="2"/><circle cx="0" cy="-73" r="5" fill="#c0392b"/>'
    if tiara: g+='<path d="M-25,-61 Q0,-80 25,-61" stroke="#f1c40f" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="0" cy="-73" r="5" fill="#c0392b"/>'
    if female: g+='<circle cx="0" cy="-53" r="3" fill="#c0392b"/><circle cx="-34" cy="-30" r="4" fill="#f1c40f"/><circle cx="34" cy="-30" r="4" fill="#f1c40f"/>'
    g+='<circle cx="-21" cy="-29" r="6" fill="#e57373" opacity="0.35"/><circle cx="21" cy="-29" r="6" fill="#e57373" opacity="0.35"/>'
    if eyes: g+='<circle cx="-12" cy="-40" r="4" fill="#2b1b12"/><circle cx="12" cy="-40" r="4" fill="#2b1b12"/>'
    if mood=="sad": g+='<path d="M-9,-20 Q0,-28 9,-20" stroke="#2b1b12" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M-19,-48 L-7,-53 M7,-53 L19,-48" stroke="#2b1b12" stroke-width="3" stroke-linecap="round"/>'
    elif mood=="stern": g+='<path d="M-9,-22 L9,-22" stroke="#2b1b12" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M-20,-53 L-7,-47 M7,-47 L20,-53" stroke="#2b1b12" stroke-width="3.5" stroke-linecap="round"/>'
    else: g+='<path d="M-9,-26 Q0,-17 9,-26" stroke="#2b1b12" stroke-width="3" fill="none" stroke-linecap="round"/>'
    return g+'</g>'

KING=dict(robe="#1f618d",beard="#d7dbdd",crown=True)
SAGE=dict(robe="#e67e22",hair="#ecf0f1",beard="#ecf0f1",beardlen=70,topknot=True,trim="#b9770e")
Q1=dict(robe="#1e8449",drape="#58d68d",female=True,tiara=True)
Q2=dict(robe="#b03a2e",drape="#ec7063",female=True,tiara=True)
Q3=dict(robe="#d4ac0d",drape="#f9e79f",female=True,tiara=True,trim="#b9770e")

def cradle(x,y,s=1,skin=None,blanket="#f1c40f"):
    g=f'<g transform="translate({x},{y}) scale({s})"><path d="M-44,58 Q0,84 44,58" stroke="#7a4a1c" stroke-width="6" fill="none" stroke-linecap="round"/>'
    if skin:
        g+=f'<circle cx="0" cy="-16" r="26" fill="{skin}"/><path d="M-10,-40 Q0,-52 10,-40" stroke="#2b1b12" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M-14,-18 Q-9,-24 -4,-18 M4,-18 Q9,-24 14,-18" stroke="#2b1b12" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M-7,-6 Q0,2 7,-6" stroke="#2b1b12" stroke-width="3" fill="none" stroke-linecap="round"/>'
    g+='<path d="M-50,0 Q0,66 50,0 Z" fill="#a0522d"/>'
    g+=(f'<path d="M-50,0 Q0,22 50,0 Q0,-8 -50,0 Z" fill="{blanket}"/>' if skin else '<ellipse cx="0" cy="0" rx="50" ry="10" fill="#5d2f14"/>')
    return g+'</g>'
def tree(x,y,r=70,c="#6aa84f"):
    return f'<rect x="{x-11}" y="{y}" width="22" height="{r*1.5}" fill="#7a4a1c"/><circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/><circle cx="{x-r*0.55}" cy="{y+r*0.35}" r="{r*0.6}" fill="{c}"/><circle cx="{x+r*0.55}" cy="{y+r*0.35}" r="{r*0.6}" fill="{c}"/>'
def palace(x,y,s,c1="#e8a33d",c2="#d9952f",c3="#c9812a",dk="#7a4a1c",flags=True):
    g=f'<g transform="translate({x},{y}) scale({s})">'
    for tx in (90,410):
        g+=f'<rect x="{tx}" y="250" width="60" height="190" fill="{c2}"/><path d="M{tx-5},250 Q{tx+30},185 {tx+65},250 Z" fill="{c3}"/>'
        if flags: g+=f'<line x1="{tx+30}" y1="218" x2="{tx+30}" y2="180" stroke="{dk}" stroke-width="3"/><polygon points="{tx+30},180 {tx+58},189 {tx+30},198" fill="#c0392b"/>'
        g+=f'<rect x="{tx+20}" y="290" width="20" height="36" rx="10" fill="{dk}"/><rect x="{tx+20}" y="360" width="20" height="36" rx="10" fill="{dk}"/>'
    g+=f'<rect x="150" y="300" width="260" height="140" fill="{c1}"/><path d="M215,300 Q280,195 345,300 Z" fill="{c2}"/><line x1="280" y1="248" x2="280" y2="215" stroke="{dk}" stroke-width="3"/><circle cx="280" cy="211" r="7" fill="#f1c40f"/>'
    g+=f'<path d="M255,440 L255,385 Q280,348 305,385 L305,440 Z" fill="{dk}"/>'
    for wx in (180,215,330,365): g+=f'<rect x="{wx}" y="340" width="18" height="34" rx="9" fill="{dk}"/>'
    return g+'</g>'
def basket(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><circle cx="-12" cy="-6" r="10" fill="#e74c3c"/><circle cx="6" cy="-10" r="10" fill="#f39c12"/><circle cx="18" cy="-3" r="8" fill="#8e44ad"/><path d="M-30,0 Q0,40 30,0 Z" fill="#a0522d"/></g>'
def bowl(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="-2" rx="22" ry="10" fill="#fffaf0"/><path d="M-28,0 Q0,36 28,0 Z" fill="#d4ac0d" stroke="#9a7d0a" stroke-width="2"/></g>'
def spark(x,y,r=12,c="#f7dc6f"):
    return f'<path d="M{x},{y-r} Q{x},{y} {x+r},{y} Q{x},{y} {x},{y+r} Q{x},{y} {x-r},{y} Q{x},{y} {x},{y-r} Z" fill="{c}"/>'
def bunting(y,sag,n=13):
    cols=["#c0392b","#f1c40f","#1f618d","#27ae60","#e67e22"]
    g=f'<path d="M0,{y} Q500,{y+2*sag} 1000,{y}" stroke="{INK}" stroke-width="3" fill="none"/>'
    for k in range(n):
        t=(k+0.5)/n; bx=1000*t; by=y+2*sag*2*t*(1-t)
        g+=f'<polygon points="{bx-24:.0f},{by-3:.0f} {bx+24:.0f},{by-3:.0f} {bx:.0f},{by+44:.0f}" fill="{cols[k%5]}"/>'
    return g

DEFS='''<defs>
<linearGradient id="sunrise" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4a261"/><stop offset="1" stop-color="#fde9a9"/></linearGradient>
<linearGradient id="night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0f1b3d"/><stop offset="1" stop-color="#34497a"/></linearGradient>
<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a235a"/><stop offset="1" stop-color="#e59866"/></linearGradient>
<linearGradient id="river" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5dade2"/><stop offset="1" stop-color="#2e86c1"/></linearGradient>
<linearGradient id="band" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7b241c"/><stop offset="1" stop-color="#943126"/></linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#fff6c9" stop-opacity="0.95"/><stop offset="1" stop-color="#fff6c9" stop-opacity="0"/></radialGradient>
<linearGradient id="forest" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#173d24"/><stop offset="1" stop-color="#2e7d32"/></linearGradient>
<linearGradient id="day" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d8f2"/><stop offset="1" stop-color="#e3f4fb"/></linearGradient>
</defs>'''


# ---- Fixed character designs. Never change these between episodes. ----
RAMA=dict(robe="#f1c40f",skin="#7fb3d5",trim="#c0392b",tiara=True)
LAKSHMANA=dict(robe="#c0392b",skin="#d49a5b",tiara=True)
BHARATA=dict(robe="#27ae60",skin="#c68642",tiara=True)
SHATRUGHNA=dict(robe="#8e44ad",skin="#c68642",tiara=True)
VISHVAMITRA=dict(robe="#a04000",hair="#5d4037",beard="#8d6e63",beardlen=60,topknot=True,trim="#6e2c00")

# ---- Props ----
def label(x,y,text,size=24,fill=INK):
    """A name tag on a cream pill, so it stays readable over any background."""
    w=len(text)*size*0.62+36
    return f'<rect x="{x-w/2:.0f}" y="{y-size-6}" width="{w:.0f}" height="{size+20}" rx="{(size+20)/2:.0f}" fill="#fffaf0" stroke="{INK}" stroke-width="2"/>'+T(x,y,[text],size,fill,"700","middle")
def staff(x,y,h=260): return f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-h}" stroke="#6e2c00" stroke-width="9" stroke-linecap="round"/>'
def bow(x,y,s=1,flip=False):
    return f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})"><path d="M0,-60 Q46,0 0,60" stroke="#7a4a1c" stroke-width="7" fill="none" stroke-linecap="round"/><line x1="0" y1="-60" x2="0" y2="60" stroke="#fffaf0" stroke-width="2.5"/></g>'
def arrow(x1,y1,x2,y2):
    a=math.atan2(y2-y1,x2-x1); hx,hy=x2-22*math.cos(a),y2-22*math.sin(a); px,py=-math.sin(a)*9,math.cos(a)*9
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#5d4037" stroke-width="5" stroke-linecap="round"/><polygon points="{x2:.0f},{y2:.0f} {hx+px:.0f},{hy+py:.0f} {hx-px:.0f},{hy-py:.0f}" fill="#5d4037"/>'
def target(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><line x1="-30" y1="60" x2="-50" y2="170" stroke="#7a4a1c" stroke-width="8"/><line x1="30" y1="60" x2="50" y2="170" stroke="#7a4a1c" stroke-width="8"/><circle r="80" fill="#fffaf0" stroke="{INK}" stroke-width="4"/><circle r="56" fill="#c0392b"/><circle r="32" fill="#fffaf0"/><circle r="12" fill="#c0392b"/></g>'
def book(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-8" width="44" height="18" rx="3" fill="#f5e6c4" stroke="#7a4a1c" stroke-width="2"/><line x1="-14" y1="-1" x2="14" y2="-1" stroke="#7a4a1c" stroke-width="1.5"/><line x1="-14" y1="4" x2="14" y2="4" stroke="#7a4a1c" stroke-width="1.5"/></g>'
def fire(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s}) translate(-500,-650)"><path d="M500,650 Q360,560 440,460 Q470,520 500,395 Q560,500 575,465 Q660,575 500,650 Z" fill="#e67e22"/><path d="M500,650 Q420,585 478,520 Q500,560 512,480 Q580,575 500,650 Z" fill="#f9e79f"/><rect x="400" y="640" width="200" height="70" fill="#8d5524"/><rect x="370" y="710" width="260" height="30" fill="#7a4a1c"/></g>'
def demon(x,y,s=1):
    """A shadowy rakshasa. Keep demons as dark silhouettes: scary shapes, no gore."""
    return f'<g transform="translate({x},{y}) scale({s})" opacity="0.92"><polygon points="-30,-38 -46,-84 -12,-50" fill="#1a1a2e"/><polygon points="30,-38 46,-84 12,-50" fill="#1a1a2e"/><path d="M-56,70 Q-70,-20 0,-56 Q70,-20 56,70 Z" fill="#1a1a2e"/><circle cx="-18" cy="-12" r="8" fill="#e74c3c"/><circle cx="18" cy="-12" r="8" fill="#e74c3c"/><path d="M-20,20 L-10,10 L0,20 L10,10 L20,20" stroke="#e74c3c" stroke-width="4" fill="none"/></g>'

# ---- Backdrops (scene coordinates are 1000 wide by 860 tall) ----
def bg_court():
    g='<rect width="1000" height="860" fill="#f6d9a8"/>'
    for cx in (200,500,800): g+=f'<path d="M{cx-110},640 L{cx-110},300 Q{cx},140 {cx+110},300 L{cx+110},640 Z" fill="#edc88e"/>'
    for px in (45,335,635,925): g+=f'<rect x="{px}" y="90" width="30" height="550" fill="#e2b97a"/><rect x="{px-8}" y="90" width="46" height="18" fill="#c9812a"/>'
    for k in range(5):
        x0=k*200; g+=f'<path d="M{x0},40 Q{x0+100},110 {x0+200},40" stroke="#27ae60" stroke-width="5" fill="none"/>'
        for j in range(1,6):
            t=j/6; g+=f'<circle cx="{x0+200*t:.0f}" cy="{40+140*t*(1-t):.0f}" r="10" fill="{"#e67e22" if j%2 else "#f1c40f"}"/>'
    g+='<rect y="640" width="1000" height="220" fill="#a0522d"/><polygon points="380,640 620,640 730,860 270,860" fill="#8e2f2f"/><polygon points="380,640 392,640 290,860 270,860" fill="#f1c40f"/><polygon points="608,640 620,640 730,860 710,860" fill="#f1c40f"/>'
    return g
def bg_garden(pond=True):
    g='<rect width="1000" height="860" fill="#cdeaf7"/><circle cx="150" cy="130" r="60" fill="#fff6c9"/>'
    for cx,cy in ((420,120),(480,110),(540,125),(800,180),(850,170)): g+=f'<circle cx="{cx}" cy="{cy}" r="36" fill="#fff" opacity="0.9"/>'
    g+='<path d="M0,520 Q250,460 500,510 T1000,500 L1000,860 L0,860 Z" fill="#9ccc65"/>'
    g+=tree(80,330,90)+tree(900,320,100,"#5b9a45")+tree(500,360,70,"#7cb866")
    for fx,fy,c in ((60,640,"#e74c3c"),(120,690,"#f1c40f"),(900,650,"#e84393"),(950,700,"#f39c12"),(840,720,"#e74c3c"),(160,750,"#e84393")):
        g+=f'<circle cx="{fx}" cy="{fy}" r="26" fill="#5b9a45"/><circle cx="{fx-8}" cy="{fy-6}" r="7" fill="{c}"/><circle cx="{fx+9}" cy="{fy+4}" r="7" fill="{c}"/>'
    if pond: g+='<ellipse cx="500" cy="790" rx="230" ry="48" fill="#5dade2"/>'
    return g
def bg_room():
    g='<rect width="1000" height="860" fill="#f6d9a8"/>'
    for px in (40,930): g+=f'<rect x="{px}" y="0" width="30" height="660" fill="#e2b97a"/>'
    g+='<path d="M380,660 L380,260 Q500,110 620,260 L620,660 Z" fill="#cdeaf7"/><path d="M380,660 L380,260 Q500,110 620,260 L620,660" stroke="#c9812a" stroke-width="14" fill="none"/><circle cx="560" cy="300" r="34" fill="#fff6c9"/>'
    g+='<path d="M0,0 L330,0 Q250,90 120,110 Q60,200 0,230 Z" fill="#8e2f2f"/><path d="M1000,0 L670,0 Q750,90 880,110 Q940,200 1000,230 Z" fill="#8e2f2f"/>'
    g+='<rect y="660" width="1000" height="200" fill="#a0522d"/><ellipse cx="500" cy="770" rx="440" ry="64" fill="#8e2f2f"/><ellipse cx="500" cy="770" rx="440" ry="64" fill="none" stroke="#f1c40f" stroke-width="5"/>'
    return g
def bg_forest():
    g='<rect width="1000" height="860" fill="url(#forest)"/><circle cx="500" cy="330" r="300" fill="url(#glow)" opacity="0.35"/>'
    for tx,tw in ((60,46),(210,34),(360,28),(650,30),(800,40),(940,50)): g+=f'<rect x="{tx-tw/2}" y="0" width="{tw}" height="680" fill="#3e2a1a"/>'
    for cx,cy,r in ((40,60,130),(220,30,120),(400,10,110),(620,20,120),(810,40,130),(980,70,120)): g+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#14351f"/>'
    g+='<path d="M0,650 Q250,610 500,645 T1000,640 L1000,860 L0,860 Z" fill="#3f6b35"/>'
    for bx in (90,300,720,900): g+=f'<circle cx="{bx}" cy="670" r="42" fill="#2f5a2a"/>'
    return g
def bg_road():
    g='<rect width="1000" height="860" fill="url(#sunrise)"/><circle cx="500" cy="330" r="190" fill="url(#glow)"/><circle cx="500" cy="330" r="100" fill="#fff6c9"/>'
    g+='<path d="M0,470 Q180,360 380,450 Q520,380 700,440 Q860,370 1000,460 L1000,860 L0,860 Z" fill="#c9a85f"/>'
    g+=palace(-40,240,0.62)
    g+='<path d="M0,560 Q250,520 500,550 T1000,540 L1000,860 L0,860 Z" fill="#8cc084"/><polygon points="470,548 530,548 760,860 240,860" fill="#e6cf9c"/>'
    g+=tree(880,470,70)+tree(760,500,46,"#5b9a45")
    return g

# ---- Added in Episode 4 ----
def boat(x,y,s=1):
    """A small wooden river boat. Draw it after the people sitting in it so the hull hides their legs."""
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M-230,0 L230,0 Q200,70 120,80 L-120,80 Q-200,70 -230,0 Z" fill="#8d5524"/><path d="M-230,0 L230,0 L222,16 L-222,16 Z" fill="#c9812a"/><line x1="-150" y1="40" x2="150" y2="40" stroke="#6e3b14" stroke-width="4"/></g>'
def rock(x,y,r=30,c="#7f6a55"):
    return f'<path d="M{x-r},{y+r*0.5} Q{x-r*1.1},{y-r*0.4} {x-r*0.3},{y-r*0.8} Q{x+r*0.6},{y-r*1.0} {x+r},{y-r*0.1} Q{x+r*1.05},{y+r*0.6} {x},{y+r*0.75} Z" fill="{c}" stroke="#4e3b2a" stroke-width="3"/>'
def dust(x,y,r=60):
    return f'<g opacity="0.55"><circle cx="{x}" cy="{y}" r="{r}" fill="#c9a87c"/><circle cx="{x+r*0.8}" cy="{y+r*0.2}" r="{r*0.7}" fill="#d8bc93"/><circle cx="{x-r*0.8}" cy="{y+r*0.3}" r="{r*0.65}" fill="#d8bc93"/></g>'
def demon_falling(x,y,s=1,angle=35):
    """A defeated demon toppling over. Still a plain silhouette, never wounded."""
    return f'<g transform="rotate({angle},{x},{y+70*s})">{demon(x,y,s)}</g>'
def soundwaves(x,y,s=1,flip=False):
    """Curved lines for a loud sound, such as a twanging bowstring or a roar."""
    return f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})" fill="none" stroke="#f9e79f" stroke-width="6" stroke-linecap="round"><path d="M0,-30 Q18,0 0,30"/><path d="M20,-50 Q48,0 20,50"/><path d="M40,-70 Q78,0 40,70"/></g>'
def bg_river(far="#9ccc65",sky="url(#day)"):
    """A wide river between two banks. Pass far="#14351f" for a dark forest on the far side."""
    g=f'<rect width="1000" height="860" fill="{sky}"/>'
    g+=f'<path d="M0,330 Q250,290 500,320 T1000,310 L1000,420 L0,420 Z" fill="{far}"/>'
    g+='<rect y="400" width="1000" height="460" fill="url(#river)"/>'
    for wx,wy in ((120,470),(420,500),(760,460),(260,560),(640,590),(880,540)): g+=f'<path d="M{wx-40},{wy} Q{wx-20},{wy-10} {wx},{wy} T{wx+40},{wy}" stroke="#d6eaf8" stroke-width="4" fill="none" stroke-linecap="round"/>'
    return g
def bg_riverbank():
    """Standing on a grassy bank, with the river and the far shore behind."""
    g=bg_river()+'<circle cx="840" cy="130" r="56" fill="#fff6c9"/>'
    g+='<path d="M0,600 Q250,570 500,600 T1000,590 L1000,860 L0,860 Z" fill="#8cc084"/>'
    g+=tree(70,480,80,"#5b9a45")+tree(940,490,74)
    return g

# ---- Added in Episode 5 ----
# A divine astra appearing in its shining form. Draw it with arms="hold" (palms joined) over halo().
ASTRA=dict(robe="#fdebd0",skin="#ffe9a8",trim="#f5b041",hair="#f8c471",tiara=True)
def halo(x,y,r=120,c="#fff6c9"):
    """A soft circle of holy light behind a figure or a divine object."""
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#glow)"/><circle cx="{x}" cy="{y}" r="{r*0.62:.0f}" fill="none" stroke="#f5b041" stroke-width="6" opacity="0.9"/>'
def astra(x,y,s=1,angle=0):
    """A divine astra: a golden arrow glowing with holy light. (x,y) is its middle; angle 0 points straight up."""
    a=f'<g transform="translate({x},{y}) rotate({angle}) scale({s})">'
    a+='<circle r="105" fill="url(#glow)"/><circle r="62" fill="#fffaf0" opacity="0.45"/>'
    a+='<line x1="0" y1="85" x2="0" y2="-70" stroke="#fffaf0" stroke-width="20" stroke-linecap="round" opacity="0.8"/>'
    a+='<line x1="0" y1="85" x2="0" y2="-70" stroke="#d4ac0d" stroke-width="9" stroke-linecap="round"/>'
    a+='<polygon points="0,-116 -24,-66 24,-66" fill="#f1c40f" stroke="#b7950b" stroke-width="3"/>'
    a+='<path d="M0,62 L-20,92 L-20,72 L0,46 Z M0,62 L20,92 L20,72 L0,46 Z" fill="#f39c12" stroke="#b9770e" stroke-width="2"/>'
    a+=spark(28,-92,10,"#fffaf0")+spark(-26,-30,8,"#fffaf0")
    return a+'</g>'
def bowing(x,y,s=1,angle=28,**kw):
    """A person leaning forward in a respectful bow, palms joined. Faces right; pass angle negative with flip=True to face left."""
    kw.setdefault("arms","hold")
    return f'<g transform="rotate({angle},{x},{y+120*s})">{person(x,y,s,**kw)}</g>'
def hut(x,y,s=1):
    """A thatched hermitage hut."""
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="-60" width="140" height="90" fill="#c9a06a"/><path d="M-95,-55 L0,-140 L95,-55 Z" fill="#b8863b"/><path d="M-95,-55 L0,-140 L95,-55" stroke="#8a5a1c" stroke-width="5" fill="none"/><path d="M-20,30 L-20,-20 Q0,-40 20,-20 L20,30 Z" fill="#6e3b14"/></g>'
def bg_dawn_forest(sun=True):
    """Early morning in a forest clearing, with the sun rising in the east (on the right). Pass sun=False to leave the sky clear for glowing figures."""
    g='<rect width="1000" height="860" fill="url(#sunrise)"/>'
    if sun: g+='<circle cx="820" cy="330" r="220" fill="url(#glow)"/><circle cx="820" cy="330" r="80" fill="#fff6c9"/>'
    for tx,tw in ((50,44),(200,30),(960,40)): g+=f'<rect x="{tx-tw/2}" y="0" width="{tw}" height="680" fill="#5a3d22"/>'
    for cx,cy,r in ((30,50,130),(210,20,110),(990,60,110)): g+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#3f6b35"/>'
    g+='<path d="M0,620 Q250,590 500,615 T1000,610 L1000,860 L0,860 Z" fill="#7cb866"/>'
    for bx in (110,880): g+=f'<circle cx="{bx}" cy="650" r="40" fill="#5b9a45"/>'
    return g
def bg_hermitage(huts=True):
    """A peaceful grove at the foot of a hill, with hermitage huts among the trees."""
    g='<rect width="1000" height="860" fill="url(#day)"/><circle cx="160" cy="120" r="50" fill="#fff6c9"/>'
    g+='<path d="M380,470 Q560,170 760,200 Q900,230 1000,420 L1000,520 L380,520 Z" fill="#7d9b6a"/>'
    g+='<path d="M0,500 Q250,450 500,490 T1000,480 L1000,860 L0,860 Z" fill="#9ccc65"/>'
    g+=tree(620,380,60,"#5b9a45")+tree(900,370,66,"#6aa84f")
    if huts: g+=hut(730,500,0.9)+hut(560,520,0.7)
    g+='<path d="M0,620 Q250,595 500,620 T1000,612 L1000,860 L0,860 Z" fill="#8cc084"/>'
    return g

# ---- Added in Episode 6 ----
# The sages who live at Siddhashrama (and other hermitage sages). Not Vasishtha, who is SAGE.
HERMIT=dict(robe="#f0b27a",hair="#bdc3c7",beard="#bdc3c7",beardlen=55,topknot=True,trim="#ca6f1e")
def stars(n=18,seed=6,top=40,bottom=320):
    """Small twinkling stars for a night sky. The same seed always gives the same sky."""
    r=random.Random(seed); g=''
    for _ in range(n):
        x,y=r.randint(30,970),r.randint(top,bottom); g+=spark(x,y,r.choice((5,7,9)),"#fdf2c4")
    return g
def moon(x,y,r=46):
    """A crescent moon."""
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fdf2c4"/><circle cx="{x+r*0.45:.0f}" cy="{y-r*0.2:.0f}" r="{r*0.85:.0f}" fill="#16234a"/>'
def wind(x,y,s=1,flip=False,c="#d6eaf8"):
    """Curling gusts of a strong wind blowing to the right (flip=True blows left)."""
    return f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"><path d="M-120,-40 L40,-40 Q80,-40 80,-70 Q80,-95 55,-95"/><path d="M-150,10 L90,10 Q130,10 130,40 Q130,65 105,65"/><path d="M-100,60 L10,60"/></g>'
def trail(x1,y1,x2,y2,c="#fff6c9"):
    """A curved dotted path showing something flying far away, from (x1,y1) to (x2,y2)."""
    mx,my=(x1+x2)/2,min(y1,y2)-120
    return f'<path d="M{x1},{y1} Q{mx:.0f},{my:.0f} {x2},{y2}" stroke="{c}" stroke-width="7" stroke-dasharray="4 18" stroke-linecap="round" fill="none" opacity="0.9"/>'
def altar(x,y,s=1):
    """A square yajna altar (vedi) of brick with the sacred fire burning on it. (x,y) is the middle of its base."""
    g=f'<g transform="translate({x},{y}) scale({s})">'
    g+='<path d="M0,-40 Q-70,-100 -30,-160 Q-15,-125 0,-200 Q30,-130 40,-150 Q80,-90 0,-40 Z" fill="#e67e22"/><path d="M0,-40 Q-38,-80 -8,-118 Q0,-98 8,-138 Q42,-84 0,-40 Z" fill="#f9e79f"/>'
    g+='<rect x="-90" y="-48" width="180" height="30" fill="#b03a2e"/><rect x="-110" y="-20" width="220" height="20" fill="#922b21"/>'
    for bx in (-80,-40,0,40): g+=f'<line x1="{bx+20}" y1="-48" x2="{bx+20}" y2="-18" stroke="#7b241c" stroke-width="2"/>'
    g+='<line x1="-90" y1="-33" x2="90" y2="-33" stroke="#7b241c" stroke-width="2"/>'
    return g+'</g>'
def bg_hermitage_night():
    """The hermitage clearing at night, under the moon and stars."""
    g='<rect width="1000" height="860" fill="url(#night)"/>'+stars()+moon(150,120)
    g+='<path d="M380,470 Q560,170 760,200 Q900,230 1000,420 L1000,520 L380,520 Z" fill="#2c3e50"/>'
    g+='<path d="M0,500 Q250,450 500,490 T1000,480 L1000,860 L0,860 Z" fill="#33513a"/>'
    g+=tree(620,380,60,"#1e3a26")+tree(900,370,66,"#24452c")
    g+='<path d="M0,620 Q250,595 500,620 T1000,612 L1000,860 L0,860 Z" fill="#3f6343"/>'
    return g

# ---- Added in Episode 7 ----
# King Sagara of Ayodhya, ancestor of Rama, and his sixty thousand sons.
SAGARA=dict(robe="#154360",beard="#aab7b8",crown=True)
SAGARA_SON=dict(robe="#5d6d7e",skin="#c68642",tiara=True)
# King Bhagiratha, Sagara's great great grandson, who brought the Ganga to earth.
BHAGIRATHA=dict(robe="#117a65",beard="#2b1b12",beardlen=0,crown=True)
# Sage Kapila, who sat in tapas deep beneath the earth.
KAPILA=dict(robe="#fbeee0",hair="#2b1b12",beard="#2b1b12",beardlen=55,topknot=True,trim="#e67e22")
# Lord Shiva: ash blue skin, tiger skin robe, matted locks with the crescent moon. Draw him with shiva(), never person().
SHIVA=dict(robe="#d68910",drape="#b9770e",skin="#a9c3d6",trim="#6e2c00",hair="#3b2414")
def shiva(x,y,s=1,arms="up2"):
    """Lord Shiva with his jata (matted locks), the crescent moon and the third eye. Shown with reverence, always calm."""
    tr=f'translate({x},{y}) scale({s})'
    g=f'<g transform="{tr}"><path d="M-38,-46 Q-52,20 -30,40 L30,40 Q52,20 38,-46 Z" fill="#3b2414"/></g>'
    g+=person(x,y,s,arms=arms,**SHIVA)
    g+=f'<g transform="{tr}">'
    g+='<ellipse cx="0" cy="-90" rx="26" ry="30" fill="#3b2414"/><path d="M-18,-108 Q0,-124 18,-108" stroke="#5d4037" stroke-width="4" fill="none"/>'
    g+='<path d="M10,-112 A16,16 0 1 0 30,-90 A12,12 0 1 1 10,-112 Z" fill="#fdf2c4"/>'
    g+='<ellipse cx="0" cy="-49" rx="2.5" ry="5" fill="#c0392b"/></g>'
    return g
def trishula(x,y,h=300):
    """Lord Shiva's trident, standing upright. (x,y) is the foot of the shaft."""
    t=y-h
    return f'<line x1="{x}" y1="{y}" x2="{x}" y2="{t}" stroke="#5d4037" stroke-width="8" stroke-linecap="round"/><path d="M{x-34},{t-40} Q{x-34},{t+8} {x},{t+8} Q{x+34},{t+8} {x+34},{t-40} L{x+26},{t-40} Q{x+24},{t-4} {x},{t-4} Q{x-24},{t-4} {x-26},{t-40} Z" fill="#d4ac0d"/><polygon points="{x},{t-60} {x-7},{t-4} {x+7},{t-4}" fill="#d4ac0d"/>'
def horse(x,y,s=1,flip=False,c="#fdfefe",mane="#d5c4a1"):
    """A white horse standing side on, facing right (flip=True faces left). (x,y) is the middle of its body."""
    g=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    for lx in (-62,-40,40,62): g+=f'<rect x="{lx-7}" y="10" width="14" height="92" rx="6" fill="{c}" stroke="#a6acaf" stroke-width="2"/><rect x="{lx-8}" y="94" width="16" height="10" fill="#5d4037"/>'
    g+=f'<path d="M-88,-10 Q-128,10 -118,70" stroke="{mane}" stroke-width="14" fill="none" stroke-linecap="round"/>'
    g+=f'<ellipse cx="0" cy="0" rx="92" ry="44" fill="{c}" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<path d="M58,-20 L92,-104 L124,-92 L96,-6 Z" fill="{c}" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<path d="M88,-110 L150,-82 Q160,-70 146,-62 L110,-70 Z" fill="{c}" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<polygon points="94,-110 100,-132 108,-108" fill="{c}" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<path d="M88,-104 Q70,-60 62,-18" stroke="{mane}" stroke-width="12" fill="none" stroke-linecap="round"/>'
    g+='<circle cx="116" cy="-92" r="5" fill="#2b1b12"/><path d="M-60,-40 Q0,-52 60,-40 L56,-26 Q0,-38 -56,-26 Z" fill="#c0392b"/>'
    return g+'</g>'
def chariot(x,y,s=1,flip=False):
    """A royal chariot facing right (flip=True faces left). Put the driver at about (x-10, y-150) at the same scale, then draw chariot() after him. (x,y) is the ground under the wheel."""
    g=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    g+='<line x1="70" y1="-90" x2="210" y2="-110" stroke="#7a4a1c" stroke-width="9" stroke-linecap="round"/>'
    g+='<path d="M-90,-170 L80,-170 L96,-80 L-100,-80 Z" fill="#c9812a" stroke="#7a4a1c" stroke-width="4"/><rect x="-100" y="-100" width="196" height="20" fill="#f1c40f"/>'
    g+='<line x1="-90" y1="-170" x2="-90" y2="-260" stroke="#7a4a1c" stroke-width="6"/><polygon points="-90,-260 -50,-246 -90,-232" fill="#c0392b"/>'
    g+='<circle cx="0" cy="-60" r="58" fill="none" stroke="#6e3b14" stroke-width="12"/>'
    for k in range(6):
        a=k*math.pi/6; g+=f'<line x1="{-55*math.cos(a):.0f}" y1="{-60-55*math.sin(a):.0f}" x2="{55*math.cos(a):.0f}" y2="{-60+55*math.sin(a):.0f}" stroke="#6e3b14" stroke-width="5"/>'
    return g+'<circle cx="0" cy="-60" r="10" fill="#f1c40f"/></g>'
def ashes(x,y,s=1):
    """A small heap of grey ashes with a curl of smoke. Used instead of showing anyone hurt."""
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M-70,0 Q-40,-50 0,-56 Q40,-50 70,0 Z" fill="#95a5a6"/><path d="M-40,-10 Q0,-40 40,-10" stroke="#bdc3c7" stroke-width="5" fill="none"/><path d="M0,-64 Q-20,-90 0,-112 Q20,-134 0,-158" stroke="#d5d8dc" stroke-width="8" fill="none" stroke-linecap="round" opacity="0.7"/></g>'
def soul(x,y,r=22):
    """A small glowing light rising up to heaven: a soul set free."""
    return f'<circle cx="{x}" cy="{y}" r="{r*2.2:.0f}" fill="url(#glow)"/><circle cx="{x}" cy="{y}" r="{r}" fill="#fff6c9" stroke="#f5b041" stroke-width="3"/>'
def post(x,y,h=170):
    """An empty wooden post with a loose rope, where an animal was tied."""
    return f'<rect x="{x-10}" y="{y-h}" width="20" height="{h}" fill="#7a4a1c"/><path d="M{x+10},{y-h+30} Q{x+60},{y-h+80} {x+40},{y-10} Q{x+70},{y} {x+90},{y-8}" stroke="#d4ac0d" stroke-width="5" fill="none" stroke-linecap="round"/>'
def ganga_fall(x,top=0,bottom=300,w=90):
    """The holy Ganga pouring straight down from the sky, ending at (x,bottom)."""
    g=f'<path d="M{x-w},{top} Q{x-w*0.4},{(top+bottom)/2:.0f} {x-w*0.25},{bottom} L{x+w*0.25},{bottom} Q{x+w*0.4},{(top+bottom)/2:.0f} {x+w},{top} Z" fill="url(#river)" opacity="0.95"/>'
    for k in (-0.5,0,0.5): g+=f'<path d="M{x+w*k:.0f},{top} Q{x+w*k*0.5:.0f},{(top+bottom)/2:.0f} {x+w*k*0.2:.0f},{bottom-10}" stroke="#d6eaf8" stroke-width="4" fill="none" stroke-linecap="round"/>'
    return g
def bg_himalaya():
    """High snowy peaks of the Himalaya under a clear sky."""
    g='<rect width="1000" height="860" fill="url(#day)"/>'
    g+='<polygon points="-60,620 180,240 420,620" fill="#85929e"/><polygon points="180,240 120,336 160,320 200,350 240,330" fill="#fdfefe"/>'
    g+='<polygon points="560,620 820,200 1080,620" fill="#7f8c8d"/><polygon points="820,200 755,305 800,290 840,320 885,300" fill="#fdfefe"/>'
    g+='<polygon points="230,640 500,300 770,640" fill="#a6acaf"/><polygon points="500,300 430,390 470,375 510,400 560,380" fill="#fdfefe"/>'
    g+='<path d="M0,620 Q250,590 500,615 T1000,608 L1000,860 L0,860 Z" fill="#b3b6b7"/><path d="M0,700 Q250,680 500,700 T1000,692 L1000,860 L0,860 Z" fill="#9aa5a8"/>'
    return g
def bg_underground():
    """A great cave deep under the earth, lit by a soft glow."""
    g='<rect width="1000" height="860" fill="#3e2a1a"/><ellipse cx="500" cy="520" rx="560" ry="420" fill="#5d4130"/><circle cx="500" cy="420" r="360" fill="url(#glow)" opacity="0.25"/>'
    for x0 in (0,170,340,520,700,860): g+=f'<polygon points="{x0},0 {x0+140},0 {x0+70},{110+(x0%3)*30}" fill="#2e1f14"/>'
    g+='<path d="M0,650 Q250,620 500,645 T1000,640 L1000,860 L0,860 Z" fill="#6e4f36"/>'
    for rx,ry,r in ((80,700,40),(930,690,46),(200,780,30),(820,790,34)): g+=rock(rx,ry,r,"#4e3b2a")
    return g

# ---- Added in Episode 8 ----
# Sage Gautama, whose hermitage stood near Mithila, and his wife Ahalya.
GAUTAMA=dict(robe="#cd6155",hair="#ecf0f1",beard="#d5d8dc",beardlen=65,topknot=True,trim="#922b21")
AHALYA=dict(robe="#f4ecf7",drape="#d2b4de",trim="#a569bd",female=True)
def faded(svg,opacity=0.3):
    """Draw anything see-through, for someone who cannot be seen, or a memory fading away."""
    return f'<g opacity="{opacity}">{svg}</g>'
def old_hut(x,y,s=1):
    """A hermitage hut left empty for a very long time: grey thatch with a gap, and vines climbing the walls."""
    g=f'<g transform="translate({x},{y}) scale({s})"><rect x="-70" y="-60" width="140" height="90" fill="#a89f91"/><path d="M-95,-55 L0,-140 L95,-55 Z" fill="#8c8070"/><path d="M10,-120 L40,-92 L18,-80 Z" fill="#6f6658"/>'
    g+='<path d="M-20,30 L-20,-20 Q0,-40 20,-20 L20,30 Z" fill="#4d4337"/>'
    g+='<path d="M-62,30 Q-80,-10 -58,-40 Q-44,-60 -60,-80" stroke="#556b2f" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M62,30 Q78,-6 56,-36" stroke="#556b2f" stroke-width="6" fill="none" stroke-linecap="round"/>'
    for lx,ly in ((-70,-6),(-56,-44),(-64,-74),(72,-4),(58,-30)): g+=f'<ellipse cx="{lx}" cy="{ly}" rx="9" ry="5" fill="#6b8e23"/>'
    return g+'</g>'
def flower_rain(n=22,seed=8,top=20,bottom=420):
    """Flowers falling from the sky as a blessing from the devas. The same seed always gives the same shower."""
    r=random.Random(seed); g=''
    for _ in range(n):
        x,y=r.randint(30,970),r.randint(top,bottom); c=r.choice(("#f1948a","#f8c471","#fdfefe","#f5b7b1","#f7dc6f"))
        for k in range(5):
            a=k*2*math.pi/5; g+=f'<circle cx="{x+7*math.cos(a):.0f}" cy="{y+7*math.sin(a):.0f}" r="6" fill="{c}"/>'
        g+=f'<circle cx="{x}" cy="{y}" r="4" fill="#d68910"/>'
    return g
def bg_old_hermitage():
    """A hermitage left empty for many years: dry grass, bare trees and a lonely hut."""
    g='<rect width="1000" height="860" fill="#d9d4c3"/><circle cx="160" cy="120" r="50" fill="#f4eed7"/>'
    g+='<path d="M380,470 Q560,170 760,200 Q900,230 1000,420 L1000,520 L380,520 Z" fill="#8f927a"/>'
    g+='<path d="M0,500 Q250,450 500,490 T1000,480 L1000,860 L0,860 Z" fill="#b5a978"/>'
    for tx,ty in ((620,300),(900,290)):
        g+=f'<path d="M{tx},{ty+200} L{tx},{ty} M{tx},{ty+60} L{tx-50},{ty+10} M{tx},{ty+40} L{tx+44},{ty-6} M{tx},{ty+100} L{tx+50},{ty+60}" stroke="#6e5a44" stroke-width="10" stroke-linecap="round" fill="none"/>'
    g+=old_hut(740,510,0.9)
    g+='<path d="M0,620 Q250,595 500,620 T1000,612 L1000,860 L0,860 Z" fill="#a39766"/>'
    for gx in range(30,1000,90): g+=f'<path d="M{gx-12},{700+(gx%4)*30} L{gx-4},{670+(gx%4)*30} M{gx},{700+(gx%4)*30} L{gx+2},{662+(gx%4)*30} M{gx+12},{700+(gx%4)*30} L{gx+8},{672+(gx%4)*30}" stroke="#8a7a4a" stroke-width="4" stroke-linecap="round"/>'
    return g

# ---- Added in Episode 9 ----
# King Janaka of Mithila, the wise rajarshi: white robe with a gold drape and a grey beard. Not Dasharatha, who is KING.
JANAKA=dict(robe="#fdfefe",drape="#f5b041",trim="#d4ac0d",beard="#aab7b8",beardlen=40,crown=True)
# Shatananda, Janaka's family priest and the eldest son of Gautama and Ahalya.
SHATANANDA=dict(robe="#f5b041",hair="#3b2414",beard="#3b2414",beardlen=45,topknot=True,trim="#a04000")
def kalash(x,y,s=1):
    """A brass water pot crowned with mango leaves and a coconut, used to welcome honoured guests. (x,y) is its base."""
    g=f'<g transform="translate({x},{y}) scale({s})">'
    for a in (-50,-25,25,50): g+=f'<ellipse cx="0" cy="-96" rx="9" ry="26" fill="#27ae60" transform="rotate({a},0,-78)"/>'
    g+='<circle cx="0" cy="-100" r="18" fill="#8d5524"/>'
    g+='<rect x="-16" y="-84" width="32" height="16" fill="#d4ac0d" stroke="#9a7d0a" stroke-width="2"/>'
    g+='<path d="M-20,-70 Q-48,-60 -46,-34 Q-42,0 0,0 Q42,0 46,-34 Q48,-60 20,-70 Z" fill="#d4ac0d" stroke="#9a7d0a" stroke-width="3"/>'
    g+='<path d="M-42,-40 Q0,-26 42,-40" stroke="#c0392b" stroke-width="5" fill="none"/>'
    return g+'</g>'
def mandap(x,y,s=1,c="#f5b7b1",roof="#c0392b"):
    """An open festival pavilion with four posts and a bright canopy, as at a great yajna. (x,y) is the middle of its floor."""
    g=f'<g transform="translate({x},{y}) scale({s})">'
    g+=f'<polygon points="-150,-180 150,-180 0,-270" fill="{roof}"/><line x1="0" y1="-270" x2="0" y2="-310" stroke="#7a4a1c" stroke-width="4"/><polygon points="0,-310 30,-300 0,-290" fill="#f1c40f"/>'
    for k in range(11): g+=f'<circle cx="{-150+k*30}" cy="-180" r="15" fill="{c}"/>'
    g+=f'<rect x="-150" y="-196" width="300" height="16" fill="{c}"/>'
    for px in (-125,-45,45,125): g+=f'<rect x="{px-8}" y="-180" width="16" height="180" fill="#e2b97a" stroke="#c9812a" stroke-width="2"/>'
    g+='<rect x="-150" y="-6" width="300" height="16" fill="#c9812a"/>'
    return g+'</g>'
def bg_mithila(sky="url(#day)",sun="#fff6c9"):
    """The great yajna grounds outside Mithila: bright pavilions, with Janaka's white palace far away. Pass sky="url(#dusk)" for evening."""
    g=f'<rect width="1000" height="860" fill="{sky}"/><circle cx="160" cy="130" r="52" fill="{sun}"/>'
    g+='<path d="M0,470 Q250,430 500,460 T1000,450 L1000,560 L0,560 Z" fill="#a8c686"/>'
    g+=palace(560,170,0.6,c1="#f8f1e4",c2="#efe1c6",c3="#d7bde2",dk="#8e6e53")
    g+='<path d="M0,530 Q250,500 500,525 T1000,515 L1000,860 L0,860 Z" fill="#9ccc65"/>'
    g+=mandap(130,560,0.6,"#f9e79f","#e67e22")+mandap(420,545,0.5,"#aed6f1","#1f618d")+mandap(880,560,0.62,"#f5b7b1","#c0392b")
    g+='<path d="M0,640 Q250,615 500,640 T1000,632 L1000,860 L0,860 Z" fill="#8cc084"/>'
    return g

# ---- Added in Episode 10 ----
# Kings from other lands who came to Mithila to try the great bow.
SUITOR=dict(robe="#6c3483",drape="#a569bd",beard="#2b1b12",beardlen=10,crown=True)
SUITOR2=dict(robe="#0e6655",drape="#48c9b0",beard="#5d4037",beardlen=20,crown=True)
# The strong men of Mithila who pulled the great bow's cart.
STRONGMAN=dict(robe="#ba4a00",skin="#a0522d",trim="#784212",hair="#2b1b12")
def great_bow(x,y,s=1,angle=0,strung=True,broken=False):
    """Lord Shiva's great bow: dark wood bound with gold, about 420 long at s=1. (x,y) is its middle grip; angle 0 stands it upright with the curve to the right.
    broken=True shows it snapped in two at the grip, the halves tipping apart with a burst of light."""
    def half(sign):
        p=f'<path d="M0,{sign*12} Q{60},{sign*110} 0,{sign*210}" stroke="#4a2c14" stroke-width="16" fill="none" stroke-linecap="round"/>'
        p+=f'<path d="M0,{sign*12} Q{60},{sign*110} 0,{sign*210}" stroke="#d4ac0d" stroke-width="5" stroke-dasharray="14 22" fill="none"/>'
        p+=f'<circle cx="0" cy="{sign*214}" r="12" fill="#f1c40f" stroke="#9a7d0a" stroke-width="3"/>'
        return p
    g=f'<g transform="translate({x},{y}) rotate({angle}) scale({s})">'
    if broken:
        g+='<circle r="80" fill="url(#glow)"/>'+spark(20,0,30,"#fffaf0")
        g+=f'<g transform="translate(-14,-8) rotate(-24)">{half(-1)}</g><g transform="translate(-14,8) rotate(24)">{half(1)}</g>'
        return g+'</g>'
    if strung: g+='<line x1="0" y1="-214" x2="0" y2="214" stroke="#fffaf0" stroke-width="3"/>'
    g+=half(-1)+half(1)+'<rect x="-6" y="-22" width="26" height="44" rx="8" fill="#c0392b" stroke="#7b241c" stroke-width="3"/>'
    return g+'</g>'
def bow_cart(x,y,s=1,bow=False):
    """The long iron chest on eight wheels that carried the great bow, seen side on. (x,y) is the ground under its middle.
    bow=True shows the lid open with the bow lying on top."""
    g=f'<g transform="translate({x},{y}) scale({s})">'
    if bow: g+=great_bow(0,-150,0.95,angle=-90,strung=False)
    g+='<rect x="-250" y="-150" width="500" height="90" rx="10" fill="#5d6d7e" stroke="#2c3e50" stroke-width="5"/>'
    g+='<rect x="-250" y="-150" width="500" height="16" fill="#d4ac0d"/><rect x="-250" y="-76" width="500" height="12" fill="#d4ac0d"/>'
    for bx in (-180,-60,60,180): g+=f'<circle cx="{bx}" cy="-105" r="10" fill="#d4ac0d" stroke="#9a7d0a" stroke-width="2"/>'
    for wx in (-200,-70,70,200): g+=f'<circle cx="{wx}" cy="-34" r="34" fill="#34495e" stroke="#1c2833" stroke-width="6"/><circle cx="{wx}" cy="-34" r="9" fill="#d4ac0d"/>'
    return g+'</g>'
def rope(x1,y1,x2,y2):
    """A thick pulling rope from (x1,y1) to (x2,y2), sagging a little."""
    return f'<path d="M{x1},{y1} Q{(x1+x2)/2:.0f},{max(y1,y2)+30:.0f} {x2},{y2}" stroke="#a0522d" stroke-width="8" fill="none" stroke-linecap="round"/>'
def plough(x,y,s=1,flip=False):
    """A golden plough for a royal yajna field, its blade cutting the earth at (x,y). Faces right; flip=True faces left."""
    g=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    g+='<line x1="0" y1="0" x2="230" y2="-70" stroke="#7a4a1c" stroke-width="12" stroke-linecap="round"/>'
    g+='<line x1="10" y1="-10" x2="-60" y2="-150" stroke="#7a4a1c" stroke-width="10" stroke-linecap="round"/><line x1="-75" y1="-150" x2="-45" y2="-150" stroke="#7a4a1c" stroke-width="10" stroke-linecap="round"/>'
    g+='<path d="M-10,-14 L34,-4 L10,18 Z" fill="#f1c40f" stroke="#b7950b" stroke-width="3"/>'
    return g+'</g>'
def baby(x,y,s=1,skin="#e8b98a",wrap="#fdebd0"):
    """A newborn baby wrapped in cloth, lying down. (x,y) is the middle of the bundle."""
    g=f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="12" cy="0" rx="46" ry="22" fill="{wrap}" stroke="#d4ac0d" stroke-width="3"/>'
    g+=f'<circle cx="-40" cy="-6" r="22" fill="{skin}"/><path d="M-50,-26 Q-40,-34 -30,-26" stroke="#2b1b12" stroke-width="4" fill="none" stroke-linecap="round"/>'
    g+='<path d="M-50,-8 Q-46,-12 -42,-8 M-36,-8 Q-32,-12 -28,-8" stroke="#2b1b12" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M-44,2 Q-38,7 -32,2" stroke="#2b1b12" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
    return g+'</g>'
def bg_field():
    """A freshly ploughed field outside Mithila, with furrows running across it and the white palace far away."""
    g='<rect width="1000" height="860" fill="url(#day)"/><circle cx="840" cy="120" r="52" fill="#fff6c9"/>'
    g+='<path d="M0,430 Q250,400 500,425 T1000,418 L1000,520 L0,520 Z" fill="#a8c686"/>'
    g+=palace(620,150,0.45,c1="#f8f1e4",c2="#efe1c6",c3="#d7bde2",dk="#8e6e53")
    g+='<path d="M0,500 Q250,480 500,500 T1000,494 L1000,860 L0,860 Z" fill="#a0703c"/>'
    for k in range(7):
        fy=540+k*48; g+=f'<path d="M0,{fy} Q500,{fy-14} 1000,{fy}" stroke="#7a4a1c" stroke-width="{4+k}" fill="none"/>'
    g+=tree(70,400,70,"#5b9a45")
    return g

# ---- Added in Episode 11 ----
# Princess Sita of Mithila, Janaka's daughter: deep pink robe with a soft pink drape and gold trim.
SITA=dict(robe="#c2185b",drape="#f8bbd0",trim="#f1c40f",skin="#d9a066",female=True,tiara=True)
# Royal messengers who carry a king's message to another kingdom.
MESSENGER=dict(robe="#7d6608",trim="#f4d03f",skin="#c68642",beard="#2b1b12",beardlen=0)
# King Dasharatha's ministers at the court of Ayodhya.
MINISTER=dict(robe="#566573",drape="#aab7b8",trim="#f4d03f",beard="#2b1b12",beardlen=20)

# ---- Added in Episode 12 ----
# King Kushadhvaja of Sankashya, Janaka's younger brother: cream robe with a teal drape and a brown beard.
KUSHADHVAJA=dict(robe="#fdebd0",drape="#48c9b0",trim="#d4ac0d",beard="#5d4037",beardlen=30,crown=True)
# Urmila, Janaka's younger daughter, who married Lakshmana.
URMILA=dict(robe="#d35400",drape="#f5cba7",trim="#f1c40f",skin="#d9a066",female=True,tiara=True)
# Mandavi and Shrutakirti, Kushadhvaja's daughters, who married Bharata and Shatrughna.
MANDAVI=dict(robe="#117864",drape="#a3e4d7",trim="#f1c40f",female=True,tiara=True)
SHRUTAKIRTI=dict(robe="#2471a3",drape="#aed6f1",trim="#f1c40f",female=True,tiara=True)
def cow(x,y,s=1,flip=False,c="#fdfefe",horns="#f1c40f"):
    """A gentle white cow with a hump and gold covered horns, standing side on and facing right (flip=True faces left). (x,y) is the middle of its body."""
    g=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    for lx in (-50,-30,34,54): g+=f'<rect x="{lx-7}" y="10" width="14" height="62" rx="6" fill="{c}" stroke="#a6acaf" stroke-width="2"/><rect x="{lx-8}" y="66" width="16" height="9" fill="#5d4037"/>'
    g+=f'<path d="M-76,-14 Q-100,20 -92,52" stroke="#a6acaf" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="-92" cy="56" r="7" fill="#5d4037"/>'
    g+=f'<ellipse cx="0" cy="0" rx="78" ry="38" fill="{c}" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<path d="M30,-34 Q46,-62 64,-34 Z" fill="{c}" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<path d="M60,-6 Q70,30 94,22 L92,-10 Z" fill="#ecf0f1" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<path d="M80,-12 Q112,-40 120,-18 L120,14 Q110,28 96,18 Z" fill="{c}" stroke="#a6acaf" stroke-width="2"/>'
    g+=f'<path d="M96,-28 Q88,-56 100,-64" stroke="{horns}" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M110,-30 Q114,-58 128,-62" stroke="{horns}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    g+='<ellipse cx="86" cy="-20" rx="12" ry="6" fill="#d5d8dc"/><circle cx="110" cy="-14" r="4.5" fill="#2b1b12"/><ellipse cx="118" cy="10" rx="6" ry="5" fill="#f5b7b1"/>'
    g+='<path d="M60,-30 Q74,-6 62,14" stroke="#c0392b" stroke-width="6" fill="none"/><circle cx="64" cy="18" r="7" fill="#f1c40f"/>'
    return g+'</g>'

# ---- Added in Episode 13 ----
# (person() also gained mood="stern": a straight mouth and firm brows, for a fierce but dignified face.)
# Sage Parashurama, son of Jamadagni: deerskin tan robe with a rust drape, black matted locks and beard.
# He is honoured as an avatar of Lord Vishnu. Draw him with parashurama(), never only person().
PARASHURAMA=dict(robe="#a9744f",drape="#ba4a00",trim="#6e2c00",hair="#1c1c1c",beard="#1c1c1c",beardlen=55,topknot=True)
def parashu(x,y,s=1,angle=0):
    """Parashurama's axe: a long wooden handle with a broad steel blade. (x,y) is the foot of the handle; angle 0 stands it upright."""
    g=f'<g transform="translate({x},{y}) rotate({angle}) scale({s})">'
    g+='<line x1="0" y1="0" x2="0" y2="-190" stroke="#6e3b14" stroke-width="10" stroke-linecap="round"/>'
    g+='<path d="M4,-186 Q50,-200 62,-158 Q48,-138 4,-142 Z" fill="#aab7b8" stroke="#566573" stroke-width="3"/><path d="M58,-188 Q72,-160 58,-132" stroke="#fdfefe" stroke-width="3" fill="none"/>'
    g+='<rect x="-7" y="-196" width="14" height="22" rx="3" fill="#d4ac0d"/>'
    return g+'</g>'
def parashurama(x,y,s=1,arms="down",mood="stern",flip=False,axe=True):
    """Sage Parashurama with his tall jata and his axe resting on his shoulder. Always shown with dignity."""
    g=person(x,y,s,arms=arms,mood=mood,flip=flip,**PARASHURAMA)
    g+=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})"><ellipse cx="0" cy="-92" rx="17" ry="24" fill="#1c1c1c"/><path d="M-10,-104 Q0,-114 10,-104" stroke="#5d4037" stroke-width="3" fill="none"/>'
    g+='<path d="M-20,2 Q0,40 20,2" stroke="#7b241c" stroke-width="5" fill="none" stroke-dasharray="2 7" stroke-linecap="round"/>'
    if axe: g+=f'<g transform="scale(-1,1)">{parashu(50,72,1,angle=8)}</g>'
    return g+'</g>'
def vishnu_bow(x,y,s=1,angle=0,strung=True,arrowed=False):
    """The divine bow of Lord Vishnu: deep blue wood bound with gold, about 340 long at s=1. (x,y) is its grip; angle 0 stands it upright with the curve to the right.
    arrowed=True fits a golden arrow on the string, pointing the way the curve faces."""
    def half(sign):
        p=f'<path d="M0,{sign*12} Q55,{sign*90} 0,{sign*170}" stroke="#1a5276" stroke-width="14" fill="none" stroke-linecap="round"/>'
        p+=f'<path d="M0,{sign*12} Q55,{sign*90} 0,{sign*170}" stroke="#f4d03f" stroke-width="4" stroke-dasharray="10 16" fill="none"/>'
        return p+f'<circle cx="0" cy="{sign*174}" r="10" fill="#f1c40f" stroke="#9a7d0a" stroke-width="3"/>'
    g=f'<g transform="translate({x},{y}) rotate({angle}) scale({s})">'
    if arrowed:
        g+='<path d="M-60,0 L0,-160 M-60,0 L0,160" stroke="#fffaf0" stroke-width="3"/>'
    elif strung: g+='<line x1="0" y1="-174" x2="0" y2="174" stroke="#fffaf0" stroke-width="3"/>'
    g+=half(-1)+half(1)+'<rect x="-6" y="-20" width="24" height="40" rx="8" fill="#f1c40f" stroke="#9a7d0a" stroke-width="3"/>'
    if arrowed:
        g+='<circle cx="120" cy="0" r="40" fill="url(#glow)"/><line x1="-60" y1="0" x2="130" y2="0" stroke="#d4ac0d" stroke-width="7" stroke-linecap="round"/>'
        g+='<polygon points="160,0 126,-14 126,14" fill="#f1c40f" stroke="#b7950b" stroke-width="2"/><path d="M-60,0 L-80,-14 L-70,0 L-80,14 Z" fill="#f39c12"/>'
    return g+'</g>'
def bird(x,y,s=1,flip=False,c="#2c3e50",crying=False):
    """A dark bird flying, facing right (flip=True faces left). crying=True opens its beak to call out."""
    g=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    g+=f'<path d="M-6,-4 Q-30,-40 -60,-34 Q-36,-20 -18,4 Z" fill="{c}"/><path d="M6,-4 Q-4,-44 26,-56 Q20,-24 14,4 Z" fill="{c}"/>'
    g+=f'<ellipse cx="0" cy="2" rx="30" ry="12" fill="{c}"/><circle cx="30" cy="-4" r="10" fill="{c}"/><polygon points="-30,0 -48,-8 -46,12" fill="{c}"/><circle cx="33" cy="-7" r="2.5" fill="#fdfefe"/>'
    g+=('<polygon points="38,-8 54,-14 40,-3" fill="#f39c12"/><polygon points="38,-1 52,6 38,2" fill="#f39c12"/>' if crying else '<polygon points="38,-6 52,-2 38,1" fill="#f39c12"/>')
    return g+'</g>'
def deer(x,y,s=1,flip=False):
    """A gentle spotted deer walking calmly, facing right (flip=True faces left). (x,y) is the middle of its body."""
    g=f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})">'
    for lx,a in ((-40,6),(-26,-6),(30,6),(44,-6)): g+=f'<line x1="{lx}" y1="10" x2="{lx+a}" y2="78" stroke="#b9770e" stroke-width="9" stroke-linecap="round"/>'
    g+='<path d="M-58,-10 Q-74,-24 -66,-34" stroke="#b9770e" stroke-width="8" fill="none" stroke-linecap="round"/>'
    g+='<ellipse cx="0" cy="0" rx="62" ry="28" fill="#d68910"/><path d="M-40,14 Q0,30 40,14" stroke="#fdebd0" stroke-width="6" fill="none"/>'
    for sx,sy in ((-30,-8),(-10,-14),(10,-6),(28,-14),(-18,6),(20,8)): g+=f'<circle cx="{sx}" cy="{sy}" r="4" fill="#fdebd0"/>'
    g+='<path d="M40,-14 L62,-62 L80,-56 L62,-6 Z" fill="#d68910"/><ellipse cx="80" cy="-64" rx="22" ry="13" fill="#d68910"/>'
    g+='<path d="M66,-74 L58,-108 M62,-92 L48,-100 M78,-76 L82,-110 M80,-96 L94,-104" stroke="#7a4a1c" stroke-width="4" stroke-linecap="round"/>'
    g+='<ellipse cx="64" cy="-78" rx="5" ry="10" fill="#b9770e" transform="rotate(-30,64,-78)"/><circle cx="84" cy="-68" r="3.5" fill="#2b1b12"/><circle cx="100" cy="-62" r="3.5" fill="#2b1b12"/>'
    return g+'</g>'
def bg_storm():
    """The road home under a sudden storm: a dark sky, a dim sun hidden by dust, and trees bent by the wind."""
    g='<rect width="1000" height="860" fill="#4d4660"/><circle cx="500" cy="300" r="90" fill="#d5c4a1" opacity="0.35"/>'
    g+='<path d="M0,470 Q180,380 380,450 Q520,390 700,440 Q860,380 1000,460 L1000,860 L0,860 Z" fill="#6d6455"/>'
    g+='<path d="M0,560 Q250,520 500,550 T1000,540 L1000,860 L0,860 Z" fill="#5f7350"/><polygon points="470,548 530,548 760,860 240,860" fill="#a8977a"/>'
    for tx,ty in ((90,420),(900,430)):
        g+=f'<path d="M{tx},{ty+150} Q{tx+10},{ty+60} {tx+40},{ty}" stroke="#4a3520" stroke-width="20" fill="none" stroke-linecap="round"/>'
        g+=f'<ellipse cx="{tx+70}" cy="{ty-10}" rx="80" ry="48" fill="#3f5a36"/><ellipse cx="{tx+130}" cy="{ty+10}" rx="44" ry="26" fill="#3f5a36"/>'
    g+=dust(240,250,90)+dust(760,220,100)+dust(500,120,70)
    return g

# ---- Card layouts. These define the look of the series. ----
def blogcard(scene):
    """Picture only, for the blog. The caption is real text under the image."""
    return '\n'.join([f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="940" viewBox="0 0 1080 940">',DEFS,
        '<rect width="1080" height="940" fill="#fdf6e3"/>',
        f'<clipPath id="clip"><rect x="40" y="40" width="1000" height="860" rx="24"/></clipPath><g clip-path="url(#clip)"><g transform="translate(40,40)">{scene}</g></g>',
        f'<rect x="40" y="40" width="1000" height="860" rx="24" fill="none" stroke="{INK}" stroke-width="6"/></svg>'])
def socialcard(n,total,scene,caption,ep):
    """Picture with caption, for Instagram, Facebook and WhatsApp."""
    P=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,f'<rect width="{W}" height="{H}" fill="#fdf6e3"/>',f'<rect width="{W}" height="100" fill="url(#band)"/>']
    P.append(T(40,40,[SERIES],20,"#f1c40f","700")+T(40,80,[ep["title"]],32,"#fff","700")+T(1040,40,[f'{ep["book"]}, Episode {ep["number"]}'],20,"#f5cba7","600","end"))
    P.append(f'<clipPath id="clip"><rect x="40" y="125" width="1000" height="860" rx="24"/></clipPath><g clip-path="url(#clip)"><g transform="translate(40,125)">{scene}</g></g><rect x="40" y="125" width="1000" height="860" rx="24" fill="none" stroke="{INK}" stroke-width="6"/>')
    P.append('<rect x="40" y="1010" width="1000" height="260" rx="20" fill="#fffaf0" stroke="#d4ac0d" stroke-width="4"/>')
    lines=textwrap.wrap(caption,46); size=36 if len(lines)<=4 else 31; lh=1.32
    if size==31: lines=textwrap.wrap(caption,54)
    y0=1140-(len(lines)-1)*size*lh/2+size*0.35
    P.append(T(540,round(y0),lines,size,INK,"500","middle",lh))
    P.append(''.join(f'<circle cx="{540+(i-(total-1)/2)*26}" cy="1312" r="{8 if i==n-1 else 5}" fill="{"#7b241c" if i==n-1 else "#d5c4a1"}"/>' for i in range(total))+'</svg>')
    return '\n'.join(P)
def valuecard(ep):
    """Closing card: today's value, a short lesson and a question to talk about."""
    P=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,f'<rect width="{W}" height="{H}" fill="#7b241c"/><rect x="30" y="30" width="1020" height="1290" rx="30" fill="none" stroke="#f1c40f" stroke-width="5"/>']
    P.append('<g transform="translate(0,-70)"><circle cx="540" cy="300" r="230" fill="url(#glow)" opacity="0.6"/><path d="M540,190 Q485,280 540,335 Q595,280 540,190 Z" fill="#f39c12"/><path d="M540,245 Q515,295 540,325 Q565,295 540,245 Z" fill="#f9e79f"/><path d="M420,335 Q540,470 660,335 Z" fill="#c9812a"/><path d="M420,335 Q540,372 660,335 Q540,318 420,335 Z" fill="#e8a33d"/><path d="M650,338 L700,322 L690,350 Z" fill="#c9812a"/></g>')
    P.append(T(540,470,["TODAY'S VALUE"],30,"#f1c40f","800","middle"))
    P.append(T(540,560,[ep["value_name"]],84 if len(ep["value_name"])<=11 else 62,"#fff","800","middle"))
    P.append(T(540,612,[ep["value_meaning"]],32,"#f5cba7","500","middle"))
    P.append(T(540,700,textwrap.wrap(ep["card_lesson"],40),36,"#fff","500","middle",1.38))
    P.append('<line x1="340" y1="1000" x2="740" y2="1000" stroke="#f1c40f" stroke-width="3"/>')
    P.append(T(540,1050,["TALK ABOUT IT"],24,"#f1c40f","800","middle"))
    P.append(T(540,1098,textwrap.wrap(ep["question"],50),28,"#fff","500","middle",1.35))
    P.append(T(540,1262,[SERIES],24,"#f1c40f","800","middle")+T(540,1294,["A new story every day"],22,"#f5cba7","500","middle")+'</svg>')
    return '\n'.join(P)

def _render(svg,path):
    tmp=path.with_suffix('.svg'); tmp.write_text(svg)
    subprocess.run(['rsvg-convert',str(tmp),'-o',str(path)],check=True); tmp.unlink()
def build(epdir,preview=None):
    """Render one episode folder: blog pictures, social cards and the value card."""
    epdir=pathlib.Path(epdir); ep=json.loads((epdir/'episode.json').read_text())
    spec=importlib.util.spec_from_file_location(f'scenes_{epdir.name}',epdir/'scenes.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    assert len(mod.SCENES)==len(ep['captions'])==7, 'An episode has exactly 7 scenes and 7 captions'
    for k in ('value_name','value_meaning','lesson','card_lesson','question','next'): assert ep.get(k), f'episode.json is missing {k}'
    assert len(textwrap.wrap(ep['card_lesson'],40))<=6 and len(textwrap.wrap(ep['question'],50))<=4, 'card_lesson or question is too long for the value card'
    (epdir/'social').mkdir(exist_ok=True); total=8
    for i,(fn,cap) in enumerate(zip(mod.SCENES,ep['captions']),1):
        assert len(textwrap.wrap(cap,54))<=5, f'caption {i} is too long'
        scene=fn(); _render(blogcard(scene),epdir/f'{i:02d}.png'); _render(socialcard(i,total,scene,cap,ep),epdir/'social'/f'{i:02d}.png')
    _render(valuecard(ep),epdir/'social'/'08.png')
    if preview:
        from PIL import Image
        ims=[Image.open(epdir/'social'/f'{i:02d}.png').convert('RGB') for i in range(1,9)]
        sh=Image.new('RGB',(4*540+50,2*675+30),'#ffffff')
        for k,im in enumerate(ims): sh.paste(im.resize((540,675)),(10+(k%4)*550,10+(k//4)*685))
        sh.save(preview)
