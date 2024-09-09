import numpy as np
import pandas as pd
from agents.agent import Agent
from city.city import City
from city.property import Property
from city.company import Job, Company
from config.config import config

def run_simulation():
    # Initialize the city
    city = City(config['city_width'], config['city_height'])

    # Create and add properties to the city
    for i in range(10):  # Example: 10 properties
        prop = Property(id=i, price=100000 + i * 5000, rent=500 + i * 20)
        city.add_property(prop)

    # Create and add companies and jobs
    company1 = Company("TechCorp")
    company1.add_job("Software Engineer", 70000)
    company1.add_job("Data Analyst", 60000)

    company2 = Company("FinanceInc")
    company2.add_job("Accountant", 50000)
    company2.add_job("Financial Analyst", 55000)

    city.add_company(company1)
    city.add_company(company2)

    # Create agents and assign default attributes
    agents = [Agent(id=i, income=0, health=100, transport="car") for i in range(config['population_size'])]

    # Assign jobs to agents
    for agent in agents:
        agent.find_job(city.companies)

    # Simulation loop
    data = []
    for step in range(config['max_steps_per_episode']):
        step_data = []
        for agent in agents:
            # For simplicity, use a random action; you might want to implement more realistic actions
            action = np.random.choice(["change_job", "switch_transport", "pay_rent", "save_money", "buy_property"])
            agent.update_state(action, city.companies)  # Pass only companies here
            
            step_data.append({
                'Step': step,
                'AgentID': agent.id,
                'Job': agent.job.title if agent.job else "Unemployed",
                'Company': agent.job.company.name if agent.job else "None",
                'Income': agent.income,
                'Savings': agent.savings,
                'OwnedSpace': agent.owned_space if agent.owned_space else "None",
                'RentedSpace': agent.rented_space if agent.rented_space else "None",
            })
        data.append(pd.DataFrame(step_data))

    # Combine all steps data into one DataFrame
    result_df = pd.concat(data, ignore_index=True)
    
    # Save the results to a CSV file
    result_df.to_csv('simulation_results.csv', index=False)
    return result_df

if __name__ == '__main__':
    run_simulation()
