import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

data = []
tradep = []  # temporary storage of trade price
tradev = []  # temporary storage of trade volume
order = []  # storage for order data
date = []  # storage for date
date1 = []
price = []  # storage for price
lots = []  # storage for lots of every order
trade = []
a = [0,0,0,0]  # initialize

def weighted_mean(x,y):
    temp = [x[i]*y[i] for i in range(len(x))]
    return sum(temp)/float((sum(y)))

flag=0

with open('/Users/fushuyue/Dropbox/CME practicum/CMEdata/ESZ5_20150917.txt') as input_file:
    for line in input_file:
        if a[1] == 'TRADEREC':
            flag = True
            # trade data structure: 0 time 1 name; 2 quantity; 3 price; 4 volume; 5 flag
        elif a[1] == 'BOOK10DEEPREC':
            flag = False
        elif a[1] == 'IMPLIEDBOOKREC':
            continue
        # read data line by line
        a = line.strip().split(',')
        #if a[0] == '00:01:04.531':
         #   break

        if a[1] == 'TRADEREC':
            # store trade price and volume
            tradep.append(float(a[3]))
            tradev.append(float(a[2]))

        if a[1] == 'BOOK10DEEPREC':
            temp = [int(k) for k in a[2:62]]
            date_temp = a[0][0:2]+a[0][3:5]+a[0][6:8]+a[0][9:12]

            ask_size = temp[32:44:3]
            ask_price = temp[30:42:3]
            bid_size = temp[15:28:3]
            bid_price = temp[17:30:3]

            average_ask_p = weighted_mean(ask_price, ask_size)
            average_bid_p = weighted_mean(bid_price, bid_size)
            spread = temp[30]-temp[29]

            volume_imbalance = sum(bid_size) - sum(ask_size)
            normalized_imbalance = volume_imbalance/(float(sum(bid_size) + sum(ask_size)))
            mid_price = (ask_price[-1]*ask_size[-1]+bid_price[0]*bid_size[0])/float(ask_size[-1]+bid_size[0])

            weighted_price = (average_ask_p*sum(ask_size)+average_bid_p*sum(bid_size))/float(sum(bid_size)+sum(ask_size))
            # 0=date; 1=bid price; 2=ask price;3=mid point; 4=spread; 5=imba; 6=normailize imba; 7=weighted price; 8=type;

            if flag:
                temp1=sum(tradev)
                lots.append(temp1)
                temp2=weighted_mean(tradep,tradev)
                order.append([date_temp, round(average_bid_p,5), round(average_ask_p,5),volume_imbalance, round(weighted_price,5),'trade',temp2 ])
                tradep = []
                tradev = []
                trade.append([date_temp,temp1,temp2])

            else:
                order.append([date_temp, round(average_bid_p,5), round(average_ask_p,5),volume_imbalance, round(weighted_price,5),'submit/cancel','NA'])
print('finish reading')

dtrade = pd.DataFrame(trade, columns=['date', 'volume', 'price'])
dorder = pd.DataFrame(order, columns=['date', 'bid price', 'ask price', 'imba', 'weighted price', 'type', 'trade price'])
'''
plt.plot(dtrade['price'])
plt.ylim(198100,199000)
plt.show()
'''

plt.hist(lots,bins=10,normed=1)
plt.show()

print('finish plot')

dorder.to_csv('OrderWholeDay.txt')
dtrade.to_csv('TradeWholeDay.txt')

'''
output=open("order.txt", "w")
for i in range(len(order)):
    for k in range(len(order[i])):
        output.write(str(order[i][k]))
        if k != len(order[i])-1:
            output.write(",")
    output.write("\n")
output.close()



output1=open("trade.txt", "w")
for i in range(len(trade)):
    for k in range(len(trade[i])):
        output1.write(str(trade[i][k]))
        output1.write(",")
    output1.write("\n")
output1.close()
'''

