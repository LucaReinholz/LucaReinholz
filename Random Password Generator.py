import random

chars = "adcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@;+-[]{}%&"

while 1: 
    password_len = int(input("Wie lang soll das Passwort sein?"))
    password_count = int(input("Wie viele Passwörter brauchst du?"))
    for x in range(0, password_count):
        password = ""
        for x in range(0,password_len):
            #char =  character
            password_char = random.choice(chars)
            password      = password + password_char 
        print("Hier ist dein Passwort : ", password)










