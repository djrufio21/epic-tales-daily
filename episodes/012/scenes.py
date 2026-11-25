from epic import *

def s1():
    g=bg_mithila()
    g+=dust(560,790,40)
    g+=person(612,688,0.75,**MESSENGER)
    g+=chariot(620,800,0.75)
    g+=horse(847,722,0.75)
    g+=person(200,520,1.5,arms="raise",**JANAKA)
    g+=bowing(470,540,1.35,angle=-20,flip=True,**KUSHADHVAJA)
    return g
def s2():
    g=bg_court()
    g+=staff(200,720,300)+person(140,500,1.5,arms="raise",**SAGE)
    g+=person(400,560,1.25,**KING)
    g+=person(640,540,1.35,arms="raise",flip=True,**JANAKA)+person(850,570,1.25,arms="hold",flip=True,**KUSHADHVAJA)
    return g
def s3():
    g=bg_court()
    g+=faded(halo(500,240,170)+person(450,260,0.8,**SITA)+person(550,270,0.75,**URMILA),0.8)
    g+=person(170,520,1.5,arms="raise",**JANAKA)
    g+=person(600,560,1.3,flip=True,**KING)
    g+=person(780,590,1.15,arms="hold",flip=True,**RAMA)+person(910,610,1.05,arms="hold",flip=True,**LAKSHMANA)
    return g
def s4():
    g=bg_court()
    g+=staff(90,730,300)+person(140,510,1.35,arms="raise",**VISHVAMITRA)
    g+=staff(260,750,290)+person(310,540,1.3,**SAGE)
    g+=person(480,590,1.1,arms="hold",**BHARATA)+person(600,600,1.05,arms="hold",**SHATRUGHNA)
    g+=person(760,540,1.3,arms="up2",flip=True,**JANAKA)+person(905,560,1.2,arms="up2",flip=True,**KUSHADHVAJA)
    return g
def s5():
    g=bg_mithila()
    g+=person(150,520,1.5,arms="raise",**KING)
    g+=cow(400,690,1.2)+cow(580,760,1.2)
    g+=person(790,560,1.25,arms="hold",flip=True,**HERMIT)+person(920,590,1.1,arms="hold",flip=True,**SHATANANDA)
    return g
def s6():
    g=bg_court()
    g+=mandap(500,770,1.9,"#f9e79f","#c0392b")
    g+=altar(500,780,1.0)
    g+=staff(110,760,300)+person(160,560,1.3,arms="raise",**SAGE)
    g+=person(690,560,1.2,**SITA)+person(780,560,1.2,flip=True,**RAMA)
    g+=person(320,560,1.3,arms="raise",**JANAKA)
    return g
def s7():
    g=bg_court()
    g+=mandap(500,770,1.9,"#f9e79f","#c0392b")
    g+=person(300,440,0.85,**MANDAVI)+person(375,440,0.85,flip=True,**BHARATA)
    g+=person(625,440,0.85,**SHRUTAKIRTI)+person(700,440,0.85,flip=True,**SHATRUGHNA)
    g+=altar(500,790,0.9)
    g+=person(150,620,1.1,**URMILA)+person(240,620,1.1,flip=True,**LAKSHMANA)
    g+=person(760,620,1.1,**SITA)+person(850,620,1.1,flip=True,**RAMA)
    g+=flower_rain(26,12,top=20,bottom=300)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
