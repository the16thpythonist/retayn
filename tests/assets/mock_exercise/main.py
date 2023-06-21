import os
import pathlib

from jinja2 import loaders

from retayn.config import Config
from retayn.exercises import Exercise
from retayn.exercises import ExerciseRenderer

PATH = pathlib.Path(__file__).parent.absolute()


class Render(ExerciseRenderer):

    def __init__(self):
        super(Render, self).__init__(PATH)

    def render_content(self, config, exercise):
        template = self.template_env.get_template('content.tex.j2')
        return template.render({'config': config, 'exercise': exercise})

    def render_solution(self, config, exercise):
        template = self.template_env.get_template('solution.tex.j2')
        return template.render({'config': config, 'exercise': exercise})


render = Render()
if __name__ == '__main__':
    render()


