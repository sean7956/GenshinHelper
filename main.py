from character import Character
from team import Team
from initializeCharacters import initializeCharacters
from InitializeTeams import initializeTeams
from InitializeTeams import initializeGoodTeams

import AbyssRandomize

characterList = initializeCharacters()  # List of every character I will use
#teamList = initializeTeams(characterList) # List of made teams
teamList = initializeGoodTeams(characterList)

AbyssRandomize.randomTeams(teamList)