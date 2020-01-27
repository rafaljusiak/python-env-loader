import os

from src.python_env_loader.parser import DefaultEnvParser


class EnvFile:
    def __init__(self, env_type, parser_class=DefaultEnvParser):
        self.parser = parser_class()
        self.env_type = env_type
        self.vars = {}

    def get(self, key, default=None):
        v = self.vars.get(key, os.environ.get(key))
        return v if v else default

    def update(self, data_dict, parse_values=True):
        if parse_values:
            data_dict = self._parse_values(data_dict)
        self.vars.update(data_dict)

    def export(self):
        for k, v in self.vars.items():
            os.environ.setdefault(k, str(v))

    def _parse_values(self, data_dict):
        for k, v in data_dict.items():
            data_dict[k] = self.parser.parse(v)
        return data_dict

    def __str__(self):
        return f"({self.env_type}) env file"
