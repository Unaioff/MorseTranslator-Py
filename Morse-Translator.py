import os
from colorama import init, Fore, Style
from time import sleep
import pyperclip as pc

# ALFABETO MORSE [A-Z] [0-9] [@ ? ¿ ! ¡]
AlfabetoMorse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "ñ": "--.--",
    "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
    "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "@": ".--.-.", "?": "..--..", "¿": "..-.-",
    "!": "-.-.--", " ": " / "
}

# CONFIGURACIÓN
slowmoprint = False
autocopy = True

# FUNCIÓN LIMPIADORA XD
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print(Fore.LIGHTCYAN_EX + Style.NORMAL + "    ___  ___                      _____                   _       _             ")
    print(Fore.CYAN + Style.NORMAL +         "    |  \/  |                     |_   _|                 | |     | |            ")
    print(Fore.LIGHTBLUE_EX + Style.NORMAL + "    | |\/| |/ _ \| '__/ __|/ _ \   | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|")
    print(Fore.BLUE + Style.NORMAL +         "    | |  | | (_) | |  \__ \  __/   | | | | (_| | | | \__ \ | (_| | || (_) | |   ")
    print(Fore.BLUE + Style.NORMAL +         "    \_|  |_/\___/|_|  |___/\___|   \_/_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   ")
    print("")

# PUES PARA INICIAR, QUE ACASO NO SABES INGLÉS?
def start():
    play(input(Fore.BLUE + Style.BRIGHT + "=====[ " + Fore.WHITE + Style.RESET_ALL).lower())
    


# AQUI VA LA TRADUCCIÓN EL RESTO ES JUST FANCY
def play(Frase):
    respuesta = []
    for letra in Frase:
        if letra in AlfabetoMorse:
            respuesta.append(AlfabetoMorse[letra])
    morse_code = " ".join(respuesta)
    for i in range(len(morse_code)):
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + morse_code[:i+1], end='\r')
        if slowmoprint == True: sleep(0.05)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + morse_code)
    if autocopy == True: pc.copy(morse_code)
    start()

# MENU PRINCIPAL
def menu():
    clear()    
    print(Fore.BLUE + Style.BRIGHT + 
    """
    1) Start
    2) Settings
    3) Exit
    """)

    choice = input(">> ")

    if choice == "1": clear(), start()
    elif choice == "2": config()
    elif choice == "3": exit()
    else: menu()

# CONFIGURACIÓN, SLOWMOPRINT, AUTOCOPY...
def config():
    global slowmoprint, autocopy
    clear()
    print("")
    if slowmoprint == True: print(Fore.BLUE + Style.BRIGHT + "    1) SlowMoPrint           " + Fore.GREEN + Style.NORMAL + "[" + str(slowmoprint) +"]")
    else: print(Fore.BLUE + Style.BRIGHT + "    1) SlowMoPrint           " + Fore.RED+ Style.NORMAL + "[" + str(slowmoprint) +"]")
    if autocopy == True: print(Fore.BLUE + Style.BRIGHT + "    2) AutoCopy              " + Fore.GREEN + Style.NORMAL + "[" + str(autocopy) +"]")
    else: print(Fore.BLUE + Style.BRIGHT + "    2) AutoCopy              " + Fore.RED + Style.NORMAL + "[" + str(autocopy) +"]")
    print(Fore.BLUE + Style.BRIGHT + "    3) Exit ")
    print("")
    choice = input(">> ")
    if choice == "1":
        slowmoprint = not slowmoprint
        config()
    elif choice == "2": 
        autocopy = not autocopy
        config()
    elif choice == "3": menu()
    else: config()

menu()
