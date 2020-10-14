class work:
    def __init__(self, age):
        self.age = age


name = ['John', 'Ahmed']
print(name.__class__)
print('paul'.__class__)

good = work(22)
print(good.age)


class School:
    def __init__(self):
        self.course = []

    def __len__(self):  # to get the length/amount of items
        return len(self.course)

    def __getitem__(self, item):  # to get a particular item
        return self.course[item]

    def __repr__(self):  # to print a content with a string
        return f'School{self.course}'

        # OR

    def __str__(self):
        return f'School with {len(self.course)} courses'


cs = School()


cs.course.append('HTML')
cs.course.append('JS')
cs.course.append('PYTHON')
cs.course.append('PHP')

print(len(cs))
print(cs[1])
print(cs)

for x in cs:
    print(x)

num = 1
for x in cs:
    print(f'{num} is {x}')
    num += 1
