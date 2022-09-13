# Task2: Queue

def enqueue(queue, element):
    queue.append(element)

def dequeue(queue):
    element= queue[0]
    del queue[0]
    return element

if __name__ == '__main__':

    print('Queue')
    queue = []
    on = True
    while on:
        print('Options')
        print('[1] print')
        print('[2] enqueue')
        print('[3] dequeue')
        print('[other] exit')
        option = int(input('option: '))
        if 1 == option:
            print('Printing...')
            print(queue)
        elif 2==option:
            print('Enqueueing...')
            element = int(input('Enter Element: '))
            print(f'Before queue {queue}')
            enqueue(queue, element)
            print(f'After queue {queue}')
        elif 3==option:
            print('Dequeueing...')
            if 0<len(queue):
                print(f'Before queue {queue}')
                element = dequeue(queue)
                print(f'Element {element}')
                print(f'After queue {queue}')
            else:
                print('Empty queue')
        else:
            on = False #off
            print('Bye')
        input('Press Enter to continue...')