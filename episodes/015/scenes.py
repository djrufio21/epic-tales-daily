from epic import *

def s1():
    g=bg_ayodhya(sky="url(#day)")
    g+=person(130,560,1.15,arms="hold",**CITIZEN)+person(290,580,1.05,arms="up2",**CITIZEN2)
    g+=person(520,540,1.4,arms="raise",flip=True,**RAMA)
    g+=person(740,560,1.2,arms="hold",flip=True,**HERMIT)+person(890,590,1.0,arms="up2",flip=True,**CITIZEN)
    return g
def s2():
    g=bg_court()
    g+=throne(500,780,1.05)
    g+=person(500,520,1.5,arms="hold",**KING)
    g+=thought(790,250,170,560,410)+person(790,250,0.95,arms="raise",flip=True,**RAMA)
    return g
def s3():
    g=bg_court()
    g+=throne(160,780,0.85)+person(160,540,1.3,arms="raise",**KING)
    g+=person(370,560,1.1,arms="up2",flip=True,**SAGE)+person(500,580,1.05,arms="up2",flip=True,**MINISTER)
    g+=person(630,560,1.1,arms="up2",flip=True,**SUITOR)+person(760,580,1.05,arms="up2",flip=True,**CITIZEN)
    g+=person(890,570,1.05,arms="up2",flip=True,**CITIZEN2)
    return g
def s4():
    g=bg_court()
    g+=throne(250,780,0.9)+person(250,520,1.45,arms="raise",**KING)
    g+=bowing(500,580,1.25,angle=-22,flip=True,**RAMA)
    g+=person(720,560,1.2,arms="hold",flip=True,**SUMANTRA)
    g+=staff(840,770,330)+person(890,550,1.2,flip=True,**SAGE)
    return g
def s5():
    g=bg_room()
    g+=person(150,540,1.25,arms="hold",**Q1)+aarti(190,585,0.85)
    g+=person(300,570,1.1,**Q3)
    g+=person(520,540,1.35,arms="raise",flip=True,**RAMA)
    g+=person(700,560,1.25,arms="hold",flip=True,**LAKSHMANA)+person(860,570,1.15,flip=True,**SITA)
    return g
def s6():
    g=bg_room_night()
    g+=staff(110,770,330)+person(160,540,1.3,arms="raise",**SAGE)
    g+=altar(500,780,1.0)
    g+=person(720,560,1.3,arms="hold",flip=True,**RAMA)+person(870,580,1.2,arms="hold",flip=True,**SITA)
    return g
def s7():
    g=bg_ayodhya(sky="url(#night)")+stars(16,15,30,100)
    for x in range(60,1000,110): g+=diya(x,650,1.0)
    g+=person(140,600,1.0,arms="up2",**CITIZEN2)+person(320,620,1.0,arms="hold",**CITIZEN)
    g+=person(680,620,1.0,arms="hold",flip=True,**CITIZEN2)+person(860,600,1.0,arms="up2",flip=True,**CITIZEN)
    for x in (230,500,770): g+=diya(x,830,1.3)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
