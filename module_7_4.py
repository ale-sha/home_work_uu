team1 = "Мастера кода"
team2 = "Волшебники данных"
team1_num, team2_num = 5, 6
score_1, score_2 = 40, 42
team1_time, team2_time = 18015.2, 20491.6


print("В команде %s участников: %s!" % (team1, team1_num))
print("В команде %s участников: %s!" % (team2, team2_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

print("Команда {} решила задач: {}!".format(team1, score_1))
print("Команда {} решила задач: {}!".format(team2, score_2))
print("{} решили задачи за {}с!".format(team1, team1_time))
print("{} решили задачи за {}с!".format(team2, team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f"победа команды {team1}"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f"победа команды {team2}"
else:
    challenge_result = "ничья!"

print(f"Результат битвы: {challenge_result}!")

tasks_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = round(time_total/tasks_total, 1)

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

