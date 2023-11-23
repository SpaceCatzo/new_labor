import json
from io import StringIO
from pathlib import Path

import yaml


def from_json_to_yaml(path, str_path):
    new_path = Path(str_path[0:-4] + 'yaml')
    with open(path) as file:
        data = file.read()

    data_dict = json.loads(data)
    output = StringIO()
    yaml.dump(data_dict, output)
    y_str = output.getvalue()

    with open(new_path, 'w') as file:
        file.write(y_str)

    notify(new_path)


def from_yaml_to_json(path, str_path):
    new_path = Path(str_path[0:-4] + 'json')
    with open(path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    with open(new_path, 'w') as file:
        new_data = json.dumps(data)
        file.write(new_data)
    notify(new_path)


def notify(new_path):
    print(f'file created in {new_path}')


def get_file():
    file_dir = input("Now you should write full file path without braces: ")
    full_file_path = Path(file_dir)
    return full_file_path


def format_file(path_, format_): # should be mpre formats
    path_string = str(path_)
    if format_ == 'yaml':
        if path_string[-4:] == 'json':
            from_json_to_yaml(path_, path_string)
    elif format_ == 'json':
        if path_string[-4:] == 'yaml':
            from_yaml_to_json(path_, path_string)


def main():
    print("""
    I`m glad to see you using my free yaml-json (and conversely) converter! :D
    Converted file will appear in directory you provide!
    Enjoy!
    (c) Elisei Senovalov 2023 
    """)
    need_format_to = input("write what format you want to receive: ")
    file_path = get_file()
    format_file(file_path, need_format_to)


main()
