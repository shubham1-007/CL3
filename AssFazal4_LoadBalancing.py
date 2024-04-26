class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_server_index = 0

    def get_next_server(self):
        server = self.servers[self.current_server_index]
        self.current_server_index = (self.current_server_index + 1) % len(self.servers)
        return server


num_server = int(input("Enter the no. of servers: "))
servers = []
for i in range(num_server):
    server_name = input("Enter name of server: ")
    servers.append(server_name)

lb = LoadBalancer(servers)

for i in range(int(input("Enter no. of request: "))):
    server = lb.get_next_server()
    print(f"Requests {i + 1} is handled by {server}")