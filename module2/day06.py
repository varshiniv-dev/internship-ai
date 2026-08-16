# Data handling and visualization numpy and pandas, matplotlib and seaborn
import pandas as pd  # pandas - excel inside the python
import numpy as np  # numpy - helps to calculate the data
sale = np.array([100, 200, 300, 400, 500])
print("Mean:", np.mean(sale))
print("Median:", np.median(sale))
print("Standard Deviation:", np.std(sale))
print("Variance:", np.var(sale))
print("Sum:", np.sum(sale))
print("Max:", np.max(sale))
print("Min:", np.min(sale))
print("Average:", np.average(sale))


# diff btw array and list. array- faster for numerical operations, list- more flexible and can hold different data types
np.zeros(10)
np.ones(10)
np.arange(1, 11)
total = int(np.sum(np.arange(1, 11)))

print(total)

array = np.array([1, 2, 3, 4, 5])
list = [1, 2, 3, 4, 5]
print("Array:", array)
print("List:", list)

# pandas -
student = {"Name": ["Ella", "Stella"], "Marsks": [80, 95]}
print(student)
df = pd.DataFrame(student)  # dataframe = df
print(df)
