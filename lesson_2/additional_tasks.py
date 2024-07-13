# вивести послідовність Фібоначі, кількість вказана в змінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
from operator import countOf


def show_fib_seq(x: int) -> None:
    seq = []
    for i in range(x):
        if len(seq) > 1:
            num = seq[i-1] + seq[i-2]
        else:
            num = 1
        seq.append(num)
    print(seq)


show_fib_seq(10)

# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
x = 225688
y = 33294


def count_odd_even(some_num: int) -> list[int]:
    odd = 0
    even = 0
    for digit in str(some_num):
        if int(digit) % 2:
            odd += 1
        elif not (int(digit) % 2):
            even += 1
    print(f"even = {even}; odd = {odd}")
    return [even, odd]


count_odd_even(x)
count_odd_even(y)


#прога, що виводить кількість кожного символа з введеної строки,
  # наприклад:
st = 'as 23 fdfdg544' #введена строка
  # 'a' -> 1  #вивело в консолі
  # 's' -> 1
  # ' ' -> 2
  # '2' -> 1
  # '3' -> 1
  # 'f' -> 2
  # 'd' -> 2
  # 'g' -> 1
  # '5' -> 1
  # '4' -> 2


def count_chars(some_string: str) -> None:
    res_dict = {}
    for char in some_string:
        res = 1
        index = some_string.index(char)
        for other_char in some_string[index + 1:]:
            if other_char == char:
                res += 1
            res_dict[char] = res
    for item in res_dict.items():
        print(f"{item[0]} -> {item[1]}")


count_chars(st)

# генеруємо список із непарних чисел у порядку зростання [1,3,5,7,9.....n]
# потрібно зробити з нього список списків на зразок:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]


def create_list_of_odds(length: int) -> list[int]:
    res_list: list[int] = []
    for integer in range(length * 2 + 1):
        if integer % 2:
            res_list.append(integer)
    return res_list


def create_list_of_lists(some_list: list[int]) -> list[list[int]]:
    res_list: list[list[int]] = []
    while len(some_list) > 0:
        j = 0
        while len(some_list):
            new_list = some_list[0:1+j]
            res_list.append(new_list)
            del some_list[0:j+1]
            j += 1
    return res_list


print(create_list_of_lists(create_list_of_odds(11)))
print(create_list_of_lists(create_list_of_odds(30)))


# знайти в списку тільки унікальні числа
# приклад [1,2,3,4,2,5,1] => [ 3, 4, 5 ]

xx = [1, 2, 3, 4, 2, 5, 1]

# v1


def get_unique(some_list: list[int]) -> list[int]:
    res_list: list[int] = []
    for item in some_list:
        if countOf(some_list, item) == 1:
            res_list.append(item)
    return res_list


print(get_unique(xx))

# v2


def get_unique_2(some_list: list[int]) -> list[int]:
    res_list: list[int] = []
    for item in some_list:
        res = 1
        index = some_list.index(item)
        for other_numb in some_list[index + 1:]:
            if other_numb == item:
                res += 1
        if res == 1:
            res_list.append(item)
    return res_list


print(get_unique_2(xx))
