import os
from sys import platform
import shutil


def help():
    print()
    print("fol \'название папки\' - Создать папку")
    print("delfol \'название папки\' - Удалить папку")
    print("go\goback(без параметров) 'путь' - Перемещение в директории")
    print("file \'название файла\' - Создать файл")
    print("text \'название файла\' \'Ваш текст\' - Записать текст в файл")
    print("opfile \'название файла\' - Просмотреть содержимое файла")
    print("delfile \'название файла\' - Удалить файл")
    print("copy \'путь файла1\' \'путь файла2\' - Копировать файл")
    print("mov \'путь от\' \'путь до\'- Переместить файл")
    print("rename \'название файла\' - Переименовать файл")
    print("set - Открыть настройки")
    print("q! - для выхода из программы")


def Syssep():
    sep = ""
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        sep = "/"
    elif platform == "win32" or platform == "win64":
        sep = "\\"
    else:
        print("Не могу определить систему")
    return sep


def check_dir(your_fol):
    try:
        f = open("file_settings.txt", "r")
    except IOError:
        f = open("file_settings.txt", "x")
        create_folder("main_folder")

    f = open('file_settings.txt', 'w')
    f.writelines(f"directory = {your_fol}{Syssep()}main_folder")
    f.close()
    return True


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print("Папка уже существует")


def delfol(folder_name):
    try:
        shutil.rmtree(folder_name)
    except Exception:
        print("Возникла ошибка")


def go(dir=None):
    try:
        if dir:
            os.chdir(os.getcwd() + Syssep() + dir)
        else:
            if os.getcwd() != main_directory:
                os.chdir(os.pardir)
            else:
                print("Нет доступа")
    except OSError:
        print("Указан неправильный путь")


def file(file_name):
    open(file_name, "x")


def write_text(file_name, text):
    f = open(file_name, "w")
    f.write(text)


def openfile(file_name):
    try:
        f = open(file_name, "r")
        print(*f)
    except FileNotFoundError:
        print("Файл не существует")


def deletefile(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("Файл не существует")


def copy(way1, way2):
    try:
        shutil.copy(os.getcwd() + Syssep() + way1, main_directory + Syssep() + way2)
    except Exception:
        print("Возникла ошибка")


def move(way1, way2):
    try:
        shutil.move(os.getcwd() + Syssep() + way1, main_directory + Syssep() + way2)
    except Exception:
        print("Возникла ошибка")


def rename(name, new_name):
    os.rename(name, new_name)


def main():
    commands = ["fol", "delfol", "go", "goback", "file", "text", "opfile", "delfile", "copy", "mov", "rename", "set", "q!",
                "help"]
    go("main_folder")
    inp = ""
    while inp != "q!":
        try:
            inp = input(f"{os.getcwd()} > ").split()

            if inp[0].lower() == "help":
                help()

            elif inp[0].lower() == "fol":
                if len(inp) == 2:
                    create_folder(inp[1])
                else: print("Вы ввели не все параметры")

            elif inp[0].lower() == "delfol":
                if len(inp) == 2:
                    delfol(inp[1])
                else: print("Вы ввели не все параметры")

            elif inp[0].lower() == "go":
                if len(inp) == 2:
                    go(inp[1])
                else: print("Вы ввели не все параметры")

            elif inp[0].lower() == "goback":
                go()

            elif inp[0].lower() == "file":
                if len(inp) == 2:
                    file(inp[1])
                else: print("Вы ввели не все параметры")

            elif inp[0].lower() == "text":
                if len(inp) == 3:
                    write_text(inp[1], inp[2])
                else: print("Вы ввели не все параметры")

            elif inp[0].lower() == "opfile":
                if len(inp) == 2:
                    openfile(inp[1])
                else:
                    print("Вы ввели не все параметры")

            elif inp[0].lower() == "delfile":
                if len(inp) == 2:
                    deletefile(inp[1])
                else:
                    print("Вы ввели не все параметры")

            elif inp[0].lower() == "copy":
                if len(inp) == 3:
                    copy(inp[1], inp[2])
                else:
                    print("Вы ввели не все параметры")

            elif inp[0].lower() == "mov":
                if len(inp) == 3:
                    move(inp[1], inp[2])
                else:
                    print("Вы ввели не все параметры")

            elif inp[0].lower() == "rename":
                if len(inp) == 3:
                    rename(inp[1], inp[2])
                else:
                    print("Вы ввели не все параметры")

            elif inp[0].lower() == "set":
                print(f"Ваша рабочая папка: {main_directory}")


            elif inp[0].lower() == "q!":
                print("Конец работы")
                break
            else:
                print("Данной команды не существует, введите help, чтобы посмотерть список команд")
        except Exception:
            print("Для просмотра команд напишите - help")



if __name__ == '__main__':
    check_dir(os.getcwd())
    f = open("file_settings.txt", "r")
    main_directory = "".join(f.readline().split()[2:])
    main()
