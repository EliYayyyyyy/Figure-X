import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read Excel file into a DataFrame
df = pd.read_excel('/Users/qichenyuan/Desktop/Automation NGS Primer Design/Data Analysis/eBlock Plot.xlsx', sheet_name='eBlock11')

# Define a color palette using a gradient
cmap = sns.diverging_palette(240, 10, n=10, as_cmap=True)

# Normalize scores for color mapping
norm = plt.Normalize(df['Score'].min(), df['Score'].max())

# Create a color list based on the normalized score
colors = [cmap(norm(score)) for score in df['Score']]

# Set up the figure and axes
plt.figure(figsize=(15, 8))
ax = sns.barplot(x='Target', y='Score', data=df, palette=colors)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, ha='right', fontsize=6)

# Set the Y-axis limit
plt.ylim(0, 20)

# Indicate 5 on the Y-axis
plt.yticks(list(plt.yticks()[0]) + [5])

# Calculate quartiles
first_quartile = np.percentile(df['Score'], 25)
median = np.percentile(df['Score'], 50)
third_quartile = np.percentile(df['Score'], 75)

# Count values above or equal to 5, 10, and 20
above_first_quartile_count = df[df['Score'] >= first_quartile]['Score'].count()
above_median_count = df[df['Score'] >= median]['Score'].count()
above_third_quartile_count = df[df['Score'] >= third_quartile]['Score'].count()

# Add quartile indicators
plt.axhline(y=first_quartile, color='g', linestyle='--', label=f'1st Quartile: {first_quartile:.2f}')
plt.axhline(y=median, color='r', linestyle='--', label=f'2nd Quartile (Median): {median:.2f}')
plt.axhline(y=third_quartile, color='b', linestyle='--', label=f'3rd Quartile: {third_quartile:.2f}')

# Calculate the number of targets with values equal to or above the indicator values
targets_above_first_quartile = df[df['Score'] >= first_quartile]['Target'].nunique()
targets_above_median = df[df['Score'] >= median]['Target'].nunique()
targets_above_third_quartile = df[df['Score'] >= third_quartile]['Target'].nunique()

# Annotate the plot with the counts first number to adjust the position of the title
plt.text(64, first_quartile, f' Count above 1st Quartile: {targets_above_first_quartile}', fontsize=10,
         ha='left', va='bottom', color='g')
plt.text(64, median, f' Count above 2nd Quartile: {targets_above_median}', fontsize=10,
         ha='left', va='bottom', color='r')
plt.text(64, third_quartile, f' Count above 3rd Quartile: {targets_above_third_quartile}', fontsize=10,
         ha='left', va='bottom', color='b')

plt.legend()

# Add labels and title
plt.xlabel('Target Name', fontsize=12, color='black')
plt.ylabel('% Perfectly Edited Allele', fontsize=12, color='black')
plt.title('eBlock Plate11 Base Editing Screening Results Using Low-Dose DAPPER Modality Z', fontsize=14, color='black')

# Show the plot
plt.show()



























