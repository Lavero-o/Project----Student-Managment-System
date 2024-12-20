import pickle
import tkinter as tk
from tkinter import ttk


data_file = 'Project -- Student Managment System/storage.data'
assets = "Project -- Student Managment System/Assets/"

class Student:
    def __init__(self, name: str, roll_number: int, student_class: str, grades: list, attendance_percentage: float, extracurricular_activities: list) -> None:
        self.name = name
        self.roll_number = roll_number
        self.student_class = student_class
        self.grades = grades
        self.attendance_percentage = attendance_percentage
        self.extracurricular_activities = extracurricular_activities
    
    def getAverageGrade(self):
        average = 0
        if self.grades.__len__() != 0:
            average = sum(self.grades)/self.grades.__len__()
        return average

class Account:
    def __init__(self, name: str, password: str, students: list[Student]):
        
        self.name = name
        self.password = password
        self.students = students
    
    def findStudentByName(self, name: str):
        for student in self.students:
            if student.name == name:
                return(student)
            


class GUI:

    def __init__(self, root:tk.Tk):
        self.currentAccount: Account = None
        self.root = root
        self.root.grid_columnconfigure(0,weight=1)
        self.root.resizable(False,False)
        self.loginGUI()
        self.root.mainloop()
    
    

    def editGUI(self, student: Student, attribute: str):
        root = self.root
        self.clearGUI()

        self.makeTable(0,student.__getattribute__[attribute], [attribute], [attribute])

    
    def viewGUI(self, mainGUI, student: Student):
        self.clearGUI()
        root = self.root

        def makeFrame(root, text):
            frame = tk.Frame(root)
            ttk.Label(frame, text=text).grid(row=0)
            ttk.Entry(frame, width=7).grid(row=0,column=1)
            return frame


        headFrame = tk.Frame(root)
        makeFrame(headFrame, text="Name - "+str(student.name)).pack()

        frame1 = tk.Frame(root)
        makeFrame(frame1, text="Roll number - "+str(student.roll_number)).pack(pady=3, anchor="e")
        makeFrame(frame1, text="Class - "+str(student.student_class)).pack(pady=3, anchor="e")
        makeFrame(frame1, text="Attendance - "+str(student.attendance_percentage)).pack(pady=3, anchor="e")

        frame2 = tk.Frame(root)
        makeFrame(frame2, text="Avg. grade - "+str(student.getAverageGrade())).pack(pady=3, anchor="e")
        makeFrame(frame2, text="Activities - "+str(student.extracurricular_activities)).pack(pady=3, anchor="e")


        headFrame.grid(columnspan=2, pady=10)
        frame1.grid(row=1,padx=5,pady=5,column=0)
        frame2.grid(row=1,padx=5,pady=5,column=1)

        ttk.Button(root, text="Done", command= self.accountGUI).grid(row=3, columnspan=2)

    def clearGUI(self):
        root = self.root
        elements = []
        for element in root.children:
          elements.append(element)
    
        for element in elements:
          root.children[element].destroy()

    def newStudentGUI(self):
        root = self.root
        self.clearGUI()
        ttk.Label(root, text="Add student", font=("",12,"bold")).grid(row=0,columnspan=2)

        ttk.Label(root, text="Student name").grid(row=1, column=0)
        name = ttk.Entry(root); name.grid(row=1,column=1)

        ttk.Label(root, text="Roll number").grid(row=2, column=0)
        rollNum = ttk.Entry(root); rollNum.grid(row=2,column=1)

        ttk.Label(root, text="Class").grid(row=3, column=0)
        studentClass = ttk.Entry(root); studentClass.grid(row=3,column=1)

        ttk.Label(root, text="Attendance").grid(row=4, column=0)
        attendance = ttk.Entry(root); attendance.grid(row=4,column=1)

        ttk.Button(root, text="Done", command=lambda: addStudent(self, name.get(),int(rollNum.get()),studentClass.get(),float(attendance.get()))).grid(row=5, columnspan=2)

    def loginGUI(self):

        root = self.root
        self.clearGUI()
        ttk.Label(root, text="Log in", font=("Calibri","20","bold")).grid(row=0,columnspan=2, pady=(10,10))

        nameFrame = ttk.Frame(root)

        nameLabel = ttk.Label(nameFrame, text="Account name")
        nameEntry = ttk.Entry(nameFrame)
        nameLabel.pack(side="left")
        nameEntry.pack(side="left",padx=(0,10))
        nameFrame.grid(row=1)


        passwordFrame = ttk.Frame(root)

        passwordLabel = ttk.Label(passwordFrame, text="Password")
        passwordEntry = ttk.Entry(passwordFrame)
        passwordLabel.pack(side="left")
        passwordEntry.pack(side="left", padx=(0,10))
        passwordFrame.grid(row=2)
        

        ttk.Button(root, text="Login", command=lambda: login(self, nameEntry, passwordEntry)).grid(row=3,columnspan=2)
        ttk.Button(root, text="Dont have account", command=lambda: self.registerGUI()).grid(row=4,columnspan=2)


    def registerGUI(self):

        root = self.root
        self.clearGUI()

        ttk.Label(root, text="Register", font=("", 12, "bold")).grid(row=0,columnspan=2)
        ttk.Label(root, text="Account name").grid(row=1, column=0)
        ttk.Label(root, text="Password").grid(row=2, column=0)
        ttk.Label(root, text="Confirm password").grid(row=3, column=0)

        name, password1, password2 = ttk.Entry(root), ttk.Entry(root), ttk.Entry(root) 

        name.grid(row=1, column=1)
        password1.grid(row=2, column=1)
        password2.grid(row=3, column=1)

        ttk.Button(root, text="Create account", command=lambda: register(self, name, password1, password2)).grid(row=4,columnspan=2)
        ttk.Button(root, text="Cancel", command=lambda: self.loginGUI()).grid(row=5, columnspan=2)


    def accountGUI(self):

        root = self.root
        self.clearGUI()
        account = self.currentAccount


        headerFrame = tk.Frame(root, background="#222324")
        ttk.Label(headerFrame, text=f"Welcome {account.name}!", font=("", 14, "bold"),anchor="center", width=14, background="#222324", foreground="white").grid(row=0, column=0,pady=(10,10), padx=(10,10))
        ttk.Button(headerFrame, text="Log out", command=lambda: self.loginGUI()).grid(row=0, column=1, padx=(0,5))
        ttk.Button(headerFrame, text="Delete account", command=lambda: removeAccount(self, account)).grid(row=0,column=2,padx=(0,10))
        headerFrame.grid(row=0,column=0)


        mainFrame = tk.Frame(root, background="#646566")

        row = 0
        for student in account.students:

            ttk.Label(mainFrame, text = student.name, font="Arial 14", foreground="white", background="#363738", padding=5).grid(row=row, column=0, pady=5,padx=5, sticky=("we"))

            viewImg = tk.PhotoImage(file = assets+"view_icon.png")
            viewButton = makeButton(mainFrame, viewImg, self.viewGUI, self, student)
            viewButton.image = viewImg
            viewButton.grid(row=row,column=1,padx=5)

            removeImg = tk.PhotoImage(file = assets+"remove_icon.png")
            removeButton = makeButton(mainFrame, removeImg, removeStudent, self, student)
            removeButton.image = removeImg
            removeButton.grid(row=row,column=2,padx=5)
            
            row += 1
        
        mainFrame.grid(row=1, sticky="we")


        plusImg = tk.PhotoImage(file = assets+"add_icon.png")
        b = ttk.Button(root, text="Add student", image=plusImg, compound=tk.LEFT, command=lambda: self.newStudentGUI())
        b.image = plusImg
        b.grid(sticky="w", row=2)




def write_data(item):
    file = open(data_file, 'wb')
    pickle.dump(item, file)
    file.close()

def read_data():
    file = open(data_file, 'rb')
    data = pickle.load(file)
    return data

data : dict[str,Account] = read_data()
print(data)


def removeStudent(mainGUI: GUI, student):
    acc = mainGUI.currentAccount
    acc.students.remove(student)
    mainGUI.accountGUI()
    write_data(data)

def addStudent(mainGUI: GUI, name, rollNum: int, studentClass: str, attendance: float):
    if name.__len__() == 0:
        print("Student name field is empty!")
        return
    
    mainGUI.currentAccount.students.append(Student(name,rollNum,studentClass,[],attendance,[]))
    mainGUI.accountGUI()
    write_data(data)


def makeButton(root, image, command, mainGUI, student):
    return ttk.Button(root, image=image, command=lambda: command(mainGUI, student))

def register(mainGUI: GUI, name: ttk.Entry, password1: ttk.Entry, password2: ttk.Entry):

    if name.get().__len__() == 0:
        print("Account name field is empty!")
    elif name.get() in data:
        print("Account name is already taken!")
    elif password1.get().__len__() == 0:
        print("Password field is empty!")
    elif password1.get() != password2.get():
        print("Passwords dont match!")
    else:
        print("Account created!")

        data[name.get()] = Account(name.get(), password1.get(), [])

        write_data(data)
        print(data)
        mainGUI.loginGUI()

def login(mainGUI: GUI, name: ttk.Entry, password: ttk.Entry):
    
    if name.get().__len__() == 0:
        print("Account name field is empty!")
    elif name.get() not in data:
        print("Account not found")
    elif password.get() != data[name.get()].password:
        print("Incorrect Password!")
    else:
        print(f"Welcome {name.get()}!")
        mainGUI.currentAccount = data[name.get()]
        mainGUI.accountGUI()


def removeAccount(mainGUI: GUI,account: Account):
    data.pop(account.name)
    write_data(data)
    mainGUI.loginGUI()
    print(f"Account {account.name} was removed")

mainGUI = GUI(tk.Tk())