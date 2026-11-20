from epic import *

def s1():
    g=bg_hermitage()
    g+=staff(200,720,300)+person(140,500,1.5,**VISHVAMITRA)
    g+=person(360,540,1.35,**RAMA)+person(530,570,1.2,**LAKSHMANA)
    for sx in (740,890): g+=person(sx,560,1.1,arms="raise",flip=True,**HERMIT)
    return g
def s2():
    g=bg_riverbank()
    g+=staff(280,720,300)+person(220,500,1.5,arms="raise",**VISHVAMITRA)
    g+=person(560,560,1.3,arms="hold",flip=True,**RAMA)+person(760,580,1.2,arms="hold",flip=True,**LAKSHMANA)
    return g
def s3():
    g=bg_hermitage(huts=False)
    g+=altar(240,780,0.9)
    g+=person(420,500,1.5,arms="raise",**SAGARA)
    g+=post(640,780,180)
    for sx,sy in ((780,560),(900,600),(690,640)): g+=person(sx,sy,0.9,arms="up2",**SAGARA_SON)
    return g
def s4():
    g=bg_underground()
    g+=halo(500,360,200)+person(500,420,1.5,arms="hold",**KAPILA)
    g+=horse(800,600,1.0,flip=True)
    for ax,ay in ((130,720),(270,760),(200,640)): g+=ashes(ax,ay,1.0)
    return g
def s5():
    g=bg_himalaya()
    g+=halo(500,160,150)+spark(500,160,30,"#fffaf0")
    for px,py in ((420,240),(590,230),(460,90),(560,90)): g+=spark(px,py,12,"#fff6c9")
    g+=person(500,520,1.6,arms="up2",**BHAGIRATHA)
    return g
def s6():
    g=bg_himalaya()
    g+=trishula(230,760,380)
    g+=ganga_fall(500,0,250,110)
    for k in (-1,1): g+=f'<path d="M{500+k*30},300 Q{500+k*200},330 {500+k*250},620 L{500+k*300},860 L{500+k*230},860 L{500+k*200},620 Q{500+k*170},380 {500+k*30},320 Z" fill="url(#river)" opacity="0.85"/>'
    g+=shiva(500,430,1.55)
    g+=bowing(870,570,1.1,angle=-18,flip=True,**BHAGIRATHA)
    return g
def s7():
    g='<rect width="1000" height="860" fill="url(#day)"/>'
    g+='<path d="M0,560 Q250,520 500,550 T1000,540 L1000,860 L0,860 Z" fill="#9ccc65"/>'
    g+='<path d="M0,380 Q300,420 420,600 Q500,740 620,860 L330,860 Q250,720 200,620 Q120,480 0,470 Z" fill="url(#river)"/>'
    for wx,wy in ((150,440),(280,560),(360,700),(470,800)): g+=f'<path d="M{wx-30},{wy} Q{wx-15},{wy-8} {wx},{wy} T{wx+30},{wy}" stroke="#d6eaf8" stroke-width="4" fill="none" stroke-linecap="round"/>'
    g+=person(660,450,1.15,arms="raise",**BHAGIRATHA)+chariot(670,620,1.0)+horse(880,560,0.75)
    for ax,ay in ((180,800),(80,740)): g+=ashes(ax,ay,0.8)
    for sx,sy,r in ((130,600,20),(220,480,18),(90,380,16),(260,330,14),(170,230,12),(320,180,10)): g+=soul(sx,sy,r)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
