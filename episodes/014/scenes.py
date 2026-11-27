from epic import *

def s1():
    g=bg_riverbank()
    g+=halo(700,300,170)+trail(420,420,700,300)
    g+=vishnu_bow(700,300,0.7)
    g+=person(300,560,1.5,arms="up2",**RAMA)
    g+=person(120,590,1.25,arms="hold",**LAKSHMANA)
    return g
def s2():
    g=bg_road()
    g+=staff(110,760,300)+person(160,540,1.35,arms="raise",**SAGE)
    g+=person(450,540,1.45,arms="up2",**KING)+person(560,560,1.35,flip=True,**RAMA)
    g+=person(760,600,1.1,flip=True,**SITA)+person(880,610,1.1,flip=True,**LAKSHMANA)
    return g
def s3():
    g=bg_ayodhya()
    g+=person(90,620,1.0,arms="up2",**CITIZEN)+person(910,620,1.0,arms="up2",flip=True,**CITIZEN2)
    g+=person(380,600,1.0,arms="raise",**KING)
    g+=chariot(400,800,0.95)+horse(640,722,0.85)
    g+=person(200,690,0.95,arms="up2",**CITIZEN2)+person(820,690,0.95,arms="up2",flip=True,**CITIZEN)
    g+=flower_rain(18,14,top=200,bottom=520)
    return g
def s4():
    g=bg_room()
    g+=person(110,540,1.2,arms="hold",**Q1)+aarti(150,580,0.85)
    g+=person(245,560,1.1,**Q3)+person(370,570,1.05,**Q2)
    g+=bowing(545,600,0.95,angle=-15,flip=True,**SITA)+bowing(670,600,0.95,angle=-15,flip=True,**URMILA)
    g+=bowing(795,600,0.95,angle=-15,flip=True,**MANDAVI)+bowing(920,600,0.95,angle=-15,flip=True,**SHRUTAKIRTI)
    return g
def s5():
    g=bg_court()
    g+=person(170,520,1.45,arms="raise",**KING)
    g+=bowing(420,570,1.2,angle=-22,flip=True,**BHARATA)+bowing(560,590,1.1,angle=-22,flip=True,**SHATRUGHNA)
    g+=person(820,540,1.35,flip=True,**YUDHAJIT)
    return g
def s6():
    g=bg_court()
    g+=person(250,520,1.5,arms="raise",**KING)
    g+=bowing(520,560,1.3,angle=-22,flip=True,**RAMA)
    g+=person(720,570,1.2,arms="hold",flip=True,**LAKSHMANA)
    g+=person(880,560,1.2,flip=True,**Q1)
    return g
def s7():
    g=bg_garden()
    g+=person(400,520,1.35,**RAMA)+person(560,530,1.3,flip=True,**SITA)
    g+=person(170,600,1.0,arms="hold",**CITIZEN)+person(830,600,1.0,arms="hold",flip=True,**CITIZEN2)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
