---
doc_id: symmetry-04-00039-v3
doc_title: "Knots on a Torus: A Model of the Elementary Particles"
section_id: sec-042-f-on-the-kauffman-bracket-polynomial-of-2-n-toru
section_title: "On the Kauffman Bracket Polynomial of (2, n) Torus Knots"
section_number: F
pages: 74-76
source_pdf: symmetry-04-00039-v3.pdf
source_sha256: 1aa8a81916887f8e
toc_source: inferred
---
Both the Kauffman bracket polynomial [8] and (2, n) torus knots have been studied at considerable 
length. The main interest here is a symmetric closed form reformulation of the KBP in the case of 
composite (2, n) torus knots, that is, knots where n is the sum of individual terms each of which is 
equal to the NHT of a constituent of a composite FMS. Also of interest as we shall see is the 
convolutional nature of this particular reformulation and its relationship to sampled data  
feedback systems.  
We begin with the recursion formula of the Kauffman bracket polynomial [8] for the (2, n)  
torus knot, 


1
2 3
1
A
1
A
n
n
n
n
K
K





 
(F-1)
The associated closed form version is readily shown to be in the form of a convolution  
2
0
 1
A
A
n
n
m
n m
n
m
K
K
x y 




 
(F-2)
where 
3
1
A (which is equal to 
) and 
A
x
K
y




 and 


2
2
0
A
A
K



. 
Note that with this notation Equation F-1 becomes 
2
1
A
A
n
n
n
K
K
x



 
(F-3)
The form of these equations suggests an isomorphic relationship to the field of sampled data 
feedback systems as summarized in the following diagrammatic portrayal. The open switch in the 
Symmetry 2012, 4 
 
113 
 
figure signifies that the 
0
K input exists for only an initial sample). Due to the circulation around the 
closed loop, the system response at time n to an impulsive input occurring at the previous time, m, is 
 (or A
)
n m
n m
y 

. Furthermore, by time n, there are n such responses to be added up, thus implying the 
summation in Equation (F-2). Also, since there is only a single initial impulse, 
0
K , switched on at  
m = 0, the associated response (the result of summation) at time n is just 
0
AnK . Note that the output 
shown in the figure is just Equation (F-3). 
Figure F1. Operational model of Eqation F-2. 
 
The simplest example of what is meant herein by a (2, n) torus knot with composite n is just the 
case of 
1
2
 
 
n
n
n


. We find that 
1
2
1
2
2
1
1
2
2
0
1
1
A A
A
n
n
n
n
n
n
m
n
n
m
m
m
n
m
m
K
K
y
x y
x
x y















 
(F-4)
Interchanging subscripts 1 and 2 in this equation and collecting the four terms that result into two 
convolution groups gives the more symmetrical formulation 
2
1
1
2
1
1
2
2
2
1
2
0
1
1
A A
A
(
 
)
(
)
/ 2
n
n
n
n
n
n
n
m
n
n
n
m
m
m
n
m
m
K
K
x
y
x y
x
y
x y

















 
(F-5)
or, more concisely, 
1
2
2
0
1
2
2
1
A A
A (
) / 2
n
n
n
K
K
C
C





 
(F-6)
where 
 1
, 
,  
1, 2
i
i
i
i
n
n
n
n
m
m
i
i
m
x
y
C
x y
i








. 
The case for three components, 
1
2
3
n
n
n
n



, proceeds in essentially the same way and in 
analogy with Equation (F-5) we find  
3
2
0
2
3
1
3 1
2
1
2
3
1
A
A (
)
in
n
K
K
y y C
y x C
x x C





 
(F-7)
where the coefficients are 
, 
, ,  
 1, 2, and 3
in
i
x y i






, and the convolutions, 
iC , are as before 
but with i = 1, 2, and 3. 
Symmetry 2012, 4 
 
114 
 
Cyclic permutation of the subscripts gives two more equations and collecting terms associated with 
each of the three convolutions produces the final, symmetrical form, 
3
2
0
1
1
2
2
3
3
1
A
A (
) / 3
in
n
K
K
C
C
C








 
(F-8)
where 
1
2
3
2
3
2
3
y y
y x
x x



, 
2
3
1
3 1
3 1
y y
y x
x x



, 
3
1
2
1
2
1
2
y y
y x
x x



. 
We can readily generalize to the case of an arbitrary number, 
F
n , of components. In analogy with 
Equation (F-8) we find that  
2
0
1
1
1
A
A (
.......
) /
F
i
F
F
n
n
n
n
n
F
K
K
C
C
n







 
(F-9)
For any particular value of 
F
n , the coefficients (the
's

) are computable in the manner illustrated 
for the case of 
F
n = 3. However, we can anticipate the results on the basis of the following selection rules: 
1. All subscripts, including that of the C's, must be present in each coefficient. 
2. The number of y terms decreases linearly from 
1
F
n  in the first coefficient to 0 for the last, 
while the number of x terms increases, correspondingly, from 0 in the first coefficient to 
1
F
n  
in the last. 
3. The highest y subscript value is 
F
n and the highest x subscript value is
1
F
n . 
For example, we can write down, ab initio, the equation analogous to Equation (F-8), for the case of 
F
n = 4 as 
4
2
0
4
3
2
1
4
3 1
2
4
1
2
3
1
2
3
4
1
A
A (
 
) / 4
in
n
K
K
y y y C
y y x C
y x x C
x x x C






 
(F-10)
