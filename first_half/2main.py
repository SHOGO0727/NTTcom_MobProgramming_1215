print("input_reading")
with open("./hv_list.csv", mode="r") as f:
  C_h,M_h = f.read().split(",")
  CPU_host = int(C_h)
  Mem_host = int(M_h)
  print(CPU_host,Mem_host)
while True:
  CPU_vm,Mem_vm = map(int,input().split(" "))

  print(CPU_vm,Mem_vm)

  if CPU_vm <= CPU_host and Mem_vm <= Mem_host:
    print("OK")
    CPU_host = CPU_host - CPU_vm
    Mem_host = Mem_host - Mem_vm
  else:
    print("NG")
