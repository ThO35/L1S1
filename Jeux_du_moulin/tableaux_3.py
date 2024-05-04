
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
lst=[[xm,ym],[xhg,yhg],[xgm,ygm],[xgb,ygb],[xmh,ymh],[xmb,ymb],[xdb,ydb],[xdm,ydm],[xdh,ydh],[xhg1,yhg1],[xgm1,ygm1],[xgb1,ygb1],[xmh1,ymh1],[xmb1,ymb1],[xdb1,ydb1],[xdm1,ydm1],[xdh1,ydh1],[xhg2,yhg2],[xgm2,ygm2],[xgb2,ygb2],[xmh2,ymh2],[xmb2,ymb2],[xdb2,ydb2],[xdm2,ydm2],[xdh2,ydh2]]

tagjeton=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]




lst=[[xm,ym],[xhg,yhg],[xgm,ygm]
,[xgb,ygb],[xmh,ymh]
,[xmb,ymb],[xdb,ydb]
,[xdm,ydm],[xdh,ydh]]









def plateau_3(cote,lst,tagjeton):



    for i in range(1):
        rectangle(5+i*cote/6,5+i*cote/6,cote-5-i*cote/6,  cote-5-i*cote/6,remplissage="#f9e4b7",epaisseur=1)

    ligne (5+i*cote/6,5+i*cote/6,cote,cote ,epaisseur=1)
    ligne (0,cote,cote,0,epaisseur=1)
    ligne(cote/2,5,cote/2,cote-5,epaisseur=1)
    ligne(5,cote/2,cote-5,cote/2,epaisseur=1)

    j=0
    while j !=9:
        cercle (lst[j][0],lst[j][1],5,remplissage= "green")# haut gauche
        j+=1


    dico={}
    listepion=[]
    jeton=0
    while jeton!=6:

        piontableau=phase1 (jeton,lst,listepion,dico,tagjeton)

        if piontableau == None :
            jeton=jeton
        else:
            listepion.append (piontableau)
            moulin_3 (dico)
            jeton+=1


    joueur=0
    fin = False
    while fin != True:
        n=phase3 (listepion,lst,dico,tagjeton,joueur  )
        if n == None:
            joueur +=0

        else:
            joueur+=1
        print (joueur)













def phase1 (jeton,lst,listepion,dico,tagjeton):
    print (tagjeton)
    lst1=[]

    x,y=attend_clic_gauche ()
    k=0
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




def phase3 (listepion,lst,dico,tagjeton,joueur ):

    x,y=attend_clic_gauche ()

    print (dico)
    for i in dico.values():


        for j in lst:


            if abs (x- j[0])<10 and abs (y-j[1])<10:

                if [j[0],j[1]] in listepion:


                    if [j[0],j[1]] == [i[0],i[1]]:

                        lst1=[]
                        x,y=attend_clic_gauche ()

                        for p in lst:
                            if abs (x- p[0])<10 and abs (y-p[1])<10:
                                lst1.append(p[0])
                                lst1.append(p[1])

                                if lst1 in listepion:
                                    return None

                                else:


                                    if joueur %2 == 0:
                                        if i[2][1] == "white":

                                            moulin_3 (dico)





                                            efface (i[2][2])
                                            cercle (p[0],p[1],i[2][0],remplissage =i[2][1],tag =i[2][2] )
                                            dico [i[2][2]]= [p[0],p[1],[10, 'white', i[2][2]]]


                                            listepion.remove (j)


                                            listepion.append ([p[0],p[1]])




                                            return "joueur"

                                        else:

                                            return None


                                    else:
                                        if i[2][1] == "black":
                                            efface (i[2][2])
                                            moulin_3 (dico)

                                            cercle (p[0],p[1],i[2][0],remplissage =i[2][1],tag =i[2][2] )
                                            dico [i[2][2]]= [p[0],p[1],[10, 'black', i[2][2]]]

                                            listepion.remove (j)
                                            listepion.append ([p[0],p[1]])
                                            print (listepion)
                                            return "joueur"

                                        else:
                                            return None



# si dans la liste de

def moulin_3 (dico):

    copitableau3 = {

            "a":[[xhg,yhg],[],[xmh,ymh],[],[xdh,ydh],[]],

            "b":[[xm,ym],[],[xgm,ygm],[],[xdm,ygm],[]],

            "c":[[xgb,ygb],[],[xmb,ymb],[],[xdb,ydb],[]],

            "d":[[xhg,yhg],[],[xm,ym],[],[xdb,ydb],[]],

            "e":[[xdh,ydh],[],[xm,ym],[],[xgb,ygb],[]],

            "f":[[xhg,yhg],[],[xgm,ygm],[],[xgb,ygb],[]],

            "g":[[xdh,ydh],[],[xdm,ydm],[],[xdb,ydb],[]],

            "h": [[xmh,ymh],[],[xm,ym],[],[xmb,ymb],[]]}

    for i in copitableau3.values():
        for j in dico.values ():
            if [j[0],j[1]] in  i:

                n=i.index([j[0],j[1]])
                i[n+1].append (j[2][1])

                if i[1] == ["black"] and i[3] == ["black"] and i[5] == ["black"]:
                    efface_tout()
#Modifi pour que les noi gagnr
                    texte(xm,ym, chaine=" Les jeton noir on gagné!", couleur='black', ancrage='nw', police='Squared Black', taille=60, tag="mz")
                    attend_fermeture ()
                    ferme_fenetr()



                if i[1] == ["white"] and i[3] == ["white"] and i[5]== ["white"]:

                    efface_tout()
                    texte(xgm,ygm, chaine="Les jeton blanc on gagné !", couleur='red', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                    attend_fermeture ()
                    ferme_fenetr()
















plateau_3(cote,lst,tagjeton)
