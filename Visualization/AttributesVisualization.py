def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet1.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
#        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1]),float(lineArr[2]),float(lineArr[3]),float(lineArr[4])])
        dataMat.append([1.0,float(lineArr[2]),float(lineArr[4])])
        labelMat.append(int(lineArr[5]))
    return dataMat,labelMat


def sguess():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import csv
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import style
    style.use("ggplot")
    from sklearn import svm


    dataMat = []; labelMat = []
    n=0
    X = []
    y= []
    with open('/Users/shengdongliu/Desktop/testSet3.csv') as inputfile:
        reader = csv.reader(inputfile)
        lineArr = list(reader)
    for n in range(len( lineArr)) :

    # fr = open('testSet2.txt')
    # for line in fr.readlines():
        print lineArr[n]

#        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1]),float(lineArr[2]),float(lineArr[3]),float(lineArr[4])])
        X.append([float(lineArr[n][0]),float(lineArr[n][1]),float(lineArr[n][2])])
        y.append(int(lineArr[n][4]))
        n=n+1
    print n

    #dataMat,labelMat=loadDataSet()
    # x = [1, 5, 1.5, 8, 1, 9]
    # y = [2, 8, 1.8, 8, 0.6, 11]

    # plt.scatter(x,y)
    # plt.show()

    #X = np.array([[1,2],
                 # [5,8],
                 # [1.5,1.8],
                 # [8,8],
                 # [1,0.6],
                 # [9,11]])
    #y = [0,1,0,1,0,1]


    #clf = svm.SVC(kernel='linear', C = 1.0)
    #clf.fit(X,y)
    # print(clf.predict([0.58,0.76]))
    # print(clf.predict([10.58,10.76]))

    #w = clf.coef_[0]
    #print(w)

    #a = -w[0] / w[1]

    xx = np.linspace(-12,12)
    #yy = a * xx - clf.intercept_[0] / w[1]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #h0 = plt.plot(xx, yy, 'k-', label="non weighted div")
    for k in range(n-1):

        if(int(y[k])==1):
            u=ax.scatter(X[k][0], X[k][1],X[k][2], c = 'red')
        elif(int(y[k]==0)):
            s=ax.scatter(X[k][0], X[k][1],X[k][2], c = 'grey')
        elif(int(y[k]==-1)):
           d=ax.scatter(X[k][0], X[k][1],X[k][2], c = 'green')


    ax.set_xlabel('diff_average_bid')
    ax.set_ylabel('diff_average_ask')
    ax.set_zlabel('diff_weighted_price')
    plt.legend((u, s, d),
           ('go up', 'same', 'go down'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
    #plt.xlim(-12,12)

    #ax.plot(x, y, z, label='parametric curve')

    plt.show()

#sguess()
# import numpy as np
# x,y= np.loadtxt('testSet-cp.txt', delimiter='\t')
# print x
# print y
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC()
clf.fit(X, y)


print(clf.predict([[-0.8, -1]]))