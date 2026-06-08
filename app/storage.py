from pathlib import Path
import json


DATA_FILE = Path("data") / "resources.json"


def load_resources():
    try:
        contents = DATA_FILE.read_text(encoding="utf-8-sig")

        if not contents.strip():
            return []

        resources = json.loads(contents)

        if not isinstance(resources, list):
            print("resources.json 格式错误：最外层应该是列表")
            return []

        return resources

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("resources.json 内容不是合法 JSON，请检查文件格式")
        return []


def save_resources(resources):
    DATA_FILE.parent.mkdir(exist_ok=True)

    content = json.dumps(resources, ensure_ascii=False, indent=4)
    DATA_FILE.write_text(content, encoding="utf-8")