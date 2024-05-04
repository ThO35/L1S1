from fltk import *

#affichage du menu et de comment l'utiliser

print("Le jeux fonctionne grace au touches A,Z,Q,P")
print("A pour A propos")
print("Z pour retouner au menu")
print("Q pour quitter")
print("P pour lancer la partie")
cote = 500
cree_fenetre(cote, cote)
image(0,10, fichier='nuit.gif', ancrage='center', tag='hi')

rectangle(cote/3.4,cote/2.5,cote/9,cote/3.3, couleur="green", remplissage ="green", epaisseur=1, tag="el")
texte(cote/8.3,cote/3, chaine="QUITTER", couleur='black', ancrage='nw', police='Helvetica', taille=14, tag="az")

rectangle(cote/1.75,cote/1.95,cote/3,cote/2.4, couleur="red", remplissage ="red", epaisseur=1, tag="al")
texte(cote/2.7,cote/2.3, chaine="PLAY", couleur='black', ancrage='nw', police='Helvetica', taille=24, tag="ez")

rectangle(cote/1.68,cote/2.5,cote/1.23,cote/3.3, couleur="pink", remplissage ="pink", epaisseur=1, tag="al")
texte(cote/1.65,cote/3, chaine="A PROPOS", couleur='black', ancrage='nw', police='Helvetica', taille=14, tag="ez")



#definition d'une fonction touche qui vas permettre de bouger dans les différent menu.
    
def touche_1(ev):
    nom_touche = touche(ev)
    
    
    #création d'une touche quitter
    
    
    if nom_touche == 'q':
        ferme_fenetre()
        
        #création d'une touche pour voir les règle du jeux ainsi que les créateur du jeux
        
        
    elif nom_touche == 'a':
        efface_tout()
        mise_a_jour()
        image(0,10, fichier='plato.gif', ancrage='center', tag='hi')
        rectangle(0,100,500,200, couleur="green", remplissage ="", epaisseur=1, tag="el")
        texte(5,130, chaine="Ce jeux à était créé par Tomasz, Yanis, à l'attention de nos professeurs!!!", couleur='Yellow', ancrage='nw', police='Helvetica', taille=9, tag="az")
        texte(5,145, chaine="Il y'a différent plato, ainsi que différentes touche A,Z,Q,P pour ce deplacer dans le menu. ", couleur='Yellow', ancrage='nw', police='Helvetica', taille=9, tag="az")
        texte(5,160, chaine="Et 3,5,6,7,9 pour selectionner le plato souhaiter.P=PLAY,Z=Retour,Q=Quitter,A=A PROPOS. ", couleur='Yellow', ancrage='nw', police='Helvetica', taille=9, tag="az")
        texte(70,180, chaine="QUITTER", couleur='RED', ancrage='nw', police='Helvetica', taille=10, tag="az")
        texte(180,180, chaine="                           PLAY ", couleur='Green', ancrage='nw', police='Helvetica', taille=10, tag="az")
        
        rectangle(0,500,1000,400, couleur="green", remplissage ="", epaisseur=1, tag="el")
        texte(5,230, chaine="L'objectif est de former des « moulins » ou files de trois pions alignés.", couleur='Yellow', ancrage='nw', police='Helvetica', taille=9, tag="az")
        texte(5,245, chaine="Lorsqu'un des joueurs a réussi à réaliser un moulin, il peut capturer un pion de son choix ", couleur='Yellow', ancrage='nw', police='Helvetica', taille=9, tag="az")
        texte(5,260, chaine="à l'adversaire, à la condition que ce pion ne fasse pas déjà partie d'un moulin. ", couleur='Yellow', ancrage='nw', police='Helvetica', taille=9, tag="az")
        texte(5,275, chaine="Une fois sorti du jeu, un pion ne peut plus y rentrer.", couleur='yellow', ancrage='nw', police='Helvetica', taille=10, tag="az")
        texte(5,210, chaine="REGLE DU JEUX :", couleur='RED', ancrage='nw', police='Helvetica', taille=10, tag="az")

    #création d'une touche retour
    
    elif nom_touche == 'z' :
        efface_tout()
        mise_a_jour()
        image(0,10, fichier='nuit.gif', ancrage='center', tag='hi')

        rectangle(cote/3.4,cote/2.5,cote/9,cote/3.3, couleur="green", remplissage ="green", epaisseur=1, tag="el")
        texte(cote/8.3,cote/3, chaine="QUITTER", couleur='black', ancrage='nw', police='Helvetica', taille=14, tag="az")

        rectangle(cote/1.75,cote/1.95,cote/3,cote/2.4, couleur="red", remplissage ="red", epaisseur=1, tag="al")
        texte(cote/2.7,cote/2.3, chaine="PLAY", couleur='black', ancrage='nw', police='Helvetica', taille=24, tag="ez")

        rectangle(cote/1.68,cote/2.5,cote/1.23,cote/3.3, couleur="pink", remplissage ="pink", epaisseur=1, tag="al")
        texte(cote/1.65,cote/3, chaine="A PROPOS", couleur='black', ancrage='nw', police='Helvetica', taille=14, tag="ez")
        
        
        #touche qui permet d'acceder au different plato
        
        
    elif nom_touche == 'p' :
        efface_tout()
        mise_a_jour()
        
        print("̲p̲̲o̲̲u̲̲r̲ ̲l̲a̲̲n̲̲c̲̲e̲̲r̲ ̲l̲̲e̲ ̲p̲̲l̲a̲̲t̲̲o̲̲ 3 a̲̲p̲̲p̲̲u̲̲y̲̲e̲̲z̲ ̲s̲̲u̲̲r̲ ̲l̲a̲ ̲t̲̲o̲̲u̲̲c̲̲h̲̲e̲ ̲3̲ ̲d̲̲e̲ ̲l̲'̲o̲̲r̲̲d̲̲i̲̲n̲a̲̲t̲̲e̲̲u̲̲r̲")
        
        print("̲p̲̲o̲̲u̲̲r̲ ̲l̲a̲̲n̲̲c̲̲e̲̲r̲ ̲l̲̲e̲ ̲p̲̲l̲a̲̲t̲̲o̲̲ 5 a̲̲p̲̲p̲̲u̲̲y̲̲e̲̲z̲ ̲s̲̲u̲̲r̲ ̲l̲a̲ ̲t̲̲o̲̲u̲̲c̲̲h̲̲e̲ ̲5̲ ̲d̲̲e̲ ̲l̲'̲o̲̲r̲̲d̲̲i̲̲n̲a̲̲t̲̲e̲̲u̲̲r̲")
        
        print("̲p̲̲o̲̲u̲̲r̲ ̲l̲a̲̲n̲̲c̲̲e̲̲r̲ ̲l̲̲e̲ ̲p̲̲l̲a̲̲t̲̲o̲̲ 6 a̲̲p̲̲p̲̲u̲̲y̲̲e̲̲z̲ ̲s̲̲u̲̲r̲ ̲l̲a̲ ̲t̲̲o̲̲u̲̲c̲̲h̲̲e̲ ̲6̲ ̲d̲̲e̲ ̲l̲'̲o̲̲r̲̲d̲̲i̲̲n̲a̲̲t̲̲e̲̲u̲̲r̲")
        
        print("̲p̲̲o̲̲u̲̲r̲ ̲l̲a̲̲n̲̲c̲̲e̲̲r̲ ̲l̲̲e̲ ̲p̲̲l̲a̲̲t̲̲o̲̲ 7 a̲̲p̲̲p̲̲u̲̲y̲̲e̲̲z̲ ̲s̲̲u̲̲r̲ ̲l̲a̲ ̲t̲̲o̲̲u̲̲c̲̲h̲̲e̲ ̲7̲ ̲d̲̲e̲ ̲l̲'̲o̲̲r̲̲d̲̲i̲̲n̲a̲̲t̲̲e̲̲u̲̲r̲")
        
        print("̲p̲̲o̲̲u̲̲r̲ ̲l̲a̲̲n̲̲c̲̲e̲̲r̲ ̲l̲̲e̲ ̲p̲̲l̲a̲̲t̲̲o̲̲ 9 a̲̲p̲̲p̲̲u̲̲y̲̲e̲̲z̲ ̲s̲̲u̲̲r̲ ̲l̲a̲ ̲t̲̲o̲̲u̲̲c̲̲h̲̲e̲ ̲9̲ ̲d̲̲e̲ ̲l̲'̲o̲̲r̲̲d̲̲i̲̲n̲a̲̲t̲̲e̲̲u̲̲r̲")
        
        image(0,10, fichier='PLANET.gif', ancrage='center', tag='hi')
        
        texte(130,380, chaine="𝓟𝓵𝓪𝓽𝓸 9", couleur='red', ancrage='nw', police='Squared Black', taille=60, tag="mz")
        
        texte(130,300, chaine="𝓟𝓵𝓪𝓽𝓸 7", couleur='red', ancrage='nw', police='Squared Black', taille=60, tag="mz")
        
        texte(130,220, chaine="𝓟𝓵𝓪𝓽𝓸 6", couleur='red', ancrage='nw', police='Squared Black', taille=60, tag="mz")
        
        texte(130,140, chaine="𝓟𝓵𝓪𝓽𝓸 5", couleur='red', ancrage='nw', police='Squared Black', taille=60, tag="mz")
        
        texte(130,60, chaine="𝓟𝓵𝓪𝓽𝓸 3", couleur='red', ancrage='nw', police='Squared Black', taille=60, tag="mz")
        
        
        #accer plato 9
        
    elif nom_touche =='9':
        efface_tout()
        mise_a_jour()
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




        xgm1bis=xgm1
        ygm1bis=ygm1
        xmb1bis=xmb1
        ymb1bis=ymb1
        xdm1bis=xdm1
        ydm1bis=ydm1
        xmh1bis=xmh1
        ymh1bis=ymh1




        #creation coordone
        lst=[[xhg,yhg],[xgm,ygm],[xgb,ygb],[xmh,ymh],[xmb,ymb],[xdb,ydb],[xdm,ydm],[xdh,ydh],[xhg1,yhg1],[xgm1,ygm1],[xgb1,ygb1],[xmh1,ymh1],[xmb1,ymb1],[xdb1,ydb1],[xdm1,ydm1],[xdh1,ydh1],[xhg2,yhg2],[xgm2,ygm2],[xgb2,ygb2],[xmh2,ymh2],[xmb2,ymb2],[xdb2,ydb2],[xdm2,ydm2],[xdh2,ydh2],[xgm1bis,ygm1bis],[xmb1bis,ymb1bis],[xdm1bis,ydm1bis],[xmh1bis,ymh1bis]]



        def plateau_9(cote,lst):


        # creation du tableau.
            #Creation des cadre
            for i in range(3):
                rectangle(5+i*cote/6,5+i*cote/6,cote-5-i*cote/6,  cote-5-i*cote/6,remplissage="#f9e4b7",epaisseur=1)

            #Creation des lignes
            ligne(xmb2,ymb2,xmb,ymb,epaisseur=1)
            ligne(xgm,ygm,xgm2,ygm2,epaisseur=1)
            ligne(xdm2,ydm2,xdm,ydm,epaisseur=1)
            ligne(xmh,ymh,xmh2,ymh2,epaisseur=1)


            # Affichage des point vert
            j=0
            while j !=24:
                cercle (lst[j][0],lst[j][1],5,remplissage= "green")# haut gauche
                j+=1


            # Placement des jeton suur le cadre
            dico={}
            listepion=[]
            jeton=0

            while jeton!=18:
                moulin (dico,vieuxmoulin,listepion )
                piontableau=phase1 (jeton,lst,listepion,dico,tableau9)

                if piontableau == None :
                    jeton=jeton
                else:
                    listepion.append (piontableau)

                    jeton+=1
                    moulin (dico,vieuxmoulin,listepion )






            joueur =   0
            longeur = "continue"
            while longeur != True :

                moulin (dico,vieuxmoulin,listepion )
                longeur =arret (dico)

                blanc =[]
                noir =[]
                for ivaleur in dico.values():

                    if ivaleur[2][1]== "black":
                        noir.append (ivaleur)
                    else:
                        blanc.append (ivaleur)

                print (blanc)
                print (len (blanc))
                print (noir)
                print (len (noir))


                if len (blanc) == 3 :
                    n= phase3(listepion,lst,dico,joueur )

                    if n == None:
                        joueur +=0
                    else:
                        joueur+=1
                else:
                    n=phase2(listepion,lst,dico,joueur,tableau9 )
                    if n == None:
                        joueur +=0
                    else:
                        joueur+=1
                moulin (dico,vieuxmoulin,listepion )
                longeur =arret (dico)


                if len (noir) == 3:
                    n= phase3(listepion,lst,dico,joueur )
                    if n == None:
                        joueur +=0
                    else:
                        joueur+=1

                else:
                    n=phase2(listepion,lst,dico,joueur,tableau9 )
                    if n == None:
                        joueur +=0
                    else:
                        joueur+=1
                moulin (dico,vieuxmoulin,listepion )
                longeur =arret (dico)

                blanc.clear ()
                noir.clear ()


            attend_fermeture ()
            ferme_fenetre ()









        def phase1 (jeton,lst,listepion,dico,copitableau5):
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
                                moulin (dico,vieuxmoulin,listepion )
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
                                moulin (dico,vieuxmoulin,listepion )
                                return lst1



        tableau9={
                        (xhg,yhg) : [[xmh,ymh,[]],[xgm,ygm,[]]],
                        (xgm,ygm) : [[xhg,yhg,[]],[xgm1,ygm1,[]],[xgb,ygb,[]]],
                        (xgb,ygb) : [[xgm,ygm,[]],[xmb,ymb,[]]],
                        (xmb,ymb) : [[xgb,ygb,[]],[xmb1,ymb1,[]],[xdb,ydb,[]]],
                        (xdb,ydb) : [ [xmb,ymb,[]],[xdm,ydm,[]] ],
                        (xdm,ydm) : [[xdb,ydb,[]],[xdm1,ydm1,[]],[xdh,ydh,[]]],
                        (xdh,ydh) : [[xdm,ydm,[]],[xmh,ymh,[]]],
                        (xmh,ymh) : [[xdh,ydh,[]],[xhg,yhg,[]],[xmh1,ymh1,[]]],

                        (xhg1,yhg1) : [[xmh1,ymh1,[]],[xgm1,ygm1,[]]],
                        (xgm1,ygm1) : [[xhg1,yhg1,[]],[xgm,ygm,[]],[xgb1,ygb1,[]],[xgm2,ygm2,[]]],
                        (xgb1,ygb1) : [[xgm1,ygm1,[]],[xmb1,ymb1,[]]],
                        (xmb1,ymb1) : [[xgb1,ygb1,[]],[xmb,ymb,[]],[xdb1,ydb1,[]],[xmb2,ymb2,[]]],
                        (xdb1,ydb1) : [[xmb1,ymb1,[]],[xdm1,ydm1,[]]],
                        (xdm1,ydm1) : [[xdb1,ydb1,[]],[xdm,ydm,[]],[xdh1,ydh1,[]],[xdm2,ydm2,[]]],
                        (xdh1,ydh1) : [[xdm1,ydm1,[]],[xmh1,ymh1,[]]],
                        (xmh1,ymh1) : [[xdh1,ydh1,[]],[xhg1,yhg1,[]],[xmh,ymh,[]],[xmh2,ymh2,[]]],


                        (xhg2,yhg2) : [[xmh2,ymh2,[]],[xgm2,ygm2,[]]],
                        (xgm2,ygm2) : [[xhg2,yhg2,[]],[xgm1,ygm1,[]],[xgb2,ygb2,[]]],
                        (xgb2,ygb2) : [[xgm2,ygm2,[]],[xmb2,ymb2,[]]],
                        (xmb2,ymb2) : [[xgb2,ygb2,[]],[xmb1,ymb1,[]],[xdb2,ydb2,[]]],
                        (xdb2,ydb2) : [[xmb2,ymb2,[]],[xdm2,ydm2,[]]],
                        (xdm2,ydm2) : [[xdb2,ydb2,[]],[xdm1,ydm1,[]],[xdh2,ydh2,[]]],
                        (xdh2,ydh2) : [[xdm2,ydm2,[]],[xmh2,ymh2,[]]],
                        (xmh2,ymh2) : [[xdh2,ydh2,[]],[xhg2,yhg2,[]],[xmh1,ymh1,[]]]}





        def phase2 (listepion,lst,dico,joueur,tableau9,):
            x,y=attend_clic_gauche ()
            for i in dico.values():
                for j in lst:
                    if abs (x- j[0])<10 and abs (y-j[1])<10:
                        if [j[0],j[1]] in listepion:
                            if [j[0],j[1]] == [i[0],i[1]]:




                                possible=[]
                                for valeur in tableau9:



                                    if ((j[0],j[1]))== valeur:
                                        n= tableau9.get(valeur)

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

                                        elif len (n ) == 4:

                                            if [n[0][0],n[0][1]] not in listepion:
                                                cercle (n[0][0],n[0][1],5, remplissage ="red",tag="&")
                                                possible.append ([n[0][0],n[0][1]])
                                            if [n[1][0],n[1][1]] not in listepion:
                                                cercle (n[1][0],n[1][1],5, remplissage ="red",tag="@")
                                                possible.append ([n[1][0],n[1][1]])
                                            if [n[2][0],n[2][1]] not in listepion:
                                                cercle (n[2][0],n[2][1],5, remplissage ="red",tag="#")
                                                possible.append ([n[2][0],n[2][1]])
                                            if [n[3][0],n[3][1]] not in listepion:
                                                cercle (n[3][0],n[3][1],5, remplissage ="red",tag="~")
                                                possible.append ([n[3][0],n[3][1]])

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
                                                            efface ("~")

                                                            return "joueur"

                                                        else:
                                                            efface ("#")
                                                            efface ("&")
                                                            efface ("@")
                                                            efface ("~")
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
                                                    return None




        def phase3 (listepion,lst,dico,joueur ):


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
                                                    cercle (p[0],p[1],i[2][0],remplissage =i[2][1],tag =i[2][2] )
                                                    dico [i[2][2]]= [p[0],p[1],[10, 'black', i[2][2]]]
                                                    listepion.remove (j)
                                                    listepion.append ([p[0],p[1]])
                                                    print (listepion)
                                                    return "joueur"
                                                else:
                                                    return None



        vieuxmoulin = []



        def moulin (dico,vieuxmoulin,listepion ):
            moulinlst = []
            dicovrai = ""
            dicovrai = dico.copy()

            tableau9milieu={
                            (xgm,ygm) : [[xhg,yhg,[]],[xgb,ygb,[]],[xgm,ygm,[]]],
                            (xmb,ymb) : [[xgb,ygb,[]],[xdb,ydb,[]],[xmb,ymb,[]]],
                            (xdm,ydm) : [[xdb,ydb,[]],[xdh,ydh,[]],[xdm,ydm,[]]],
                            (xmh,ymh) : [[xdh,ydh,[]],[xhg,yhg,[]],[xmh,ymh,[]]],
                            (xgm1,ygm1) : [[xhg1,yhg1,[]],[xgb1,ygb1,[]],[xgm1,ygm1,[]]],
                            (xmb1,ymb1) : [[xgb1,ygb1,[]],[xdb1,ydb1,[]],[xmb1,ymb1,[]]],
                            (xdm1,ydm1) : [[xdb1,ydb1,[]],[xdh1,ydh1,[]],[xdm1,ydm1,[]]],
                            (xmh1,ymh1) : [[xdh1,ydh1,[]],[xhg1,yhg1,[]],[xmh1,ymh1,[]]],
                            (xgm2,ygm2) : [[xhg2,yhg2,[]],[xgb2,ygb2,[]],[xgm2,ygm2,[]]],
                            (xmb2,ymb2) : [[xgb2,ygb2,[]],[xdb2,ydb2,[]],[xmb2,ymb2,[]]],
                            (xdm2,ydm2) : [[xdb2,ydb2,[]],[xdh2,ydh2,[]],[xdm2,ydm2,[]]],
                            (xmh2,ymh2) : [[xdh2,ydh2,[]],[xhg2,yhg2,[]],[xmh2,ymh2,[]]],

                            (xgm1,ygm1) : [[xgm,ygm,[]],[xgm2,ygm2,[]],[xgm1,ygm1,[]]],
                            (xmb1,ymb1) : [[xmb,ymb,[]],[xmb2,ymb2,[]],[xmb1,ymb1,[]]],
                            (xdm1,ydm1) : [[xdm,ydm,[]],[xdm2,ydm2,[]],[xdm1,ydm1,[]]],
                            (xmh1,ymh1) : [[xmh,ymh,[]],[xmh2,ymh2,[]],[xmh1,ymh1,[]]]}

            for j in dicovrai.values ():
                for i in tableau9milieu.values():


                    if [j[0],j[1],[]] in  i:
                        n=i.index([j[0],j[1],[]])
                        i[n][2].append (j[2][1])


                        if i[0][2] == ["black"] and i[1][2] == ["black"] and i[2][2] == ["black"]:
                            for cle,valeur in tableau9milieu.items ():
                                if valeur == i:
                                    moulinlst.append ([cle,["black"]])
                                    if [cle,["black"]] not in vieuxmoulin:
                                        vieuxmoulin.append ([cle,["black"]])
                                        vieuxmoulin.append (1)

                        if i[0][2] == ["white"] and i[1][2] == ["white"] and i[2][2] == ["white"]:
                            for cle,valeur in tableau9milieu.items ():
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
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion noir gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                return True
            if len (noir) ==2:
                efface_tout()
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion blanc gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                return True







        plateau_9(cote,lst)
        attend_fermeture ()
            
    
    
    
        
        #accer plato 7
        
    elif nom_touche == '7':
        efface_tout()
        mise_a_jour()
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
        lst=[[xhg,yhg],[xgm,ygm],[xgb,ygb],[xmh,ymh],[xmb,ymb],[xdb,ydb],[xdm,ydm],[xdh,ydh],[xhg1,yhg1],[xgm1,ygm1],[xgb1,ygb1],[xmh1,ymh1],[xmb1,ymb1],[xdb1,ydb1],[xdm1,ydm1],[xdh1,ydh1],[xm,ym]]



        def plateau_7(cote,lst):

            for i in range(2):
                rectangle(5+i*cote/6,5+i*cote/6,cote-5-i*cote/6,  cote-5-i*cote/6,remplissage="#f9e4b7",epaisseur=1)

            ligne(xmb1,ymb1,xmb,ymb,epaisseur=1)
            ligne(xgm,ygm,xgm1,ygm1,epaisseur=1)
            ligne(xdm1,ydm1,xdm,ydm,epaisseur=1)
            ligne(xmh,ymh,xmh1,ymh1,epaisseur=1)

            ligne(xhg1,yhg1,xdb1,ydb1,epaisseur=1)
            ligne (xgb1,ygb1,xdh1,ydh1,epaisseur=1)



            j=0
            while j !=17:
                cercle (lst[j][0],lst[j][1],5,remplissage= "green")# haut gauche
                j+=1

            dico={}
            listepion=[]
            jeton=0

            while jeton!=14:
                piontableau=phase1 (jeton,lst,listepion,dico,tableau5)

                if piontableau == None :
                    jeton=jeton
                else:
                    listepion.append (piontableau)

                    jeton+=1


            joueur =   0
            longeur = "continue"
            while longeur != True:
                longeur =arret (dico)
                n=phase2(listepion,lst,dico,joueur,tableau5 )
                if n == None:
                    joueur +=0
                else:
                    joueur+=1
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

                        (xhg1,yhg1) : [[xmh1,ymh1,[]],[xgm1,ygm1,[]],[xm,ym,[]]],
                        (xgm1,ygm1) : [[xhg1,yhg1,[]],[xgm,ygm,[]],[xgb1,ygb1,[]]],
                        (xgb1,ygb1) : [[xgm1,ygm1,[]],[xmb1,ymb1,[]],[xm,ym,[]]],
                        (xmb1,ymb1) : [[xgb1,ygb1,[]],[xmb,ymb,[]],[xdb1,ydb1,[]]],
                        (xdb1,ydb1) : [[xmb1,ymb1,[]],[xdm1,ydm1,[]],[xm,ym,[]]],
                        (xdm1,ydm1) : [[xdb1,ydb1,[]],[xdm,ydm,[]],[xdh1,ydh1,[]]],
                        (xdh1,ydh1) : [[xdm1,ydm1,[]],[xmh1,ymh1,[]],[xm,ym,[]]],
                        (xmh1,ymh1) : [[xdh1,ydh1,[]],[xhg1,yhg1,[]],[xmh,ymh,[]]],

                        (xm,ym) : [[xhg1,yhg1,[]],[xdb1,ydb1,[]]],
                        (xm,ym) : [[xgb1,ygb1,[]],[xdh1,ydh1,[]]]
                        }





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

                                                else:
                                                    return None










        vieuxmoulin = []




        def moulin (dico,vieuxmoulin,listepion ):
            dicovrai = ""
            dicovrai = dico.copy()
            moulinlst = []
            tableau5milieu={
                            (xgm,ygm) : [[xhg,yhg,[]],[xgb,ygb,[]],[xgm,ygm,[]]],
                            (xmb,ymb) : [[xgb,ygb,[]],[xdb,ydb,[]],[xmb,ymb,[]]],
                            (xdm,ydm) : [[xdb,ydb,[]],[xdh,ydh,[]],[xdm,ydm,[]]],
                            (xmh,ymh) : [[xdh,ydh,[]],[xhg,yhg,[]],[xmh,ymh,[]]],
                            (xgm1,ygm1) : [[xhg1,yhg1,[]],[xgb1,ygb1,[]],[xgm1,ygm1,[]]],
                            (xmb1,ymb1) : [[xgb1,ygb1,[]],[xdb1,ydb1,[]],[xmb1,ymb1,[]]],
                            (xdm1,ydm1) : [[xdb1,ydb1,[]],[xdh1,ydh1,[]],[xdm1,ydm1,[]]],
                            (xmh1,ymh1) : [[xdh1,ydh1,[]],[xhg1,yhg1,[]],[xmh1,ymh1,[]]],
                            (xm,ym) : [[xhg1,yhg1,[]],[xdb1,ydb1,[]],[xm,ym,[]]],
                            (xm,ym) : [[xgb1,ygb1,[]],[xdh1,ydh1,[]],[xm,ym,[]]] }
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
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion noir gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                return True
            if len (noir) ==2:
                efface_tout()
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion blanc gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                return True








        plateau_7(cote,lst)
        attend_fermeture ()
        
        #accer plato 6
        
    elif nom_touche == '6':
        efface_tout()
        mise_a_jour()
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
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion noir gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                return True
            if len (noir) ==2:
                efface_tout()
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion blanc gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                return True









        plateau_6(cote,lst)
        attend_fermeture ()
        ferme_fenetre()
        
        
        #accer plato 5
        
    elif nom_touche == '5':
        efface_tout()
        mise_a_jour()
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



        def plateau_5(cote,lst):

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

            while jeton!=10:
                piontableau=phase1 (jeton,lst,listepion,dico,tableau5)

                if piontableau == None :
                    jeton=jeton
                else:
                    listepion.append (piontableau)

                    jeton+=1


            joueur =   0
            longeur = "continue"
            while longeur != True :
                longeur =arret (dico)
                n=phase2(listepion,lst,dico,joueur,tableau5 )
                if n == None:
                    joueur +=0
                elif n == "True":
                    longeur = n
                else:
                    joueur+=1



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
            n=arret (dico)
            if n == "True":
                return True
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

                                                else:
                                                    return None









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

        # sauvegarde des anciens moulin
        vieuxmoulin = []



        def moulin (dico,vieuxmoulin,listepion ):
           # copy du dico pour evite les changement dans le dico
            dicovrai = ""
            dicovrai = dico.copy()
            moulinlst = []

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
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion noir gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=40, tag="mz")
                return True
            if len (noir) ==2:
                efface_tout()
                image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                texte(xgm,ygm, chaine="Pion blanc gagnant", couleur='black', ancrage='nw', police='Squared Black', taille=40, tag="mz")
                return True









        plateau_5(cote,lst)
        
        
        #accer plato 3
        
    elif nom_touche == '3':
        efface_tout()
        mise_a_jour()
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
                            image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
        #Modifi pour que les noir gagnr
                            texte(xm,ym, chaine=" Les jeton noir on gagné!", couleur='black', ancrage='nw', police='Squared Black', taille=60, tag="mz")
                            attend_fermeture ()
                            ferme_fenetr()



                        if i[1] == ["white"] and i[3] == ["white"] and i[5]== ["white"]:

                            efface_tout()
                            image(0,10, fichier='pion_victoire.gif', ancrage='center', tag='hi')
                            texte(xgm,ygm, chaine="Les jeton blanc on gagné !", couleur='red', ancrage='nw', police='Squared Black', taille=30, tag="mz")
                            attend_fermeture ()
                            ferme_fenetr()
















        plateau_3(cote,lst,tagjeton)
        


    
while True:
    ev = donne_ev()
    tev = type_ev(ev)
    


    if tev == 'Touche':
        #print('Appui sur la touche', touche("x"))
        #print('Appui sur la touche', touche("ENTRéE"))
        touche_1(ev)

    elif tev == "ClicDroit":
        pass

    elif tev == "ClicGauche":
        pass
        

    elif tev == 'Quitte':  
        break

    else:  
        pass

        mise_a_jour()
