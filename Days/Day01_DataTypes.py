# Day 1: DataTypes, Conversion and True/False Values

#1. Types: Python picks the type from how you write the value

ecu_name = "EBS"      # Str: text
supply_voltage = 24.0 # float: number with a decimal point
dtc_count = 0         # int: whole number
abs_active = False    # bool: True or False
can_id = 0x18F        # int written in hex, like in a CAN trace
last_fault = None     # None: no value yet

print(type(ecu_name))
print(type(supply_voltage))
print(type(dtc_count))
print(type(abs_active))
print(type(can_id))
print(type(last_fault))
print(f"CAN ID {can_id} in decimal is 0x{can_id:X} in hex")

#2. Conversion: values from files and logs arrive as text
voltage_text = "27.5"
voltage = float(voltage_text)
print(voltage_text + " V")
print(voltage + 0.5)
print(f"voltage is {voltage} V")

#3. True/False values: what does Python treat as False
print(bool(0), bool(0.0), bool(""), bool(None))
print(bool(-1), bool(6.5), bool("0"), bool("EBS"))

#4. The trap: 0.0 is a real reading, not a missing one
wheel_speed = 0.0
if wheel_speed:
    print("Wheel Speed is received")
else:
    print("No Wheel Speed")
if wheel_speed is not None:
    print(f"wheel speed received: {wheel_speed} km/h")

###################
###  Results
###################
##   <class 'str'>
##   <class 'float'>
##   <class 'int'>
##   <class 'bool'>
##   <class 'int'>
##   <class 'NoneType'>
##   CAN ID 399 in decimal is 0x18F in hex
##   27.5 V
##   28.0
##   voltage is 27.5 V
##   False False False False
##   True True True True
##   No Wheel Speed
##   wheel speed received: 0.0 km/h
####################