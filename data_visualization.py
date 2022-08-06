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

    x = np.array(flight_num_list)
    y = np.array(flight_length_list)
    plt.scatter(x,y)
    
    return plt.show()
