from pathlib import Path
import json
from collections import Counter

DATA_FILE = Path("data") / "resources.json"
def show_menu():
    print("菜单：")
    path = Path("data\\functions_menus.txt")   
    functions = path.read_text(encoding="utf-8").rstrip().splitlines()
    for function in functions:
        print(function)

def load_resources():
    try:
        contents = DATA_FILE.read_text(encoding="utf-8")
        resources = json.loads(contents)
        return resources
    except FileNotFoundError:
        return []

def save_resources(resources):
      DATA_FILE.parent.mkdir(exist_ok=True)

      content = json.dumps(resources, ensure_ascii=False, indent=4)
      DATA_FILE.write_text(content, encoding="utf-8")

def add_resources():
    name=input("请输入资料名称：")
    subject=input("请输入科目：")
    file_path=input("请输入路径：")
    tag = input("请输入标签，多个标签用英文逗号分隔：").split(",")

    p={
        'name':name,
        'subject':subject,
        'path':file_path,
        'tag':tag
        }

    resources=load_resources()
    resources.append(p)
    save_resources(resources)

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

def delete_resources():
    tep=input("请输入删除文件名字：")
    resources=load_resources()
    for resource in resources:
        if resource['name']==tep:
            flag=input(f"{resource}\n确认删除该文件吗（YES/NO）:")
            if flag=='YES':
                resources.remove(resource)
                print("该文件已删除！")
            elif flag=='NO':
                print("未删除该文件")
                continue
    save_resources(resources)

def print_all_reources():
    resources=load_resources()
    if resources!=[]:
        for index,resource in enumerate(resources,start=1):
            print(f"{index}.{resource}\n")
    else:
        print("目前没有资料存入")

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