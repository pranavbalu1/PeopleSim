def apply_tax_law(agent):
    tax_rate = 0.2  # Example tax rate
    agent.income *= (1 - tax_rate)  # Reduce income by tax
    return agent
