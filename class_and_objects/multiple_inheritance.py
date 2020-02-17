"""
Problem Defination:
Three types of employee Manager, Consultant, SalesPerson.
Three Types of payment policy SalaryPolicy, HourlyPolicy, CommissionPolicy, CommissionPolicy Inherited From
SalaryPolicy other two are unique.

Manager get payment according to SalaryPolicy,
Consultant get payment according to HourlyPolicy,
and SalesPerson get payment according to CommissionPolicy.
"""
class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Manager(Employee, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)


class Consultant(Employee, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked=hours_worked, hour_rate=hour_rate)
        super().__init__(id, name)


class SalesPerson(Employee, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)

    def total_yearly_salary(self):
        total = self.weekly_salary + self.commission
        return total * 12


m = Manager('10', 'sharif', 10000)
print(m.calculate_payroll())

c = Consultant('11', 'hanif', 20, 50)
print(c.calculate_payroll())

s = SalesPerson('12', 'kanan vai', 10000, 20)
print(s.calculate_payroll())

print("Total Yearly Salary:", s.total_yearly_salary())
