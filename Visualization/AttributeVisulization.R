data = read.csv('~/Dropbox/CME practicum/Apr 22nd/Data/with1BookRec.txt')
library('ggplot2')
df = data[data$pchange != 0, ]
df$pchange = ifelse(df$pchange < 0, 'down', 'up')
ask = ggplot(data = df[1:1000,], aes(x = trade.best.ask.size.change, fill = factor(pchange))) +
		geom_histogram(alpha = 0.5, position = 'identity',bins = 50) +
			scale_fill_discrete(name='price change')+xlim(c(-100,100))+ylim(c(0,50))+guides(fill=FALSE) +
      ggtitle('histogram of best ask size change between trades') +
      theme(axis.title.x = element_text(colour="dark grey", size=10)) + ylab('')

bid = ggplot(data = df[1:1000,], aes(x = trade.best.bid.size.change, fill = factor(pchange))) +
		geom_histogram(alpha = 0.5, position = 'identity',bins = 50) +
			scale_fill_discrete(name='price change')+xlim(c(-100,100))+ylim(c(0,50))+guides(fill=FALSE) +
      ggtitle('histogram of best bid size change between trades') +
      theme(axis.title.x = element_text(colour="dark grey", size=10)) + ylab('')

askbidPoint = ggplot(data = df[1:150,], aes(x = trade.best.bid.size.change, y = trade.best.ask.size.change,
				colour = factor(pchange))) + geom_point() + scale_colour_discrete(name='price change') +
				xlim(c(-40,40))+ylim(c(-50,50))

imba = ggplot(data = df[1:10000,], aes(x = trade.imba.change, fill = factor(pchange))) +
		geom_histogram(alpha = 0.5, position = 'identity',bins = 100) +
			scale_fill_discrete(name='price change')+ylim(c(0,60))+xlim(c(-400,400)) + guides(fill=FALSE) +
      ggtitle('histogram of imbalance change between trades') +
      theme(axis.title.x = element_text(colour="dark grey", size=10)) + ylab('')

imbaChange = ggplot(data = df[1:10000,], aes(x = book1.imba.change, fill = factor(pchange))) +
		geom_histogram(alpha = 0.5, position = 'identity',bins = 100) +
			scale_fill_discrete(name='price change')+guides(fill=FALSE)+ylim(c(0,60))+xlim(c(-400,400)) +
      ggtitle('histogram of imbalance change between books') +
      theme(axis.title.x = element_text(colour="dark grey", size=10)) + ylab('')

imbaPoint = ggplot(data = df[1:500,], aes(x = trade.imba.change, y = book1.imba.change,
				colour = factor(pchange))) + geom_point() + scale_colour_discrete(name='price change') +
				xlim(c(-50,50))+ylim(c(-25,25))+ guides(fill=FALSE)

volume = ggplot(data = df[1:500,], aes(x = vol.change, fill = factor(pchange))) +
		geom_histogram(alpha = 0.5, position = 'identity',bins = 70) +
			scale_fill_discrete(name='price change') +
			xlim(c(-30,30))+ylim(c(0,30)) + 
      ggtitle('histogram of volume between trades') +
      theme(axis.title.x = element_text(colour="dark grey", size=10)) + ylab('')

direction = ggplot(data = df[1:500,], aes(x = direction, fill = factor(pchange))) +
		geom_histogram(alpha = 0.5, position = 'identity',bins = 70) +
			scale_fill_discrete(name='price change') +
			xlim(c(-30,30))+ylim(c(0,30)) + xlab('number of consecutive direction trades') +
      ggtitle('histogram of bnumber of consecutive direction trades') +
      theme(axis.title.x = element_text(colour="dark grey", size=10)) + ylab('')

strangePoint = ggplot(data = df[1:500,], aes(x = direction, y = vol.change,
				colour = factor(pchange))) + geom_point() + scale_colour_discrete(name='price change') +
				xlim(c(-25,25))+ylim(c(-25,25))+ xlab('number of consecutive direction trades')


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
    layout <- t(layout)
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




