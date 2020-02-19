#####
# File: program.py
# Copyright: 2020, Blaise Aranador
# Description: File contains the code to solve CTF Learn challenge 120.
#####
e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

# n ** 1 is always n
m = c

# Convert integer to binary
m = bin(m)[2:]

# Prepend 0's to the front of binary string
# Binary string must be a multiple of 8 bits (1 byte)
# ASCII characters are 1 byte
while len(m) % 8 != 0:
	m = '0' + m

# Convert binary string to hexidecimal string
m = hex(int(m, 2))

# Convert hexidecimal string to ASCII string
m = bytearray.fromhex(m[2:]).decode()

print(m)
