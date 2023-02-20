import requests
import shutil
import os

print("Minecraft Skin Grabber!\n------------------------\n")

mcusername = input('Enter the Username of the player: ')

res = requests.get("https://www.minotar.net/skin/"+mcusername, stream = True)

if res.status_code == 200:
    os.system("md GrabbedSkins")
    with open("GrabbedSkins/"+mcusername,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('\nSkin grabbed!\nCheck the "GrabbedSkins" folder.')
    os.system('cd GrabbedSkins && rename '+mcusername+' '+mcusername+".png")
else:
    print('\nSkin was unable to be grabbed.')

input()