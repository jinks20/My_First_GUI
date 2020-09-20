from tkinter import *
import os,shutil
from tkinter import filedialog,messagebox
class Sorting_Application():
    def __init__(self,root):
        self.root=root
        self.root.geometry("850x560")
        self.root.maxsize(910,620)
        self.root.minsize(830,540)
        self.root.title("Ajinkya Makode - Welcome To My GUI")
        self.root.config(bg="white")
        title = Label(self.root, padx=10, text="SORTING  APPLICATION", font="impact 20", bg="#262626", fg="white"
                      ,anchor="w").place(x=0, y=0, relwidth=1)


        select_folder = Label(self.root, text="Select Folder", font="georgia 15", bg="white").place(x=50, y=90)
        self.folder_name = StringVar()
        Select_path = Entry(self.root, font=("times new roman", 14), bg="lightgray", fg="black",textvariable=self.folder_name).place(x=180, y=93, width=350)
        button_brw = Button(self.root, text="BROWSE", font="georgia 11", relief=SUNKEN, bg="#262626", command=self.browse1,fg="white",
                            cursor="hand2").place(x=550, y=89, height=30, width=100)


        line = Label(self.root, bg="#262626").place(x=30, y=160, height=1, width=790)

        self.total_file = Label(root, text="Total Files: ", font="georgia 15", bg="white")
        self.total_file.place(x=60, y=180)

        line2 = Label(self.root, bg="#262626").place(x=30, y=290, height=1, width=790)

        self.dicto = {"Images": [".png", ".JPG", ".jpeg", ".jpg", ".JPEG", ".ai", ".tif"],
                      "Videos": [".mp4", ".mkv", ".avi", ".webm", ".3gp", ".mov", ".wmv", ],
                      "Audios": [".wav", ".mp3", ".aif", ".wpl", ".cda", ".mid", ".midi", ".mpa"],
                      "Compressed File": [".rar", ".pkg", ".zip", ".7z", ".arj", ".deb", ".rpm", ".z"],
                      "Software": [".apk", ".bin", ".exe", ".wsf", ".msi"],
                      "codes": [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".swift", ".class"],
                      "Documents": [".pdf", ".txt", ".xlsx", ".xls", ".ods", ".doc", ".docx", ".ppt", ".pptx", ".pps"]}


        self.name_other = StringVar()
        select_otherfolder = Label(self.root, text="For Unknown File:", font="georgia 15", bg="white", fg="blue").place(x=50,y=380)
        select_otherfolder_name = Label(self.root, text="Enter Folder Name", font="georgia 13", bg="white").place(x=70,y=420)
        Select_othername = Entry(self.root, font="georgia 13", bg="lightgray", textvariable=self.name_other, fg="blue").place(x=230, y=423,width=280)

        self.button_clear = Button(self.root, text="CLEAR", activebackground="lightyellow",command=self.clear, font="georgia 11",
                                   relief=SUNKEN,bg="yellow",fg="#262626", cursor="hand2").place(x=550, y=480, height=30, width=100)
        self.button_start = Button(self.root, text="START", activebackground="lightyellow",command=self.starttte ,font="georgia 11",
                                   relief=SUNKEN,bg="orange",fg="#262626", cursor="hand2").place(x=670, y=480, height=30, width=100)



    def Renamee(self):
        for i in self.Filess:
            if os.path.isdir(os.path.join(self.Folderr, i)) == True:
                os.rename(os.path.join(self.Folderr, i), os.path.join(self.Folderr, i.capitalize()))

    def Otherrr(self):
        kp=self.name_other
        # if self.name_other !="":
        if kp != None:
            self.other_folder=self.name_other.get()
        # else:
        #     messagebox.showinfo("Error", "Please Enter Name")

    def browse1(self):
        op = filedialog.askdirectory()
        if op != None:
            self.folder_name.set(op)
            self.Folderr = self.folder_name.get()
            self.Otherrr()
            self.Filess=os.listdir(self.Folderr)
            self.count=1
            self.length=len(self.Filess)
            self.Renamee()

    def clear(self):
        self.folder_name.set("")
        self.name_other.set("")
        self.total_file.setvar("")


    def createe(self,ext, file_name):

        for folder_name in self.dicto:
            if "." + ext in self.dicto[folder_name]:
                if folder_name not in os.listdir(self.Folderr):
                    os.mkdir(os.path.join(self.Folderr, folder_name))
                shutil.move(os.path.join(self.Folderr, file_name), os.path.join(self.Folderr, folder_name))
                break

        else:
            if self.other_folder not in os.listdir(self.Folderr):
                os.mkdir(os.path.join(self.Folderr, self.other_folder))
            shutil.move(os.path.join(self.Folderr, file_name), os.path.join(self.Folderr, self.other_folder))


    def starttte(self):
        self.Otherrr()
        self.total_file.config(text="Total Files: " + str(self.length))

        if self.other_folder !="":
            # if kp != None:
                self.other_folder=self.name_other.get()
        else:
            messagebox.showinfo("Error", "Please Enter Name")


        if self.folder_name.get()!="":
            self.Filess = os.listdir(self.Folderr)
            for i in self.Filess:
                if os.path.isfile(os.path.join(self.Folderr, i)) == True:
                    ext = i.split(".")[-1]
                    self.createe(ext, i)
            messagebox.showinfo("Success","All Filess Has sort Successfully")
        else:
            messagebox.showinfo("Error","Please Select Folder")



root=Tk()
ajinkya=Sorting_Application(root)
root.mainloop()