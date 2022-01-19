import re
from io import open
from os import path

from jupyter_packaging import (
    combine_commands,
    create_cmdclass,
    ensure_targets,
    install_npm,
)
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(this_directory, "jupyterlab-itables/version.py")) as f:
    version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    version = version_match.group(1)

setup_args = dict(
    name="jupyterlab-itables",
    version=version,
    author="Marc Wouts",
    author_email="marc.wouts@gmail.com",
    description="A JupyterLab extension for ITables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwouts/jupyterlab-itables",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

# Install labextension using jupyter_packaging
lab_path = path.join(this_directory, "jupyterlab-itables", "labextension")

data_files_spec = [
    ("share/jupyter/labextensions/jupyterlab-itables", lab_path, "**"),
    (
        "share/jupyter/labextensions/jupyterlab-itables",
        this_directory,
        "install.json",
    ),
]

# Representative files that should exist after a successful build
jstargets = [
    path.join(lab_path, "package.json"),
]

cmdclass = create_cmdclass(
    "jsdeps",
    data_files_spec=data_files_spec,
)

cmdclass["jsdeps"] = combine_commands(
    install_npm(
        lab_path,
        build_cmd="build:prod",
        npm=["jlpm"],
    ),
    ensure_targets(jstargets),
)
setup_args["cmdclass"] = cmdclass

# Call setup
setup(**setup_args)
