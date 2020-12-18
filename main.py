import  colorama
from  colorama import Fore , Back ,Style
colorama.init()
import solint

a1 = "  ____             _       _   _       _     _____                                            _    "
a2 = " / ___|  ___   ___(_) __ _| | (_)_ __ | |_  |  ____ __ __ _ _ __ ___   _____      _____  _ __| | __"
a3 = " \___ \ / _ \ / __| |/ _` | | | | '_ \| __| | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /"
a4 = "  ___) | (_) | (__| | (_| | | | | | | | |_  |  _|| | | (_| | | | | | |  __/\ V  V | (_) | |  |   < "
a5 = " |____/ \___/ \___|_|\__,_|_| |_|_| |_|\__| |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\ "

print(Fore.MAGENTA)
print(Back.LIGHTWHITE_EX)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print("Social Int Framework was created by                                 ")
print("The Framework use by default IG for scraping photos and Selenium for its automation ")
print("Please select the prefered option and press enter")
print(Fore.RED)
print("1) Use google and Yandex for scaning")
print("2) Use only google for scaning")
print("3) Use only Yandex for scaning")
print("4) Use all scraped data for generate a wordlist")
print("5) Download all photos from the target account ")
print("6) Input my own Image URL ")

choice = input("Select a option: ")

try:
    a = int(choice)
except:
    print("The select option its not valid")

solint.run_all()

