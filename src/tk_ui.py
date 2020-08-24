import tkinter as tk 
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 
from rename_fun import rename

class renamer_ui():
    def __init__(self):

        self.root=tk.Tk() 
        
        # setting the windows size 
        self.root.geometry("350x150") 
        self.root.title('FILE RENAMER')
        # declaring string variable 
        # for storing name and count 
        self.name_var=tk.StringVar() 
        self.count_int=tk.StringVar() 
        self.folder_path = tk.StringVar()
    def main(self):
        # creating a label for  
        # name using widget Label 
        self.name_label = tk.Label(self.root, text = 'FileName', 
                            font=('calibre', 
                                    10, 'bold')) 
        
        # creating a entry for input 
        # name using widget Entry 
        self.name_entry = tk.Entry(self.root, 
                            textvariable = self.name_var,font=('calibre',10,'normal')) 
        
        # creating a label for count 
        self.count_label = tk.Label(self.root, 
                            text = 'Enter Starting No.', 
                            font = ('calibre',10,'bold')) 
        
        # creating a entry for count 
        self.count_entry=tk.Entry(self.root, 
                            textvariable = self.count_int, 
                            font = ('calibre',10,'normal')) 

        # creating a label for location 
        self.loc_lab = tk.Label(self.root, 
                            text = 'Select_Directory', 
                            font = ('calibre',10,'bold')) 
        
        # creating a entry for location 
        self.loc_entry=tk.Entry(self.root, 
                            textvariable = self.folder_path, 
                            font = ('calibre',10,'normal')) 
        
        # creating a button using the widget  
        # Button that will call the submit function  
        self.submit_button=tk.Button(self.root,text = 'Submit', 
                        command = self.submit) 
        
        # placing the label and entry in 
        # the required position using grid 
        # method 
        self.name_label.grid(row=4,column=1) 
        self.name_entry.grid(row=4,column=2) 
        self.count_label.grid(row=5,column=1) 
        self.count_entry.grid(row=5,column=2) 
        self.loc_lab.grid(row=2,column=1) 
        self.loc_entry.grid(row=2,column=2) 
        self.submit_button.grid(row=6,column=2) 


        self.button2 = Button(text="Browse", command=self.browse_button)
        self.button2.grid(row=2, column=3)



        # performing an infinite loop  
        # for the window to display 
        self.root.mainloop()


    # defining a function that will 
    # get the name and count and  
    # print them on the screen 
    def submit(self): 
    
        name=self.name_entry.get() 
        count=int(self.count_int.get()) 
        loc = self.loc_entry.get()
        

        if len(loc) >3: 
            loc = loc+"/"
        
            print("file directory : ",loc)
            if len(name)>0 and (count)>0:
                print("The name of the files to change : " + name) 
                print("The no for the file name start : " + str(count)) 
                rename(loc,name,count)
                tk.messagebox.showinfo("Submitted", "completed") 
                self.root.quit()
            else:
                print("Enter name first")
                print("Enter count first")
                tk.messagebox.askretrycancel("Enter name & count", "Try again?")


        else:
            print("select file location first")
            tk.messagebox.askretrycancel("select file location first", "Try again?")

        self.name_var.set("") 
        self.count_int.set("") 
    
    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called self.folder_path
        # global self.folder_path
        filename = filedialog.askdirectory()
        self.folder_path.set(filename)
    
        
