from numpy import *




def getcomb():
    import scipy.special as sp
    fr = open('/Users/shengdongliu/Downloads/0401.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        totalcolumn=len(lineArr)-2
        break
    number=sp.comb(totalcolumn,2,exact=False)
    return number

def settwofactor(number):
    import itertools
    a=list(itertools.combinations('abcdefghijklmno',2))
    col1=ord(str(a[number][0]))-97
    col2=ord(str(a[number][1]))-97
    #col3=ord(str(a[number][2]))-97
    return col1,col2

def readheader():
    import csv
    with open('/Users/shengdongliu/Downloads/data-2.csv', 'rb') as inputfile:
        reader = csv.reader(inputfile)
        head= list(reader)

    return head[0][1:16]


def loadDataSet(col1,col2):
    dataMat = []; labelMat = []
    fr = open('/Users/shengdongliu/Downloads/eminicsv.txt')
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
#        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1]),float(lineArr[2]),float(lineArr[3]),float(lineArr[4])])
        dataMat.append([1.0,float(lineArr[col1]),float(lineArr[col2])])
                           #,float(lineArr[col3])])
        labelMat.append(int(lineArr[15]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #convert to NumPy matrix
    labelMat = mat(classLabels).transpose() #convert to NumPy matrix
    m,n = shape(dataMatrix)
    alpha = 0.01
    maxCycles = 150
    weights = ones((n,1))
    for k in range(maxCycles):              #heavy on matrix operations
        h = sigmoid(dataMatrix*weights)     #matrix mult
        error = (labelMat - h)              #vector subtraction
        weights = weights+alpha * dataMatrix.transpose()* error #matrix mult
    return weights

def plotBestFit(col1,col2):
    
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    # weights=wei.getA()
    dataMat,labelMat=loadDataSet(col1,col2)
    dataArr = array(dataMat)
    #print dataArr
        #weights=gradAscent(dataArr,labelMat)
    # w0=weights[0]
    # w1=weights[1]
    # w2=weights[2]
    
    n = shape(dataArr)[0]
    #  print n
    xcord1 = []; ycord1 = [];zcord1=[]

    xcord2 = []; ycord2 = [];zcord2=[]
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
            #zcord1.append(dataArr[i,3])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
            #zcord2.append(dataArr[i,3])
    #print xcord1
    fig = plt.figure()
    ax = fig.add_subplot(111)
                         #,projection='3D')
    ax.scatter(xcord1, ycord1,s=30, c='red', marker='s')

    ax.scatter(xcord2, ycord2, s=30, c='green')
        #x = arange(-30,50, 0.11)
    #print weights.item(0)
        #y = (-weights.item(0)-weights.item(1)*x)/weights.item(2)
    # print y
    #  print x
        #ax.plot(x, y)
    #axes = plt.gca()
        # axes.set_xlim([-1,0.5])
        #axes.set_ylim([-0.5,1])
    #axes.set_ylim([0.5,1.5])
    name=readheader()
    #print name
    #print name
    str1='emini_'+str(name[col1])
    str2='emini_'+str(name[col2])
    str1=str1.replace(".", "_")
    str2=str2.replace(".", "_")
    plt.xlabel(str1); plt.ylabel(str2);
    #plt.show()
    s=str1+'-'+str2
    plt.savefig(s+'.pdf')


def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones((n,1))   #initialize to all ones
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights

def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)   #initialize to all ones
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.001    #apha decreases with iteration, does not
            randIndex = int(random.uniform(0,len(dataIndex)))#go to 0 because of the constant
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

def Test():
    import csv
    frTrain = open('/Users/shengdongliu/Downloads/eminitrain.txt'); frTest = open('/Users/shengdongliu/Downloads/eminitest.txt')
    #print 1
    #frTrain = open('Training.txt'); frTest = open('Test.txt')
    column=15
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        #print 2

        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(column):
            lineArr.append(float(currLine[i]))
        #print 3
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[column]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 100)
    #print 4
    errorCount = 0; numTestVec = 0.0
    upcount=0.0;downcount=0.0;
    totalup=0.0;totaldown=0.0;
    predict=[]
    for line in frTest.readlines():
        numTestVec += 1.0
        if int(currLine[column])==1:
                totalup+=1
        if int(currLine[column])==0:
                totaldown+=1
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(column):
            lineArr.append(float(currLine[i]))

        if int(classifyVector(array(lineArr), trainWeights))!= int(currLine[column]):
            errorCount += 1
            if int(currLine[column])==1:
                upcount+=1
            if int(currLine[column])==0:
                downcount+=1

        predict.append(int(classifyVector(array(lineArr), trainWeights)))

    errorRate = (float(errorCount)/numTestVec)
    up_correct_Rate = 1-(float(upcount)/totalup)
    down_correct_Rate=1-(float(downcount)/totaldown)

    file = open("/Users/shengdongliu/Downloads/towu.txt", "w")
    for n in range(len(predict)) :
        file.write(str(predict[n]))
        file.write("\n")
    errorRate=1-errorRate
    print "correct rate is: %f" %errorRate
    print "correct up rate: %f" %up_correct_Rate
    print "correct down rate: %f" %down_correct_Rate

    return errorRate

def multiTest():
    numTests = 10; errorSum=0.0
    for k in range(numTests):
        errorSum += Test()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests))
#csvtotxt()
Test()
#multiTest()

#readheader()
# for n in range(int(getcomb())):
#       col1,col2=settwofactor(n)
#       plotBestFit(col1,col2)
#
#
