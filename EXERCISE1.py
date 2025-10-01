class Employee:
    def __init__(self,employeeId,employeeName):
        self.id=employeeId
        self.name=employeeName
        self.baseSalary=0
        self.grossSalary=0
        self.tax=0
        self.bonus=0
        self.type = "employee"
        self.deduction=0


    def setBaseSalary(self,salary):
        self.baseSalary=salary

    def setbonus(self):
        pass



    def calculateGrossPay(self):
        self.grossSalary = self.baseSalary + self.bonus
        print(f"Base Salary:{self.baseSalary} \nBonus:{self.bonus}\nGross salary:{self.grossSalary}")
        return self.grossSalary


    def deductiontax(self):
        self.tax=0
        self.pensionfund = self.grossSalary*9//100
        y=self.grossSalary
        if y>4000:
            self.tax+=(y-4000)*20//100
            y=4000
        if 1001<y<4000:
            self.tax+=(y-1000)*10//100
            y=1000
        self.deduction=self.tax+self.pensionfund
        print(f"Tax is { self.tax}\nPensionfund is {self.pensionfund}\nTotal deduction is {self.deduction}")
        return self.tax

    def calcNetPay(self):
        self.netPay=self.grossSalary-self.tax-self.pensionfund
        print(f"Final get after tax:{self.netPay}")

    def displayDetails(self):
        print(f"My id is {self.id}, My name is {self.name} , I am a {self.type}")

class SalariedEmployee(Employee):

    def calculateGrossPay(self):
        self.grossSalary = self.baseSalary + self.bonus
        print(f"Base Salary:{self.baseSalary} \nBonus:{self.bonus}\nGross salary:{self.grossSalary}")
        return self.grossSalary




class Manager(SalariedEmployee):
    def __init__(self, employeeId, employeeName, basesalary):
        super().__init__(employeeId, employeeName)
        self.baseSalary=basesalary
    def calculateGrossPay(self):
        self.grossSalary = self.baseSalary + self.bonus + 500 + 250
        print(f"Base Salary:{self.baseSalary} \nBonus:{self.bonus}\nGross salary:{self.grossSalary}")
        return self.grossSalary


class Executive(SalariedEmployee):
    def __init__(self, employeeId, employeeName, basesalary,score):
        super().__init__(employeeId, employeeName)
        self.baseSalary = basesalary
        self.score=score
    def setbonus(self):
        score=self.score
        if score <=2:
            self.bonus = 0

        if score==3:
            self.bonus = self.baseSalary*5//100

        if score ==4:
            self.bonus = self.baseSalary*10//100

        if score ==5:
            self.bonus = self.baseSalary*15//100


    def calculateGrossPay(self):
        self.grossSalary = self.baseSalary+ self.bonus
        print(f"Base Salary:{self.baseSalary} \nBonus:{self.bonus}\nGross salary:{self.grossSalary}")
        return self.grossSalary

class HourlyEmployee(Employee):
    def __init__(self,employeeId,employeeName,hoursRate,hoursWork):
        super().__init__(employeeId,employeeName)
        self.type="Temporary Staff"
        self.hoursRate=hoursRate
        self.hoursWork=hoursWork

    def calculateGrossPay(self):
        if self.hoursWork<=160:
            self.bonus=0
            self.grossSalary=self.hoursWork*self.hoursRate

        else:
            self.baseSalary = 160*self.hoursRate
            self.bonus = self.hoursRate*(self.hoursWork-160)*1.50
            self.grossSalary=self.bonus+self.baseSalary
        print(f"Base Salary:{self.baseSalary} \nBonus:{self.bonus}\nGross salary:{self.grossSalary}")
        return self.grossSalary


class CommissionedEmployee(Employee):
    def __init__(self,employeeId,employeeName,baseStipend,totalSale):
        super().__init__(employeeId,employeeName)
        self.type="Contract Staff"
        self.baseStipend = baseStipend
        self.baseSalary=self.baseStipend
        self.totalSale=totalSale
        self.commission = 0


    def cacltotalSale(self):
        x= self.totalSale
        if x>50000:
            self.commission+=(x-50000)*18//100
            x=50000
        if 20001<=x<=50000:
            self.commission+=(x-20000)*12//100
            x=20000
        if x<=20000:
            self.commission+=(x)*8//100

        return self.commission
    def calculateGrossPay(self):
        self.cacltotalSale()
        self.grossSalary=self.commission+self.baseSalary
        print(f"Base Salary:{self.baseSalary} \nBonus:{self.bonus}\nGross salary:{self.grossSalary}")
        return self.grossSalary





class PayRollProcessor:
    def main(self,z:int):
        b=Manager(1,"A",5000)
        c=Executive(2,"B",4500,6)
        d=HourlyEmployee(3,"C",40,200)
        e=CommissionedEmployee(4,"D",3000,12500)

        listtype=[b,c,d,e]
        salary=[]
        totalpay=0
        for p in listtype:
            p.displayDetails()
            p.setbonus()
            p.calculateGrossPay()
            p.deductiontax()
            p.calcNetPay()
            salary.append(p.grossSalary)

        for salaries in salary:
            totalpay+=salaries
        print(f"Total money need to be paid is {totalpay}")




h=PayRollProcessor()
h.main(7)


