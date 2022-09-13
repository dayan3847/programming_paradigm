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
        print('[1] print')
        print('[2] push')
        print('[3] pop')
        print('[other] exit')
        opcion = int(input('opcion: '))
        if 1 == opcion:
            print(stack)
        elif 2==opcion:
            element = int(input('Enter Element: '))
            print(f'Before Stack {stack}')
            push(stack, element)
            print(f'After Stack {stack}')
        elif 3==opcion:
            if 0<len(stack):
                print(f'Before Stack {stack}')
                element = pop(stack)
                print(f'Element {element}')
                print(f'After Stack {stack}')
            else:
                print('[3] pop')
        else:
            on = False #off
            print('Bye')
        input('Press Enter to continue...')
