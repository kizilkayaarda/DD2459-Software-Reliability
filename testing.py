from random import randint
from algos import isMember

def generateRandomTests(arrSize, suiteSize, lower, upper):
    """Generates random arrays and keys for random testing and writes them to seperate files"""
    # generate random arrays and keys
    # writing them to file
    arraysFile = open(f"random{suiteSize}.txt", "w+")

    for i in range(suiteSize):
        arr = [str(randint(lower, upper)) for k in range(arrSize + 1)]
        arraysFile.write(" ".join(arr) + "\n")

    arraysFile.close()

def runRandomTests(suiteSize):
    """Runs the prepared random tests by reading inputs from files"""
    # read the array items
    arraysFile = open(f"random{suiteSize}.txt", "r")
    lines = arraysFile.readlines()
    arraysFile.close()

    inputs = [[int(item) for item in array.split(" ")] for array in lines]

    # testing the algorithm
    testCount = 0

    for i in range(suiteSize):
        testCount += 1
        arr = inputs[:-1]
        key = inputs[-1]

        if not isMember(arr, key) is (key in arr):
            break

    return testCount

def generatePairwiseTests(noOfInputs, lower, upper):
    """Generate default values and typical values fır pairwise testing"""
    # generate default values for each array item and the key
    defaults = [str(randint(lower, upper)) for i in range(noOfInputs)]
    typicals = []

    # generating typical values so they are different from defaults
    while len(typicals) < len(defaults):
        item = str(randint(lower, upper))
        curIndex = len(typicals)

        if item != defaults[curIndex]:
            typicals.append(item)

    testCases = []

    # generate 2-wise test cases
    for i in range(noOfInputs):
        for j in range(i + 1, noOfInputs):
            testCase = defaults[0:i] + typicals[i:i + 1] + defaults[i + 1:j] + typicals[j:j+1] + defaults[j+1:]
            testCases.append(testCase)

    # generate 1-wise test cases
    for k in range(noOfInputs):
        testCase = defaults[0:k] + typicals[k:k + 1] + defaults[k + 1:]
        testCases.append(testCase)

    # append 0-wise test case
    testCases.append(defaults)

    pairwiseFile = open(f"pairwise{noOfInputs}.txt", "w+")

    # write the test cases to files
    for tc in testCases:
        pairwiseFile.write(" ".join(tc) + "\n")

    pairwiseFile.close()

def runPairwiseTests(noOfInputs):
    """Reads the pairwise test cases and executes the function with them"""

    # reading the input values from the file and converting them to appropriate format
    inputs = open(f"pairwise{noOfInputs}.txt", "r")
    testCases = inputs.readlines()
    testCases = [[int(item) for item in tc.split(" ")] for tc in testCases]
    inputs.close()

    testCount = 0

    for tc in testCases:
        testCount += 1
        arr = tc[:-1]
        key = tc[-1]

        if not isMember(arr, key) is (key in arr):
            break

    return testCount