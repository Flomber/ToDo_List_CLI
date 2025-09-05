# MODULE TO MANAGE SAVING AND LOADING OF TO-DO FILES

from .models import ToDoManager
from .utils import list_content, write_content

header_dict: dict[int, str] = {
    1: "===| Fragen/Vorschlaege |===",
    2: "===| Tasks |===",
    3: "===| Done Tasks |==="
}

class ToDoEditor:
    def __init__(self) -> None:
        self.manager = ToDoManager()

    #hier eine Funktion, um eine neue Listendatei zu erstellen.
    def create_txt(self, file):
        lines = [header_dict[1], header_dict[2], header_dict[3]]

        write_content(file, lines)

    #hier eine Funktion, um eine existierende Listendatei zu laden
    #def load_txt():

    def export_to_txt(self, file: str):
        matter_list: list[str] = list_content(header_dict[1], self.manager.matters)
        task_list: list[str] = list_content(header_dict[2], self.manager.tasks)
        done_list: list[str] = list_content(header_dict[3], self.manager.done)

        content_list = matter_list + task_list + done_list

        write_content(file , content_list)
