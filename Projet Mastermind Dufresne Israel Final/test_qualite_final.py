# DUFRESNE Erwan et ISRAEL Richard
# MASTERMIND

from random import *

import random
[]


couleur = ["Rouge","Bleu","Jaune","Vert","Orange","Turquoise","Gris","Mauve"]
couleur2 = ["Rouge","Bleu","Jaune","Vert","Orange","Turquoise","Gris","Mauve"]


#Partie 1: Ordinateur qui choisit les couleurs




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
    cl=ci
    
    
initialisation_jeu()

def selection_combi():
    """
    Cette fonction va choisir 4 couleurs aléatoirement dans la liste "couleur"
    definie préalablement
    C.U : combinaison est un liste : type()==list
    """
    global combinaison
    combinaison = []
    for i in range(4):
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
    #print (l)
    assert len(l)==pion
    for e in l:
        if e not in couleur :
            return False
    return True



def placement_et_couleur(l,lo2):
    """
    cette fonction renvoie, en fonction de la liste l en parametre et de la
    combinaison choisie au départ :
    - noir si c'est la bonne couleur et à la bonne place
    - blanc si c'est la bonne couleur mais à la mauvaise place
    C.U : l est une liste, combinaison est une liste : type()==list
    """
    assert analyse_reponse(l)==True
    noir=0
    blanc=0
    c=[e for e in lo2]
#    print("combinaison =",c)                               #######################   POUR VOIR COMBINAISON ORDI
    for i in range(pion):
        if l[i] in c and l[i]==c[i]:
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


#print(placement_et_couleur(["Rouge","Bleu","Orange","Vert"],["Jaune","Bleu","Orange","Rouge"])," on a normalement 2,1")


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
    return combinaison_testee_par_ordinateur

#print('test choix :',decision_combinaion_aléatoire(ens_combi))             
    



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


def partie_2_programme_final():
    """
    Permet de mettre en corrélation le travail des différents programmes afin que la partie numéro 1 du projet
    et la partie numéro 2 du projet, se répondent. Ainsi le nombre retourné à la fin du programme est le nombre d'essai nécessaire
    à l'ordinateur pour trouver la combinaison secrète. Si il faut plus de 10 essai à l'ordinateur (se qui n'arrive jamais)
    le nombre retourné à la fin est un nombre immense (9999999).
    C.U : réponse -> int
    """    
    ensemble_des_choix_restants = [e for e in ens_combi]
    combi_a_trouver = decision_combinaion_aléatoire(ensemble_des_choix_restants)
    #print('a find ',combi_a_trouver)
    essai = decision_combinaion_aléatoire(ensemble_des_choix_restants)
    #print('essai ' ,essai)
    for i in range (1,11):
        nombre_d_essai=i
        #print(i)
        essaié=[e for e in essai]
        verdict=placement_et_couleur(essaié,combi_a_trouver)
        #print(verdict)
        lverdict=list(verdict)
        lo=str(verdict[0]),str(verdict[1])
        l=list(lo)
        #print(l)
        reste_des_possibilitees = reduction_de_lensemble_des_combinaisons_possibles(essai,l,ensemble_des_choix_restants)
        
        ensemble_des_choix_restants = reste_des_possibilitees
        #print(len(ensemble_des_choix_restants))
        if len(ensemble_des_choix_restants)==1:
            return nombre_d_essai
        essai = decision_combinaion_aléatoire(ensemble_des_choix_restants)
    return 9999999

#print("nombre d'essai, ma gueule",partie_2_programme_final())




x=100

def qualité_algorithme(x):
    """
    Permet de faire fonctionner le programme précédent x fois.
    Une fois ces x parties réalisées, ceette fonction renvoie un tuple
    de type (a,b,c) où a est le nombre minimum d'essais necessaires qu'il a fallu à l'ordinateur pour trouver la combinaison secrète de l'utilisateur durant les x parties
    c est le nombre maximum d'essais necessaires qu'il a fallu à l'ordinateur pour trouver la combinaison secrète de l'utilisateur durant les x parties
    b est la moyenne des nombres d'essais necessaires pour trouver la combinaison secrète de l'utilisateur durant les x parties
    C.U : x est du type int ; la réponse est du type tuple -> (a,b,c) ; a, b et c sont du type int
    """
    stock_essai = []
    stock_moyenne = 0
    t=tuple()
    for i in range (1,x+1):
        r = partie_2_programme_final()
        stock_essai = stock_essai + [r]
        stock_moyenne = stock_moyenne + r
    m=max(stock_essai)
    mi=min(stock_essai)
    moyenne = stock_moyenne/(x)
    t=(mi,moyenne,m)
    #print(type(t))
    print("Sur ",x," parties, l'ordinateur à effectué ce score : ",t," c'est à dire qu'en moyenne, il a trouvé la solution en ",t[1]," coups,\nsans jamais faire plus de ",t[2]," coups et moins de ",t[0]," coups.")
    return t

qualité_algorithme(x)
qualité_algorithme(x)
qualité_algorithme(x)







