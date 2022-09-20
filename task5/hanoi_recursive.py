# Task5: Hanoi Recursive

def hanoi_recursive_move(src, dst, aux, count):
    if count > 0:
        hanoi_recursive_move(src, aux, dst, count - 1)
        print(f'Move element "{count}" from column "{src}" to column "{dst}"')
        hanoi_recursive_move(aux, dst, src, count - 1)


if __name__ == '__main__':
    print('Task5: Hanoi Recursive')
    my_count = int(input('Enter the number of items we want to move: '))
    if 1 <= my_count:
        hanoi_recursive_move('A', 'B', 'C', my_count)
