from time import sleep
import httpx
from datetime import timedelta
from prefect import flow, task, get_run_logger
from prefect.tasks import task_input_hash


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
def get_url(url: str, params: dict = None):
    response = httpx.get(url, params=params)
    response.raise_for_status()
    sleep(2)
    return response.json()


@flow(log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    for id in range(1, 6):
        url = f"https://dummyjson.com/products/{id}"
        data = get_url(url)
        print(data)


get_repo_info()
