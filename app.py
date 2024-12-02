import pandas as pd
import random
namelist=["John","Kirthik","Kiran","Boss"]
print(random.choice(namelist))


import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
