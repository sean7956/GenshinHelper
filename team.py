from character import Character

class Team:
    def __init__(self, c1, c2, c3, c4):
        self.character1 = c1
        self.character2 = c2
        self.character3 = c3
        self.character4 = c4
        self.characters = []
        self.hasPyro = False
        self.hasCryo = False
        self.hasHydro = False
        self.hasElectro = False
        self.hasAnemo = False
        self.hasGeo = False
        self.hasDendro = False

        if c1.element == "Pyro" or c2.element == "Pyro" or c3.element == "Pyro" or c4.element == "Pyro":
            self.hasPyro = True

        if c1.element == "Cryo" or c2.element == "Cryo" or c3.element == "Cryo" or c4.element == "Cryo":
            self.hasCryo = True

        if c1.element == "Hydro" or c2.element == "Hydro" or c3.element == "Hydro" or c4.element == "Hydro":
            self.hasHydro = True

        if c1.element == "Electro" or c2.element == "Electro" or c3.element == "Electro" or c4.element == "Electro":
            self.hasElectro = True

        if c1.element == "Anemo" or c2.element == "Anemo" or c3.element == "Anemo" or c4.element == "Anemo":
            self.hasAnemo = True

        if c1.element == "Geo" or c2.element == "Geo" or c3.element == "Geo" or c4.element == "Geo":
            self.hasGeo = True

        if c1.element == "Dendro" or c2.element == "Dendro" or c3.element == "Dendro" or c4.element == "Dendro":
            self.hasDendro = True

        self.characters.append(c1)
        self.characters.append(c2)
        self.characters.append(c3)
        self.characters.append(c4)

    def __str__(self):
        return self.character1.name + " " + self.character2.name + " " + self.character3.name + " " + self.character4.name

    def alreadyInUse(self, team2):  # Used to check if there are matching characters in 2 teams
        for i in range(4):
            for j in range(4):
                if self.characters[i] == team2.characters[j]:
                    return True

        return False



