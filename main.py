from character import Character
from team import Team
from initializeCharacters import initializeCharacters
from InitializeTeams import initializeTeams
from InitializeTeams import initializeGoodTeams
from InitializeTeams import initializeYSHelperTeams

from InitializeTeams import compareTeamLists
from InitializeTeams import teamsWith
import AbyssRandomize

# <editor-fold desc="Character variables">
TRAVELER = 0
JEAN = 1
NOELLE = 2
SUCROSE = 3
FISCHL = 4
MONA = 5
KAEYA = 6
DILUC = 7
RAZOR = 8
BENNETT = 9
BEIDOU = 10
KEQING = 11
XIANGLING = 12
CHONGYUN = 13
XINGQUI = 14
VENTI = 15
KLEE = 16
DIONA = 17
Zhongli = 18
ALEBEDO = 19
GANYU = 20
HUTAO = 21
ROSARIA = 22
KAZUHA = 23
RAIDEN = 24
SARA = 25
KOKOMI = 26
THOMA = 27
GOROU = 28
SHENHE = 29
YAEMIKO = 30
YELAN = 31
KUKI = 32
HEIZOU = 33
TIGHNARI = 34
CANDACE = 35
NILOU = 36
NAHIDA = 37
LAYLA = 38
WANDERER = 39
FARUZAN = 40
YAOYAO = 41
NEUVILLETTE = 42
FURINA = 43
CHARLOTTE = 44
NAVIA = 45
DORI = 46
FREMINET = 47
CHILDE = 48
GAMING = 49

# </editor-fold>


def printTeamsWithCharacter(teams, character):  # Prints the list of all teams with a certain character
    checker = teamsWith(teams, characterList[character])
    for i in checker:
        print(i)


characterList = initializeCharacters()  # List of every character I will use
badteamList = initializeTeams(characterList) # List of made teams
teamList = initializeGoodTeams(characterList) # List of every good team
YSHelper = initializeYSHelperTeams(characterList)
# printTeamsWithCharacter(teamList, NOELLE)  # Prints out all teams with the specified character


AbyssRandomize.randomTeams(badteamList)  # Prints 2 random teams

# compareTeamLists(badteamList, teamList)  #  checks to see all teams in badteamList but not teamList
