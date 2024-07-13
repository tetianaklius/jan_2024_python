# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання
from typing import Callable


def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_todos() -> list[str]:
        nonlocal todo_list
        for item in todo_list:
            print(f'-- {item}')
        return todo_list.copy()

    return [add_todo, get_todos]


add_todo, get_todos = notebook()
add_todo("some todo")
add_todo("something else")
add_todo("something more")
get_todos()

print("*****")

# 3) створити функцію котра буде повертати суму розрядів числа у вигляді строки (також використовуємо типізацію)
# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


def expanded_form(num: int) -> str:
    def get_the_rest_str() -> str:
        res = ""
        j = 1
        for i in range(1, len(str(num))):
            res += f'{f' + {str(num)[i]}{("0" * (len(str(num)) - (j + 1)))}' if not (str(num)[i] == "0") else ""}'
            j += 1
        return res

    return (
            f'{num} = ' +
            f'{num // int(f'1{"0"*(len(str(num)) - 1)}')}{"0" * (len(str(num)) - 1)}' +
            get_the_rest_str()
    )


n = expanded_form(32)
print(n)
# 3 digits
n = expanded_form(322)
print(n)
n = expanded_form(350)
print(n)
n = expanded_form(302)
print(n)
# 4 digits
n = expanded_form(3555)
print(n)
n = expanded_form(3550)
print(n)
n = expanded_form(3500)
print(n)
n = expanded_form(3055)
print(n)
n = expanded_form(3050)
print(n)
n = expanded_form(3005)
print(n)
n = expanded_form(3000)
print(n)
# 5 digits
n = expanded_form(70304)
print(n)
n = expanded_form(72304)
print(n)
n = expanded_form(70005)
print(n)
# x digits
n = expanded_form(13555555512)
print(n)

print("*****")


# ---------------> added part
# ex. 3 mentor version

# def expanded_form(num: int) -> str:
#     st = str(num)
#     length = len(st) - 1
#     res = []
#     for i, ch in enumerate(st):
#         if ch != "0":
#             res.append(ch + "0" * (length - i))
#     return f"{' + '.join(res)} = {st}"

# ---------------> the end of added part

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій


def counter(func: Callable) -> Callable[[], int]:
    count = 0

    def inner():
        nonlocal count
        count += 1
        func()
        print(f'count = {count}\n*')
        return count

    return inner


@counter
def func_1():
    print("hello 1")


@counter
def func_2():
    print("hello 2")


func_1()
func_2()
func_1()
func_2()
func_1()
func_2()
