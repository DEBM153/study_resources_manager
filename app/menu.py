from pathlib import Path


def show_menu():
    print("菜单：")
    path = Path("data\\functions_menus.txt")   
    functions = path.read_text(encoding="utf-8").rstrip().splitlines()
    for function in functions:
        print(function)
