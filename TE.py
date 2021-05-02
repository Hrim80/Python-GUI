from tkinter import *
from tkinter import ttk
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
from tkinter.filedialog import asksaveasfilename, askopenfilename

window = Tk()
window.title("Text Editor")
tabs=ttk.Notebook(window)
def newTabs(tabs):
    tab=ttk.Frame(tabs)
    tabs.add(tab,text="Tabs")
    tabs.pack(fill="both",expand=1)
    scrollbarY = Scrollbar(tab)
    scrollbarY.pack( side = RIGHT, fill=Y )
    ##scrollbarX = Scrollbar(window)
    ##scrollbarX.pack( side = BOTTOM, fill=X )
    editorFrame=Frame(tab)
    editor = Text(editorFrame,background = "#2a2a2f",foreground = "#F2F0ED",insertbackground="white",undo='True',yscrollcommand=scrollbarY.set)
    editor.pack(fill=BOTH,expand=True)
    editorFrame.pack(fill=BOTH,expand=True)
    scrollbarY.config( command = editor.yview,highlightbackground="BLACK",highlightcolor="BLACk",bg='BLACK')



file_path=''

def set_file_path(path):
    global file_path
    file_path=path

def newFile(event):
    newTabs(tabs)

def openFile(event):
    path=askopenfilename(initialdir='C:',
    filetypes=[("All Files","*.*"),("Text Documents","*.txt"),("Python","*.py"),("C","*.c"),("C++","*.cpp"),("Hyper Text Markup Language","*.html")])
    with open(path,'r') as file:
        data=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',data)
        set_file_path(path)


def saveFile(event):
    if file_path=='':
        path=asksaveasfilename(initialfile="Untitled",defaultextension=".txt",
        filetypes=[("All Files","*.*"),("Text Documents","*.txt"),("Python","*.py"),("C","*.c"),("C++","*.cpp"),("Hyper Text Markup Language","*.html")])
    else:
        path=file_path
    with open(path,'w') as file:
        data=editor.get('1.0',END)
        file.write(data)
        set_file_path(path)
        

def savefileAs(event):
    path=asksaveasfilename(initialfile="Untitled",defaultextension=".txt",
    filetypes=[("All Files","*.*"),("Text Documents","*.txt"),("Python","*.py"),("C","*.c"),("C++","*.cpp"),("Hyper Text Markup Language","*.html")])
    with open(path,'w') as file:
        data=editor.get('1.0',END)
        file.write(data)
        set_file_path(path)


window.bind("<Control-s>",saveFile)
window.bind("<Control-S>",saveFile)
window.bind("<Control-Shift-S>",savefileAs)
window.bind("<Control-o>",openFile)
window.bind("<Control-n>",lambda x:newFile(tabs))
window.bind("<Control-q>",lambda x:window.destroy())

menuFrame=Frame(window)
menu_bar = Menu(menuFrame)
menu_bar.config(bg='#2a2a2f',fg='WHITE',activeborderwidth=0,bd=0)

fileBar=Menu(menu_bar,tearoff=0,borderwidth=0,bg='#2a2a2f')
fileBar.config(bg='#2a2a2f',fg='WHITE')
fileBar.add_command(label="New",command=lambda:newFile(tabs))
fileBar.add_command(label="Open",command=openFile)
#fileBar.add_command(label="Close",command="")
fileBar.add_command(label="Save",command=saveFile)
fileBar.add_command(label="Save As",command=savefileAs)
#fileBar.add_command(label="Rename",command="")
fileBar.add_command(label="Exit",command=window.destroy)
menu_bar.add_cascade(label="File",menu=fileBar)


toolBar=Menu(window)

newTabs(tabs)
window.config(menu=menu_bar)

#scrollbarX.config( command = editor.xview,orient=HORIZONTAL)



window.mainloop()
