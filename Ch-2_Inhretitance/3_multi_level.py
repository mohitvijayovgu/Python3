class company:

    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        return f"Company Name: {self.company_name}"

class manager(company):

    def __init__(self, manager_name):
        self.manager_name = manager_name

    def info(self):
        response = company.info(self)
        return(f"The manager: {self.manager_name}, {response}")


class employee(manager):
    def __init__(self, employee_name, company_name, manager_name):
        self.employee_name = employee_name
        self.company_name = company_name
        self.manager_name = manager_name

    def info(self):
        response = manager.info(self)
        return(f"The employee: {self.employee_name}, {response}")

obj = employee("Mohit Vijay","Amritha","Accenture")
print(obj.info())