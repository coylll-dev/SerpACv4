import os
from pathlib import Path
import webbrowser
import pathlib
import time
import keyboard


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[36m'
    BLUE = '\033[35m'
    RED = '\033[32m'
    WHITE = '\033[31m'


list_file = []
path = 'C:\\'
disks = os.listdrives()
count_disks = len(disks)

fordelete = []

Roaming = Path(os.environ["USERPROFILE"]) / "AppData\\Roaming"
Roaming = os.path.realpath(Roaming)

Disk_C = "C:\\"
Disk_C = os.path.realpath(Disk_C)

Local = Path(os.environ["USERPROFILE"]) / "AppData\\Local"
Local = os.path.realpath(Local)

Temp = "C:\\Windows\\Temp"
Temp = os.path.realpath(Temp)

Prefetch = "C:\\Windows\\Prefetch"
Prefetch = os.path.realpath(Prefetch)

RecycleBin = "C:\\$Recycle.Bin"
RecycleBin = os.path.realpath(RecycleBin)

ProgramFiles = "C:\\Program Files"
ProgramFiles = os.path.realpath(ProgramFiles)

ProgramFilesX86 = "C:\\Program Files (x86)"
ProgramFilesX86 = os.path.realpath(ProgramFilesX86)

Downloads = Path(os.environ["USERPROFILE"]) / "Downloads"
Downloads = os.path.realpath(Downloads)

keywords = [
			"INTERIUM",
            "XONE",
            "xone",
            "Luno",
            "ExLoader",
            ".cfg",
            "Enigma",
            "En1gma",
            "naim",
            "AimStar",
            "Aimmy",
            "plague",
            "TKazer",
            "Ekkond",
            "Osiris",
            "Victoria",
            "W1nner",
            "NeverLose",
            ".ahk",
            "ExtrimHack",
            "MultiHack",
            "Nexusoftware",
            "skinchanger",
            "MaxHack",
            "ezHack",
            "Valthrun",
            "Aimware",
            "Aimware",
            "Asphyxia",
            "IMXNOOBX",
            "Orbit",
            "Primordial",
            "SDK2Changer",
            "Sensum",
            "Warware",
            "VRedux",
            "memesense",
            "gamesense",
            "fatality",
            "skeet",
            "cheat",
            # "чит",
            "neverlose",
            "CS2Test",
            "onetap",
            "Mason",
            "Fecurity",
            "Softhub",
            "WinX",
            "NixWare",
            "Predator",
            "OneMacro",
            "AXIOS",
            "Pussycat",
            "Pellix",
            "Antropomeda",
            "S0ul",
            "1LT",
            "PornHub",
            "SYNCWARE",
            "Aquila",
            "Easywin",
            "Ampetamine",
            "Nova",
            "MillionWare",
            "Kernel",
            "Detorus",
            "VTA",
            "MaSoN",
            "MASON",
            "Spurdo",
            "ProExt",
            "VREDUX",
            "Hellhit",
            "0x666",
            "SAPH",
            "AM",
            "Advance",
            "Sapphire",
            "AQUILA",
            "InterWebz",
            "R8",
            "PROCHEAT",
            "BAUNTI",
            "RAZERCLUB",
            "LOR",
            "hvh",
            "HVH",
            "Midnight",
            "nl",
            "NL",
            ]


def tt(text, delay):
    for i in text:
        print(end=i)
        time.sleep(delay)		
	

def folders():
	os.startfile(Disk_C)
	os.startfile(Roaming)
	os.startfile(Local)
	os.startfile(Prefetch)
	os.startfile(Temp)
	os.startfile(RecycleBin)
	os.startfile(ProgramFiles)
	os.startfile(ProgramFilesX86)
	os.startfile(Downloads)


#Открывает сайты читов
def history():
	print(bcolors.RED, "\nОткрытие сайтов...", bcolors.ENDC)
	print(bcolors.OKCYAN, "\nPress *enter* for continue", bcolors.ENDC)
	webbrowser.open('https://midnight.im/', new=2)
	webbrowser.open('https://xone.fun/', new=2)
	webbrowser.open('https://neverlose.cc/', new=2)
	webbrowser.open('https://en1gma.tech/', new=2)
	webbrowser.open('https://m.youtube.com/', new=2)
	#Открытие истории
	time.sleep(1)
	keyboard.press_and_release('Ctrl+H')


def search_files(keywords):
    for root, dirs, files in os.walk(path):
        for file in files:
            for keyword in keywords:
                if keyword in file:
                    print(bcolors.OKCYAN, f"\n❆Найден файл❆: {file}\n", bcolors.OKGREEN)
                    file_path = os.path.join(root, file)
                    print("   File directory :", file_path, "\n")
                    file_size = os.path.getsize(file_path)
                    print(bcolors.OKBLUE, "  File Size is :", file_size, "bytes\n")

                    try:
                        p_file = pathlib.Path(file)
                        file_time = p_file.stat().st_mtime
                        print("Last update files : ", file_time)
                    except FileNotFoundError:
                        print(bcolors.PURPLE, "Невозможно прочитать файл, что-бы узнать его дату изменения")
                        pass

                    print("\n▶--------------------------------------◀")


def search_directory(keyword):
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            for keyword in keywords:
                if keyword in directory:
                    print(bcolors.WARNING, f"\n☁ Найдена папка☁ : {directory}\n", bcolors.OKGREEN)
                    directory_path = os.path.join(root, directory)
                    print("   Folder folder :", directory_path, "\n")
                    directory_size = os.path.getsize(directory_path)
                    print(bcolors.WHITE, "  Directory Size is :", directory_size, "bytes\n")

                    try:
                        p_directory = pathlib.Path(directory)
                        directory_time = p_directory.stat().st_mtime
                        print("Last update files : ", directory_time)
                    except FileNotFoundError:
                        print(bcolors.PURPLE, "Невозможно прочитать папку, что-бы узнать его дату изменения")
                        pass

                    print("\n▶--------------------------------------◀")


def itog():
    # Итог
    print(bcolors.BOLD, bcolors.WARNING, "\n\n\n\n\n\n\nПрийдётся немного подождать, идёт сканирование всех дисков...\n\nИТОГ:\n")
    global disk
    for disk in disks:
        search_directories(disk)


#Выборы действий
folders_say = "\n A - Открыть папки"
history_say = "B - Открыть сайты читов и историю"
find_say = "C - Начать проверку всех файлов на читы"
exit_say = "D - Выход (Нажимать после все действий)"

#Меню
def menu():
    proverka = True 
    while proverka:
        print(bcolors.PURPLE, "\nВыберите действие:\n\n")
        print(bcolors.PURPLE, folders_say)
        print(bcolors.PURPLE, history_say)
        print(bcolors.PURPLE, find_say)
        print(bcolors.PURPLE, exit_say)
        print(bcolors.PURPLE, "\nВсе варианты лучше вводить по очереди!")
        vibor = input("\nВведите вариант ответа английской раскладкой (Например: A)\n")
        if vibor == "A":
            folders()
        elif vibor == "B":
            history()
        elif vibor == "C":
            po_fanu()
        elif vibor == "D":
            proverka = False
        else:
            print("Такого выбора не существует...")


def search_directories(path):
    for root, dirs, files in os.walk(path):
        for keyword in keywords:
            file_path = os.path.join(root, keyword)
            if os.path.exists(file_path):
                print(bcolors.WARNING, f"\nНайден странный файл: {keyword}\n", f"\nFile directory: {file_path}")
                print("▶--------------------------------------◀\n")

        for keyword in keywords:
            directory_path = os.path.join(root, keyword)
            if os.path.exists(directory_path):
                print(bcolors.WARNING, f"\nНайдена странная папка: {keyword}\n", f"\nFolder directory: {directory_path}")
                print("▶--------------------------------------◀\n")

        if all(not os.path.exists(os.path.join(root, keyword)) for keyword in keywords):
            lol_1 =+ 1
        else:
            lol_2 =+ 1
            print("\n ▶--------------------------------------◀")
            print(bcolors.BOLD, bcolors.WARNING, f" На диске {disk} обнаружен подозрительный файл\папка, администратор обязан проверить его\ее путь: {root}", bcolors.ENDC)
            print(bcolors.WARNING, "▶--------------------------------------◀")


def po_fanu():
    # Проверяет диски на файлы похожие по названиям на читы
    for i in range(count_disks):
        disks_print = print(bcolors.OKGREEN, "Ваши диски: ", disks)
        disk_choice = input("Введите букву диска, на котором нужно выполнить поиск (например, C): ")
        disk_path = disk_choice + ":\\"
        global path
        path = disk_path
        print("\nПоиск папок и файлов...")
        print(bcolors.OKCYAN, "\nPress *enter* for continue", bcolors.ENDC)
        search_files(keywords)
        search_directory(keywords)


print(bcolors.PURPLE, "░██████╗███████╗██████╗░██████╗░░░░░█████╗░░█████╗░".encode("utf-8").decode("utf-8"))
time.sleep(0.3)
print(bcolors.PURPLE, "██╔════╝██╔════╝██╔══██╗██╔══██╗░░░██╔══██╗██╔══██╗".encode("utf-8").decode("utf-8"))
time.sleep(0.3)
print(bcolors.PURPLE, "╚█████╗░█████╗░░██████╔╝██████╔╝░░░███████║██║░░╚═╝".encode("utf-8").decode("utf-8"))
time.sleep(0.3)
print(bcolors.PURPLE, "░╚═══██╗██╔══╝░░██╔══██╗██╔═══╝░░░░██╔══██║██║░░██╗".encode("utf-8").decode("utf-8"))
time.sleep(0.3)
print(bcolors.PURPLE, "██████╔╝███████╗██║░░██║██║░░░░░██╗██║░░██║╚█████╔╝".encode("utf-8").decode("utf-8"))
time.sleep(0.3)
print(bcolors.PURPLE, "╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░".encode("utf-8").decode("utf-8"))
time.sleep(0.3)
print("               ✦ Program created by Soul")
time.sleep(0.3)
print("           ● Discord: coylll")
time.sleep(1)
print("\n   ☭ For server Aztec")
time.sleep(1)
tt("...", 0.5)


menu()  # Add colon
#Выход из цикла
itog()
