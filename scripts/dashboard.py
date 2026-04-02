import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv(r"C:\Users\Shreya patel\OneDrive\Desktop\Trae\Sales-Data-Analysis\data\train.csv")

dataset.info()
dataset.isnull().sum()

dataset["Order Date"] = pd.to_datetime(dataset["Order Date"], format="mixed")
dataset["Month"] = dataset["Order Date"].dt.strftime("%b")
dataset["Ship Date"] = pd.to_datetime(dataset["Ship Date"], format="mixed")

dataset.describe()

dataset["Category"].value_counts()

dataset.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

dataset.groupby("Region")["Sales"].sum().plot(kind="pie",autopct='%1.1f%%')
plt.title("Sales by Region")
plt.ylabel("")
plt.show()

dataset.groupby("Month")["Sales"].sum().plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

dataset.groupby("Ship Mode")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")
plt.show()

dataset.groupby("Sub-Category")["Sales"].sum().sort_values().plot(kind="barh")
plt.title("Sales by Sub-Category")
plt.xlabel("Sales")
plt.ylabel("Sub-Category")
plt.show()

dataset.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top 10 Sales by State")
plt.xlabel("State")
plt.ylabel("Sales")
plt.show()

dataset.groupby("Segment")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.show()