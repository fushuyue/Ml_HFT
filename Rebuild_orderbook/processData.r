data=read.csv("/Users/fushuyue/Desktop/clOrderWholeDay.txt",header=T,sep=',')
n=length(data[,1])
# price change from 1 to n-1
pchange=data$trade.price[-1]-data$trade.price[-n]
pchange=pchange[-1]
# attri change from 2 to n
attrichange=data[2:n,3:8]-data[1:(n-1),3:8]
attrichange=attrichange[1:(length(attrichange[,1])-1),]
imba=data$imba[2:(n-1)]
vol=data$trade.volume[2:(n-1)]
a=cbind(attrichange[,1:4],attrichange[,6],imba,vol,pchange)
colnames(a)[1:5]=c('bid.price.change', 'ask.price.change', 'imba.change', 'weighted.price.change','vol.change')
a$pchange=ifelse(a$pchange>0,1,ifelse(a$pchange<0,-1,0))
n=length(a[,1])
b=cbind(a[1:(n-4),6:7],a[2:(n-3),6:7],a[3:(n-2),6:7],a[4:(n-1),6:7],a[5:n,])
colnames(b)[1:8]=c('imba.lag4', 'vol.lag4', 'imba.lag3', 'vol.lag3', 'imba.lag2', 'vol.lag2', 'imba.lag1', 'vol.lag1')
write.csv(b,"keke.csv")