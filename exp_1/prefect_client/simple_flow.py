from prefect import flow


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def simple_flow():
    print("success")


if __name__ == "__main__":
    simple_flow()

