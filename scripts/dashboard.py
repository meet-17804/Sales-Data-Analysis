import pandas as pd
dataset = pd.read_csv(r"C:\Users\Shreya patel\OneDrive\Desktop\Trae\Sales-Data-Analysis\data\train.csv")

dataset.info()
dataset.isnull().sum()

dataset["Order Date"] = pd.to_datetime(dataset["Order Date"], format="mixed")
dataset["Ship Date"] = pd.to_datetime(dataset["Ship Date"], format="mixed")

dataset.describe()