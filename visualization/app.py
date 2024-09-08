import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to load or generate simulation data
def load_simulation_data():
    # Replace this with actual data loading from your simulation
    # Here we generate some example data
    steps = np.arange(0, 50, 10)
    incomes = np.random.randint(40000, 50000, size=len(steps))
    savings = np.random.randint(10000, 20000, size=len(steps))
    return pd.DataFrame({
        'Steps': steps,
        'Income': incomes,
        'Savings': savings
    })

def main():
    st.title('Population Simulation Dashboard')

    # Add a slider to control the number of steps
    num_steps = st.slider('Number of Steps', min_value=10, max_value=100, value=50)

    # Load data based on the number of steps
    data = load_simulation_data()  # Modify this function to handle the number of steps

    st.write("## Simulation Data")
    st.write(data)

    st.write("## Income Over Time")
    fig, ax = plt.subplots()
    ax.plot(data['Steps'], data['Income'], marker='o', label='Income')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Income')
    ax.set_title('Income Over Time')
    ax.legend()
    st.pyplot(fig)

    st.write("## Savings Over Time")
    fig, ax = plt.subplots()
    ax.plot(data['Steps'], data['Savings'], marker='o', color='orange', label='Savings')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Savings')
    ax.set_title('Savings Over Time')
    ax.legend()
    st.pyplot(fig)


if __name__ == '__main__':
    main()
