# Check other examples: https://github.com/pyscript/pyscript/blob/main/examples

# import math
import numpy as np
import random
from utils import add_class

# name = 'Brad' 
# print(name) 

# def getSum(x, y):
#     return x + y

# sum = getSum(5, 5)
# print(sum)

# using JS methods
# console.log(sum) 

# create a div
# pyscript.write('output', sum)
      
# use math
# pyscript.write('output', math.sqrt(10)) # 3.162277

# use numpy
arr = np.array([22, 58, 57, 87, 34, 5])
#pyscript.write('output', f"{arr}")

# JS way
output_el = Element("output").element
# console.log(output_el)
output_el.innerHTML = f"{arr}"

def shuffle_array(*args):
    #pyscript.write('output', 'Hello')
    shuffled = sorted(arr, key=lambda k: random.random())
    # pyscript.write('output', f"{shuffled}")
    output_el.innerHTML = f"{shuffled}"
    add_class(output_el, "text-blue-500")