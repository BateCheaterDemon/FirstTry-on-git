# 继承类的学习

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id=id
    
    def print_info(self):
        print(f"员工名字:{self.name}，工号：{self.id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, id ,monthly_salary):
        super().__init__(name, id)
        self.monthly_salary=monthly_salary
    
    def calculate_monthly_pay(self):
        return self.monthly_salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, id, dayly_salary):
        super().__init__(name, id)
        self.dayly_salary=dayly_salary

    def caculate_monthly_pay(self,work_days):
        return self.dayly_salary*work_days
    
Zhangsan=FullTimeEmployee("Zhangsan",18,6000)
print(Zhangsan.calculate_monthly_pay())

Lisi=PartTimeEmployee("Lisi",56,300)
print(Lisi.caculate_monthly_pay(31))

Zhangsan.print_info()
Lisi.print_info()
    
