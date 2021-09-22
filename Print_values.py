def flowchart(a, b, c):
    if a > b:
        if b > c:
            print(a + ',' + b + ',' + c)
        else:
            if a > c:
                print(a + ',' + c + ',' + b)
            print(c + ',' + a + ',' + b)
    else:
        if b > c:
            if a > c:
                print(a + ',' + c + ',' + b)
            print(c + ',' + a + ',' + b)
        print(c + ',' + a + ',' + b)


if __name__ == '__main__':
    # a = input()
    # b = input()
    # c = input()
    # flowchart(1, 2, 3)
    # flowchart(3, 2, 1)
    a = [1, 2, 3]
