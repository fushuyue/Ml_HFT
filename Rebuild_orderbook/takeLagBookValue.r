data=read.csv("/Users/fushuyue/Desktop/clOrderWholeDay.txt",header=T,sep=',')
ncol=length(data[1,])-1
data=data[,2:(ncol+1)]
n=length(data[,1])
# price change from 1 to n-1
pchange=data$trade.price[-1]-data$trade.price[-n]
pchange=pchange[-1]

direction=data$buy.sell
direction[direction==0]=-1
nd=length(direction)
for(i in 2:nd){
	if(direction[i]*direction[i-1]>0)
		direction[i]=direction[i-1]+direction[i]
}
data$buy.sell=direction


# trade attri change from 2 to n
attrichange=data[2:n,5:14]-data[1:(n-1),5:14]
attrichange=attrichange[1:(length(attrichange[,1])-1),]
imba=data$imbalance[2:(n-1)]
direction=data$buy.sell[2:(n-1)]
vol=data$trade.volume[2:(n-1)]
volchange=attrichange[,10]
bestask=data$best.ask[2:(n-1)]
bestbid=data$best.bid[2:(n-1)]
asksize=data$ask.size[2:(n-1)]
bidsize=data$bid.size[2:(n-1)]
bestasksize=data$best.ask.size[2:(n-1)]
bestbidsize=data$best.bid.size[2:(n-1)]
time=data$time[2:(n-1)]
a=cbind(asksize,bidsize,bestasksize,bestbidsize,imba,vol,volchange,direction,pchange,data$trade.price[2:(n-1)])
a=data.frame(attrichange[,1:8],a)
colnames(a)[1:18]=c('trade.best.ask.size.change', 'trade.best.bid.size.change','trade.bid.price.change', 
					'trade.ask.price.change', 'trade.ask.size.change', 'trade.bid.size.change',
					'trade.imba.change', 'trade.weighted.price.change','ask.size','bid.size','best.ask.size','best.bid.size',
					'imba','vol','vol.change','direction','pchange','trade.price')

a$pchange=ifelse(a$pchange>0,1,ifelse(a$pchange<0,-1,0))
n=length(a[,1])
b=cbind(time[5:n],a[2:(n-3),11:14],a[3:(n-2),11:14],a[4:(n-1),11:14],a[5:n,])
colnames(b)[2:13]=c('bestasksize.lag3','bestbidsize.lag3','imba.lag3', 'vol.lag3',
				   'bestasksize.lag2','bestbidsize.lag2','imba.lag2', 'vol.lag2', 
				   'bestasksize.lag1','bestbidsize.lag1','imba.lag1', 'vol.lag1')
#write.csv(b,"~/Desktop/withoutBookRec.txt")

n=length(data[,1])
lag1=data[2:(n-1),18:25]
diff1=data[2:(n-1),5:12]-lag1
diff1=cbind(diff1,lag1[,1:2],lag1[,5:7])
colnames(diff1)=c('book1.best.ask.size.change', 'book1.best.bid.size.change','book1.bid.price.change', 'book1.ask.price.change', 
				  'book1.ask.size.change', 'book1.bid.size.change','book1.imba.change', 'book1.weighted.price.change',
				  'book1.best.ask.size', 'book1.best.bid.size','book1.ask.size','book1.bid.size','book1.imbalance')

dflag1=cbind(diff1[5:length(a[,1]),],b)
write.csv(dflag1,"~/Desktop/with1BookRec.txt")

lag2=data[2:(n-1),28:35]
diff2=lag1-lag2
diff2=cbind(diff2,lag2[,1:2],lag2[,5:7])
colnames(diff2)=c('book2.best.ask.size.change', 'book2.best.bid.size.change','book2.bid.price.change', 'book2.ask.price.change', 
				  'book2.ask.size.change', 'book2.bid.size.change','book2.imba.change', 'book2.weighted.price.change',
				  'book2.best.ask.size', 'book2.best.bid.size','book2.ask.size','book2.bid.size','book2.imbalance')

lag3=data[2:(n-1),38:45]
diff3=lag2-lag3
diff3=cbind(diff3,lag3[,1:2],lag3[,5:7])
colnames(diff3)=c('book3.best.ask.size.change', 'book3.best.bid.size.change','book3.bid.price.change', 'book3.ask.price.change', 
				  'book3.ask.size.change', 'book3.bid.size.change','book3.imba.change', 'book3.weighted.price.change',
				  'book3.best.ask.size', 'book3.best.bid.size','book3.ask.size','book3.bid.size','book3.imbalance')

dflag3=cbind(diff3[5:length(a[,1]),],diff2[5:length(a[,1]),],dflag1)
write.csv(dflag3,"~/Desktop/with3BookRec.txt")

lag4=data[2:(n-1),40:45]
diff4=lag3-lag4
diff4=cbind(diff4,lag4[,3:5])
colnames(diff4)=c('book4.bid.price.change', 'book4.ask.price.change', 'book4.ask.size.change', 'book4.bid.size.change',
					'book4.imba.change', 'book4.weighted.price.change','book4.ask.size','book4.bid.size','book4.imbalance')

lag5=data[2:(n-1),48:53]
diff5=lag4-lag5
diff5=cbind(diff5,lag5[,3:5])
colnames(diff5)=c('book5.bid.price.change', 'book5.ask.price.change', 'book5.ask.size.change', 'book5.bid.size.change',
					'book5.imba.change', 'book5.weighted.price.change','book5.ask.size','book5.bid.size','book5.imbalance')


dflag5=cbind(diff5[5:length(a[,1]),],diff4[5:length(a[,1]),],dflag3)

write.csv(dflag5,"~/Desktop/with5BookRec.txt")











