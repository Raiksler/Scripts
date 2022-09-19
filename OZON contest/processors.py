# Энергоэффективное распределение нагрузки на процессоры. Пусть дано несколько процессоров. Пусть дан ряд задач, которые необходимо обработать.
# Задачи приходят "на исполнение" в разные моменты времени. Один процессор в одну единицу времени способен выполнять лишь оду задачу.
# Каждый процессор обладает своим коэффицентом энергоэфективности, показателем, отражающим то, сколько энергии тратит этот процессор за единицу времени выполнения задачи.
# Расход энергии в момент простоя не учитывается. При поступлении задачи, программа назначает ее обработку свободному процессору с наименьшим энергопотреблением.
# По обработке всех задач, выводится показатель "израсходованной энергии"
# Скрипт оптимизирован для использования с PyPy и способен эффективно обрабатывать данные при сверхвысоких нагрузках.
# Входные данные:
# 1-я строка - количество процессоров и количество задач в формате cpu_num task_num (через пробел)
# 2-я строка - коэффицент энергопотребления  для каждого процессора в формате first second third.... и т.д (через пробел)
# 3-я + строки - момент времени, в который приходит задача и количество времени, необходимое на ее выполнение в формате first second (через пробел)

utility_row = input().split()                    # Прием первой строчки
machines_num = int(utility_row[0])
tasks_num = int(utility_row[1])
machines_performance = input().split()

def machine_choise(mach):                                   # Выбор наименее энергозатратной машины для обработки задачи
    for item in mach:
        if item[2] == 0:
            return mach.index(item)
    return None                              # Возникает, если нет свободных машин


def planner():                                          # Выделение процессоров под задачи + временная шкала
    time = 0
    time_old = 0
    task_complete = 0
    tasks = list()
    machines = list()
    energy_counter = 0
    i = 0
    while i < machines_num:
        machines.append([i, int(machines_performance[i]), 0])
        i += 1
        machines = sorted(machines, key=lambda x: x[1])
    i = 0
    while i < tasks_num:
        tasks.append(list(map(int, (input().split()))))
        i += 1

    while task_complete < tasks_num:
        if time == 0:
            time = tasks[0][0]
            time_old = time
        if len(tasks) == 0:
            break
        if tasks[0][0] == time:
            best_cpu_id = machine_choise(machines)
            try: 
                energy_counter += tasks[0][1] * machines[best_cpu_id][-2]
                machines[best_cpu_id][-1] = tasks[0][1]
                del tasks[0]
            except TypeError:
                del tasks[0]
                task_complete += 1
                continue
        try:
            time = tasks[0][0]
        except IndexError:
            break
        i = 0
        while i < len(machines):                                           # ex time_processing
            if machines[i][-1] > 0:
                machines[i][-1] -= time - time_old
                if machines[i][-1] < 0:
                    machines[i][-1] = 0
                    task_complete += 1
            i += 1
        time_old = time
    return energy_counter

result = planner()
print(result)