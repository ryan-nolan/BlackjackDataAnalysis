import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import os
from pathlib import Path
from collections import Counter
import statistics
import sys
import operator

def autopct(values):
    def my_autopct(pct):
        sumOf = sum(values)
        ret = int(round(pct * sumOf / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=ret)
    return my_autopct

#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Source/Data") #insert folder path here
os.chdir(path)
files = os.listdir()
print(sys.argv)

if len(sys.argv) == 1: 
    for file in files:
        if os.path.isfile(file):
            with open(file) as csvfile:
                csv_reader = csv.reader(csvfile)
                print(file)
                overMinBetPercentage = {}
                i = 0
                for row in csv_reader:
                    turnNumber = row[0]
                    stake = row[8]
                    if i == 2:
                        minBet = stake
                    
                    overMinBetPercentage[turnNumber] = stake
                    i+= 1
                overMinBetCounter = Counter()
                for result in overMinBetPercentage.values():
                    overMinBetCounter[result] += 1
                del overMinBetCounter['PlayerStake']
                
                #Plot figure
                figureObject, axesObject = plt.subplots()
                axesObject.pie(overMinBetCounter.values(), labels=overMinBetCounter.keys(), autopct=autopct(overMinBetCounter.values()),startangle=90)

                plt.title(file+ "\nAmount Bet Percentage")
                plt.savefig(os.getcwd()+'\\Graphs\\ExactBetAmountPie\\'+file+'.png')
                