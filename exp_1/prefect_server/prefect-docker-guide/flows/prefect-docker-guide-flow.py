from prefect import flow


@flow(log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    print("heeey")


if __name__ == "__main__":
    get_repo_info.serve(name="prefect-docker-guide")

