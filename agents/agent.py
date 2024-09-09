import numpy as np
from city.company import Company

class Agent:
    def __init__(self, id, income, health, transport, job=None):
        self.id = id
        self.income = income
        self.health = health
        self.transport = transport
        self.job = job
        self.savings = 0
        self.rented_space = None
        self.owned_space = None

    def update_state(self, action, city_properties):
        # Filter city_properties to get only Company objects
        companies = [item for item in city_properties if isinstance(item, Company)]
        
        # Implement logic to update the agent's state based on the action and city properties
        if action == "change_job":
            self.find_job(city_properties)
        elif action == "switch_transport":
            # Logic to change transport
            pass
        elif action == "pay_rent":
            # Logic to pay rent
            pass
        elif action == "save_money":
            # Logic to save money
            pass
        elif action == "buy_property":
            # Logic to buy property
            pass
        # Additional actions can be implemented here
        pass

    def change_job(self):
        # Change the agent's job and adjust income accordingly
        available_jobs = self.job.company.jobs
        new_job = np.random.choice(available_jobs)
        self.job = new_job
        self.income = new_job.pay

    def pay_rent(self):
        if self.rented_space:
            rent = self.rented_space.rent
            self.savings -= rent

    def save_money(self):
        self.savings += self.income * 0.2  # Save 20% of income

    def buy_property(self, city_properties):
        # Simplified property buying logic
        affordable_properties = [p for p in city_properties if p.price <= self.savings]
        if affordable_properties:
            new_home = np.random.choice(affordable_properties)
            self.owned_space = new_home
            self.savings -= new_home.price
            city_properties.remove(new_home)

    def find_job(self, companies):
        # Ensure companies is a list of Company objects
        available_jobs = []
        for company in companies:
            if isinstance(company, Company):
                available_jobs.extend(company.get_jobs())
        
        if available_jobs:
            self.job = np.random.choice(available_jobs)
            self.income = self.job.pay