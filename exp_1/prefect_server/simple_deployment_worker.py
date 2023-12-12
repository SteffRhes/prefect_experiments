from prefect import flow


@flow(log_prints=True)
def simple_flow(param_1: str, param_2: int):
    print("success 3", param_1, param_2)


if __name__ == "__main__":
    simple_flow.deploy(
        name="simple_flow deployment via worker, now with Exception",
        work_pool_name="my-docker-pool-sresch",
        image="my-first-deployment-image:tutorial",
        push=False,
    )
