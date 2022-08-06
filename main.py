import time
import random
import psycopg2

# CONNECT TO DATABASE
def connect_db():
    try:
        conn = psycopg2.connect(database="airport", user='postgres', password='0167174jg', host='127.0.0.1', port= '5432')
        return(conn)
    except psycopg2.Error:
        return("Failed to connect to DB")

class Flight:
    def __init__(self, flight_length, pilot, curr_time, flight_num, flight_origin, flight_destination):
        self.flight_length = flight_length
        self.pilot = pilot
        self.flight_land_time = flight_length + curr_time
        self.flight_num = flight_num
        self.flight_origin = flight_origin
        self.flight_destination = flight_destination
        

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

# CREATES FLIGHT
def flight_occurs(curr_time, pilot_name, id_for_flight, flight_origin, flight_destination):
    new_flight = Flight(random.randint(0, 5), pilot_name, curr_time, id_for_flight, flight_origin, flight_destination) 
    flight_list.append(new_flight)
    print(curr_time, ": TAKE-OFF: Flight_id", id_for_flight, "\n    Pilot:", pilot_name,"\n    Flight_length:", new_flight.flight_length,
    "\n    Flight_land_time:", new_flight.flight_land_time)
    return new_flight.flight_length + curr_time

def assign_pilot(cursor, employee_id):
    cursor.execute("SELECT pilot_name FROM PILOT WHERE employee_id = %(employee_id)s", {"employee_id": employee_id} )
    pilot = cursor.fetchall()
    pilot = ''.join(pilot[0])
    pilot = pilot.strip("()',")
    return pilot

def get_flight_num(cursor, flight_index):
    cursor.execute("SELECT flight_num FROM flight")
    flight_num = cursor.fetchall()
    flight_num = ''.join(flight_num[flight_index])
    flight_num = flight_num.strip("()',")
    return flight_num

def get_flight_origin(cursor, flight_index):
    cursor.execute("SELECT origin FROM flight")
    flight_origin = cursor.fetchall()
    flight_origin = ''.join(flight_origin[flight_index])
    flight_origin = flight_origin.strip("()',")
    return flight_origin

def run_airport(days, curr_time, cursor):
    employee_id = 352
    flight_index = 99

    while days > 0:
    # START OF DAY
        flight_occured = False
        landing_occured = False
        time.sleep(speed_of_time)

        flight_percent_chance = random.randint(0, 10) #NUMBER OF GUESSES
# FLIGHT TAKES OFF
        if (if_flight(flight_percent_chance)):
            # PILOT
            pilot_for_flight = assign_pilot(cursor, employee_id)
            employee_id = employee_id - 1
            # FLIGHT_NUM
            flight_num = get_flight_num(cursor, flight_index)
            # FLIGHT_ORIGIN
            flight_origin = get_flight_origin(cursor, flight_index)
            # FLIGHT_DESTINATION
            flight_destination = get_flight_origin(cursor, flight_index)
            # MOVES TO THE NEXT ROW OF DATA
            flight_index = flight_index - 1 

# CREATES FLIGHT
            flight_occurs(curr_time, pilot_for_flight, flight_num, flight_origin, flight_destination)
            flight_occured = True #CHECK LOGIC HERE

# FLIGHT LANDS
        for x in range(0, len(flight_list), 1):
            # print(curr_time, " and ", flight_list[x].flight_land_time)
            if curr_time == flight_list[x].flight_land_time:
                print(curr_time, ":" ,"LANDING: Flight_id", flight_list[x].flight_num, " landed at ", flight_list[x].flight_land_time)
                landing_occured = True

        if nor(flight_occured, landing_occured):
            print(curr_time, ":")

        curr_time = curr_time + 1

# ENDS CYCLE
        if ((days * 24) + 1 == curr_time): 
            days = 0

    print("Total flights:", len(flight_list))


curr_time = 0
speed_of_time = 1
flight_list = []
conn = connect_db()
cursor = conn.cursor()
# days = input("How many days of flights would you like to observe: ")
# STUCK TO 12 HOURS FOR TESTING
days = 0.5 

run_airport(days, curr_time, cursor)