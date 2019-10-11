#!/usr/bin/env python3
# -*- coding: utf-8

"""Script launcher.

This launcher generate its own virtual environment and installs the needed
dependencies.
"""

import pathlib
import subprocess
import sys
import venv


BASE_DIR = pathlib.Path(__file__).parent
VENV = BASE_DIR / 'venv'
SCRIPTS = VENV / 'Scripts' if sys.platform == 'win32' else venv / 'bin'
PIP = str(SCRIPTS / 'pip')
PYTHON = str(SCRIPTS / 'python')


def main():
    """Ensures the virtualenvironment exists and install dependencies."""
    if not VENV.exists():
        # Creates a virtual environment and installs dependencies using pip
        venv.create(VENV, with_pip=True)
        subprocess.run([PIP, 'install', '-r', 'requirements.txt'])

    subprocess.run([PYTHON, '-m', 'demo'])


if __name__ == "__main__":
    main()
