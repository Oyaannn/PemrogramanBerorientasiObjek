class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: {self.calculate_salary()}")


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + (0.20 * self.salary)


class Engineer(Employee):
    def calculate_salary(self):
        return self.salary + (0.10 * self.salary)


class Intern(Employee):
    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id, stipend)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# Example usage
if __name__ == "__main__":
    manager = Manager("Alice", 1, 5000)
    engineer = Engineer("Bob", 2, 4000)
    intern = Intern("Charlie", 3, 1000)

    manager.show_details()
    print()
    engineer.show_details()
    print()
    intern.show_details()