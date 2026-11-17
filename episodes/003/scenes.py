from epic import *

def s1():
    g=bg_court()
    g+=staff(370,700,330)+person(300,460,1.9,**VISHVAMITRA)
    g+=person(650,460,1.9,arms="hold",**KING)
    return g
def s2():
    g=bg_room()
    g+=person(290,440,2.0,arms="up2",**KING)
    g+=staff(790,690,330)+person(710,440,2.0,**VISHVAMITRA)
    return g
def s3():
    g=bg_forest()+demon(700,250,1.5)+demon(880,360,1.2)+demon(560,150,0.9)
    g+=fire(470,640,0.8)
    g+=person(210,480,1.7,arms="up2",mood="sad",**VISHVAMITRA)
    return g
def s4():
    g=bg_room()
    g+=person(250,440,2.0,arms="up2",mood="sad",**KING)
    g+=person(500,550,1.3,**RAMA)
    g+=staff(850,690,320)+person(770,450,1.9,**VISHVAMITRA)
    return g
def s5():
    g=bg_court()
    g+=person(300,460,1.9,arms="raise",**SAGE)
    g+=person(650,460,1.9,mood="sad",**KING)
    return g
def s6():
    g=bg_room()
    g+=person(210,430,1.9,arms="raise",**KING)
    g+=person(470,545,1.35,arms="hold",**RAMA)+person(620,545,1.35,arms="hold",**LAKSHMANA)
    g+=staff(905,690,310)+person(830,450,1.8,**VISHVAMITRA)
    return g
def s7():
    g=bg_road()
    g+=bow(330,520,1.3)+person(380,520,1.25,**RAMA)
    g+=bow(690,520,1.3,flip=True)+person(640,520,1.25,**LAKSHMANA)
    g+=staff(565,640,250)+person(510,440,1.5,**VISHVAMITRA)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
