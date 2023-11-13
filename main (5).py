import math
length = input('length= ')
length_unit = input('is that i or c= ')
length = float(length)
width = input('width= ')
width = float(width)
width_unit = input('is that i or c= ')
height = input('height= ')
height_unit = input('is that i or c= ')
height = float(height)

if (length_unit == 'c'):
  length = length / 2.54
if (width_unit == 'c'):
  width = width / 2.54
if (height_unit == 'c'):
  height = height / 2.54 
base = length * width 
print(f"base: {base}")
volume = (base * height) / 3
print(f"volume: {volume}")