# ###
# def create_server(name, weight):
#     return {"name": name, "weight": weight}

# def create_load_balancer(servers):
#     return {"servers": servers, "current_index": 0}

# def add_server(load_balancer, server):
#     load_balancer["servers"].append(server)

# def get_next_server(load_balancer):
    # next_server = load_balancer["server"][load_balancer["current_index"]]
#     load_balancer["current_index"] = (load_balancer["current_index"] + 1) % len(load_balancer["servers"])
#     return next_server

# def prompt_server_info(index):
#     name = input("Enter the name of server " + str(index) + ": ")
#     weight = int(input("Enter the weight of server " + str(index) + ": "))
#     return create_server(name, weight)

# def assign_load(load_balancer, i):
#     next_server = get_next_server(load_balancer)
#     print("Load", i, "assigned to server:", next_server["name"])

# if __name__ == "__main__":
#     servers = []
#     num_servers = int(input("Enter the number of servers: "))
#     for i in range(1, num_servers + 1):
#         servers.append(prompt_server_info(i))

#     lb = create_load_balancer(servers)
#     # print(lb)
#     # {'servers': [{'name': 's1', 'weight': 1}, {'name': 's2', 'weight': 2}], 'current_index': 0}

#     num_loads = int(input("Enter the number of loads: "))

#     print("\nLoad balancing result:")
#     for i in range(1, num_loads + 1):
#         assign_load(lb, i)


def create_server(name,weight):
  return {"name":name, 'weight':weight}

def create_load_balancer(servers):
  return {"servers":servers,"curr_Idx":0}

def get_next_server(load_balancer):
  next_server=load_balancer['servers'][load_balancer['current_Idx']]
  load_balancer['current_Idx']=((load_balancer['current_Idx']+1) % len(load_balancer['servers']))
  return next_server

def prompt_server_info(index):
  name=input("Enter the name of server "+str(index)+": ")
  weight=input("Enter the weight for server "+str(index)+": ")
  create_server(name,weight)

def assign_load(load_balancer,i):
  next_server=get_next_server(load_balancer)
  print("load "+i+" is assigned to server "+next_server)

if __name__ =='__main__':
  servers=[]
  num_server=int(input("Enter the no of servers :"))
  for i in range(1,num_server+1):
    servers.append(prompt_server_info(i))
    
  lb=create_load_balancer(servers)
  num_loads = int(input("Enter the number of loads: "))

  print("\nLoad balancing result:")
  for i in range(1, num_loads + 1):
    assign_load(lb, i)
  

  