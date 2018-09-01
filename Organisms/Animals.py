from Organisms.Animal import Animal
from Organisms.Types import Types
from random import randint


class Wolf(Animal):

    def __init__(self, world, posX, posY,  age=0, strenght=-1, iniciative=-1):
        if strenght == -1:
            super(Wolf, self).__init__(world, posX, posY, age, 9, 5)
        else:
            super(Wolf, self).__init__(world, posX, posY, age, strenght, iniciative)

    def drawing(self):
        return 'W'

    def getType(self):
        typ = Types.wolf
        return typ

    def getTypeInString(self):
        return "Wolf"


class Sheep(Animal):
    def __init__(self, world, posX, posY,  age=0, strenght=-1, iniciative=-1):
        if strenght == -1:
            super(Sheep, self).__init__(world, posX, posY, age, 4, 4)
        else:
            super(Sheep, self).__init__(world, posX, posY, age, strenght, iniciative)

    def drawing(self):
        return 'A'

    def getType(self):
        typ = Types.sheep
        return typ

    def getTypeInString(self):
        return "Sheep"


class Antelope(Animal):
    def __init__(self, world, posX, posY, age=0, strenght=-1, iniciative=-1):
        if strenght == -1:
            super(Antelope, self).__init__(world, posX, posY, age, 4, 4)
        else:
            super(Antelope, self).__init__(world, posX, posY, age, strenght, iniciative)

    def action(self):
        p = self.randField(self.posX, self.posY, 2)
        self.moveOrCollide(self.posX, self.posY, p.X, p.Y)

    def drawing(self):
        return 'A'

    def getType(self):
        return Types.antelope

    def getTypeInString(self):
        return "Antelope"

    def runAway(self):
        i = randint(0, 1)
        if i == 0:
            return True
        return False


class Turtle(Animal):
    def __init__(self, world, posX, posY, age=0, strenght=-1, iniciative=-1):
        if strenght == -1:
            super(Turtle, self).__init__(world, posX, posY, age, 2, 1)
        else:
            super(Turtle, self).__init__(world, posX, posY, age, strenght, iniciative)

    def action(self):
        rnd = randint(0, 4)
        if rnd == 3:
            super(Turtle, self).action()

    def drawing(self):
        return 'T'

    def getType(self):
        return Types.turtle

    def getTypeInString(self):
        return "Turtle"

    def blocked(self, opponent):
        if opponent.getStrenght() < 5:
            return True
        return False


class Fox(Animal):
    def __init__(self, world, posX, posY,  age=0, strenght=-1, iniciative=-1):
        if strenght == -1:
            super(Fox, self).__init__(world, posX, posY,  age, 3, 7)
        else:
            super(Fox, self).__init__(world, posX, posY,  age, strenght, iniciative)

    def isThereStronger(self, newPosX, newPosY):
        if self.world.getXY(newPosX, newPosY) is not None:
            if self.world.getXY(newPosX, newPosY).getStrenght() > self.strenght:
                return True
        return False

    def action(self):
        p = self.randField(self.posX, self.posY, 1)
        braker = 0
        while self.isThereStronger(p.X, p.Y) and (braker < 20):
            p = self.randField(self.posX, self.posY, 1)
            braker = braker + 1
        self.moveOrCollide(self.posX, self.posY, p.X, p.Y)

    def drawing(self):
        return 'F'

    def getType(self):
        return Types.fox

    def getTypeInString(self):
        return "Fox"


class CyberSheep(Animal):
    def __init__(self, world, posX, posY,  age=0, strenght=-1, iniciative=-1):
        if strenght == -1:
            super(CyberSheep, self).__init__(world, posX, posY,  age, 11, 4)
        else:
            super(CyberSheep, self).__init__(world, posX, posY,  age, strenght, iniciative)

    def findClosestHogweed(self):
        closestHegweed = None
        dys = 1000000
        for i in range(len(self.world.vecOrganism)):
            if self.world.vecOrganism[i].drawing() == 's':
                help = self.world.vecOrganism[i]
                dys2 = abs(help.getPosY()-self.posY)
                if abs(help.getPosX()-self.posX) > dys2:
                    dys2 = abs(help.getPosX() - self.posX)
                if dys2 < dys:
                    dys = dys2
                    closestHegweed = help
        return closestHegweed

    def goToTheHogweed(self, closestHegweed):
        pX = 0
        pY = 0
        if self.posX > closestHegweed.getPosX():
            pX = -1
        elif self.posX < closestHegweed.getPosX():
            pX = 1
        if self.posY > closestHegweed.getPosY():
            pY = -1
        elif self.posY < closestHegweed.getPosY():
            pY = 1
        self.moveOrCollide(self.posX, self.posY, self.posX + pX, self.posY + pY)

    def action(self):
        closestHegweed = self.findClosestHogweed()
        if closestHegweed is not None:
            self.goToTheHogweed(closestHegweed)
        else:
            super(CyberSheep, self).action()

    def drawing(self):
        return 'C'

    def getType(self):
        return Types.cyberSheep

    def getTypeInString(self):
        return "Cyber Sheep"


class Human(Animal):
    def __init__(self, world, posX, posY, alzureShieldInt=-5, age=0, strenght=-1, iniciative=-1):
        if strenght == -1:
            super(Human, self).__init__(world, posX, posY, age, 5, 4)
        else:
            super(Human, self).__init__(world, posX, posY, age, strenght, iniciative, alzureShieldInt)
        self.alzureShieldInt = alzureShieldInt

    def action2(self, zn):
        if (zn == 1) and (self.posY > 0):
            self.world.changeHumanY(self.posY-1)
            self.moveOrCollide(self.posX, self.posY, self.posX, self.posY-1)
        if (zn == 2) and (self.posY < (self.world.getY()-1)):
            self.world.changeHumanY(self.posY+1)
            self.moveOrCollide(self.posX, self.posY, self.posX, self.posY + 1)
        if (zn == 3) and (self.posX > 0):
            self.world.changeHumanX(self.posX-1)
            self.moveOrCollide(self.posX, self.posY, self.posX - 1, self.posY)
        if (zn == 4) and (self.posX < (self.world.getX()-1)):
            self.world.changeHumanX(self.posX+1)
            self.moveOrCollide(self.posX, self.posY, self.posX + 1, self.posY)
        if self.alzureShieldInt != -5:
            self.alzureShieldInt = self.alzureShieldInt - 1

    def collision(self, attackerX, attackerY, code):
        if self.world.getXY(attackerX, attackerY) is not None:
            if code == 3:
                p = self.world.findFreeField(self.posX, self.posY)
                if p.X != -1:
                    self.world.move(attackerX, attackerY, p.X, p.Y)
                    com = self.world.getXY(p.X, p.Y).getTypeInString() + "in place X=" + str(self.posX) + " Y=" + str(self.posY) + " attacked "
                    com += self.getTypeInString() + " but he used alzure shield so " + self.world.getXY(p.X, p.Y).getTypeInString() + "run away to X="
                    com += str(p.X) + " Y=" + str(p.Y)
                    self.world.addCommunicate(com)
            else:
                opponent = self.world.getXY(attackerX, attackerY)
                self.world.setXY(opponent.getPosX(), opponent.getPosY(), None)
                com = opponent.getTypeInString() + " in place X=" + str(self.posX) + " Y=" + str(self.posY)
                com += " was killed by alzure shield of " + self.getTypeInString() + " becouse there was no place to run"
                self.world.addCommunicate(com)
                self.world.removeFromVector(opponent)
        else:
            super(Human, self).collision(attackerX, attackerY, code)

    def drawing(self):
        return 'H'

    def getType(self):
        return Types.human

    def getTypeInString(self):
        return "Human"

    def alzureShield(self):
        if self.alzureShieldInt > 0:
            return True
        return False

    def alzureShieldActive(self):
        if self.alzureShieldInt == -5:
            self.alzureShieldInt = 5

    def alzureShieldHowManyTures(self):
        return self.alzureShieldInt