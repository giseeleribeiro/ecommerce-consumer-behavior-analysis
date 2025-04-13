
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("Ecommerce_Selected_Analysis_Data.xlsx") #dataset

correlation = df.corr(numeric_only=True)
print("Correlation Matrix:\n", correlation)

plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('age_distribution.png')
plt.close()


plt.figure(figsize=(8, 5))
sns.boxplot(x='Gender', y='Purchase_Amount', data=df)
plt.title('Purchase Amount by Gender')
plt.tight_layout()
plt.savefig('purchase_amount_by_gender.png')
plt.close()

plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Device_Used_for_Shopping', hue='Discount_Used')
plt.title('Device Used for Shopping vs Discount Usage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('device_vs_discount.png')
plt.close()


