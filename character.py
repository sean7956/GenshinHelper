class Character:
    def __init__(self, name, element, role1, role2="None"):
        self.name = name
        self.element = element
        self.role1 = role1    # Rolls are DPS, Sub DPS, Buffer, Healer, Shielder and None
        self.role2 = role2


    def __str__(self):
        return self.name

    def getElement(self):
        return self.element

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False