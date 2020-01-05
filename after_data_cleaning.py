import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('data.csv')

df_product = df[['Premiums in LOB: Motor', 'Premiums in LOB: Household', 
                 'Premiums in LOB: Health', 'Premiums in LOB:  Life', 
                 'Premiums in LOB: Work Compensations']]

df_costumers = df[['First Policy´s Year', 'Educational Degree', 'Gross Monthly Salary', 'Geographic Living Area', 'Has Children (Y=1)', 
                   'Customer Monetary Value', 'Claims Rate', 'Age As Client', 'Anual Salary', 'Costumer Annual Profit', 'Acquisition Cost']]

#distributions
sns.pairplot(df_product)

plt.show()

sns.pairplot(df_costumers)

plt.show()

#correlation
correlation_prod = df_product.corr()

sns.heatmap(correlation_prod, annot = True, cmap = "RdYlGn")

plt.show()

correlation_cos = df_costumers.corr()

sns.heatmap(correlation_cos, annot = True, cmap = "RdYlGn")

plt.show()
