import pandas as pd
data = {
'EmployeeID': ['E02001', 'E02002', 'E02003', 'E02004'],
'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Department': ['IT', 'HR', 'IT', 'Finance'],
'Gender': ['Female', 'Male', 'Male', 'Male']
}
employee_df = pd.DataFrame(data)
def createCollection(collection_name):
global employee_df
employee_df = employee_df.copy()
print(f"Collection '{collection_name}' created.")
def getEmpCount():
count = len(employee_df)
print(f"Employee count: {count}")
return count
def indexData(column_name, new_data):
global employee_df
new_df = pd.DataFrame(new_data)
employee_df = pd.concat([employee_df, new_df], ignore_index=True)
print(f"Data indexed based on column '{column_name}'.")
def delEmpById(emp_id):
global employee_df
employee_df = employee_df[employee_df['EmployeeID'] != emp_id]
print(f"Employee with ID '{emp_id}' deleted.")
def searchByColumn(column_name, value):
results = employee_df[employee_df[column_name] == value]
print(f"Search results for {column_name} = '{value}':")
print(results)
return results
def getDepFacet():
facets = employee_df['Department'].value_counts()
print(f"Department facets:")
print(facets)
return facets
v_nameCollection = 'Hash_YourName'
v_phoneCollection = 'Hash_1234'
createCollection(v_nameCollection)
createCollection(v_phoneCollection)
getEmpCount()
indexData('Department', [{'EmployeeID': 'E02005', 'Name': 'Eve', 'Department': 'IT', 'Gender': 'Female'}])
indexData('Gender', [{'EmployeeID': 'E02006', 'Name': 'Frank', 'Department': 'HR', 'Gender': 'Male'}])
getEmpCount()
delEmpById('E02003')
getEmpCount()
searchByColumn('Department', 'IT')
searchByColumn('Gender', 'Male')
getDepFacet()
