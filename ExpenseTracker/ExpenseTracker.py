import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,35],
    'City': ['New York', 'Los Angeles', 'Chicago']       
}

df = pd.DataFrame
print("Original DataFrame")
print(df)

print("\nAccess the 'Name' column:")
print(df['Name'])

print("\nAccess the second row using iloc:")
print(df.ilco[1])

df['Salary'] = [70000, 80000, 75000]
print("\nDataFrame after adding a new column 'Salary:")
print(df)

filtered_df + df[df['Age'] > 28]
print("\nFiltered DataFrame where Age > 28:")
print(filtered_df)

average_salary = df['Sarlary'].mean()
print(f"\nAverage Salary: {average_salary}")