import dirsync
from tkinter import *
from tkinter import filedialog

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("File Synchronizer")
        self.rowcount = 0
        self.sourcefile = []
        self.targetfile = []
        self.browsericon = PhotoImage(file="folderimage.png")

        self.row_frame = Frame(self.root)
        self.button_frame = Frame(self.root)

        self.button_frame.pack(side = "bottom", fill="x")
        self.row_frame.pack(side="top", fill="both", expand=True)

        startSync = Button(self.button_frame, text="Start", command=self.synchronize)
        plusButton = Button(self.button_frame, text = "+", command=self.create_new)

        startSync.grid(row=1, column=2)
        plusButton.grid(row=0, column=10)

        self.create_new()

        self.root.mainloop()

    def create_new(self):
        self.rowcount += 1
        self.sourceDirectory = Entry(self.row_frame, width=10)
        self.targetDirectory = Entry(self.row_frame, width=10)
        self.sourceDirectory.insert(0, "Source")
        self.targetDirectory.insert(1, "Target")
        selectSource = Button(self.row_frame, image=self.browsericon, command=self.select_source, height=15, width=15)
        selectTarget = Button(self.row_frame, image=self.browsericon, command=self.select_target, height=15, width=15)

        self.sourceDirectory.grid(row=self.rowcount, column=0)
        self.targetDirectory.grid(row=self.rowcount, column=5)
        selectSource.grid(row=self.rowcount, column=1)
        selectTarget.grid(row=self.rowcount, column=10)

    def select_source(self):
        source = filedialog.askdirectory(title="Select Source")
        self.sourceDirectory.delete(0, END)
        self.sourceDirectory.insert(0, source)
#        source = self.sourceDirectory.get()
        self.sourcefile.append(source)

    def select_target(self):
        target = filedialog.askdirectory(title="Select Target")
        self.targetDirectory.delete(0, END)
        self.targetDirectory.insert(1, target)
#        target = self.targetDirectory.get()
        self.targetfile.append(target)

    def synchronize(self):
        for path in range(len(self.sourcefile)):
            dirsync.sync(self.sourcefile[path], self.targetfile[path], "sync", verbose = True)
            dirsync.sync(self.sourcefile[path], self.targetfile[path], "update", verbose = True)

Application()
