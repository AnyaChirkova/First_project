# -*- coding: utf-8 -*-
"""Копия блокнота "baseline.ipynb"

Original file is located at
    https://colab.research.google.com/drive/1ZtYNIYsxlCK5U8YbIc1Er7H4GI8KLuyE

# Угадай число
Нужно написать программу, которая угадывает число за минимальное число попыток.

## Условия соревнования
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».    
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.

Импортируем библиотеку, которая нам пригодится для генерации случайных чисел. В следующих темах вы познакомитесь с ней подробнее:
"""

import numpy as np

"""
## Функция для оценки

Эта функция необходима, чтобы определить, за какое число попыток программа угадывает наше число.
"""

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")



def game_core_v3(number: int = 1) -> int:
    """ Реализуем алгоритм половинного деления (бинарный поиск) для нахождения
    загаданного числа.
    Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    
    count = 0
    # границы поиска
    min_number = 1
    max_number = 101

    while min_number <= max_number:
      count += 1
      predict = (min_number+max_number)//2 # предполагаем, что загаданное число - среднее, между мах и min возможным.
#  в зависимости от того, больше или меньше загаданное число, изменяем границы поиска
      if predict < number:   
        min_number = predict+1
      elif predict > number:
          max_number = predict - 1
      else:
          return count

"""Оценим качество вашего алгоритма:"""

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

