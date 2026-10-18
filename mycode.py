import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}


df = pd.DataFrame(data)

#Adding a new row for version2 
new_row = pd.DataFrame({'Name': ['Eve'], 'Age': [28], 'City': ['Phoenix']})
df = pd.concat([df, new_row], ignore_index=True)

#Adding a new row for version3 
new_row = pd.DataFrame({'Name': ['July'], 'Age': [24], 'City': ['Mexico City']})
df = pd.concat([df, new_row], ignore_index=True)

# Save the DataFrame to a CSV file
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
csv_file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(csv_file_path, index=False)
print(f"CSV file saved to {csv_file_path}")