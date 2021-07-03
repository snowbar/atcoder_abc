class Employee_A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_sum(self):
        return self.a + self.b
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    
    def __lt__(self, other):
        return self.get_a() < other.get_a()

    def __gt__(self, other):
        return self.get_a() > other.get_a()
   
class Employee_B:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_sum(self):
        return self.a + self.b
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    
    def __lt__(self, other):
        return self.get_b() < other.get_b()

    def __gt__(self, other):
        return self.get_b() > other.get_b()
     
n = int(input())
employeeList_A = list()
employeeList_B = list()
for i in range(n):
    a, b = map(int, input().split())
    employeeList_A.append(Employee_A(a, b))
    employeeList_B.append(Employee_B(a, b))
    
employeeList_A.sort()
employeeList_B.sort()

sum_task = 2000000
for employee in employeeList_A:
    if sum_task > employee.get_sum():
        sum_task = employee.get_sum()

a_task = employeeList_A[0].get_a() 
min_b = 1000000
employeeList_A.pop(0)
for employee in employeeList_A:
    if min_b > employee.get_b():
        min_b = employee.get_b()
        
b_task = employeeList_B[0].get_b() 
min_a = 1000000
employeeList_B.pop(0)
for employee in employeeList_B:
    if min_a > employee.get_a():
        min_a = employee.get_a()

print(min(min(max(a_task, min_b),max(b_task,min_a)),sum_task))