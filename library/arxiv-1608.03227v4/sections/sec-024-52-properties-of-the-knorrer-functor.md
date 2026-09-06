---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-024-52-properties-of-the-knorrer-functor
section_title: "Properties of the Knorrer functor"
section_number: 5.2
pages: 25-26
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
CC :=
î
( ˜X1−−) ( Y1− Adg12 (Y2)++)
ó
Let us explain the equivariant structure of this matrix factorizatio n. Since B(2)-action does not change
entries of the complex CC , the B(2) equivariant structure of B(2) is trivial.
To describe B(1) equivariant structure, let us write the diﬀerential of CC as
Dkn =Dkn
+ +Dkn
− , D kn
+ =
∑
k>l
( ˜X1,−−)klθkl,
Dkn
− =
∑
k>l
(Y1− Adg12 (Y2)++)lk
∂
∂θkl
,
where θij are odd variables. The equivariant structure is deﬁned by the actio n on θkl:
Eij·θkl =
∑
k>i
θki−
∑
j>l
θjl
The diﬀerential Dkn is not n(2) invariant:
Eij·Dkn
+ = 0, E ij·Dkn
− =
∑
j>l
[Adg12 (Y2)−]il
∂
∂θjl
−
∑
k>i
[Adg12 (Y2)−]ik
∂
∂θki
.
Thus the correction diﬀerentials are non-trivial in Φ( F ) but the correction diﬀerentials are not arbitrary and
below we emphasize properties of the correction diﬀerentials that a re needed for the proofs that follow.
Proposition 5.2. LetF = (M,D,∂ l,∂ r)∈ MFsc
B2(X 2,W ), M =Vm⊗ C[X 2], Vm∈ Modf ilt
n2 The matrix
factorization Φ(F )∈ MFsc
B2(X2,W ) is the equivariant matrix factorization
(Vm⊗ C[X2],D +Dkn, ˜∂l, ˜∂r)
where ˜∂r =∂r.
Proof. The only part that requires a discussion is the fact that the diﬀeren tial Φ(F )♯ has diﬀerential D+Dkn:
a priori our construction of the push forward jx
∗ (π∗
y (F )) relies on the extension lemma 3.1 and involves choice
of an extension ˜D ofD from variety ~X2 to X2 and completion of ˜D +Dkn
+ to the diﬀerential ˜D +Dkn
+ +d−
such that ( ˜D +Dkn
+ +d−)2 =W .
However, in our case map jx is actually a section of the (non-equivariant) map:
πx : X2→ ~X2, π x(X,g 1,Y 1,g 2,Y 2) = (Ad −1
g1 (X)+,g −1
1 g2,Y 2).
25
Thus according to the remark 3.3 we can choose ˜D to be D = ¯π∗(D) = π∗
x(π∗
y (D)). Moreover, d− = Dkn
−
because (D +Dkn)2 =W and the completion of the diﬀerential is unique up to an isomorphism. ✷
