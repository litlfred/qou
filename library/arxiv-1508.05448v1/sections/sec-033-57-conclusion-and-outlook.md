---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-033-57-conclusion-and-outlook
section_title: "Conclusion and Outlook"
section_number: 5.7
pages: 122-127
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Conclusion and Outlook
As previously mentioned, the results in this section are preliminary steps toward
bounding the ﬂuctuations of the length of the longest increasing subsequence of a
Mallows permutation. The next step is to use the approach of the four square problem
to solve a nine square problem. Once the asymptotics are computed for that problem,
we can generalize to a large number of small squares and obtain a local central limit
theorem for the counts on small subsquares. After that, we hope to couple our model
to the model of Deuschel and Zeitouni [Deuschel and Zeitouni, 1999] and then use
Talagrand’s isoperimetric inequality to bound the ﬂuctuations.
These results will
appear in a future work.
A Python code: Simulating a

Mallows Random Permutation

p999

permutation. py

@author: Meg Walters
import numpy as np
import random
import math

import bisect

import matplotlib.pyplot at plt

def patience_sort(list ):

#This function creates a multidimensional array
#containing all of the stacks

#of the patience sorting algorithm

#Input:

# list: list of numbers to sort

#Output:

# len(stacks): returns the numbers of stacks

stacks = []
len_stacks=[|] #variable to keep track of number of stacks
for x in list: #iterate through list of numbers
temp_stack = [x] #put number in a temporary stack
i = bisect.bisect_left (stacks , temp-stack)
#determines where number should be inserted if
# it was to be inserted in order
if i != len(stacks ):
#if number is not larger then all numbers on top
#of stacks
stacks[i].insert(0, x) #put number on appropriate stack
len_stacks.append(len(stacks)) #update length variable
else:
stacks.append(temp-_stack) #create new stack

len_stacks.append(len(stacks)) #update length variable

def fisher_yates (length ):

#uses fisher yates algorithm to create random permutation

#Input:

# length: desired length of permutation
#Output :

# L: random permutation

L=[1] #begin with only 1 in the list

for i in xrange(length —1):

#iterate to create a list of length ‘length’

m=i+2 #initialize/update m
k=random. randint (1 ,m)
#generate a random integer between 1 and m.
if k—n:
L.append(m) #append m to the end of the list
else:

L.insert(k—lm) #insert m in k-1 place in list

return L #return random permutation

def mallows (length ,q):

#uses the mallows measure to create a permutatioin
#Input:

# length: desired length of permutation

# q: I-probability

#Output :

# L: permutation

L=[1] #begin with only 1 in the list

for i in xrange(length —1):
#iterate to create list of length ‘length’
m=i+2 #initialize/update m
x=np.random. geometric (p=l—q, size =1)
#generate a geometric random integer, probability p
y=14+((x-l)%) find y based on mallows
if y==1:
L.append(m) #append m to end of the list

else:
L. insert (m+l-y ,m)
#insert m at the m+tl-y position in the list

return L

length_list=10000 #change this variable to change n
length_data=200 #change this value to change
#number of times program should

#run to collect data

data=|] #initialize array to hold data

q=.8 #change this value to change the Mallows q

#create data
for i in xrange(length_data):

data.append(patience_sort (mallows(length_list ,q)))

#create histogram for given data
fig=plt. figure ()
ax=fig .add_subplot (111)
n, bins, patches = ax. hist (data ,30,normed=False ,...
... facecolor=’green’, histtype=’bar’ ,align=’mid’)
ax. grid (True)
plt. title (’LLIS of a.Mallows. Permutation ’)
plt.xlabel(’ Length of the. Longest Increasing .Subsequence ’ )
plt.ylabel( ’Number_of_ occurences ’)

plt . show ()
