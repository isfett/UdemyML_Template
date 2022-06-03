from typing import List


def list_max(input_list: List[int | float]) -> int | float:
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    return max_value


def list_min(input_list: List[int | float]) -> int | float:
    min_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] < min_value:
            min_value = input_list[i]

    return min_value


def main():
    list1 = [-2, 1, 2, -10, 22, -10]
    print(list_max(list1))
    print(list_min(list1))
    list2 = [-20, 123, 112, -10, 22, -120]
    print(list_max(list2))
    print(list_min(list2))

    print(list_max([0.5, 1]))


if __name__ == "__main__":
    main()
