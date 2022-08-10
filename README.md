# Проект. Угадай число

## Оглавление  
[1. Описание проекта](#Описание-проекта)  
[2. Какой кейс решаем?](#Какой-кейс-решаем)  
[3. Краткая информация о данных](#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](#Этапы-работы-над-проектом)  
[5. Результат](#Результат)    
[6. Выводы](#Выводы) 


## Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

[:arrow_up:Оглавление](#Оглавление)


## Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


## Краткая информация о данных
В качестве входных данных используются условия задачи. 
Исходя из них диапазон угадывания ограничен областью от 1 до 100
Для генерации загадываемого числа используется модуль псевдослучайных чисел random
  
[:arrow_up:Оглавление](#Оглавление)


## Этапы работы над проектом  
Проект разбит на этапы:
1. Импорт модуля генератора псевдослучайных чисел
2. Использование модуля псевдослучайных чисел для генерации числа загадки
3. Задания начальной позиции для счетчика угадывания
4. Модуля угадывания
5. Вывода сообщения о результатах 
6. Создание модуля поиска среднего значения угадываний на 1000
7. В файлах:
7.1. game.py Первая часть задания - загадываем и угадываем число
7.2. game_average_value.py Вторая часть задания - Вычисляем среднее количество попыток угадывания на 1000
7.3. all_in_one.py Совмещенная версия первого и второго задания 


## Результаты:  
В качестве результата работы программы мы получаем сообщение о 
угаданном числе и количестве попыток угадывания, 
либо, в случае превышения количества попыток угадать число, 
сообщение об исперпании попыток угадывания

[:arrow_up:Оглавление](#Оглавление)


## Выводы:  
В практике работы над этой программой получены и применены знания по написанию программы на python 
и размещению кода и описательной части на gihub.com
Расширена практика применения PEP 8 в написании и оформлении кода

[:arrow_up:Оглавление](#Оглавление)


____
Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
