class Organism:

    def __init__(self, world=None, posX=0, posY=0,  age=0, strenght=0, iniciative=0, alzureShieldInt=-5):
        self.posX = posX
        self.posY = posY
        self.world = world
        self.age = age
        self.strenght = strenght
        self.iniciative = iniciative
        self.alzureShieldInt = alzureShieldInt

    def action(self):
        pass

    def moveOrCollide(self, posXint, posY, newPosX, newPosY):
        pass

    def action2(self, zn):
        pass

    def collision(self, attackerX, attackerY, code):
        pass

    def drawing(self):
        pass

    def getType(self):
        pass

    def getPosX(self):
        pass

    def getPosY(self):
        pass

    def setPosX(self, newPosX):
        pass

    def setPosY(self, newPosY):
        pass

    def incrementAge(self):
        pass

    def getAge(self):
        pass

    def getIniciative(self):
        pass

    def setStrenght(self, str):
        pass

    def getStrenght(self):
        pass

    def getTypeInString(self):
        pass

    def blocked(self, opponent):
        pass

    def runAway(self):
        pass

    def alzureShield(self):
        pass

    def alzureShieldHowManyTures(self):
        pass

    def alzureShieldActive(self):
        pass