import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import statsmodels.api as sm

# Load data from Excel file
file_path = "/Users/qichenyuan/Desktop/NGS-075/Correlation.xlsx"
sheet_name = "Sheet2"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Set column names
x_column = "Rule Set2 Score"
y_column = "Editing Efficiency"

# Create a scatter plot with a regression line
sns.regplot(x=x_column, y=y_column, data=df)

# Perform linear regression to get R-squared
X = sm.add_constant(df[x_column])
model = sm.OLS(df[y_column], X).fit()
r_squared = model.rsquared

# Calculate the correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(df[x_column], df[y_column])

# Set plot labels, title, and include the p-value and R-squared in the title
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title(f"Correlation Plot: {x_column} vs {y_column} (Correlation = {correlation_coefficient:.4f}, p-value = {p_value:.4f}, R-squared = {r_squared:.4f})")

# Show the plot
plt.show()

