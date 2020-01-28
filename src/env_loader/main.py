import os

from .consts import EnvTypes, HIERARCHY
from .env_file import EnvFile


def find_env_dir():
    raise NotImplementedError


def load_env(dir_path=None, env_type=EnvTypes.DEFAULT_ENV, export_to_env=True, raise_file_not_found=False, auto_parse=True):
    dir_path = dir_path or find_env_dir()
    file_hierarchy = HIERARCHY[env_type]
    env_file = EnvFile(env_type, auto_parse=auto_parse)
    for file in file_hierarchy:
        file_path = os.path.join(dir_path, file)
        try:
            data = _read_file(file_path)
            env_file.update(data)
        except FileNotFoundError as e:
            if raise_file_not_found:
                raise e
    if export_to_env:
        env_file.export()
    return env_file


def _read_file(file_path):
    output = {}
    with open(file_path, "r") as file:
        for line in file.readlines():
            if "=" in line:
                key, value = line.split("=")
                output[key] = value
    return output
