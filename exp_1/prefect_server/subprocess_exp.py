import subprocess
from prefect import flow


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def bash_flow():
    bash_command = "docker ps"


    try:
        result = subprocess.run(
            bash_command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Error output:")
        print(e.stderr)


if __name__ == "__main__":
    bash_flow()
