import time
from prefect import flow, serve


#@flow
#def slow_flow(sleep: int = 60):
#    "Sleepy flow - sleeps the provided amount of time (in seconds)."
#    time.sleep(sleep)
#
#
#@flow
#def fast_flow():
#    "Fastest flow this side of the Mississippi."
#    return


@flow
def foo():
    print("foo")


if __name__ == "__main__":
    foo.serve(name="foo-deployment")

    #slow_deploy = slow_flow.to_deployment(name="sleeper", interval=45)
    #fast_deploy = fast_flow.to_deployment(name="fast")
    #serve(slow_deploy, fast_deploy)

