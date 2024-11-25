from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customers import Customer


class Operator:

    def __init__(self, id: int, talking_charge: float, message_cost: float,
                 network_charge: float, discount_rate: int) -> None:
        # Конструктор
        self.id = id
        self.talking_charge: float = talking_charge
        self.message_cost: float = message_cost
        self.network_charge: float = network_charge
        self.discount_rate: int = discount_rate

    def calc_talking_cost(self, minutes: float, customer: 'Customer') -> float:
        # Розрахунок вартості дзвінка з урахуванням вікових знижок
        cost = self.talking_charge * minutes
        if customer.age < 18 or customer.age > 65:
            discount = cost * (self.discount_rate / 100)
            cost -= discount
        return cost

    def calc_message_cost(self, quantity: int, customer: 'Customer', other: 'Customer') -> float:
        # Розрахунок вартості повідомлень
        cost = self.message_cost * quantity
        if self.id == other.operators[self.id].id:
            discount = cost * (self.discount_rate / 100)
            cost -= discount
        return cost

    def calc_network_cost(self, amount: float) -> float:
        # Розрахунок вартості інтернету
        return self.network_charge * amount