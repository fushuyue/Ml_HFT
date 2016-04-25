import pandas as pd

df = pd.read_csv("/Users/fushuyue/Desktop/clOrderWholeDay.txt")
n = len(df)
# price change from 0 to n-1
pChange = df['trade price'].sub(df['trade price'].shift())
pChange[pChange>0] = 1
pChange[pChange<0] = -1

# attrChange from 1 to n
attrChange = df.ix[:,2:6].sub(df.ix[:,2:6].shift())
imba1 = df.ix[1:,4]
vChange = df['trade volume'].sub(df['trade volume'].shift())

frame = [attrChange.ix[1:,:],imba1,vChange[1:]]
df2 = pd.concat(frame)

print(frame)

