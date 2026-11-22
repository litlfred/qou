---
doc_id: symmetry-04-00039-v3
doc_title: "Knots on a Torus: A Model of the Elementary Particles"
section_id: sec-042-appendix-f-on-the-kauffman-bracket-polynomial-of
section_title: "On the Kauffman Bracket Polynomial of (2, n) Torus Knots"
section_number: Appendix F
pages: 74-76
source_pdf: symmetry-04-00039-v3.pdf
source_sha256: 1aa8a81916887f8e
toc_source: inferred
doc_brief: "Knots on a Torus: A Model of the Elementary Particles — Two knots; just two rudimentary knots, the unknot and the trefoil."
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
Symmetry 2012, 4 113

figure signifies that the K, input exists for only an initial sample). Due to the circulation around the

closed loop, the system response at time 7 to an impulsive input occurring at the previous time, m, is
y"™ (or A""). Furthermore, by time n, there are n such responses to be added up, thus implying the

summation in Equation (F-2). Also, since there is only a single initial impulse, K,, switched on at
m = 0, the associated response (the result of summation) at time n is just A"K,. Note that the output

shown in the figure is just Equation (F-3).

Figure F1. Operational model of Eqation F-2.

Ky /

K, =AK,, -A’x"

oe

3

Ax? —> eo —— A c

Vv

Delay

The simplest example of what is meant herein by a (2, n) torus knot with composite n is just the
case of n = n,+n,. We find that

K, =A"APK,—A? pier roy | 4
m=l m=l

Interchanging subscripts | and 2 in this equation and collecting the four terms that result into two
convolution groups gives the more symmetrical formulation

onan afore nEer tar angers|a s)
m=l1 m=l
or, more concisely,
K, =A"A"K, -A’(o,C, +.0,C,)/2 (F-6)

Nj
where o, =x" +y", C= yey, i =1, 2.

m=

The case for three components, n=n,+n,+n,, proceeds in essentially the same way and in

analogy with Equation (F-5) we find
2 2
K, =|]A"«, —A?(V,V,C, + ¥3x,C, + x,X,C;) (F-7)
1

where the coefficients are a, =a", a=x, y, i = 1, 2, and 3, and the convolutions, C,, are as before

but with i = 1, 2, and 3.
Symmetry 2012, 4 114

Cyclic permutation of the subscripts gives two more equations and collecting terms associated with

each of the three convolutions produces the final, symmetrical form,

3
K, =[[A"«, -A(BC, + B,C, + B,C,)/3 (F-8)
1

where J, = ¥yV3+ V2X3+XpX3, By = V3 Vi + Vy% +31%,, By = VV_ + YX FHA.
We can readily generalize to the case of an arbitrary number, n,, of components. In analogy with

Equation (F-8) we find that

Np

K, =] [A Ky HAG, Hee t Xp Cy,)/ Mp (F-9)
1

For any particular value of n,., the coefficients (the y's) are computable in the manner illustrated

for the case of n,, = 3. However, we can anticipate the results on the basis of the following selection rules:

1. All subscripts, including that of the C's, must be present in each coefficient.
2. The number of y terms decreases linearly from n, —1 in the first coefficient to 0 for the last,

while the number of x terms increases, correspondingly, from 0 in the first coefficient to n, —1

in the last.
3. The highest y subscript value is n,, and the highest x subscript value isn, —1.

For example, we can write down, ab initio, the equation analogous to Equation (F-8), for the case of
n,=4 as

4
K, = [][4"% APY VG, + VV Cy + VM VC, +.XVAGC,)/ 4 (F-10)
1
