class Node(object):

  def __init__(self, idx, CPU, MEM):
    self.name = "HV%d" % idx
    self.C_h = CPU
    self.C_h_used = 0
    self.M_h = MEM
    self.M_h_used = 0

  def __repr__(self):
    return "name:{}, cpu:{}, memory:{}, cpu_usage:{}, id:{}".format(
      self.name, self.C_h, self.M_h, self.cpu_usage, id(self)
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

  def assign(self,cpu,memory):
    self.C_h_used += cpu
    self.M_h_used += memory

nodes = []

print("input_reading")
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

# print(nodes)

while True:
  CPU_vm,Mem_vm = map(int,input().split(" "))
  # print(CPU_vm,Mem_vm)
  nodes = sorted(nodes, key=lambda x: x.cpu_usage)
  print(nodes)
  for node in nodes:
    if node.is_available(CPU_vm,Mem_vm) :
      node.assign(CPU_vm,Mem_vm)
      print("OK")
      print("allocate to {}".format(node.name))
      break
  else:
    print("NG")
