import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load simulation data
def load_simulation_data():
    # Load data from CSV file
    try:
        data = pd.read_csv('simulation_results.csv')
    except FileNotFoundError:
        st.error("Simulation results file not found. Please run the simulation first.")
        return pd.DataFrame()
    return data

def main():
    st.title('Population Simulation Dashboard')

    # Load data
    data = load_simulation_data()
    if data.empty:
        return
    
    # Display simulation data
    st.write("## Simulation Data")
    st.write(data)
    
    # Display job distribution
    st.write("## Job Distribution")
    job_distribution = data['Job'].value_counts()
    st.bar_chart(job_distribution)
    
    # Display income over time
    st.write("## Income Over Time")
    income_over_time = data.groupby('Step')['Income'].mean()
    fig, ax = plt.subplots()
    ax.plot(income_over_time.index, income_over_time.values, marker='o', label='Average Income')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Income')
    ax.set_title('Income Over Time')
    ax.legend()
    st.pyplot(fig)
    
    # Display savings over time
    st.write("## Savings Over Time")
    savings_over_time = data.groupby('Step')['Savings'].mean()
    fig, ax = plt.subplots()
    ax.plot(savings_over_time.index, savings_over_time.values, marker='o', color='orange', label='Average Savings')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Savings')
    ax.set_title('Savings Over Time')
    ax.legend()
    st.pyplot(fig)
    
    # Display agent-specific data
    st.write("## Agent-Specific Data")
    agent_ids = data['AgentID'].unique()
    selected_agent = st.selectbox('Select Agent ID', options=['All'] + list(agent_ids))
    
    if selected_agent == 'All':
        agent_data = data
    else:
        agent_data = data[data['AgentID'] == int(selected_agent)]
    
    st.write(f"Showing data for agent {selected_agent}")
    st.write(agent_data)
    
    # Display agent-specific job distribution
    st.write("## Agent-Specific Job Distribution")
    if not agent_data.empty:
        job_distribution = agent_data['Job'].value_counts()
        st.bar_chart(job_distribution)

if __name__ == '__main__':
    main()
