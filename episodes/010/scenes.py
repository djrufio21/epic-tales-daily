from epic import *

def s1():
    g=bg_court()
    g+=staff(200,720,300)+person(140,500,1.5,arms="raise",**VISHVAMITRA)
    g+=person(370,540,1.35,**RAMA)+person(530,570,1.2,**LAKSHMANA)
    g+=person(800,510,1.5,arms="raise",flip=True,**JANAKA)
    return g
def s2():
    g=bg_court()
    g+=faded(halo(560,230,190)+shiva(530,250,0.85,arms="raise")+great_bow(630,235,0.62),0.75)
    g+=person(170,520,1.5,arms="raise",**JANAKA)
    g+=person(700,580,1.2,arms="hold",flip=True,**RAMA)+person(870,600,1.1,arms="hold",flip=True,**LAKSHMANA)
    return g
def s3():
    g=bg_field()
    g+=halo(860,650,140)+baby(870,660,1.3)
    g+=plough(480,700,0.95)
    g+=person(400,460,1.4,arms="hold",**JANAKA)
    for px,py in ((620,520),(830,540),(700,460)): g+=spark(px,py,14,"#fff6c9")
    return g
def s4():
    g=bg_court()
    g+=bow_cart(500,830,1.0,bow=True)
    g+=bowing(250,500,1.2,angle=18,mood="sad",**SUITOR)
    g+=person(110,500,1.2,mood="sad",**SUITOR2)
    g+=person(860,490,1.3,arms="raise",mood="sad",flip=True,**SUITOR)
    return g
def s5():
    g=bg_court()
    for mx,my in ((330,540),(210,520),(90,500)): g+=bowing(mx,my,1.05,angle=-16,flip=True,arms="raise",**STRONGMAN)
    g+=rope(420,725,40,500)
    g+=bow_cart(640,840,0.9)
    g+=person(900,500,1.2,arms="raise",flip=True,**JANAKA)
    return g
def s6():
    g=bg_court()
    g+=staff(200,720,300)+person(140,500,1.5,arms="raise",**VISHVAMITRA)
    g+=person(440,540,1.4,arms="raise",**RAMA)+great_bow(524,500,0.85)
    g+=person(720,570,1.2,arms="hold",flip=True,**LAKSHMANA)+person(880,540,1.3,arms="hold",flip=True,**JANAKA)
    return g
def s7():
    g=bg_court()
    g+=great_bow(500,400,0.8,angle=-90,broken=True)
    g+=soundwaves(640,360,1.3)+soundwaves(360,360,1.3,flip=True)
    g+=person(500,560,1.4,arms="up2",**RAMA)
    g+=staff(160,730,300)+person(110,520,1.4,**VISHVAMITRA)
    g+=person(780,600,1.15,flip=True,**LAKSHMANA)+person(910,560,1.3,arms="up2",flip=True,**JANAKA)
    g+=bowing(320,690,0.65,angle=-72,flip=True,**HERMIT)+bowing(590,700,0.65,angle=72,**SUITOR2)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
