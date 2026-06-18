import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("weather.csv")

# Data Cleaning
df.dropna(inplace=True)

# Average Temperature
avg_temp = df["Temperature"].mean()
print("Average Temperature:", avg_temp)

# Total Rainfall
total_rain = df["Rainfall"].sum()
print("Total Rainfall:", total_rain)

# Highest Temperature Day
max_temp_day = df.loc[df["Temperature"].idxmax()]
print("\nHottest Day:\n", max_temp_day)

# Condition count
condition_count = df["Condition"].value_counts()
print("\nWeather Condition Count:\n", condition_count)

# Visualization - Pie Chart
plt.figure()
condition_count.plot(kind="pie", autopct='%1.1f%%')
plt.title("Weather Condition Distribution")
plt.ylabel("")
plt.savefig("pie_chart.png")

# Visualization - Bar Graph (Temperature)
plt.figure()
df.plot(x="Date", y="Temperature", kind="bar")
plt.title("Daily Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("bar_chart.png")

print("\nCharts saved successfully!")
