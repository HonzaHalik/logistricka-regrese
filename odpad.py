import matplotlib.pyplot as plt

# Years for the x-axis
years = list(range(1990, 2022))

# Inflation rates for Czechoslovakia and the Czech Republic
czechoslovakia_inflation = [33, 50, 71] + [None] * 29
czech_republic_inflation = [None] + [10.9, 9.3, 10.4, 6.4, 6.6, 4.5, 2.3, 3.5, 2.9, 1.7, 0.8, 2.6, 1.9, 2.1, 2.9, 6.3, 1.0, 1.4, 2.1, 3.3, 1.4, 0.4, 0.3, 0.6, 2.0, 2.0, 2.7, 2.3, 2.8]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(years, czechoslovakia_inflation, label='Czechoslovakia Inflation', marker='o')
plt.plot(years, czech_republic_inflation, label='Czech Republic Inflation', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.title('Inflation Rates: Czechoslovakia (1990-1992) vs. Czech Republic (1993-2021)')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
