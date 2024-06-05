import functools


account = [
    {"login": "Daniil", "root": True, "sum": 1000},
    {"login": "Login", "root": False, "sum": 321},
    {"login": "Igor", "root": False, "sum": 500},
    {"login": "Harry", "root": True, "sum": 9100},
    {"login": "Obi", "root": False, "sum": 530},
    {"login": "Li", "root": False, "sum": 15},
]



def check_root(funciton):
    @functools.wraps(funciton)
    def wrapped(login):
        el = 0
        while el < 6:
            if login == account[el]["login"]:
                if  account[el]["root"] == False:
                    return "У Вас нету доступа"
            el += 1
        return funciton(login)
    return wrapped 

               


@check_root
def fun_print_sum(_login):
    el = 0
    sum = 0
    while el < 6:
        if _login == account[el]["login"]:
            sum = account[el]["sum"]
            return f"У вас на счет - {sum} рублей"
        el += 1
    return "Данный пользователь не найден"
    




login = input("Введите Ваш логин: ")

print(fun_print_sum(login))


