from epic import *

def s1():
    g=bg_garden(pond=False)+'<circle cx="500" cy="300" r="34" fill="#e74c3c"/><path d="M470,290 Q500,270 530,290" stroke="#fffaf0" stroke-width="5" fill="none"/>'
    for x,c,n in ((170,RAMA,"Rama"),(390,LAKSHMANA,"Lakshmana"),(610,BHARATA,"Bharata"),(830,SHATRUGHNA,"Shatrughna")):
        g+=person(x,520,1.35,arms="up2",**c)+label(x,740,n,26)
    return g
def s2():
    g=bg_garden()
    g+=person(210,470,1.6,**RAMA)+person(350,480,1.5,arms="raise",flip=True,**LAKSHMANA)
    g+=person(650,470,1.6,**BHARATA)+person(790,480,1.5,arms="raise",flip=True,**SHATRUGHNA)
    return g
def s3():
    g=bg_garden(pond=False)
    g+=person(200,440,1.9,arms="raise",**SAGE)
    for x,c in ((470,RAMA),(600,LAKSHMANA),(730,BHARATA),(860,SHATRUGHNA)):
        g+=person(x,560,1.2,arms="hold",**c)+book(x,560+56*1.2,1.3)
    return g
def s4():
    g=bg_garden(pond=False)+target(840,470,1.0)
    g+=person(120,540,1.4,arms="up2",**LAKSHMANA)
    g+=person(330,480,1.7,arms="raise",**RAMA)+bow(330+62*1.7,480-22*1.7,1.5)
    g+=arrow(560,446,790,466)
    return g
def s5():
    g=bg_room()
    g+=person(170,430,1.8,arms="raise",**KING)+person(350,445,1.7,**Q1)
    for x,c in ((540,RAMA),(655,LAKSHMANA),(770,BHARATA),(885,SHATRUGHNA)): g+=person(x,545,1.25,arms="hold",**c)
    return g
def s6():
    g='<rect width="1000" height="860" fill="url(#day)"/>'+palace(215,40,1.0)+'<rect y="480" width="1000" height="380" fill="#e6cf9c"/>'
    g+=tree(70,380,70)+tree(930,370,76,"#5b9a45")
    g+=person(130,560,1.45,robe="#8e44ad",female=True,drape="#c39bd3",arms="up2")+person(880,560,1.45,robe="#16a085",arms="up2")
    g+=person(330,520,1.6,robe="#7f8c8d",hair="#ecf0f1",beard="#ecf0f1",trim="#566573")
    g+=person(520,520,1.6,arms="hold",**RAMA)+basket(520-70,520+50*1.6,1.5)
    g+=person(690,530,1.5,**LAKSHMANA)
    return g
def s7():
    g=bg_court()+'<rect x="370" y="600" width="260" height="42" rx="6" fill="#c9812a"/>'
    g+=person(560,400,1.9,**KING)
    g+=staff(275,700,330)+person(200,470,1.9,**VISHVAMITRA)
    g+=person(840,520,1.5,robe="#16a085",beard="#2b1b12",beardlen=10)
    return g

SCENES=[s1,s2,s3,s4,s5,s6,s7]
