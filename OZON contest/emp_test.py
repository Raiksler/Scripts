# Оценка производительности сотрудника. Дано некоторое число сотрудников. Дано некоторое число задач для каждого сотрудника, которые он выполняет в течении дня. У каждой задачи есть уникальный номер.
# Скрипт проверяет, "отвлекается" ли сотрудник от выполнения той или иной задачи, переключаясь на другую, чтобы в последствии снова вернуться к первой задачи.
# Для каждого сотрудника выводится NO или YES, в зависимости от того, прошел сотрудник проверку или нет.
# Входные данные:
# 1-я строка - количество наборов данных (сотрудников)
# Следующие строки - наборы данных, состоящие из двух строк:
# 1-я строка - количество задач, которые сотрудник выполняет в течении дня
# 2-я строка - id задач, выполняемых сотрудником в формате first_id second_id third_id third_id... и т.д

days = int(input())
i = 0
result = []
     
def uniq_task_checker(ids):
    unic_task = set()
    prev_task = None
    for item in ids:
        if item in unic_task and item != prev_task:
            return 'NO'
        elif item not in unic_task:
            unic_task.add(item)
        prev_task = item
    return 'YES'
     
while i < days:
    task_num = int(input())
    task_ids = input().split()
    result.append(uniq_task_checker(task_ids))
    i += 1
for item in result:
    print(item)