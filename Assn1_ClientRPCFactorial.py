# import xmlrpc.client

# n = int(input("Enter an integer value: "))
# proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')
# result = proxy.factorial(n)
# print(f"The factorial of {n} is {result}")

import xmlrpc.client

n=int(input("Enter the int value: "))
proxy=xmlrpc.client.ServerProxy('http://localhost:8000')
result=proxy.factorial(n)
print(f'the factorial is {result}')
