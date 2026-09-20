import time
def decorator_timer(func):
    def wrapper():
        print("начало исполнения")
        func()
        print("конец исполнения")

    return wrapper

def load_file():
   print("Uploading file")
   time.sleep(2)

load_file = decorator_timer(load_file)

load_file()