from customers import Customer
from operators import Operator
from bills import Bill


def main():
    # Ініціалізація операторів
    operators = [Operator(0, 0.5, 0.1, 0.2, 10), Operator(1, 0.6, 0.2, 0.25, 5)]

    bills = [Bill(1000), Bill(500)]

    customers = [Customer(0, 'Олег', 'Стецик', 18, operators, bills),
                 Customer(1, 'Влад', 'Школик', 19, operators, bills)]

    # Виклик дій для клієнтів
    customers[0].talk(10, customers[1], 0)
    customers[1].message(5, customers[0], 1)
    customers[0].connection(100, 0)

    # Оплата рахунку
    customers[0].get_bill(0).pay(200)

    # Зміна ліміту рахунку
    customers[0].get_bill(0).change_limit(200)


if __name__ == "__main__":
    main()