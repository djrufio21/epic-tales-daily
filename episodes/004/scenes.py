from epic import *

def s1():
    g=bg_riverbank()
    g+=staff(370,700,320)+person(300,470,1.8,arms="raise",**VISHVAMITRA)
    g+=person(580,540,1.4,**RAMA)+person(760,540,1.4,**LAKSHMANA)
    g+=spark(470,250,16)+spark(520,200,10)+spark(430,190,12)
    return g
def s2():
    g=bg_river(far="#14351f")
    for tx in (100,300,520,760,930): g+=tree(tx,250,70,"#173d24")
    for ex in (300,700): g+=f'<circle cx="{ex-12}" cy="270" r="6" fill="#e74c3c"/><circle cx="{ex+12}" cy="270" r="6" fill="#e74c3c"/>'
    g+=soundwaves(560,170,1.0)+soundwaves(440,170,1.0,flip=True)
    g+=person(310,560,1.25,**VISHVAMITRA)+person(500,580,1.1,**RAMA)+person(670,580,1.1,**LAKSHMANA)
    g+=boat(490,640,1.15)
    return g
def s3():
    g=bg_forest()+demon(720,260,2.0)
    g+=staff(320,700,320)+person(250,470,1.8,arms="raise",**VISHVAMITRA)
    g+=person(470,560,1.3,**RAMA)+person(640,570,1.25,**LAKSHMANA)
    return g
def s4():
    g=bg_forest()
    g+=staff(300,700,320)+person(230,470,1.8,arms="raise",**VISHVAMITRA)
    g+=person(560,500,1.6,mood="sad",**RAMA)+person(790,520,1.45,**LAKSHMANA)
    return g
def s5():
    g=bg_forest()
    g+=staff(200,700,300)+person(140,480,1.6,**VISHVAMITRA)
    g+=person(440,480,1.7,arms="raise",**RAMA)+bow(440+62*1.7,480-22*1.7,1.5)
    g+=soundwaves(620,440,1.3)
    g+=person(820,530,1.4,**LAKSHMANA)
    return g
def s6():
    g='<rect width="1000" height="860" fill="url(#dusk)"/><path d="M0,650 Q250,610 500,645 T1000,640 L1000,860 L0,860 Z" fill="#6b5a3a"/>'
    g+=dust(720,580,110)+dust(520,640,80)+dust(880,360,80)
    g+=demon_falling(690,400,1.8,30)
    g+=rock(560,250,34)+rock(470,360,26)+rock(700,170,22)
    g+=arrow(300,430,590,410)+arrow(330,360,520,260)
    g+=person(110,600,1.2,**LAKSHMANA)
    g+=person(240,480,1.6,arms="raise",**RAMA)+bow(240+62*1.6,480-22*1.6,1.4)
    return g
def s7():
    g=bg_garden(pond=False)
    for px,py in ((300,140),(420,90),(560,130),(680,80),(760,160),(240,230),(620,220)): g+=spark(px,py,14,"#f8c471")
    g+=staff(320,700,320)+person(250,470,1.8,arms="raise",**VISHVAMITRA)
    g+=person(540,540,1.4,**RAMA)+person(720,540,1.4,**LAKSHMANA)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
