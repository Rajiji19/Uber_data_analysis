import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'uber-raw-data.csv'  # Change this to your actual file path
df = pd.read_csv(file_path)

# Print column names to verify the correct column name for date/time
print("Column Names:", df.columns)

# Assuming the correct column name is 'Date/Time', if not, update it accordingly
datetime_column = 'Date/Time'  # Update this to match the actual column name in your dataset

# Check if the datetime_column exists in the DataFrame
if datetime_column not in df.columns:
    raise KeyError(f"Column '{datetime_column}' not found in the dataset. Available columns: {df.columns}")

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())
print("\n")

print("First 5 Rows of the Dataset:")
print(df.head())
print("\n")

# Convert the 'Date/Time' column to datetime format
df[datetime_column] = pd.to_datetime(df[datetime_column])

# Extract additional information from the 'Date/Time' column
df['Hour'] = df[datetime_column].dt.hour
df['Day'] = df[datetime_column].dt.day
df['Month'] = df[datetime_column].dt.month
df['DayOfWeek'] = df[datetime_column].dt.dayofweek

# Display the first 5 rows after adding new columns
print("First 5 Rows with Extracted Date/Time Columns:")
print(df.head())
print("\n")

# Plot the number of trips per hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=df, palette='viridis')
plt.title('Number of Trips per Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Trips')
plt.show()

# Plot the number of trips per day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='DayOfWeek', data=df, palette='viridis')
plt.title('Number of Trips per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Trips')
plt.show()

# Plot the number of trips per day of the month
plt.figure(figsize=(10, 6))
sns.countplot(x='Day', data=df, palette='viridis')
plt.title('Number of Trips per Day of the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Trips')
plt.show()

# Plot the number of trips per month
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', data=df, palette='viridis')
plt.title('Number of Trips per Month')
plt.xlabel('Month')
plt.ylabel('Number of Trips')
plt.show()

# Plot heatmap of trips by hour and day of the week
hour_day = df.groupby(['DayOfWeek', 'Hour']).size().unstack()
plt.figure(figsize=(12, 6))
sns.heatmap(hour_day, cmap='viridis')
plt.title('Heatmap of Trips by Hour and Day of the Week')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.show()
