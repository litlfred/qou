---
doc_id: arxiv-math-9808030v1
doc_title: "Planscherel Measure on Eq(2)"
section_id: sec-003-2-invariant-integral-on-eq2
section_title: "Invariant Integral on Eq(2)"
section_number: 2
pages: 3-6
source_pdf: 9808030v1.pdf
source_sha256: 7889d6481b876b12
doc_brief: "Planscherel Measure on Eq(2) — Following the construction of the invariant integral and the scalar p roduct for the quantum Euclidean group Eq(2), we obtained the full matrix elements of its unitary"
---
Let us start by reviewing the construction of the invariant integra l for SUq(2)
which will guide in Eq(2) case.
Rewiev of the invariant integral on SUq(2)
The coordinate functions x, u, x∗, u∗ generating the ∗–Hopf algebra
A(SUq(2)) satisfy the following relations [2]
u(x) = qxu, x ∗u =qux∗, uu ∗ =u∗u,
xx∗ +uu∗ = 1, x ∗x +q2uu∗ = 1. (II.1)
In q → 1 limit the above relations deﬁne the three dimensional sphere S3
which is the topological manifold of SU (2). In q ⁄= 1 case we consider
irreducible ∗–representation π of the associative algebra A(SUq(2)) in the
Hilbert space L2(Z) with the orthonormal basis {|n⟩}n∈Z [3]
π(x) |n⟩ = (1 −q2n)1/ 2 |n − 1⟩, π (u) |n⟩ =qn |n⟩,
π(u∗) |n⟩ =qn |n⟩, π (x∗) |n⟩ = (1 −q2n+2)1/ 2 |n + 1⟩ (II.2)
for 0 < q < 1. We associate a vector v ∈ L 2(Z) to each point of the
“topological space” SUq(2). Then
fv = ⟨v |π(f ) |v⟩ (II.3)
gives the value of any function f ∈A(SUq(2)) at this point. Thus by topolog-
ical space of the quantum group SUq(2) we mean the carrier space L2(Z) of
the ∗–representation of A(SUq(2)). By the subspace Xq of SUq(2) we mean
the subspace H ′ of the Hilbert space L2(Z). The empty set in SUq(2) is the
empty set in L2(Z). Two subspaces Xq and X ′
q of SUq(2) are said to have
zero intersection (Xq
⋂
X ′
q = ∅ ) if the corresponding subspaces H andH ′ of
the Hilbert space L2(Z) has zero intersection. The union and intersection of
subspaces Xq, X ′
q ⊂SUq(2) are understood as the union and intersection of
corresponding subspaces H, H ′ ⊂ L 2(Z).
3
Consider the linear map µ :SUq(2) → [0, ∞) deﬁned by
µ(Xq) = (1 −q2)
∑
n∈J
⟨n |π(µS) |n⟩, (II.4)
whereJ ⊂Z, such that the vectors |n⟩,n ∈J span the subspace H of L2(Z)
corresponding to the subspace Xq ofSUq(2), µS ∈A(SUq(2)). Since the left
hand side of the above expression is positive deﬁnite the operator π(µS) must
be self–adjoint and positive deﬁnite in L2(Z0). To make the linear map (II.4)
a measure on SUq(2) we have to impose the additivity condition
µ(
⋃
j
Xqj ) =
∑
j
µ(Xqj ) (II.5)
for the disjoint subspaces Xqj of SUq(2). Inspecting (II.2) and (II.4) we
conclude that µS is a polynomial of ξ =uu∗. The measure on SUq(2) is then
given by
µ(Xq) = (1 −q2)
∑
n∈J
⟨n |π(µS(ξ)) |n⟩ = (1 −q2)
∑
n∈J
µS(q2n). (II.6)
By means of the measure µ on the quantum group SUq(2) we introduce
the linear functional ψ :A(SUq(2)) →C as
ψ (f ) = (1 −q2)
∞∑
n=0
⟨n |π(fµS) |n⟩. (II.7)
If f is the function of ξ only we can rewrite (II.7) as
ψ (f ) =
∫ 1
0
f (ξ)dq2µS(ξ). (II.8)
On the other hand the invariant integral on SUq(2) is [3]
ψ (f ) =
∫ 1
0
f (ξ)dq2ξ. (II.9)
Comparing to (II.8) we see that if
µS(ξ) = ξ, (II.10)
4
the linear functional (II.7) deﬁnes the invariant integral on SUq(2). Hence,
the invariant measure and invariant integral on the quantum group SUq(2)
are given by
µ(Xq) = (1 −q2)
∑
n∈J
q2n (II.11)
and
ψ (f ) = (1 −q2)
∞∑
n=0
⟨n |π(fξ) |n⟩ (II.12)
respectively. Here J ⊂Z, such that the vectors |n⟩,n ∈J span the subspace
H of L2(Z) corresponding to the subspace Xq of SUq(2).
Invariant integral on Eq(2)
In fashion parallel to SUq(2) we can deﬁne the invariant measure on Eq(2).
The irreducible ∗–representationπ of the algebra of polynomials on Eq(2) is
constructed in the Hilbert space L2(S) of square integrable functions on the
circle S. In the orthonormal basis |j⟩ = 1√
2πeijψ , −∞<j < ∞ we have
π(z) |j⟩ =q−j |j − 1⟩, π (z∗) |j⟩ =q−j−1 |j + 1⟩, π (δ) |j⟩ =|j − 2⟩.
(II.13)
Thus as topological space the quantum Euclidean group Eq(2) is equivalent
to the Hilbert space L2(S). The measure on Eq(2) is given by
µ(Xq) = (1 −q2)
∑
j∈J
⟨j |π(µE) |j⟩, (II.14)
where µE is polynomial of coordinate functions z, z∗, δ±1; and J ⊂ Z such
that the vectors | j⟩, j ∈ J, span a basis in the subspace H ⊂ L 2(S) cor-
responding to the subspace Xq ⊂ Eq(2). Since Eq(2) can be obtained from
SUq(2) by contraction we deﬁne µE from µS of (II.11) as
µE = limr→∞(r2µS(u0u∗
0
r2 )) = zz ∗ =ρ2. (II.15)
Thus the invariant measure on Eq(2) is given by
µ(Xq) = (1 −q2)
∑
j∈J
⟨j |π(ρ2) |j⟩ =N
∑
j∈J
q−2j. (II.16)
5
By the virtue of the invariant measure we deﬁne the invariant integr al on
Eq(2) as
ψ (f ) = (1 −q2)
∞∑
j=−∞
⟨j |π(fρ 2) |j⟩, (II.17)
provided that the left–hand side is ﬁnite. If f (g) = f (ρ) the above expression
can be rewritten by means of q–integral as
ψ (f ) =
∫ ∞
−∞
f (ρ)dq2(ρ2). (II.18)
The invariant measure and invariant integral on the quantum group Eq(2)
are then given by
µ(Xq) = (1 −q2)
∑
j∈J
q−2j (II.19)
and
ψ (f ) = (1 −q2)
∞∑
j=−∞
⟨j |π(fρ 2) |j⟩ (II.20)
respectively. The subset J ⊂ Z is deﬁned such that the vectors | j⟩, j ∈ J
span the subspace H ⊂ L 2(S) corresponding to the subspace Xq of Eq(2).
