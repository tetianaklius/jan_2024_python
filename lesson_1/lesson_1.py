#ДЗ

# strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4    #вивело в консолі.

input_str = input("Enter a string: ")

print(",".join([item for item in input_str if item.isdigit()]))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

print(",".join("".join([item if item.isdigit() else " " for item in input_str]).split()))

#################################################################################

# list comprehension

# 1)є рядок:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заголовним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

print([char.upper() for char in greeting])

# 2) з діапазону 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

print([num ** 2 for num in range(50) if num % 2])


# function

# - створити функцію яка виводить ліст


def show_list(some_list):
    print(some_list)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.


def find_max_num(num_1, num_2, num_3):
    max_num = max(num_1, num_2, num_3)
    print(max_num)
    return max_num


# - створити функцію, яка приймає будь-яку кількість чисел, повертає найменше, а виводить найбільше


def find_min_max_num(*args):
    print(max(args))
    return max(args)


# - створити функцію яка повертає найбільше число з ліста


def max_num_from_list(some_list):
    return max(some_list)


# - створити функцію яка повертає найменше число з ліста


def min_num_from_list(some_list):
    return min(some_list)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


def sum_of_list(some_list):
    return sum(some_list)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.


def average_of_list(some_list):
    return sum(some_list) / len(some_list)


# ################################################################################################
# 1)Дано list:
list_x = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - знайти мін. число
print(min(list_x))


#   - видалити всі дублікати


def del_duplicates(some_list):
    list_copy = some_list.copy()
    set_list = set(list_copy)
    return list(set_list)


print(del_duplicates(list_x))


#   - замінити кожне 4-те значення на 'X'


def num_to_x(some_list):
    print(["X" if not (i + 1) % 4 else num for i, num in enumerate(some_list)])


num_to_x(list_x)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції


def print_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")


print_square(10)


# 3) вивести табличку множення за допомогою циклу while


def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            print(f'{res:4}', end="")
            j += 1
        print()
        i += 1


multi_table()

# 4) переробити це завдання під меню

while True:
    print("1) знайти найменше число")
    print("2) видалити всі дублікати")
    print("3) замінити кожне 4-те значення на 'X'")
    print("4) вивести на екран пустий квадрат із '*', сторона якого вказана як агрумент функції")
    print("5) вивести табличку множення за допомогою циклу while")
    print("6) вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print(min(list_x))
    elif choice == "2":
        print(del_duplicates(list_x))
    elif choice == "3":
        num_to_x(list_x)
    elif choice == "4":
        print_square(10)
    elif choice == "5":
        multi_table()
    elif choice == "6":
        break
