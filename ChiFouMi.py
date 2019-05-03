# -*- coding: utf-8 -*-
from random import randint
import os # Pour utiliser les commandes
global NumberOfParts # Variable Global permis de selectionner le nombre des parties pour annoncer le Gagnant
NumberOfParts = 5

def bye(): # Une function qui affiche les CopyRight
    # Color: Une classe qui permis de retourner un code ASCII des Couleurs
    print (Color.PURPLE + "***********************************************" + Color.ENDC)
    print (Color.PURPLE + "*"+ '\n' +Color.PURPLE + "*")
    print (Color.PURPLE + "*"+ Color.GREEN +  Color.BOLD +"     Au revoir ! " + Color.ENDC)
    print (Color.PURPLE + "*"+ '\n' +Color.PURPLE + "*")
    print (Color.PURPLE + "***********************************************" + Color.ENDC)
    exit()

def Choice(choice): # une methode qui return le format String du choix
    choices = [1,2,3,4]
    if choice in choices:
        if(choice == 1):
            return "Pierre"
        elif(choice == 2):
            return "Feuille"
        elif(choice == 3):
            return "Ciseaux"
        elif(choice == 4):
            bye()
    else:
        return False

def StartGame():
    os.system("clear")  # Clear Console
    # Une présentation du Jeux
    print (Color.PURPLE + "***********************************************" + Color.ENDC)
    print (Color.PURPLE + "*"+ '\n' +Color.PURPLE + "*")
    print (Color.PURPLE + "*"+ Color.GREEN + "    Chifoumi v1.0" + Color.ENDC)
    print (Color.PURPLE + "*"+ '\n' +Color.PURPLE + "*")
    print (Color.PURPLE + "*"+ Color.GREEN + "    Developed with ❤ by:" + Color.ENDC)
    print (Color.PURPLE + "*"+ Color.BLUE + "        - AYOUNI Charif" + Color.ENDC)
    print (Color.PURPLE + "*"+ Color.BLUE + "        - OUARRADI Brahim" + Color.ENDC)
    print (Color.PURPLE + "*"+('\n') +Color.PURPLE + "*")
    print (Color.PURPLE + "***********************************************" + Color.ENDC)
    print ('\n \n')

def WhoWins(player, computer, ThisPart):
    # La fonction qui permis de faire les testes et mettre a jour le score des joueurs
    
    # Les regles:
    # - La pierre ecrase les ciseaux et gagne.
    # - La feuille enveloppe la pierre et gagne.
    # - Les ciseaux decoupent la feuille et gagnent.

    if(player.getChoice() == computer.getChoice() ):
        print('Egalite')

    # Les testes
    if( player.getChoice() == 'Pierre' and computer.getChoice() == 'Ciseaux' ):
        print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez gagne 5 points' + Color.ENDC)
        player.setScore(5)
    elif ( player.getChoice() == 'Pierre' and computer.getChoice() == 'Feuille'):
        print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez perdu' + Color.ENDC)
        computer.setScore(5)

    if(player.getChoice() == 'Feuille' and computer.getChoice() == 'Pierre' ):
        print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez gagne 5 points' + Color.ENDC)
        player.setScore(5)
    elif (player.getChoice() == 'Feuille' and computer.getChoice() == 'Ciseaux' ):
        print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez perdu' + Color.ENDC)
        computer.setScore(5)

    if(player.getChoice() == 'Ciseaux' and computer.getChoice() == 'Feuille' ):
        print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez gagne 5 points' + Color.ENDC)
        player.setScore(5)

    elif (player.getChoice() == 'Ciseaux' and computer.getChoice() == 'Pierre' ):
        print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez perdu' + Color.ENDC)
        computer.setScore(5)

    # Si le nombre des parties egale au Nombre Global -> fin de la partie
    if( ThisPart >= NumberOfParts ):
        # je recupere le score de chaqu'un pour voir le gagnant
        os.system("clear")  # Clear Console

        if( player.getScore() == computer.getScore() ):
            print (Color.GREEN +  Color.BOLD + ' EGALITE ' + Color.ENDC)
            print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez un score de: '+ str( player.getScore() ) + Color.ENDC)
            print (Color.GREEN +  Color.BOLD + computer.getName() + ' Vous avez un score de: '+ str( computer.getScore() ) + Color.ENDC)

        if( player.getScore() > computer.getScore() ):
            print (Color.GREEN +  Color.BOLD + player.getName() + ' Vous avez gagne la partie avec un score de: '+ str( player.getScore() ) + Color.ENDC)
            print (Color.WARNING + 'Le score de ' + computer.getName() + " est: " + str( computer.getScore() ) + Color.ENDC)
        else:
            print (Color.WARNING +  Color.BOLD + player.getName() + ' Vous avez perdu la partie contre '+ computer.getName() + ' avec un score de: '+ str( player.getScore() ) + Color.ENDC)
            print (Color.GREEN +  Color.BOLD + 'Le score de ' + computer.getName() + " est: " + str( computer.getScore() ) + Color.ENDC)
        bye()
        exit()
        
class Computer: # La classe Ordinateur, La classe a comme attribut Nom, Score et Choix
    def __init__(self, Name, Score): # Le constructeur de la classe
        self.name = Name
        self.score = Score
        self.choice = ''
        self.getRandomChoice() # Lancement de la fonction qui permis de generer le choix aleatoire de d'ordinateur

    def getRandomChoice(self):
        mychoice = randint(1,3)
        self.setChoice( Choice(mychoice) ) # Le setteur permis d'affecter a l'attribut sa valeur recupere depuis la methode Choice()

    def setChoice(self, Choice): # Le setteur
        self.choice = Choice

    def getChoice(self): # le getteur
        return self.choice
    def getName(self):
        return self.name
    def setScore(self, Score):
        self.score += Score
    def getScore(self):
        if( self.score < 0): # Le score ne sera jamais négatif
            self.score = 0
        return self.score

class Player: # La classe Joueur, La classe a comme attribut Nom, Score et Choix
    def __init__(self, Name, Score):
        self.name = Name
        self.score = Score
        self.choice = ''

    def getInputChoice (self):
        choice = 0
        while ( Choice(choice) == False ): # Tantque l'utilisateur tape une valeur erroné, la methode Choice() return False
                try:
                    print('Veuillez saisir votre choix: ')
                    print('1 - Pierre \n2 - Feuille \n3 - Ciseaux \n4 - exit')
                    print('\n')
                    choice = input(Color.GREEN+'     Your choice: '+Color.ENDC)
                    print('\n')
                except:
                    os.system("clear")  # Clear Console
                    print('Veuillez saisir un chiffre entre 1 et 3')
                    print('\n')
                if(Choice(choice) == False):
                    os.system("clear")  # Clear Console
                    print('Veuillez saisir un chiffre entre 1 et 3')

        self.setChoice( Choice(choice) ) # Affecter le choix au joueur

    # Les setteurs et Getteurs de la classe Player
    def setChoice(self, Choice):
        self.choice = Choice
    def getChoice(self):
        return self.choice
    def getName(self):
        return self.name
    def setScore(self, Score):
        self.score += Score
    def getScore(self):
        if( self.score < 0):
            self.score = 0
        return self.score

class Color: # La classe Color permis de retourner le code ASCII d'une couleur
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

StartGame()
computer = Computer("MAC PRO", 0) # Instancer l'objet computer de la class Computer
name = ''
while(name == ''): # Recupere un Nom pour notre joueur
    try:
        name = raw_input("Veuillez saisir votre Nom: ")
    except:
        print('Veuillez saisir un Nom correct \n')
    os.system("clear")  # Clear Console

print ('\n') # Espace
player = Player(name, 0) # Instancer l'objet player de la class Player
print (Color.PURPLE + "BIENVENU "+ player.getName() + Color.PURPLE + Color.ENDC)
print ('\n') # Espace

i = 1
while(True): # Le jour est en Boocle
    player.getInputChoice() # Demander au player de selectionner son choix
    WhoWins(player, computer,i) # Faire les testes pour voir le gagnant
    i = i + 1 # incrémenter la partie
