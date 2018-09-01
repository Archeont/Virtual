import math
import tkinter as tk
from World import World

X = 40
Y = 35
fieldPixelSize = 20


def on_closing():
    root.destroy()
    exit()


def key(event):
    C.delete("all")
    T.delete('1.0', tk.END)
    if event.keysym == "Left":
        world.processActions(3)
    if event.keysym == "Right":
        world.processActions(4)
    if event.keysym == "Down":
        world.processActions(2)
    if event.keysym == "Up":
        world.processActions(1)
    world.drawWorld()
    world.drawCommunicates()


def saveFunction():
    win = tk.Toplevel()
    message = "Where to save"
    tk.Label(win, text=message).pack()
    v = tk.StringVar()
    tk.Entry(win, textvariable=v).pack()
    btn = tk.Button(win, text='OK', width=20, command=lambda: world.saveWorld(v.get(), win))
    btn.pack()


def loadFunction():
    win = tk.Toplevel()
    message = "From where load"
    tk.Label(win, text=message).pack()
    v = tk.StringVar()
    tk.Entry(win, textvariable=v).pack()
    btn = tk.Button(win, text='OK', width=20, command=lambda: world.loadWorld(v.get(), win))
    btn.pack()


def alzureFunction():
    p = world.getHumanPos()
    if p.X != -1:
        world.getXY(p.X, p.Y).alzureShieldActive()


def callback(event):
    x = event.x / fieldPixelSize
    x = math.floor(x)
    y = event.y / fieldPixelSize
    y = math.floor(y)
    master = tk.Tk()
    listbox = tk.Listbox(master)
    listbox.pack()
    for item in ["Wolf", "Human", "Sheep", "Cyber Sheep", "Turtle", "Antelope", "Fox", "Grass", "Guarana",
                 "Wolfish Berry", "Sosnowsky Hogweed", "Dandelion"]:
        listbox.insert(tk.END, item)
    btn = tk.Button(master, text='OK', width=20, command=lambda: world.insertNewOrganismByString(x, y,
                    listbox.get(listbox.curselection()), master))
    btn.pack()
    master.mainloop()


root = tk.Tk()
root.configure(background='blue')
root.protocol("WM_DELETE_WINDOW", on_closing)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
X = math.floor(screen_width/20)
Y = math.floor((screen_height-300)/20)
C = tk.Canvas(root, bg="green", height=Y*fieldPixelSize, width=X*fieldPixelSize)
AlzureBtn = tk.Button(root, text="Active alzure shield", command=alzureFunction)
SaveBtn = tk.Button(root, text="Save", command=saveFunction)
LoadBtn = tk.Button(root, text="Load", command=loadFunction)
root.bind('<Key>', key)
C.bind("<Button-1>", callback)
C.pack()
AlzureBtn.pack()
SaveBtn.pack()
LoadBtn.pack()
S = tk.Scrollbar(root)
T = tk.Text(root, height=5)
S.pack(side=tk.RIGHT, fill="y", expand=False)
T.pack(side=tk.LEFT)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
world = World(X, Y, C, T)
world.drawWorld()
root.mainloop()
