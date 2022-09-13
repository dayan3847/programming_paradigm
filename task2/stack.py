# Task2: Stack

def push(stack, element):
    stack.append(element)

def pop(stack):
    element= stack[-1]
    del stack[-1]
    return element

if __name__ == '__main__':

    print('Stack')
    stack = [2,7,9,4]
    on = True
    while on:
        print('Options')
        print('[1] print')
        print('[2] push')
        print('[3] pop')
        print('[other] exit')
        option = int(input('option: '))
        if 1 == option:
            print('Printing...')
            print(stack)
        elif 2==option:
            print('Pushing...')
            element = int(input('Enter Element: '))
            print(f'Before stack {stack}')
            push(stack, element)
            print(f'After stack {stack}')
        elif 3==option:
            print('Pop...')
            if 0<len(stack):
                print(f'Before stack {stack}')
                element = pop(stack)
                print(f'Element {element}')
                print(f'After stack {stack}')
            else:
                print('Empty stack')
        else:
            on = False #off
            print('Bye')
        input('Press Enter to continue...')
