from pathlib import Path

def show_menu():
    print("菜单：")
    path = Path("data\\functions_menus.txt")   
    functions = path.read_text(encoding="utf-8").rstrip().splitlines()
    for function in functions:
        print(function)

def main():
    while True:
        show_menu()
        choice = input("请选择任意一项操作（输入对应数字）: ")
        if choice == "8":
            print("退出程序")
            break

main()