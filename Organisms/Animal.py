from Organisms.Organism import Organism
from Organisms.Point import Point
from random import randint


class Animal(Organism):

    def getTypeInString(self):
        return "Animal"

    def __init__(self, posX, posY, world, age, strenght, iniciative, alzureShieldInt=-5):
        super(Animal, self).__init__(posX, posY, world, age, strenght, iniciative, alzureShieldInt)
        self.minimalAgeToBreed = 15

    def action(self):
        p = self.randField(self.posX, self.posY, 1)
        self.moveOrCollide(self.posX, self.posY, p.X, p.Y)

    def randField(self, x, y, change):
        newPosX = x
        newPosY = y
        numOfTry = 0
        while (newPosX == x) and (newPosY == y) and (numOfTry < 20):
            while True:
                newPosX = self.posX + randint(-change, change)
                if (newPosX >= 0) and (newPosX < self.world.getX()):
                    break
            while True:
                newPosY = self.posY + randint(-change, change)
                if (newPosY >= 0) and (newPosY < self.world.getY()):
                    break
            numOfTry += 1
        return Point(newPosX, newPosY)

    def moveOrCollide(self, posX, posY, newPosX, newPosY):
        if self.world.getXY(newPosX, newPosY) is not None:
            self.world.collisionSlover(posX, posY, newPosX, newPosY)
        else:
            self.world.move(self.posX, self.posY, newPosX, newPosY)

    def action2(self, zn):
        return None

    def collision(self, attackerX, attackerY, code):
        opponent = self.world.getXY(attackerX, attackerY)
        if opponent is not None:
            if code == 1:   # rozmnozenie
                if opponent.getAge() > self.minimalAgeToBreed:
                    if self.age > self.minimalAgeToBreed:
                        p = self.world.findFreeField(self.posX, self.posY)
                        if p.X != -1:
                            self.world.insertNewOrganism(p.X, p.Y, self.getType())
                            com = opponent.getTypeInString() + " in place X=" + str(self.posX) + " Y=" + str(self.posY) + " has bred "
                            self.world.addCommunicate(com)
                        else:
                            com = opponent.getTypeInString() + " in place X=" + str(self.posX) + " Y=" + str(self.posY) + " meet his partner but there was no place for their child"
                            self.world.addCommunicate(com)
            elif code == 2:  # ucieczka
                p = self.world.findFreeField(self.posX, self.posY)
                if p.X != -1:
                    self.world.move(self.posX, self.posY, p.X, p.Y)
                    self.world.move(attackerX, attackerY, self.posX, self.posY)
                    com = opponent.getTypeInString() + " in place X=" + str(self.posX) + " Y=" + str(self.posY) + " attacked "
                    com += self.getTypeInString() + " but it run away"
                    self.world.addCommunicate(com)
                else:
                    self.world.move(attackerX, attackerY, self.posX, self.posY)
                    com = opponent.getTypeInString() + " in place X=" + str(self.posX) + " Y=" + str(self.posY)
                    com += " eats " + self.getTypeInString()
                    self.world.addCommunicate(com)
                    self.world.removeFromVector(self)
            elif opponent.getStrenght() >= self.strenght:  # walka - wygrana atakujacego
                self.world.move(attackerX, attackerY, self.posX, self.posY)
                com = opponent.getTypeInString() + " in place X=" + str(self.posX) + " Y=" + str(self.posY)
                com += " eats " + self.getTypeInString()
                self.world.addCommunicate(com)
                self.world.removeFromVector(self)
            else:  # walka - wygrana broniacego
                self.world.setXY(opponent.getPosX(), opponent.getPosY(), None)
                com = opponent.getTypeInString() + " in place X=" + str(self.posX) + " Y=" + str(self.posY)
                com += " was eaten by " + self.getTypeInString()
                self.world.addCommunicate(com)
                self.world.removeFromVector(opponent)

    def drawing(self):
        return 'A'

    def getType(self):
        return None

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def setPosX(self, newPosX):
        self.posX = newPosX

    def setPosY(self, newPosY):
        self.posY = newPosY

    def incrementAge(self):
        self.age += 1

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