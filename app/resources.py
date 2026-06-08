from collections import Counter
import uuid
from datetime import datetime
from app.storage import load_resources, save_resources
from tkinter import dialog, filedialog
from pathlib import Path
import shutil
import os
import tkinter as tk
from tkinter import ttk
from app.functions import refresh_treeview

FILE_STORAGE_PATH =Path("files")

def add_resources(tree):
    file_path=filedialog.askopenfilename(title="请选择文件！")
    src_path=Path(file_path)
    destination=filedialog.askdirectory(title="请选择文件转存地址！",initialdir=str(FILE_STORAGE_PATH))
    des_path=Path(destination)
    
    subject=src_path.name
    parent=src_path.parent
    suffix=src_path.suffix
    stem=src_path.stem

    index=1

    try:
        shutil.copy2(src_path,des_path)

    except Exception as e:
        tk.messagebox.showerror(title="添加失败",message=f"无法添加文件！\n错误信息：{e}")

    file_id=str(uuid.uuid4())
    
    p={
        'id':file_id,
        'subject':subject,
        ##'tags':tags,
        'title':src_path.stem,
        'original_name':src_path.name,
        'original_path':str(src_path),
        'create_time':datetime.now().isoformat(timespec="seconds"),
        "updated_at": datetime.now().isoformat(timespec="seconds")
        }


    resources=load_resources()
    resources.append(p)
    save_resources(resources)
    refresh_treeview(tree)
    print("资料添加成功！")


def select_resources():
    items=['name','subject','path','tag']
    tep=input("请确定检索对象(name/subject/path/tag)：")
    chosen_name=input("请输入对象名字：")
    for item in items:
        if tep==item:
            resources=load_resources()
            for resource in resources:
                if chosen_name in resource[item]:
                    print(resource)
            break

##删除资源，删除后会在数据库中删除对应项，并且删除文件
def delete_resources(tree):
    file_path=filedialog.askopenfilename(title="请选择删除的文件！",initialdir=str(FILE_STORAGE_PATH))
    src_path=Path(file_path)
    tep=src_path.stem
    ##跳出确认框
    if src_path.exists():
        confirm=tk.messagebox.askyesno(title="确认删除",message=f"你确定要删除{src_path.name}吗？")
        if not confirm:
            return
        elif confirm:
            print("正在删除文件...")
            ##遍历数据库，在数据库中删除对应项
            resources=load_resources()
            for resource in resources:
                if resource['title']==tep:
                    resources.remove(resource)
                    print("该文件已删除！")
            ##删除文件
            try:
                os.unlink(src_path)
            except PermissionError as e:
                tk.messagebox.showerror(title="删除失败",message=f"无法删除文件！请检查文件是否被占用或权限设置！\n错误信息：{e}")  
    save_resources(resources)
    refresh_treeview(tree) 
    


def print_all_resources(tree):
    resources=load_resources()
    for resource in resources:
        tree.insert("", tk.END, values=(resource["title"], resource["subject"], resource["original_path"]))

def select_from_tags():
    resources=load_resources()
    chosen_tags=input("请输入你想查询的标签（有多个请用英文逗号隔开）;")
    flag=0
    for resource in resources:
        if chosen_tags in resource['tag']:
            print(f"{resource}\n")
            flag=1
    if flag==1:
        print("已找到对应资料")
    elif flag==0:
        print("未找到对应资料")


def count_items():
    resources=load_resources()
    subject_count=Counter()
    tags_count=Counter()
    for resource in resources:
        subject=resource["subject"]
        tags=resource["tag"]

        subject_count[subject]+=1
        for tag in tags:
            tags_count[tag]+=1

    print("\n科目统计：")
    for subject,count in subject_count.items():
        print(f"{subject}:{count}")

    print("\n标签统计：")
    for tag,count in tags_count.items():
        print(f"{tag}:{count}")
    print(f"\n科目总数：{len(subject_count)}")
    print(f"\n标签总数：{len(tags_count)}")


def sort_resources():
    resources=load_resources()
    for resource in resources:
        resource["subject"]=resource["subject"].strip()
        resource["name"]=resource["name"].strip()
    
        tags=resource["tag"]
        tags=[t.strip() for t in tags if t.strip()]
        tags=sorted(set(tags))
        resource["tag"]=tags

    resources.sort(
        key=lambda resource:(
                   resource["subject"],
                   resource["tag"][0] if resource["tag"] else "",
                   resource["name"])
                   )
    save_resources(resources)

    print("自动整理已完成！")
