print("input_reading")
with open("./hv_list.csv", mode="r") as f:
  C_h,M_h = f.read().split(",")

print(C_h,M_h)

C_v,M_v = input().split(" ")

print(C_v,M_v)

if C_v <= C_h and M_v <= M_h:
  print("OK")
else:
  print("NG")
