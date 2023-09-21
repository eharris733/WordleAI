import math

import matplotlib.pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def logstar(n):
    iterations = 0
    var = n
    while var > 1:
        var = math.log2(var)
        iterations+= 1

    return iterations


def logk(n, k):
    if(k == 1):
        return n
    return logk(math.log2(n), k - 1)

ns = []
logstars = []
logks = []
def generateGraph(maxN):
    for i in range(2, maxN):
        ns.append(i)
        logstars.append(logstar(i))
        logks.append(logk(i, 3))

    print(len(ns))
    print(len(logstars))
    print(len(logks))
    plt.plot(ns, logks)
    plt.show()



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generateGraph(1000)
