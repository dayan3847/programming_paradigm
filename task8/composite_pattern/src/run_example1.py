# Task8: Composite Pattern

if __name__ == '__main__':




    print('Collatz Conjecture')
    numbers_string = input('Enter two numbers separated by space: ')
    numbers = numbers_string.split()
    if 2 != len(numbers):
        print('error')
    else:
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        number = -1
        max = -1
        for i in range(n1, n2 + 1):
            count = collatz_conjecture(i)
            if count > max:
                max = count
                number = i
        print(f'{n1} {n2} {max} number: ({number}) ')
