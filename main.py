from app.menu import show_menu
from app.resources import (
    add_resources,
    count_items,
    delete_resources,
    print_all_reources,
    select_from_tags,
    select_resources,
    sort_resources,
)


def main():
    while True:
        show_menu()
        choice = input("请选择任意一项操作（输入对应数字）: ")
        if choice == "1":
            add_resources()

        if choice=="2":
            select_resources()
            
        if choice=="3":
            print_all_reources()

        if choice=="4":
            select_from_tags()
        
        if choice=="5":
            sort_resources()

        if choice=="6":
            count_items()

        if choice=='7':
            delete_resources()

        if choice == "8":
            print("已退出程序！！！欢迎下次光临")
            break


if __name__=="__main__":
    main()
