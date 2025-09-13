# DEFINE CLI COMMANDS
from .models import ToDoManager as Manager
from .editor import ToDoEditor as Editor
from .utils import set_parser, resolve_basename, save_last_filename, delete_last_filename

def cli_logics() -> None:
    args = set_parser()

    # create objects
    manager = Manager()
    editor = Editor()
    editor.manager = manager

    if args.command in {"addt", "addm", "done", "list", "export"}:
        basename = resolve_basename(getattr(args, "filename", None))
    elif args.command == "init":
        basename = resolve_basename(getattr(args, "filename", None))
    else:
        basename = resolve_basename(None)

    # Check for entered command
    if args.command == "init":
        editor.create_json(basename)
        editor.create_txt(basename)
        save_last_filename(basename)
    elif args.command == "delete":
        editor.delete_files(basename)
        delete_last_filename()
    elif args.command == "reload":
        editor.load_from_json(basename)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "list":
        editor.load_from_json(basename)
        editor.manager.list(args.section)
        save_last_filename(basename)
    elif args.command == "renum":
        editor.load_from_json(basename)
        editor.manager.renumber()
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "clear":
        editor.load_from_json(basename)
        editor.clear_json(basename, args.section)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "addm":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.create_matter(titel)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "notem":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.note_matter(args.id, titel)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "delm":
        editor.load_from_json(basename)
        editor.manager.remove_matter(args.id)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "addt":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.create_task(titel)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "notet":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.note_task(args.id, titel)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "delt":
        editor.load_from_json(basename)
        editor.manager.remove_task(args.id)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    elif args.command == "done":
        editor.load_from_json(basename)
        editor.manager.mark_done(args.id)
        editor.save_to_json()
        editor.json_to_txt()
        save_last_filename(basename)
    # elif args.command == "export":
    #     editor.export_to_txt(args.filename)
