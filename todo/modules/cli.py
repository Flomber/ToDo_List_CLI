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
        editor.manager.list_all()
        save_last_filename(basename)
    elif args.command == "renum":
        editor.load_from_json(basename)
        editor.manager.renumber()
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "addm":
        editor.load_from_json(basename)
        editor.manager.create_matter(args.titel)
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "notem":
        editor.load_from_json(basename)
        editor.manager.note_matter(args.id, args.titel)
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "delm":
        editor.load_from_json(basename)
        editor.manager.remove_matter(args.id)
        editor.save_to_json()
    elif args.command == "addt":
        editor.load_from_json(basename)
        editor.manager.create_task(args.titel)
        editor.save_to_json()
        save_last_filename(basename)
    elif args.command == "done":
        editor.load_from_json(basename)
        editor.manager.mark_done(args.id)
        editor.save_to_json()
        save_last_filename(basename)
    # elif args.command == "export":
    #     editor.export_to_txt(args.filename)
