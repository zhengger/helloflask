import pandas as pd


df = pd.DataFrame(data=[[1,2,3], [4,5,6], [7,8,9]], index=[1,2,3], columns=['age', 'height', 'gender'])
print(df)
