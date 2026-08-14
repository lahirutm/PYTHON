from ucimlrepo import fetch_ucirepo
import pandas as pd
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

file = pd.read_csv('https://archive.ics.uci.edu/static/public/53/data.csv')

no_of_lines = 0
unique_names = set()

for index, row in file.iterrows():
    # Access specific columns using the column name
    # print(f"Row Index: {index}")
    # print(row)

    unique_names.add(row['class'])
    
    no_of_lines = no_of_lines + 1

print("\nTotal no. of lines: " + str(no_of_lines))

print(f"Found {len(unique_names)} unique names in the first column:")
print(list(unique_names))