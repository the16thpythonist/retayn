import os

from retayn.exercises import Exercise

from .utils import ASSETS_PATH


def test_loading_mock_exercise_from_folder_works():
    path = os.path.join(ASSETS_PATH, 'mock_exercise')
    exercise = Exercise.from_folder('test', path)
    assert isinstance(exercise, Exercise)
    assert 'title' in exercise.metadata

    content: str = exercise.get_content()
    assert content != ''
    assert exercise.metadata['title'] in content

    solution: str = exercise.get_solution()
    assert solution != ''
    assert exercise.metadata['title'] in content

