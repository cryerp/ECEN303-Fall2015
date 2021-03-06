__author__ = "Zachary Smadi"
__NetID__ = "smadi94"
__GitHubID__ = "smadi94"
__challenge__ = "1"
__version__ = "3.1"
__grader__ = "Logan Barnard"
__SelfGrade__ = "4"
__PeerGrade__ = "5" #everything seems to be working great and is order with the answers submitted by email

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):

    if random.random() < p:
        return 1  #if the coin is heads
    else:
        return 0  #if the coin is tails

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):

    addFlips= 0  #no flips yet, temporary sum
    for InnerIndex in range(0, NumberFlips): #NumberFlips is set to 8, so 0 to 8 flips
        addFlips += biasedcoinflip(ParameterP)
    SumTrials.append(addFlips)  #each SumTrials add addFlips


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)

sumDistribution = 0
for item in Distribution:
    sumDistribution += item
print(repr(sumDistribution))

OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.
As ParameterP increases from zero to one the graph shifts from left to right. This is because the more the coin is flipped
the higher the probablility of it being a one.


What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
If ParameterP = 0.7 and NumberFlips = 8, then the most likely outcome is 6. It has about a 30% probability.


"""
