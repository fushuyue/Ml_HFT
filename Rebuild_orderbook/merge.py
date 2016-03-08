order = []
trade = []
date2 = []
date1 = []


with open('order.txt') as input_file:
    for line in input_file:
        a = line.strip().split(',')
        if a[8]=='trade':
            order.append(a)

with open('processed_trade.txt') as input_file:
    for line in input_file:
        trade.append(line.strip().split(','))

m = len(order)
n = len(trade)

print(m)
print(n)



'''
i = 0
for j in range(m):
    # if already gone through every trade data, keep the price unchanged
    if i >= n-1:
        for k in range(j, m):
            order[k].append(trade[i][1])
            order[k].append(0)
        break
    # match every trade with order data; if matched, goto next trade
    if order[j][0] >= trade[i][0]:
        order[j].append(trade[i][1])
        order[j].append(trade[i][2])
        i += 1
    # if not match, keep the price unchange
    else:
        order[j].append(trade[i-1][1])
        order[j].append(0)



print(i)
print(n)

output1=open("test.txt", "w")
for i in range(len(order)):
    for k in range(len(order[i])):
        output1.write(str(order[i][k]))
        output1.write(",")
    output1.write("\n")
output1.close()
'''