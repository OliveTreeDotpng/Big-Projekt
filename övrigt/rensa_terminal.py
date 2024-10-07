import os
def rensa_terminalen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")