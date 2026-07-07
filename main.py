import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
print(df.head())
print(df.columns.tolist())

#Data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns.tolist())
df = df.drop_duplicates()

# Numaric column cleaning
df["price"]= df["price"].astype(str).str.replace(",", "").astype(float)
df["area"]= df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"]= df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)
# print(df["rate_per_sqft"])
# print(df["price"])
# print(df["area"])

#Categorical column cleaning
df["status"] = df["status"].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()
df = df.drop_duplicates()
# print(df) 
# print(df.info())

# print(df["status"])
# print(df["rera_approval"])
# print(df["flat_type"])


#Question-1. Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]    
print(costliest_flat) 

'''
price                                1226300000.0
status                              ready to move
area                                        16500
rate_per_sqft                               74323
property_type    6 BHK Apartment in DLF Camellias
locality                                Sector 42
builder_name                    Provident Capital
rera_approval                               False
bhk_count                                       6
society                             DLF Camellias
company_name                                  DLF
flat_type                               apartment
'''
print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000} crores in {costliest_flat['society']} built by {costliest_flat['builder_name']} and it is {costliest_flat['status']} with a rate per sqft of {costliest_flat['rate_per_sqft']}.")


#Question-2.Which locality has the highest average price?
locality_avg_price = df.groupby('locality')['price'].mean()
highest_avg_price_locality = locality_avg_price.idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality} with an average price of {locality_avg_price[highest_avg_price_locality]/10000000} crores.")


#Question-3. Which locality has the highest rate per square foot?
locality_avg_rate_per_sqft = df.groupby('locality')['rate_per_sqft'].mean()
highest_avg_rate_locality = locality_avg_rate_per_sqft.idxmax()
print(f"The locality with the highest average rate per square foot is {highest_avg_rate_locality} with an average rate of {locality_avg_rate_per_sqft[highest_avg_rate_locality]}.")

# Question-4.Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print(f"Ready-to-move properties cost more than under-construction properties.")
else:    
    print(f"Under-construction properties cost more than ready-to-move properties.")

# Question-5.Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > not_rera_approved_avg_price:
    print(f"RERA-approved properties command a price premium.")
else:
    print(f"RERA-approved properties do not command a price premium.")
    
# Question-6.How does area (sqft) impact property price?
sns.scatterplot(x='area', y='price', data=df)
plt.title('Area vs Price')
plt.xlabel('Area (sqft)')   
plt.ylabel('Price')
plt.show()    

# Question-7 Which BHK configuration is the most expensive on average?
bhk_avg_price = df.groupby('bhk_count')['price'].mean()
most_expensive_bhk = bhk_avg_price.idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")

# Question-8 Which property type (Apartment, Floor, Plot) is the costliest?
property_type_avg_price = df.groupby('property_type')['price'].mean()
costliest_property_type = property_type_avg_price.idxmax()  
print(f"The costliest property type on average is {costliest_property_type}.")

# Question-9 Do certain builders or companies consistently price higher?
builder_avg_price = df.groupby('builder_name')['price'].mean()
company_avg_price = df.groupby('company_name')['price'].mean()
print(f"The builder with the highest average price is {builder_avg_price.idxmax()}.")
print(f"The company with the highest average price is {company_avg_price.idxmax()}.")

# Question-10 Are larger homes always more expensive per square foot?
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area vs Rate per Square Foot')   
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Square Foot')
plt.show()
