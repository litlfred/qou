---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-011-53-r-matrices-and-product-states
section_title: "R-matrices and product states"
section_number: 5.3
pages: 28-30
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
R-matrices and product states
Our Yang-Baxter characters are deﬁned by composing the homomorphism ρR : C[S∞] →
E0 with the unique tracial product state τ = N
n≥1
TrV
d
of E0 (2.4). In this section, we
28
brieﬂy discuss how this construction extends to a much larger class of extremal char-
acters when we change τ to a diﬀerent product state on E0: All extremal characters
with Thoma parameters summing to 1 can, together with their GNS representations,
be expressed in terms of R-matrices and product states. The essential diﬀerence to
our Yang-Baxter setting is that instead of the canonical trace τ, a diﬀerent product
state is used.
Let R ∈R0(V ) and Z ∈End(V ) such that [R, Z ⊗Z] = 0. We consider the
product state ωZ := N
n≥1 TrV (Z · ) on E0, which is tracial in restriction to ρR(C[S∞]).
Composed with ρR, we thus get a character ωR
Z := ωZ ◦ρR of S∞. As in Prop. 2.2,
one shows that ωR
Z is extremal.
We want to show that any extremal S∞-character with Thoma parameters (α, β)
satisfying P
i(αi + βi) = 1 is of this form. To this end, consider two Hilbert spaces
V1, V2, such that dim V1 and dim V2 equal the number of non-vanishing α’s and β’s,
respectively (which might be countably inﬁnite). Let us ﬁx orthonormal bases {ei}i
and {fj}j of V1 and V2, and trace class operators A ∈B(V1), B ∈B(V2) deﬁned by
Aei = αi · ei, Bfj = βj · fj.
Lemma 5.9. In the notation introduced above, consider the Hilbert space W := V1⊕V2
and the (now possibly inﬁnite dimensional) R-matrix F ⊞−F ∈R0(W). Then
ωF ⊞−F
A⊕B
:=
O
n≥1
TrW ((A ⊕B) · ) ◦ρF ⊞−F : S∞→C
(5.8)
is an extremal character of S∞. Its α-parameters are the eigenvalues of A, and its
β-parameters are the eigenvalues of B.
Proof. In view of the simple structure of F ⊞−F, it is easy to see that this operator
commutes with Z⊗Z, where Z := A⊕B. Thus ωF ⊞−F
A⊕B
is indeed an extremal character,
and it remains to compute its Thoma parameters. Using the orthogonality V1 ⊥V2
and the direct sum structure of Z = A ⊕B, one shows in close analogy to Prop. 4.4
(see, in particular, (4.7)), that for any n-cycle,
ωF ⊞−F
A⊕B (cn) = ωF
A(cn) + ω−F
B (cn) .
(5.9)
Furthermore,
ωF
A(cn) =
X
i1,...,in
αi1 · · · αin ⟨ei1 ⊗. . . ⊗ein, ei2 ⊗. . . ⊗ein ⊗ei1⟩=
X
i
αn
i ,
ω−F
B (cn) = (−1)n+1 X
j1,...,jn
βj1 · · · βjn ⟨fj1 ⊗. . . ⊗fjn, fj2 ⊗. . . ⊗fjn ⊗fj1⟩
= (−1)n+1 X
j
βn
j .
These two terms sum to the value of the extremal character with Thoma parameters
(α, β).
We next describe the GNS representation of ωF ⊞−F
A⊕B , which turns out to be closely
related to R-matrices as well. In the notation introduced above, let V := W ⊗W and
R := (F ⊞−F) ⊠1 ∈R0(V ) ,
(5.10)
where F ∈R0(V1), −F ∈R0(V2), and 1 ∈R0(W). In V , we ﬁx the unit vector
ξ :=
X
i
√αiei ⊗ei +
X
j
p
βjfj ⊗fj ∈W ⊗W = V.
(5.11)
29
This vector determines inclusions V ⊗n →V ⊗(n+1) by tensoring with ξ from the right,
and we denote the corresponding inductive limit Hilbert space Nξ
n≥1 V .
Proposition 5.10. Let χ be an extremal S∞-character with Thoma parameters (α, β)
satisfying P
i(αi +βi) = 1. Then the GNS data (πχ, Hχ, Ωχ) can be described in terms
of the previously introduced V, R, and ξ as
Ωχ =
O
n≥1
ξ,
Hχ = ρR(C[S∞])Ωχ,
πχ = ρR .
(5.12)
Proof. Observe that for w1, w2, w3, w4 ∈W, the R-matrix (5.10) acts according to
R(w1 ⊗w2 ⊗w3 ⊗w4) = ± w3 ⊗w2 ⊗w1 ⊗w4 ,
(5.13)
where the sign is negative if both w1 and w3 lie in V2, and positive otherwise.
Let w1, . . . , wn, u1, . . . , un ∈W, and σ ∈Sn. Then this action of R implies
ρR(σ)
n
O
k=1
(wk ⊗uk) = ±
n
O
k=1
(wσ−1(k) ⊗uk),
(5.14)
with the sign depending on the number of vectors wk lying in V2. From here one
veriﬁes
⟨
O
n≥1
ξ, ρR(σ)
O
n≥1
ξ⟩= χ(σ)
(5.15)
by following [24, Prop. 10.5, Prop. 10.6].
The representation in the above proposition is known (see the original literature
[32, 26] or the monograph [24], where also the relation to spherical representations of
S∞is discussed), but takes a particularly simple form in terms of our operations ⊞
and ⊠.
