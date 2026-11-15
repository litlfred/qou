---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-017-26-example-41
section_title: "Example: 41"
section_number: 2.6
pages: 14-15
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
the ﬁgure-eight knot complement M.
It has a well known regular ideal triangulation T
consisting of N = 2 tetrahedra, to which we assign logarithmic shape parameters (Z, Z′, Z′′)
and (W, W ′, W ′′).
z
z′
z′′ w
w′
w′′
E1
E2
µ
z
z′
z′′
w
w′
w′′
z
z′
z′′ w
w′
w′′
z
z′
z′′
w
w′
w′′
Figure 5. The boundary of the cusp neighborhood for the ﬁgure-eight knot.
A map of the boundary of the cusp neighborhood is shown in Figure 5. We have chosen
one of 32 possible cyclic labelings by Z’s and W’s (i.e. one of 32 possible quad types). Each
of the edges intersects the cusp twice, so it is easy to read oﬀfrom Figure 5 that the edge
constraints (2.3) are
E1 :
2Z + Z′′ + 2W + W ′′ = 2πi
E2 :
2Z′ + Z′′ + 2W ′ + W ′′ = 2πi .
The sum of the left-hand sides is automatically 4πi, so we can choose to ignore the second
constraint. If we choose the meridian path µ as in Figure 5, the meridian constraint (2.5) is
µ :
−Z′ + W = 0
Putting together the ﬁrst edge constraint and the meridian into matrices, we have

2
2
0
1
 
Z
W

+

0
0
−1
0
 
Z′
W ′

+

1
1
0
0
 
Z′′
W ′′

= iπ

2
0

.
Using Z + Z′ + Z′′ = W + W ′ + W ′′ = iπ to eliminate Z′ and W ′, we get

2
2
1
1
 
Z
W

+

1
1
1
0
 
Z′′
W ′′

= iπ

2
1

.
THE QUANTUM CONTENT OF THE GLUING EQUATIONS
15
From this last expression, we can read oﬀ
(2.13)
A =

2
2
1
1

,
B =

1
1
1
0

,
ν =

2
1

.
The two gluing equations (2.12) are then
(2.14)
z2w2z′′w′′ = 1 ,
zwz′′ = −1 ,
with z′′ = 1 −z−1 and w′′ = 1 −w−1. The solution for the complete hyperbolic structure is
z = w = eiπ/3.
Finally, a ﬂattening (fz, f ′
z, f ′′
z ; fw, f ′
w, f ′′
w) ∈Z6, i.e. an integer solution to Af + Bf ′′ = ν
and f + f ′ + f ′′ = 1, is given by
(2.15)
(fz, f ′
z, f ′′
z ; fw, f ′
w, f ′′
w) = (0, 1, 0; 1, 0, 0)
It is easy to see that every ﬂattening has the form (a, b, 1 −a −b; b, a, 1 −a −b) for integers
a, b.
