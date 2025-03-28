import threading
import time
import random


mutex = {threading.Semaphore(1), threading.Semaphore(1), threading.Semaphore(1), threading.Semaphore(1)}

mutex_intersection = threading.Semaphore(3)

check = {1, 1, 1, 1}

def enter_square(square):
    mutex[square].acquire()
    mutex_intersection.acquire()
    check[square] = 0

def leave_square(square):
    mutex_intersection.release()
    mutex[square].release()
    check[square] = 1

def view_intersection():
print("Viewing intersection")
print("    |  |  |\n")
print("  __|  |  |__\n")
print("  __ {} {} __\n".format(1 - check[0], 1 - check[1]))
print("  __ {} {} __\n".format(1 - check[3], 1 - check[2]))
print("    |  |  |\n")
print("    |  |  |\n")





def intersection(road, turn):
    square = road
    enter_square(square)
    view_intersection()
    time.sleep(random.uniform(0.5, 1.5))  # Simulate time spent in the intersection
    if turn == 0:
        enter_square((road + 1) % 4)
        leave_square(road)
        view_intersection()
        time.sleep(random.uniform(0.5, 1.5))
        leave_square((road + 1) % 4)
        view_intersection()
        

    elif turn == 1:
        leave_square(road)
        view_intersection()
        time.sleep(random.uniform(0.5, 1.5))
    else:
        enter_square((road + 1) % 4)
        leave_square(road)
        view_intersection()
        time.sleep(random.uniform(0.5, 1.5))
        enter_square((road + 2) % 4)
        leave_square((road + 1) % 4)
        view_intersection()
        
    mutex_intersection.release()
    threads = []
    for i in range(4):
        t = threading.Thread(target=intersection, args=(i, random.randint(0, 2)))
        threads.append(t)
        t.start()

def main():
    threads = []
    for i in range(4):
        t = threading.Thread(target=intersection, args=(i, random.randint(0, 2)))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    