import numpy as np

class Agent:
    def __init__(self, id, income, health, transport, savings=0, rented_space=None):
        self.id = id
        self.income = income
        self.health = health
        self.transport = transport
        self.savings = savings
        self.rented_space = rented_space  # Reference to the rented living space, if any
        self.owned_space = None  # Reference to the owned living space, if any

    def update_state(self, action, city_properties=None):
        if action == "change_job":
            self.income = self.get_new_income()
        elif action == "switch_transport":
            self.transport = "public"
        elif action == "pay_rent":
            self.pay_rent()
        elif action == "save_money":
            self.save_money()
        elif action == "buy_property":
            if city_properties is not None:
                self.buy_property(city_properties)
        return self

    def get_new_income(self):
        # Example method to determine new income based on job change
        work_options = {"job1": 50000, "job2": 60000, "job3": 70000}
        return work_options.get(np.random.choice(list(work_options.keys())), 50000)

    def pay_rent(self):
        if self.rented_space:
            rent_amount = self.rented_space.rent
            self.savings -= rent_amount
            self.rented_space.owner.income += rent_amount  # Rent goes to the property owner

    def save_money(self):
        self.savings += 0.1 * self.income  # Example saving 10% of income

    def buy_property(self, city_properties):
        if self.savings > 100000:  # Example property cost
            affordable_properties = [prop for prop in city_properties if prop.price <= self.savings]
            if affordable_properties:
                chosen_property = np.random.choice(affordable_properties)
                self.savings -= chosen_property.price
                self.owned_space = chosen_property
                city_properties.remove(chosen_property)  # Remove the bought property from available list