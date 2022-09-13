# Task3: Collatz Conjecture

def collatz_conjecture_iterative(number):
    count = 0
    while number > 1:
        print(number, end=' ')
        number = (number // 2) if number % 2 == 0 else (3*number+1)
        count += 1
    print(number)
    return count


def collatz_conjecture_recursive(number):
    return 1


if __name__ == '__main__':
    print('Collatz Conjecture')
    number = int(input('Enter a number: '))
    count = collatz_conjecture_iterative(number)
    print(f'Count {count}')
