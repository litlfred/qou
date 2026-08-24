---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-003-22-neumannzagier-data
section_title: "Neumann–Zagier data"
section_number: 2.2
pages: 6-8
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further choices)"
---
following [11]. We start with a 3-manifold M with torus boundary component (all manifolds
and their triangulations will be oriented throughout the paper) equ ipped with a concrete
oriented ideal triangulation, that is with a triangulation such that ea ch tetrahedron ∆ of T
comes with a bijection of its vertices with those of the standard 3-s implex. (All triangulations
that are used in the computer programs SnapPy [8] and Regina [7] are concrete).
Every concrete tetrahedron ∆ has shape parameters ( z,z ′,z ′′) assigned to pairs of opposite
edges as in Figure 1, where the complex numbers z′ = 1/(1 −z) and z′′ = 1 − 1/z satisfy
the equations
z′′ +z−1 = 1, zz ′z′′ = −1. (13)
0
1
2
3 z
z
z′
z′
z′′
z′′
Figure 1. The shapes of an ideal tetrahedron.
If T is a triangulation as above, an Euler characteristic argument shows that the number
of tetrahedra equals to the number of edges. Fix an ordering of th e tetrahedra ∆ j for
j = 1,...,N and of the edges e1,...,e N of T , and assign a shape zj to the tetrahedron ∆ j
forj = 1,...,N . To describe the complete hyperbolic structure of M (when it exists) and its
deformations, Thurston [34] introduced the gluing equations for the variables z = (z1,...,z N )
around each edge ei, for i = 1,...,N . In logarithmic form, these equations have the form
N∑
j=1
Gi,j logzj +G′
i,j logz′
j +G′′
i,j logz′′
j = 2 πi, (i = 1,...,N ) (14)
where Gi,j (and likewise for G′
i,j and G′′
i,j) denote the number of times that an edge of ∆ j
labelled zj winds around the edge ei. Every peripheral curve γ in the boundary also gives
rise to a gluing equation of the same form as (
14), except the right hand side is 0 instead
of 2πi. Choosing a symplectic basis for H1(∂M, /CI ), we can enhance the equations ( 14) by
adding the peripheral equations
N∑
j=1
GN +c,j logzj +G′
N +c,j logz′
j +G′′
N +c,j logz′′
j = 0 , (c = 1, 2). (15)
It turns out that the (N +2)×N matricesG,G′ andG′′ have both symmetry and redundancy.
Any one of the edge equations is implies by the others, and we make a c hoice to remove one
of them, and replace it by one peripheral equation for a ﬁxed periph eral curve, resulting
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 7
into N ×N matrices G, G′ and G′′. Using the second Equation ( 13) in logarithmic form
logzj + logz′
j + logz′′
j = πi, we can eliminate one of the three shapes of each tetrahedron
(this is a choice of quad). For example, eliminating the shape z′
j forj = 1,...,N then results
into a system of equations
N∑
j=1
Ai,j logzj +Bi,j logz′′
j = πiν (i = 1,...,N ) (16)
where
A = G − G′, B = G′′ − G′ (17)
are the Neumann–Zagier matrices [ 29] and ν = (2,..., 2, 0)t − G′(1,..., 1, 1)t ∈ /CI
N . The
Neumann–Zagier matrices (A |B) have an important symplectic property, they are the upper
part of a symplectic matrix over /CI [1/2] (and even a symplectic matrix over /CI if one divides
the peripheral gluing equation by 2 while keeping the integrality of its c oeﬃcients) [ 29]. It
follows that ABt is symmetric, that ( A |B) has full rank, and that one can always choose a
quad such that B is invertible–for this see [ 11, Lem.A.3].
A further ingredient of a Neumann–Zagier datum is a ﬂattening, tha t is a triple ( f,f ′,f ′′)
of vectors in /CI
N that satisfy the conditions
f +f ′ +f ′′ = (1,..., 1)t, Gf + G′f ′ + G′′f ′′ = (2,..., 2, 0)t. (18)
Using our choice of quad, we can eliminate f ′ and thus obtain a pair ( f,f ′′) of vectors in /CI
N
that satisfy the condition
Af +Bf ′′ =ν. (19)
This deﬁnes all the terms that appear in a NZ-datum Ξ = ( A,B,ν,z,f,f ′′). The deﬁnition of
the series Φ Ξ (ℏ) requires a nondegenerate NZ datum Ξ, that is one that satisﬁes t he condition
det(B) ⁄= 0, which as we discussed above, can always be achieved, as well as t he condition
det(Λ) ⁄= 0. We discuss this choice next, and connect it to the geometric rep resentation of a
hyperbolic 3-manifold M.
We end this section with a comment regarding Neumann–Zagier data o f 3-manifolds
with several (as opposed to one) torus boundary components. T heir ideal triangulations
with equal number N of tetrahedra as edges and the edge gluing equations have the sam e
shape ( 14) as above. If r denotes the number of boundary components, then there are 2 r
peripheral equations ( 15) and after a choice of one peripheral curve per boundary compo-
nent, this leads to ( N +r) ×N matrices G, G′ and G′′. The edge gluing equations have
redundancy, and although it is not true that we can remove any r of them, it is shown in [ 18,
Sec.4.6] that one can remove r of them and and replace them by r peripheral equations so
as to obtain N ×N matrices G, G′ and G′′ such that the corresponding matrices ( A |B)
deﬁned in ( 17) have the same symplectic properties as in the case of r = 1. Moreover, any
two choices of removal of the r edge equations are related to each other by an invertible
matrix in GL r( /CI ). Finally, ﬂattenings satisfy Equations ( 18) where the right hand side of
the second equation is the vector (2 ,..., 2, 0,..., 0)t ∈ /CI
N +r with the ﬁrst N coordinates
equal to 2 and the remaining r coordinates equal to zero.
8 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WHE ELER
For simplicity in the presentation (related to the choice of periphera l curves and the
ﬂattenings), we will give the proof of Theorem 1.1 assuming that the 3-manifold M has one
cusp. The proof applies verbatim to the general case of arbitrary number of cusps.
