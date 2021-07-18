def print_max(x, y):
    '''打印两个数值中的最大的数


    这两个数应该是整数'''
    # 如果可能，将其转换为整数类型
    x =int(x)
    y =int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
