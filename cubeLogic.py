class logic():
    def __init__(self):
        self.cubeShell={}
        self.edge=[]
        self.corner=[]
        self.center=[]
        faces=['A', 'B', 'C', 'D', 'E', 'F']
        for face in faces:
            if (face == 'A'):
                value = "yellow"
            if (face == 'B'):
                value = "orange"
            if (face == 'C'):
                value = "blue"
            if (face == 'D'):
                value = "red"
            if (face == 'E'):
                value = "green"
            if (face == 'F'):
                value = "white"
            #Create Centers
            for i in range(9):
                self.cubeShell[face + str(i)] = value
            self.center.append((face+"4",))
        #Create Edges
        self.edge.append(("C1","A7"))
        self.edge.append(("C3", "B5"))
        self.edge.append(("C5", "D3"))
        self.edge.append(("C7", "F1"))
        self.edge.append(("E1", "A1"))
        self.edge.append(("E3", "D5"))
        self.edge.append(("E5", "B3"))
        self.edge.append(("E7", "F7"))
        self.edge.append(("A5", "D1"))
        self.edge.append(("F5", "D7"))
        self.edge.append(("A3", "B1"))
        self.edge.append(("F3", "B7"))

        #Create Corners
        self.corner.append(("C0", "B2", "A6"))
        self.corner.append(("C2", "D0", "A8"))
        self.corner.append(("C6", "B8", "F0"))
        self.corner.append(("C8", "D6", "F2"))
        self.corner.append(("E0", "D2", "A2"))
        self.corner.append(("E2", "B0", "A0"))
        self.corner.append(("E6", "D8", "F8"))
        self.corner.append(("E8", "B6", "F6"))

    #swaps 4 corners 1->2 2->3 3->4 4->1
    def cycleCorners(self,face,index1,index2,index3,index4):
        temp=[]
        cE= [0, 0]
        dB= [0, 0]
        fA = [0, 0]
        rotate=0
        if face == 'C' or face == 'E':
            i=0
            cE = [1,2]
        if face == 'D' or face == 'B':
            i=1
            dB= [0, 2]
        if face == 'F' or face == 'A':
            i=2
            fA= [0,1]
        for x in range(3):
            if x%2==0:
                a = dB[0] + cE[0] + fA[0]
                b = dB[1] + cE[1] + fA[1]
            if x%2==1:
                a = dB[1] + cE[1] + fA[1]
                b = dB[0] + cE[0] + fA[0]
            if x==0: a=b=i
            temp.append(self.cubeShell[self.corner[index4][b]])
            self.cubeShell[self.corner[index4][b]]=self.cubeShell[self.corner[index3][a]]
            self.cubeShell[self.corner[index3][a]] = self.cubeShell[self.corner[index2][b]]
            self.cubeShell[self.corner[index2][b]] = self.cubeShell[self.corner[index1][a]]
            self.cubeShell[self.corner[index1][a]] = temp[-1]
            i+=1
            if i==3: i=0


    def cycleEdges(self,face, index1, index2, index3, index4):
        temp = []
        inverse=0
        if face=='A' or face=='F'  or face=="Slice":
            inverse=-1
        for i in range(2):
            temp.append(self.cubeShell[self.edge[index4][i+inverse]])
            self.cubeShell[self.edge[index4][i+inverse]] = self.cubeShell[self.edge[index3][i]]
            self.cubeShell[self.edge[index3][i]] = self.cubeShell[self.edge[index2][i+inverse]]
            self.cubeShell[self.edge[index2][i+inverse]] = self.cubeShell[self.edge[index1][i]]
            self.cubeShell[self.edge[index1][i]] = temp[-1]

    def getFace(self,face):
        rtn=[]
        x=0
        for i in range(9):
            rtn.append(self.cubeShell[face+str(i)])
        return rtn
    #Precondition, valid move in 3x3 notation
    def move(self, notation):
        chars = {'U':'A', 'L':'B', 'F':'C','R':'D', 'B':'E', 'D':'F'}
        if notation in chars:
            keyChar = chars[notation]
            edgeIndex = [-1, -1, -1, -1]
            cornerIndex = [-1, -1, -1, -1]
            for i in range(len(self.edge)):
                if keyChar + "1" in self.edge[i]: edgeIndex[0] = i
                if keyChar + "5" in self.edge[i]: edgeIndex[1] = i
                if keyChar + "7" in self.edge[i]: edgeIndex[2] = i
                if keyChar + "3" in self.edge[i]: edgeIndex[3] = i

            for i in range(len(self.corner)):
                if keyChar + "0" in self.corner[i]: cornerIndex[0] = i
                if keyChar + "2" in self.corner[i]: cornerIndex[1] = i
                if keyChar + "8" in self.corner[i]: cornerIndex[2] = i
                if keyChar + "6" in self.corner[i]: cornerIndex[3] = i
            self.cycleEdges(keyChar, edgeIndex[0], edgeIndex[1], edgeIndex[2], edgeIndex[3])
            self.cycleCorners(keyChar, cornerIndex[0], cornerIndex[1], cornerIndex[2], cornerIndex[3])
        #all single letter exceptions
        if notation == 'M':
            self.cycleEdges("Slice", 0, 4, 7, 3)
            temp=self.cubeShell["C4"]
            self.cubeShell["C4"]=self.cubeShell["F4"]
            self.cubeShell["F4"]=self.cubeShell["E4"]
            self.cubeShell["E4"]=self.cubeShell["A4"]
            self.cubeShell["A4"]=temp
        if(notation=='E'):
            self.cycleEdges("Slice", 1, 2, 5, 6)
            temp=self.cubeShell["C4"]
            self.cubeShell["C4"]=self.cubeShell["B4"]
            self.cubeShell["B4"]=self.cubeShell["E4"]
            self.cubeShell["E4"]=self.cubeShell["D4"]
            self.cubeShell["D4"]=temp
        if (notation == 'S'):
            self.cycleEdges("Slice", 8, 10, 11, 9)
            temp = self.cubeShell["B4"]
            self.cubeShell["B4"] = self.cubeShell["A4"]
            self.cubeShell["A4"] = self.cubeShell["D4"]
            self.cubeShell["D4"] = self.cubeShell["F4"]
            self.cubeShell["F4"] = temp
        # lower case
        if notation in ["l", "r", "u", "d", "f", "b"]:
            self.move(notation.upper())
            withSlice=["r","d","b"]
            modifier="\'"
            if notation in withSlice: modifier=""
            if notation in ["l","r"]:
                self.move("M"+modifier)
            if notation in ["u","d"]:
                self.move("E"+modifier)
            if notation in ["f","b"]:
                self.move("S"+modifier)
        #Cube Rotations
        if notation=="X":
            self.move("r")
            self.move("L\'")
        if notation=="Z":
            self.move("f")
            self.move("B\'")
        if notation=="Y":
            self.move("u")
            self.move("D\'")
        #all [x]2 moves
        if notation[-1]=="2":
            for i in range(2): self.move(notation[0])
        #all [x]' moves
        if notation[-1]=="\'":

            for i in range(3): self.move(notation[0])

    #takes an algortham in the form of a list and applies it to the cube
    def algoritham(self,lst):
        for step in lst:
            self.move(step)