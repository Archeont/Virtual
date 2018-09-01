from Organisms.Plant import Plant
from Organisms.Types import Types
from random import randint


class Grass(Plant):
    def __init__(self, world, posX, posY,  age=0, strenght=-1, iniciative=0):
        if strenght == -1:
            super(Grass, self).__init__(world, posX, posY, age, 0, 0)
        else:
            super(Grass, self).__init__(world, posX, posY, age, strenght, iniciative)

    def drawing(self):
        return 'G'

    def getType(self):
        return Types.grass

    def getTypeInString(self):
        return "Grass"


class Dandelion(Plant):
    def __init__(self, world, posX, posY, age=0, strenght=-1, iniciative=0):
        if strenght == -1:
            super(Dandelion, self).__init__(world, posX, posY, age, 0, 0)
        else:
            super(Dandelion, self).__init__(world, posX, posY, age, strenght, iniciative)

    def action(self):
        for i in range(3):
            super(Dandelion, self).action()

    def drawing(self):
        return 'D'

    def getType(self):
        return Types.dandelion

    def getTypeInString(self):
        return "Dandelion"


class Guarana(Plant):
    def __init__(self, world, posX, posY, age=0, strenght=-1, iniciative=0):
        if strenght == -1:
            super(Guarana, self).__init__(world, posX, posY, age, 0, 0)
        else:
            super(Guarana, self).__init__(world, posX, posY, age, strenght, iniciative)

    def collision(self, attackerX, attackerY, code):
        opponent = self.world.getXY(attackerX, attackerY)
        if opponent is not None:
            if opponent.getStrenght() >= self.strenght:
                self.world.move(attackerX, attackerY, self.posX, self.posY)
                com = opponent.getTypeInString() + "in place X=" + str(self.posX) + " Y=" + str(self.posY)
                com += " eats " + self.getTypeInString() + "so his strenght is increased by 3"
                opponent.setStrenght(opponent.getStrenght() + 3)
                self.world.addCommunicate(com)
                self.world.removeFromVector(self)

    def drawing(self):
        return 'g'

    def getType(self):
        return Types.guarana

    def getTypeInString(self):
        return "Guarana"


class SosnowskyHogweed(Plant):
    def __init__(self, world, posX, posY, age=0, strenght=-1, iniciative=0):
        if strenght == -1:
            super(SosnowskyHogweed, self).__init__(world, posX, posY, age, 10, 0)
        else:
            super(SosnowskyHogweed, self).__init__(world, posX, posY, age, strenght, iniciative)

    def action(self):
        super(SosnowskyHogweed, self).action()
        for i in range (-1, 1):
            for j in range(-1, 1):
                if self.world.areInWorld(self.posX + i, self.posY + j):
                    if self.world.isThisAnimal(self.posX + i, self.posY + j):
                        opponent = self.world.getXY(self.posX + i, self.posY + j)
                        self.world.setXY(self.posX + i, self.posY + j, None)
                        self.world.removeFromVector(opponent)
                        com = opponent.getTypeInString() + "in place X=" + str(self.posX) + " Y=" + str(self.posY)
                        com += " was killed by " + self.getTypeInString()
                        self.world.addCommunicate(com)

    def collision(self, attackerX, attackerY, code):
        opponent = self.world.getXY(attackerX, attackerY)
        if opponent is not None:
            com = opponent.getTypeInString() + "in place X=" + str(self.posX) + " Y=" + str(self.posY)
            com += " eats " + self.getTypeInString()
            if opponent.drawing() != 'C':
                self.world.setXY(attackerX, attackerY, None)
                self.world.removeFromVector(opponent)
                com += "so he died"
            else:
                self.world.move(attackerX, attackerY, self.posX, self.posY)
            self.world.addCommunicate(com)
            self.world.removeFromVector(self)


    def drawing(self):
        return 's'

    def getType(self):
        return Types.sosnowskyHogweed

    def getTypeInString(self):
        return "Sosnowsky Hogweed"


class WolfishBerry(Plant):
    def __init__(self, world, posX, posY, age=0, strenght=-1, iniciative=0):
        if strenght == -1:
            super(WolfishBerry, self).__init__(world, posX, posY, age, 99, 0)
        else:
            super(WolfishBerry, self).__init__(world, posX, posY, age, strenght, iniciative)

    def collision(self, attackerX, attackerY, code):
        opponent = self.world.getXY(attackerX, attackerY)
        if opponent is not None:
            self.world.setXY(attackerX, attackerY, None)
            self.world.setXY(self.posX, self.posY, None)
            self.world.removeFromVector(opponent)
            com = opponent.getTypeInString() + "in place X=" + str(self.posX) + " Y=" + str(self.posY)
            com += " eats " + self.getTypeInString() + "so he died"
            self.world.addCommunicate(com)
            self.world.removeFromVector(self)

    def drawing(self):
        return 'w'

    def getType(self):
        return Types.wolfishBerry

    def getTypeInString(self):
        return "Wolfish Berry"
