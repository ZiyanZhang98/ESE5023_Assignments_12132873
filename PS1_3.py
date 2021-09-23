def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


def pascal_triangle(k):
    """
    Find nth row of the pascal triangle
    :param n:
    :return: a list of row nth of pascal triangle
    """
    length = k - 1
    mid = length//2
    row = []
    for i in range(mid+1):
        num = factorial(length)//(factorial(i)*factorial(length - i))
        row.append(num)
    if k % 2 == 0:
        row.extend(row[::-1])
    else:
        row.extend(row[1::-1])
    return row


if __name__ == '__main__':
    print(pascal_triangle(int(input())))

