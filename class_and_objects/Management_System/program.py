from class_and_objects.Management_System import productivity
from class_and_objects.Management_System.employees import (SalaryEmployee,
                                                           HourlyEmployee,
                                                           CommissionEmployee,
                                                           Manager, Secretary, SalesPerson, FactoryWorker)
from class_and_objects.Management_System.hr import PayrollSystem

# salary_employee = SalaryEmployee(id=1, name='Sharif', weekly_salary=10000)
# hourly_employee = HourlyEmployee(id=2, name='Kanan vai', hours_worked=20, hour_rate=200)
# commission_employee = CommissionEmployee(id=2, name='Shakil vai vai', weekly_salary=15000, commission=500)
#
# payroll_system = PayrollSystem().calculate_payroll([salary_employee, hourly_employee, commission_employee])


manager = Manager(1, 'Mary Poppins', 3000)
secretary = Secretary(2, 'John Smith', 1500)
sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = FactoryWorker(2, 'Jane Doe', 40, 15)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)