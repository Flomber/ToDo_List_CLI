# MODULE TO MANAGE SAVING AND LOADING OF TO-DO FILES

import json
import os
from .models import ToDoManager, Matter, Task
from .utils import list_content, write_content_txt, write_content_json

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
            "removed_matters": [],
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
            "removed_matters": [matter.__dict__ for matter in self.manager.removed_matters],
            "tasks": [task.__dict__ for task in self.manager.tasks],
            "removed_tasks": [task.__dict__ for task in self.manager.removed_tasks],
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
        self.manager.removed_matters = [Matter(**m) for m in data.get("removed_matters", [])]
        self.manager.tasks = [Task(**t) for t in data.get("tasks", [])]
        self.manager.removed_tasks = [Task(**t) for t in data.get("removed_tasks", [])]
        self.manager.done = [Task(**d) for d in data.get("done", [])]

    def clear_json(self, basename, section) -> None:
        if section == "matters":
            clear: bool = True if input(f"Are you sure you want to clear content of {section} in {basename}?\n(y/n)\n").lower() == "y" or "yes" or "1" else False
            if clear is False:
                return
            self.manager.matters.clear()
        elif section == "tasks":
            clear: bool = True if input(f"Are you sure you want to content of {section} in {basename}?\n(y/n)\n").lower() == "y" or "yes" or "1" else False
            if clear is False:
                return
            self.manager.tasks.clear()
        elif section == "done":
            clear: bool = True if input(f"Are you sure you want to content of {section} in {basename}?\n(y/n)\n").lower() == "y" or "yes" or "1" else False
            if clear is False:
                return
            self.manager.done.clear()
        elif section == "removed matters":
            clear: bool = True if input(f"Are you sure you want to content of {section} in {basename}?\n(y/n)\n").lower() == "y" or "yes" or "1" else False
            if clear is False:
                return
            self.manager.removed_matters.clear()
        elif section == "removed tasks":
            clear: bool = True if input(f"Are you sure you want to content of {section} in {basename}?\n(y/n)\n").lower() == "y" or "yes" or "1" else False
            if clear is False:
                return
            self.manager.removed_tasks.clear()
        elif section is None:
            clear: bool = True if input(f"Are you sure you want to clear all content of {basename}?\n(y/n)\n").lower() == "y" or "yes" or "1" else False
            if clear is False:
                return
            self.manager.matters.clear()
            self.manager.removed_matters.clear()
            self.manager.tasks.clear()
            self.manager.removed_tasks.clear()
            self.manager.done.clear()
        else:
            print("section does not exist")
    
    def json_to_txt(self):
        json_file = self.file
        txt_file = self.file.split(".")[0] + ".txt"

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        lines = []
        lines += list_content("===| Fragen/Vorschlaege |===", [Matter(**m) for m in data["matters"]])
        lines += list_content("\n===| Tasks |===", [Task(**t) for t in data["tasks"]])
        lines += list_content("\n===| Done Tasks |===", [Task(**d) for d in data["done"]])
        write_content_txt(txt_file, lines)

    def delete_files(self, basename: str):
        json_file: str = basename + ".json"
        txt_file: str = basename + ".txt"
        clear: bool = True if input(f"Are you sure you want to delete your todo list named '{basename}'?\n(y/n)\n").lower() == "y" or "yes" or "1" else False
        
        for file in [json_file, txt_file]:
            if clear is False:
                return
            if os.path.exists(file):
                os.remove(file)
                print(f"{file} was deleted")
 
    #==========| txt stuff |==========#
    #hier eine Funktion, um eine neue Listendatei zu erstellen.
    def create_txt(self, basename: str = "todo"):
        file = basename + ".txt"
        if os.path.exists(file):
            print(f"File {file} exists already")
            return
        
        lines = ["===| Fragen/Vorschlaege |===", "\n", "===| Tasks |===", "\n", "===| Done Tasks |==="]

        write_content_txt(file, lines)
        print(f"Created empty txt file named {file}")

    #hier eine Funktion, um eine existierende Listendatei zu laden
    def load_txt(self, file: str) -> None:
        pass

    def export_to_txt(self, file: str):
        matter_list: list[str] = list_content("===| Fragen/Vorschlaege |===", self.manager.matters)
        task_list: list[str] = list_content("===| Tasks |===", self.manager.tasks)
        done_list: list[str] = list_content("===| Done Tasks |===", self.manager.done)

        content_list = matter_list + task_list + done_list

        write_content_txt(file , content_list)
