from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
	install_requires = f.readlines()

setup(
    name="hello_world",
    version="0.1.0",
    description="Tool for setting up coding projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gregbioinf/hello_world",
    author="Gregory Leeman",
    author_email="gregoryleeman@outlook.com",
    python_requires=">=3.5",
    install_requires=install_requires,
	packages=find_packages(),
	package_data = {"": ["data"]},
    entry_points={
        "console_scripts": [
			"hello = hello_world.hello_world:main",
        ]
    }
)
