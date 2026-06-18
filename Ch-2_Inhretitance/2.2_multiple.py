class company:
    title:str = "consultancy"

    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        return f"Company Name: {self.company_name}"

class client_company:
    title:str = "client company"

    def __init__(self,client_company_name:str):
        self.client_company_name:str = client_company_name

    def info(self):
        print(f"Client Company Name: {self.client_company_name}")
        return f"Client Company Name: {self.company_name}"
    
class employee(company, client_company):
    def __init__(self, employee_name, company_name, client_company_name):
        self.employee_name = employee_name
        self.company_name = company_name
        self.client_company_name = client_company_name

    def info(self):
        response1 = company.info(self)
        response2 = client_company.info(self)
        print(f"The employee : {self.employee_name}, {response1},{response2}")
        return f"The employee: {self.employee_name},{response1}, {response2}"
    
obj = employee("Mohit","Accenture","DHL")
obj.info()