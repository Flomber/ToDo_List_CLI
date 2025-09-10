# MODULE TO DEFINE CLASSES TO MANAGE TASKS, ETC.

from typing import Optional

class Matter:
    def __init__(self, id: int, titel: str, note: Optional[list[str]] = None) -> None:
        self.id = id
        self.titel = titel
        self.note = note if note is not None else []

class Task:
    def __init__(self, id: int, titel: str, note: Optional[list[str]] = None, done: Optional[bool] = False) -> None:
        self.id = id
        self.titel = titel
        self.note = note if note is not None else []
        self.done = done if done is not False else False

# class Done(Task):
#     def __init__(self):
#         self.done = True

class ToDoManager:
    def __init__(self) -> None:
        self.matters: list[Matter] = []
        self.removed_matters: list[Matter] = []
        self.tasks: list[Task] = []
        self.removed_tasks: list[Task] = []
        self.done: list[Task] = []

    def renumber(self) -> None:
        for idx, matter in enumerate(self.matters, start=1):
            matter.id = idx
        for idx, task in enumerate(self.tasks, start=1):
            task.id = idx
        for idx, done in enumerate(self.done, start=1):
            done.id = idx

    def create_matter(self, titel) -> None:
        matter = Matter(len(self.matters) + 1, titel)
        self.matters.append(matter)
        self.renumber()

    def create_task(self, titel) -> None:
        task = Task(len(self.tasks) + 1, titel)
        self.tasks.append(task)
        self.renumber()
    
    def note_matter(self, matter_id, titel) -> None:
        for matter in self.matters:
            if matter.id == matter_id:
                matter.note.append(titel)

    def note_task(self, task_id, titel) -> None:
        for task in self.tasks:
            if task.id == task_id:
                task.note.append(titel)
        
    def remove_matter(self, matter_id: int) -> None:
        for matter in self.matters:
            if matter.id == matter_id:
                self.removed_matters.append(matter)
                self.matters.remove(matter)
        self.renumber()
    
    def remove_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                self.removed_tasks.append(task)
                self.tasks.remove(task)
        self.renumber()

    def mark_done(self, task_id: int) -> None:
        for task in list(self.tasks):
            if task.id == task_id:
                task.done = True
                self.done.append(task)
                self.tasks.remove(task)
                break
        self.renumber()

    def list_matters(self) -> None:
        print("Fragen/Vorschlaege:")
        for matter in self.matters:
            print(f"{matter.id}: {matter.titel}")
            if matter.note:
                for note in matter.note:
                    print(f"\t-> {note}")
    def list_tasks(self) -> None:
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.id}: {task.titel}")
            if task.note:
                for note in task.note:
                    print(f"\t-> {note}")
    def list_done(self) -> None:
        print("Done Tasks:")
        for task in self.done:
            print(f"{task.id}: {task.titel}")
            if task.note:
                for note in task.note:
                    print(f"\t-> {note}")
    def list(self, section) -> None:
        if section == "matters":
            self.list_matters()
        elif section == "tasks":
            self.list_tasks()
        elif section == "done":
            self.list_done()
        elif section is None:
            self.list_matters()
            self.list_tasks()
            self.list_done()
        else:
            print("section does not exist")