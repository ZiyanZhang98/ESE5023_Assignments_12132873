def flowchart(a, b, c):
    if a > b:
        if b > c:
            print('%s, %s, %s' % (a, b, c))
            return 0
        else:
            if a > c:
                print('%s, %s, %s' % (a, c, b))
                return 0
            print('%s, %s, %s' % (c, a, b))
    else:
        if b > c:
            if a > c:
                print('%s, %s, %s' % (a, c, b))
                return 0
            print('%s, %s, %s' % (c, a, b))
            return 0
        print('%s, %s, %s' % (c, b, a))
        return 0


if __name__ == '__main__':
    flowchart(1, 2, 3)
    flowchart(1, 3, 2)
    flowchart(2, 3, 1)
    flowchart(2, 1, 3)
    flowchart(3, 2, 1)
