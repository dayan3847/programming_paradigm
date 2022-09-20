# Task5: Palindrome Recursive

def palindrome_recursive(word):
    return 1 >= len(word) or (word[0] == word[-1] and palindrome_recursive(word[1:-1]))


if __name__ == '__main__':
    print('Task5: Palindrome Recursive')
    my_word = input('Enter a Word: ')
    is_palindrome = palindrome_recursive(my_word)
    if is_palindrome:
        print('\033[92m' + f'The word "{my_word}" is a palindrome')
    else:
        print('\033[91m' + f'The word "{my_word}" is not a palindrome')
