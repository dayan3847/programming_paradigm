# Task3: Collatz Conjecture

def collatz_conjecture(number, vervose=False):
    count = 1
    while number > 1:
        if vervose:
            print(number, end=' ')
        number = (number // 2) if number % 2 == 0 else (3*number+1)
        count += 1
    if vervose:
        print(number)
    return count

if __name__ == '__main__':
    print('Collatz Conjecture')
    number = int(input('Enter a number: '))
    count = collatz_conjecture(number, True)
    print(f'Count {count}')
