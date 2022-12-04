import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число / Guessing algorithm

    Args:
        number (int, optional): Picked number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0 # counter
    max_cur = 100 # текущая верхняя граница диапазона загаданного числа / the current upper bound of the range of the picked number
    min_cur = 1 # текущая нижняя граница диапазона загаданного числа / the current lower bound of the range of the picked number

    while True:
        count += 1
        predict_number = np.random.randint(min_cur, max_cur+1) # предполагаемое число c поправкой на обратную связь / predict number adjusted for feedback
        if number < predict_number: max_cur = predict_number # учет обратной связи для корректировки верхней границы возможного диапазона / current upper bound of the range of the picked number adjustment
        elif number > predict_number: min_cur = predict_number # учет обратной связи для корректировки нижней границы возможного диапазона / current lower bound of the range of the picked number adjustment
        else:
            break # execution of the loop stop, if the picked numbe is guessed
    
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм / What is the average number of tries the algorithm needs to guess a picked each of 1000 numbers?

    Args:
        random_predict ([type]): функция угадывания / guessing function

    Returns:
        int: среднее количество попыток / average number of tries
    """
    count_ls = [] # список для сохранения количества попыток / list for saving of tries numbers
    np.random.seed(1) # фиксируем сид для воспроизводимости / fixing of seed
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел / list of picked numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток / average number of tries

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток') #Your algorithm guesses a picked number within ... tries
    return(score)

#RUN
score_game(random_predict)
