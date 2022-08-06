from inspect import currentframe
import matplotlib.pyplot as plt
import numpy as np

def average_flight_length(flight_list):
    total = 0
    for x in range(0, len(flight_list), 1):
        total = total + (flight_list[x].flight_length)
    return (total / len(flight_list))

def graph_flight_times(flight_list):
    flight_length_list = []
    flight_num_list = []
    
    for x in range(0, len(flight_list), 1):
        flight_length_list.append(flight_list[x].flight_length)
    for x in range(0, len(flight_list), 1):
        flight_num_list.append(flight_list[x].flight_num)

    plt.xlabel("Flight_num")
    plt.ylabel("Flight_length")
    x = np.array(flight_num_list)
    y = np.array(flight_length_list)
    plt.scatter(x,y)
    
    return plt.show()

daily_avg_flight_length = []
day_list = []
def graph_num_flight_per_day(flight_list, days,current_day):
    total = 0
    for x in range(0, len(flight_list), 1):
        # CALCUALTE DAILY AVERAGE
        total = total + (flight_list[x].flight_length)

    daily_avg_flight_length.append(total / len(flight_list))
    day_list.append(current_day)

    plt.xlabel("day")
    plt.ylabel("avg_flight_length")
    x = np.array(day_list)
    y = np.array(daily_avg_flight_length)

    if days == current_day:
        plt.bar(x,y)
        return(plt.show())
