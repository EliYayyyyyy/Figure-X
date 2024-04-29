import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Excel file with the specified sheet name
file_path = "/Users/qichenyuan/Desktop/NGS-111/Plot.xlsx"
sheet_name = "Compare"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Print out the column names
print(df.columns)

# Create the violin plot with statistics
plt.figure(figsize=(10, 6))
sns.violinplot(data=df[['100pmol', '200pmol']], inner="quartile")

# Add strip plot with jitter to avoid overlapping dots
sns.stripplot(data=df[['100pmol', '200pmol']], jitter=True, palette={'100pmol': 'skyblue', '200pmol': 'orange'}, alpha=0.8)

# Add sample amount labels
for i, col in enumerate(df.columns):
    plt.text(i + 0.15, df[col].max() + 0.2, f"n={len(df[col].dropna())}", ha='center')

# Calculate statistics
stats = df[['100pmol', '200pmol']].describe()

# Add statistical labels on the left side of each violin plot
for i, col in enumerate(stats.columns):
    plt.text(i - 0.3, stats.loc['max', col] + 0.2, f"Mean: {stats.loc['mean', col]:.2f}\nStd: {stats.loc['std', col]:.2f}\nMedian: {stats.loc['50%', col]:.2f}", ha='left')

plt.title('12-plex Base Editing with pooled SYNTHEGO gRNAs and ABE9 mRNA')
plt.xlabel('Dose of Pooled 12-plex gRNAs for each transfection')
plt.ylabel('% Perfectly Edited Allele')
plt.show()
