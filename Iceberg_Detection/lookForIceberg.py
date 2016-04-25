import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
iceberg = []
dictionary = {}
tradep = []  # temporary storage of trade price
tradev = []  # temporary storage of trade volume
a = [0,0,0,0]  # initialize
iceberg_flag = 0
flag=0

with open('/Users/fushuyue/Desktop/python/ESZ5_20150917.txt') as input_file:
    for line in input_file:

        # trade data structure: 0 time 1 name; 2 quantity; 3 price; 4 volume; 5 flag
        # keep track of the type of last update
        if a[1] == 'TRADEREC':
            flag = True
        else:
            flag = False

        # read data line by line
        a = line.strip().split(',')


        if a[1] == 'TRADEREC':

            date_temp1 = a[0][0:2]+a[0][3:5]+a[0][6:8]+a[0][9:12]

            if float(a[3]) > bid1:
                # buy order
                aggressor = 1
                levelOneAsk = [ask1, ask1_size]
            else:
                # sell order
                aggressor= 0
                levelOneBid = [bid1, bid1_size]

            # buy order when big price appear first, there is iceberg order
            # the opposite for sell order
            if len(tradep) != 0:
                if aggressor:
                    if float(a[3]) < tradep[-1]:
                        # iceberg.append([date_temp, a[3]])
                        iceberg_flag = 1
                        iceberg_price = float(a[3])
                        iceberg_time = date_temp1
                else:
                    if float(a[3]) > tradep[-1]:
                        iceberg_flag = 1
                        iceberg_price = float(a[3])
                        iceberg_time = date_temp1

            tradep.append(float(a[3]))
            tradev.append(float(a[2]))

             # one trade may have different price so
             # store trade price and volume in a dictionary
             # use trade price as key, trade volume as value

            if float(a[3]) not in dictionary.keys():
                dictionary[float(a[3])] = float(a[2])
            else:
                dictionary[float(a[3])] += float(a[2])


        if a[1] == 'BOOK10DEEPREC':
            temp = [int(k) for k in a[2:62]]
            date_temp = a[0][0:2]+a[0][3:5]+a[0][6:8]+a[0][9:12]

            ask_size = temp[32:60:3]
            ask_price = temp[30:58:3]
            bid_size = temp[0:28:3]
            bid_price = temp[2:30:3]
            bid1=temp[29]
            ask1=temp[30]
            ask1_size = ask_size[0]
            bid1_size = bid_size[-1]

            # if this is the book updates right after a trade happens
            if flag:

                # if the trade price is in the spread, means there's iceberg order in the spread
                # cannot figure out the whole iceberg order size
                if aggressor:
                    if levelOneAsk[0] not in dictionary.keys():
                        iceberg.append([date_temp1, min(dictionary.keys()), dictionary[min(dictionary.keys())], levelOneAsk[1], aggressor, 'in the spread'])
                        continue
                else:
                    if levelOneBid[0] not in dictionary.keys():
                        iceberg.append([date_temp1, max(dictionary.keys()), dictionary[max(dictionary.keys())], levelOneBid[1], aggressor, 'in the spread'])
                        continue

                # if we already know there is iceberg order
                if iceberg_flag:
                    if aggressor:
                        # there's different price and larger price happens first
                        if dictionary[iceberg_price] < levelOneAsk[1]:
                            # if the displayed level one has not been fully executed
                            iceberg.append([iceberg_time, iceberg_price, dictionary[iceberg_price], levelOneAsk[1], aggressor, 'part,need check'])
                        else:
                            if levelOneAsk[0] == ask1:
                                # if the displayed level one has not been fully executed, but refreshed
                                iceberg.append([iceberg_time, iceberg_price, dictionary[iceberg_price], levelOneAsk[1], aggressor, 'part'])
                            else:
                                # not refreshed, still needs to check next updates
                                # if next bookupdates shows level one been refreshed, then needs to check for if bid level moves
                                iceberg.append([iceberg_time, iceberg_price, dictionary[iceberg_price], levelOneAsk[1], aggressor, 'whole'])
                    else:
                        if dictionary[iceberg_price] < levelOneBid[1]:
                            iceberg.append([iceberg_time, iceberg_price, dictionary[iceberg_price], levelOneBid[1], aggressor, 'part'])
                        else:
                            if levelOneBid[0] == bid1:
                                iceberg.append([iceberg_time, iceberg_price, dictionary[iceberg_price], levelOneBid[1], aggressor, 'part'])
                            else:
                                iceberg.append([iceberg_time, iceberg_price, dictionary[iceberg_price], levelOneBid[1], aggressor, 'whole'])

                # if in a buy order, volume is larger than best ask size, we know there is iceberg
                else:
                    if aggressor:
                        if dictionary[levelOneAsk[0]] > levelOneAsk[1]:
                            # if level one moves
                            if levelOneAsk[0] != ask1:
                                iceberg.append([date_temp1, levelOneAsk[0], dictionary[levelOneAsk[0]], levelOneAsk[1], aggressor, 'whole'])
                            else:
                                iceberg.append([date_temp1, levelOneAsk[0], dictionary[levelOneAsk[0]], levelOneAsk[1], aggressor, 'part'])

                    else:
                        if dictionary[levelOneBid[0]] > levelOneBid[1]:
                            if levelOneBid[0] != bid1:
                                iceberg.append([date_temp1, levelOneBid[0], dictionary[levelOneBid[0]], levelOneBid[1], aggressor, 'whole'])
                            else:
                                iceberg.append([date_temp1, levelOneBid[0], dictionary[levelOneBid[0]], levelOneBid[1], aggressor, 'part'])

                # empty the variable
                iceberg_flag = 0
                tradep = []
                tradev = []
                dictionary = {}




df = pd.DataFrame(iceberg, columns = ['time', 'price', 'volume', 'displayed size', 'buy/sell', 'type'])

df.to_csv('iceberg.txt',index=False)

