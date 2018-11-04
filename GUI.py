from tkinter import *
import cubeLogic
class GUI():
    def __init__(self,logicCube):
        self.logicCube=logicCube
        root = Tk()
        topFrame = Frame(root)
        self.midFrame = Frame(root)
        bottomFrame= Frame(root)
        topFrame.pack(side=TOP)
        self.midFrame.pack()
        bottomFrame.pack(side=BOTTOM)
        #Buttons
        notations = [
            ["L", "R", "U", "D", "F", "B", "L\'", "R\'", "U\'", "D\'", "F\'", "B\'", "L2", "R2", "U2", "D2", "F2",
             "B2"],
            ["l", "r", "u", "d", "f", "b", "l\'", "r\'", "u\'", "d\'", "f\'", "b\'", "l2", "r2", "u2", "d2", "f2",
             "b2"], ["M", "E", "S", "M\'", "E\'", "S\'", "M2", "E2", "S2"], ["X", "Y", "Z", "X\'", "Y\'", "Z\'"]]
        btnNotations = []
        y = 0
        for array in notations:
            y0 = y
            x = 0
            lastx = -1
            for notation in array:
                btnNotations.append(Button(bottomFrame, text=notation, command=lambda n=notation: self.btnMove(n)))
                if "\'" in notation: x = 1
                if "2" in notation: x = 2
                if not (lastx == x): y = y0
                btnNotations[-1].grid(row=x, column=y)
                y += 1
                lastx = x
            y += 1
            spacer = Label(bottomFrame, text="       ")
            for i in range(4): spacer.grid(row=i, column=y)
            y += 1
        #render faces
        label = Label(topFrame, text="2D-Rubik's Cube")
        label.pack()
        colors = [logicCube.getFace("B"), logicCube.getFace("C"), logicCube.getFace("D"), logicCube.getFace("E"),
                  logicCube.getFace("A"), logicCube.getFace("F")]
        face = []

        for color in colors:
            face.append(Canvas(self.midFrame, height=75, width=75, bg="white"))
            x1 = 0
            x2 = 25
            y1 = 0
            y2 = -25
            for i in range(9):
                x1 += 25
                x2 += 25
                if (i % 3 == 0):
                    x1 = 0
                    x2 = 25
                    y1 += 25
                    y2 += 25
                face[-1].create_rectangle(x1, y1, x2, y2, fill=color[i])
        #Puts faces into place
        face[0].grid(row=1, column=0)
        face[1].grid(row=1, column=1)
        face[2].grid(row=1, column=2)
        face[3].grid(row=1, column=3)
        face[4].grid(row=0, column=1)
        face[5].grid(row=2, column=1)
        root.mainloop()
    #Update GUI
    def btnMove(self, n):
        self.logicCube.move(n)
        colors = [self.logicCube.getFace("B"), self.logicCube.getFace("C"), self.logicCube.getFace("D"), self.logicCube.getFace("E"),
                  self.logicCube.getFace("A"), self.logicCube.getFace("F")]
        face = []

        for color in colors:
            face.append(Canvas(self.midFrame, height=75, width=75, bg="white"))
            x1 = 0
            x2 = 25
            y1 = 0
            y2 = -25
            for i in range(9):
                x1 += 25
                x2 += 25
                if (i % 3 == 0):
                    x1 = 0
                    x2 = 25
                    y1 += 25
                    y2 += 25
                face[-1].create_rectangle(x1, y1, x2, y2, fill=color[i])
        #Puts faces into place
        face[0].grid(row=1, column=0)
        face[1].grid(row=1, column=1)
        face[2].grid(row=1, column=2)
        face[3].grid(row=1, column=3)
        face[4].grid(row=0, column=1)
        face[5].grid(row=2, column=1)
