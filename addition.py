import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("Sum: ", add(num1, num2))
    else:
        x = 10
        y = 20
        print("Sum: ", add(x, y))