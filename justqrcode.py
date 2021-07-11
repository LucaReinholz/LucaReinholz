#import
import qrcode
import sys
from termcolor import colored, cprint
import os, re 
import tempfile
import os.path

#input
name = input("Enter your the Name you want the file to get called, you don't need to tipe .jpg: ")
path = input("Where is the file supposed to be stored? ( type skip if you don't know any name! ): ")
link = input("Now just enter the Link and you're good 2 go :): ")
img = qrcode.make(link)
img.save(name + ".jpg")

#print
print("Here you go:")
print("---------------------------------------------------")
cprint("That's the name: " +  name + '.jpg', 'cyan')
print("")
def Path():
    if path == "skip":
        print(os.getcwd() + "\\" +  name)
    else:
        print(path, 'cyan')
Path()
print("")
cprint("Goodbye!", 'cyan')
print("")