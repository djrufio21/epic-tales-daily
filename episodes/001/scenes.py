from epic import *

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


SCENES=[s1,s2,s3,s4,s5,s6,s7]
