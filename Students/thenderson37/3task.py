__author__ = "Tyler Henderson"
__NetID__ = "tyler.henderson07"
__GitHubID__ = "thenderson37"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    #TrialSequence.append(random.randrange(Cardinality)) this line was no longer needed
    
    if random.random() <= .75: #probability of one side of the coin is now .75
        TrialSequence.append(1)
    
    else:
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution) # added () 
