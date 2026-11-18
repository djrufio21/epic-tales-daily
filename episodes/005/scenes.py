from epic import *

def s1():
    g=bg_dawn_forest()
    g+=staff(320,700,320)+person(250,470,1.8,arms="raise",**VISHVAMITRA)
    g+=person(560,540,1.4,**RAMA)+person(740,540,1.4,**LAKSHMANA)
    return g
def s2():
    g=bg_dawn_forest()
    for px,py in ((420,230),(480,170),(540,220),(600,160)): g+=spark(px,py,14,"#fff6c9")
    g+=staff(270,700,320)+person(200,470,1.8,arms="raise",**VISHVAMITRA)
    g+=person(560,520,1.5,arms="hold",**RAMA)
    g+=person(820,560,1.25,arms="hold",**LAKSHMANA)
    return g
def s3():
    g=bg_dawn_forest(sun=False)
    for ax,ay in ((500,330),(680,270),(850,330)): g+=halo(ax,ay-30,120)+person(ax,ay,1.3,arms="hold",**ASTRA)
    g+=person(200,500,1.6,**RAMA)
    return g
def s4():
    g=bg_dawn_forest(sun=False)
    g+=halo(650,340,150)+person(650,380,1.45,arms="hold",**ASTRA)
    g+=halo(860,320,110)+person(860,350,1.05,arms="hold",**ASTRA)
    g+=person(360,480,1.7,arms="raise",**RAMA)
    return g
def s5():
    g=bg_dawn_forest()
    g+=staff(320,700,320)+person(250,470,1.8,arms="raise",**VISHVAMITRA)
    g+=person(620,500,1.6,arms="hold",**RAMA)
    for px,py in ((420,250),(470,190),(380,200)): g+=spark(px,py,13,"#fff6c9")
    return g
def s6():
    g=bg_dawn_forest()
    g+=staff(270,700,320)+person(200,470,1.8,arms="raise",**VISHVAMITRA)
    g+=bowing(520,520,1.5,angle=-12,flip=True,**RAMA)
    g+=person(800,550,1.3,arms="hold",**LAKSHMANA)
    return g
def s7():
    g=bg_hermitage()
    g+=staff(170,720,300)+person(110,500,1.6,**VISHVAMITRA)
    g+=person(300,520,1.5,arms="raise",**RAMA)+person(490,560,1.3,**LAKSHMANA)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
