# StudyVault 学习资料管理器

StudyVault 是一个适合 Python 初学者练习的命令行项目。它不是为了让别人直接给你写完程序，而是帮助你按照真实项目流程，自己一步一步完成一个能运行、能保存数据、能上传到 GitHub 的小工具。

这个项目的第一版目标是：用 Python 标准库制作一个学习资料管理器，可以添加资料、查看资料、搜索资料、删除资料、统计资料，并把数据保存到 JSON 文件中。

## 适合人群

- 刚学完 Python 基础语法
- 想第一次完整做一个小项目
- 想学习 Git、GitHub、VS Code 的基本项目流程
- 想练习把需求拆成函数和文件

## 第一版功能目标

第一版只做命令行基础版，不做图形界面，也不做真实移动文件的自动整理功能。

计划完成的菜单：

```text
欢迎使用 StudyVault 学习资料管理器

1. 添加学习资料
2. 查看所有资料
3. 按科目搜索资料
4. 按关键词搜索资料
5. 查看统计信息
6. 删除资料记录
7. 今日随机推荐
8. 退出程序
```

## 建议项目结构

```text
Study Srouce manage/
├── main.py
├── data/
│   └── resources.json
├── README.md
└── .gitignore
```

刚开始可以把所有 Python 代码都写在 `main.py` 里。等你熟练以后，再考虑拆成多个文件。

## 数据设计

学习资料建议保存为 JSON 列表，每一条资料是一个字典：

```json
[
  {
    "id": 1,
    "name": "Python 函数笔记",
    "subject": "Python",
    "path": "D:/notes/function.txt",
    "tags": ["基础", "函数", "复习"],
    "created_time": "2026-05-26"
  }
]
```

你需要重点理解：

- 列表用来保存多条资料
- 字典用来保存一条资料的信息
- JSON 文件用来让数据在程序关闭后仍然保留

## 建议函数拆分

你可以按下面的顺序逐步写函数：

```python
load_resources()          # 从 JSON 文件读取资料
save_resources()          # 把资料保存到 JSON 文件
show_menu()               # 显示菜单
add_resource()            # 添加学习资料
list_resources()          # 查看所有资料
search_by_subject()       # 按科目搜索
search_by_keyword()       # 按关键词搜索
show_statistics()         # 查看统计信息
delete_resource()         # 删除资料
recommend_resource()      # 随机推荐资料
main()                    # 程序入口和菜单循环
```

每次只写一个函数。写完一个函数就运行程序测试，不要一次写太多。

## 一周学习计划

### 第 1 天：项目准备

目标：理解项目要做什么，并把仓库整理好。

要做：

- 用 VS Code 打开项目文件夹
- 阅读并理解本 README
- 确认 `main.py` 是你的主程序文件
- 确认 `.gitignore` 已经忽略 `.vs/`、`__pycache__/` 等临时文件

学习点：

- 什么是项目根目录
- README 的作用
- Git 仓库的作用
- `.gitignore` 的作用

建议 Git 提交：

```text
chore: initialize learning project
```

### 第 2 天：菜单和主循环

目标：先让程序能启动、能显示菜单、能根据输入选择功能。

要做：

- 写 `show_menu()`
- 写 `main()`
- 用 `while True` 保持程序运行
- 用户输入 `8` 时退出
- 其他功能先打印“功能开发中”

学习点：

- 函数
- 循环
- 条件判断
- `if __name__ == "__main__"`

建议 Git 提交：

```text
feat: add command line menu
```

### 第 3 天：JSON 读写和添加资料

目标：让资料可以被保存下来。

要做：

- 创建 `data/resources.json`
- 写 `load_resources()`
- 写 `save_resources()`
- 写 `add_resource()`
- 添加资料时记录名称、科目、路径、标签、日期

学习点：

- 文件读写
- JSON
- 列表和字典
- 日期时间

建议 Git 提交：

```text
feat: add resource creation and json storage
```

### 第 4 天：查看、搜索、删除

目标：让用户可以管理已经添加的资料。

要做：

- 写 `list_resources()`
- 写 `search_by_subject()`
- 写 `search_by_keyword()`
- 写 `delete_resource()`

学习点：

- 遍历列表
- 字符串匹配
- 条件筛选
- 删除列表元素

建议 Git 提交：

```text
feat: add list search and delete features
```

### 第 5 天：统计和随机推荐

目标：让项目更像一个真正的小工具。

要做：

- 写 `show_statistics()`
- 统计资料总数
- 统计每个科目的资料数量
- 统计常用标签
- 写 `recommend_resource()`

学习点：

- 字典计数
- `random` 模块
- 函数复用

建议 Git 提交：

```text
feat: add statistics and random recommendation
```

### 第 6 天：测试和优化

目标：检查程序是否稳定。

要测试：

- 第一次运行时没有 `resources.json` 是否会崩溃
- 添加资料后重新运行，资料是否还在
- 空输入时程序是否能提示
- 搜索不存在的内容是否显示合理提示
- 删除不存在的编号是否会崩溃
- 没有资料时统计和随机推荐是否能正常处理

学习点：

- 测试用例
- 异常情况
- 用户体验

建议 Git 提交：

```text
fix: improve validation and user prompts
```

### 第 7 天：整理文档和上传 GitHub

目标：把项目变成一个可以展示的学习成果。

要做：

- 更新 README，写清楚项目已经完成的功能
- 补充运行方法
- 补充学习总结
- 在 GitHub 新建仓库
- 把本地仓库推送到 GitHub

建议 Git 提交：

```text
docs: add project summary
```

## Git 使用建议

每完成一个小功能，就提交一次。

常用提交类型：

```text
feat: 新功能
fix: 修复问题
docs: 文档更新
chore: 项目配置或杂项
```

推荐流程：

```text
1. 写一个小功能
2. 运行程序测试
3. 查看改了哪些文件
4. 提交这次改动
5. 继续写下一个小功能
```

不要把这些内容提交到 Git：

- `.vs/`
- `__pycache__/`
- `.pyc`
- 临时测试文件
- 系统缓存文件

## VS Code 使用建议

- 每次只打开当前项目文件夹
- 主要编辑 `main.py` 和 `README.md`
- 运行程序时使用终端执行 `python main.py`
- 报错时先看最后一行，再看文件名和行号
- 不懂的代码先写注释，再慢慢实现

## 验收标准

当你完成第一版时，项目应该满足：

- 可以用 `python main.py` 启动
- 菜单 1 到 8 都可以选择
- 数据可以保存到 JSON 文件
- 关闭程序后重新打开，资料仍然存在
- 搜索、删除、统计、随机推荐都能正常工作
- README 能让别人看懂这个项目是什么、怎么运行、你学到了什么
- Git 里有清晰的提交记录

## 以后如何自己写项目计划

以后你可以按这个模板规划任何小项目：

```text
1. 项目名称：这个项目叫什么？
2. 项目目标：它解决什么问题？
3. 使用对象：谁会用它？
4. 第一版范围：最小可运行版本做哪些功能？
5. 暂时不做什么：先排除哪些复杂功能？
6. 数据设计：需要保存哪些信息？
7. 功能拆分：每个功能输入什么、输出什么？
8. 文件结构：代码和数据放在哪里？
9. 开发步骤：每天或每阶段完成什么？
10. 测试清单：怎么证明它真的能用？
11. Git 计划：什么时候提交，提交信息怎么写？
12. 后续扩展：第一版完成后还能升级什么？
```

第一次做项目时，最重要的不是功能多，而是完整走完一次流程：计划、编码、测试、文档、提交、上传、复盘。
