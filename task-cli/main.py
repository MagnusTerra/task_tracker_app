from functions import TaskCLI
from datetime import datetime

def main():
    """
    Main function.

    This function is the entry point of the application. It creates
    an instance of TaskCLI and calls its list_tasks method with the
    status argument set to "in-progress".

    Parameters:
    None

    Returns:
    None
    """

    task_cli = TaskCLI()
    task_cli.list_tasks(status="completed")
    
if __name__ == "__main__":
    main()
