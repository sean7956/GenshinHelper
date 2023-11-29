from character import Character
from team import Team
from initializeCharacters import initializeCharacters
import random


def randomBadTeams(characterList):  # Gets 2 random teams
    tempCharList = characterList
    tempteam1 = random.sample(tempCharList, 4)

    tempCharList2 = [i for i in tempCharList if i not in tempteam1]  # Removes all characters from team 1

    tempteam2 = random.sample(tempCharList2, 4)

    team1 = Team(tempteam1[0], tempteam1[1], tempteam1[2], tempteam1[3])
    print("Team 1")
    print(team1)

    team2 = Team(tempteam2[0], tempteam2[1], tempteam2[2], tempteam2[3])
    print("Team 2")
    print(team2)

def randomTeams(teamList):
    tempTeamList = teamList

    tempTeam1 = random.sample(tempTeamList, 1)[0]   # Gives a random team from the predefined list
    tempTeam2 = random.sample(tempTeamList, 1)[0]

    while(tempTeam1.alreadyInUse(tempTeam2)):
        tempTeam2 = random.sample(tempTeamList, 1)[0]

    print(tempTeam1)
    print(tempTeam2)
