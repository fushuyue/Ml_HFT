## Price Prediction with Machine Learning Models
This project proposed a machine learning (Logistic Regreesion and SVM) framework to predict price movement in a high frequency environment and build trading strategy based on this prediction. <br>

###The project has three main parts:<br>
#####Part 1: Data processing and visualization
- Data for this project is the limit order book of E-mini S&P500 future. A sample data is in sample_data folder.<br>
- Training set is created at every trade entry with attributes calculate from previous book entry. <br>
- Target value is the directional movement of next trade price.<br>
- 'ggplot' package is used for visualization

#####Part 2: Model training and testing
- Logistic Regression with nearly 78% accuracy
- Support Vector Machines with nearly 87% accuracy

#####Part 3: Iceberg Detection
- Introduce the basic idea of iceberg order detection algorithm
- Found more than 11,000 iceberg orders within one day

<img src="https://raw.githubusercontent.com/fushuyue/Machine_Learning_Price_Prediction/master/Visualization/iceberg.png" width="300" height="300" />
---
> 
Shuyue Fu<br>
MSFE candidate at University of Illinois at Urbana-Champaign<br>
My Resume：[Shuyue Fu](https://github.com/fushuyue/Financial_Computing/raw/master/MyResume/MyResume.pdf)<br>
My Linkedln：[Linkedln](https://www.linkedin.com/in/shuyuefu)<br>
My Email：sfu11@illinois.edu
