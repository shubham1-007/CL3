import xmlrpc.server

def factorial(n):
  if n==0:
    return 1
  else:
    return n * factorial(n-1)

server=xmlrpc.server.SimpleXMLRPCServer(('localhost',8000))
server.register_function(factorial)
print("server started on port no 8000")
server.serve_forever()
    


