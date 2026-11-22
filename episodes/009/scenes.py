from epic import *

def s1():
    g=bg_mithila()
    g+=staff(200,720,300)+person(140,500,1.5,arms="raise",**VISHVAMITRA)
    g+=person(370,540,1.35,arms="raise",**RAMA)+person(530,570,1.2,**LAKSHMANA)
    for sx,sy in ((720,560),(860,580)): g+=person(sx,sy,1.05,arms="hold",flip=True,**HERMIT)
    return g
def s2():
    g=bg_court()
    g+=person(560,520,1.45,arms="raise",**SHATANANDA)
    g+=person(360,540,1.5,**JANAKA)
    for sx,sy in ((170,580),(60,600)): g+=person(sx,sy,1.05,arms="hold",**HERMIT)
    g+=kalash(170,700,0.7)+kalash(60,720,0.7)
    return g
def s3():
    g=bg_mithila()
    g+=staff(840,720,300)+person(780,500,1.5,flip=True,**VISHVAMITRA)
    g+=kalash(580,760,0.9)
    g+=bowing(420,520,1.45,angle=22,**JANAKA)
    g+=person(170,560,1.2,arms="hold",**SHATANANDA)
    return g
def s4():
    g=bg_mithila()
    g+=person(160,510,1.5,arms="raise",**JANAKA)
    g+=staff(359,710,300)+person(420,520,1.3,flip=True,**VISHVAMITRA)
    g+=person(640,540,1.35,arms="hold",flip=True,**RAMA)+person(830,560,1.25,arms="hold",flip=True,**LAKSHMANA)
    return g
def s5():
    g=bg_mithila()
    g+=faded(halo(500,200,150)+person(440,210,0.8,arms="hold",**GAUTAMA)+person(560,220,0.75,arms="hold",flip=True,**AHALYA),0.6)
    g+=staff(200,720,300)+person(140,500,1.5,arms="raise",**VISHVAMITRA)
    for px,py in ((640,380),(860,370),(700,300),(820,290)): g+=spark(px,py,14,"#fff6c9")
    g+=person(750,520,1.5,arms="up2",flip=True,**SHATANANDA)
    return g
def s6():
    g=bg_mithila()
    g+=faded(halo(500,200,150)+person(500,230,0.85,arms="hold",**VISHVAMITRA),0.6)
    g+=person(200,520,1.5,arms="raise",**SHATANANDA)
    g+=person(620,540,1.35,arms="hold",flip=True,**RAMA)+person(810,560,1.25,arms="hold",flip=True,**LAKSHMANA)
    return g
def s7():
    g=bg_mithila(sky="url(#dusk)",sun="#f8c471")
    g+=staff(260,720,300)+person(200,500,1.5,arms="hold",**VISHVAMITRA)
    g+=person(400,560,1.2,**RAMA)+person(530,580,1.1,**LAKSHMANA)
    g+=bowing(800,520,1.45,angle=-20,flip=True,**JANAKA)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
