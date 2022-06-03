def list_max(input_list):
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    return max_value


list1 = [-2, 1, 2, -10, 22, -10]
max_value = list_max(list1)
print(max_value)

list2 = [-20, 123, 112, -10, 22, -120]
max_value = list_max(list2)
print(max_value)
