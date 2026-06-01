from pathlib import Path
import json


DATA_FILE = Path("data") / "resources.json"


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
