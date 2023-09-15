import pandas as pd

data = {'A': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

idx = df['A'].idxmax()
print(idx)