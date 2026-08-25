---
doc_id: symmetry-04-00039-v3
doc_title: "Knots on a Torus: A Model of the Elementary Particles"
section_id: sec-034-0-bb-0-a-b-c
section_title: "BB* 0 (A, B, C)"
section_number: 0
pages: 73-76
source_pdf: symmetry-04-00039-v3.pdf
source_sha256: 1aa8a81916887f8e
doc_brief: "Knots on a Torus: A Model of the Elementary Particles — Two knots; just two rudimentary knots, th e unknot and the trefoil."
---
0        0    CC*
  and 
0       AB*    AC*
BA*   0      BC* (A, B, C)
CA*  CB*    0
  
Symmetry 2012, 4  112 
 
which evaluates as the direct sum of  six matrices, listed below. Toge ther these contain a total of 27 
three letter terms, each of which coincides uniquely with one of the 27 three letter terms that remain in 
Figures 28 and 29 of Section 4 after all terms containing letters D or D* are deleted.  
    0          0          0    0         0         0 AA*A  AA*B  AA*C 
    0          0          0 , BB*A  BB*B  BB*C ,    0          0          0
CC*A  CC*B   CC*C    0           0         0    0          0           0
, 
AC*A   AC*B  AC*C AB*A  AB*B  AB*C   0           0         0
BC*A  BC*B   BC*C ,    0           0        0 , BA*A  BA*B  BA*C
0               0           0 CB*A  CB*B CB*C BA*A  BA*B  BA*C
. 
Collecting terms then reduces the direct sum of these six terms to the outer product of two vectors 
A*
B * (A, B, C)
C*




 
 
where *  is the direct sum of three terms, 
*( A *B *C * )    (E-17)
Although this expression still encompasses all of the 27 terms, it is a little more succinct.  
Appendix F. On the Kauffman Bracket Polynomial of (2, n) Torus Knots 
Both the Kauffman bracket polynomial [8] and (2, n) torus knots have been studied at considerable 
length. The main interest here is a symmetric closed form reformulation of the KBP in the case of 
composite (2, n) torus knots, that is, knots where n is the sum of individual terms each of which is 
equal to the NHT of a constituent of a composite FMS. Also of interest as we shall see is the 
convolutional nature of this pa rticular reformulation and its relationship to sampled data  
feedback systems.  
We begin with the recursion formula of the Kauffman bracket polynomial [8] for the (2, n)  
torus knot, 

1 23
1A1 A
n n
nnKK
 
   (F-1)
The associated closed form version is readily shown to be in the form of a convolution  
2
0
 1
AA
n
nm n m
n
m
KK x y 

   (F-2)
where 3
1A (which is equal to ) and AxK y 
   and  
22
0 AAK   . 
Note that with this notation Equation F-1 becomes 
2
1AA n
nnKK x   (F-3)
The form of these equations suggests an isomor phic relationship to the field of sampled data 
feedback systems as summarized in the followi ng diagrammatic portrayal. The open switch in the 
Symmetry 2012, 4  113 
 
figure signifies that the 0K  input exists for only an initial sample). Due to the circulation around the 
closed loop, the syst em response at time n to an impulsive input occu rring at the previous time, m, is 
 (or A )nm nmy  . Furthermore, by time n, there are n such responses to be added up, thus implying the 
summation in Equation (F-2). Also, since there is only a single initial impulse, 0K , switched on at  
m = 0, the associated response (t he result of summation) at time n is just 0An K . Note that the output 
shown in the figure is just Equation (F-3). 
Figure F1. Operational model of Eqation F-2. 
 
The simplest example of what  is meant herein by a (2, n) torus knot with composite n is just the 
case of 12  nn n . We find that 
12
12 2 1 1 2 2
0
11
AA A
nn
nn n n m n n m mm
n
mm
KK y x y x x y 

    
   (F-4)
Interchanging subscripts 1 and 2 in this equation and collecting the four terms that result into two 
convolution groups gives the more symmetrical formulation 
21
12 1 1 2 2 2 1 2
0
11
AA A (  ) ( ) / 2
nn
nn n n n m n n n m mm
n
mm
K K x y xy x y xy 

    

  (F-5)
or, more concisely, 
12 2
01 2 2 1AA A ( ) / 2nn
nKK C C    (F-6)
where 
 1
, ,  1 , 2
i
ii i
n
nn n m m
ii
m
xy C x y i 

    . 
The case for three components, 123nn n n , proceeds in essentially the same way and in 
analogy with Equation (F-5) we find  
3
2
02 3 1 3 1 2 1 2 3
1
AA ( )in
nKK y y C y x C x x C    (F-7)
where the coefficients are , , ,   1 , 2 , a n d  3in
i xyi , and the convolutions, iC , are as before 
but with i = 1, 2, and 3. 
Symmetry 2012, 4  114 
 
Cyclic permutation of the subscripts gives two more equations and collecting terms associated with 
each of the three convolutions produces the final, symmetrical form, 
3
2
01 1 2 2 3 3
1
AA ( ) / 3in
nKK C C C     (F-8)
where 12 3 2 3 2 3y yy xx x  , 23 1 3 1 3 1y yy xx x  , 31 2 1 2 1 2y yy xx x   . 
We can readily generalize to th e case of an arbitrary number, Fn , of components. In analogy with 
Equation (F-8) we find that  
2
01 1
1
A A ( ....... ) /
F
i
FF
n
n
nn n FKK C C n     (F-9)
For any particular value of Fn , the coefficients (the 's ) are computable in the manner illustrated 
for the case of Fn  = 3. However, we can anticipate the results on the basis of the following selection rules: 
1. All subscripts, including that of the C's, must be present in each coefficient. 
2. The number of y terms decreases linearly from 1Fn   in the first coefficient to 0 for the last, 
while the number of x terms increases, correspondingly, from 0 in the first coefficient to 1Fn   
in the last. 
3. The highest y subscript value is Fn  and the highest x subscript value is 1Fn  . 
For example, we can write down, ab initio, the equation analogous to Equation (F-8), for the case of 
Fn = 4 as 
4
2
0 4321 43 1 2 4 1 2 3 1 23 4
1
AA (  ) / 4in
nKK y y y C y y x C y x x C x x x C     (F-10)
