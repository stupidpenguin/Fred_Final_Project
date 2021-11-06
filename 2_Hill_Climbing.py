import numpy as np

def get_schedule_length(given_array):
    # Adjust the given_array (schedule), for example [A, B, C] -> [A, B, C, A]
    # then compute the travel distance of the given array.
    given_array = np.append(given_array, given_array[0])
    sum = 0
    for j in range(len(given_array)-1):
        sum += Test_Adjacency_Matrix[given_array[j],given_array[j+1]]
    return sum

def Hill_Climbing(best_schedule,
                  best_result,
                  HC):
    for i in range(100):
        for j in range(1000):  # try 1000 possible route in each iteration. (much less than 15!)
            current_schedule = np.random.permutation(best_schedule)
            if (get_schedule_length(current_schedule) < best_result):
                best_schedule = current_schedule
                best_result = get_schedule_length(current_schedule)
        HC.append(best_result)
    return best_schedule, HC