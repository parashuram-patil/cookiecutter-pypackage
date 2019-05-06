#!/usr/bin/env python
import os
from os.path import dirname

import virtualenv

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
VIRTUAL_ENV_DIR_NAME = 'venv'


def get_project_root_path():
    return dirname(__file__)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_pytest }}' == 'y':
        remove_file('tests/__init__.py')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '' == 'y':
        virtualenv.create_environment(get_project_root_path + '/' + VIRTUAL_ENV_DIR_NAME)
