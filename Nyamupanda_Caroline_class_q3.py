# Caroline Nyamupanda
# R00205878

class Cinema:
    def __init__(self, name, capacity, ticket_price):
        self.name = name
        self.capacity = capacity
        self.ticket_price = ticket_price

    def __str__(self):
        return f"{self.name} has {self.capacity} seats  and tickets costs €{self.ticket_price} "

    def cost_of_family_tickets(self):
        return self.ticket_price * 3

    def price_increase(self):
        return self.ticket_price * 0.1 + self.ticket_price


