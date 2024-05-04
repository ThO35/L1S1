from fltk import *
cote=500
cree_fenetre(cote,cote)

#  coordone gauche haut
xhg=5+0*cote/6
yhg=5+0*cote/6

xhg1=5+1*cote/6
yhg1=5+1*cote/6

xhg2=5+2*cote/6
yhg2=5+2*cote/6
# gauche milieu
xgm=5+0*cote/6
ygm=cote/2

xgm1=5+1*cote/6
ygm1=cote/2

xgm2=5+2*cote/6
ygm2=cote/2
# gauche bas
xgb= 5+0*cote/6
ygb= cote-5

xgb1= 5+1*cote/6
ygb1= cote-5-1*cote/6

xgb2= 5+2*cote/6
ygb2= cote-5-2*cote/6
#milieu
xm=cote/2
ym=cote/2
#milieu haut
xmh=cote/2
ymh=5+0*cote/6

xmh1=cote/2
ymh1=5+1*cote/6

xmh2=cote/2
ymh2=5+2*cote/6
#milieu bas
xmb=cote/2
ymb=cote-5

xmb1=cote/2
ymb1=cote-5-1*cote/6

xmb2=cote/2
ymb2=cote-5-2*cote/6
#droit bas
xdb=cote-5-0*cote/6
ydb=cote-5-0*cote/6

xdb1=cote-5-1*cote/6
ydb1=cote-5-1*cote/6

xdb2=cote-5-2*cote/6
ydb2=cote-5-2*cote/6
#droite milieu
xdm=cote-5-0*cote/6
ydm=cote/2

xdm1=cote-5-1*cote/6
ydm1=cote/2

xdm2=cote-5-2*cote/6
ydm2=cote/2
#droite haut
xdh=cote-5-0*cote/6
ydh=5+0*cote/6

xdh1=cote-5-1*cote/6
ydh1=5+1*cote/6

xdh2=cote-5-2*cote/6
ydh2=5+2*cote/6

#creation coordone
lst=[[xhg,yhg],[xgm,ygm],[xgb,ygb],[xmh,ymh],[xmb,ymb],[xdb,ydb],[xdm,ydm],[xdh,ydh],[xhg1,yhg1],[xgm1,ygm1],[xgb1,ygb1],[xmh1,ymh1],[xmb1,ymb1],[xdb1,ydb1],[xdm1,ydm1],[xdh1,ydh1]]



def plateau_6(cote,lst):

    for i in range(2):
        rectangle(5+i*cote/6,5+i*cote/6,cote-5-i*cote/6,  cote-5-i*cote/6,remplissage="#f9e4b7",epaisseur=1)


    ligne(xmh,ymh,xmh1,ymh1,epaisseur=1)
    ligne(xmb1,ymb1,xmb,ymb,epaisseur=1)
    ligne(xgm,ygm,xgm1,ygm1,epaisseur=1)
    ligne(xdm1,ydm1,xdm,ydm,epaisseur=1)

    j=0
    while j !=16:
        cercle (lst[j][0],lst[j][1],5,remplissage= "green")# haut gauche
        j+=1

    dico={}
    listepion=[]
    jeton=0

    while jeton!=12:
        piontableau=phase1 (jeton,lst,listepion,dico,tableau5)

        if piontableau == None :
            jeton=jeton
        else:
            listepion.append (piontableau)

            jeton+=1


    joueur =   0
    longeur = "continue"
    while longeur != True:


        n=phase2(listepion,lst,dico,joueur,tableau5 )
        if n == None:
            joueur +=0
        else:
            joueur+=1
        longeur =arret (dico)

    attend_fermeture ()
    ferme_fenetre()









def phase1 (jeton,lst,listepion,dico,copitableau5):

    moulin (dico,vieuxmoulin,listepion )
    lst1=[]
    tagjeton=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    x,y=attend_clic_gauche ()
    for i in lst:
        if abs (x- i[0])<10 and abs (y-i[1])<10:

                if jeton %2==1:
                    lst1.append (i[0])
                    lst1.append (i[1])


                    if lst1 in listepion:
                        return lst1.clear ()

                    else:
                        x=i[0]
                        y=i[1]
                        cercle (x,y,10,remplissage= 'black',tag = tagjeton[jeton])
                        dico [tagjeton[jeton]] = [i[0],i[1],[10,'black',tagjeton[jeton]]]
                        return lst1
                else:
                    lst1.append (i[0])
                    lst1.append (i[1])


                    if lst1 in listepion:
                        return lst1.clear ()
                    else:
                        x=i[0]
                        y=i[1]
                        cercle (x,y,10,remplissage= 'white',tag = tagjeton[jeton] )
                        dico [tagjeton[jeton]]= [i[0],i[1],[10, 'white', tagjeton[jeton]]]
                        return lst1



tableau5={
                (xhg,yhg) : [[xmh,ymh,[]],[xgm,ygm,[]]],
                (xgm,ygm) : [[xhg,yhg,[]],[xgm1,ygm1,[]],[xgb,ygb,[]]],
                (xgb,ygb) : [[xgm,ygm,[]],[xmb,ymb,[]]],
                (xmb,ymb) : [[xgb,ygb,[]],[xmb1,ymb1,[]],[xdb,ydb,[]]],
                (xdb,ydb) : [ [xmb,ymb,[]],[xdm,ydm,[]] ],
                (xdm,ydm) : [[xdb,ydb,[]],[xdm1,ydm1,[]],[xdh,ydh,[]]],
                (xdh,ydh) : [[xdm,ydm,[]],[xmh,ymh,[]]],
                (xmh,ymh) : [[xdh,ydh,[]],[xhg,yhg,[]],[xmh1,ymh1,[]]],
                (xhg1,yhg1) : [[xmh1,ymh1,[]],[xgm1,ygm1,[]]],
                (xgm1,ygm1) : [[xhg1,yhg1,[]],[xgm,ygm,[]],[xgb1,ygb1,[]]],
                (xgb1,ygb1) : [[xgm1,ygm1,[]],[xmb1,ymb1,[]]],
                (xmb1,ymb1) : [[xgb1,ygb1,[]],[xmb,ymb,[]],[xdb1,ydb1,[]]],
                (xdb1,ydb1) : [[xmb1,ymb1,[]],[xdm1,ydm1,[]]],
                (xdm1,ydm1) : [[xdb1,ydb1,[]],[xdm,ydm,[]],[xdh1,ydh1,[]]],
                (xdh1,ydh1) : [[xdm1,ydm1,[]],[xmh1,ymh1,[]]],
                (xmh1,ymh1) : [[xdh1,ydh1,[]],[xhg1,yhg1,[]],[xmh,ymh,[]]],}





def phase2 (listepion,lst,dico,joueur,tableau5,):


    moulin (dico,vieuxmoulin,listepion )


    x,y=attend_clic_gauche ()
    for i in dico.values():
        for j in lst:
            if abs (x- j[0])<10 and abs (y-j[1])<10:
                if [j[0],j[1]] in listepion:
                    if [j[0],j[1]] == [i[0],i[1]]:




                        possible=[]
                        for valeur in tableau5:



                            if ((j[0],j[1]))== valeur:
                                n= tableau5.get(valeur)

                                if len (n) == 3:

                                    if [n[0][0],n[0][1]] not in listepion:
                                        cercle (n[0][0],n[0][1],5, remplissage ="red",tag="&")
                                        possible.append ([n[0][0],n[0][1]])
                                    if [n[1][0],n[1][1]] not in listepion:
                                        cercle (n[1][0],n[1][1],5, remplissage ="red",tag="@")
                                        possible.append ([n[1][0],n[1][1]])
                                    if [n[2][0],n[2][1]] not in listepion:
                                        cercle (n[2][0],n[2][1],5, remplissage ="red",tag="#")
                                        possible.append ([n[2][0],n[2][1]])

                                else :
                                    if [n[0][0],n[0][1]] not in listepion:
                                        cercle (n[0][0],n[0][1],5, remplissage ="red",tag="&")
                                        possible.append ([n[0][0],n[0][1]])
                                    if [n[1][0],n[1][1]] not in listepion:
                                        cercle (n[1][0],n[1][1],5, remplissage ="red",tag="@")
                                        possible.append ([n[1][0],n[1][1]])






                                x1,y1=attend_clic_gauche ()
                                for m in lst:
                                    if abs (x1- m[0])<10 and abs (y1-m[1])<10:

                                        if [m[0], m[1]] in possible:
                                            if joueur%2==0:
                                                if i[2][1] == "white":

                                                    efface (i[2][2])
                                                    cercle (m[0],m[1],i[2][0],remplissage =i[2][1],tag =i[2][2] )
                                                    dico [i[2][2]]= [m[0],m[1],[10, 'white', i[2][2]]]
                                                    listepion.remove (j)
                                                    listepion.append ([m[0],m[1]])
                                                    efface ("#")
                                                    efface ("&")
                                                    efface ("@")

                                                    return "joueur"

                                                else:
                                                    efface ("#")
                                                    efface ("&")
                                                    efface ("@")
                                                    return None
                                                efface ("#")
                                                efface ("&")
                                                efface ("@")


                                            else:
                                                if i[2][1] == "black":
                                                    efface (i[2][2])
                                                    cercle (m[0],m[1],i[2][0],remplissage =i[2][1],tag =i[2][2] )
                                                    dico [i[2][2]]= [m[0],m[1],[10, 'black', i[2][2]]]
                                                    listepion.remove (j)
                                                    listepion.append ([m[0],m[1]])
                                                    efface ("#")
                                                    efface ("&")
                                                    efface ("@")

                                                    return "joueur"

                                                else:
                                                    efface ("#")
                                                    efface ("&")
                                                    efface ("@")
                                                    return None

                                                efface ("#")
                                                efface ("&")
                                                efface ("@")

                                        else:
                                            efface ("#")
                                            efface ("&")
                                            efface ("@")
                                            return None











vieuxmoulin = []



def moulin (dico,vieuxmoulin,listepion ):
    moulinlst = []
    dicovrai = ""
    dicovrai = dico.copy()

    tableau5milieu={
                    (xgm,ygm) : [[xhg,yhg,[]],[xgb,ygb,[]],[xgm,ygm,[]]],
                    (xmb,ymb) : [[xgb,ygb,[]],[xdb,ydb,[]],[xmb,ymb,[]]],
                    (xdm,ydm) : [[xdb,ydb,[]],[xdh,ydh,[]],[xdm,ydm,[]]],
                    (xmh,ymh) : [[xdh,ydh,[]],[xhg,yhg,[]],[xmh,ymh,[]]],
                    (xgm1,ygm1) : [[xhg1,yhg1,[]],[xgb1,ygb1,[]],[xgm1,ygm1,[]]],
                    (xmb1,ymb1) : [[xgb1,ygb1,[]],[xdb1,ydb1,[]],[xmb1,ymb1,[]]],
                    (xdm1,ydm1) : [[xdb1,ydb1,[]],[xdh1,ydh1,[]],[xdm1,ydm1,[]]],
                    (xmh1,ymh1) : [[xdh1,ydh1,[]],[xhg1,yhg1,[]],[xmh1,ymh1,[]]] }

    for j in dicovrai.values ():
        for i in tableau5milieu.values():


            if [j[0],j[1],[]] in  i:
                n=i.index([j[0],j[1],[]])
                i[n][2].append (j[2][1])


                if i[0][2] == ["black"] and i[1][2] == ["black"] and i[2][2] == ["black"]:
                    for cle,valeur in tableau5milieu.items ():
                        if valeur == i:
                            moulinlst.append ([cle,["black"]])
                            if [cle,["black"]] not in vieuxmoulin:
                                vieuxmoulin.append ([cle,["black"]])
                                vieuxmoulin.append (1)

                if i[0][2] == ["white"] and i[1][2] == ["white"] and i[2][2] == ["white"]:
                    for cle,valeur in tableau5milieu.items ():
                        if valeur == i:
                            moulinlst.append ([cle,["white"]])
                            if [cle,["white"]] not in vieuxmoulin:
                                vieuxmoulin.append ([cle,["white"]])
                                vieuxmoulin.append (1)

    for test in moulinlst:
        for testvieux in vieuxmoulin:
            if test ==testvieux:
                index=vieuxmoulin.index (test)

                if vieuxmoulin[index+1] == 1:
                    boucle=0
                    while boucle!=1:
                        boucle = deletepion (moulinlst,dico,lst,vieuxmoulin,listepion )
                    vieuxmoulin[index+1]+=2

    b=0
    while b!= (len (vieuxmoulin)):
        if vieuxmoulin[b] not in moulinlst:
            print (vieuxmoulin[b+1])
            vieuxmoulin[b+1]=1
            print (vieuxmoulin[b+1])
        b+=2


def deletepion (moulinlst,dico,lst,vieuxmoulin,listepion ):
    couleur=[]
    m=0
    while m != len (vieuxmoulin):
        if vieuxmoulin[m][1][0] == "white" and vieuxmoulin [m+1]:

            for dic,value in dico.items():
                if value [2][1] == "black":
                    couleur.append (value)

            x,y = attend_clic_gauche()
            for k in lst:

                if abs (x- k[0])<10 and abs (y-k[1])<10:

                    for c in couleur:


                        if [k[0],k[1]] == [c[0],c[1]]:
                            efface (c[2][2])
                            dico.pop (c[2][2])
                            listepion.remove ([k[0],k[1]])
                            return 1



        if  vieuxmoulin[m][1][0] == "black" and vieuxmoulin [m+1]:

            for dic,value in dico.items():
                if value [2][1] == "white":
                    couleur.append (value)


            x,y = attend_clic_gauche()
            for k in lst:
                if abs (x- k[0])<10 and abs (y-k[1])<10:

                    for c in couleur:

                        if [k[0],k[1]] == [c[0],c[1]]:
                            efface (c[2][2])
                            dico.pop (c[2][2])
                            listepion.remove ([k[0],k[1]])
                            return 1
        m+=2

    else:
        return 0



def arret (dico):
    blanc =[]
    noir =[]
    for i in dico.values():

        if i[2][1]== "black":
            noir.append (i)
        else:
            blanc.append (i)
    if len (blanc) == 2 :
        efface_tout()
        texte(xgm,ygm, chaine="Pion noir gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
        return True
    if len (noir) ==2:
        efface_tout()
        texte(xgm,ygm, chaine="Pion noir gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
        return True









plateau_6(cote,lst)
attend_fermeture ()
ferme_fenetre()