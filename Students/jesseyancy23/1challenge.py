__author__ = "Jesse Yancy"
__NetID__ = "jpy234"
__GitHubID__ = "jesseyancy23"
__challenge__ = "1"
__version__ = "0.0"
__grader__ = "Tyler Henderson"
__SelfGrade__ = "4"
__PeerGrade__ = "3"

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
            return 1
        else:
            return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):

    sum_of_flips = 0
    for Index in range (0, NumberFlips):
        sum_of_flips += biasedcoinflip(ParameterP)
    SumTrials.append(sum_of_flips)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
dist_sum = 0
for element in Distribution:
    dist_sum += element
print(repr(dist_sum))

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
With p being one you will only get ones, as P goes down to zero you will get less and less 1s while getting
more and more 0s

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?


"""
