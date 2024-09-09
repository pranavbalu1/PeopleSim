import numpy as np

class City:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height))
        self.properties = []
        self.companies = []

    def add_property(self, prop):
        self.properties.append(prop)

    def add_company(self, company):
        self.companies.append(company)  # Method to add a company