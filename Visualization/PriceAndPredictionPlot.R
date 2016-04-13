multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)

  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)

  numPlots = length(plots)

  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                    ncol = cols, nrow = ceiling(numPlots/cols))
  }

 if (numPlots==1) {
    print(plots[[1]])

  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))

    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))

      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}




setwd('~/Dropbox/CME practicum/Data/Apr 15th/')
tdata=read.csv("tradeDataForPlotting.txt")
p=tdata$trade.price
n=length(p)
pchange=p[-1]-p[-n]
p=ifelse(pchange>0,'up',ifelse(pchange<0,'down','stay'))
direction=tdata$buy.sell
direction[direction==0]=-1
nd=length(direction)
for(i in 2:nd){
	if(direction[i]*direction[i-1]>0)
		direction[i]=direction[i-1]+direction[i]
}
tdata$buy.sell=direction


tdata=cbind(tdata[1:(n-1),],p)
library(ggplot2)
test=tdata[tdata$p!='stay',]
n=length(tdata[,1])
test=tdata[(n+1-11397):n,]
qplot(test$trade.volume,data=test,geom="density",colour=p,xlim=c(0,15))

data=read.csv("~/Dropbox/CME practicum/Apr 15th/Data/esOrderWholeDay.txt")
trade=read.csv("~/Desktop/python/esTradeWholeDay.txt")
data=cbind(data,0)
colnames(data)[14]='movement'
type=data$type
data$movement[type=='trade']=trade$next.price.move

# svm
 n <-nrow(df)*.8
> x <-df[1:n,3:12]
> y <-df[1:n,14]
> g=y[y!=0]
> g=as.factor(g)
> f=x[y!=0,]
> library('e1071')
> model <-svm(f,g, kernel = "radial")
training <-df[(n+1):nrow(df),3:12]
> z <-df[(n+1):nrow(df),14]
> t=training[z!=0,]
> z=z[z!=0]
> pred <-predict(model,t)

training <-df[(n+1):nrow(df),1:13]
z <-df[(n+1):nrow(df),14]
t=training[z!=0,]
fu1=data.frame(t,z,pred)
accr=ifelse(fu1$z==fu1$pred,1,0)
fu1=data.frame(fu1,accr)
fu1=fu1[1:(length(fu1[,1])-1),]

accr_rate=vector()
accr_rate[1]=0
for(i in 101:length(accr)){
	accr_rate[i-100]=sum(accr[i-100:i]/i)
}



vol=data$trade.volume[type=='trade']
n=length(vol)
vchange=vol[-1]-vol[-n]
vchange=ifelse(vchange<0,'decrease',ifelse(vchange>0,'increase','stay'))
data=cbind(data,0)
colnames(data)[15]='vol.movement'
vchange1=c(0,vchange)
data$vol.movement[data$type=='trade']=vchange1


fu=data[data$time>=143656051,]
n=length(fu[,1])
time=fu$time
time=(time-time[1])/1000
fu$time=time

n=length(fu1[,1])
time=fu1$time
time=(time-time[1])/1000
fu1$time=time


#fu1=fu[fu$type=='trade',]
#fu1$trade.price=ifelse(fu1$buy.sell==1,fu1$trade.price+200,fu1$trade.price-200)
#fu$trade.price[fu$type=='trade']=fu1$trade.price

fu=fu[fu$time>=25000,]
fu1=fu1[fu1$time>=25000,]
wrong=fu1[fu1$accr==0,]
wrong$z[wrong$z==-1]='dark blue'
wrong$z[wrong$z==1]='grey'


right=fu1[fu1$accr==1,]
right$z[right$z==-1]='dark blue'
right$z[right$z==1]='grey'

p=ggplot()+geom_line(data=fu,aes(x=time,y=best.ask+200,colour='ask'))+xlab('time')+ylab('price')
p=p+geom_line(data=fu,aes(x=time,y=best.bid-200,colour='bid'))+xlab('time')+ylab('price')
p=p+geom_line(data=fu,aes(x=time,y=trade.volume+197000,color='dark blue',alpha=0.6))
p1=p+geom_point(x=wrong$time,y=wrong$trade.price,data=wrong,color=wrong$z)+labs(title="plot of wrong prediction")
p2=p+geom_point(x=right$time,y=right$trade.price,data=right,color=right$z)+labs(title="plot of right prediction")
p3=qplot(x=time,y=accr_rate*100,data=fu2,geom="line",ylim=c(60,100),main="Accuracy of prediction")

multiplot(p1,p2,p3)



#fu1$trade.price=ifelse(fu1$z==1,fu1$trade.price+200,fu1$trade.price-200)






















