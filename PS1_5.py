import matplotlib.pyplot as plt


class Solution:
    def __init__(self, target):
        self.answer = []
        self.target = target
        self.string = ''

    def Find_expression(self, s, pointer, path=''):
        if len(s) == 0 and pointer == self.target:
            self.answer.append(path)
        for i in range(len(s)):
            self.Find_expression(s[i + 1:], pointer + int(s[:i + 1]), path + '+' + s[:i + 1])
            self.Find_expression(s[i + 1:], pointer - int(s[:i + 1]), path + '-' + s[:i + 1])

    def __len__(self):
        count = 0
        for string in self.answer:
            if string[0] == '+':
                count += 1
        return count

    def __str__(self):
        for string in self.answer:
            if string[0] == '+':
                string = string[1:]
                print(string, end='=')
                print(eval(string))
        return ''


def get_key(dict, target):
    for item in dict.items():
        if item[1] == target:
            return item[0]


if __name__ == '__main__':
    target = int(input())
    total_solution = []
    a = Solution(target)
    a.Find_expression("123456789", 0)
    print('Possible Solutions:')
    print(a)
    print('Total number:%d' % len(a))

    # Question 2

    y_dict = {}
    for i in range(1, 101):
        a = Solution(i)
        a.Find_expression("123456789", 0)
        y_dict[i] = len(a)
    max_key = get_key(y_dict, max(y_dict.values()))
    min_key = get_key(y_dict, min(y_dict.values()))
    x = []
    y = []
    for key in y_dict.keys():
        x.append(key)
    for value in y_dict.values():
        y.append(value)
    plt.plot(x, y)
    plt.text(1, 26, 'Max(1,26)', color='r')
    plt.text(88, 6, 'Min(88,6)', color='r')
    plt.title('Distribution')
    plt.show()
