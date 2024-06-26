import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from pylab import rcParams
import warnings
import seaborn as sns
from google.colab import drive
drive.mount('/content/drive')
rcParams["figure.figsize"]=(30,18)
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 15
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)

Data=pd.read_csv("/content/drive/MyDrive/miterm/material.csv")
Data.isnull().sum()
Data.duplicated().sum()

df=Data.copy()
duplicated_rows = df[df.duplicated()]
duplicated_names = duplicated_rows['Material'].unique()
print(duplicated_names)

df.drop_duplicates(inplace=True)
duplicated_rows = df[df.duplicated()]
duplicated_names = duplicated_rows['Material'].unique()
print(duplicated_names)

import tensorflow as tf
if tf.test.is_gpu_available():
    print("GPU is available")
    print("GPU device name:", tf.test.gpu_device_name())
else:
    print("GPU is not available")

plt.scatter(df['Sy'], df['E'], c='blue', alpha=0.5)
plt.xlabel('Yield Strength (Sy)')
plt.ylabel("Young's Modulus (E)")
plt.title("Scatter plot of Yield Strength vs. Young's Modulus")
plt.grid(True)
plt.show()

sns.boxplot(x='Use', y='E', data=df)
plt.xlabel('Usage')
plt.ylabel("Young's Modulus (E)")
plt.title("Box plot of Young's Modulus for Different Usages")
plt.xticks(ticks=[0, 1], labels=['False', 'True'])
plt.show()

sns.pairplot(df.drop(columns=['Use', 'Ro']), diag_kind='kde')
plt.suptitle('Pairplot of Numerical Variables')
plt.show()

plt.hist(df['Ro'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Density (Ro)')
plt.ylabel('Frequency')
plt.title('Histogram of Material Density')
plt.show()

sns.scatterplot(x='Su', y='Sy', hue='Use', data=df)
plt.xlabel('Ultimate Strength (Su)')
plt.ylabel('Yield Strength (Sy)')
plt.title('Scatter plot of Ultimate Strength vs. Yield Strength (Colored by Usage)')
plt.legend(title='Usage')
plt.show()

def get_rating(row):
    conditions = [
        (438.3 <= row['Su'] <= 535.7, 318.6 <= row['Sy'] <= 389.4, 204930 <= row['E'] <= 209070, 71100 <= row['G'] <= 86900, 0.285 <= row['mu'] <= 0.315, 7467 <= row['Ro'] <= 8253),
        (389.6 <= row['Su'] <= 584.4, 283.2 <= row['Sy'] <= 424.8, 202860 <= row['E'] <= 211140, 63200 <= row['G'] <= 94800, 0.27 <= row['mu'] <= 0.33, 7074 <= row['Ro'] <= 8646),
        (340.9 <= row['Su'] <= 633.1, 247.8 <= row['Sy'] <= 460.2, 200790 <= row['E'] <= 213210, 55300 <= row['G'] <= 102700, 0.255 <= row['mu'] <= 0.345, 6681 <= row['Ro'] <= 9039),
        (292.2 <= row['Su'] <= 681.8, 212.4 <= row['Sy'] <= 495.6, 198720 <= row['E'] <= 215280, 47400 <= row['G'] <= 110600, 0.24 <= row['mu'] <= 0.36, 6288 <= row['Ro'] <= 9432)
    ]
    ratings = [5, 4, 3, 2]

    for rating, condition in zip(ratings, conditions):
        if all(condition):
            return rating
    return 1

df['rating'] = df.apply(get_rating, axis=1)
df

df['Use'] = df['Use'].astype(int)
df

df['Su/Sy'] = df['Su'] / df['Sy']
df

from scipy.stats import pearsonr, ttest_ind, f_oneway, chi2_contingency
from sklearn.linear_model import LinearRegression
numeric_df = df.select_dtypes(include=np.number)

# Correlation Analysis
correlation_matrix = numeric_df.corr()

# T-Test or ANOVA - Example: Compare 'Su' across different 'Use' categories
t_statistic, p_value = ttest_ind(numeric_df[numeric_df['Use'] == 0]['Su'], numeric_df[numeric_df['Use'] == 1]['Su'])
# Alternatively, for ANOVA across multiple categories, replace 'Category' with another categorical column if available.
#f_statistic, p_value_anova = f_oneway(numeric_df[numeric_df['Category'] == 'A']['Su'], numeric_df[numeric_df['Category'] == 'B']['Su'], numeric_df[numeric_df['Category'] == 'C']['Su'])

# Chi-Square Test - Example: Test independence between 'Use' and 'Rating' categories
chi2_statistic, chi2_p_value, _, _ = chi2_contingency(pd.crosstab(df['Use'], df['rating']))

chi2_statistic

X = numeric_df[['Sy', 'E', 'G', 'mu', 'Ro']]
y = numeric_df['Su']
regressor = LinearRegression()
regressor.fit(X, y)
coefficients = regressor.coef_
intercept = regressor.intercept_

print("Correlation Matrix:")
print(correlation_matrix)
print("\nT-Test p-value:", p_value)
# print("ANOVA p-value:", p_value_anova)
print("\nChi-Square Test p-value:", chi2_p_value)
print("\nLinear Regression Coefficients:", coefficients)
print("Linear Regression Intercept:", intercept)

z_scores = (numeric_df - numeric_df.mean()) / numeric_df.std()

threshold = 3

outliers = (z_scores.abs() > threshold)

print("Count of outliers in each column:")
print(outliers.sum())

print("\nRows containing outliers:")
print(df[outliers.any(axis=1)])

# Convert DataFrame to NumPy array
numeric_array = numeric_df.to_numpy()

# Replace masked values with NaN
numeric_array = np.where(np.isinf(numeric_array), np.nan, numeric_array)

# Check for NaN values
nan_mask = np.isnan(numeric_array)

# Count NaN values in each column
nan_count = np.sum(nan_mask, axis=0)

# Drop rows containing NaN values
numeric_array = numeric_array[~np.any(nan_mask, axis=1)]

# Check the count of outliers in each column after processing
outliers_after_processing = (numeric_array - np.mean(numeric_array, axis=0)) / np.std(numeric_array, axis=0) > threshold
print("Count of outliers in each column after processing:")
print(np.sum(outliers_after_processing, axis=0))

df.drop(["Material"]  , axis=1 , inplace=True)

sns.pairplot(df, hue='Use', palette='husl')
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

for i, column in enumerate(df.columns):
    plt.subplot(3, 3, i + 1)
    sns.histplot(df[column], kde=True, color='skyblue', stat='density')
    plt.title(column)
    plt.xlabel('Values')
    plt.ylabel('Density')
plt.tight_layout()
plt.show()

for i, column in enumerate(df.columns[1:]):
    plt.subplot(3, 3, i + 1)
    sns.histplot(df[column], kde=True, color='skyblue', stat='density')
    plt.title(column)
    plt.xlabel('Values')
    plt.ylabel('Density')
plt.tight_layout()
plt.show()

columns_to_plot = ['Su', 'Sy', 'E', 'G', 'mu', 'Ro', 'rating', 'Su/Sy']

fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15, 20))

# Plotting each column
for i, column in enumerate(columns_to_plot):
    ax = axes.flatten()[i]
    ax.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    ax.set_title(column)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

# Adjusting layout
plt.tight_layout()
plt.show()

plt.subplots_adjust(hspace=0.5)
for i, column in enumerate(columns_to_plot, 1):
    plt.subplot(2, 4, i)
    sns.boxplot(x=df[column], color='skyblue')
    plt.title(column)
plt.figure(figsize=(15, 10))
plt.subplots_adjust(hspace=0.5)
for i, column in enumerate(columns_to_plot, 1):
    plt.subplot(2, 4, i)
    sns.violinplot(x=df[column], color='salmon')
    plt.title(column)

plt.show()

sns.pairplot(df, vars=['Su', 'Sy', 'E', 'G', 'mu', 'Ro', 'rating', 'Su/Sy'], kind='scatter')
plt.suptitle('Pair Plot of Numerical Variables', y=1.02)
plt.show()

sns.jointplot(data=df, x='Su', y='Sy', kind='scatter')
plt.suptitle('Joint Plot of Su vs Sy', y=1.02)
plt.show()

sns.violinplot(data=df, inner='point')
plt.title('Violin Plot')
plt.show()

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['Su', 'Sy', 'E', 'G', 'mu']])
pca = PCA(n_components=3)  # Choose number of principal components
principal_components = pca.fit_transform(scaled_features)
principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3'])

df

sns.jointplot(x='Su', y='Sy', data=df, kind='hex')
sns.residplot(x='E', y='G', data=df, scatter_kws={'s': 80})
sns.swarmplot(x='Use', y='rating', hue='Use', data=df)
plt.show()

g = sns.PairGrid(df)
g.map_upper(sns.scatterplot)
g.map_diag(sns.histplot, kde=True)
g.map_lower(sns.kdeplot)

sns.clustermap(df.corr(), cmap='coolwarm', annot=True)
g = sns.FacetGrid(df, col='Use', hue='Use')
g.map(sns.scatterplot, 'Su', 'Sy')
sns.kdeplot(data=df['E'], shade=True)
plt.show()

X = df.drop(columns=['Use'])
y = df['Use']

oversampler = SMOTE(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = oversampler.fit_resample(X, y)

resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
resampled_df['Use'] = y_resampled

print(resampled_df)

resampled_df["Use"].value_counts()

plt.scatter(df['Su'], df['Sy'], color='skyblue', alpha=0.5)
plt.xlabel('Su')
plt.ylabel('Sy')
plt.title('Relationship between Su and Sy')
plt.grid(True)
plt.show()

plt.hist(df['Su'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Su')
plt.ylabel('Frequency')
plt.title('Distribution of Su')
plt.grid(True)
plt.show()

sns.boxplot(x=df['Use'], y=df['Su'])
plt.xlabel('Use')
plt.ylabel('Su')
plt.title('Box plot of Su by Use')
plt.show()

sns.pairplot(df[['Su', 'Sy', 'E', 'G', 'mu']])
plt.title('Pairwise Relationships')
plt.show()

sns.barplot(x='Use', y='Su', data=df)
plt.xlabel('Use')
plt.ylabel('Su')
plt.title('Average Su by Use')
plt.show()

corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

sns.jointplot(x='Su', y='Sy', data=df, kind='hex')
plt.xlabel('Su')
plt.ylabel('Sy')
plt.title('Joint Plot of Su vs. Sy')
plt.show()

sns.clustermap(df.corr(), cmap='coolwarm', annot=True)
plt.title('Clustermap of Correlation Matrix')
plt.show()

sns.jointplot(x='Su', y='Sy', data=df, kind='kde')
plt.xlabel('Su')
plt.ylabel('Sy')
plt.title('Joint Distribution Plot of Su vs. Sy')
plt.show()

g = sns.PairGrid(df, hue='Use')
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.subplots_adjust(top=0.9)
g.fig.suptitle('PairGrid of Variables with KDE Diagonals')
plt.show()

fig, axs = plt.subplots(2, 3, figsize=(12, 8))
variables = ['Su', 'Sy', 'E', 'G', 'mu', 'Ro']
for i, var in enumerate(variables):
    sns.histplot(df[var], ax=axs[i//3, i%3], kde=True)
    axs[i//3, i%3].set_title(f'Distribution of {var}')
plt.tight_layout()
plt.show()

g = sns.PairGrid(df)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.scatterplot)
plt.subplots_adjust(top=0.9)
g.fig.suptitle('PairGrid with KDE Diagonals')
plt.show()

g = sns.PairGrid(df)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.scatterplot)
plt.subplots_adjust(top=0.9)
g.fig.suptitle('PairGrid with KDE Diagonals')
plt.show()
