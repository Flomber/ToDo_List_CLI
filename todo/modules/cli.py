# DEFINE CLI COMMANDS
from .models import ToDoManager as Manager
from .editor import ToDoEditor as Editor
from .utils import set_parser, resolve_basename, save_last_filename

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

    if args.command == "init":
        editor.create_json(basename)
        save_last_filename(basename)
    elif args.command == "list":
        editor.load_from_json(basename)
        editor.manager.list(args.section)
        save_last_filename(basename)
    elif args.command == "renum":
        editor.load_from_json(basename)
        editor.manager.renumber()
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "addm":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.create_matter(titel)
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "notem":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.note_matter(args.id, titel)
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "delm":
        editor.load_from_json(basename)
        editor.manager.remove_matter(args.id)
        editor.save_to_json()
    elif args.command == "addt":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.create_task(titel)
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "notet":
        titel = " ".join(args.titel)
        editor.load_from_json(basename)
        editor.manager.note_task(args.id, titel)
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "delt":
        editor.load_from_json(basename)
        editor.manager.remove_task(args.id)
        editor.save_to_json()
    elif args.command == "done":
        editor.load_from_json(basename)
        editor.manager.mark_done(args.id)
        editor.save_to_json()
        save_last_filename(basename)
    # elif args.command == "export":
    #     editor.export_to_txt(args.filename)
