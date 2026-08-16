---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-033-61-a-brief-review-of-the-melvin-morton-rozansky
section_title: "A Brief Review of the Melvin-Morton-Rozansky Conjectu re"
section_number: 6.1
pages: 45-47
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
Let JN (K,q ) be the N -colored Jones polynomial of a knot K. We deﬁne a reduced
Jones polynomial as
VN (K,q ) = JN (K,q )
JN (unknot,q ), V N∈ Z Z[q,q −1] (6 .1)
44
where q = exp(2πi/k) and
JN (unknot,q ) = [N ] = qN/ 2−q−N/ 2
q1/ 2−q−1/ 2 (6.2)
is the N -colored Jones polynomial for the trivial knot.
Following [87], let us denote by J (tr)
N (K,q ) (resp. V (tr)
N (K,q )) the trivial connection
contribution to the colored Jones polynomial. Consider the Melvin-Morton expansion of
the colored Jones polynomial in powers of N and h =q− 1 [88],
V (tr)
N (K,q ) =
∑
m,n ≥0
Dm,n (K)N 2mhn (6.3)
Here, the rational numbers Dm,n (K) are Vassiliev invariants of order n [4,68], and we
assume that both N and k are integer. The extension to non-rational values of a = N/k
is related to the generalized volume conjecture and will be d iscussed further below.
It was conjectured by Melvin and Morton [88] and later proved by Rozansky [29], and
by Bar-Natan and Garoufalidis [89], that the coeﬃcients Dm,n (K) in the expansion (6.3)
have the following properties 20,
Dm,n = 0 for m>n/ 2
∑
m≥0
Dm, 2ma2m = 1
∇A(K,e iπa −e−iπa )
(6.4)
where ∇A(K,z ) is the Alexander polynomial of the knot K, normalized such that
∇A(unknot,z ) = 1. We remind, that the Alexander polynomial can be deﬁned b y the
skein relation,
∇A(L+,z )−∇ A(L−,z ) = z∇A(L0,z ) (6 .5)
corresponding to the link diagrams shown on the ﬁgure below.
L L L+ 0 −
Fig. 11: Link diagrams connected by the skein relation.
20 To avoid cluttering, in what follows we suppress the depende nce of Dm,n (K) on the knot K.
45
The bound on the powers of N allows to rewrite (6.3) in the form
V (tr)
N (K,q ) =
∑
n≥0
hn∑
m≥0
Dm,n +2m(Nh )2m (6.6)
which is reminiscent of the t’ Hooft expansion in a U (N ) gauge theory. Let us rewrite this
expansion in yet another form, replacing ( Nh ) with a new parameter
z =qN/ 2−q−N/ 2 = 2i sin(πa),
such that [90]:
Nh = 2 log
( √
1 +z2/4 +z/2
) h
log(1 +h) =z +... (6.7)
Then, the Melvin-Morton expansion (6.6) of the colored Jone s polynomial can be written
in the form
V (tr)
N (K,q ) =
∑
n≥0
V (n)(K,z )hn =
∑
n≥0
hn∑
m≥0
d(n)
m z2m (6.8)
In terms of the new variable z, the Melvin-Morton conjecture (6.4) turns into a statement
about the ﬁrst line in the expansion (6.8),
V (0)(K,z ) = 1
∇A(K,z ) (6.9)
which, among other things, implies that the coeﬃcients d(0)
m are all integer numbers. Rozan-
sky conjectured [90] and proved later [91], that all the coeﬃ cientsd(n)
m are integer numbers
and that the n-th line in the expansion (6.8) is a rational function of z:
V (n)(K,z ) = P (n)(K,z )
∇2n+1
A (K,z ) , P (n)(K,z )∈ Z Z[z2] (6 .10)
In order to understand a connection between the Melvin-Mort on-Rozansky and the
volume conjectures, it is helpful to look at the path integra l interpretation.
