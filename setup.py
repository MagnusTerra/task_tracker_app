from setuptools import setup, find_packages

setup(
    name="task-cli-app",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "task-cli-app=task_cli.main:main",
        ],
    },
    install_requires=[
        "click",
    ],
    author="MagnusTerra",
    author_email="escalantejose22@gmail.com",
    description="A simple task CLI application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MagnusTerra/task-cli-app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
