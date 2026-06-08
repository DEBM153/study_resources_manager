下面我把 `ttk.Treeview` 按 **StudyVault v2 资料表格** 来系统讲一遍。

你可以把 Treeview 理解成：

> Tkinter 里的“表格控件”，用来显示多行、多列数据。

在 StudyVault v2 里，它最适合显示：

```text
标题        科目      类型      大小      创建时间
高数笔记    数学      .pdf     2MB      2026-06-03
英语作文    英语      .docx    500KB    2026-06-03
Python项目  编程      .zip     10MB     2026-06-03
```

------

# 一、Treeview 解决什么问题？

普通 `Label` 只能显示一段文字：

```python
tk.Label(window, text="高数笔记")
```

但你的 StudyVault v2 要显示很多资料，每个资料又有很多字段：

```python
{
    "id": "abc123",
    "title": "高数笔记",
    "subject": "数学",
    "file_type": ".pdf",
    "file_size": 204800,
    "create_time": "2026-06-03T10:30:00"
}
```

这种数据就应该用 `Treeview` 显示成表格。

------

# 二、最小 Treeview 示例

```python
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Treeview 入门")
window.geometry("800x400")

columns = ("title", "subject", "file_type")

tree = ttk.Treeview(
    window,
    columns=columns,
    show="headings"
)

tree.heading("title", text="标题")
tree.heading("subject", text="科目")
tree.heading("file_type", text="文件类型")

tree.column("title", width=200)
tree.column("subject", width=100)
tree.column("file_type", width=100)

tree.insert("", "end", values=("高数笔记", "数学", ".pdf"))
tree.insert("", "end", values=("英语作文", "英语", ".docx"))

tree.pack(fill="both", expand=True)

window.mainloop()
```

------

# 三、创建 Treeview：参数详解

核心代码是：

```python
tree = ttk.Treeview(
    window,
    columns=columns,
    show="headings"
)
```

## 1. `ttk.Treeview(...)`

表示创建一个 Treeview 表格控件。

------

## 2. `window`

```python
ttk.Treeview(window, ...)
```

这里的 `window` 是父容器。

意思是：

> 这个表格放在 `window` 这个窗口里面。

以后你也可以放到某个区域里，比如：

```python
main_frame = tk.Frame(window)
tree = ttk.Treeview(main_frame, ...)
```

这样结构会更清楚。

------

## 3. `columns=columns`

```python
columns = ("title", "subject", "file_type")
```

这里定义表格有哪些列。

注意，这里的 `"title"`、`"subject"`、`"file_type"` 是程序内部使用的列名，不一定是用户看到的文字。

用户看到的表头文字要用：

```python
tree.heading("title", text="标题")
```

设置。

------

## 4. `show="headings"`

```python
show="headings"
```

表示只显示表头和数据列。

Treeview 默认有一个特殊列，叫：

```python
"#0"
```

这个列原本是给“树形结构”用的，比如文件夹树：

```text
资料库
├── 数学
│   └── 高数笔记.pdf
└── 英语
    └── 作文模板.docx
```

但你现在主要做的是表格，所以通常写：

```python
show="headings"
```

这样会隐藏默认的 `#0` 列。

常见写法有：

```python
show="headings"
```

只显示普通表格，StudyVault v2 最常用。

```python
show="tree"
```

只显示树形列 `#0`。

```python
show="tree headings"
```

既显示树形列，也显示表格列。

------

# 四、设置表头：`heading()`

代码：

```python
tree.heading("title", text="标题")
```

完整理解：

```python
tree.heading(column, text="显示文字", anchor="对齐方式", command=点击表头时执行的函数)
```

## 1. `column`

```python
"title"
```

表示你要设置哪一列的表头。

必须是 `columns` 里面定义过的名字。

------

## 2. `text`

```python
text="标题"
```

表示用户在界面上看到的表头文字。

比如：

```python
tree.heading("subject", text="科目")
```

程序列名是 `"subject"`，界面显示 `"科目"`。

------

## 3. `anchor`

表示表头文字的对齐方式。

```python
tree.heading("title", text="标题", anchor="w")
```

常见值：

```text
"w"      左对齐，west
"center" 居中
"e"      右对齐，east
```

例子：

```python
tree.heading("title", text="标题", anchor="w")
tree.heading("file_size", text="大小", anchor="e")
```

------

## 4. `command`

点击表头时执行某个函数，常用于排序。

```python
tree.heading("title", text="标题", command=sort_by_title)
```

意思是：

> 用户点击“标题”这个表头时，执行 `sort_by_title()`。

------

# 五、设置列宽：`column()`

代码：

```python
tree.column("title", width=200)
```

完整理解：

```python
tree.column(column, width=宽度, minwidth=最小宽度, stretch=是否拉伸, anchor=内容对齐方式)
```

## 1. `column`

表示设置哪一列。

```python
tree.column("title", ...)
```

------

## 2. `width`

设置列宽，单位大致是像素。

```python
tree.column("title", width=200)
```

------

## 3. `minwidth`

设置最小宽度。

```python
tree.column("title", width=200, minwidth=100)
```

意思是：

> 这一列正常宽度 200，但用户拖动时最小不能小于 100。

------

## 4. `stretch`

表示窗口变大时，这一列是否跟着拉伸。

```python
tree.column("title", width=200, stretch=True)
tree.column("file_type", width=80, stretch=False)
```

在 StudyVault v2 里：

```text
标题、原文件名、备注：可以 stretch=True
文件类型、收藏状态、大小：可以 stretch=False
```

------

## 5. `anchor`

设置这一列内容的对齐方式。

```python
tree.column("title", anchor="w")
tree.column("file_size", anchor="e")
```

常用：

```text
"w"      左对齐
"center" 居中
"e"      右对齐
```

------

# 六、插入数据：`insert()`

这是 Treeview 最重要的方法之一。

```python
tree.insert("", "end", values=("高数笔记", "数学", ".pdf"))
```

完整形式：

```python
tree.insert(parent, index, iid=None, text="", values=(), tags=())
```

------

## 1. `parent`

```python
""
```

表示插入到根节点下面。

如果你只是做普通表格，通常写空字符串：

```python
tree.insert("", "end", values=(...))
```

如果你做树形结构，`parent` 可以是某个父节点的 ID。

------

## 2. `index`

```python
"end"
```

表示插入到最后。

也可以写数字：

```python
tree.insert("", 0, values=(...))
```

表示插入到第一行。

常用：

```python
"end"
```

------

## 3. `iid`

`iid` 是这一行在 Treeview 里的唯一 ID。

默认情况下，Treeview 会自动生成类似：

```text
I001
I002
I003
```

但在 StudyVault v2 里，我强烈建议你自己指定：

```python
tree.insert(
    "",
    "end",
    iid=resource["id"],
    values=(resource["title"], resource["subject"])
)
```

因为你的 JSON 里本来就有：

```python
"id": "abc123"
```

这样 Treeview 的行 ID 就和资料 ID 对应起来了。

以后删除、打开、修改资料时会很方便。

注意：`iid` 不能重复。如果重复，会报错。

------

## 4. `text`

`text` 是给默认树形列 `#0` 用的。

如果你用了：

```python
show="headings"
```

那么 `text` 基本用不上。

树形结构时才常用：

```python
tree.insert("", "end", text="数学")
```

------

## 5. `values`

这是表格真正显示的数据。

```python
values=("高数笔记", "数学", ".pdf")
```

顺序必须和你的 `columns` 对应。

比如：

```python
columns = ("title", "subject", "file_type")
```

那么：

```python
values=("高数笔记", "数学", ".pdf")
```

对应关系是：

```text
title      高数笔记
subject    数学
file_type  .pdf
```

------

## 6. `tags`

给某一行加标签，用来设置样式或分类。

```python
tree.insert(
    "",
    "end",
    values=("高数笔记", "数学", ".pdf"),
    tags=("favorite",)
)
```

然后可以设置标签样式：

```python
tree.tag_configure("favorite", background="#FFF2CC")
```

在 StudyVault v2 中，可以用来标记收藏资料：

```python
if resource.get("favorite"):
    tags = ("favorite",)
else:
    tags = ()

tree.insert("", "end", values=(...), tags=tags)
```

------

# 七、把 JSON 资料显示到 Treeview

假设你的资料数据是：

```python
resources = [
    {
        "id": "001",
        "title": "高数笔记",
        "subject": "数学",
        "file_type": ".pdf",
        "create_time": "2026-06-03T10:30:00"
    },
    {
        "id": "002",
        "title": "英语作文",
        "subject": "英语",
        "file_type": ".docx",
        "create_time": "2026-06-03T11:00:00"
    }
]
```

可以这样显示：

```python
def show_resources(resources):
    for resource in resources:
        tree.insert(
            "",
            "end",
            iid=resource["id"],
            values=(
                resource.get("title", ""),
                resource.get("subject", ""),
                resource.get("file_type", ""),
                resource.get("create_time", "")
            )
        )
```

这里用到了：

```python
resource.get("title", "")
```

而不是：

```python
resource["title"]
```

原因是：

> 如果某个旧数据没有 `title` 字段，`.get()` 不会报错，而是返回空字符串。

这对你的 StudyVault v2 旧数据兼容很有用。

------

# 八、清空表格

搜索、刷新、重新加载数据时，经常要先清空 Treeview。

写法一：

```python
for item in tree.get_children():
    tree.delete(item)
```

写法二：

```python
tree.delete(*tree.get_children())
```

初学阶段建议先用写法一，更容易理解。

------

## `get_children()` 参数解释

```python
tree.get_children()
```

返回根节点下面所有行的 ID。

如果是普通表格，它返回所有行。

```python
tree.get_children(item)
```

返回某个父节点下面的子节点。

在普通表格里，你通常用：

```python
tree.get_children()
```

------

## `delete()` 参数解释

```python
tree.delete(item)
```

删除某一行。

```python
tree.delete(item1, item2, item3)
```

可以一次删除多行。

注意：这里只是删除 Treeview 界面上的一行，不会自动删除 JSON 数据，也不会删除真实文件。

对 StudyVault v2 来说，真正删除资料时应该分三步：

```text
1. 从 Treeview 删除显示
2. 从 resources.json 删除记录
3. 可选：删除真实文件，但必须弹窗确认
```

------

# 九、刷新表格：最常用函数

这是你 StudyVault v2 里非常重要的函数。

```python
def refresh_tree(resources):
    for item in tree.get_children():
        tree.delete(item)

    for resource in resources:
        tree.insert(
            "",
            "end",
            iid=resource.get("id"),
            values=(
                resource.get("title", ""),
                resource.get("subject", ""),
                resource.get("original_name", ""),
                resource.get("file_type", ""),
                resource.get("create_time", "")
            )
        )
```

它做两件事：

```text
先清空旧表格
再插入新数据
```

搜索功能、显示全部、导入后刷新、删除后刷新，都会用到它。

------

# 十、完整 StudyVault Treeview 示例

下面这个例子比较像你的 StudyVault v2 主界面雏形。

```python
import tkinter as tk
from tkinter import ttk


resources = [
    {
        "id": "001",
        "title": "高数笔记",
        "subject": "数学",
        "original_name": "高数笔记.pdf",
        "file_type": ".pdf",
        "create_time": "2026-06-03T10:30:00",
        "favorite": True
    },
    {
        "id": "002",
        "title": "英语作文模板",
        "subject": "英语",
        "original_name": "作文模板.docx",
        "file_type": ".docx",
        "create_time": "2026-06-03T11:00:00",
        "favorite": False
    }
]


def refresh_tree(data):
    for item in tree.get_children():
        tree.delete(item)

    for resource in data:
        if resource.get("favorite"):
            tags = ("favorite",)
        else:
            tags = ()

        tree.insert(
            "",
            "end",
            iid=resource.get("id"),
            values=(
                resource.get("title", ""),
                resource.get("subject", ""),
                resource.get("original_name", ""),
                resource.get("file_type", ""),
                resource.get("create_time", "")
            ),
            tags=tags
        )


window = tk.Tk()
window.title("StudyVault v2 - Treeview 示例")
window.geometry("900x500")

columns = ("title", "subject", "original_name", "file_type", "create_time")

tree = ttk.Treeview(
    window,
    columns=columns,
    show="headings",
    selectmode="browse"
)

tree.heading("title", text="标题", anchor="w")
tree.heading("subject", text="科目", anchor="center")
tree.heading("original_name", text="原文件名", anchor="w")
tree.heading("file_type", text="类型", anchor="center")
tree.heading("create_time", text="创建时间", anchor="w")

tree.column("title", width=180, anchor="w")
tree.column("subject", width=100, anchor="center")
tree.column("original_name", width=220, anchor="w")
tree.column("file_type", width=80, anchor="center")
tree.column("create_time", width=180, anchor="w")

tree.tag_configure("favorite", background="#FFF2CC")

tree.pack(fill="both", expand=True, padx=10, pady=10)

refresh_tree(resources)

window.mainloop()
```

------

# 十一、`selectmode` 选择模式

创建 Treeview 时可以写：

```python
tree = ttk.Treeview(
    window,
    columns=columns,
    show="headings",
    selectmode="browse"
)
```

`selectmode` 表示用户可以怎样选择行。

常见值：

```text
"browse"    只能选择一行，StudyVault v2 最常用
"extended"  可以按 Ctrl / Shift 选择多行
"none"      不允许选择
```

StudyVault v2 初期建议用：

```python
selectmode="browse"
```

因为打开、重命名、删除资料时，一次处理一个资料最简单、安全。

------

# 十二、获取当前选中的行

常用写法：

```python
selected = tree.selection()
```

`selection()` 返回当前选中的行 ID，结果通常是一个元组。

比如：

```python
("001",)
```

所以要这样判断：

```python
def get_selected_resource_id():
    selected = tree.selection()

    if not selected:
        print("没有选择任何资料")
        return None

    resource_id = selected[0]
    return resource_id
```

在 StudyVault v2 中，如果你插入行时用了：

```python
iid=resource["id"]
```

那么：

```python
selected[0]
```

拿到的就是资料 ID。

------

# 十三、获取选中行的数据

方法一：通过 `item()` 获取整行数据。

```python
selected = tree.selection()

if selected:
    item_id = selected[0]
    values = tree.item(item_id, "values")
    print(values)
```

假设这一行是：

```text
高数笔记    数学    高数笔记.pdf    .pdf
```

那么 `values` 可能是：

```python
("高数笔记", "数学", "高数笔记.pdf", ".pdf", "2026-06-03T10:30:00")
```

------

## `item()` 参数解释

```python
tree.item(item_id)
```

获取这一行的完整信息，返回字典。

```python
tree.item(item_id, "values")
```

只获取这一行的 values。

```python
tree.item(item_id, values=(...))
```

修改这一行的 values。

------

# 十四、按钮操作：查看选中资料

```python
def show_selected():
    selected = tree.selection()

    if not selected:
        print("请先选择一条资料")
        return

    item_id = selected[0]
    values = tree.item(item_id, "values")

    print("资料 ID:", item_id)
    print("这一行的数据:", values)
```

配合按钮：

```python
button = tk.Button(window, text="查看选中资料", command=show_selected)
button.pack()
```

------

# 十五、删除选中行

只从 Treeview 删除：

```python
def delete_selected_from_tree():
    selected = tree.selection()

    if not selected:
        print("请先选择资料")
        return

    item_id = selected[0]
    tree.delete(item_id)
```

但注意：

> 这只删除界面上的行，不会删除 JSON，也不会删除真实文件。

真正 StudyVault v2 删除资料时，应该这样设计：

```python
from tkinter import messagebox

def delete_selected_resource():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("提示", "请先选择要删除的资料")
        return

    resource_id = selected[0]

    confirm = messagebox.askyesno(
        "确认删除",
        "确定要删除这条资料记录吗？"
    )

    if not confirm:
        return

    tree.delete(resource_id)

    # 后面还要：
    # 1. 从 resources.json 删除对应资料
    # 2. 询问是否删除真实文件
```

文件删除是危险操作，后面你做真实文件删除时，一定要加确认弹窗，最好先只删除 JSON 记录，不直接删除原文件。

------

# 十六、双击某一行

Treeview 可以绑定事件。

```python
tree.bind("<Double-1>", on_double_click)
```

意思是：

> 用户鼠标左键双击 Treeview 时，执行 `on_double_click()`。

完整例子：

```python
def on_double_click(event):
    selected = tree.selection()

    if not selected:
        return

    resource_id = selected[0]
    values = tree.item(resource_id, "values")

    print("双击了资料:", resource_id)
    print(values)


tree.bind("<Double-1>", on_double_click)
```

------

## `bind()` 参数解释

```python
tree.bind(event_name, function)
```

## 1. `event_name`

表示事件类型。

常用：

```text
"<Double-1>"     鼠标左键双击
"<Button-1>"     鼠标左键单击
"<Return>"       回车键
"<<TreeviewSelect>>"  选中行变化时触发
```

------

## 2. `function`

事件发生后执行的函数。

注意：事件绑定函数通常要接收一个参数：

```python
def on_double_click(event):
    ...
```

这个 `event` 里面有鼠标位置、键盘信息等。

------

# 十七、双击打开文件的思路

StudyVault v2 里，双击某行应该打开真实文件。

关键思路：

```text
双击 Treeview 行
        ↓
拿到 resource_id
        ↓
去 resources.json 里找到对应资料
        ↓
拿到 stored_path
        ↓
用 os.startfile 打开文件
```

Windows 上可以这样打开文件：

```python
import os
from pathlib import Path
from tkinter import messagebox


def open_file(path):
    file_path = Path(path)

    if not file_path.exists():
        messagebox.showerror("错误", "文件不存在")
        return

    os.startfile(str(file_path))
```

双击函数大概是：

```python
def on_double_click(event):
    selected = tree.selection()

    if not selected:
        return

    resource_id = selected[0]

    for resource in resources:
        if resource.get("id") == resource_id:
            open_file(resource.get("stored_path"))
            break
```

------

# 十八、修改某一行的数据

可以用：

```python
tree.item(item_id, values=new_values)
```

例子：

```python
def rename_selected_title():
    selected = tree.selection()

    if not selected:
        return

    item_id = selected[0]
    old_values = tree.item(item_id, "values")

    new_values = (
        "新标题",
        old_values[1],
        old_values[2],
        old_values[3],
        old_values[4]
    )

    tree.item(item_id, values=new_values)
```

不过在 StudyVault v2 里，修改资料不要只改 Treeview。

正确流程应该是：

```text
修改 JSON 数据
保存 JSON
刷新 Treeview
```

也就是说：

```python
resource["title"] = "新标题"
save_resources(resources)
refresh_tree(resources)
```

Treeview 只是显示层，不应该当作真正的数据存储。

------

# 十九、用 `set()` 读取或修改某个单元格

Treeview 还可以用 `set()` 操作某一列。

读取：

```python
title = tree.set(item_id, "title")
```

修改：

```python
tree.set(item_id, "title", "新标题")
```

## `set()` 参数解释

```python
tree.set(item, column=None, value=None)
```

## 1. `item`

行 ID。

## 2. `column`

列名。

## 3. `value`

新值。

如果不传 `value`，表示读取。

如果传了 `value`，表示修改。

例子：

```python
tree.set("001", "title")
```

读取 ID 为 `"001"` 的行的标题。

```python
tree.set("001", "title", "线性代数笔记")
```

把这一行的标题改成 `"线性代数笔记"`。

------

# 二十、搜索后刷新 Treeview

搜索的本质是：

```text
从 resources 里筛选出结果
然后 refresh_tree(results)
```

例子：

```python
def search_resources(keyword):
    keyword = keyword.strip().lower()

    if not keyword:
        return resources

    results = []

    for resource in resources:
        text = " ".join([
            resource.get("title", ""),
            resource.get("subject", ""),
            resource.get("original_name", ""),
            resource.get("file_type", ""),
            resource.get("note", "")
        ]).lower()

        if keyword in text:
            results.append(resource)

    return results
```

按钮函数：

```python
def on_search():
    keyword = search_var.get()
    results = search_resources(keyword)
    refresh_tree(results)
```

界面：

```python
search_var = tk.StringVar()

search_entry = tk.Entry(window, textvariable=search_var)
search_entry.pack()

search_button = tk.Button(window, text="搜索", command=on_search)
search_button.pack()
```

------

# 二十一、给 Treeview 加滚动条

资料多了之后，必须加滚动条。

推荐用 `Frame` 包住 Treeview 和滚动条。

```python
table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

y_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=y_scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
y_scrollbar.pack(side="right", fill="y")
```

------

## `Scrollbar(...)` 参数解释

```python
ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
```

## 1. `parent`

滚动条放在哪个容器里。

这里是：

```python
table_frame
```

------

## 2. `orient`

方向。

```python
orient="vertical"
```

垂直滚动条。

```python
orient="horizontal"
```

水平滚动条。

------

## 3. `command`

滚动条拖动时，控制谁滚动。

```python
command=tree.yview
```

表示滚动条控制 Treeview 上下滚动。

------

## `tree.configure(yscrollcommand=...)`

```python
tree.configure(yscrollcommand=y_scrollbar.set)
```

意思是：

> Treeview 滚动时，也要同步更新滚动条的位置。

滚动条和 Treeview 要互相绑定：

```python
Scrollbar command -> tree.yview
Treeview yscrollcommand -> scrollbar.set
```

------

# 二十二、横向滚动条

列很多时可以加横向滚动条。

```python
x_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="horizontal",
    command=tree.xview
)

tree.configure(xscrollcommand=x_scrollbar.set)

tree.pack(side="top", fill="both", expand=True)
x_scrollbar.pack(side="bottom", fill="x")
```

不过初期可以先不加横向滚动条，而是控制列宽。

------

# 二十三、点击表头排序

简单排序可以直接对 Treeview 里的数据排。

```python
def sort_by_column(column, reverse=False):
    items = list(tree.get_children())

    items.sort(
        key=lambda item: tree.set(item, column),
        reverse=reverse
    )

    for index, item in enumerate(items):
        tree.move(item, "", index)

    tree.heading(
        column,
        command=lambda: sort_by_column(column, not reverse)
    )
```

设置表头：

```python
tree.heading(
    "title",
    text="标题",
    command=lambda: sort_by_column("title", False)
)
```

------

## `move()` 参数解释

```python
tree.move(item, parent, index)
```

## 1. `item`

要移动的行 ID。

## 2. `parent`

移动到哪个父节点下面。

普通表格写：

```python
""
```

## 3. `index`

移动到第几行。

```python
0
```

表示第一行。

------

# 二十四、用 `displaycolumns` 控制显示哪些列

创建 Treeview 时可以写：

```python
tree = ttk.Treeview(
    window,
    columns=("id", "title", "subject", "file_type"),
    displaycolumns=("title", "subject", "file_type"),
    show="headings"
)
```

## `columns`

表示所有数据列。

## `displaycolumns`

表示真正显示出来的列。

这个很适合 StudyVault v2：

```text
id 需要保存，但不一定要显示给用户看
```

不过更推荐你用 `iid=resource["id"]` 保存 ID，这样就不必显示 ID 列了。

------

# 二十五、判断某一行是否存在

```python
tree.exists(item_id)
```

例子：

```python
if tree.exists("001"):
    print("这一行存在")
else:
    print("这一行不存在")
```

在刷新、删除、更新时可以用到。

------

# 二十六、获取焦点行：`focus()`

```python
item_id = tree.focus()
```

表示当前焦点所在的行。

它和 `selection()` 有点像，但初学阶段更推荐用：

```python
tree.selection()
```

因为它更直接表示“用户选中的行”。

------

# 二十七、Treeview 常见错误

## 1. 忘记 `show="headings"`

现象：表格左边多出一列空白列。

修法：

```python
tree = ttk.Treeview(window, columns=columns, show="headings")
```

------

## 2. `values` 数量和列数量对不上

列定义：

```python
columns = ("title", "subject", "file_type")
```

但是插入：

```python
tree.insert("", "end", values=("高数笔记", "数学"))
```

少了一个值。

虽然不一定立刻报错，但显示会不完整。

------

## 3. `iid` 重复

```python
tree.insert("", "end", iid="001", values=(...))
tree.insert("", "end", iid="001", values=(...))
```

这样会报错。

因为每一行 ID 必须唯一。

------

## 4. 只删除 Treeview，没有保存 JSON

很多初学者会写：

```python
tree.delete(resource_id)
```

然后以为资料真的删除了。

实际上只是界面消失了。

StudyVault v2 正确删除应该是：

```text
删除内存里的 resources 数据
save_resources(resources)
refresh_tree(resources)
可选：确认后删除真实文件
```

------

## 5. 把 Treeview 当数据库

Treeview 不是数据库，也不是 JSON 文件。

它只是显示控件。

你的真实数据应该在：

```text
resources.json
```

程序运行时读成：

```python
resources = load_resources()
```

Treeview 只是把 `resources` 显示出来。

------

# 二十八、StudyVault v2 推荐写法总结

你的主流程可以这样设计：

```python
resources = load_resources()

refresh_tree(resources)
```

导入资料后：

```python
resources = load_resources()
resources.append(new_resource)
save_resources(resources)
refresh_tree(resources)
```

搜索资料后：

```python
results = search_resources(keyword)
refresh_tree(results)
```

删除资料后：

```python
resources = [r for r in resources if r["id"] != selected_id]
save_resources(resources)
refresh_tree(resources)
```

双击打开资料：

```python
selected_id = tree.selection()[0]
resource = find_resource_by_id(selected_id)
open_file(resource["stored_path"])
```

------

# 二十九、你现在最应该掌握的 8 个 Treeview 操作

先把这 8 个练熟就够你做 StudyVault v2 第一版表格了：

```python
ttk.Treeview(...)
```

创建表格。

```python
tree.heading(...)
```

设置表头。

```python
tree.column(...)
```

设置列宽和对齐。

```python
tree.insert(...)
```

插入一行资料。

```python
tree.get_children()
```

获取所有行。

```python
tree.delete(...)
```

删除行或清空表格。

```python
tree.selection()
```

获取用户选中的行。

```python
tree.item(...)
```

读取或修改某一行的数据。

------

# 三十、建议你的 StudyVault Treeview 列设计

初期可以先用这些列：

```python
columns = (
    "title",
    "subject",
    "original_name",
    "file_type",
    "file_size",
    "create_time"
)
```

对应表头：

```python
tree.heading("title", text="标题")
tree.heading("subject", text="科目")
tree.heading("original_name", text="原文件名")
tree.heading("file_type", text="类型")
tree.heading("file_size", text="大小")
tree.heading("create_time", text="创建时间")
```

对应插入：

```python
tree.insert(
    "",
    "end",
    iid=resource.get("id"),
    values=(
        resource.get("title", ""),
        resource.get("subject", ""),
        resource.get("original_name", ""),
        resource.get("file_type", ""),
        resource.get("file_size", ""),
        resource.get("create_time", "")
    )
)
```

这就是 StudyVault v2 资料表格的核心。
先把“显示所有资料、选中一条资料、搜索后刷新表格”做出来，Treeview 你就已经掌握了一大半。