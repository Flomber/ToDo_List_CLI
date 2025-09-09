# MODULE TO MANAGE SAVING AND LOADING OF TO-DO FILES

import json
import os
from .models import ToDoManager, Matter, Task
from .utils import list_content, write_content_txt, write_content_json

header_dict: dict[int, str] = {
    1: "===| Fragen/Vorschlaege |===",
    2: "===| Tasks |===",
    3: "===| Done Tasks |==="
}

class ToDoEditor:
    def __init__(self) -> None:
        self.file: str = "todo.json"
        self.manager = ToDoManager()

    #==========| JSON stuff |==========#
    def create_json(self, basename: str = "todo") -> None:
        file = basename + ".json"
        if os.path.exists(file):
            print(f"File {file} exists already")
            return
        
        data = {
            "matters": [],
            "tasks": [],
            "done": []
        }
        write_content_json(file, data)
        self.file = file
        print(f"Created empty JSON file named {file}")

    def save_to_json(self):
        if not hasattr(self, "file") or not self.file:
            raise RuntimeError("No JSON file selected. Load or create a list first!")
        data = {
            "matters": [matter.__dict__ for matter in self.manager.matters],
            "tasks": [task.__dict__ for task in self.manager.tasks],
            "done": [done.__dict__ for done in self.manager.done]
        }
        write_content_json(self.file, data)
        print(f"Saved content to {self.file}")

    def load_from_json(self, basename: str) -> None:
        self.file = basename + ".json"
        if not os.path.exists(self.file):
            print(f"File {self.file} doesn't exist")
            return
        
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.manager.matters = [Matter(**m) for m in data.get("matters", [])]
        self.manager.tasks = [Task(**t) for t in data.get("tasks", [])]
        self.manager.done = [Task(**d) for d in data.get("done", [])]
    
    def json_to_txt(self):
        json_file = self.file
        txt_file = self.file.split(".")[0] + ".txt"

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        lines = []
        lines += list_content("===| Fragen/Vorschlaege |===", [Matter(**m) for m in data["matters"]])
        lines += list_content("===| Tasks |===", [Task(**t) for t in data["tasks"]])
        lines += list_content("===| Done Tasks |===", [Task(**d) for d in data["done"]])
        write_content_txt(txt_file, lines)



    #==========| txt stuff |==========#
    #hier eine Funktion, um eine neue Listendatei zu erstellen.
    def create_txt(self, basename: str = "todo"):
        file = basename + ".txt"
        if os.path.exists(file):
            print(f"File {file} exists already")
            return
        
        lines = [header_dict[1], "\n", header_dict[2], "\n", header_dict[3]]

        write_content_txt(file, lines)
        print(f"Created empty txt file named {file}")

    #hier eine Funktion, um eine existierende Listendatei zu laden
    def load_txt(self, file: str) -> None:
        pass

    def export_to_txt(self, file: str):
        matter_list: list[str] = list_content(header_dict[1], self.manager.matters)
        task_list: list[str] = list_content(header_dict[2], self.manager.tasks)
        done_list: list[str] = list_content(header_dict[3], self.manager.done)

        content_list = matter_list + task_list + done_list

        write_content_txt(file , content_list)
