class company:

    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        return f"Company Name: {self.company_name}"

class employee(company):
    def __init__(self,employee_name, company_name):
        self.employee_name = employee_name
        self.company_name = company_name

    def employee_info(self):
        response = company.info(self)
        print(f"The employee: {self.employee_name}, {response}")

class contractor(company):

    def __init__(self, contractor_name, company_name):
        self.contractor_name = contractor_name
        self.company_name = company_name
    
    def contractor_info(self):
        response = company.info(self)
        print(f"The contractor: {self.contractor_name}, {response}")

obj = employee("John Doe", "Tech Solutions")
obj.employee_info()

obj2 = contractor("lakhan", "Tech Solutions")
obj2.contractor_info()
