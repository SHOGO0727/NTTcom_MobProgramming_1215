print("input_reading")
with open("./input", mode="r") as f:
  line = f.read().split(" ")
#line = input().split(" ")#1:r 2:b
m = int(line[-1])
print("m =", m)#4

a_array = []
s_array = []
for ch in line[:-2]:#1:r 2:b
    a,s = ch.split(":")#1 r 2 b
    a_array.append(int(a)) #a_array <- a
    s_array.append(s) #s_array <- s

flag = False
for i in range(len(a_array)):
  if m % a_array[i] == 0:
    flag = True
    print(s_array[i], end="")

print(a_array, s_array)
print(m)
