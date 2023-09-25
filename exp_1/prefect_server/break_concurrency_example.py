import time
from prefect import flow, task


value = None


@task()
def bar(i):
    global value
    if i == 1:
        value = 1
        print("case 1, value:", value)
        time.sleep(3)
        print("case 1, value:", value)
    elif i == 2:
        value = 2
        print("case 2, value:", value)


@flow()
def foo():
    bar.submit(1)
    bar.submit(2)
    

if __name__ == "__main__":
    foo()


