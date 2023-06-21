from __future__ import annotations
import os
import yaml
import typing as t

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from retayn.config import Config
from retayn.utils import dynamic_import


class ExerciseRenderer:

    def __init__(self, path: str):
        self.path = path
        self.template_env = Environment(loader=FileSystemLoader(path))

    def render_content(self, config, exercise):
        raise NotImplemented

    def render_solution(self, config, exercise):
        raise NotImplemented


class Exercise:

    def __init__(self,
                 config: Config,
                 name: str,
                 metadata: dict,
                 content_func: t.Callable[[Config, Exercise], str],
                 solution_func: t.Callable[[Config, Exercise], str],
                 ):
        self.config = config
        self.name = name
        self.metadata = metadata
        self.content_func = content_func
        self.solution_func = solution_func

    def get_content(self) -> str:
        return self.content_func(self.config, self)

    def get_solution(self) -> str:
        return self.solution_func(self.config, self)

    @classmethod
    def from_folder(cls, name: str, path: str):
        meta_path = os.path.join(path, 'meta.yml')
        with open(meta_path) as file:
            metadata = yaml.load(file, yaml.FullLoader)

        module_path = os.path.join(path, 'main.py')
        module = dynamic_import(module_path)
        renderers = [value for key, value in vars(module).items() if isinstance(value, ExerciseRenderer)]
        renderer = renderers[0]

        return cls(
            config=Config(),
            name=name,
            metadata=metadata,
            content_func=renderer.render_content,
            solution_func=renderer.render_solution,
        )
