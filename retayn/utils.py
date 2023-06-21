import os
import sys
import pathlib
import logging
import importlib
import importlib.util

import jinja2 as j2

PATH = pathlib.Path(__file__).parent.absolute()
VERSION_PATH = os.path.join(PATH, 'VERSION')
TEMPLATES_PATH = os.path.join(PATH, 'templates')

# Use this jinja environment to access the templates defined in j2
TEMPLATE_ENV = j2.Environment(
    loader=j2.FileSystemLoader(TEMPLATES_PATH),
    autoescape=j2.select_autoescape()
)

# You can use this logger as a default argument for functions which may optionally use a logger! It can be
# used like any other logger but doesn't actually log anything.
NULL_LOGGER = logging.getLogger('NULL')
NULL_LOGGER.addHandler(logging.NullHandler())


def get_version() -> str:
    """
    Returns the version string which is saved in the VERSION file within the package's main folder.

    :return str: the version string
    """
    with open(VERSION_PATH, mode='r') as file:
        content = file.read()
        return content.replace(' ', '').replace('\n', '')


def dynamic_import(module_path: str, name: str = 'module'):
    """
    Given an absolute path ``module_path`` to a python module, this function will dynamically import that
    module and return the module object, which can be used to access the contents of that module.

    :param str module_path: The absolute path to the module to be imported
    :param str name: The string name to be assigned to that module

    :returns: The module object
    """
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    # 24.03.2023 - I have learned that this is rather important to add this as well because if this line
    # is missing that will screw a lot of "inspect" shenanigans in the imported module
    sys.modules[name] = module
    spec.loader.exec_module(module)

    return module
