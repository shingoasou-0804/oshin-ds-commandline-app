import math
from typing import Literal


Grade = Literal["junior", "middle", "senior", "expert"]


class Employee:
    def __init__(self, name: str, grade: Grade) -> None:
        self.name = name
        self.grade = grade


class BonusCalculator:
    def __init__(self, base: int) -> None:
        self.base = base
    
    def get_bonus(self, employee: Employee) -> int:
        if employee.grade == "junior":
            return math.floor(self.base * 1.1)
        elif employee.grade == "middle":
            return math.floor(self.base * 1.5)
        elif employee.grade == "senior":
            return math.floor(self.base * 2)
        elif employee.grade == "expert":
            return math.floor(self.base * 3)


if __name__ == "__main__":
    emp1 = Employee("Yamada", "junior")
    emp2 = Employee("Suzuki", "middle")
    emp3 = Employee("Tanaka", "senior")
    emp4 = Employee("Kato", "expert")

    bonus_calculator = BonusCalculator(100)
    print(bonus_calculator.get_bonus(emp1))
    print(bonus_calculator.get_bonus(emp2))
    print(bonus_calculator.get_bonus(emp3))
    print(bonus_calculator.get_bonus(emp4))
