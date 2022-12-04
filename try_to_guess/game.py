import numpy as np

def random_predict(number:int=1) -> int:
    """Guessing algorithm

    Args:
        number (int, optional): Picked number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0 # counter
    max_cur = 100 # the current upper bound of the range of the picked number
    min_cur = 1 # the current lower bound of the range of the picked number

    while True:
        count += 1
        predict_number = np.random.randint(min_cur, max_cur+1) # predict number adjusted for feedback
        if number < predict_number: max_cur = predict_number # current upper bound of the range of the picked number adjustment
        elif number > predict_number: min_cur = predict_number # current lower bound of the range of the picked number adjustment
        else:
            break # execution of the loop stop, if the picked number is guessed
    
    return(count)


def score_game(random_predict) -> int:
    """What is the average number of tries the algorithm needs to guess a picked each of 1000 numbers?

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of tries
    """
    count_ls = [] # list for saving of tries numbers
    np.random.seed(1) # fixing of seed
    random_array = np.random.randint(1, 101, size=(1000)) # list of picked numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # average number of tries

    print(f'Your algorithm guesses a picked number within: {score} tries')
    return(score)

#RUN
score_game(random_predict)
