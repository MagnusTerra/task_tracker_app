import os
import sys

def get_config_path():
    if sys.platform == "win32":
        config_path = os.path.join(os.environ["APPDATA"], "task-cli")
    else:
        config_path = os.path.join(os.path.expanduser("~"), ".task-cli") 

    os.makedirs(config_path, exist_ok=True)

    return config_path


def get_config_file():
    config_path = get_config_path()
    return os.path.join(config_path, "config.json")


def print_config():
    from task_cli import __version__
    return f"Task CLI version: {__version__}"
    