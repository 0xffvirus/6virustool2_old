def clear():
    from sys import platform
    from os import system
    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "darwin":
        system("clear")
    elif platform == "win32":
        system("cls")
