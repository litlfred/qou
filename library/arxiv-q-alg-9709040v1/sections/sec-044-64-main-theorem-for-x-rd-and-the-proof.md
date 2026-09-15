---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-044-64-main-theorem-for-x-rd-and-the-proof
section_title: "Main Theorem for X = Rd, and the proof"
section_number: 6.4
pages: 24-25
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
We deﬁne an L∞-morphismU :Tpoly(Rd)−→Dpoly(Rd) by the formula for its n-th derivativeUn, n≥ 1
considered as a skew-symmetric polylinear map (see 4.2) fro m⊗nTpoly(Rd) to Dpoly(Rd)[1−n]:
Un =
∑
m≥0
∑
Γ∈Gn,m
WΓ ×U Γ .
HereGn,m denotes the set of all admissible graphs with n vertices of the ﬁrst type, m vertices in the second
group and 2n +m− 2 edges, where n≥ 1, m≥ 0 (and automatically 2 n +m− 2≥ 0).
Theorem. U is an L∞-morphism, and also a quasi-isomorphism.
Proof: ﬁrst of all, we should check that Un is skew-symmetric, i.e. that U is a pre-L∞-morphism. For
this see subsection 6.5.
The condition that U is an L∞-morhism (see 4.3 and 3.4.2) can be written explicitly as
f1· (Un(γ1∧... ∧γn)) (f2⊗... ⊗fm)± (Un(γ1∧... ∧γn)) (f1⊗... ⊗fm−1)·fm+
+
m−1∑
i=1
± (Un(γ1∧... ∧γn)) (f1⊗... ⊗ (fifi+1)⊗... ⊗fm)+
+
∑
i⁄=j
± (Un−1([γi,γ j]∧γ1∧... ∧γn)) (f1⊗... ⊗fm)+
+ 1
2
∑
k,l≥1, k +l=n
1
k!l!
∑
σ∈Σ n
±
[
Uk(γσ 1∧... ∧γσ k ),Ul(γσ k+1∧... ∧γσ n )
]
(f1⊗... ⊗fm) = 0 .
Hereγi are polyvector ﬁelds, fi are functions,Un are homogeneous components of U (see 4.1). There is
a way to rewrite this formula. Namely, we deﬁne U0 as the map ⊗0(Tpoly(Rd))−→Dpoly(Rd)[1] which maps
the generator 1 of R≃⊗ 0(Tpoly(Rd)) to the product mA∈D1
poly(Rd) in the algebra A :=C∞(Rd). Here
mA :f1⊗f2↦→f1f2 is considered as a bidiﬀerential operator.
The condition from above for U to be an L∞-morphism is equivalent to the following one:
∑
i⁄=j
± (Un−1((γi•γj)∧γ1∧... ∧γn)) (f1⊗... ⊗fm)+
+
∑
k,l≥0, k +l=n
1
k!l!
∑
σ∈Σ n
±
(
Uk(γσ 1∧... ∧γσ k )◦U l(γσ k+1∧... ∧γσ n )
)
(f1⊗... ⊗fm) = 0 .
Here we use deﬁnitions of brackets in Dpoly and Tpoly via operations◦ (see 3.4.2) and • (see 4.6.1). We
denote the l.h.s. of the expression above as ( F ).
U +U0 is not a pre-L∞-morphism because it maps 0 to a non-zero point mA. Still the equation ( F ) = 0
makes sense and means that the map ( U +U0) from formal Q-manifold Tpoly(Rd)[1]
)
f ormal to the formal
neighborhood of point mA in super vector space Dpoly(Rd)[1] is Q-equivariant, where the odd vector ﬁeld Q
on the target is purely quadratic and comes from the bracket o nDpoly(Rd), forgetting the diﬀerential.
Also, the term U0 comes from the unique graph Γ 0 which was missing in the deﬁnition of U. Namely,
Γ 0 has n = 0 vertices of the ﬁrst type, m = 2 vertices of the second type, and no edges at all. It is easy t o
see that WΓ 0 = 1 and UΓ 0 =U0.
24
We consider the expression ( F ) simultaneously for all possible dimensions d. It is clear that one can
write (F ) as a linear combination
∑
Γ
cΓ ·U Γ
(
γ1⊗... ⊗γn)
)
(f1⊗... ⊗fm)
of expressionsUΓ for admissible graphs Γ with n vertices of the ﬁrst type, m vertices of the second type, and
2n +m− 3 edges where n≥ 0, m≥ 0, 2n +m− 3≥ 0. We assume that cΓ =±cΓ ′ if graph Γ ′ is obtained
from Γ by a renumeration of vertices of ﬁrst type and by a relab eling of edges in sets Star(v) (see 6.5 where
we discuss signs).
Coeﬃcients cΓ of this linear combination are equal to certain sums with sig ns of weightsWΓ ′ associated
with some other graphs Γ ′, and of products of two such weights. In particular, numbers cΓ do not depend
on the dimension d in our problem. Perhaps it is better to use here the language o f operads, but we will not
do it.
We want to check that cΓ vanishes for each Γ.
The idea is to identify cΓ with the integral over the boundary ∂Cn,m of the closed diﬀerential form
constructed from Γ as in 6.2. The Stokes formula gives the van ishing:
∫
∂ C n,m
⋀
e∈EΓ
dφe =
∫
Cn,m
d
( ⋀
e∈EΓ
dφe
)
= 0 .
We are going to calculate integrals of the form ∧e∈EΓdφe restricted to all possible boundary strata of
∂Cn,m , and prove that the total integral as above is equal to cΓ . At the subsection 5.2 we listed two groups
of boundary strata, denoted by S1 and S2 and labeled by sets or pairs of sets. Thus,
0 =
∫
∂ C n,m
⋀
e∈EΓ
dφe =
∑
S
∫
∂ S C n,m
⋀
e∈EΓ
dφe +
∑
S,S ′
∫
∂ S,S ′ C n,m
⋀
e∈EΓ
dφe .
