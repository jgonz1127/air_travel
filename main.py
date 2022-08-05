import time
import random

curr_time = 0
speed_of_time = 1

class Flight:
    def __init__(self, flight_length):
        self.flight_length = flight_length

# EXPAND object WITH DATA BASE SUCH AS flight_id, num_passengers etc...
def NOR(a, b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0

def if_flight(flight_percent_chance):
    list_of_guesses = []
    number_to_guess = random.randint(1, 10) #IF guessed then flight occurs
    while flight_percent_chance > 0: #GENERATES GUESSES
        guesses = random.randint(1, 10)
        list_of_guesses.append(guesses)
        flight_percent_chance = flight_percent_chance - 1

#CHECKS if guessed
    if number_to_guess in list_of_guesses:
        # print(number_to_guess, " was found in ", list_of_guesses)
        return True
    else:
        # print("No match found ", number_to_guess, " and ", list_of_guesses)
        return False


def flight_occurs(curr_time):
    print(curr_time, ":" ,"TAKE-OFF: Flight_id", id(new_flight), "with a length of", new_flight.flight_length)
    return new_flight.flight_length + curr_time

# days = input("How many days of flights would you like to observe: ")

# STUCK TO 12 HOURS FOR TESTING
days = 0.5 

while days > 0:
# START OF DAY
    flight_occured = False
    landing_occured = False

    time.sleep(speed_of_time)

    flight_percent_chance = random.randint(0, 10) #NUMBER OF GUESSES
    if (if_flight(flight_percent_chance)): #FLIGHT OCCURS
        # CREATE FLIGHT flight(flight_length)
        new_flight = Flight(random.randint(0, 5)) 
        flight_land_time = flight_occurs(curr_time)
        flight_occured = True

# FLIGHT LANDING TIME
    if flight_occured and (curr_time ==  flight_land_time):
        print(curr_time, ":" ,"LANDING: Flight_id", id(new_flight), " landed at ", flight_land_time)
        landing_occured = True

    if NOR(flight_occured, landing_occured):
        print(curr_time, ":")

    curr_time = curr_time + 1
# ENDS CYCLE
    if ((days * 24) + 1 == curr_time): 
        days = 0