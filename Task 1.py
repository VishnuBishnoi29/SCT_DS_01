import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('D:/world_population.csv')

# Show basic info
print("Basic Info:")
print(df.info(), "\n")

# Show first few rows
print("Head of Dataset:")
print(df.head(), "\n")

# Descriptive statistics
print("Descriptive Statistics:")
print(df.describe(include='all'), "\n")

# Null values before cleaning
print("Missing Values Before Cleaning:")
print(df.isnull().sum(), "\n")

# Get the top 10 countries by 2022 population
top10 = df.nlargest(10, '2022 Population')

# Create the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='Country/Territory', y='2022 Population', data=top10, palette='viridis')

plt.title('Top 10 Countries by 2022 Population', fontsize=16)
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot histogram of growth rates
plt.figure(figsize=(10, 6))
sns.histplot(df['Growth Rate'], bins=30, kde=True, color='salmon')

plt.title('Distribution of Population Growth Rate (2022)', fontsize=16)
plt.xlabel('Growth Rate')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()


# Group by continent and calculate average growth rate
continent_growth = df.groupby('Continent')['Growth Rate'].mean().sort_values(ascending=False)

# Create bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=continent_growth.index, y=continent_growth.values, palette='coolwarm')

# Add titles and labels
plt.title('Average Population Growth Rate by Continent (2022)', fontsize=16)
plt.xlabel('Continent')
plt.ylabel('Average Growth Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
