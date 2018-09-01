from Organisms.Organism import Organism
from random import randint


class Plant(Organism):
    def __init__(self, posX, posY, world, age, strenght, iniciative=0):
        super(Plant, self).__init__(posX, posY, world, age, strenght, iniciative)

    def action(self):
        possibilityOfExpand = randint(0, 20)
        if possibilityOfExpand == 10:
            p = self.world.findFreeField(self.posX, self.posY)
            if p.X != -1:
                com = self.getTypeInString() + "in place X=" + str(self.posX) + " Y=" + str(self.posY)
                com += " expanded to the place X=" + str(p.X) + " Y=" + str(p.Y)
                self.world.addCommunicate(com)
                self.world.insertNewOrganism(p.X, p.Y, self.getType())

    def action2(self, zn):
        return

    def collision(self, attackerX, attackerY, code):
        opponent = self.world.getXY(attackerX, attackerY)
        if opponent is not None:
            self.world.move(attackerX, attackerY, self.posX, self.posY)
            com = opponent.getTypeInString() + "in place X=" + str(self.posX) + " Y=" + str(self.posY)
            com += " eats " + self.getTypeInString()
            self.world.addCommunicate(com)
            self.world.removeFromVector(self)

    def moveOrCollide(self, posX, posY, newPosX, newPosY):
        return

    def drawing(self):
        return 'P'

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def setPosX(self, newPosX):
        self.posX = newPosX

    def setPosY(self, newPosY):
        self.posY = newPosY

    def getAge(self):
        return self.age

    def getIniciative(self):
        return self.iniciative

    def setStrenght(self, str):
        self.strenght = str

    def getStrenght(self):
        return self.strenght

    def blocked(self, opponent):
        return False

    def runAway(self):
        return False

    def alzureShield(self):
        return False

    def incrementAge(self):
        self.age += 1

