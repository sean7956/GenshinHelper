from character import Character
from team import Team
from initializeCharacters import initializeCharacters
import AbyssRandomize

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


# Possible expansion is to make an ARCHETYPE Class to sort every team into archetypes

def initializeGoodTeams(characterList):  # TODO uncomment Charlotte when leveled up
    teamList = [
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[RAIDEN], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[SUCROSE], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[NAHIDA], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[RAIDEN], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[HUTAO], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[KOKOMI], characterList[FURINA]),
        Team(characterList[YELAN], characterList[GOROU], characterList[NOELLE], characterList[FURINA]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[NOELLE], characterList[FURINA]),
        Team(characterList[TRAVELER], characterList[KOKOMI], characterList[NAHIDA], characterList[NILOU]),
        Team(characterList[XINGQUI], characterList[YAOYAO], characterList[NAHIDA], characterList[NILOU]),
        Team(characterList[FURINA], characterList[KOKOMI], characterList[NAHIDA], characterList[NILOU]),
        Team(characterList[KAZUHA], characterList[KOKOMI], characterList[SHENHE], characterList[CHONGYUN]),
        #Team(characterList[KAZUHA], characterList[CHARLOTTE], characterList[NEUVILLETTE], characterList[FURINA]),
        Team(characterList[VENTI], characterList[KOKOMI], characterList[GANYU], characterList[SHENHE]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[CHONGYUN], characterList[BENNETT], characterList[SHENHE], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[SUCROSE], characterList[BEIDOU]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[NAHIDA], characterList[BEIDOU]),
        Team(characterList[YELAN], characterList[FISCHL], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[FISCHL], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[YELAN], characterList[JEAN], characterList[RAIDEN], characterList[FURINA]),
        Team(characterList[XINGQUI], characterList[JEAN], characterList[RAIDEN], characterList[FURINA]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[NAHIDA], characterList[KUKI]),
        Team(characterList[XINGQUI], characterList[RAIDEN], characterList[NAHIDA], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[NAHIDA], characterList[NOELLE], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[FURINA], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[TIGHNARI], characterList[YAEMIKO]),
        Team(characterList[XINGQUI], characterList[KOKOMI], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[KEQING], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[YAEMIKO], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[NEUVILLETTE], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[RAIDEN], characterList[NEUVILLETTE], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[TIGHNARI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[TIGHNARI], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[RAIDEN], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[YAEMIKO], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[KEQING], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KOKOMI], characterList[BEIDOU]),
        Team(characterList[NAHIDA], characterList[FURINA], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[NAHIDA], characterList[BEIDOU]),
        Team(characterList[XINGQUI], characterList[LAYLA], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[GANYU], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[LAYLA], characterList[NEUVILLETTE], characterList[RAIDEN]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[SHENHE], characterList[KUKI]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[RAZOR], characterList[NAHIDA]),
        Team(characterList[YELAN], characterList[NAHIDA], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[YELAN], characterList[NAHIDA], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[FURINA], characterList[NAHIDA], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[RAIDEN], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KEQING], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[RAIDEN], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[YAEMIKO], characterList[TIGHNARI], characterList[Zhongli]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[RAIDEN], characterList[SARA]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[RAIDEN], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[JEAN], characterList[RAIDEN], characterList[SARA]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[ALEBEDO], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[FARUZAN], characterList[BENNETT], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[FARUZAN], characterList[JEAN], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[FARUZAN], characterList[JEAN], characterList[WANDERER], characterList[FURINA]),
        #Team(characterList[FARUZAN], characterList[CHARLOTTE], characterList[WANDERER], characterList[FURINA]),
        Team(characterList[KAZUHA], characterList[FURINA], characterList[NEUVILLETTE], characterList[Zhongli]),
        Team(characterList[KAZUHA], characterList[FURINA], characterList[NEUVILLETTE], characterList[FISCHL]),
        Team(characterList[KAZUHA], characterList[FURINA], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[Zhongli]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[FISCHL]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[XIANGLING]),

    ]

    return  teamList

def initializeTeams(characterList):
    teamList = [
        # National Teams
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[RAIDEN], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[SUCROSE], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[NOELLE], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[NAHIDA], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[WANDERER], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[HEIZOU], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[CHONGYUN], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[KAEYA], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[YELAN], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[CANDACE], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[NILOU], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[FURINA], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[CHARLOTTE], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[RAIDEN], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[SUCROSE], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[NOELLE], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[NAHIDA], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[WANDERER], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[HEIZOU], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[CHONGYUN], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[KAEYA], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[CANDACE], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[NILOU], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[FURINA], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[CHARLOTTE], characterList[XIANGLING]),

        # ANEMO National Teams
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[HEIZOU], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[FURINA], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[NILOU], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[GANYU], characterList[XIANGLING]),

        Team(characterList[SUCROSE], characterList[BENNETT], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[SUCROSE], characterList[BENNETT], characterList[HEIZOU], characterList[XIANGLING]),
        Team(characterList[SUCROSE], characterList[BENNETT], characterList[FURINA], characterList[XIANGLING]),
        Team(characterList[SUCROSE], characterList[BENNETT], characterList[NILOU], characterList[XIANGLING]),
        Team(characterList[SUCROSE], characterList[BENNETT], characterList[GANYU], characterList[XIANGLING]),

        # Mono Pyro
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[DILUC], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[KLEE], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[HUTAO], characterList[XIANGLING]),

        # Mono Hydro
        Team(characterList[XINGQUI], characterList[YELAN], characterList[KOKOMI], characterList[FURINA]),
        Team(characterList[KAZUHA], characterList[XINGQUI], characterList[KOKOMI], characterList[YELAN]),
        Team(characterList[KAZUHA], characterList[FURINA], characterList[KOKOMI], characterList[YELAN]),
        Team(characterList[XINGQUI], characterList[JEAN], characterList[CANDACE], characterList[FURINA]),

        # MONO Cryo
        Team(characterList[KAZUHA], characterList[LAYLA], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[KAZUHA], characterList[DIONA], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[KAZUHA], characterList[CHARLOTTE], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[KAZUHA], characterList[CHONGYUN], characterList[SHENHE], characterList[Zhongli]),

        # Noelle
        Team(characterList[ALEBEDO], characterList[GOROU], characterList[NOELLE], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[GOROU], characterList[NOELLE], characterList[FURINA]),
        Team(characterList[YELAN], characterList[GOROU], characterList[NOELLE], characterList[FURINA]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[NOELLE], characterList[FURINA]),

        # Nilou
        Team(characterList[TRAVELER], characterList[KOKOMI], characterList[NAHIDA], characterList[NILOU]),
        Team(characterList[XINGQUI], characterList[YAOYAO], characterList[NAHIDA], characterList[NILOU]),
        Team(characterList[YELAN], characterList[YAOYAO], characterList[NAHIDA], characterList[NILOU]),
        Team(characterList[CANDACE], characterList[YAOYAO], characterList[NAHIDA], characterList[NILOU]),
        Team(characterList[NAHIDA], characterList[YAOYAO], characterList[NEUVILLETTE], characterList[NILOU]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[NEUVILLETTE], characterList[NILOU]),
        Team(characterList[FURINA], characterList[KOKOMI], characterList[NAHIDA], characterList[NILOU]),

        # Freeze
        Team(characterList[KAZUHA], characterList[KOKOMI], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[KAZUHA], characterList[SHENHE], characterList[KOKOMI], characterList[KAEYA]),
        Team(characterList[KAZUHA], characterList[CHARLOTTE], characterList[NEUVILLETTE], characterList[FURINA]),
        Team(characterList[FURINA], characterList[JEAN], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[XINGQUI], characterList[LAYLA], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[XINGQUI], characterList[LAYLA], characterList[SHENHE], characterList[KAEYA]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[KOKOMI], characterList[GANYU]),
        Team(characterList[YELAN], characterList[LAYLA], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[FURINA], characterList[CHARLOTTE], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[FURINA], characterList[CHARLOTTE], characterList[SHENHE], characterList[KAEYA]),
        Team(characterList[FURINA], characterList[CHARLOTTE], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[LAYLA]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[GANYU]),
        Team(characterList[VENTI], characterList[KOKOMI], characterList[GANYU], characterList[LAYLA]),
        Team(characterList[VENTI], characterList[KOKOMI], characterList[GANYU], characterList[SHENHE]),
        Team(characterList[VENTI], characterList[CHARLOTTE], characterList[GANYU], characterList[FURINA]),
        Team(characterList[KAZUHA], characterList[KOKOMI], characterList[GANYU], characterList[LAYLA]),
        Team(characterList[KAZUHA], characterList[KOKOMI], characterList[GANYU], characterList[SHENHE]),
        Team(characterList[KAZUHA], characterList[CHARLOTTE], characterList[GANYU], characterList[FURINA]),

        # Melt
        Team(characterList[XIANGLING], characterList[BENNETT], characterList[GANYU], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[BENNETT], characterList[GANYU], characterList[Zhongli]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[SHENHE], characterList[CHONGYUN]),
        Team(characterList[CHONGYUN], characterList[BENNETT], characterList[SHENHE], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[KAEYA], characterList[ROSARIA]),

        # Taser
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[SUCROSE], characterList[BEIDOU]),
        Team(characterList[YELAN], characterList[FISCHL], characterList[KOKOMI], characterList[BEIDOU]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[YELAN], characterList[FISCHL], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[XINGQUI], characterList[KOKOMI], characterList[SUCROSE], characterList[FISCHL]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[WANDERER], characterList[BEIDOU]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[HEIZOU], characterList[BEIDOU]),
        Team(characterList[FURINA], characterList[FISCHL], characterList[KOKOMI], characterList[BEIDOU]),
        Team(characterList[FURINA], characterList[FISCHL], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[FISCHL], characterList[KOKOMI], characterList[BEIDOU]),
        Team(characterList[KAZUHA], characterList[FISCHL], characterList[KOKOMI], characterList[FURINA]),
        Team(characterList[YELAN], characterList[JEAN], characterList[RAIDEN], characterList[FURINA]),
        Team(characterList[YELAN], characterList[JEAN], characterList[YAEMIKO], characterList[FURINA]),
        Team(characterList[XINGQUI], characterList[JEAN], characterList[RAIDEN], characterList[FURINA]),
        Team(characterList[XINGQUI], characterList[JEAN], characterList[YAEMIKO], characterList[FURINA]),

        # Hyperbloom
        Team(characterList[XINGQUI], characterList[YELAN], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[NAHIDA], characterList[KUKI]),
        Team(characterList[XINGQUI], characterList[CANDACE], characterList[NAHIDA], characterList[KUKI]),
        Team(characterList[XINGQUI], characterList[RAIDEN], characterList[NAHIDA], characterList[Zhongli]),
        Team(characterList[YELAN], characterList[RAIDEN], characterList[NAHIDA], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[BEIDOU], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[CANDACE], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[NOELLE], characterList[RAIDEN]),
        Team(characterList[YELAN], characterList[NAHIDA], characterList[NOELLE], characterList[RAIDEN]),
        Team(characterList[FURINA], characterList[NAHIDA], characterList[NOELLE], characterList[RAIDEN]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[WANDERER], characterList[KUKI]),
        Team(characterList[YELAN], characterList[NAHIDA], characterList[WANDERER], characterList[KUKI]),
        Team(characterList[NAHIDA], characterList[FURINA], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[RAIDEN], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[RAIDEN], characterList[FISCHL]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[TIGHNARI], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[TIGHNARI], characterList[FISCHL]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[KEQING], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[KEQING], characterList[FISCHL]),
        Team(characterList[XINGQUI], characterList[KOKOMI], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[YELAN], characterList[KOKOMI], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[KEQING], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[KEQING], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[YAEMIKO], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[NEUVILLETTE], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[NEUVILLETTE], characterList[KUKI]),
        Team(characterList[NAHIDA], characterList[RAIDEN], characterList[NEUVILLETTE], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[TIGHNARI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[KOKOMI], characterList[TIGHNARI], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[RAIDEN], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[YAEMIKO], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[KEQING], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KOKOMI], characterList[BEIDOU]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[FURINA], characterList[KOKOMI], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[FURINA], characterList[KOKOMI], characterList[FISCHL]),
        Team(characterList[KAZUHA], characterList[KOKOMI], characterList[NAHIDA], characterList[YAEMIKO]),
        Team(characterList[KAZUHA], characterList[KOKOMI], characterList[NAHIDA], characterList[FISCHL]),
        Team(characterList[XINGQUI], characterList[KUKI], characterList[NAHIDA], characterList[KAZUHA]),
        Team(characterList[YELAN], characterList[KUKI], characterList[NAHIDA], characterList[KAZUHA]),
        Team(characterList[XINGQUI], characterList[KOKOMI], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[YELAN], characterList[KOKOMI], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[XINGQUI], characterList[YAOYAO], characterList[CANDACE], characterList[RAIDEN]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[CANDACE], characterList[RAIDEN]),
        Team(characterList[FURINA], characterList[JEAN], characterList[TIGHNARI], characterList[YAEMIKO]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[NAHIDA], characterList[BEIDOU]),

        # HyperFridge
        Team(characterList[XINGQUI], characterList[LAYLA], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[XINGQUI], characterList[KAEYA], characterList[NAHIDA], characterList[KUKI]),
        Team(characterList[YELAN], characterList[LAYLA], characterList[NAHIDA], characterList[RAIDEN]),
        Team(characterList[YELAN], characterList[KAEYA], characterList[NAHIDA], characterList[KUKI]),
        Team(characterList[NAHIDA], characterList[KAEYA], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[GANYU], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[LAYLA], characterList[KOKOMI], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[LAYLA], characterList[NEUVILLETTE], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[KAEYA], characterList[NEUVILLETTE], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[GANYU], characterList[NEUVILLETTE], characterList[RAIDEN]),
        Team(characterList[NAHIDA], characterList[KAEYA], characterList[NEUVILLETTE], characterList[KUKI]),
        Team(characterList[NAHIDA], characterList[GANYU], characterList[NEUVILLETTE], characterList[KUKI]),
        Team(characterList[YELAN], characterList[NAHIDA], characterList[SHENHE], characterList[KUKI]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[SHENHE], characterList[KUKI]),

        # Burgeon
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[RAZOR], characterList[NAHIDA]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[YELAN], characterList[NAHIDA], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[FURINA], characterList[NAHIDA], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[KAZUHA], characterList[NAHIDA], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[VENTI], characterList[NAHIDA], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[NAHIDA], characterList[RAIDEN], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[NAHIDA], characterList[KAEYA], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[NAHIDA], characterList[BEIDOU], characterList[KOKOMI], characterList[THOMA]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[YELAN], characterList[NAHIDA], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[FURINA], characterList[NAHIDA], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[KAZUHA], characterList[NAHIDA], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[RAIDEN], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[KAEYA], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[BEIDOU], characterList[KOKOMI], characterList[XIANGLING]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[DILUC], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[NAHIDA], characterList[KLEE], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[DILUC], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[KLEE], characterList[FURINA]),
        Team(characterList[NAHIDA], characterList[JEAN], characterList[HUTAO], characterList[FURINA]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[CANDACE], characterList[XIANGLING]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[CANDACE], characterList[THOMA]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[XINGQUI], characterList[XIANGLING]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[XINGQUI], characterList[THOMA]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[YELAN], characterList[XIANGLING]),
        Team(characterList[FURINA], characterList[YAOYAO], characterList[YELAN], characterList[THOMA]),
        Team(characterList[NAHIDA], characterList[RAIDEN], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[BEIDOU], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[LAYLA], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[NAHIDA], characterList[KAEYA], characterList[NEUVILLETTE], characterList[XIANGLING]),

        # A Aggravate/Spread
        Team(characterList[NAHIDA], characterList[YAOYAO], characterList[KEQING], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[KEQING], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[KEQING], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[YAEMIKO], characterList[KEQING], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[KEQING], characterList[YAEMIKO]),
        Team(characterList[FISCHL], characterList[YAOYAO], characterList[KEQING], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[YAOYAO], characterList[YAEMIKO], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[YAEMIKO], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[YAOYAO], characterList[RAIDEN], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[RAIDEN], characterList[FISCHL]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[RAIDEN], characterList[Zhongli]),
        Team(characterList[KAZUHA], characterList[YAOYAO], characterList[KEQING], characterList[FISCHL]),
        Team(characterList[KAZUHA], characterList[YAOYAO], characterList[YAEMIKO], characterList[FISCHL]),
        Team(characterList[KAZUHA], characterList[YAOYAO], characterList[RAIDEN], characterList[FISCHL]),
        Team(characterList[KAZUHA], characterList[YAOYAO], characterList[KEQING], characterList[YAEMIKO]),
        Team(characterList[KAZUHA], characterList[YAOYAO], characterList[RAIDEN], characterList[YAEMIKO]),
        Team(characterList[FISCHL], characterList[YAOYAO], characterList[RAIDEN], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[FISCHL], characterList[TIGHNARI], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[YAEMIKO], characterList[TIGHNARI], characterList[Zhongli]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[TIGHNARI], characterList[YAEMIKO]),
        Team(characterList[NAHIDA], characterList[KUKI], characterList[TIGHNARI], characterList[FISCHL]),

        # Raiden Hyper
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[RAIDEN], characterList[SARA]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[RAIDEN], characterList[YAEMIKO]),
        Team(characterList[KAZUHA], characterList[BENNETT], characterList[RAIDEN], characterList[FISCHL]),
        Team(characterList[FURINA], characterList[JEAN], characterList[RAIDEN], characterList[SARA]),
        Team(characterList[FURINA], characterList[JEAN], characterList[RAIDEN], characterList[YAEMIKO]),
        Team(characterList[FURINA], characterList[JEAN], characterList[RAIDEN], characterList[FISCHL]),
        Team(characterList[FURINA], characterList[BENNETT], characterList[RAIDEN], characterList[JEAN]),

        # Hu Tao
        Team(characterList[XINGQUI], characterList[YELAN], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[ALEBEDO], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[YELAN], characterList[ALEBEDO], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[FISCHL], characterList[HUTAO], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[HUTAO], characterList[KAZUHA]),
        Team(characterList[XINGQUI], characterList[THOMA], characterList[HUTAO], characterList[KAZUHA]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[HUTAO], characterList[FURINA]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[HUTAO], characterList[Zhongli]),

        # Wanderer
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[YELAN], characterList[BENNETT], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[YELAN], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[XINGQUI], characterList[BENNETT], characterList[WANDERER], characterList[YELAN]),
        Team(characterList[XINGQUI], characterList[JEAN], characterList[WANDERER], characterList[YELAN]),
        Team(characterList[XINGQUI], characterList[JEAN], characterList[WANDERER], characterList[FURINA]),
        Team(characterList[FARUZAN], characterList[JEAN], characterList[WANDERER], characterList[FURINA]),
        Team(characterList[FARUZAN], characterList[CHARLOTTE], characterList[WANDERER], characterList[FURINA]),
        Team(characterList[FURINA], characterList[BENNETT], characterList[WANDERER], characterList[CHARLOTTE]),
        Team(characterList[FURINA], characterList[CHARLOTTE], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[FARUZAN], characterList[BENNETT], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[FARUZAN], characterList[BENNETT], characterList[WANDERER], characterList[THOMA]),
        Team(characterList[FARUZAN], characterList[BENNETT], characterList[WANDERER], characterList[XIANGLING]),
        Team(characterList[FARUZAN], characterList[JEAN], characterList[WANDERER], characterList[Zhongli]),
        Team(characterList[FARUZAN], characterList[BENNETT], characterList[WANDERER], characterList[JEAN]),
        Team(characterList[XINGQUI], characterList[JEAN], characterList[WANDERER], characterList[FARUZAN]),

        # Neuvillette
        Team(characterList[KAZUHA], characterList[FURINA], characterList[NEUVILLETTE], characterList[Zhongli]),
        Team(characterList[KAZUHA], characterList[FURINA], characterList[NEUVILLETTE], characterList[FISCHL]),
        Team(characterList[KAZUHA], characterList[FURINA], characterList[NEUVILLETTE], characterList[XIANGLING]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[Zhongli]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[FISCHL]),
        Team(characterList[FURINA], characterList[JEAN], characterList[NEUVILLETTE], characterList[XIANGLING]),


    ]
    return teamList
