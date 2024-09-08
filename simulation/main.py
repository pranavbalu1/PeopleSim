import agent
from agent.agent import Agent
from city.city import City, Property
from laws.tax_law import apply_tax_law
from config.config import config
import numpy as np
import pandas as pd

def run_simulation():
    city = City(config['city_width'], config['city_height'])
    
    # Create and add properties to the city
    for i in range(10):  # Example: 10 properties
        prop = Property(id=i, price=100000 + i * 5000, rent=500 + i * 20)
        city.add_property(prop)

    agents = [Agent(id=i, income=50000, health=100, transport="car") for i in range(config['population_size'])]

    # Assign properties to agents
    for agent in agents:
        if np.random.rand() < 0.5:  # 50% chance to rent
            city.assign_property(agent, np.random.choice([prop.id for prop in city.properties]))
        else:
            agent.rented_space = None
            agent.owned_space = None

# Initialize a DataFrame to store simulation data
    data = pd.DataFrame(columns=['Step', 'AgentID', 'Income', 'Savings', 'OwnedSpace'])

    # Simulation loop
    for step in range(config['max_steps_per_episode']):
        for agent in agents:
            action = np.random.choice(["change_job", "switch_transport", "pay_rent", "save_money", "buy_property"])
            agent.update_state(action, city.properties)  # Pass city properties here

        # Collect data for this step
        for agent in agents:
            data = data.append({
                'Step': step,
                'AgentID': agent.id,
                'Income': agent.income,
                'Savings': agent.savings,
                'OwnedSpace': agent.owned_space
            }, ignore_index=True)
            
        # Save the data to a CSV file
        data.to_csv('simulation_results.csv', index=False)

                                                                                                
        if step % 10 == 0:
            print(f"Step {step}: {agents[0].income}, Savings: {agents[0].savings}, Owned Space: {agents[0].owned_space}")

if __name__ == "__main__":
    run_simulation()
