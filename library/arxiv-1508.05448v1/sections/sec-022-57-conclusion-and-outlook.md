---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-022-57-conclusion-and-outlook
section_title: "Conclusion and Outlook"
section_number: 5.7
pages: 122-127
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
doc_brief: "Concentration of Measure Techniques and Applications — 25 sections: Front matter; Biographical Sketch; Acknowledgments"
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
114
A
Python code: Simulating a
Mallows Random Permutation
’ ’ ’ ’
permutation . py
@author : Meg Walters
’ ’ ’
import numpy as np
import random
import math
import b i s e c t
import matplotlib . pyplot at
plt
def
p a ti e n c e s o rt ( l i s t ) :
#This
function
creates a multidimensional
array
#containing
a l l
of
the
stacks
#of
the
patience
sorting
algorithm
#Input :
#
l i s t :
l i s t
of numbers to
sort
#Output :
#
len ( stacks ) :
returns
the numbers of
stacks
115
#
stacks = [ ]
l e n s t a c k s =[] #v a r i a b l e
to
keep
track
of number of
stacks
for x in
l i s t : #i t e r a t e
through
l i s t
of numbers
temp stack = [ x ] #put number in a temporary
stack
i = b i s e c t . b i s e c t l e f t ( stacks ,
temp stack )
#determines where number should be
inserted
i f
# i t
was to be
inserted
in
order
i f
i != len ( stacks ) :
#i f
number i s
not
larger
then
a l l
numbers on top
#of
stacks
stacks [ i ] . i n s e r t (0 , x) #put number on appropriate
stack
l e n s t a c k s . append ( len ( stacks )) #update
length
v a r i a b l e
else :
stacks . append ( temp stack ) #create new stack
l e n s t a c k s . append ( len ( stacks )) #update
length
v a r i a b l e
def
f i s h e r y a t e s ( length ) :
#uses
f i s h e r
yates
algorithm
to
create random permutation
#Input :
#
length :
desired
length
of
permutation
#Output :
#
L: random permutation
L=[1] #begin
with
only 1 in
the
l i s t
for
i
in xrange ( length −1):
#i t e r a t e
to
create a
l i s t
of
length
’ length ’
116
m=i+2 #i n i t i a l i z e /update m
k=random . randint (1 ,m)
#generate a random integer
between 1 and m.
i f k==m:
L. append (m) #append m to
the end of
the
l i s t
else :
L. i n s e r t (k−1,m) #i n s e r t m in k−1 place
in
l i s t
return L #return random permutation
def mallows ( length , q ) :
#uses
the
mallows measure to
create a permutatioin
#Input :
#
length :
desired
length
of
permutation
#
q : 1−p r o b a b i l i t y
#Output :
#
L:
permutation
L=[1] #begin
with
only 1 in
the
l i s t
for
i
in xrange ( length −1):
#i t e r a t e
to
create
l i s t
of
length
’ length ’
m=i+2 #i n i t i a l i z e /update m
x=np . random . geometric (p=1−q , s i z e =1)
#generate a geometric random integer ,
p r o b a b i l i t y p
y=1+((x−1)%m) #find y based on mallows
i f y==1:
L. append (m) #append m to end of
the
l i s t
117
else :
L. i n s e r t (m+1−y ,m)
#i n s e r t m at
the m+1−y position
in
the
l i s t
return L
l e n g t h l i s t =10000
#change
t h i s
v a r i a b l e
to change n
length data =200 #change
t h i s
value
to change
#number of
times program should
#run to
c o l l e c t
data
data =[] #i n i t i a l i z e
array
to
hold
data
q=.8 #change
t h i s
value
to change the Mallows q
#create
data
for
i
in xrange ( length data ) :
data . append ( p a ti e n c e s o r t ( mallows ( l e n g t h l i s t , q ) ) )
#create
histogram
for
given
data
f i g=plt . f i g u r e ()
ax=f i g . add subplot (111)
n ,
bins ,
patches = ax . h i s t ( data ,30 , normed=False , . . .
. . . f a c e c o l o r=’ green ’ ,
histtype=’ bar ’ , align=’mid ’ )
ax . grid ( True )
plt . t i t l e ( ’ LLIS of a Mallows Permutation ’ )
plt . xlabel ( ’ Length of
the Longest
Increasing
Subsequence ’ )
plt . ylabel ( ’Number of
occurences ’ )
plt . show ()
