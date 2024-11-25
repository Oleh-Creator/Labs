from typing import List, Dict, Self
from bills import Bill
from operators import Operator


class Customer:
    """Клас Customer представляє клієнта системи зв'язку"""

    def __init__(self, id: int, first_name: str, last_name: str,
                 age: int, operators: List[Operator], bills: List[Bill], limiting_amount: float = 1000.0) -> None:
        """Конструктор"""
        self.id: int = id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self._age: int = age
        self.operators: Dict[int, Operator] = {operator.id: operator for operator in operators}
        self.bills: Dict[int, Bill] = {operator.id: bills[idx] for idx, operator in enumerate(operators)}
        self.limiting_amount: float = limiting_amount

    def talk(self, minutes: float, customer: Self, operator_id: int) -> None:
        """Метод для дзвінку"""
        operator = self.operators.get(operator_id)
        if operator:
            talk_cost = operator.calc_talking_cost(minutes, self)
            bill = self.bills.get(operator_id)
            if bill and not bill.check():
                bill.add_debt(talk_cost)
                print(f"{self.first_name} говорив з {customer.first_name} {minutes} хвилин.")
            else:
                print(f"{self.first_name} перевищив ліміт рахунку і не може виконати дзвінок.")
        else:
            print(f"Оператор з ID {operator_id} не знайдений.")

    def message(self, quantity: int, customer: Self, operator_id: int) -> None:
        """Метод для відправлення повідомлення"""
        operator = self.operators.get(operator_id)
        if operator:
            message_cost = operator.calc_message_cost(quantity, self, customer)
            bill = self.bills.get(operator_id)
            if bill and not bill.check():
                bill.add_debt(message_cost)
                print(f"{self.first_name} відправив {quantity} повідомлень для {customer.first_name}.")
            else:
                print(f"{self.first_name} перевищив ліміт рахунку і не може надіслати повідомлення.")
        else:
            print(f"Оператор з ID {operator_id} не знайдений.")

    def connection(self, amount: float, operator_id: int) -> None:
        """Метод підключення до інтернету"""
        operator = self.operators.get(operator_id)
        if operator:
            network_cost = operator.calc_network_cost(amount)
            bill = self.bills.get(operator_id)
            if bill and not bill.check():
                bill.add_debt(network_cost)
                print(f"{self.first_name} використав {amount} MB.")
            else:
                print(f"{self.first_name} перевищив ліміт рахунку і не може використовувати інтернет.")
        else:
            print(f"Оператор з ID {operator_id} не знайдений.")

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if age <= 0:
            raise ValueError('Age must be positive')
        self._age = age

    def get_operator(self, operator_id: int) -> Operator:
        """Отримати оператора за ID"""
        operator = self.operators.get(operator_id)
        if operator is None:
            raise ValueError(f"Оператор з ID {operator_id} не знайдений.")
        return operator

    def set_operator(self, operator_id: int, operator: Operator) -> None:
        """Додати або оновити оператора за ID"""
        self.operators[operator_id] = operator

    def get_bill(self, operator_id: int) -> Bill:
        """Отримати рахунок за ID оператора"""
        bill = self.bills.get(operator_id)
        if bill is None:
            raise ValueError(f"Рахунок з ID {operator_id} не знайдений.")
        return bill

    def set_bill(self, operator_id: int, bill: Bill) -> None:
        """Додати або оновити рахунок за ID оператора"""
        self.bills[operator_id] = bill
