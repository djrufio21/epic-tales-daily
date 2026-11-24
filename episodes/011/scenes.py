from epic import *

def s1():
    g=bg_court()
    g+=faded(halo(470,230,160)+person(470,250,0.85,arms="hold",**SITA),0.75)
    g+=person(170,510,1.5,arms="raise",**JANAKA)
    g+=staff(570,720,300)+person(630,520,1.35,flip=True,**VISHVAMITRA)
    g+=person(790,560,1.25,arms="hold",flip=True,**RAMA)+person(910,590,1.1,arms="hold",flip=True,**LAKSHMANA)
    return g
def s2():
    g=bg_road()
    g+=dust(200,770,60)
    g+=person(370,600,1.0,arms="raise",**MESSENGER)
    g+=chariot(380,800,1.0)
    g+=horse(682,696,1.0)
    return g
def s3():
    g=bg_court()
    g+=bowing(200,560,1.1,angle=16,**MESSENGER)+bowing(400,540,1.2,angle=16,**MESSENGER)
    g+=person(780,500,1.5,arms="raise",flip=True,**KING)
    return g
def s4():
    g=bg_court()
    g+=person(240,510,1.5,arms="up2",**KING)
    g+=staff(530,720,300)+person(590,520,1.4,arms="raise",flip=True,**SAGE)
    g+=person(770,560,1.2,arms="hold",flip=True,**HERMIT)
    g+=person(910,590,1.05,arms="hold",flip=True,**MINISTER)
    return g
def s5():
    g=bg_road()
    g+=dust(110,790,50)
    g+=person(241,640,0.9,arms="raise",**KING)
    g+=chariot(250,820,0.9)
    g+=horse(522,726,0.9)
    g+=staff(760,770,280)+person(810,580,1.1,**SAGE)
    g+=person(925,600,1.0,arms="hold",**HERMIT)
    return g
def s6():
    g=bg_mithila()
    g+=person(210,520,1.5,arms="raise",**JANAKA)
    g+=kalash(450,760,0.85)
    g+=person(690,520,1.5,arms="raise",flip=True,**KING)
    g+=staff(840,730,300)+person(900,570,1.15,flip=True,**SAGE)
    return g
def s7():
    g=bg_mithila(sky="url(#dusk)",sun="#f8c471")
    g+=staff(170,720,300)+person(110,500,1.4,**VISHVAMITRA)
    g+=bowing(330,560,1.1,angle=18,**LAKSHMANA)+bowing(510,540,1.2,angle=18,**RAMA)
    g+=person(790,500,1.5,arms="raise",flip=True,**KING)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
