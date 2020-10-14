'''x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))
# or

x = lambda a, b, c: a * b * c
print(x(2, 4, 6))

def func(n):
    return lambda a : a * n
double = func(2)

print(double(10))

def func(n):
    return lambda a : a * n
function1 = func(3)
function2 = func(4)

print(function1(12))
print(function2(5))


cars = ['bmw', 'toyota', 'range']
x = len(cars)


print('_____________')

# using function
def average(classwork):
    return sum(classwork)/len(classwork)

average = lambda classwork: sum(classwork) / len(classwork)
students = [
    {'name': 'john', 'grade': (62, 89, 70, 38)},
    {'name': 'mary', 'grade': (90, 35, 33, 73)},
    {'name': 'cole', 'grade': (50, 65, 40, 52)},
]
for student in students:
    print(average(student['grade']))

    L - local
    E - Enclosed
    G - Global
    B - B

print('=====LEGB=====')
import builtins

print(dir(builtins))

m = max(10, 20, 30, 50)
m = min(10, 20, 30, 50)
print(m)

x = 'local x'  # global variable
def newSchool():
    global y
    y = 'local y'  # local variable
    print(x)
    print(y)

newSchool()
print(y)


def good(z):
    print(z)
good('good work')
# print(z)

def greet():
    print('Hello')
#greet()

good = greet
good()

def average():
    return sum(seq)/len(seq)'''

average = lambda seq: sum(seq)/len(seq)
top = lambda seq: max(seq)
total = lambda seq: sum(seq)

students = [
    {'name': 'john', 'grade': (62, 89, 70, 38)},
    {'name': 'mary', 'grade': (90, 35, 33, 73)},
    {'name': 'cole', 'grade': (50, 65, 40, 52)}
]
for student in students:
    name = student['name']
    grade = student['grade']
    print(f'student: {name}')
    operation = input("Enter 'average', 'total', or 'top': ")
    if operation == 'average':
        #print(student['name'], 'has an avg of', average(grade))
        print(average(grade))
    elif operation == 'total':
        #print(student['name'], 'has a total of', average(grade))
        print(total(grade))
    elif operation == 'top':
        #print(student['name'], 'has a maximum score of', average(grade))
        print(top(grade))
    else:
        print("Incorrect Input")

        #OR


        #print(exit())

#print(student(name))
#print(average)

'''good = lambda x, y: x+y
print(good(5, 6))'''