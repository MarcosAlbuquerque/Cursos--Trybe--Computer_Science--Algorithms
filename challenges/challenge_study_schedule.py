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
