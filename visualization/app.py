import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_simulation_data(num_steps=None):
    data = pd.read_csv('simulation_results.csv')
    if num_steps:
        data = data[data['Step'] <= num_steps]
    return data

def main():
    st.title('Population Simulation Dashboard')

    # Add a slider to control the number of steps
    num_steps = st.slider('Number of Steps', min_value=10, max_value=100, value=50)

    # Load data based on the number of steps
    data = load_simulation_data(num_steps)

    st.write("## Simulation Data")
    st.write(data)

    # Add agent selection
    agent_ids = data['AgentID'].unique()
    selected_agent = st.selectbox('Select Agent ID', options=agent_ids)

    # Filter data for the selected agent
    agent_data = data[data['AgentID'] == selected_agent]

    st.write(f"## Data for Agent {selected_agent}")
    st.write(agent_data)

    # Income Over Time for Selected Agent
    st.write(f"## Income Over Time for Agent {selected_agent}")
    fig, ax = plt.subplots()
    ax.plot(agent_data['Step'], agent_data['Income'], marker='o', label='Income')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Income')
    ax.set_title(f'Income Over Time for Agent {selected_agent}')
    ax.legend()
    st.pyplot(fig)

    # Savings Over Time for Selected Agent
    st.write(f"## Savings Over Time for Agent {selected_agent}")
    fig, ax = plt.subplots()
    ax.plot(agent_data['Step'], agent_data['Savings'], marker='o', color='orange', label='Savings')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Savings')
    ax.set_title(f'Savings Over Time for Agent {selected_agent}')
    ax.legend()
    st.pyplot(fig)

    # General Trends for All Agents
    st.write("## General Trends for All Agents")

    # Income Over Time
    fig, ax = plt.subplots()
    ax.plot(data['Step'], data['Income'], marker='o', label='Income')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Income')
    ax.set_title('Income Over Time for All Agents')
    ax.legend()
    st.pyplot(fig)

    # Savings Over Time
    fig, ax = plt.subplots()
    ax.plot(data['Step'], data['Savings'], marker='o', color='orange', label='Savings')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Savings')
    ax.set_title('Savings Over Time for All Agents')
    ax.legend()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
