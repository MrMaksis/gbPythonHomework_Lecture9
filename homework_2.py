import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

min_population = df['population'].min()
filtered_df = df[df['population'] == min_population]

max_households = filtered_df['households'].max()

print("Максимальное значение households в зоне минимального значения population:", max_households)