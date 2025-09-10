# MODULE TO DEFINE GENERAL FUNKTIONS

import argparse
import json
import os
from typing import Optional

def add_new_parser(subparsers, command_name: str, help_text: str, args: Optional[list[tuple[str, type, str]]] = None) -> None:
    # useless right now
    parser_name = command_name + "_parser"
    parser_name = subparsers.add_parser(command_name, help=help_text)
    if args:
        for name, typ, arg_help in args:
            parser_name.add_argument(name, type=typ, help=arg_help)

def set_parser() -> argparse.Namespace:
    #set up parser and subparser
    parser = argparse.ArgumentParser(description="ToDo CLI to manage your ToDo's")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_new_parser(command_name: str, help_text: str, args: Optional[list[tuple[str, type, str, dict]]] = None, subparsers=subparsers) -> argparse.ArgumentParser:
        parser_obj = subparsers.add_parser(command_name, help=help_text)
        if args:
            for name, typ, arg_help, extra in args:
                parser_obj.add_argument(name, type=typ, help=arg_help, **(extra or {}))
        return parser_obj

    #create todo list
    add_new_parser(
        "init", 
        "Create a txt file with base todo list layout", 
        [
            ("filename", str, "Choose a filename for your todo list (optional, dafault: 'todo')", {"nargs": "?"})
        ]
    )

    #list todos
    add_new_parser(
        "list", 
        "List all matters and tasks", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
        ]
    ).add_argument(
        "--section", "-s",
        choices = ["matters", "tasks", "done"],
        help = "List a specific section"
    )

    #manually renumber tasks
    add_new_parser(
        "renum", 
        "Renumber all todo's", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"})
        ]
    )

    #add matter
    add_new_parser(
        "addm", 
        "Add new matter", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
            ("titel", str, "Titel of matter in ''", {"nargs": "+"})
        ]
    )

    #add note to matter
    add_new_parser(
        "notem", 
        "Add note to existing matter", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
            ("id", int, "ID of matter", {}), 
            ("titel", str, "Titel of note in ''", {"nargs": "+"})
        ]
    )

    #remove matter
    add_new_parser(
        "delm", 
        "Deletes existing matter", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
            ("id", int, "ID of matter", {})
        ]
    )

    #add task
    add_new_parser(
        "addt", 
        "Add new task", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
            ("titel", str, "Titel of task in ''", {"nargs": "+"})
        ]
    )

    #add note to task
    add_new_parser(
        "notet", 
        "Add note to existing task", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
            ("id", int, "ID of task", {}), 
            ("titel", str, "Titel of note in ''", {"nargs": "+"})
        ]
    )

    #remove task
    add_new_parser(
        "delt", 
        "Deletes existing task", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
            ("id", int, "ID of task", {})
        ]
    )

    #mark task done
    add_new_parser(
        "done", 
        "Marks task as done", 
        [
            ("filename", str, "Filename of todo list (optional)", {"nargs": "?"}), 
            ("id", int, "ID of task", {})
        ]
    )

    #export todo list
    #add_new_parser("export", "Export ToDo list to txt file", [("filename", str, "Filename of todo list (optional)", {"nargs": "?"})])

    args = parser.parse_args()

    return args

#Hilfsfunktion, um matters und tasks in Listen zu schreiben
def list_content(header: str, attribute: list) -> list[str]:
    lines: list[str] = []
    lines.append(header)
    for content in attribute:
        lines.append(f"{content.id}. {content.titel}")
        for note in content.note:
            lines.append(f"\t-> {note}")
    return lines

def write_content_txt(file: str, lines: list[str]) -> None:
    with open(file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def write_content_json(file: str, data: dict[str, list[dict]]) -> None:
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Funktion zur Speicherung des letzten Dateinamens
LAST_FILE_MARKER: str = ".todo_last"

def save_last_filename(basename: str, base_dir: str = ".") -> None:
    # saves last used filename (without .txt or .json) in ".todo_last"
    marker_path: str = os.path.join(base_dir, "todo", "modules", LAST_FILE_MARKER)
    with open(marker_path, "w", encoding="utf-8") as f:
        f.write(basename.strip())

def load_last_filename(base_dir: str = ".") -> Optional[str]:
    # reads last used filename if it exists
    marker_path: str = os.path.join(base_dir, "todo", "modules", LAST_FILE_MARKER)
    if os.path.exists(marker_path):
        with open(marker_path, "r", encoding="utf-8") as f:
            name: str = f.read().strip()
            return name if name else None
    return None

def resolve_basename(preferred: Optional[str]) -> str:
    # chooses basename in order 1) preferred, 2) last saved filename, 3) Fallback 'todo'
    if preferred and preferred.strip():
        return preferred.strip()
    last = load_last_filename()
    return last if last else "todo"
