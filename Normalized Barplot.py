import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read Excel file into a DataFrame
df = pd.read_excel('/Users/qichenyuan/Desktop/Automation NGS Primer Design/Data Analysis/eBlock Plot.xlsx', sheet_name='eBlock11')

# Define a color palette using the "viridis" colormap
cmap = plt.cm.get_cmap('Spectral')

# Normalize scores for color mapping, ensuring highest value is mapped to 100 and lowest to 0
max_score = df['Score'].max()
min_score = df['Score'].min()
df['Normalized_Score'] = (df['Score'] - min_score) / (max_score - min_score) * 100

# Create a color list based on the normalized score
colors = [cmap(norm_score/100) for norm_score in df['Normalized_Score']]

# Set up the figure and axes
plt.figure(figsize=(15, 8))
ax = sns.barplot(x='Target', y='Normalized_Score', data=df, palette=colors)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, ha='right', fontsize=6)

# Set the Y-axis limit
plt.ylim(0, 100)

# Set Y-axis ticks
plt.yticks([0, 20, 40, 60, 80, 100])

# Calculate quartiles
first_quartile = np.percentile(df['Score'], 25)
median = np.percentile(df['Score'], 50)
third_quartile = np.percentile(df['Score'], 75)

# Normalize quartiles
norm_first_quartile = (first_quartile - min_score) / (max_score - min_score) * 100
norm_median = (median - min_score) / (max_score - min_score) * 100
norm_third_quartile = (third_quartile - min_score) / (max_score - min_score) * 100

# Add quartile indicators
plt.axhline(y=norm_first_quartile, color='g', linestyle='--', label=f'1st Quartile: {norm_first_quartile:.2f}')
plt.axhline(y=norm_median, color='r', linestyle='--', label=f'2nd Quartile (Median): {norm_median:.2f}')
plt.axhline(y=norm_third_quartile, color='b', linestyle='--', label=f'3rd Quartile: {norm_third_quartile:.2f}')

# Calculate the number of targets with values equal to or above the indicator values
targets_above_first_quartile = df[df['Score'] >= first_quartile]['Target'].nunique()
targets_above_median = df[df['Score'] >= median]['Target'].nunique()
targets_above_third_quartile = df[df['Score'] >= third_quartile]['Target'].nunique()

# Annotate the plot with the counts first number to adjust the position of the title
plt.text(64, norm_first_quartile, f' Count above 1st Quartile: {targets_above_first_quartile}', fontsize=10,
         ha='left', va='bottom', color='g')
plt.text(64, norm_median, f' Count above 2nd Quartile: {targets_above_median}', fontsize=10,
         ha='left', va='bottom', color='r')
plt.text(64, norm_third_quartile, f' Count above 3rd Quartile: {targets_above_third_quartile}', fontsize=10,
         ha='left', va='bottom', color='b')

plt.legend()

# Add labels and title
plt.xlabel('Target Name', fontsize=12, color='black')
plt.ylabel('Editing Score (0-100)', fontsize=12, color='black')
plt.title('Normalized eBlock Plate11 Base Editing Screening Results Using Low-Dose DAPPER Modality Z', fontsize=14, color='black')

# Show the plot
plt.show()
