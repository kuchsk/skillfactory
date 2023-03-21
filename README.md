# ЗАДАНИЕ 9.11. МОДУЛЬ 13 (HW-01)


## ЗАДАНИЯ

#### 9.1. Каково соотношение ушедших и лояльных клиентов? Покажите это на графике и дайте комментарий по соотношению.

#### 9.2. Постройте график, показывающий распределение баланса пользователей, у которых на счету больше 2 500 долларов. Опишите распределение и сделайте выводы.

#### 9.3. Посмотрите на распределение баланса клиента в разрезе признака оттока. Как различаются суммы на накопительном счёте ушедших и лояльных клиентов? Подумайте и напишите, с чем это может быть связано, что может не устраивать ушедших клиентов в банке.

#### 9.4. Посмотрите на распределение возраста в разрезе признака оттока. В какой группе больше потенциальных выбросов? На какую возрастную категорию клиентов стоит обратить внимание банку?

#### 9.5. Постройте график, который показывает взаимосвязь кредитного рейтинга клиента и его предполагаемой зарплаты. Добавьте расцветку по признаку оттока клиентов. Какова взаимосвязь между признаками? Если не видите явной взаимосвязи, укажите это.

#### 9.6. Кто чаще уходит, мужчины или женщины? Постройте график, который иллюстрирует это.
Подсказка

#### 9.7. Как отток клиентов зависит от числа приобретённых у банка услуг? Для ответа на этот вопрос постройте многоуровневую столбчатую диаграмму.

#### 9.8. Как влияет наличие статуса активного клиента на отток клиентов? Постройте диаграмму, иллюстрирующую это. Что бы вы предложили банку, чтобы уменьшить отток клиентов среди неактивных?

#### 9.9. В какой стране доля ушедших клиентов больше? Постройте тепловую картограмму, которая покажет это соотношение на карте мира. Предположите, с чем это может быть связано.

#### 9.10. Переведите числовой признак CreditScore в категориальный. Для этого воспользуйтесь функцией get_credit_score_cat(), которая приведена ниже. Примените её к столбцу CreditScore и создайте новый признак CreditScoreCat — категории кредитного рейтинга.

##### def get_credit_score_cat(credit_score):
##### if credit_score >= 300 and credit_score < 500:
#####    return "Very_Poor"
##### elif credit_score >= 500 and credit_score < 601:
#####     return "Poor"
##### elif credit_score >= 601 and credit_score < 661:
#####     return "Fair"
##### elif credit_score >= 661 and credit_score < 781:
#####     return "Good"
##### elif credit_score >= 781 and credit_score < 851:
#####     return "Excellent"
##### elif credit_score >= 851:
#####     return "Top"
##### elif credit_score < 300:
#####     return "Deep"
        
Постройте сводную таблицу, строками которой являются категории кредитного рейтинга (CreditScoreCat), а столбцами — количество лет, в течение которых клиент пользуется услугами банка (Tenure). В ячейках сводной таблицы должно находиться среднее по признаку оттока (Exited) — доля ушедших пользователей.

На основе полученной сводной таблицы постройте тепловую карту с аннотацией. Найдите на тепловой карте категории клиентов, которые уходят чаще всего.



### → В файле должно содержаться 10 графиков — 10 ответов к заданиям.

### → Каждый график и преобразования к нему выполняются в отдельной ячейке.

### → Под графиком вы должны предоставить свой ответ на вопрос по нему и, если это требуется, выводы, которые вы можете сделать, исходя из графика.



### Загружаем исходные данные, источник открыт и авторизации не требует
import pandas as pd ...
### Продолжение в файле https://github.com/kuchsk/skillfactory/blob/main/ЗАДАНИЕ_9_11_МОДУЛЬ_13_(HW_01).ipynb


[:arrow_up:ЗАДАНИЯ](#ЗАДАНИЯ)


____
Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами

