import threading
import time
import random


mutex = [threading.Semaphore(1), threading.Semaphore(1), threading.Semaphore(1), threading.Semaphore(1)]

mutex_intersection = threading.Semaphore(3)

mutex_print = threading.Semaphore(1)

check = [1, 1, 1, 1]

def enter_square(square):
    mutex_intersection.acquire()
    mutex[square].acquire()
    check[square] = 0

def leave_square(square):
    mutex_intersection.release()
    mutex[square].release()
    check[square] = 1

def view_intersection():
    mutex_intersection.acquire()
    print("Viewing intersection")
    print("    | | |")
    print("  __| | |__")
    print("  __ {} {} __".format(1 - check[0], 1 - check[1]))
    print("  __ {} {} __".format(1 - check[3], 1 - check[2]))
    print("    | | |")
    print("    | | |")
    mutex_intersection.release()





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
        car = random.randint(0,3)
        turning = random.randint(0,2)
        print("{} {}".format(car, turning))
        t = threading.Thread(target=intersection, args=(car, turning))
        threads.append(t)
        t.start()

def main():
    threads = []
    cars = []
    n=5
    for i in range(n):
        cars.append([random.randint(0,3),random.randint(0,2)])
        
    for i in range(n):
        print(cars[i])

    for i in range(n):
        t = threading.Thread(target=intersection, args=(cars[i][0],cars[i][1]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

main()
    