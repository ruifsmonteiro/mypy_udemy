
from func_sayhello import *
"""
age = 30

print(age)
fun()
"""
"""
from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)
"""

x = 6 #997
def check_prime(number):
  
  if(number < 0):
    raise ValueError('please enter a positive number')

  if(not isinstance(number,int)):
     raise ValueError('please enter an integer number')
  
  if(number == 0 or number == 1 or number == 2):
    is_prime = True
    return is_prime
  
  is_prime = None
  for i in range(2,number):
    if((number % i) == 0):
      #print(i, ': prime condition violated')
      is_prime = False
      break
    else:
      #print(i, ': prime condition not violated')
      is_prime = True
  return is_prime

#print('x:', check_prime(x))


ctr = 0
n = 10
for i in range(n+1):  
  print(i, ':', check_prime(i))
  if(check_prime(i)):
    #print(i, ':', check_prime(i))
    ctr += 1

print('number of primes:', ctr)  
    
    
  


# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-68.php
"""
def count_Primes_nums(n):
    ctr = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

print(count_Primes_nums(10))
print(count_Primes_nums(100))


x = range(6)
for n in x:
  print("range",n)
"""