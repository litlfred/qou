---
doc_id: arxiv-0906.1500v4
doc_title: "TWISTED ALEXANDER INV ARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS"
section_id: sec-023-2-m-is-endowed-with-h2-c2
section_title: "(M ) is endowed with h2 = c′2 ="
section_number: 2
pages: 18-19
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "TWISTED ALEXANDER INVARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS — W e study a computational method of the hyperbolic Reidemeister torsion (also"
---
{
[ [P ρ
1 ⊗ T 2
1 ] ], . . . ,[ [P ρ
b ⊗ T 2
b ] ]
}
.
With obvious notation, choose a set of vectors b′′i+1 in C′′
i+1 such that ∂′′
i+1(b′′i+1) is
a basis of B′′
i = im(∂′′
i+1 : C′′
i+1 → C′′
i ).
Observe that the set of vectors 1 ⊗ b′′i+1 in C′′
i+1(t) generates a subspace on which
the boundary operator ∂i+1 : Ci+1(t) → Ci(t) is injective.
With b′′3 = c′′3 in mind, the torsion of C′′
∗ (t) (with respect to the basis c′′∗) can be
computed as follows:
Tor(C′′
∗ (t), c′′∗, ∅) =
2∏
i=0
[
∂′′
i+1(1 ⊗ b′′i+1) 1 ⊗ b′′i/c′′i] (−1)i+1
=
2∏
i=0
[
c′i ∪ ∂i+1(bi+1)bi/c′i ∪ c′′i] (−1)i+1
.
Here bi denotes a lift of 1 ⊗ b′′i to C∗(t). As a result, we can rewrite
Tor(C′′
∗ (t), c′′∗, ∅) =
[
c′2∂3(b3)b2/c′2 ∪ c′′2] −1
(25)
·
[
c′1∂2(b2)b1/c′1 ∪ c′′1]
·
[
∂1(b1)/c′′0] −1
.
We want now to relate Equation (25) to an expression closer to the t orsion of the twisted
complex C∗(M ; sl2(C)ρ). For this we permute the vectors of ∂2(b2) and ∂1(b1) with the
ones of c′2 and c′1 in one of the determinants in Equation (25). Each set of c′1 and c′2
consists of b vectors and it is easy to observe that ∂3(b3) consists of dim C3(t)(= dim C3)
vectors and ∂2(b2) consists of rk ∂2 = dim C1(t) − b − dim C0(t) (≡ dim C0 + dim C1 + b
mod 2) vectors. Hence the sign arises from the permutation, whos e exponent is given by
b(dim C0 + dim C1 + b) + b dim C3. When we write ε = ( −1)b(dim C0+dim C1) and ( −1)α
for ( −1)b dim C3 as in Lemma 9, thus we have:
Tor(C′′
∗ (t), c′′∗, ∅) = ( −1)b+α · ε ·
[
∂3(b3)c′2b2/c′2 ∪ c′′2] −1
(26)
·
[
∂2(b2)c′1b1/c′1 ∪ c′′1]
·
[
∂1(b1)/c′′0] −1
.
18
By making a change of basis in Equation (26), we obtain the following ex pression:
Tor(C′′
∗ (t), c′′∗, ∅) = ( −1)b+α · (
∏
i/greaterorequalslant0
[
ci/c′i ∪ c′′i] (−1)i+1
)
· ε ·
[
∂3(b3)c′2b2/c2
] −1
·
[
∂2(b2)c′1b1/c1
]
·
[
∂1(b1)/c0] −1
.(27)
Moreover, using the deﬁnition of the bases c′1 and c′2, it is easy to observe that
lim
t→1
ε ·
[
∂3(b3)c′2b2/c2
] −1
·
[
∂2(b2)c′1b1/c1
]
·
[
∂1(b1)/c0] −1
= ε ·
[
∂3(b3)˜h2b2/c2
] −1
·
[
∂2(b2)˜h1b1/c1
]
·
[
∂1(b1)/c0] −1
(28)
= Tor(C∗, c∗, h∗).
The last step in Equations (28) is due to the fact that
(−1)|C∗| = (−1)α1(C∗)β1(C∗) = (−1)(dim C1+dim C0)b = ε.
Hence, combining Equations (27) and (28), we obtain
lim
t→1
Tor(C′′
∗ (t), c′′∗, ∅) = ( −1)b+α(
∏
i/greaterorequalslant0
[ci/c′i ∪ c′′i](−1)i+1
) · Tor(C∗, c∗, h∗)
which is exactly the desired equality because TM
λ (ρ) = τ0 · Tor(C∗, c∗, h∗). □
We ﬁnish the proof by combining Equation (23) and (24) and using the deﬁnition of
the polynomial torsion ∆ ϕ⊗Ad◦ρ
M (t) given in Equation (20).
