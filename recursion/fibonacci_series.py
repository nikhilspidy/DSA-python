def fib(number):
    if number == 1:
        return 1

    if number == 0:
        return 0

    return fib(number - 1) + fib(number - 2)


if __name__ == '__main__':
    print("Enter number : ")
    number = int(input())
    print(fib(number))


