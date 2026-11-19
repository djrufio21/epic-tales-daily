from epic import *

def s1():
    g=bg_hermitage()
    g+=staff(200,720,300)+person(140,500,1.6,arms="raise",**VISHVAMITRA)
    g+=person(380,540,1.4,**RAMA)+person(540,570,1.25,**LAKSHMANA)
    return g
def s2():
    g=bg_hermitage(huts=True)
    g+=altar(500,760,1.1)
    g+=person(200,560,1.4,arms="hold",**VISHVAMITRA)
    for sx in (760,900): g+=person(sx,560,1.15,arms="hold",**HERMIT)
    return g
def s3():
    g=bg_hermitage()
    g+=person(170,560,1.4,arms="raise",**HERMIT)
    g+=person(430,520,1.45,**RAMA)+person(620,550,1.3,**LAKSHMANA)
    g+=altar(860,780,0.8)
    return g
def s4():
    g=bg_hermitage_night()
    g+=altar(500,780,1.0)
    g+=person(220,520,1.5,**RAMA)+bow(220+47*1.5,520+66*1.5-60,1.1)
    g+=person(790,520,1.5,flip=True,**LAKSHMANA)+bow(790-47*1.5,520+66*1.5-60,1.1,flip=True)
    return g
def s5():
    g='<rect width="1000" height="860" fill="url(#dusk)"/><path d="M0,620 Q250,595 500,620 T1000,612 L1000,860 L0,860 Z" fill="#5d6b3a"/>'
    g+=demon(620,180,1.3)+demon(800,240,1.0)+demon(420,150,0.8)+demon(920,120,0.7)
    g+=soundwaves(700,330,1.0)+soundwaves(560,330,1.0,flip=True)
    g+=altar(500,800,1.25)
    g+=person(170,560,1.4,arms="raise",**RAMA)+bow(170+62*1.4,560-22*1.4,1.2)
    g+=person(850,580,1.3,arms="raise",flip=True,**LAKSHMANA)+bow(850-62*1.3,580-22*1.3,1.1,flip=True)
    return g
def s6():
    g='<rect width="1000" height="860" fill="url(#dusk)"/>'
    g+='<rect y="430" width="1000" height="80" fill="url(#river)"/>'
    g+='<path d="M0,560 Q250,520 500,550 T1000,540 L1000,860 L0,860 Z" fill="#5d6b3a"/>'
    g+=trail(560,300,900,400)
    g+=f'<g transform="rotate(60,900,400)">{demon(900,400,0.45)}</g>'
    g+=astra(470,320,0.8,angle=60)
    g+=person(200,560,1.6,arms="raise",**RAMA)+bow(200+62*1.6,560-22*1.6,1.4)
    return g
def s7():
    g=bg_hermitage()
    g+=wind(700,170,0.8)
    g+=demon(880,110,0.45)+demon(930,220,0.38)
    g+=demon_falling(640,250,0.75,40)
    g+=altar(470,790,0.85)
    g+=staff(170,720,300)+person(110,500,1.6,arms="raise",**VISHVAMITRA)
    g+=person(310,540,1.4,**RAMA)+person(640,570,1.25,**LAKSHMANA)
    g+=person(850,580,1.15,arms="hold",flip=True,**HERMIT)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
