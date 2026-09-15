---
doc_id: arxiv-math-0408210v3
doc_title: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM"
section_id: sec-005-22-the-chern-weil-homomorphism
section_title: "The Chern-Weil homomorphism"
section_number: 2.2
pages: 5-9
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
doc_brief: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
Let g be a Lie algebra and h ⊂ g be a subalgebra of g. Suppose that there is an h-equivariant
projection pr : g ↦→h, that is a map commuting with the adjoint action of h and satisfying
the property pr |h =Id h. The amount by which pr fails to be a Lie algebra homomorphism
is measured by the “curvature” C ∈Hom(∧2g, h)
C(v,w ) = [pr(v),pr (w)] −pr([v,w ]), v,w ∈ g. (7)
Given the “curvature” (7) of the h-equivariant projection pr, it is not hard to see that
for any adjoint invariant form Q ∈ ((Sjh)∗)h the formula
χ (Q)(v1,...,v 2j) = 1
(2j)!
∑
ν∈S2j
(−)νQ(C(vν(1),v ν(2)),...,C (vν(2j−1),v ν(2j))) (8)
deﬁnes a relative Lie algebra cocycle χ (Q) ∈C 2j(g, h). The standard argument of the theory
of characteristic classes shows that the cohomology class [ χ (Q)] of the cocycle χ (Q) does not
depend on the choice of the projection pr. Thus (8) induces a map from the vector space
((Sjh)∗)h to H 2j(g, h). The latter map is called the Chern-Weil homomorphism .
In our case we set g = glN (W), h = glN ⊕ sp2n and deﬁne the projection pr from g to h
by the formula
pr(v) = pr0(v) +pr2(v), (9)
pr0(v) = v
⏐⏐⏐
y=0
, pr 2(v) = 1
Nσ2(tr(v))IN,
where σ2 denotes the projection onto the monomials of the second degree in y’s,tr is the
ordinary matrix trace, IN is the identity matrix of size N ×N, and the Lie algebra sp2n is
realized as a subalgebra of scalar matrices in glN (W) with values in quadratic monomials in
W .
Due to [10] we have the following
Theorem 1 (Feigin-Felder-Shoikhet [10]) The Lie algebra cocycle Θ N
2n ∈ C 2n(g, g∗) is
relative with respect to the subalgebra h = glN ⊕ sp2n. The evaluation of (6) on the identity
matrix IN ∈ g gives a relative Lie algebra cocycle
ϕ ∈C 2n(g, h)
ϕ = Θ N
2n(·,..., ·,I N ) : ∧2n(g) ↦→C((ℏ))
5
whose cohomology class
[ϕ ] = [χ (Qn)], (10)
coincides with the image of the n-th componentQn ∈ ((Snh)∗)h of the adjoint invariant form
Q ∈ ((Sh)∗)h
Q(X,...,X ) = det
( X1/ 2ℏ
sinh (X1/ 2ℏ)
) 1/ 2
tr exp
( X2
ℏ
)
, (11)
X =X1 ⊕X2 ∈ sp2n ⊕ glN
under the Chern-Weil homomorphism (8).
2.3 Fedosov deformation quantization with twisted coeﬃcie nts.
Let M be a symplectic manifold of dimension 2 n. We denote by ω = ω ij(x)dxidxj the
corresponding symplectic form and by
ω =ω ij(x) ∂
∂xi ∧ ∂
∂xj
the corresponding Poisson tensor. Here xi denote local coordinates and the indices i,j run
from 1 from 2 n . For a vector bundle V of rank N over M we will denote by End(V ) the
bundle of endomorphisms of V and by EndV = Γ( M,End (V )) the algebra of global sections
of End(V ) .
If the vector bundle V is endowed with a connection ∂V then
Deﬁnition 2 By quantization of the algebra EndV we mean a construction of an associative
C((h))-linear product in EndV ((ℏ)) given by the formal power series
a ∗b =ab +
∑
k≥1
ℏkBk(a,b ), a, b ∈EndV (12)
of bidiﬀerential operators Bk : EndV ⊗EndV ↦→EndV such that
B1(a,b ) −B1(b,a ) = ω ij(x)∂V
i (a)∂V
j (b).
In [9] B. Fedosov proposed a simple procedure for the deformation quantization of the
algebra of endomorphisms of a vector bundle V over a symplectic manifold M. The main
ingredient of the construction is the Weyl algebra bundle W (EndV ) whose sections are the
following formal power series
a =a(x,y,h ) =
∑
k,l
ℏkak;i1i2...i l(x)yi1...y il, (13)
where y = (y1...y 2n) are ﬁber coordinates of the tangent bundle T M, ak;i1i2...i l represent
sections of End(V ) ⊗Sl(T ∗M) and the summation over k is bounded below.
Multiplication of two sections of W (EndV ) is given by the Weyl formula
a ◦b(x,y, ℏ) = exp
( ℏ
2ω ij ∂
∂y i
∂
∂z j
)
a(x,y, ℏ)b(x,z, ℏ)|y=z. (14)
6
Notice that in the right hand side of (14) the sections of W (EndV ) are multiplied via the
product induced from the algebra EndV .
For any pointp ∈ M the ﬁber Wp(EndV ) of the Weyl algebra bundle at p is isomorphic to
the algebra glN (W) of N ×N-matrices of the Weyl algebra W associated with the cotangent
space T ∗
p (M) at the point p with the symplectic form ω p . The transition functions are
realized by the adjoint action of the group GLN .
The ﬁltration (4) of the Weyl algebra gives us a natural ﬁltration of the bundle W (EndV )
... ⊂W 1(EndV ) ⊂W 0(EndV ) ⊂W −1(EndV )... ⊂W (EndV ),
Γ(W m(EndV )) = {a =
∑
2k+p≥m
ℏkak;i1...i p(x)yi1...y ip}. (15)
This ﬁltration deﬁnes the 2[ ℏ] + [y]-adic topology in the algebra Γ( W (EndV )) of sections of
W (EndV ) .
The vector space Ω •(W (EndV )) of smooth exterior forms with values in W (EndV ) is
naturally a graded associative algebra with the product induced by ( 14) and the following
graded commutator
[a,b ] = a ◦b − (−)qaqbb ◦a,
where qa and qb are exterior degrees of a and b , respectively. The ﬁltration of W (EndV )
(15) gives us a ﬁltration of the algebra Ω •(W (EndV ))
... ⊂ Ω •(W 1(EndV )) ⊂ Ω •(W 0(EndV )) ⊂
⊂ Ω •(W −1(EndV )) ⊂... ⊂ Ω •(W (EndV )).
In what follows we refer to the algebra Ω •(M) of exterior forms on M as an algebra embedded
into Ω •(W (EndV )) via the natural map ι : Ω •(M) ↦→Ω •(W (EndV )), which sends an
exterior form η ∈ Ω •(M) to the scalar matrix ηIN ∈ Ω •(W (EndV )) .
Let ∂s be a torsion free connection on T M compatible with the symplectic structure ω .
Using the connection ∂s and the connection ∂V onV we deﬁne the following linear operator
∇ : Ω •(W (EndV )) ↦→Ω •+1(W (EndV )),
∇ =dxi ∂
∂xi −dxiΓ k
ij(x)yj ∂
∂y k + [Γ V, · ], (16)
where Γ k
ij(x) are Christoﬀel symbols of ∂s and Γ V is the connection form of ∂V .
Thanks to the compatibility of ∂s with the symplectic structure ω the operator (16) is a
derivation of the graded algebra Ω •(W (EndV )) . Furthermore, a simple computation shows
that
∇2a = 1
2 [R +RV,a ], ∀ a ∈ Ω(W (EndV )),
where RV ∈ Ω 2(EndV ) is the curvature form of ∂V ,
R = 1
2ℏω km(Rij)m
l (x)ykyldxidxj,
and (Rij)m
l (x) is the Riemann curvature tensor of ∂s .
7
Deﬁnition 3 The Fedosov connection is a nilpotent derivation of the grad ed algebra
Ω •(W (EndV )) of the following form
D = ∇ + 1
ℏ [A, · ], A = −dxiω ij(x)yj +r, (17)
wherer is an element in Ω 1(W 2(EndV ))
The ﬂatness of D is equivalent to the fact that the Fedosov-Weyl curvature
C W = ℏ(R +RV ) + 2∇A + 1
ℏ [A,A ] (18)
ofD belongs to the subspace Ω 2(M)((ℏ)) ⊂ Ω 2(W (EndV )) . A simple analysis of degrees in
ℏ and y shows that C W is of the form
C W = −ω + Ω ℏ, Ω h ∈ ℏΩ 2(M)[[ℏ]] (19)
whereas the Bianchi identity D(C W ) = 0 implies that Ω h is a series of two-forms closed with
respect to the De Rham diﬀerential.
One can observe that the deﬁnition of the Fedosov connection dep ends on the choice of
the symplectic connection ∂s and the connection ∂V onV . The following proposition shows
how this problem can be remedied
Proposition 1 If ∇ and ~∇ are two operator (16) corresponding to the symplectic conne c-
tions∂s, ~∂s and the connections ∂V , ~∂V onV , respectively, then the diﬀerence ~D −D between
two Fedosov connections
~D = ~∇ + 1
ℏ [−dxiω ij(x)yj + ~r, · ], D = ∇ + 1
ℏ [−dxiω ij(x)yj +r, · ], (20)
takes the form of the commutator
~D −D = 1
ℏ [∆r, · ],
where ∆r ∈ Ω 1(W 2(EndV )) . In other words any deviations of the connections ∂s and ∂V
can be absorbed into the form r ∈ Ω 1(W 2(EndV )) .
Proof. See page 151 in [9] . ✷
Let us consider the aﬃne subspace IN ⊕ Γ(W 1(EndV )) in Γ(W (EndV )) consisting of the
sums U = IN +U1, where IN is the identity endomorphism of V and U1 is an arbitrary
element in Γ( W 1(EndV )). It is straightforward that
Proposition 2 The aﬃne subspace IN ⊕ Γ(W 1(EndV )) ⊂ Γ(W (EndV )) is a subgroup in
the group of invertible elements of Γ(W (EndV )) . ✷
We are now ready to give the following
Deﬁnition 4 Two Fedosov connections
D = ∇ + 1
ℏ [A, · ], ~D = ∇ + 1
ℏ [ ~A, · ]
are called equivalent if there exists an element U ∈IN ⊕ Γ(W 1(EndV )) such that
~D =D + [U −1 ◦DU, · ] (21)
or equivalently ~A =U −1 ◦A ◦U + ℏU −1 ◦ ∇U.
8
Let us remark that the Fedosov connection (17) can be rewritten as
D = ∇ −δ + 1
ℏ [r, · ], (22)
where
δ = 1
ℏ [dxiω ij(x)yj, · ] = dxi ∂
∂y i (23)
is the Koszul derivation of the algebra Ω •(W (EndV )) .
For our purposes we will need the homotopy operator for the Kosz ul diﬀerential δ
δ−1a =yki
( ∂
∂xk
) 1∫
0
a(x, ℏ,ty,tdx )dt
t , (24)
wherei(∂/∂x k) denotes the contraction of an exterior form with the vector ﬁeld ∂/∂x k , and
δ−1 is extended to Γ( W (EndV )) by zero.
Simple calculations show that δ−1 is indeed the homotopy operator for δ, namely
a =σ(a) +δδ−1a +δ−1δa, ∀ a ∈ Ω(W (EndV )) (25)
where σ is the natural projection
σ(a) = a
⏐⏐⏐
y=0, dx =0
, a ∈ Ω •(W (EndV )) (26)
from Ω •(W (EndV )) onto the algebra of endomorphisms EndV ((ℏ)) .
The proof of the following theorem is contained in section 5 . 3 of [9]. (More precisely, see
theorem 5. 3. 3 and remarks at the end of section 5 . 3)
Theorem 2 (Fedosov, [9]) If ∂s is a symplectic connection on M, ∂V is a connection on
V and Ω ℏ is a series of closed two-forms in ℏΩ 2(M)[[ℏ]] then
