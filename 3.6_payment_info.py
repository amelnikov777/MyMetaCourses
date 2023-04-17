class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " has paid " + str(self.amount)
        else:
            return self.name + " isn't paid yet"

maksim = Payslips("Maksim", "no", 5000)
anna = Payslips("Anna", "no", 3500)

print(maksim.status())
print(anna.status())

maksim.pay()

print(maksim.status())
print(anna.status())
