import random
import statistics
import os

firstline = ["Happy", "families", "are", "all", "alike;", "every", \
              "unhappy", "family", "is", "unhappy", "in", "its", "own", \
              "way.", "Leo Tolstoy", "Anna Karenina"] 

def problem4_1(wordlist):
    print(wordlist)
    wordlist.sort(key = str.lower)
    print(wordlist)
    

numList = []
random.seed(150)
for i in range(0,25):
    numList.append(round(100*random.random(),1))
    
def problem4_2(ran_list):
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))

def problem4_3(product, cost):
    out1 = "{0:<25}${1:>6.2f}"
    print(out1.format(product, cost))
