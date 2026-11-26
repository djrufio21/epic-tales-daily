from epic import *

def s1():
    g=bg_mithila()
    g+=staff(170,720,300)+person(110,500,1.4,arms="raise",**VISHVAMITRA)
    g+=person(330,540,1.3,arms="hold",**JANAKA)
    g+=basket(450,770,1.3)+kalash(530,790,0.8)
    g+=person(660,520,1.4,flip=True,**KING)
    g+=person(800,580,1.15,flip=True,**RAMA)+person(910,600,1.05,flip=True,**SITA)
    return g
def s2():
    g=bg_road()
    g+=bird(200,150,1.1,crying=True)+bird(380,100,0.9,flip=True,crying=True)+bird(640,140,1.0,crying=True)+bird(820,90,0.85,flip=True,crying=True)
    g+=soundwaves(260,140,0.6)+soundwaves(700,130,0.6)
    g+=staff(200,760,300)+person(140,560,1.35,arms="raise",**SAGE)
    g+=deer(460,740,0.95)+deer(640,790,0.95,flip=True)
    g+=person(840,560,1.35,mood="sad",flip=True,**KING)
    return g
def s3():
    g=bg_storm()
    g+=wind(300,330,1.3)+wind(720,250,1.1)
    g+=person(200,560,1.3,mood="sad",**KING)
    g+=person(400,600,1.15,mood="sad",**LAKSHMANA)
    g+=person(820,560,1.3,flip=True,**RAMA)
    g+=dust(600,780,70)+wind(620,560,0.8,c="#bfb6a6")
    return g
def s4():
    g=bg_storm()
    g+='<circle cx="700" cy="420" r="300" fill="url(#glow)" opacity="0.55"/>'
    g+=parashurama(700,440,1.7)+vishnu_bow(810,580,0.7)
    g+=bowing(200,560,1.3,angle=18,**SAGE)+kalash(340,770,0.75)
    return g
def s5():
    g=bg_storm()
    g+='<circle cx="760" cy="420" r="260" fill="url(#glow)" opacity="0.5"/>'
    g+=person(170,520,1.45,arms="up2",mood="sad",**KING)
    g+=person(410,560,1.3,**RAMA)
    g+=parashurama(760,460,1.6,arms="raise",flip=True)+vishnu_bow(760-60*1.6,460-22*1.6-10,0.75,angle=0)
    return g
def s6():
    g=bg_storm()
    g+='<circle cx="380" cy="420" r="280" fill="url(#glow)" opacity="0.5"/>'
    g+=person(350,520,1.5,arms="raise",**RAMA)+vishnu_bow(350+60*1.5,520-22*1.5,0.8,angle=-40,arrowed=True)
    g+=parashurama(760,540,1.4,flip=True)
    return g
def s7():
    g=bg_road()
    g+=trail(560,300,900,60)+spark(900,60,22,"#fffaf0")
    g+=halo(340,440,190)
    g+=person(340,500,1.45,arms="raise",**RAMA)+vishnu_bow(340+60*1.45,500-22*1.45,0.75,angle=0,strung=True)
    g+=parashurama(720,560,1.35,arms="hold",mood="smile",flip=True)
    g+=flower_rain(14,13,top=30,bottom=260)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
