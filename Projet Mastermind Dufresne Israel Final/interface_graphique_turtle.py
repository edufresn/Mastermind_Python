# DUFRESNE Erwan et ISRAEL Richard
# MASTERMIND
from turtle import *
from random import *
import turtle
import random
[]

speed(1000)

couleur = ["red","blue","yellow","green","orange","grey","purple","pink"]
dico_couleur = {"r" : "red","b" : "blue","j" : "yellow","v" : "green","o" : "orange","g" : "grey","m" : "purple","p" : "pink"}


#Partie 1: Ordinateur qui choisit les couleurs


wn = turtle.Screen()      # permet de creer la fenêtre de jeu
wn.bgcolor("lightgreen")  # permet de doner une couleur particulière au fond d'écran de la fenêtre
wn.title("MASTERMIND")    # permet de renommer notre fenêtre de jeu


def Cercle(diam,c) :
    """
    fonction qui permet de créer un cercle avec une couleur de remplissage
    
    'diam' est un int qui correspond au diamètre du disque que l'on souhaite déssiner
    'c' correspond à la couleur de remplissage de notre disque, 'c' est du type str
    """
    setheading(0)
    pencolor("black")
    fillcolor(c)
    begin_fill()
    circle(diam)
    end_fill()


def corespondance_dico_couleur(liste_de_premieres_lettres):
    """
    Cette fonction fait correspondre la première lettre d'une couleur avec un caractère rentré par l'utilisateur
    et qui permet de faire gagner du temps à l'utilisateur, par exemple si l'utilisateur veut écrire "Bleu,Vert,Jaune,Rouge",
    il lui suffit d'écrire "b,v,j,r"
    C.U : la variable passée en paramètre doit etre une liste : type()==list
    """
    lauxiliaire=[e for e in liste_de_premieres_lettres]
    lresultat=[]
    for i in range (len(lauxiliaire)):
        aux=lauxiliaire[i]
        aux2 = dico_couleur[aux]
        lresultat=lresultat +[aux2]
    return lresultat

        
#print(corespondance_dico_couleur(['r','j','r','g']))


def initialisation_jeu():
    """
    Cette fonction va permettre d'initialiser le nombre de pions
    et le nombre de couleurs que le joueur décide de prendre pour sa partie
    C.U: les variables p et c sont des entiers : type()==int et elles sont comprises entre 1 et 10 
    """
    global pion
    pion=4
    global coul
    coul=8
    assert type(pion) == type(coul)== int
    assert 1<=coul<=10 and 1<=pion<=10
    ci=[a for a in couleur]
    global cl
    cl=[]
    for e in range (coul):
        r=random.choice(ci)
        cl = cl + [r]
        ci.remove(r)
    print("""\nVous avez choisi de jouer avec """+str(pion)+""" pions. Les couleurs disponibles sont les suivantes : """+str(cl))

    
initialisation_jeu()


def selection_combi():
    """
    Cette fonction va choisir 4 couleurs aléatoirement dans la liste "couleur"
    definie préalablement
    C.U : combinaison est un liste : type()==list
    """
    global combinaison
    combinaison = []
    for i in range(pion):
        combinaison = combinaison + [(random.choice(cl))]
    return combinaison

selection_combi()


def analyse_reponse(l):
    """
    Cette fonction va analyser la combinaison rentrée par le joueur et renvoyer
    True si toutes les couleurs rentrées sont bien dans la liste de couleurs
    prédefinies; et False sinon
    C.U : l est une liste de p couleurs : type()==list
    """
    assert type(l)==list
    print (l)
    assert len(l)==pion
    for e in l:
        if e not in couleur :
            return False
    return True

#print(analyse_reponse(["Rouge","Bleu","Jaune","Vert"]))
#print(analyse_reponse(["Jaune","Papillon","Rouge","Blanc"]))

        
def placement_et_couleur(l):
    """
    cette fonction renvoie, en fonction de la liste l en parametre et de la
    combinaison choisie au départ :
    - noir si c'est la bonne couleur et à la bonne place
    - blanc si c'est la bonne couleur mais à la mauvaise place
    C.U : l est une liste, combinaison est une liste : type()==list
    """
    l=corespondance_dico_couleur(l)
    assert analyse_reponse(l)==True
    noir=0
    blanc=0
    c=[e for e in combinaison]
    #print("combinaison =",combinaison)                               #######################   POUR VOIR COMBINAISON ORDI
    for i in range(pion):
        if l[i] in combinaison and l[i]==combinaison[i]:
            noir = noir + 1
            l[i]='donnée traitée'
            c[i]='donnée étudiée'
    for i in range(pion):
        try :
            l.remove("donnée traitée")
            c.remove("donnée étudiée")
        except:
            pass
    for i in range(len(l)):
        if l[i] in c :
            for d in range(len(c)):
                if c[d]==l[i]:
                    c[d]='donnée traitée'
                    blanc = blanc + 1
                    l[i]='donnée étudiée'                           
    return noir,blanc


def lose():
    """
    permet d'afficher le texte "lose" en plusieurs couleurs, lorsque la partie est perdue
    le code est long mais necessaire pour afficher un texte sur turtle
    """
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.speed(2000000)
    tess.pensize(5)
    for i in range(50):
        if i%3==1:            
            tess.color("black")
            tess.penup()
            tess.goto(-250,100)
            tess.right(90)
            tess.pendown()
            tess.forward(100)
            tess.left(90)
            tess.forward(60)
            tess.penup()
            tess.forward (35)
            tess.pendown()
            tess.forward (80)
            tess.left(90)
            tess.forward(100)
            tess.left(90)
            tess.forward(80)
            tess.left(90)
            tess.forward(100)
            tess.penup()
            tess.left(90)
            tess.forward (125)
            tess.pendown()
            tess.forward (80)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(80)
            tess.right(90)
            tess.forward(50)
            tess.right(90)
            tess.forward (80)
            tess.penup()
            tess.forward(35)
            tess.pendown()
            tess.forward(80)
            tess.right(180)
            tess.forward(80)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(60)
            tess.right(180)
            tess.forward(60)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(80)
        if i%3==1:
            tess.color("orange")
            tess.penup()
            tess.goto(-250,100)
            tess.right(90)
            tess.pendown()
            tess.forward(100)
            tess.left(90)
            tess.forward(60)
            tess.penup()
            tess.forward (35)
            tess.pendown()
            tess.forward (80)
            tess.left(90)
            tess.forward(100)
            tess.left(90)
            tess.forward(80)
            tess.left(90)
            tess.forward(100)
            tess.penup()
            tess.left(90)
            tess.forward (125)
            tess.pendown()
            tess.forward (80)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(80)
            tess.right(90)
            tess.forward(50)
            tess.right(90)
            tess.forward (80)
            tess.penup()
            tess.forward(35)
            tess.pendown()
            tess.forward(80)
            tess.right(180)
            tess.forward(80)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(60)
            tess.right(180)
            tess.forward(60)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(80)
        if i%3==1:
            tess.color("red")
            tess.penup()
            tess.goto(-250,100)
            tess.right(90)
            tess.pendown()
            tess.forward(100)
            tess.left(90)
            tess.forward(60)
            tess.penup()
            tess.forward (35)
            tess.pendown()
            tess.forward (80)
            tess.left(90)
            tess.forward(100)
            tess.left(90)
            tess.forward(80)
            tess.left(90)
            tess.forward(100)
            tess.penup()
            tess.left(90)
            tess.forward (125)
            tess.pendown()
            tess.forward (80)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(80)
            tess.right(90)
            tess.forward(50)
            tess.right(90)
            tess.forward (80)
            tess.penup()
            tess.forward(35)
            tess.pendown()
            tess.forward(80)
            tess.right(180)
            tess.forward(80)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(60)
            tess.right(180)
            tess.forward(60)
            tess.left(90)
            tess.forward(50)
            tess.left(90)
            tess.forward(80)

def win():
    """
    permet d'afficher le texte "win", en plusieurs couleurs, lorsque la partie est perdue
    le code est long mais necessaire pour afficher un texte sur turtle
    """
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.speed(2000000)
    tess.pensize(5)
    for i in range(50):
        if i%3==1:                                    
            tess.color("red")            
            tess.penup()
            tess.goto(0,0)
            tess.pendown()
            tess.right(60)
            tess.forward(130)
            tess.left(120)
            tess.forward(100)
            tess.right(120)
            tess.forward(100)
            tess.left(120)
            tess.forward (130)
            tess.penup()
            tess.right(60)
            tess.forward(35)
            tess.pendown()
            tess.right(90)
            tess.forward(100)
            tess.penup()
            tess.left(90)
            tess.forward(35)
            tess.pendown()
            tess.left(90)
            tess.forward(100)
            tess.right(140)
            tess.forward(130)
            tess.left(140)
            tess.forward(100)         
        if i%3==1:
            tess.color("blue")           
            tess.penup()
            tess.goto(0,0)
            tess.pendown()
            tess.right(60)
            tess.forward(130)
            tess.left(120)
            tess.forward(100)
            tess.right(120)
            tess.forward(100)
            tess.left(120)
            tess.forward (130)
            tess.penup()
            tess.right(60)
            tess.forward(35)
            tess.pendown()
            tess.right(90)
            tess.forward(100)
            tess.penup()
            tess.left(90)
            tess.forward(35)
            tess.pendown()
            tess.left(90)
            tess.forward(100)
            tess.right(140)
            tess.forward(130)
            tess.left(140)
            tess.forward(100)
        if i%3==2:
            tess.color("yellow")
            tess.penup()
            tess.goto(0,0)
            tess.pendown()
            tess.right(60)
            tess.forward(130)
            tess.left(120)
            tess.forward(100)
            tess.right(120)
            tess.forward(100)
            tess.left(120)
            tess.forward (130)
            tess.penup()
            tess.right(60)
            tess.forward(35)
            tess.pendown()
            tess.right(90)
            tess.forward(100)
            tess.penup()
            tess.left(90)
            tess.forward(35)
            tess.pendown()
            tess.left(90)
            tess.forward(100)
            tess.right(140)
            tess.forward(130)
            tess.left(140)
            tess.forward(100)
            
            

def ordinateur_vs_joueur():
    """
    Cette fonction fait s'affronter l'ordinateur, ayant choisi une combinaison
    aléatoirement, et le joueur qui doit trouver cette combinaison.
    La partie est finie quand le joueur a trouvé les bonnes couleurs à la
    bonne place (noir:4) ou quand 10 tours se sont écoulés.
    De plus, on y applique une partie graphique. C'est à dire que lorsque la combinaison sera testée
    et la réponse de l'ordinateur donnée, on utilisera turtle pour appliquer un aspect graphique à cette fonction
    via la fonction cercle définie précédement
    C.U : l doit etre une liste de 4 couleurs : type(l)==list et len(l)==4
    (ex:v,r,b,o)
    """
    print("""\nVeuillez rentrer votre combinaison de """+str(pion)+""" couleurs sans espaces, avec uniquement la première lettre de chaque couleur séparée par une virgule \n(ex: v,r,b,o pour Vert,Rouge,Bleu,Orange si vous avez 4 pions)""") ################# mofier regle si rjvb
    for nbtours in range(1,11) :
        i=nbtours
        li=input("\nEntrez vos couleurs (essai numéro "+str(nbtours)+") :")
        l=li.split(',')
        liste_finale=corespondance_dico_couleur(l)
        penup()
        goto(-400,-450+(i*80))
        pendown()
        Cercle(20,liste_finale[0])
        penup()
        goto(-300,-450+(i*80))
        pendown()
        Cercle(20,liste_finale[1])
        penup()
        goto(-200,-450+(i*80))
        pendown()
        Cercle(20,liste_finale[2])
        penup()
        goto(-100,-450+(i*80))
        pendown()
        Cercle(20,liste_finale[3])
        print('\nVous avez décidé de tester la combinaison : ',liste_finale)
        r=placement_et_couleur(l)
        print('noir :',r[0], 'blanc :',r[1])
        if r[0]==0 and r[1]==1:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'white')            
        if r[0]==0 and r[1]==2:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'white')            
        if r[0]==0 and r[1]==3:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'white')            
        if r[0]==0 and r[1]==4:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(400,-450+(i*80))
            pendown()
            Cercle(20, 'white')            
        if r[0]==1 and r[1]==0:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
        if r[0]==1 and r[1]==1:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'white')
        if r[0]==1 and r[1]==2:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'white')
        if r[0]==1 and r[1]==3:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(400,-450+(i*80))
            pendown()
            Cercle(20, 'white')            
        if r[0]==2 and r[1]==0:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'black')            
        if r[0]==2 and r[1]==1:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'white')            
        if r[0]==2 and r[1]==2:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'white')
            penup()
            goto(400,-450+(i*80))
            pendown()
            Cercle(20, 'white')
        if r[0]==3 and r[1]==0:
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'black')
        if r[0]==pion :
            penup()
            goto(100,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(200,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(300,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            penup()
            goto(400,-450+(i*80))
            pendown()
            Cercle(20, 'black')
            clearscreen()
            win()   
            return '\nVOUS AVEZ GAGNE CETTE MANCHE'
    print('\nEt non..., la bonne combinaison était : ',combinaison)
    clearscreen()
    lose()
    return '\nVOUS AVEZ PERDU CETTE MANCHE'


print(ordinateur_vs_joueur())






