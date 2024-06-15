
#Importing necessary libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
RNG_SEED=42
np.random.seed(seed=RNG_SEED)
from sklearn.preprocessing import MinMaxScaler
# %matplotlib inline
# %config InlineBackend.figure_format='retina'

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

#Change path according to your file position.
data_path= '/content/drive/MyDrive/miterm/data.csv'
df = pd.read_csv(data_path, encoding='latin-1')
print(f'Original Dataframe shape{df.shape}')

!pip install pandas-profiling

!pip install ydata-profiling

#Profiling Data
from ydata_profiling import ProfileReport
profile=ProfileReport(df,title="Profiling Report")
profile.to_widgets()

df.columns

# Check for columns with all NaN values
empty_columns = df.columns[df.isnull().all()]

# Drop columns with all NaN values
df.drop(empty_columns, axis=1, inplace=True)
df.columns

# Fill missing values with a specific value or a suitable strategy
df = df.fillna(method='ffill')

# Print a part of the DataFrame after handling missing values
print(df.head())

#Renaming columns for ease
rename_dict = {
    "SAE Grade": "grade",
    "Conditions": "condition",
    "UTS (MPa)": "uts_mpa",
    "YS (MPa)": "ys_mpa",
    "C (Min)": "c_min",
    "C (Max)": "c_max",
    "Mn (Min)": "mn_min",
    "Mn (Max)": "mn_max"
}
df = df.rename(columns=rename_dict)
df.columns

# Convert numeric columns to appropriate data types
numeric_cols = ['uts_mpa', 'UTS (Ksi)', 'ys_mpa', 'YS (ksi)', 'Elongation (%)', 'Reduction (%)', 'Hardness (HB)']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Print a part of the DataFrame after converting data types
print(df.head())

# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))

# Plot Yield Strength (MPa) with blue color and label
ax.plot(df['ys_mpa'], label='Yield Strength (MPa)')

# Plot Ultimate Tensile Strength (MPa) with red color and label
ax.plot(df['uts_mpa'], color='darkorange', label='Ultimate Tensile Strength (MPa)')

# Set labels and title
ax.set_xlabel('Sample Number')
ax.set_ylabel('MPa')
ax.set_title('Material Properties vs. Grade')

# Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend()

# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))

# Plot Young's Modulus (MPa) with blue color and label
ax.plot(df['Elongation (%)'], label='Elongation (%)')

# Plot Ultimate Tensile Strength (MPa) with red color and label
ax.plot(df['Reduction (%)'], color='darkorange', label='Reduction (%)')

# Set labels and title
ax.set_xlabel('Sample Number')
ax.set_ylabel('%')
ax.set_title('Material Properties vs. Grade')

# Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend()

# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))

# Plot Young's Modulus (MPa) with blue color and label
ax.plot(df['Hardness (HB)'], label='Hardness (HB)')


# Set labels and title
ax.set_xlabel('Sample Number')
ax.set_ylabel('HB')
ax.set_title('Material Properties vs. Grade')

# Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is already loaded and processed as per your previous steps

# Select only numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Calculate the correlation matrix for numeric columns
correlation_matrix = df[numeric_cols].corr()

# Print the correlation matrix
print(correlation_matrix)

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
