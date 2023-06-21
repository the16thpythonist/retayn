import unittest
import os

from utils import ASSETS_PATH



def test_asset_path_exists(self):
    assert os.path.exists(ASSETS_PATH)
    assert os.path.isdir(ASSETS_PATH)


def test_assets_readme_exists(self):
    readme_path = os.path.join(ASSETS_PATH, 'README.rst')
    assert os.path.exists(readme_path)
    assert os.path.isfile(readme_path)
