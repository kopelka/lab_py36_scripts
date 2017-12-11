import threading
import random
import time


class Philosopher(threading.Thread):
    running = True

    def __init__(self, xname, fork_on_left, fork_on_right):
        threading.Thread.__init__(self)
        self.name = xname
        self.fork_on_left = fork_on_left
        self.fork_on_right = fork_on_right

    def run(self):
        while self.running:
            time.sleep(random.uniform(3, 13))
            print('%s is hungry.' % self.name)
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork_on_left, self.fork_on_right

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print('%s swaps forks' % self.name)
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print('%s starts eating ' % self.name)
        time.sleep(random.uniform(1, 10))
        print('%s finishes eating and leaves to think.' % self.name)


def dining_philosophers():
    """
    If failed to get second fork, release first fork,
   ap which fork is first and which is second and retry until getting both.
   """

    philosopher_names = ('Plato', 'Nietzsche', 'Rousseau', 'Bacon', 'Schopenhauer')
    forks = [threading.Lock() for n in range(5)]
    philosophers = [Philosopher(philosopher_names[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]
    random.seed(883930)
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(100)
    Philosopher.running = False


if __name__ == '__main__':
    dining_philosophers()