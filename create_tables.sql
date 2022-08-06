drop 
  table if exists PILOT;
drop 
  table if exists FLIGHT;
drop 
  table if exists AIRCRAFT;
drop 
  table if exists BOOKED_ON;
drop 
  table if exists PLANE_TYPE;
drop 
  table if exists CUSTOMER;
drop 
  table if exists DEPARTURE;
drop 
  table if exists EMPLOYEE;
drop 
  table if exists ASSSIGNED_TO;

CREATE TABLE EMPLOYEE (
  employee_id INT NOT NULL, 
  employee_name VARCHAR(50) NOT NULL, 
  salary INT NOT NULL, 
  PRIMARY KEY (employee_id)
);

CREATE TABLE PILOT (
  employee_id INT NOT NULL, 
  pilot_name VARCHAR(50) NOT NULL, 
  license_date VARCHAR(20) NOT NULL, 
  plane_model_can_fly VARCHAR(10) NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id)
);

CREATE TABLE PLANE_TYPE (
  model_number VARCHAR(20) NOT NULL, 
  manufacturer VARCHAR(20) NOT NULL,
  PRIMARY KEY (model_number)
);

CREATE TABLE FLIGHT (
  flight_num INT NOT NULL, 
  origin VARCHAR(3) NOT NULL, 
  dest VARCHAR(3) NOT NULL, 
  dep_date VARCHAR(20) NOT NULL,
  dep_time VARCHAR(5) NOT NULL, 
  arr_time VARCHAR(5) NOT NULL, 
  PRIMARY KEY (flight_num)
);

CREATE TABLE AIRCRAFT (
  serial_number VARCHAR(5) NOT NULL, 
  model_number VARCHAR(4) NOT NULL, 
  FOREIGN KEY (model_number) REFERENCES PLANE_TYPE(model_number),
  PRIMARY KEY (serial_number)
);

CREATE TABLE BOOKED_ON (
  customer_name VARCHAR(25) NOT NULL, 
  departure_date VARCHAR(25) NOT NULL, 
  flight_num  INT NOT NULL,
  FOREIGN KEY (flight_num) REFERENCES FLIGHT(flight_num)
);

CREATE TABLE PASSNGER (
  first_name VARCHAR(25) NOT NULL, 
  last_name VARCHAR(25) NOT NULL, 
  street VARCHAR(20) NOT NULL, 
  city VARCHAR(20) NOT NULL, 
  p_state CHAR(2) NOT NULL, 
  zip_code INT NOT NULL, 
  id VARCHAR(12) NOT NULL, 
  PRIMARY KEY(id)
);

CREATE TABLE DEPARTURE (
  Departure_Date CHAR(11) NOT NULL, 
  Flight_Number INT NOT NULL, 
  Aircraft_serial_no VARCHAR(5)
);

CREATE TABLE ASSSIGNED_TO (
  employee_id INT NOT NULL, 
  flight_num INT NOT NULL,
  FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id),
  FOREIGN KEY (flight_num) REFERENCES FLIGHT(flight_num)
);

