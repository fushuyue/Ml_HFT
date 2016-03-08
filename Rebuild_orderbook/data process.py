data = []
trade = []
trade1 = [[0,0]]
order = []
date = []
date1 = []
price = []
a=[0,0]
def weighted_mean(x,y):
    temp = [x[i]*y[i] for i in range(len(x))]
    return sum(temp)/float((sum(y)))



with open('ESZ5_20150917.txt') as input_file:
    for line in input_file:
        if a[1] == 'TRADEREC':
            flag = True
        else:
            flag = False

        a = line.strip().split(',')
        if a[0] == '13:00:00.002':
            break
       '''
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

            order.append([date_temp, round(average_bid_p,5), round(average_ask_p,5), round(mid_price,5), spread,\
                          volume_imbalance, round(normalized_imbalance,5), round(weighted_price,5)])
            if flag:
                order[-1].append('trade')
            else:
                order[-1].append('submit/cancel')
        '''
        if a[1] == 'TRADEREC':
            # 0 time 1 name; 2 quantity; 3 price; 4 volume; 5 flag
            date_temp = a[0][0:2]+a[0][3:5]+a[0][6:8]+a[0][9:12]
            trade.append([date_temp, a[1], int(a[2]), int(a[3])])
            date.append(date_temp)


'''
for i in range(len(order)):
    print(order[i])
'''

output=open("order.csv", "w")
for i in range(len(order)):
    for k in range(len(order[i])):
        output.write(str(order[i][k]))
        if k != len(order[1]):
            output.write(",")
    output.write("\n")
output.close()

'''
output1=open("trade.txt", "w")
for i in range(len(trade)):
    for k in range(len(trade[i])):
        output1.write(str(trade[i][k]))
        output1.write(",")
    output1.write("\n")
output1.close()


print('finish reading')
n = len(trade)
print(trade[-1][0])
i = 0
print(n)
# merge same trade together using weighted average
for f in range(n):
    if i >= n-1:
        break
    k = date.count(trade[i][0])
    temp = 0
    weights = 0
    for j in range(k):
        temp = temp+trade[i+j][2]*trade[i+j][3]
        weights = weights+trade[i+j][2]
    trade1.append([trade[i][0], temp/weights, weights])
    date1.append(trade[i][0])
    i = i+k
    if i % 1000 == 0:
        print(trade[i][0])

output1=open("processed_trade.txt", "w")
for i in range(len(trade1)):
    for k in range(len(trade1[i])):
        output1.write(str(trade1[i][k]))
        output1.write(",")
    output1.write("\n")
output1.close()



print('finish merging')

'''
