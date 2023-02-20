from tkinter import *
import requests
import shutil
import os

root = Tk()

root.configure(bg="#eeeeee")
root.title("Python Minecraft Skin Grabber")
root.geometry("200x100")
root.resizable(False, False)

Label(root, text="Minecraft Username").pack()
mcusernamebox = Entry(root, width=30)
mcusernamebox.pack()

def mcusernamegetbox():
    mcusername = mcusernamebox.get()
    res = requests.get("https://www.minotar.net/skin/"+str(mcusername), stream = True)

    if res.status_code == 200:
        os.system("md GrabbedSkins")
        with open("GrabbedSkins/"+str(mcusername),'wb') as f:
            shutil.copyfileobj(res.raw, f)
        os.system('cd GrabbedSkins && rename '+str(mcusername)+' '+str(mcusername)+".png")
        Label(root, text="Grabbed skin!\nCheck the GrabbedSkins folder!").pack()
    else:
        Label(root, text="Unable to grab skin!\nCheck your internet connection.").pack()

downloadbutton = Button(root, text="Download Skin", command=mcusernamegetbox)
downloadbutton.pack()

root.mainloop()

input()