#zigzag

print("k.trisha,USN:1AY24AI051,SEC:M")

lines=9
max_spaces = lines
for i in range(lines):
 if i <=max_spaces:
   spaces = i
else:
   spaces = lines-i-1
print(" " *spaces+ "*"*8)