import pandas as pd
from faker import Faker

# Initialize faker generator
fake = Faker()

# Define the number of rows and columns
num_rows = 100
num_cols = 5

# Generate data for each column
data = {f'column_{i+1}': [fake.pystr_format() for _ in range(num_rows)] for i in range(num_cols)}

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('testing_certData.xlsx', index=False)

# Read the Excel file
df = pd.read_excel('testing_certData.xlsx')

# Filter rows where 'column_1' is equal to 'some_value'
filtered_df = df[df['column_1'] == 'some_value']

# Manipulate data: Add a new column that is the length of the value in 'column_1'
df['column_1_length'] = df['column_1'].apply(len)

# Write the DataFrame back to the Excel file
df.to_excel('DevTest_JoinMulDataSet_MOCData.xlsx', index=False)