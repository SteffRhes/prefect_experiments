from prefect import flow, task, variables


@task
def simple_task(params):
    print("task, params:", params)
    print("var:", variables.get("test_var"))


@flow(log_prints=True)
def simple_flow(param_1: str, param_2: int):
    print("flow")
    simple_task({"1": param_1, "2": param_2})


if __name__ == "__main__":
    simple_flow.serve("flow with tasks")

