# funktioniert nicht mit prefect 2.x anscheinend

from prefect.tasks.shell import ShellTask
from prefect import flow


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def simple_flow():
    bash_task = ShellTask(command='echo "Hello from Bash"')
    bash_task()
    print("success")


if __name__ == "__main__":
    simple_flow()

