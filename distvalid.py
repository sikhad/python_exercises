# Program including gui to validate whether a statistical distribution is valid

from tkinter import*

class DistValid:

    def __init__(self, rootWin):
        rootWin.title("Distribution Validator")

        f = Frame(rootWin)
        f.pack()

        l = Label(f, text="random label!", command=self.clicked)
        l.pack()

        b = Button(rootWin, text="Select File", command=self.clicked)
        b.grid(row=0, sticky=E)

        self.s = StringVar()
        self.t = StringVar()
        self.u = StringVar()
        self.v = StringVar()
        
        Label(rootWin, text="Valid Distribution?").grid(row=1, sticky=E)
        Label(rootWin, text="E(X)=").grid(row=2, sticky=E)
        Label(rootWin, text="E(Y)=").grid(row=3, sticky=E)

        self.e1 = Entry(rootWin, textvariable = self.s, width=60, state="readonly")
        self.s.set("...")
        
        self.e2 = Entry(rootWin, state="readonly", textvariable = self.t)
        self.e3 = Entry(rootWin, state="readonly", textvariable = self.u)
        self.e4 = Entry(rootWin, state="readonly", textvariable = self.v)

        self.e1.grid(row=0, column=1, sticky=W)
        self.e2.grid(row=1, column=1, sticky=W)
        self.e3.grid(row=2, column=1, sticky=W)
        self.e4.grid(row=3, column=1, sticky=W)

    def clicked(self):
        filepath = filedialog.askopenfilename()

        if filepath != "":
            self.s.set(filepath)
            
            self.readData(filepath)
            self.convertData(self.CSVData)
            
            self.checkValid()
        else:
            self.s.set("...")
            self.t.set("")
            self.u.set("")
            self.v.set("")

    # Read data
    def readData(self, fileName):
        import csv
        
        f = open(fileName, "r")
        reader = csv.reader(f, delimiter=",")
        self.CSVData = []
        for item in reader:
            self.CSVData.append(item)
        f.close()

        for i in range(len(self.CSVData)):
            for j in range(len(self.CSVData[i])):
                self.CSVData[i][j] = self.CSVData[i][j].strip()

    # Convert data to float
    def convertData(self, data):
        for i in range(0,1):
            for j in range(1, len(self.CSVData[i])):
                self.CSVData[i][j] = float(self.CSVData[i][j])
            
        for i in range(1, len(self.CSVData)):
            for j in range(len(self.CSVData[i])):
                self.CSVData[i][j] = float(self.CSVData[i][j])
    
    # Calculate marginal probabilities 
    def checkValid(self):
        xSum = 0
        ySum = 0
        self.xMarginalProb = []
        self.yMarginalProb = []
        for col in range(1, len(self.CSVData)):
            for row in range(1, len(self.CSVData[col])):
                ySum += self.CSVData[col][row]
                self.yMarginalProb.append(self.CSVData[col][row])

        for col in range(1, len(self.CSVData[0])):
            for row in range(1, len(self.CSVData)):
                xSum += self.CSVData[row][col]
                self.xMarginalProb.append(self.CSVData[row][col])

        if 0.9999 < xSum < 1.0001 and 0.9999 < ySum < 1.0001:
            self.t.set("Yes")
            self.calcExpected()
        else:
            self.t.set("No")
            print("The marginal probabilities do not sum to 1.")
            self.u.set("")
            self.v.set("")

    # Calculate expected values
    def calcExpected(self):
        a = 0
        aSum = 0
        bSum = 0
        xprob = 0
        yprob = 0
        for i in range(len(self.xMarginalProb)):
            aSum += self.xMarginalProb[i]
            if (i+1)%(len(self.CSVData)-1) == 0:
                a += 1
                xprob += self.CSVData[0][a]*aSum
                aSum = 0

        a = 0
        for i in range(len(self.xMarginalProb)):
            bSum += self.yMarginalProb[i]
            if (i+1)%(len(self.CSVData[0])-1) == 0:
                a += 1
                yprob += self.CSVData[a][0]*bSum
                bSum = 0
                
        self.u.set(xprob)
        self.v.set(yprob)                  

# Create gui and run program        
rootWin = Tk()
app.DistValid(rootWin)
rootWin.mainloop()
