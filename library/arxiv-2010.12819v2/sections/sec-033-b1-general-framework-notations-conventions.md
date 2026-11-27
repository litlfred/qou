---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-033-b1-general-framework-notations-conventions
section_title: "B.1 General framework, notations, conventions"
section_number: null
pages: 38-39
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
We shall follow the work in [58]. We ﬁrst ﬁx our notation. The XXZ R-matrix is written as
R(λ,µ ) =


1 0 0 0
0 b(λ,µ ) c(λ,µ ) 0
0 c(λ,µ ) b(λ,µ ) 0
0 0 0 1

 , (152)
with
b(λ,µ ) = sinh(λ−µ)
sinh(λ−µ +η), (153a)
c(λ,µ ) = sinh(η)
sinh(λ−µ +η) (153b)
andη =iγ. Since R only depends on the diﬀerenceλ−µ, we shall sometimes write it in terms of only one variable,
R(u)≡R(λ,µ ) withu =λ−µ. We write the corresponding monodromy matrix as T(u) =
(
A(u) B(u)
C(u) D(u)
)
, thereby
deﬁning the operators A,B,C,D that will be used below. Let a(λ) and d(λ) be the eigenvalues of A(λ) and
D(λ) when acting on |0⟩, where|0⟩ denotes the pseudo-vacuum of all spins pointing up. The Bethe equations
take the form
d(λj)
a(λj)
∏
k⁄=j
b(λk,λj)
b(λj,λk) = 1 (154)
for j = 1, 2,..., N
2−Sz, and an on-shell Bethe state is written as ∏
jB(λj)|0⟩ with the Bethe roots λj solving
(154). (If the roots do not solve the Bethe equations, the state is called oﬀ-shell.)
38
The above holds for periodic boundary conditions, but we also wish to consider boundary conditions
parametrized by a twist φ. Let κ∈GL2(C). Then κT gives us the monodromy matrix for the case of twisted
boundary conditions on the form σa
N+1 = κσa
1κ−1. For the boundary conditions that we wish to implement
(namely σz
N+1 =σz
1 and σ±
N+1 =e∓iφσ±
1 ) the proper choice is the following diagonal twist matrix:
κ =
(1 0
0 eiφ
)
. (155)
We obtain thus the twisted monodromy matrix
κT(u) =
(1 0
0 eiφ
)(A(u) B(u)
C(u) D(u)
)
=
( A(u) B(u)
eiφC(u) eiφD(u)
)
. (156)
Twisting the monondromy matrix T(u)→κT(u) in this fashion leads to a modiﬁed eigenvalue d(u)→eiφd(u)
that will enter into the Bethe equations, since the latter contain the ratios d(λk)
a(λk).
With a diagonal twist κ as above, any general Bethe considerations for the untwisted case will also be valid
for the twisted case. For instance, while (156) implies that B†(λ∗) = C(λ) for the untwisted case (up to a
phase), this same property will still hold after the twist (up to another phase). 16 Notice however that this does
not carry over to the general case of non-diagonal κ, where the dual Bethe states (deﬁned from C) might no
longer be given by the conjugate of the Bethe states (deﬁned from B).
