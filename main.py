import testing as test

upper = 100
lower = -100
arraySizes = [10, 100]
randomSuiteSize = 100

for size in arraySizes:
    test.generateRandomTests(size, randomSuiteSize, lower, upper)
    test.generatePairwiseTests(size + 1, lower, upper)

for size in arraySizes:
    print(f"Random {size} detected at: {test.runRandomTests(size)}")
    print(f"Pariwise {size + 1} detected at: {test.runPairwiseTests(size + 1)}")
    




