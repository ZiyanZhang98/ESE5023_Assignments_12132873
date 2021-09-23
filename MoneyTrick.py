import random


def least_move(n):
    count = 0
    while n % 2 == 0:
        n = n // 2
        count += 1
    if n == 1:
        return count
    count += 1
    count += least_move(n-1)
    return count


if __name__ == '__main__':
    number = random.randint(1, 101)
    print('We randomly generate a target number: %d' % number)
    print('Minimum operation time: %d' % least_move(number))
