# MODULE TO DEFINE CLASSES TO MANAGE TASKS, ETC.

from typing import Optional

class Matter:
    def __init__(self, id: int, titel: str, note: Optional[list[str]] = None) -> None:
        self.id = id
        self.titel = titel
        self.note = note if note is not None else []

class Task:
    def __init__(self, id: int, titel: str, note: Optional[list[str]] = None) -> None:
        self.id = id
        self.titel = titel
        self.note = note if note is not None else []
        self.done: bool = False

# class Done(Task):
#     def __init__(self):
#         self.done = True

class ToDoManager:
    def __init__(self) -> None:
        # self.data: dict[str, list] = {
        #     "Fragen/Vorschlaege": [],
        #     "Tasks": [],
        #     "Done": []
        # }
        self.next_matter_id: int = 1
        self.next_task_id: int = 1
        self.next_done_id: int = 1

        self.matters: list[Matter] = []
        self.tasks: list[Task] = []
        self.done: list[Task] = []
    

    def add_matter(self, matter: Matter) -> None:
        self.matters.append(matter)
    def create_matter(self, titel) -> None:
        matter = Matter(self.next_matter_id, titel)
        self.add_matter(matter)
        self.next_matter_id += 1
    def remove_matter(self, matter_id: int) -> None:
        for matter in self.matters:
            if matter.id == matter_id:
                self.matters.remove(matter)
                #self.next_matter_id -= 1
    
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
    def create_task(self, titel) -> None:
        task = Task(self.next_task_id, titel)
        self.add_task(task)
        self.next_task_id += 1
    def remove_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                #self.next_task_id -= 1

    def mark_done(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                task.id = self.next_done_id
                self.done.append(task)
                self.tasks.remove(task)

    def list_matters(self) -> None:
        print("Fragen/Vorschlaege:")
        for matter in self.matters:
            print(f"{matter.id}: {matter.titel}")
            if matter.note:
                for note in matter.note:
                    print(f"\t-> {note}\n")
    def list_tasks(self) -> None:
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.id}: {task.titel}")
            if task.note:
                for note in task.note:
                    print(f"\t-> {note}\n")
    def list_done(self) -> None:
        print("Done Tasks:")
        for task in self.done:
            print(f"{task.id}: {task.titel}")
            if task.note:
                for note in task.note:
                    print(f"\t-> {note}\n")
    def list_all(self) -> None:
        self.list_matters()
        self.list_tasks()
        self.list_done()