from calendar import c


#CREDIT CARD CLASS
class credit_card:
    def __init__(self,card_number,expiration_date,security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code

    

account = credit_card(input("card_number: "),input("expiration_date: "),input("security_code: "))
print("{} with a security code {} expiring {} ".format(account.card_number,account.security_code,account.expiration_date))

#NO.2
class animal:
    def __init__(self):
        print("Animal is ready")
    def whoisThis(self):
        print("animal")

class dog(animal):
    def __init__(self):
        super().__init__()
        


    def whoisThis(self):
       return"Dog"

    def bark(self):
        print("bark loud")   


pet = dog()
pet.bark()

#no.3
class Queue:
    def __init__(self):
       print("list")
       
       
list_1 = list()
maximum = 5

def isEmpty():
        return len(list_1) == 0    



def isFull():
        return len(list_1) == "maximum"

def enqueue(element):
    if not isFull():
        list_1.insert(0,element)
        return list_1
    else:
        return 'list is already full'


def dequeue():
    if not isEmpty():
        list_1.pop()
        return list_1

    else:
        return 'yo the list is already empty'

def display(f):
    print(f)

display(enqueue(6))
display(enqueue(7))
display(enqueue(8))
display(enqueue(9))
display(enqueue(10))
display(isFull())
display(enqueue(1))

# no.4
class Stack:
    def __init__(self):
        self.stack = list()

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            return ("stack empty")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.size())

#no.5
class person:
    def __init__(self,name,address,age,):
        self.name = name
        self.age = age
        self.address = address

    
     # instance method
    def eat(self, food):
        return "{} is eating".format(self.name, food)

    # instance method
    def sleep(self,bed):
        return "{} is  sleeping".format(self.name,bed)
    def work(self,job):
        return "{} is  working".format(self.name,job)
# instantiate the object
print("first person")
first = person(input("name: "),input("age: "),input("address: "))
print("second person")
second = person(input("name: "),input("age: "),input("address: "))
print("third person")
third = person(input("name: "),input("age: "),input("address: "))


# access the instance methods
print(first.sleep("Happy"))
print(second.work("Happy"))
print(third.eat("Happy"))


#no.6
class Employee:
    def __init__(self, name, age, salary):
         self.name = name
         self.age = age
         self.address = salary

    
     
    def eat(self, food):
        return "{} is eating".format(self.name, food)

  
    def sleep(self,bed):
        return "{} is  sleeping".format(self.name,bed)
    def work(self,job):
        return "{} is  working".format(self.name,job)

print("first person")
first = person(input("name: "),input("age: "),input("address: "))
print("second person")
second = person(input("name: "),input("age: "),input("address: "))
print("third person")
third = person(input("name: "),input("age: "),input("address: "))

print(first.sleep("Happy"))
print(second.work("Happy"))
print(third.eat("Happy"))

class Programmer(Employee):
    def __init_subclass__(self) -> None:
        return super().__init_subclass__()
    
    def program(self):
        print("Uses programming language")

dan = Programmer()
dan.program()

