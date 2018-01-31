from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import random

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def q5():
    accuracy = []   #testPenData
    for i in range(5):
        accuracy.append(testPenData()[1])
    max = 0
    average = 0
    stdDev = 0
    total = 0
    for a in accuracy:
        if (a > max):
            max = a
        total += a
    average = total / 5.0
    stdDev = stDeviation(accuracy)
    print "PenTest"
    print "max: {0}".format(max)
    print "average: {0}".format(average)
    print "stdDev: {0}".format(stdDev)

    accuracy = []   #testCarData
    max = 0
    average = 0
    stdDev = 0
    for i in range(5):
        accuracy.append(testCarData()[1])
    max = 0
    average = 0
    stdDev = 0
    total = 0
    for a in accuracy:
        if (a > max):
            max = a
        total += a
    average = total / 5.0
    stdDev = stDeviation(accuracy)
    print "CarTest"
    print "max: {0}".format(max)
    print "average: {0}".format(average)
    print "stdDev: {0}".format(stdDev)

def q6():
    file = open("statistics.txt", "w")
    for i in range(0, 41, 5):
        accuracy = []  # testPenData
        for j in range(5):
            accuracy.append(testPenData([i])[1])
        max = 0
        average = 0
        stdDev = 0
        total = 0
        for a in accuracy:
            if (a > max):
                max = a
            total += a
        average = total / 5.0
        stdDev = stDeviation(accuracy)

        file.write("PenTest\n")
        file.write("{0}\n".format(max))
        file.write("{0}\n".format(average))
        file.write("{0}\n".format(stdDev))
        file.write("{0}\n\n".format(i))

        accuracy = []  # testCarData
        max = 0
        average = 0
        stdDev = 0
        for j in range(5):
            accuracy.append(testCarData([i])[1])
        max = 0
        average = 0
        stdDev = 0
        total = 0
        for a in accuracy:
            if (a > max):
                max = a
            total += a
        average = total / 5.0
        stdDev = stDeviation(accuracy)
        file.write("CarTest\n")
        file.write("{0}\n".format(max))
        file.write("{0}\n".format(average))
        file.write("{0}\n".format(stdDev))
        file.write("{0}\n\n".format(i))
    file.close()

xorData = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]
def testXorData(hiddenLayers = []):
    return buildNeuralNet((xorData, xorData),maxItr = 10000,hiddenLayerList =  hiddenLayers)
def q7():
    file = open("statisticsq7.txt", "w")
    file.write("Format: Max\nAverage\nStandard Deviation\nPerceptrons\n\n\n")
    accuracy = []
    file.write("No Hidden Layer Accuracy: {0}\n\n".format(testXorData([])[1]))
    for i in range(1, 40, 1):
        accuracy = []  # testXorData
        for j in range(5):
            accuracy.append(testXorData([i])[1])
        max = 0
        average = 0
        stdDev = 0
        total = 0
        for a in accuracy:
            if (a > max):
                max = a
            total += a
        average = total / 5.0
        stdDev = stDeviation(accuracy)

        file.write("XorTest\n")
        file.write("{0}\n".format(max))
        file.write("{0}\n".format(average))
        file.write("{0}\n".format(stdDev))
        file.write("{0}\n\n".format(i))
    file.close()

q7()