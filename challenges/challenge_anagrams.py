from collections import defaultdict


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    letters_counted1 = letter_counter(first_string.lower())
    letters_counted2 = letter_counter(second_string.lower())

    return letters_counted1 == letters_counted2


def letter_counter(word):
    letter_counter = defaultdict(int)

    for l in word:
        letter_counter[l] += 1

    return letter_counter


# references
# https://app.betrybe.com/course/computer-science/introducao-a-python/aprendendo-python/
# https://docs.python.org/pt-br/3/library/collections.html#collections.defaultdict
# https://www.geeksforgeeks.org/defaultdict-in-python/
