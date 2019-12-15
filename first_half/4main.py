import csv
#16,16
#32,128
CPU_host = []
Mem_host = []

with open("./hv_list.csv") as f:
  reader = csv.reader(f)
  for r in reader:
    CPU_host.append(int(r[0]))
    Mem_host.append(int(r[1]))

print("CPU_host", CPU_host)
print("Mem_host", Mem_host)

while True:
  CPU_vm,Mem_vm = map(int,input().split(" "))
  print("CPU_vm", CPU_vm)
  print("Mem_vm", Mem_vm)

  #違う
  CPU_max = max(CPU_host)
  print("CPU_max", CPU_max)
  #

  CPU_max_index = CPU_host.index(CPU_max);
  print("CPU_max_index", CPU_max_index)

  if CPU_vm <= CPU_host[CPU_max_index] and Mem_vm <= Mem_host[CPU_max_index]:
    print("OK")
    print("allocate to HV"+str(CPU_max_index))
    CPU_host[CPU_max_index] -= CPU_vm
    Mem_host[CPU_max_index] -= Mem_vm
    print("CPU_host", CPU_host)
    print("Mem_host", Mem_host)
  else:
    print("NG")
