
from Organisms.Organism import Organism
from Organisms.Point import Point
from Organisms.Animals import *
from Organisms.Plants import *


class World:
    def __init__(self, X, Y, canvas, T):
        self.createNew(X, Y)
        self.TextField = T
        self.fieldPixelSize = 20
        self.canvas = canvas
        self.DENSITY = 0.1
        self.help = 0
        self.communicates = ""
        self.NUMBER_OF_CREATURES = 11
        self.table[0][0] = Human(self, 0, 0)
        self.humanPos = Point(0, 0)
        self.vecOrganism.append(self.table[0][0])
        cuantity = randint(1, int(self.X * self.Y * self.DENSITY))
        for i in range(0, cuantity-1):
            posX = randint(0, self.X-1)
            posY = randint(0, self.Y-1)
            while not self.isPlaceFree(posX, posY):
                posX = randint(0, self.X-1)
                posY = randint(0, self.Y-1)
            creatureID = randint(3, 3+self.NUMBER_OF_CREATURES)
            if creatureID == 3:
                self.table[posY][posX] = Wolf(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 4:
                self.table[posY][posX] = Sheep(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 5:
                self.table[posY][posX] = Fox(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 6:
                self.table[posY][posX] = Turtle(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 7:
                self.table[posY][posX] = Antelope(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 8:
                self.table[posY][posX] = Grass(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 9:
                self.table[posY][posX] = Dandelion(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 10:
                self.table[posY][posX] = Guarana(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 11:
                self.table[posY][posX] = WolfishBerry(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 12:
                self.table[posY][posX] = SosnowskyHogweed(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])
            elif creatureID == 13:
                self.table[posY][posX] = CyberSheep(self, posX, posY)
                self.vecOrganism.append(self.table[posY][posX])

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def collisionSlover(self, posX, posY, newPosX, newPosY):
        if self.table[posY][posX] is not None:
            if self.table[newPosY][newPosX].getType() == self.table[posY][posX].getType():
                self.table[newPosY][newPosX].collision(posX, posY, 1)
            elif self.table[newPosY][newPosX].runAway():
                self.table[newPosY][newPosX].collision(posX, posY, 2)
            elif self.table[newPosY][newPosX].alzureShield():
                self.table[newPosY][newPosX].collision(posX, posY, 3)
            elif not self.table[newPosY][newPosX].blocked(self.table[posY][posX]):
                self.table[newPosY][newPosX].collision(posX, posY, 0)

    def move(self, posX, posY, newPosX, newPosY):
        if (newPosX >= 0) and (newPosX < self.X):
            if (newPosY >= 0) and (newPosY < self.Y):
                if self.table[posY][posX] is not None:
                    self.table[newPosY][newPosX] = self.table[posY][posX]
                    self.table[newPosY][newPosX].setPosX(newPosX)
                    self.table[newPosY][newPosX].setPosY(newPosY)
                    self.table[posY][posX] = None

    def isPlaceFree(self, X, Y):
        if self.areInWorld(X, Y):
            if self.table[Y][X] is None:
                return True
        return False

    def getXY(self, newPosX, newPosY):
        return self.table[newPosY][newPosX]

    def setXY(self, ourX, ourY, toPut):
        self.table[ourY][ourX] = toPut

    def processActions(self, zn):
        self.communicates = ""
        self.vecOrganism.sort(reverse=True, key=lambda x: x.iniciative)
        hum = Types.human
        for i in range(0, len(self.vecOrganism)):
            if i < len(self.vecOrganism):
                if self.vecOrganism[i] is not None:
                    self.vecOrganism[i].incrementAge()
                    if self.vecOrganism[i].getType() is not hum:
                        self.vecOrganism[i].action()
                    else:
                        self.vecOrganism[i].action2(zn)
            else:
                return

    def findFreeField(self, posX, posY):
        for i in range(-1, 1):
            for j in range(-1, 1):
                if self.areInWorld(posX+i, posY+j):
                    if self.table[posY+j][posX+i] is None:
                        return Point(posX+i, posY+j)
        return Point(-1, -1)

    def changeHumanX(self, how):
        self.humanPos.X = how

    def changeHumanY(self, how):
        self.humanPos.Y = how

    def getHumanPos(self):
        return self.humanPos

    def insertNewOrganism(self, posX, posY, type):
        if type is Types.wolf:
            self.table[posY][posX] = Wolf(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.sheep:
            self.table[posY][posX] = Sheep(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.fox:
            self.table[posY][posX] = Fox(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.turtle:
            self.table[posY][posX] = Turtle(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.antelope:
            self.table[posY][posX] = Antelope(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.grass:
            self.table[posY][posX] = Grass(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.guarana:
            self.table[posY][posX] = Guarana(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.dandelion:
            self.table[posY][posX] = Dandelion(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.wolfishBerry:
            self.table[posY][posX] = WolfishBerry(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.sosnowskyHogweed:
            self.table[posY][posX] = SosnowskyHogweed(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type is Types.cyberSheep:
            self.table[posY][posX] = CyberSheep(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])

    def insertNewOrganismByString(self, posX, posY, type, master):
        master.destroy()
        if type == "Wolf":
            self.table[posY][posX] = Wolf(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Sheep":
            self.table[posY][posX] = Sheep(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Fox":
            self.table[posY][posX] = Fox(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Turtle":
            self.table[posY][posX] = Turtle(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Antelope":
            self.table[posY][posX] = Antelope(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Grass":
            self.table[posY][posX] = Grass(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Guarana":
            self.table[posY][posX] = Guarana(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Dandelion":
            self.table[posY][posX] = Dandelion(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Wolfish Berry":
            self.table[posY][posX] = WolfishBerry(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Sosnowsky Hogweed":
            self.table[posY][posX] = SosnowskyHogweed(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Cyber Sheep":
            self.table[posY][posX] = CyberSheep(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        elif type == "Human":
            self.table[posY][posX] = Human(self, posX, posY)
            self.vecOrganism.append(self.table[posY][posX])
        self.drawWorld()

    def addCommunicate(self, com):
        self.communicates += com + '\n'

    def drawCommunicates(self):
        if self.humanPos.X != -1:
            if self.getXY(self.humanPos.X, self.humanPos.Y) is not None:
                if self.getXY(self.humanPos.X, self.humanPos.Y).alzureShield():
                    self.TextField.insert('1.0', "Alzure Shield is active\n")
            else:
                self.humanPos.X = -1
        self.TextField.insert('2.0', self.communicates)
        self.communicates = ""

    def removeFromVector(self, toDelete):
        self.vecOrganism.remove(toDelete)

    def areInWorld(self, X2, Y2):
        if (X2 >= 0) and (X2 < self.X):
            if (Y2 >= 0) and (Y2 < self.Y):
                return True
        return False

    def isThisAnimal(self, posX, posY):
        if self.table[posY][posX] is not None:
            help = self.table[posY][posX].getType()
            if (help == Types.wolf) or (help == Types.sheep) or (help == Types.human):
                return True
            if (help == Types.turtle) or (help == Types.fox) or (help == Types.antelope):
                return True
        return False

    def drawWorld(self):
        for i in range(0, self.Y):
            for j in range(0, self.X):
                if self.table[i][j] is not None:
                    if self.table[i][j].getType() == Types.human:
                        self.canvas.create_rectangle(j * self.fieldPixelSize, i * self.fieldPixelSize,
                                                     (j + 1) * self.fieldPixelSize, (i + 1) * self.fieldPixelSize,
                                                     fill='blue')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="H")
                    if self.table[i][j].getType() == Types.wolf:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize, fill='red')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="W")
                    if self.table[i][j].getType() == Types.sheep:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='yellow')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="S")
                    if self.table[i][j].getType() == Types.turtle:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='yellow')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="T")
                    if self.table[i][j].getType() == Types.antelope:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='yellow')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="A")
                    if self.table[i][j].getType() == Types.fox:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='yellow')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="F")
                    if self.table[i][j].getType() == Types.cyberSheep:
                        self.canvas.create_rectangle(j * self.fieldPixelSize, i * self.fieldPixelSize,
                                                     (j + 1) * self.fieldPixelSize, (i + 1) * self.fieldPixelSize,
                                                     fill='red')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="C")
                    if self.table[i][j].getType() == Types.grass:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize, fill='green')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="G")
                    if self.table[i][j].getType() == Types.dandelion:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='green')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="D")
                    if self.table[i][j].getType() == Types.guarana:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='green')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="g")
                    if self.table[i][j].getType() == Types.wolfishBerry:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='green')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="w")
                    if self.table[i][j].getType() == Types.sosnowskyHogweed:
                        self.canvas.create_rectangle(j*self.fieldPixelSize, i*self.fieldPixelSize,
                                                     (j+1)*self.fieldPixelSize, (i+1)*self.fieldPixelSize,
                                                     fill='green')
                        self.canvas.create_text((j+0.5)*self.fieldPixelSize, (i+0.5)*self.fieldPixelSize, fill='black', text="s")

    def deleteAll(self):
        self.vecOrganism = None
        self.table = None
        self.X = 0
        self.Y = 0

    def createNew(self, X, Y):
        self.X = X
        self.Y = Y
        self.vecOrganism = list()
        self.table = [[Organism() for _ in range(0, self.X)] for _ in range(0, self.Y)]
        for i in range(0, self.Y):
            for j in range(0, self.X):
                self.table[i][j] = None

    def readNextNumber(self, allString):
        num = 0
        while self.help <= len(allString) and allString[self.help] != '?':
            if allString[self.help] == '-':
                self.help += 1
                num += int(allString[self.help])
                num = -num
            else:
                num *= 10
                num += int(allString[self.help])
            self.help += 1
        self.help += 1
        return num

    def saveWorld(self, path, win):
        win.destroy()
        file = open(path, "w")
        file.write("%d?%d?" % (self.X,  self.Y))
        for i in range(len(self.vecOrganism)):
            file.write("%c?%d?%d?%d?%d?" % (self.vecOrganism[i].drawing(), int(self.vecOrganism[i].getStrenght()),
                                         int(self.vecOrganism[i].getAge()), int(self.vecOrganism[i].getPosX()),
                                         int(self.vecOrganism[i].getPosY())))
            if self.vecOrganism[i].drawing() == 'H':
                file.write("%d?" % int(self.vecOrganism[i].alzureShieldHowManyTures()))
        file.write("!")
        file.close()

    def loadWorld(self, path, win):
        win.destroy()
        file = open(path, "r")
        allString = file.read()
        self.deleteAll()
        self.help = 0
        x = self.readNextNumber(allString)
        y = self.readNextNumber(allString)
        self.createNew(x, y)
        while allString[self.help] != '!':
            type = allString[self.help]
            self.help += 2
            str = self.readNextNumber(allString)
            age = self.readNextNumber(allString)
            posX = self.readNextNumber(allString)
            posY = self.readNextNumber(allString)
            if type == 'H':
                alzure = self.readNextNumber(allString)
                self.table[posY][posX] = Human(self, posX, posY, alzure, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'W':
                self.table[posY][posX] = Wolf(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'g':
                self.table[posY][posX] = Guarana(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'S':
                self.table[posY][posX] = Sheep(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'A':
                self.table[posY][posX] = Antelope(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'F':
                self.table[posY][posX] = Fox(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'T':
                self.table[posY][posX] = Turtle(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'G':
                self.table[posY][posX] = Grass(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'D':
                self.table[posY][posX] = Dandelion(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'w':
                self.table[posY][posX] = WolfishBerry(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 's':
                self.table[posY][posX] = SosnowskyHogweed(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
            if type == 'C':
                self.table[posY][posX] = CyberSheep(self, posX, posY, age, str)
                self.vecOrganism.append(self.table[posY][posX])
        file.close()
        self.canvas.delete("all")
        self.drawWorld()
