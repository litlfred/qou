---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-014-7-computations
section_title: "Computations"
section_number: 7
pages: 43-44
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
7.1. How to compute the coe
cients of a q-series. In this section we will explain a
general method to compute the coe
cients of a q-series which is given by a multi-dimensional
sum of some basic q-series. The idea is simple, but the eective aspects of it are tricky and
were explained to the 
rst author by D. Zagier. The method is applied in forthcoming work
[GV] which computes the coe
cients of the stabilization of the coloured Jones polynomial
of an alternating knot [GL].
Fix a 1-e
cient ideal triangulation T with n tetrahedra of a 1-cusped hyperbolic manifold
M and an oriented multi-curve ϖ on ∂M . The index IT(ϖ)(q)∈ Z((q1/2)) is given by a
convergent (n−1)-dimensional sum over the integers of a summand that depends on the angle
structure equation matrices of T; see Equation (17). The summand of IT(ϖ) is a product of
tetrahedron indices (one per tetrahedron of T) of linear forms in k = (k1,...,k n−1)∈ Zn−1
and the turning number vectors (aϖ|bϖ) of ϖ.
The building block of the summand is the tetrahedron index I∆, whose degree (i.e., mini-
mum degree with respect to q) is a piecewise quadratic function on R2; see Section 4.2. By
a piecewise quadratic function on Rm, we mean that there exists a partition F of Rm into
a 
nite number of chambers whose boundaries are rational polyhedral cones such that the
restriction of the function to each chamber is given by a quadratic polynomial. It follows
that for 
xed ϖ, the degree δ(ϖ,k) of the summand in (17) is a piecewise quadratic function
de
ned on a partition FT of Rn−1. In a later publication, we will explain how to compute
FT directly from T. A priori, FT need not be a fan in Rn−1 as the cones in the partition may
not be convex.
Since T is 1-e
cient, it follows that its index IT(ϖ)(q) is a convergent series. In other
words, the degree of the summand is a proper function on Zn−1. Thus, for 
xed ϖ and every
44 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
half-integer N , the set {k∈ Zn−1 : δ(ϖ,k)≤ N} is 
nite. To compute the index of T,
we need to compute bounds on this 
nite set. Since δ is convex and piecewise quadratic, it
follows that to bound δ(ϖ,k), it su
ces to bound the restriction of δ(ϖ,k) to an arbitrary
ray ρ ={k′ρ0 : k′∈ N} of FT . Now δ(ϖ,k′ρ0) is a quadratic function of k′∈ N, and we
obtain sharp bounds for ki typically of the form ki =O(
√
N) and exceptionally of the form
ki =O(N). The latter happens when δ has linear growth on some ray of FT . These directions
of linear growth (also observed in [GL] in the context of stabilization of the coloured Jones
function) are computationally costly. For an example, see the case of the knot 61 discussed
below.
The bounds for ki discussed above are rigorous and sharp, and work well for n = 2 and
n = 3 tetrahedra. However, they quickly become ine
cient when n increases (e.g. n = 9).
The better way to proceed for larger n, as was explained to us by D. Zagier and is applied
successfully in [GV], is to use iterated summation . In the examples shown below for n = 2
and n = 3 iterated summation is not needed. For simplicity, we focus on 1-cusped manifolds
and their index for [ϖ] = 0 ∈ H1(∂M ; Z). The data presented below are available from
[Gara].
Remark 7.1 . If two 1-cusped hyperbolic 3-manifolds M and M′ have 1-e
cient ideal tri-
angulations T and T′ with equal angle structure matrices, then IT(0)(q) = IT′(0)(q). For
example, M and −M have such triangulations, where −M denotes the orientation reversed
cusped hyperbolic manifold. Also, Mφ and M−φ have such triangulations for a pseudo-
Anosov homeomorphism φ of a once punctured torus, where Mφ denotes the mapping torus
of φ.
