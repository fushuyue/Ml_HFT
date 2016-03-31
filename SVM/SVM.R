setwd("/Users/Peng/Desktop/")
data <-read.table("result.txt",header=T)
data$mid_price_indicator. <-as.numeric(data$mid_price_indicator.)
data$bid.ask_spread_size. <-as.numeric(data$bid.ask_spread_size.)
data$price_indicator <-as.numeric(data$price_indicator)
n <-nrow(data)*.8
x <-data[1:n,1:2]
y <-data[1:n,3]
g=y[y!=0]
f=x[y!=0,]
model <-svm(f,g)
training <-data[(n+1):nrow(data),1:2]
z <-data[(n+1):nrow(data),3]
t=training[z!=0,]
z=z[z!=0]
pred <-predict(model,training)
u=ifelse(pred>0,1,-1)
table(u,z)