# MODULE TO DEFINE GENERAL FUNKTIONS

import argparse
from typing import Optional

def add_new_parser(subparsers, command_name: str, help_text: str, args: Optional[list[tuple[str, type, str]]] = None) -> None:
    parser_name = command_name + "_parser"
    parser_name = subparsers.add_parser(command_name, help=help_text)
    if args:
        for name, typ, arg_help in args:
            parser_name.add_argument(name, type=typ, help=arg_help)

def set_parser() -> argparse.Namespace:
    #set up parser and subparser
    parser = argparse.ArgumentParser(description="ToDo CLI to manage your ToDo's")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_new_parser(command_name: str, help_text: str, args: Optional[list[tuple[str, type, str]]] = None, subparsers=subparsers) -> None:
        parser_name = command_name + "_parser"
        parser_name = subparsers.add_parser(command_name, help=help_text)
        if args:
            for name, typ, arg_help in args:
                parser_name.add_argument(name, type=typ, help=arg_help)

    #add task
    add_new_parser("addt", "Add new task", [("titel", str, "Titel of task")])

    #add matter
    add_new_parser("addm", "Add new matter", [("titel", str, "Titel of matter")])

    #mark task done
    add_new_parser("done", "Marks task as done", [("id", int, "ID of task")])

    #list task
    add_new_parser("list", "List all matters and tasks")

    #export todo list
    add_new_parser("export", "Export ToDo list to txt file", [("filename", str, "Filename of ToDo List file")])

    args = parser.parse_args()

    return args

#Hilfsfunktion, um matters und tasks in Listen zu schreiben
def list_content(header: str, attribute: list) -> list[str]:
    lines: list[str] = []
    lines.append(header)
    for contend in attribute:
        lines.append(f"{contend.id}. {contend.titel}")
        for note in contend.note:
            lines.append(f"\t-> {note}")
    return lines

def write_content(file: str, lines: list[str]):
    with open(file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
