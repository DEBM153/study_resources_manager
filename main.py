from app.menu import show_menu
from app.resources import (
    add_resources,
    count_items,
    delete_resources,
    print_all_resources,
    select_from_tags,
    select_resources,
    sort_resources,
)
import tkinter as tk
from tkinter import ttk
from app.functions import refresh_treeview, show_context_menu

def main():
    window = tk.Tk()
    window.title("学习资料管理系统")
    window.geometry("900x600")
    window.minsize(700, 480)

    ##设置主题和样式
    style = ttk.Style()
    try:
        style.theme_use('clam')
    except Exception:
        pass
    style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
    style.configure("Treeview", font=("Segoe UI", 10), rowheight=26)
    style.configure("TButton", font=("Segoe UI", 10), padding=6)

    ##创建板块功能栏和表格栏
    frame_a = ttk.Frame(window, padding=(12, 10))
    frame_b = ttk.Frame(window, padding=(12, 6, 12, 12))
    frame_a.pack(side=tk.TOP, fill=tk.X)
    frame_b.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    ##创建表格视图
    tree = ttk.Treeview(
        columns=("title", "subject", "path"),
        master=frame_b,
        show='headings',
        selectmode=tk.BROWSE
    )

    ##创建右键菜单
    menu=tk.Menu(tree, tearoff=0)
    menu.add_command(label="删除", command=lambda: delete_resources(tree))##为右键菜单添加删除功能
    tree.bind("<Button-3>", lambda event: show_context_menu(event,tree,menu))##绑定右键点击事件，显示右键菜单

    ##设置表头
    tree.heading('title', text='标题', anchor=tk.CENTER)
    tree.heading('subject', text='学科', anchor=tk.CENTER)
    tree.heading('path', text='路径', anchor=tk.CENTER)

    ##设置列宽和对齐方式
    tree.column('title', width=320, anchor=tk.W)
    tree.column('subject', width=120, anchor=tk.CENTER)
    tree.column('path', width=420, anchor=tk.W)

    ##添加垂直滚动条
    scrollbar = ttk.Scrollbar(frame_b, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(6, 0))
    tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
    
    ##加载资源数据到表格
    print_all_resources(tree)
    
    ##工具栏按钮
    btn_add_resource = ttk.Button(frame_a, text='添加资料', command=lambda: add_resources(tree))
    btn_delete_resource = ttk.Button(frame_a, text='删除资料', command=lambda: delete_resources(tree))

    for btn in (btn_add_resource, btn_delete_resource):
        btn.pack(side=tk.LEFT, padx=8, pady=4)

    window.mainloop()


if __name__=="__main__":
    main()
