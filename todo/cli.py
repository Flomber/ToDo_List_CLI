# DEFINE CLI COMMANDS
from .models import ToDoManager as Manager
from .editor import ToDoEditor as Editor
from .utils import set_parser

def main() -> None:
    args = set_parser()

    # create objects
    manager = Manager()
    editor = Editor()
    editor.manager = manager

    if args.command == "addt":
        editor.manager.create_task(args.titel)

    elif args.command == "addm":
        editor.manager.create_matter(args.titel)
    elif args.command == "done":
        editor.manager.mark_done(args.id)
    elif args.command == "list":
        editor.manager.list_all()
    elif args.command == "export":
        editor.export_to_txt(args.filename)

if __name__ == "__main__":
    main()
