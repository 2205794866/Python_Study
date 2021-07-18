x = 50


def func(x):
    print("x is", x)
    x = 2
    print("chaned local x to", x)


func(x)
print("x is still", x)
