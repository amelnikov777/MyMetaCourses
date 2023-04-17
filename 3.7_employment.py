class Employees():
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May i take a leave for " + str(days) + " days?"

andrew = Supervisors("Andrew", "A", "apple")
emili = Chefs("Emili", "E")
juno = Chefs("Juno", "J")

print(emili.leave_request(3))
print(andrew.password)
print(emili.name)