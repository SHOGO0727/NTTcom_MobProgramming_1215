import csv

CPU_host = []
Mem_host = []

with open("./hv_list.csv") as f:
  reader = csv.reader(f)
  for r in reader:
    # r[0] must be cpu_host
    CPU_host.append(int(r[0]))
    Mem_host.append(int(r[1]))

print("CPU_host", CPU_host)
print("Mem_host", Mem_host)

while True:
  CPU_vm,Mem_vm = map(int,input().split(" "))
  print("CPU_vm", CPU_vm)
  print("Mem_vm", Mem_vm)
  for i in range(len(CPU_host)):
    if CPU_vm <= CPU_host[i] and Mem_vm <= Mem_host[i]:
      print("OK")
      print("allocate to HV"+str(i+1))
      CPU_host[i] -= CPU_vm
      Mem_host[i] -= Mem_vm
      print("CPU_host", CPU_host)
      print("Mem_host", Mem_host)
      break
    else:
      if i == len(CPU_host)-1:
        print("NG")
