#!/usr/bin/env python3
# -*- coding: utf-8

"""Script launcher.

This launcher generate its own virtual environment dans install the needed
dependencies.
"""

import os.path as osp
import pip
import subprocess
import sys
import venv


def main():
    """Starts the application and creates a virtualenv in case of failure."""
    _dir, _script = osp.split(osp.abspath(__file__))
    _venv = osp.join(_dir, 'venv')
    _bin = osp.join(_venv, 'Scripts' if sys.platform == 'win32' else 'bin')
    _py = osp.join(_bin, 'python')

    try:
        # We try to import our application module
        import demo
    except ImportError:
        # Our application fails to import dependencies
        if not osp.exists(_venv):
            # Creates a virtual environment and installs
            # dependencies using pip
            venv.create(_venv, with_pip=True)
            pip.main(['install', '-r', 'requirements.txt', '--prefix', _venv])
        # Execute the script with the venv python executable
        subprocess.run([_py, _script])
    else:
        demo.main()

if __name__ == "__main__":
    main()
