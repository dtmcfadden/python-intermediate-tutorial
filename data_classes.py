# Dataclasses
from dataclasses import dataclass, astuple, asdict, field


class Student:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other_student):
        return self.first_name == other_student.first_name \
            and self.last_name == other_student.last_name


student_1 = Student("Harry", "Potter", 18)
print(student_1)
student_2 = Student("Harry", "Potter", 18)
print(student_1 == student_2)


@dataclass
class StudentDataclass:
    first_name: str
    last_name: str
    age: int

    def __eq__(self, other):
        return self.first_name == other.first_name


student_1 = StudentDataclass("Frodo", "Baggins", 30)
student_2 = StudentDataclass("Frodo", "Doe", 20)
print(astuple(student_1))
print(asdict(student_1))
print(student_1)
# print(student_1 == student_2)


@dataclass(order=True)
class Product:
    sort_index: float = field(init=False, repr=False)
    name: str
    price: float
    quantity: int
    in_stock: bool = field(init=False)

    def __post_init__(self):
        self.in_stock = self.quantity > 0
        self.sort_index = self.price


chocolate = Product("Chocolate", 2.00, 15)
apple = Product("Apple", 1.50, 10)
orange = Product("Orange", 1.60, 20)

items = [apple, orange, chocolate]
# print(sorted(items))


@dataclass(frozen=True)
class Invoice:
    payer: str
    payee: str
    amount: float


invoice_1 = Invoice(payer="Harry Potter", payee="Frodo Baggins", amount=100)
# invoice_1.payer = "John Doe"
