import time


for i in range(150):
    # seconds = round(time.time() * 100)
    # seconds = time.time() * 100
    # seconds = time.time()
    # print(seconds % 4)
    # print(seconds)
    # print(seconds * 100)
    # time.sleep(0.25)

    seconds = round(time.time() * 100)
    print(seconds)
    print(seconds % 100)
    time.sleep(0.25)
