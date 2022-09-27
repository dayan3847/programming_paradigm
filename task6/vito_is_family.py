# Task6: Vito’s Family

def cal_median(house_arr):
    house_arr.sort()
    median_index = int(len(house_arr) / 2)
    return house_arr[median_index]


def minimal_distance(house_arr):
    result = 0
    median = cal_median(house_arr)
    for h in house_arr:
        result += abs(h - median)

    return result


def get_house_list(input_string):
    result = []
    input_string_array = input_string.split()
    the_len = int(input_string_array[0])
    for y in range(1, the_len + 1):
        result.append(int(input_string_array[y]))
    return result


def validate_case(input_string):
    input_string_array = input_string.split()
    input_string_array_len = len(input_string_array)
    if 1 >= input_string_array_len:
        return False
    house_count = int(input_string_array[0])
    if 0 >= house_count or 500 <= house_count or input_string_array_len - 1 != house_count:
        return False
    for e in range(1, input_string_array_len):
        i_house = int(input_string_array[i])
        if 0 >= i_house or 30000 <= i_house:
            return False
    return True


if __name__ == '__main__':
    print('Task6: Vito’s Family')
    my_count = int(input('Enter the number of test cases: '))
    if 0 >= my_count:
        print('ERROR: Input Data')
        exit()
    my_inputs = []
    for i in range(1, my_count + 1):
        my_inputs.append(input(f'Case {i}: '))
    for i_input in my_inputs:
        if not validate_case(i_input):
            print('ERROR: Input Data')
            exit()
    houses = []
    for i_input in my_inputs:
        houses.append(get_house_list(i_input))
    print('Output:')
    for house in houses:
        print(minimal_distance(house))
