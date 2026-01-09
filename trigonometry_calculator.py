import math
import time

# "Fancy print"
def fprint(msg):
    time.sleep(0.25)
    print(msg)

# Main trigonometric functions, deg. mode
def sine(theta):
    fprint(math.sin(theta * math.pi / 180))

def cosine(theta):
    fprint(math.cos(theta * math.pi / 180))

def tangent(theta):
    fprint(math.tan(theta * math.pi / 180))

# Main program section
fprint("Trigonometry Calculator V1.0.0")

while True:
    fprint("Select Operator.") # Input
    time.sleep(0.25)
    a = int(input(""" 
1. Sine
2. Cosine
3. Tangent
Please input '1', '2' or '3'.
    """))

    b = int(input("Please input the chosen value."))
    if a == 1:
        sine(b)
    elif a == 2:
        cosine(b)
    elif a == 3:
        tangent(b)
    else:
        fprint("Interpret Error.")
