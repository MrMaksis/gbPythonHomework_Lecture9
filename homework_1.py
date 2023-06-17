import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
filtered_df = df[df['population'] <= 500]

mean_house_value = filtered_df['median_house_value'].mean()

print("Средняя стоимость дома, где количество людей от 0 до 500: ", mean_house_value)