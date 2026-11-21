from epic import *

def s1():
    g=bg_river()+'<circle cx="840" cy="130" r="56" fill="#fff6c9"/>'
    g+=person(250,540,1.0,**HERMIT)
    g+=person(400,540,1.2,arms="raise",**VISHVAMITRA)+person(580,570,1.1,**RAMA)+person(740,570,1.1,**LAKSHMANA)
    g+=boat(490,640,1.15)
    return g
def s2():
    g=bg_old_hermitage()
    g+=staff(200,720,300)+person(140,500,1.5,arms="raise",**VISHVAMITRA)
    g+=person(370,540,1.35,arms="raise",**RAMA)+person(530,570,1.2,**LAKSHMANA)
    return g
def s3():
    g=bg_hermitage()
    g+=person(330,520,1.45,arms="hold",**GAUTAMA)+person(530,540,1.35,arms="hold",**AHALYA)
    g+=altar(820,790,0.8)
    return g
def s4():
    g=bg_hermitage()
    g+=staff(260,730,320)+person(330,500,1.55,arms="raise",mood="sad",**GAUTAMA)
    g+=bowing(640,540,1.35,angle=-14,flip=True,mood="sad",**AHALYA)
    return g
def s5():
    g=bg_old_hermitage()
    g+=faded(person(400,520,1.45,arms="hold",**AHALYA),0.35)
    g+=staff(960,520,150)+person(920,410,0.6,flip=True,**GAUTAMA)
    return g
def s6():
    g=bg_old_hermitage()
    g+=halo(640,420,230)+person(640,480,1.45,arms="hold",**AHALYA)
    g+=person(230,530,1.4,arms="raise",**RAMA)+person(80,570,1.2,**LAKSHMANA)
    for px,py in ((470,260),(810,280),(540,170),(760,160)): g+=spark(px,py,14,"#fff6c9")
    return g
def s7():
    g=bg_hermitage()+flower_rain()
    g+=person(860,500,1.4,arms="hold",flip=True,**GAUTAMA)+person(640,520,1.35,arms="raise",flip=True,**AHALYA)
    g+=bowing(330,540,1.3,angle=14,**RAMA)+bowing(140,570,1.15,angle=14,**LAKSHMANA)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
