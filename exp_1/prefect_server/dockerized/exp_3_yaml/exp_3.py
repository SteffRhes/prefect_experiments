from prefect import flow


@flow(log_prints=True)
def exp_3():
    print("exp_3")

if __name__ == "__main__":
    exp_3()
    # simple_flow.deploy(
    #     name="simple_flow deployment via worker, now with Exception",
    #     work_pool_name="my-docker-pool-sresch",
    #     image="my-first-deployment-image:tutorial",
    #     push=False,
    # )
