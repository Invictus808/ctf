#####
# File: program.py
# Copyright: 2020, Blaise Aranador
# Description: File contains the code to solve CTF Learn challenge 115.
#####
m = "0x41424354467B34354331315F31355F55353346554C7D"

m = bytearray.fromhex(m[2:]).decode()

print(m)
