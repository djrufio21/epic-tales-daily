import textwrap, subprocess, random, math
W,H=1080,1350
FONT="Inter, DejaVu Sans, sans-serif"
SERIES="EPIC TALES DAILY"; BOOK="Ramayana, Episode 1"; TITLE="The King Who Longed for a Child"
INK="#3b2414"

def T(x,y,lines,size=20,fill=INK,weight="400",anchor="start",lh=1.3):
    o=f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">'
    for i,l in enumerate(lines): o+=f'<tspan x="{x}" dy="{0 if i==0 else size*lh}">{l}</tspan>'
    return o+'</text>'

def person(x,y,s=1,robe="#1f618d",skin="#c68642",trim="#f1c40f",hair="#2b1b12",crown=False,beard=None,beardlen=30,mood="smile",topknot=False,female=False,drape=None,arms="down",tiara=False,flip=False):
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
    g+='<circle cx="-12" cy="-40" r="4" fill="#2b1b12"/><circle cx="12" cy="-40" r="4" fill="#2b1b12"/>'
    if mood=="sad": g+='<path d="M-9,-20 Q0,-28 9,-20" stroke="#2b1b12" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M-19,-48 L-7,-53 M7,-53 L19,-48" stroke="#2b1b12" stroke-width="3" stroke-linecap="round"/>'
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
</defs>'''

def s1():
    g='<rect width="1000" height="860" fill="url(#sunrise)"/><circle cx="770" cy="300" r="180" fill="url(#glow)"/><circle cx="770" cy="300" r="105" fill="#fff6c9"/>'
    g+='<path d="M0,560 Q220,470 440,545 T1000,520 L1000,700 L0,700 Z" fill="#d9b86c"/>'
    for bx,by in ((140,200),(240,150),(560,170)): g+=f'<path d="M{bx},{by} q14,-14 28,0 q14,-14 28,0" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    g+=palace(178,135,1.15)+'<rect y="640" width="1000" height="60" fill="#7fb069"/>'
    g+=tree(90,560,60)+tree(915,555,66)
    g+='<rect y="700" width="1000" height="160" fill="url(#river)"/>'
    for wx,wy in ((80,740),(420,725),(820,750),(300,820),(600,840),(900,815)): g+=f'<path d="M{wx},{wy} q20,-10 40,0 q20,10 40,0" stroke="#fff" stroke-width="4" fill="none" opacity="0.55" stroke-linecap="round"/>'
    for bx,by,c in ((230,775,"#c0392b"),(700,800,"#fffaf0")):
        g+=f'<g transform="translate({bx},{by})"><line x1="0" y1="0" x2="0" y2="-80" stroke="{INK}" stroke-width="4"/><polygon points="4,-78 4,-14 52,-14" fill="{c}"/><path d="M-60,0 L60,0 L44,26 L-44,26 Z" fill="#7a4a1c"/></g>'
    return g
def s2():
    g='<rect width="1000" height="860" fill="#f6d9a8"/>'
    for cx in (200,500,800): g+=f'<path d="M{cx-110},640 L{cx-110},300 Q{cx},140 {cx+110},300 L{cx+110},640 Z" fill="#edc88e"/>'
    for px in (45,335,635,925): g+=f'<rect x="{px}" y="90" width="30" height="550" fill="#e2b97a"/><rect x="{px-8}" y="90" width="46" height="18" fill="#c9812a"/>'
    for k in range(5):
        x0=k*200; g+=f'<path d="M{x0},40 Q{x0+100},110 {x0+200},40" stroke="#27ae60" stroke-width="5" fill="none"/>'
        for j in range(1,6):
            t=j/6; g+=f'<circle cx="{x0+200*t:.0f}" cy="{40+140*t*(1-t):.0f}" r="10" fill="{"#e67e22" if j%2 else "#f1c40f"}"/>'
    g+='<rect y="640" width="1000" height="220" fill="#a0522d"/><polygon points="380,640 620,640 730,860 270,860" fill="#8e2f2f"/><polygon points="380,640 392,640 290,860 270,860" fill="#f1c40f"/><polygon points="608,640 620,640 730,860 710,860" fill="#f1c40f"/>'
    g+='<rect x="370" y="600" width="260" height="42" rx="6" fill="#c9812a"/>'
    g+=person(500,400,1.9,arms="up2",**KING)
    g+=person(190,500,1.6,robe="#27ae60",arms="hold")+basket(190,500+52*1.6,1.6)
    g+=person(810,500,1.6,robe="#d35400",female=True,drape="#f5b041",arms="hold")+basket(810,500+52*1.6,1.6)
    g+=person(300,545,1.5,robe="#8e44ad",female=True,drape="#c39bd3",arms="up2")
    g+=person(700,545,1.5,robe="#16a085",arms="up2",beard="#2b1b12",beardlen=10)
    return g
def s3():
    R=random.Random(7)
    g='<rect width="1000" height="860" fill="url(#night)"/>'
    for _ in range(40): g+=f'<circle cx="{R.randint(10,990)}" cy="{R.randint(10,430)}" r="{R.choice((2,2,3,4))}" fill="#fff" opacity="{R.choice((0.6,0.8,1))}"/>'
    g+='<circle cx="790" cy="170" r="150" fill="url(#glow)" opacity="0.5"/><circle cx="790" cy="170" r="72" fill="#fdf3c4"/><circle cx="765" cy="150" r="12" fill="#f0e2a0"/><circle cx="812" cy="195" r="9" fill="#f0e2a0"/>'
    g+=palace(560,235,0.75,"#1b2a52","#18254a","#152043","#0f1b3d",flags=False)
    g+='<rect y="620" width="1000" height="240" fill="#b8ad9e"/><rect y="470" width="1000" height="24" fill="#d8cfc2"/><rect y="596" width="1000" height="24" fill="#d8cfc2"/>'
    for bx in range(20,1000,64): g+=f'<rect x="{bx}" y="494" width="20" height="102" rx="8" fill="#cfc6b8"/>'
    g+='<ellipse cx="690" cy="835" rx="170" ry="18" fill="#000" opacity="0.15"/><ellipse cx="300" cy="725" rx="110" ry="14" fill="#000" opacity="0.15"/>'
    g+=person(300,470,2.1,mood="sad",**KING)+cradle(690,640,2.4)
    return g
def s4():
    g='<rect width="1000" height="860" fill="#cdeaf7"/><circle cx="150" cy="130" r="60" fill="#fff6c9"/>'
    for cx,cy in ((420,120),(480,110),(540,125),(800,180),(850,170)): g+=f'<circle cx="{cx}" cy="{cy}" r="36" fill="#fff" opacity="0.9"/>'
    g+='<path d="M0,520 Q250,460 500,510 T1000,500 L1000,860 L0,860 Z" fill="#9ccc65"/>'
    g+=tree(80,330,90)+tree(900,320,100,"#5b9a45")+tree(500,360,70,"#7cb866")
    for fx,fy,c in ((60,640,"#e74c3c"),(120,690,"#f1c40f"),(900,650,"#e84393"),(950,700,"#f39c12"),(840,720,"#e74c3c"),(160,750,"#e84393")):
        g+=f'<circle cx="{fx}" cy="{fy}" r="26" fill="#5b9a45"/><circle cx="{fx-8}" cy="{fy-6}" r="7" fill="{c}"/><circle cx="{fx+9}" cy="{fy+4}" r="7" fill="{c}"/>'
    g+='<ellipse cx="500" cy="790" rx="230" ry="48" fill="#5dade2"/>'
    for lx,ly in ((430,780),(570,798)): g+=f'<ellipse cx="{lx}" cy="{ly+6}" rx="26" ry="8" fill="#27ae60"/><ellipse cx="{lx-9}" cy="{ly-4}" rx="7" ry="13" fill="#f5a9c8" transform="rotate(-25 {lx-9} {ly-4})"/><ellipse cx="{lx+9}" cy="{ly-4}" rx="7" ry="13" fill="#f5a9c8" transform="rotate(25 {lx+9} {ly-4})"/><ellipse cx="{lx}" cy="{ly-7}" rx="7" ry="14" fill="#f8c8dc"/>'
    g+=person(300,440,2.0,**KING)+person(690,440,2.0,arms="raise",flip=True,**SAGE)
    return g
def s5():
    g='<rect width="1000" height="860" fill="url(#dusk)"/><rect y="380" width="1000" height="240" fill="#7a4a3a"/>'
    for cx in (120,330,670,880): g+=f'<path d="M{cx-70},620 L{cx-70},480 Q{cx},400 {cx+70},480 L{cx+70},620 Z" fill="#5e372b"/>'
    g+='<rect y="620" width="1000" height="240" fill="#c9b78e"/><circle cx="500" cy="300" r="330" fill="url(#glow)"/>'
    for k in range(16):
        a=math.pi*2*k/16; g+=f'<line x1="{500+175*math.cos(a):.0f}" y1="{240+175*math.sin(a):.0f}" x2="{500+250*math.cos(a):.0f}" y2="{240+250*math.sin(a):.0f}" stroke="#fff6c9" stroke-width="7" stroke-linecap="round" opacity="0.75"/>'
    g+=person(500,250,1.5,robe="#f4d03f",skin="#fbe6a2",hair="#d4ac0d",trim="#fffaf0",arms="hold")+bowl(500,250+50*1.5,1.5)
    g+='<path d="M500,650 Q360,560 440,460 Q470,520 500,395 Q560,500 575,465 Q660,575 500,650 Z" fill="#e67e22"/><path d="M500,650 Q420,585 478,520 Q500,560 512,480 Q580,575 500,650 Z" fill="#f9e79f"/>'
    g+='<rect x="400" y="640" width="200" height="70" fill="#8d5524"/><rect x="370" y="710" width="260" height="30" fill="#7a4a1c"/>'
    for bx in (450,500,550): g+=f'<line x1="{bx}" y1="640" x2="{bx}" y2="710" stroke="#7a4a1c" stroke-width="3"/>'
    g+=person(190,500,1.7,arms="up2",**KING)
    g+=person(905,515,1.4,robe="#e67e22",trim="#b9770e",topknot=True,arms="up2")+person(790,555,1.5,arms="raise",flip=True,**SAGE)
    return g
def s6():
    g='<rect width="1000" height="860" fill="#f6d9a8"/>'
    for px in (40,930): g+=f'<rect x="{px}" y="0" width="30" height="660" fill="#e2b97a"/>'
    g+='<path d="M380,660 L380,260 Q500,110 620,260 L620,660 Z" fill="#cdeaf7"/><path d="M380,660 L380,260 Q500,110 620,260 L620,660" stroke="#c9812a" stroke-width="14" fill="none"/><circle cx="560" cy="300" r="34" fill="#fff6c9"/>'
    g+='<path d="M0,0 L330,0 Q250,90 120,110 Q60,200 0,230 Z" fill="#8e2f2f"/><path d="M1000,0 L670,0 Q750,90 880,110 Q940,200 1000,230 Z" fill="#8e2f2f"/>'
    g+='<rect y="660" width="1000" height="200" fill="#a0522d"/><ellipse cx="500" cy="760" rx="440" ry="70" fill="#8e2f2f"/><ellipse cx="500" cy="760" rx="440" ry="70" fill="none" stroke="#f1c40f" stroke-width="5"/>'
    g+=person(200,440,2.0,arms="hold",**KING)+bowl(200,440+50*2,2.0)
    for sx,sy in ((120,470),(290,500),(150,600),(275,585)): g+=spark(sx,sy,13)
    for qx,q in ((480,Q1),(670,Q2),(860,Q3)): g+=person(qx,460,1.85,**q)
    for lx,n in ((200,"King Dasharatha"),(480,"Kausalya"),(670,"Kaikeyi"),(860,"Sumitra")): g+=T(lx,770,[n],24,"#fffaf0","700","middle")
    return g
def s7():
    R=random.Random(3); cols=["#c0392b","#f1c40f","#1f618d","#27ae60","#e67e22"]
    g='<rect width="1000" height="860" fill="#fdebd0"/>'
    for cx in (200,500,800): g+=f'<path d="M{cx-120},500 L{cx-120},260 Q{cx},120 {cx+120},260 L{cx+120},500 Z" fill="#fbdcb4"/>'
    g+=bunting(20,45)
    for _ in range(40): g+=f'<circle cx="{R.randint(20,980)}" cy="{R.randint(110,480)}" r="7" fill="{R.choice(cols)}"/>'
    g+='<rect y="500" width="1000" height="360" fill="#e8c9a0"/>'
    g+=person(200,330,1.55,arms="up2",**Q1)+person(400,330,1.55,arms="up2",**KING)+person(600,330,1.55,arms="up2",**Q2)+person(800,330,1.55,arms="up2",**Q3)
    for cx,n,sk,bl in ((140,"Rama","#7fb3d5","#f1c40f"),(380,"Bharata","#c68642","#27ae60"),(620,"Lakshmana","#d49a5b","#c0392b"),(860,"Shatrughna","#c68642","#8e44ad")):
        g+=cradle(cx,640,1.7,sk,bl)+T(cx,828,[n],28,INK,"700","middle")
    return g

def card(n,total,scene,caption):
    P=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,f'<rect width="{W}" height="{H}" fill="#fdf6e3"/>',f'<rect width="{W}" height="100" fill="url(#band)"/>']
    P.append(T(40,40,[SERIES],20,"#f1c40f","700")+T(40,80,[TITLE],32,"#fff","700")+T(1040,40,[BOOK],20,"#f5cba7","600","end"))
    P.append(f'<clipPath id="clip"><rect x="40" y="125" width="1000" height="860" rx="24"/></clipPath><g clip-path="url(#clip)"><g transform="translate(40,125)">{scene}</g></g><rect x="40" y="125" width="1000" height="860" rx="24" fill="none" stroke="{INK}" stroke-width="6"/>')
    P.append('<rect x="40" y="1010" width="1000" height="260" rx="20" fill="#fffaf0" stroke="#d4ac0d" stroke-width="4"/>')
    lines=textwrap.wrap(caption,46); size=36; lh=1.32
    y0=1140-(len(lines)-1)*size*lh/2+size*0.35
    P.append(T(540,round(y0),lines,size,INK,"500","middle",lh))
    dots=''.join(f'<circle cx="{540+(i-(total-1)/2)*26}" cy="1312" r="{8 if i==n-1 else 5}" fill="{"#7b241c" if i==n-1 else "#d5c4a1"}"/>' for i in range(total))
    P.append(dots+'</svg>')
    return '\n'.join(P)
def lastcard(total):
    P=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS,f'<rect width="{W}" height="{H}" fill="#7b241c"/><rect x="30" y="30" width="1020" height="1290" rx="30" fill="none" stroke="#f1c40f" stroke-width="5"/>']
    P.append('<circle cx="540" cy="300" r="230" fill="url(#glow)" opacity="0.6"/><path d="M540,190 Q485,280 540,335 Q595,280 540,190 Z" fill="#f39c12"/><path d="M540,245 Q515,295 540,325 Q565,295 540,245 Z" fill="#f9e79f"/><path d="M420,335 Q540,470 660,335 Z" fill="#c9812a"/><path d="M420,335 Q540,372 660,335 Q540,318 420,335 Z" fill="#e8a33d"/><path d="M650,338 L700,322 L690,350 Z" fill="#c9812a"/>')
    P.append(T(540,560,["TODAY'S TAKEAWAY"],34,"#f1c40f","800","middle"))
    P.append(T(540,660,textwrap.wrap("Even a great king could not do everything alone. When something matters, ask for wise advice, do your part, and be patient.",30),48,"#fff","600","middle",1.35))
    P.append('<line x1="340" y1="1010" x2="740" y2="1010" stroke="#f1c40f" stroke-width="3"/>')
    P.append(T(540,1080,["Next episode"],26,"#f5cba7","600","middle")+T(540,1135,["The Four Princes Grow Up"],40,"#fff","700","middle"))
    P.append(T(540,1235,[SERIES],26,"#f1c40f","800","middle")+T(540,1275,["A new story three times a week"],24,"#f5cba7","500","middle")+'</svg>')
    return '\n'.join(P)

EP=[(s1,"Long ago, on the banks of the river Sarayu, stood the golden city of Ayodhya."),
(s2,"Its king, Dasharatha, was brave and fair. His people loved him, and the kingdom had everything it needed."),
(s3,"But the king carried one sorrow. He had no child, and no heir to care for Ayodhya after him."),
(s4,"His teacher, the sage Vasishtha, told him: “Do not lose hope. Hold a sacred fire ceremony and pray with a true heart.”"),
(s5,"The fire blazed, and from it rose a shining messenger carrying a golden bowl of blessed sweet rice."),
(s6,"The king shared the gift among his three queens: Kausalya, Kaikeyi and Sumitra."),
(s7,"In time, four princes were born. All of Ayodhya rejoiced!")]
total=len(EP)+1
for i,(fn,cap) in enumerate(EP,1):
    open(f'ep1/ep1_{i:02d}.svg','w').write(card(i,total,fn(),cap))
open(f'ep1/ep1_{total:02d}.svg','w').write(lastcard(total))
for i in range(1,total+1):
    subprocess.run(['rsvg-convert',f'ep1/ep1_{i:02d}.svg','-o',f'ep1/ep1_{i:02d}.png'],check=True)
try:
    from PIL import Image
    ims=[Image.open(f'ep1/ep1_{i:02d}.png').convert('RGB') for i in range(1,total+1)]
    sh=Image.new('RGB',(4*540+50,2*675+30),'#ffffff')
    for k,im in enumerate(ims): sh.paste(im.resize((540,675)),(10+(k%4)*550,10+(k//4)*685))
    sh.save('ep1/preview.png'); print('sheet ok')
except Exception as e: print('no sheet',e)
