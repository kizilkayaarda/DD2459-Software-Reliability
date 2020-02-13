import testing as test

randomSuiteSize = 100
randomArraySize = 15
upperLimit = 100
lowerLimit = -100

pairwiseDimension = 16 # no. of inputs

test.generateRandomTests(randomArraySize, randomSuiteSize, lowerLimit, upperLimit)
print(test.runRandomTests(randomSuiteSize))

test.generatePairwiseTests(pairwiseDimension, lowerLimit, upperLimit)
print(test.runPairwiseTests(pairwiseDimension))