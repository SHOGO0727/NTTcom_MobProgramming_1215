class Node(object):

  def __init__(self, idx, CPU, MEM):
    self.name = "HV%d" % idx
    self.C_h = CPU
    self.C_h_used = 0
    self.M_h = MEM
    self.M_h_used = 0
    self.vms = []

  # "HV1":[{"id":1,"cpu":4,"mem":4}]
  def __repr__(self):
    return "{},{}".format(
      self.name,self.vms
    )
    return "cpu:" + str(self.C_h) + ",memory:" + str(self.M_h)

  @property
  def cpu_usage(self):
    return self.C_h_used / self.C_h

  def is_available(self,cpu,memory):
    if (self.C_h - self.C_h_used) >= cpu and (self.M_h - self.M_h_used)>= memory:
      return True
    else:
      return False


  def assign(self,cpu,memory, idx):
    self.C_h_used += cpu
    self.M_h_used += memory
    vm = VM(idx, cpu, memory)
    self.vms.append(vm)

  def delete(self, idx):
    for delete_vm_id, vm in enumerate(self.vms):
      if vm.idx == idx:
        self.vms.pop(delete_vm_id)


  def is_allocated(self,idx):
    for vm in self.vms:
      if vm.idx == idx :
        return True
    return False


class VM(object):
  def __init__(self, idx, CPU, MEM):
    self.idx = idx
    self.cpu = CPU
    self.mem = MEM

  # {"id":1,"cpu":4,"mem":4}
  def __repr__(self):
    return '{"id":%d,"cpu":%d,"mem":%d}' % (self.idx, self.cpu, self.mem)

nodes = []


with open("./hv_list.csv", mode="r") as f:
  #C_h,M_h = f.readline().split(",")

  idx = 0
  while True:
    idx+=1
    line = f.readline()
    #print(line)
    if not line:
      break
    C_h,M_h = line.split(",")
    CPU_host = int(C_h)
    Mem_host = int(M_h)
    node = Node(idx, CPU_host, Mem_host)
    nodes.append(node)

print("input_reading")
# print(nodes)
vmid = 1
while True:
  #CPU_vm,Mem_vm = map(int,input().split(" "))
  line = input().split(" ")
  if line[0] == "create":
    CPU_vm,Mem_vm = int(line[1]),int(line[2])

    # print(CPU_vm,Mem_vm)
    nodes = sorted(nodes, key=lambda x: x.cpu_usage)
    print(nodes)
    for node in nodes:
      if node.is_available(CPU_vm,Mem_vm) :
        node.assign(CPU_vm,Mem_vm,vmid)
        vmid+=1
        print("OK")
        print("allocate to {}".format(node.name))
        break
    else:
      print("NG")
  elif line[0] == "delete":
    id_del = int(line[1])
    for node in nodes:
      if node.is_allocated(id_del):
        node.delete(id_del)

  elif line[0] == "list":
    for node in nodes:
      print(node)
