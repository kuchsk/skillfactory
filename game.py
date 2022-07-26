# Зададим Диапазон угадывания (с миллионом интереснее)
range = 100

import random
# Импортируем модуль псевдо случайности

# Создаем функцию для ее последующего вызова согласно условию задания
def function():

# Загадываем число
  riddle_number = random.randint(1,(range + 1))

# Показываем загаданное число (Чтобы все было честно :) )
  print(f'Загаданное число: {riddle_number}')

# Задаем начальную позицию счётчика угадываний
  count = 0

#Задаем искомое число равное половине диапазона угадывания
  desired_number = range/2

# Задаем шаг деления равный половине остатка диапазона
  division_step = desired_number/2

# Задаем количество попыток угадывания - не более 20 согласно условию задачи
  while count < 20:

# Проверим условие: загаданное больше половины диапазона угадывания 
    if riddle_number > desired_number: 

# Сообщим об этом 
      print(f'{riddle_number} больше {int(desired_number)}, прибавим {int(division_step)}')

# Изменим диапазон сравнения
      desired_number = int(desired_number) + int(division_step)

# Минимальный шаг не должен быть меньше единицы, мы ищем целое число
      if division_step > 1:

# Обновляем диапазон дробления
        division_step = int(division_step/2)
      else: division_step = 1

# Засчитываем попытку угадывания
      count += 1

# Проверим условие: загаданное меньше половины диапазона угадывания
    elif riddle_number < desired_number: 

# Сообщим об этом 
      print(f'{riddle_number} меньше {int(desired_number)}, вычтем {int(division_step)}')
      desired_number = int(desired_number) - int(division_step)

# Минимальный шаг не должен быть меньше единицы, мы ищем целое число
      if division_step > 1:

# Обновляем диапазон дробления
        division_step = int(division_step/2)
      else: division_step = 1

# Засчитываем попытку угадывания
      count += 1

# Если мы угадали число, сообщим об этом    
    else:
      return (f'Это число {desired_number}. Число попыток: {count}') 

# И выйдем из цикла
      break
      return

# Если количество попыток превысит 20, сообщим об этом    
  if count >= 20:
    return ('Исчерпаны попытки угадывания')

# Вызываем функцию согласно условию задания
function()
