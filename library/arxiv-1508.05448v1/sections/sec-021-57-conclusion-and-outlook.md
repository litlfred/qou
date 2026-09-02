---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-021-57-conclusion-and-outlook
section_title: "Conclusion and Outlook"
section_number: 5.7
pages: 122-127
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
---
As previously mentioned, the results in this section are preliminary steps toward
bounding the ﬂuctuations of the length of the longest increasing subsequence of a
Mallows permutation. The next step is to use the approach of the four square problem
to solve a nine square problem. Once the asymptotics are computed for that problem,
we can generalize to a large number of small squares and obtain a local central limit
theorem for the counts on small subsquares. After that, we hope to couple our model
to the model of Deuschel and Zeitouni [Deuschel and Zeitouni, 1999] and then use
Talagrand’s isoperimetric inequality to bound the ﬂuctuations. These results will
appear in a future work.
114
A Python code: Simulating a
Mallows Random Permutation
’ ’ ’ ’
permutation . py
@author : Meg Walters
’ ’ ’
import numpy as np
import random
import math
import b i s e c t
import matplotlib . pyplot at p l t
def p a t i e n c es o r t ( l i s t ) :
#This f u n c t i o n c r e a t e s a m u l t i d i m e n s i o n a l array
#c o n t a i n i n g a l l o f t h e s t a c k s
#o f t h e p a t i e n c e s o r t i n g a l g o r i t h m
#Input :
# l i s t : l i s t o f numbers to s o r t
#Output :
# l e n ( s t a c k s ) : r e t u r n s t h e numbers o f s t a c k s
115
#
s t a c k s = [ ]
l e n s t a c k s =[] #v a r i a b l e to keep t r a c k o f number o f s t a c k s
f o r x in l i s t : #i t e r a t e through l i s t o f numbers
temp stack = [ x ] #put number in a temporary s t a c k
i = b i s e c t . b i s e c t l e f t ( stacks , temp stack )
#determines where number s h o u l d be i n s e r t e d i f
# i t was to be i n s e r t e d in order
i f i != len ( s t a c k s ) :
#i f number i s not l a r g e r then a l l numbers on top
#o f s t a c k s
s t a c k s [ i ] . i n s e r t (0 , x )#put number on a p p r o p r i a t e s t a c k
l e n s t a c k s . append ( len ( s t a c k s ) )#update l e n g t h v a r i a b l e
e l s e:
s t a c k s . append ( temp stack ) #c r e a t e new s t a c k
l e n s t a c k s . append ( len ( s t a c k s ) )#update l e n g t h v a r i a b l e
def f i s h e r y a t e s ( length ) :
#uses f i s h e r y a t e s a l g o r i t h m to c r e a t e random permutation
#Input :
# l e n g t h : d e s i r e d l e n g t h o f permutation
#Output :
# L : random permutation
L=[1] #b e g i n with only 1 in t h e l i s t
f o r i in xrange ( length −1):
#i t e r a t e to c r e a t e a l i s t o f l e n g t h ’ l e n g t h ’
116
m =i +2#i n i t i a l i z e / update m
k=random . randint (1 ,m)
#g e n e r a t e a random i n t e g e r between 1 and m.
i f k== m:
L . append (m) #append m to t h e end o f t h e l i s t
e l s e:
L . i n s e r t (k−1,m) #i n s e r t m in k −1 p l a c e in l i s t
return L #r e t u r n random permutation
def mallows ( length , q ) :
#uses t h e mallows measure to c r e a t e a p e r m u t a t i o i n
#Input :
# l e n g t h : d e s i r e d l e n g t h o f permutation
# q : 1 − p r o b a b i l i t y
#Output :
# L : permutation
L=[1] #b e g i n with only 1 in t h e l i s t
f o r i in xrange ( length −1):
#i t e r a t e to c r e a t e l i s t o f l e n g t h ’ l e n g t h ’
m =i +2#i n i t i a l i z e / update m
x=np . random . geometric (p=1 −q , s i z e =1)
#g e n e r a t e a geometric random i n t e g e r , p r o b a b i l i t y p
y=1+((x−1)% m)#f i n d y based on mallows
i f y==1:
L . append (m) #append m to end o f t h e l i s t
117
e l s e:
L . i n s e r t (m +1−y ,m)
#i n s e r t m at t h e m +1 −y p o s i t i o n in t h e l i s t
return L
l e n g t h l i s t =10000 #change t h i s v a r i a b l e to change n
length data =200 #change t h i s v a l u e to change
#number o f times program s h o u l d
#run to c o l l e c t data
data =[] #i n i t i a l i z e array to h o l d data
q=.8 #change t h i s v a l u e to change t h e Mallows q
#c r e a t e data
f o r i in xrange ( length data ) :
data . append ( p a t i e n c e s o r t ( mallows ( l e n g t hl i s t , q ) ) )
#c r e a t e histogram f o r g i v e n data
f i g=p l t . f i g u r e ( )
ax=f i g . add subplot (111)
n , bins , patches = ax . h i s t ( data , 3 0 , normed=False , . . .
. . . f a c e c o l o r=’ green ’ , h i s t t y p e=’ bar ’ , a l i g n=’ mid ’ )
ax . g r i d ( True )
p l t . t i t l e ( ’ LLIS of a Mallows Permutation ’ )
p l t . x l a b e l ( ’ Length of the Longest I n c r e a s i n gSubsequence ’ )
p l t . y l a b e l ( ’Numberof occurences ’ )
p l t . show ( )
118
