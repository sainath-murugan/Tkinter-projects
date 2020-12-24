"""def func1(name):
  return f"hello {name}"

def func2(name):
  return f"{name},what r u doing?"

def func3(func4):
  return func4("sainath")

def ex():
    print("fool")
def func5(sai):
    return sai()
print(func5(ex))
print(func3(func1))
print(func3(func2))
"""

##strings
'''print('sainath\'s computer')
print("sai's")
print("\"python\" was more popular")
print('py\nth\to\0n')
print("sainath\tmurugan")
print("sainath\bmurugan")
print("sainath\\murugan")
print("sainath murugan\b \b \b")
print(type("sai"))
print("sainath".find("ai"))
print("sainath".replace("sai","ram"))
print("sainath".capitalize())
print("SAINATH".lower())
print("sai".isalnum())
print("7876".isdigit())
print("sai".isidentifier())
print("sai".isalpha())
print("sai".isprintable())
print("425".isprintable())
print("123".isdecimal())
print("Sainath And Arjuna".istitle())
print("SAI".isupper())
print("sai".islower())
print("sai".isspace())
print(" ".isspace())'''

'''c = "g"
print("The ASCII value of'"+ c +"'is",ord(c))
k = "greater"
print("the value of 10 is "+k+"")'''


##factorial number
'''n = int(input("enter the number"))
i = 1
fact= 1
while(i<=n):
     fact = fact*i
     i = i+1
print(fact)
print(i)'''

##sum of n numbers
"""n = int(input("enter the number:"))
sum = 0
i = 1
while(i<=n):
    sum = sum+i
    i = i+1
print(sum)
print(i)"""

##prime number or not
"""n = int(input("enter the number"))
if(n%2 == 0):
    print("the number not is prime number")
else:
    print("it is a prime number")"""


## swapping of two variable
"""a = int(input("enter a value"))
b = int(input("enter b value"))

temp = a
a = b
b = temp

print("the value of a is:{}".format(a))
print("the value of b is:{}".format(b))"""

"""x = 4
y = 2
if not 1+1 == y or x == 4 and 7 == 8:
    print ("s")
elif x>y:
    print("no")"""


## febonocci series
'''terms = int(input("enter the values"))
a = 0
b = 1
count = 1
if terms < 0:
   print("enter a positive number")
if terms == 0:
   print("enter a positive number")
while(count <= terms):
    print(a)
    c = a + b
    a = b
    b = c
    count = count + 1'''

"""if not True:
    print("1")
elif not(1+1 == 3):
    print("2")
else:
    print("3")"""

"""def func(word):
  print(word + "?")
func("what")"""

"""def hello():
    print("hai")
hello()"""


##normal function
"""def add(x,y):
    print(x+y)
add(1,3)"""

##lambda function

"""add = lambda x,y: print(x+y)
add(1,3)"""


"""a = [333,44,22,56,76,31,45,89]
final_list = list(filter(lambda x : (x%2==0),a))
print(final_list)"""

"""import json
json_obj = '{"name":"sainath.M, "class":"ECE","age":18}'
python_obj = json.loads(json_obj)
print(python_obj)
print("\n Name:", python_obj["name"])
print("class:", python_obj["class"])
print("age:", python_obj["age"])""" ## doubt program

"""import heapq as si
num = [22,67,44,56,34,78,90]
print(num)
largest_number = si.nlargest(3,num) 
print("\n largest number are :",largest_number)  ## to find largest number"""

"""import heapq as hq
def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h,value)
    return[hq.heappop(h) for i in range(len(h))]
print(heapsort([1,34,56,87,354,767,2,0,]))"""         ##arranging number in order


"""import heapq as hq
num = [23,45,34,56,768,3434,9]
print(num)
smallest_nums = hq.nsmallest(3,num)
print( "the smallest number are:",smallest_nums)"""

'''import heapq as hq
raw_heap = [23,54,67,54,465,86]
print("raw heap",raw_heap)
hq.heapify(raw_heap)
print(raw_heap)'''  #no idea


#tkinter

from tkinter import *

"""root = Tk()

class function:
    def button(self):
        label = Label(root, text= "you clicked it")
        label.pack()
s1 = function()
a = Label(root, text = "hai")
b = Button(root, text = "click me", padx= 10, command = s1.button, fg = "blue")
a.pack()
b.pack()
root.mainloop()"""


root = Tk()
entry  =Entry(root, width = 100, borderwidth = 10 )
entry.pack()
entry.insert(0,"enter your name")
class function:
    def button(self):
        label = Label(root, text= entry.get())
        label.pack()
s1 = function()
b = Button(root, text = "click me", padx= 10, command = s1.button, fg = "blue")

b.pack()
root.mainloop()



