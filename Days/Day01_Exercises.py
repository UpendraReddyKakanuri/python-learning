#Day01: Excersise practice

#1. Predict, then check

bool(0)          # False
bool("0")        # True
bool(0.001)      # True
bool(" ")        # True
bool(None)       # False
bool(False)      # False
bool("False")    # True
bool([])         # False

print(bool(0))
print(bool("0"))
print(bool(0.001))
print(bool(" "))
print(bool(None))
print(bool(False))
print(bool("False"))
print(bool([]))


#2. Convert and Calculate

pressure_text = "6.5"
count_text = "3"

pressure = float(pressure_text)
count = int(count_text)
pressure_int = int(pressure)

print(2*(pressure_int) + 1)
print(2*(pressure) + 1.0)
print(count + 1)


#3. CAN IDs from trace

can_id_1_text = "18F"
can_id_2_text = "7DF"

can_id_1 = int(can_id_1_text, 16)
can_id_2 = int(can_id_2_text, 16)

print(f"CAN ID {can_id_1} in decimal is 0x{can_id_1:X} in hex")
print(f"CAN ID {can_id_2} in decimal is 0x{can_id_2:X} in hex")


#4. Fix the zero trap

brake_pressure = 0.0

if brake_pressure:
    print("Pressure is received")
else:
    print("Pressure received: 0.0 bar")
if brake_pressure is not None:
    print("No pressure signal for None")

brake_pressure = 5.0

if brake_pressure:
    print("Pressure is received")
else:
    print("Pressure received: 0.0 bar")
if brake_pressure is not None:
    print("No pressure signal for None")

brake_pressure = 5.0

if brake_pressure:
    print("Pressure is received")
else:
    print("Pressure received: 0.0 bar")
if brake_pressure is None:
    print("No pressure signal for None")



###################
###  Results
###################
##   False
##   True
##   True
##   True
##   False
##   False
##   True
##   False
##   13
##   14.0
##   4
##   CAN ID 399 in decimal is 0x18F in hex
##   CAN ID 2015 in decimal is 0x7DF in hex
##   Pressure received: 0.0 bar
##   No pressure signal for None
##   Pressure is received
##   No pressure signal for None
##   Pressure is received
###################