def study_schedule(permanence_period, target_time):
    counter = 0
    if not isinstance(target_time, int):
        return None
    for value1, value2 in permanence_period:
        if not isinstance(value1, int) or not isinstance(value2, int):
            return None

        if value1 <= target_time <= value2:
            counter += 1

    return counter


# counter {2: 4, 1: 2, 3: 1, 5: 3, 4: 2}

# Nos arrays temos 6 estudantes

# estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
# target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
# target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
# target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
# target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.
# target_time = ""
# Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
# study_schedule(permanence_period, target_time)
