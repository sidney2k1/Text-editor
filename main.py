from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("Text editor")
window.geometry("400x300")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
def openfile():
    filepath=askopenfilename(filetype=[("Text files","*.txt"),("All files","*.*")])
    if not filepath:
        return 
    txt_edit.delete(1.0,END)
    with open(filepath,"r") as inputfile:
        text=inputfile.read()
        txt_edit.insert(END,text)
        inputfile.close()
    window.title(f"Codingals text editor-{filepath}")
def savefile():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt"),("All files","*.*")])
    if not filepath:
        return
    with open(filepath,"w") as outputfiles:
        text=txt_edit.get(1.0,END)
        outputfiles.write(text)
        window.title(f"Codingal text editor-{filepath}")
txt_edit=Text(window)
frbuttons=Frame(window,relief=RAISED,bd=2)
btnopen=Button(frbuttons,text="Open",command=openfile)
btnsave=Button(frbuttons,text="Save as",command=savefile)
btnopen.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btnsave.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
frbuttons.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()