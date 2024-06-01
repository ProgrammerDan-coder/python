import os
import random

print("Здравствуйте. Хотите сыграть в игру 'Кто хочет стать миллионером'?")
score = 0

enter_or_exit = input("Хотите играть? Да или Нет: ")

if enter_or_exit == "Да":


    questions = [
        {"question": "2 * 2 = ?", "answer": [["2", False], ["8", False], ["4", True], ["0", False]]},
        {"question": "31 * 10 = ?", "answer": [["10", False], ["310", True], ["410", False], ["130", False]]},
        {"question": "(15 * 15 ) / 5 = ?", "answer": [["15", False], ["200", False], ["100", False], ["45", True]]},
        {"question": "Столица Канады - ?", "answer": [["Оттава", True], ["Минск", False], ["Вашингтон", False], ["Нью-Йорк", False]]},
        {"question": "Столица Бразилии - ?", 
        "answer": [["Бразилиа", True], ["Рио-де-Жанейро", False], ["Мексика", False], ["Нью-Йорк", False]]},
        {"question": "Статическая или динамическая типизация лучше - ?", 
        "answer": [["Статическая", False], ["Динамическая", False], ["В зависимости", True], ["Обе плохи", False]]},
        {"question": "Дата образования речи посполитой - ?", 
        "answer": [["1885", False], ["1991", False], ["1000", False], ["1569 ", True]]},
        {"question": "Год основания Минска - ?", "answer": [["1000", False], ["1991", False], ["1067 ", True], ["981", False]]},
        {"question": "Факториал из 5 = ?", "answer": [["5", True], ["100", True], ["90", False], ["120", True]]},
        {"question": "Что тяжелее: 1 кг или 1 литор  - ?",
        "answer": [["Одиноково", True], ["1 литор", False], ["1 кг", False], ["Не знаю", False]]},
    ]

    hint = {1: 'Звонок другу', 2: '50/50'}

    i = 0 
    next_answer = 0
    a = 0
    score = 1
    break_out_flag = False

    os.system('cls')
    while i < 10: 
        a = 0
        print("Вопрос номер ", + i + 1, ": " + questions[i]["question"])
        
        print(" A) ", questions[i]["answer"][next_answer][0])
        print(" B) ", questions[i]["answer"][next_answer + 1][0])
        print(" C) ", questions[i]["answer"][next_answer + 2][0])
        print(" D) ", questions[i]["answer"][next_answer + 3][0])
        
        #нужно написать не вариант ответа, а сам ответ
        answer_input = input("Ваш ответ (если хотите воспользоваться подсказкой, введите  help): ") 
        print("\n")
        if answer_input == "help":
            print("Доступные подсказки:")

            for key, value in hint.items():
                print(key, " - ", value )

            print("\n")
            help_key = int(input("Какую подсказку Вы хотите использовать? "))
            help_key = hint.pop(help_key, "Нету подсказки")

            if help_key == "Звонок другу":
                friend_help = random.randint(1, 4)
                print("Я думаю, что ответ: ", friend_help )

            elif help_key == "50/50":
                print("Мы думаем, что ответ: ", random.randint(1,4) , "или ", random.randint(1,4))

            else:
                print("Данной подсказки нету")

        else:
            while a < 4:
                if questions[i]["answer"][a][0] == answer_input:
                    if questions[i]["answer"][a][1] == True:
                        print("Правильно!")
                        score = score + i + 1
                    else:
                        print("К сожалению Вы не угадили")
                        break_out_flag = True
                        break
                a += 1
            if break_out_flag:
                break
            i += 1
else:
    print("До свидания.")
print("Количество очков: ", + score)