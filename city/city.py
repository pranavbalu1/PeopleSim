import numpy as np

class Property:
    def __init__(self, id, price, rent, owner=None):
        self.id = id
        self.price = price
        self.rent = rent
        self.owner = owner

class City:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height))
        self.properties = []

    def add_property(self, prop):
        self.properties.append(prop)

    def assign_property(self, agent, property_id):
        property = next((p for p in self.properties if p.id == property_id), None)
        if property:
            agent.rented_space = property
            property.owner = agent
