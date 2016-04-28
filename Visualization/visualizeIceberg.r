iceberg = read.csv('~/Desktop/python/iceberg.txt')
data=read.csv('~/Dropbox/CME practicum/Apr 22nd/Data/with1BookRec.txt')
fu = iceberg[iceberg$type!='in the spread',]
library('ggplot2')
p = ggplot() + 
	geom_line(data = data, aes(x = time.5.n./10000000, y = trade.price),colour = 'tomato1')+xlab('time')

q = ggplot() + geom_bar(data = data, aes(x = time.5.n./10000000,y=vol), stat ='identity',
                      fill = 'grey28', alpha=0.8, width = 0.5)
f = q + geom_bar(data = fu,aes(x = time/10000000, y=volume), stat = 'identity',
          fill = 'grey60', width = 0.5) + xlab('time') + ylab('order size')

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

multiplot(p,q)