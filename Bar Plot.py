import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read Excel file into a DataFrame
df = pd.read_excel('/Users/qichenyuan/Desktop/TEST.xlsx', sheet_name='Sheet1')

# Create a color list based on the condition (Score > 5)
colors = ['maroon' if score > 5 else 'teal' for score in df['Score']]

# Set up the figure and axes
plt.figure(figsize=(15, 8))
ax = sns.barplot(x='Target', y='Score', data=df, palette=colors)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, ha='right',fontsize=6)

# Add a dashed line at y=5 to highlight bars above 5
plt.axhline(y=5, color='gold', linestyle='--', linewidth=2)

# Set the Y-axis limit to 100
plt.ylim(0, 60)

# Indicate 5 on the Y-axis
plt.yticks(list(plt.yticks()[0]) + [5])

# Add labels and title
plt.xlabel('Target Name')
plt.ylabel('% Perfectly Edited Allele')
plt.title('eBlock Plate 1 Base Editing Screening Results Using Low-Dose DAPPER Modality Z')

# Show the plot
plt.show()


