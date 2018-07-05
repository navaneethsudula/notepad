import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
class Notepad:
     root=Tk()
     #default dimensions
     _width=650
     _height=400
     
     textarea=Text(root)
     _menubar=Menu(root)
     filemenu=Menu(_menubar,tearoff=0)
     editmenu=Menu(_menubar,tearoff=0)
     helpmenu=Menu(_menubar,tearoff=0)
     #adding scrollbar
     scroll=Scrollbar(textarea)
     _file=None
    
     def __init__(self,**kwargs):
       
        #setting icon
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        #set window size
        try:
            self._width=kwargs['width']
        except KeyError:
            pass

        try:
            self._height=kwargs['height']
        except KeyError:
            pass

        #set title
        self.root.title("Untitled-Notepad") 
        #centre the window
        screenwidth=self.root.winfo_screenwidth()
        screenheight=self.root.winfo_screenheight()

        #geometry of window
        left=(screenwidth/2)-(self._width/2)
        top=(screenheight/2)-(self._height/2)
        self.root.geometry('%dx%d+%d+%d'%(self._width,self._height,left,top))

        #to make text area autoresizable
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.textarea.grid(sticky=N+E+S+W)

        #add widgets
        #to open new file
        self.filemenu.add_command(label="New",command=self.newfile)
        #to open existing file
        self.filemenu.add_command(label="Open",command=self.openfile)
        #to save file
        self.filemenu.add_command(label="Save",command=self.savefile)
        self.filemenu.add_separator()
        #to exit application
        self.filemenu.add_command(label="Exit",command=self.exitapplication)
        self._menubar.add_cascade(label="File",menu=self.filemenu)
        #to copy text in file
        self.editmenu.add_command(label="Copy",command=self.copytext)
        #to give feature of cut
        self.editmenu.add_command(label="Cut",command=self.cuttext)
        #to give feature of paste
        self.editmenu.add_command(label="Paste",command=self.pastetext)
        self.editmenu.add_command(label="Undo",command=self.undo)
        self._menubar.add_cascade(label="Edit",menu=self.editmenu)
        #to show description about(help)
        self.helpmenu.add_command(label="About",command=self.showabout)
        self._menubar.add_cascade(label="Help",menu=self.helpmenu)

        #to configure menu
        self.root.config(menu=self._menubar)

        #adjusting scrollbar
        self.scroll.pack(side=RIGHT,fill=Y)
        self.scroll.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scroll.set)

     #adding functionality to widgets/controls
     #to exit application
     def exitapplication(self):
         self.root.destroy()
     def showabout(self):
         showinfo("Notepad","ask snr")
     def newfile(self):
         self.root.title("Untitled-Notepad")
         self._file=None
         self.textarea.delete(1.0,END)
     def openfile(self):
         self._file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt*")])
         if self._file=="":
            self._file=None 
         else:  
              # Try to open the file
              # set the window title
            self.root.title(os.path.basename(self._file)+"-Notepad")
            self.textarea.delete(1.0,END)
            file=open(self._file,"r")
            self.textarea.insert(1.0,file.read())
            file.close()
     def savefile(self):
         if self._file==None:
             #saving new file
             self._file = asksaveasfilename(initialfile='Untitled-txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files", "*.*"), 
                                                       ("Text Documents", "*.txt*")])
             if self._file=="":
                self._file=None
             else:
                 # Try to save the file
                 file=open(self._file,"w")
                 file.write(self.textarea.get(1.0,END))
                 file.close()
                 # Change the window title
                 self.root.title(os.path.basename(self._file)+"-Notepad")
         else:
             file = open(self._file, "w")
             file.write(self.textarea.get(1.0, END))
             file.close()
     def copytext(self):
         self.textarea.event_generate("<<Copy>>")
     def cuttext(self):
         self.textarea.event_generate("<<Cut>>")
     def pastetext(self):
         self.textarea.event_generate("<<Paste>>")
     def undo(self):
         self.textarea.event_generate("<<Undo>>")    
    
 #run main application
notepad=Notepad()
notepad.root.mainloop()       


         



  
