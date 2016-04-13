import pandas as pd
'''
df = pd.read_csv("/Users/fushuyue/Dropbox/CME practicum/Apr 15th/Data/esOrderWholeDay.txt")
df = df.iloc[::-1]
df.to_table('/Users/fushuyue/Desktop/inverse.txt')
mydata = []
numberBeforeTrade = 5
nrow = df.shape[0]
ncol = df.shape[1]

for i in df.index:
    if df.ix[i,0] == 'trade':
        mydata.append(df.ix[i,:])
        for j in range(numberBeforeTrade):
            if df.ix[i+1,0] != 'trade':
                mydata[-1]=mydata[-1]+df.ix[i,:]
            else:
                mydata[-1]=mydata[-1]+[]

'''
mydata = []
numberBeforeTrade = 5
flag = 0
count = 0
with open("/Users/fushuyue/Desktop/python/inverse.txt") as input_file:
    for line in input_file:
        a = line.strip().split(',')
        if flag:
            if a[1] == 'submit/cancel':
                mydata[-1] = mydata[-1] + a[3:11]
                count += 1
            else:
                mydata[-1] = mydata[-1] + [0]*(8*(numberBeforeTrade-count))
                count = 0
                flag = 0
            if count == numberBeforeTrade:
                flag = 0
                count = 0

        if a[1] == 'trade':
            mydata.append(a[1:])
            flag = 1

#        if a[2] == '235836949':
#           break

header = ['type','time','best ask','best bid','average bid price','average ask price','ask size','bid size'\
    ,'imbalance','weighted price','buy/sell','trade volume','trade price','best ask1','best bid1','average bid price1','average ask price1','ask size1','bid size1'\
    ,'imbalance1','weighted price1','best ask2','best bid2','average bid price2','average ask price2','ask size2','bid size2'\
    ,'imbalance2','weighted price2','best ask3','best bid3','average bid price3','average ask price3','ask size3','bid size3'\
    ,'imbalance3','weighted price3','best ask4','best bid4','average bid price4','average ask price4','ask size4','bid size4'\
    ,'imbalance4','weighted price4','best ask5','best bid5','average bid price5','average ask price5','ask size5','bid size5'\
    ,'imbalance5','weighted price5']

header3 = ['type','time','best ask','best bid','average bid price','average ask price','ask size','bid size'\
    ,'imbalance','weighted price','buy/sell','trade volume','trade price','best ask1','best bid1','average bid price1','average ask price1','ask size1','bid size1'\
    ,'imbalance1','weighted price1','best ask2','best bid2','average bid price2','average ask price2','ask size2','bid size2'\
    ,'imbalance2','weighted price2','best ask3','best bid3','average bid price3','average ask price3','ask size3','bid size3'\
    ,'imbalance3','weighted price3']

header1 = ['type','time','best ask','best bid','average bid price','average ask price','ask size','bid size'\
    ,'imbalance','weighted price','buy/sell','trade volume','trade price','best ask1','best bid1','average bid price1','average ask price1','ask size1','bid size1'\
    ,'imbalance1','weighted price1']


df = pd.DataFrame(mydata,columns=header)
df = df.ix[::-1]

df.to_csv("keke1.txt")
