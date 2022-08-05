import time
import random
import psycopg2

curr_time = 0
speed_of_time = 1
flight_list = []

# CONNECT TO DATABASE
def connect_db():
    try:
        conn = psycopg2.connect(database="airport", user='postgres', password='0167174jg', host='127.0.0.1', port= '5432')
        return("DB_Connection Sucess", conn)
    except:
        return("Failed to connect to DB")

class Flight:
    def __init__(self, flight_length, pilot):
        self.flight_length = flight_length
        self.pilot = pilot

# EXPAND object WITH DATA BASE SUCH AS flight_id, num_passengers etc...
def nor(a, b):
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

def flight_occurs(curr_time, new_flight, pilot_name):
    flight_list.append(id(new_flight))
    print(curr_time, ":" ,"TAKE-OFF: Flight_id", id(new_flight), "\nPilot:", pilot_name,"\nFlight_length:", new_flight.flight_length)
    return new_flight.flight_length + curr_time

employee_id = 352
def assign_pilot(cursor, employee_id):
    cursor.execute("SELECT pilot_name FROM PILOT WHERE employee_id = %(employee_id)s", {"employee_id": employee_id} )
    pilot = cursor.fetchall()
    return(pilot)


db = connect_db()
conn = db[1]
cursor = conn.cursor()
# days = input("How many days of flights would you like to observe: ")
# STUCK TO 12 HOURS FOR TESTING
days = 0.5 

def run_airport(days, curr_time, cursor):
    while days > 0:
    # START OF DAY
        flight_occured = False
        landing_occured = False

        time.sleep(speed_of_time)

        flight_percent_chance = random.randint(0, 10) #NUMBER OF GUESSES
        if (if_flight(flight_percent_chance)): #FLIGHT OCCURS
            # CREATE FLIGHT flight(flight_length)
            pilot_for_flight = assign_pilot(cursor, employee_id)
            new_flight = Flight(random.randint(0, 5), pilot_for_flight) 
            flight_land_time = flight_occurs(curr_time, new_flight, pilot_for_flight)
            flight_occured = True

    # FLIGHT LANDING TIME
        if flight_occured and (curr_time ==  flight_land_time):
            print(curr_time, ":" ,"LANDING: Flight_id", id(new_flight), " landed at ", flight_land_time)
            landing_occured = True

        if nor(flight_occured, landing_occured):
            print(curr_time, ":")

        curr_time = curr_time + 1
    # ENDS CYCLE
        if ((days * 24) + 1 == curr_time): 
            days = 0

    print("Total flights:",len(flight_list))

run_airport(days, curr_time, cursor)