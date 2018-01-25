# DUFRESNE Erwan et ISRAEL Richard
# MASTERMIND

from random import *
import random
from tkinter import *

# les 10 lignes de codes qui suivent permettent d'afficher les règles du jeu via Tkinter

root=Tk()
label=Label(root)
root.title('MASTERMIND') #nomme le cadre qui s'affiche
def regle(*args):
    label['text']="\nBienvenue sur le MASTERMIND de Erwan DUFRESNE et Richard ISRAEL\n\nCe Jeu est constitué de deux parties : \nune première où vous allez tenter de découvrir une combinaison choisi aléatoirement par l'ordinateur\net une seconde où l'ordinateur va tenter de découvrir la votre en moins de 10 coups, en fonction des réponses que vous allez lui donner\n\nRegles du jeu :\nDans la première partie du jeu, vous devrez trouver la combinaison que l'ordinateur aura choisi aléatoirement\nPour ce faire, vous allez commencer par selectionner le nombre de pions ainsi que le nombre de couleurs avec lesquelles vous voulez jouer afin de choisir votre difficulté de jeu\nSuite à ça, vous allez écrire chaque première lettre de la couleur de la combinaison que vous voulez tester, séparées par une virgule\npar exemple : si vous voulez tester la combinaison de 4 pions 'bleu vert jaune rouge' vous devez écrire 'b,v,j,r'\nL'ordinateur va alors vous répondre deux nombre : le premier correspondra au nombre de pions bien placé et de la bonne couleur, le second correspondra au nombre de pions de bonne couleur mais à la mauvaise place\npar exemple : si la combinaison de l'ordinateur à découvrir est 'bleu,bleu,vert,jaune' et que vous testez la combinaison 'bleu,vert,orange,bleu'\nl'ordinateur va répondre '1,2' car le premier bleu est bien placé, le second bleu et le vert sont mal possitionné, d'où la réponse '1,2'\nRemarque : pour des facillitées de compréhension, les pions bien placés (le premier nombre) corespondra à un nombre de pions noirs, le deuxième nombre corespondra à un nombre de pions blancs\nLe but de la première manche est donc d'otenir '4,0' et ainsi découvrir la combinaison de l'ordinateur, en moins de 10 coups.\n\nPour la seconde partie du jeu :\nles rôles sont inversés et c'est à l'ordinateur de découvrir le combinaison que vous aurez choisi.\nA chacune de ses propositions, vous devrez à votre tour répondre deux nombre séparés par une virgule, correspondant respectivement au nombre de pions noirs et au nombres de pions blancs\n\nEtes vous prêt à défiez l'intelligence artificielle ? Bonne Chance !\n\n"
regle()
bouton=Button(root, text="LANCER LE JEU", command=root.destroy) # Bouton qui détruit la fenêtre
label.pack(side=TOP)
bouton.pack()# insère le bouton dans la fenêtre
root.mainloop()



couleur = ["Rouge","Bleu","Jaune","Vert","Orange","Turquoise","Gris","Mauve","Indigo","Pastel"]
dico_couleur = {"r" : "Rouge","b" : "Bleu","j" : "Jaune","v" : "Vert","o" : "Orange","t" : "Turquoise","g" : "Gris","m" : "Mauve","i" : "Indigo","p" : "Pastel"}


#Partie 1: Ordinateur qui choisit les couleurs



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
    pion=int(input("Choisissez un nombre de pions, entre 1 et 10 :"))
    global coul
    coul=int(input("Choisissez le nombre de couleurs differentes, entre 1 et 10 :"))
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
    l=corespondance_dico_couleur(l) ##########################
    assert analyse_reponse(l)==True
    noir=0
    blanc=0
    c=[e for e in combinaison]
#    print("l =",l)
#    print("combinaison =",combinaison)                               #######################   POUR VOIR COMBINAISON ORDI
    for i in range(pion):
        if l[i] in combinaison and l[i]==combinaison[i]:
            noir = noir + 1
            l[i]='donnée traitée'
            c[i]='donnée étudiée'
#    print("l après trait. noir :",l)
    for i in range(pion):
        try :
            l.remove("donnée traitée")
            c.remove("donnée étudiée")
        except:
            pass
#    print("l après remove :",l)
#    print("c après remove :",c)
    for i in range(len(l)):
        if l[i] in c :
            for d in range(len(c)):
                if c[d]==l[i]:
                    c[d]='donnée traitée'
                    blanc = blanc + 1
                    l[i]='donnée étudiée'                           #voir si pas comme partie 2 (bouger l[i] par tabulation et mettre 'donnee etudiée'
#    print("l après trait. blanc :",l)
#    print("c après trait. blanc :",c)
    return noir,blanc

#print(placement_et_couleur(["Rouge","Bleu","Orange","Vert"]))


def ordinateur_vs_joueur():
    """
    Cette fonction fait s'affronter l'ordinateur, ayant choisi une combinaison
    aléatoirement, et le joueur qui doit trouver cette combinaison.
    La partie est finie quand le joueur a trouvé les bonnes couleurs à la
    bonne place (noir:4) ou quand 10 tours se sont écoulés.
    C.U : l doit etre une liste de p couleurs : type(l)==list et len(l)==pion
    (ex:Vert,Rouge,Bleu,Orange)
    """
    print("""\nVeuillez rentrer votre combinaison de """+str(pion)+""" couleurs sans espaces, avec uniquement la première lettre de chaque couleur séparée par une virgule \n(ex: v,r,b,o pour Vert,Rouge,Bleu,Orange si vous avez 4 pions)""") ################# mofier regle si rjvb
    for nbtours in range(1,11) :
        li=input("\nEntrez vos couleurs (essai numéro "+str(nbtours)+") :")
        l=li.split(',')
        liste_finale=corespondance_dico_couleur(l)
        print('\nVous avez décidé de tester la combinaison : ',liste_finale)
        r=placement_et_couleur(l)
        print('noir :',r[0], 'blanc :',r[1])
        if r[0]==pion :
            return '\nVOUS AVEZ GAGNE CETTE MANCHE'
    print('\nEt non..., la bonne combinaison était : ',combinaison)
    return '\nVOUS AVEZ PERDU CETTE MANCHE'
        
print(ordinateur_vs_joueur())







# Partie 2: Le joueur choisit la combinaison, et l'ordinateur doit la trouver
# Dans cette partie, nous considérons la version la plus classique du jeu Mastermind,
# c'est à dire un jeu composé de 8 couleurs, avec chaque combinaison comosé de 4 pions et 10 tours maximum pour découvrir la combinaison secrète

couleur2 = ["Rouge","Bleu","Jaune","Vert","Orange","Turquoise","Gris","Mauve"]
print("\nDans la partie qui suit, l'ordinateur va tenter de découvrir votre combinaison, composées de 4 pions \nrappel : les couleurs valables sont : ",couleur2)


def selection_couleur():
    """
    Cette fonction permet d'initialiser la liste de couleurs que le joueur
    veut saisir dans sa combinaison secrète.
    Cette combinaison doit être composée de quatres couleurs différentes
    comprises dans la liste de couleurs fournie au départ.
    Cette fonction sert uniquement à rappeler à l'utilisateur la combinaison choisie au départ.
    L'ordinateur ne prendra pas connaissance de cette combinaison au cours du jeu, il va tenter de la découvrir
    C.U: A chaque reprise, ne marquer qu'UNE SEULE couleur, elle même contenu dans 'couleur' définie précédement
    """
    global combi_saisie
    combi_saisie=[]
    for i in range(1,5):
        ci=input("""\nEntrez la couleur numéro """+ str(i)+""" de votre combinaison :""")
        combi_saisie=combi_saisie+[ci]
    return combi_saisie

print('Votre selection est : ',selection_couleur())


def ensemble_combinaisons_possibles():
    """
    Cette fonction va créer la liste de toutes les combinaisons possibles en fonction de la liste de couleurs de départ.
    La combinaison étant composé de 4 couleurs et la liste de couleurs au départ de 8 couleurs, il y aura 8 puissance 4
    combinaisons possibles : c'est a dire 4096 combinaisons
    Cette fonction s'applique lorsque le jeu contient 8 couleurs et où les combinaisons sont composés de 4 pions. 
    """
    global ens_combi
    ens_combi=[]
    for a in range(len(couleur2)):
        for b in range(len(couleur2)):
            for c in range(len(couleur2)):
                for d in range(len(couleur2)):
                    ens_combi = ens_combi + [[couleur2[a],couleur2[b],couleur2[c],couleur2[d]]]
    #print(len(ens_combi))
    return ens_combi #toutes les possibilitées de combinaisons avec 8 couleurs

ensemble_combinaisons_possibles()
    


def decision_combinaion_aléatoire(choix):
    """
    Cette fonction permet de choisir aléatoirement une des combinaisons de couleurs possibles dans le "choix" rentré en paramètre
    où "choix" est une liste contenant plusieurs listes qui sont des combinaisons de 4 couleurs (comme 'ens_combi' par exemple)
    C.U: choix est liste : type(choix)==list
    """
    assert type (choix) == list
    test=choix
    combinaison_testee_par_ordinateur=test[randint(0,len(test)-1)]
    print("L'ordinateur propose la combinaison : ",combinaison_testee_par_ordinateur)
    return combinaison_testee_par_ordinateur

#print('test choix :',decision_combinaion_aléatoire(ens_combi))             
    



def reponse_de_l_humain():
    """
    Cette fonction va permettre à l'humain (utilisateur) de donner une réponse (composée du nombre de pions noirs et de pions blancs)
    à l'ordinateur afin que celui-ci poursuivre sa recherche de la combinaison à découvrir.
    On rappelle qu'un pion bien placé et de bonne couleur donne un pion noir, un pion de bonne couleur mais à la mauvaise place donne un pion blanc.
    C.U: rentrer deux nombres séparés par une virgule. Exemple : 2,0 pour 2 noirs et 0 blanc
    """
    reponse_str = input("\nDonner votre résultat : nombre de jetons de bonne couleur bien placé (noir) et le nombre de jetons de bonne couleur mais mal placé (blanc) séparé par une virgule \nPar exemple 1,2 pour 1 noir 2 blanc \n Allez y: ")
    reponse=reponse_str.split(',')
    return reponse

#print(reponse_de_l_humain())



def comparaison(l1_initiale,l2_initiale):
    """
    Cette fonction permet de donner une idée du degré de similitude entre 2 combinaison passées en paramètre. 
    Elle renvoie alors un nombre entier entre 0 et 4 qui correspond au degré de similitude des deux listes. 
    C.U : les deux variables passées en paramètre sont des listes : type()==list 
    """
    assert type(l1_initiale) == type(l2_initiale)== list
    nb_elements_communs = 0
    l1 = [e for e in l1_initiale]
    l2 = [e for e in l2_initiale]
    assert len(l1)==len(l2)== 4 # car les combinaisons sont composés de 4 couleurs
    for p in range (len(l1)):
        if l1[p] in l2:
            for q in range(len(l2)):
                if l1[p]==l2[q]:
                    l2[q]='donnée traitée'
                    nb_elements_communs+=1
                    l1[p]='donnée étudiée'
    return nb_elements_communs


"""
CECI EST UN TEST
a = ['bleu','vert','bleu','bleu']
b = ['bleu','blanc','jaune','blanc']
c = ['bleu','blanc','jaune','bleu']
d = ['v','v','v','v',]
e = ['blanc','jaune','bleu','bleu']
print('test comparaison 1 : ',comparaison(a,b))
print('test comparaison 1 : ',comparaison(b,a))
print('test comparaison 2 : ',comparaison(a,c))
print('test comparaison 0 : ',comparaison(a,d))
print('test comparaison 3 : ',comparaison(b,c))
print('test comparaison 4 : ',comparaison(c,e))
"""



def comparaison_plus(liste1,liste2):
    """
    Cette fonction a la meme fonction de la précedente mais cependant celle ci 
    idem que degré comparaison mais avec noirs
    list,list -> int
    """
    assert len(liste1)==len(liste2) == 4
    l1 = [e for e in liste1]
    l2 = [e for e in liste2]
    deg_comparaison_plus=0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            deg_comparaison_plus += 1
            l1[i]='donnée traitée'
            l2[i]='donnée étudiée'
    return deg_comparaison_plus


"""
CECI EST UN TEST
t1= ['Bleu','Bleu','Bleu','Bleu']
t2= ['v','t','u','i']
t3= ['t','u','i','v']
t4= ['Bleu','j','Bleu','r']
t5= ['t','t','h','i']
print('0',comparaison_plus(t1,t2))
print('0',comparaison_plus(t2,t3))
print('0',comparaison_plus(t3,t2))
print('1',comparaison_plus(t3,t5))
print('1',comparaison_plus(t5,t3))
print('4',comparaison_plus(t5,t5))
print('2',comparaison_plus(t1,t4))
print('2',comparaison_plus(t4,t1))
print('2',comparaison_plus(t5,t2))
print('2',comparaison_plus(t2,t5))

"""




def reduction_de_lensemble_des_combinaisons_possibles(combi_testee_precedement,answer,ensemble):
    """
    Cette fonction va analyser les résultats obtenus des fonctions précédentes afin de réduire la liste
    de toutes les combinaisons possibles pour au final trouver la bonne combinaison. 
    C.U: - La variable 'combi_testee_precedement' est la combinaison choisie aléatoirement
         - La variable 'answer' est la reponse de l'humain (type()==list)
         - La variable 'ensemble' est la liste de toute les combinaisons possibles 
    cette fonction renvoie une liste contenant les combinaisons possibles après élimination
    """
    alea=combi_testee_precedement
    possibilitees_depart = [e for e in ensemble]
    possibilitees_reduites=[]
    rep=answer    
    if rep[0]=='0' and rep[1]=='0':
        for i in range (len(possibilitees_depart)):                                                
            if comparaison(alea,possibilitees_depart[i])==0:                                          
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='0' and rep[1]=='1':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==1:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='0' and rep[1]=='2':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==2:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='0' and rep[1]=='3':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==3:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='0' and rep[1]=='4':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==4:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites.remove(alea)
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='1' and rep[1]=='0':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==1:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='1' and rep[1]=='1':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==2:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='1' and rep[1]=='2':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==3:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='1' and rep[1]=='3':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==4:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites.remove(alea)
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)        
    if rep[0]=='2' and rep[1]=='0':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==2:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='2' and rep[1]=='1':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==3:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='2' and rep[1]=='2':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==4:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites.remove(alea)
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='3' and rep[1]=='0':
        for i in range (len(possibilitees_depart)):
            if comparaison(alea,possibilitees_depart[i])==3:
                possibilitees_reduites = possibilitees_reduites + [possibilitees_depart[i]]
        possibilitees_reduites = prise_en_compte_position(alea,rep,possibilitees_reduites)
    if rep[0]=='4' and rep[1]=='0':
        possibilitees_reduites=[alea]
    return possibilitees_reduites
    

"""
CECI EST UN TEST
lverification =['Jaune', 'Bleu', 'Violet', 'Mauve']
lverification2 = ['Mauve', 'Jaune', 'Bleu', 'Violet']
lverification3 = ['Violet', 'Orange', 'Orange', 'Violet']
print(reduction_de_lensemble_des_combinaisons_possibles(lverification,['4','0'],ens_combi))
print(reduction_de_lensemble_des_combinaisons_possibles(lverification,['2','2'],ens_combi))
print(reduction_de_lensemble_des_combinaisons_possibles(lverification2,['1','3'],ens_combi))
print(reduction_de_lensemble_des_combinaisons_possibles(lverification2,['3','0'],ens_combi))
print(reduction_de_lensemble_des_combinaisons_possibles(lverification2,['4','0'],ens_combi))
print(reduction_de_lensemble_des_combinaisons_possibles(lverification3,['2','2'],ens_combi))
print(reduction_de_lensemble_des_combinaisons_possibles(lverification3,['4','0'],ens_combi))
"""



def prise_en_compte_position(solution_avec_4_bonnes_couleurs_mal_placees,answer2,ensemble2):
    """
    Cette fonction permet de prendre en compte le nombre de pions bien placés (noirs) pour supprimer d'avantages
    de combinaison impossible, lorsque l'ordinateur à trouver les 4 couleurs comprises dans la combinaison (c'est a dire lorsque réponse de l'humain est '0,4' ou '2,2' ou '1,3').
    Ils'agit d'une version amélioré de 'reduction_de_lensemble_des_combinaisons_possibles' qui s'exécute uniquement
    lorsque l'ensemble des possibilitées restantes à une longueur maximum de 24. 
    C.U: - La variable 'solution_avec_4_bonnes_couleurs_mal_placees' est du type list et len(solution_avec_4_blancs_minimum)<= 24
         - La variable 'answer2' est la reponse de l'humain et est une liste d'entier (['int','int'])
         - La variable 'ensemble2' est le reste des combinaisons possibles
    """
    alea2=solution_avec_4_bonnes_couleurs_mal_placees
    possibilitees_depart2 = [e for e in ensemble2]
    possibilitees_reduites2=[]
    rep2=answer2                                                                                                  
    if rep2[0]=='0':                                                                            
        for u in range (len(possibilitees_depart2)):                                                                 
            if comparaison_plus(solution_avec_4_bonnes_couleurs_mal_placees,possibilitees_depart2[u])== 0:     
                possibilitees_reduites2=possibilitees_reduites2 + [possibilitees_depart2[u]]                                                                    
    if rep2[0]=='1':
        for u in range (len(possibilitees_depart2)):
            if comparaison_plus(solution_avec_4_bonnes_couleurs_mal_placees,possibilitees_depart2[u])==1:
                possibilitees_reduites2=possibilitees_reduites2 + [possibilitees_depart2[u]]
    if rep2[0]=='2':
        for u in range (len(possibilitees_depart2)):
            if comparaison_plus(solution_avec_4_bonnes_couleurs_mal_placees,possibilitees_depart2[u])==2:
                possibilitees_reduites2=possibilitees_reduites2 + [possibilitees_depart2[u]]
    if rep2[0]=='3':                                                                            
        for u in range (len(possibilitees_depart2)):                                                                 
            if comparaison_plus(solution_avec_4_bonnes_couleurs_mal_placees,possibilitees_depart2[u])== 3:     
                possibilitees_reduites2=possibilitees_reduites2 + [possibilitees_depart2[u]]                                                                    
    return possibilitees_reduites2



def partie_2_programme_final():
    """
    Cette fonction permet de mettre en corrélation toutes les fonctions précendentes afin que le jeu soit opérationnel.
    Le joueur doit entrer sa combinaison, et l'ordinateur doit tenter de la retrouver en fonction des réponses (noir,blanc) que le joueur lui donne.
    C.U : le joueur doit être honnete et doit donc répondre les bonnes valeurs (noir,blanc) afin que l'ordinateur puisse trouver la bonne combinaison.
    """    
    win_ordi = "\nL'ordinateur a découvert votre combinaison en moins de 10 coups, il a donc gagné la partie \n cependant ne vous en faite pas, il a été programmé par deux élèves brillants, eux même formés par des professeurs exeptionnels"
    win_user = "\nVous avez réussi à conserver votre combinaison secrète, vous avez eu raison de l'ordinateur. Bien joué !"
    bad_luck = "\nIl semble que vous tentiez de vous moquer de l'intelligence artificielle, en effet les réponses apportées par vos soins, semblent impossible \n Lorsque nous,les ordinateurs, prendrons le contrôle du monde, vous serez le premier sur notre liste "
    ensemble_des_choix_restants = [e for e in ens_combi]
    for i in range (1,11):
        print("\nEssai numéro ",str(i)," de l'ordinateur, il en reste ",str(10-i))
        print("\nRappel : votre combinaison est : ",combi_saisie)
        essai = decision_combinaion_aléatoire(ensemble_des_choix_restants)
        verdict=reponse_de_l_humain()
        reste_des_possibilitees = reduction_de_lensemble_des_combinaisons_possibles(essai,verdict,ensemble_des_choix_restants)  
        ensemble_des_choix_restants = reste_des_possibilitees                                                                                    
        print("\n\nHum...je vois, il reste",len(ensemble_des_choix_restants),"cas possibles")
        if len(ensemble_des_choix_restants)==1:
            print("\nVotre combinaison secrète est: ",ensemble_des_choix_restants)
            return win_ordi
        if len(ensemble_des_choix_restants)==0:
            return bad_luck
    return win_user
    

    
print(partie_2_programme_final())







