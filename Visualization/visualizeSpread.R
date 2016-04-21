setwd('~/Dropbox/CME practicum/Apr 22nd/SVM/testing set/')
tdata=read.csv("with1_80_20_testing_data.csv")
data=read.csv('~/Desktop/python/esOrderWholeDay.txt')
time=tdata$time.5.n.
Data=data[data$time>=time[1],]

fu = tdata[30:100,]
time = fu$time.5.n
df = Data[Data$time <= time[71],]
df = df[df$time>=time[1],]
accr = ifelse(fu$real==fu$pred,'right','wrong')
fu = cbind(fu,accr)

fu$time.5.n = fu$time.5.n/1000
df$time = df$time/1000
fu$real1 = ifelse(fu$real1 == 1, 'firebrick1', 'green')


p = ggplot()+geom_line(data = df,aes(x = time/10000,y = best.ask+30,colour = best.ask.size),size = 3)+
    xlab('time')+ylab('price')

p = p+geom_line(data = df,aes(x = time/10000,y = best.bid-30,colour = best.bid.size), size = 3)

p = p + scale_color_gradient(name = 'liquidity of \nask and bid',low = 'pink', high = 'red')

fuup = fu[fu$real1 == 'firebrick1',]
fudown = fu[fu$real1 == 'green',]

p1 = p + geom_point(data = fuup,aes(x = time.5.n/10000, y = trade_price1, alpha = 0.8, shape = factor(accr)),colour = 'blue',size = 5)
p1 = p1 + geom_point(data = fudown,aes(x = time.5.n/10000, y = trade_price1, alpha = 0.8, shape = factor(accr)),colour = 'black',size = 5)
p1 = p1  + guides(alpha = F) + scale_shape_discrete(name = 'prediction outcome', solid = F) + guides(alpha=F)

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
