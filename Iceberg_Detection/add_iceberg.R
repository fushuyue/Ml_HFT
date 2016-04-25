data=read.csv('~/Dropbox/CME practicum/Apr 22nd/Data/with1BookRec.txt')
iceberg=read.csv('~/Desktop/python/iceberg.txt')
iceberg=iceberg[iceberg$type!='in the spread',]
n = length(iceberg[,1])
for(i in 1:n){

	if(iceberg$buy.sell)
		data$book1.best.ask.size[data$time.5.n==iceberg$time[i]] = iceberg$volume[i]+
		data$book1.best.ask.size[data$time.5.n==iceberg$time[i]]
	else
		data$book1.best.bid.size[data$time.5.n==iceberg$time[i]] = iceberg$volume[i]+
		data$book1.best.bid.size[data$time.5.n==iceberg$time[i]]

}