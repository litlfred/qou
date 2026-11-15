---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-020-53-the-gns-description
section_title: "The GNS description"
section_number: 5.3
pages: 44-46
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
The GNS description
Given our multiplicative unitary
W = e
i
2πb2 log A−1⊗log ˆ
Agb(B ⊗q ˆB ˆA−1) ∈M(A ⊗B(H)),
(5.28)
the space ˆ
A ⊂B(H) is originally deﬁned to be
ˆ
A = {(ω ⊗1)W : ω ∈A∗}norm closure.
(5.29)
In order to ﬁnd the GNS representation ˆΛ of
ˆ
A on the original space HL, we
introduce the contraction map λ [24, (8.2)] which relates A∗to the deﬁnition of
ˆ
A above using the multiplicative unitary, and the ξ map [24, Notation 8.4], which
relates A∗to the original GNS representation space HL of A by the Riesz’s theorem
for Hilbert spaces.
Then ˆΛ is just the composition of the two maps, which is
naturally compatible with the previous GNS construction for A.
Deﬁnition 5.10. For ω ∈A∗, x ∈A, we deﬁne
λ
:
A∗−→ˆ
A
λ(ω)
=
(ω ⊗1)W.
(5.30)
and
ξ
:
A∗−→HL
ω(x∗)
=
⟨ξ(ω), Λ(x)⟩L
(5.31)
Then the GNS map ˆΛ is given by
ˆΛ
:
ˆ
A −→HL
ˆΛ(λ(ω))
=
ξ(ω).
(5.32)
Proposition 5.11. λ is the identity map from A∗to ˆ
A as elements in B(H).
Proof. Using the second form (4.62) for W, and the integral form (4.58) for gb, we
get
W =
 Z
R+i0
Bib−1τA−ib−1τ ⊗ˆBib−1τ
Gb(Q + iτ)
dτ
!
e
i
2πb2 log A−1⊗log ˆ
A.
By the pairing (5.21) we have
λ(ω)
=
ZZ
ˆf(s, t) ˆBib−1t ˆAib−1sdsdt ⊗1

(W)
=
ZZ
ˆf(s, t)(q2ib−1s)−ib−1t
Gb(Q + it)
Gb(Q + it)e−2πist ˆBib−1t ˆA
i
2πb2 (2πbs)dsdt
=
ZZ
ˆf(s, t) ˆBib−1t ˆAib−1sdsdt.
44
Proposition 5.12. The map ξ : A∗⊂ˆH −→H is given by:
ξ : ˆf(s, t) 7→F(s, t) :=
Z
R
ˆf(s′, iQ −t)Gb(−it)e2πis′(s+t−iQ)ds′,
(5.33)
it naturally extends to an invertible map ξ : ˆH −→H with the inverse given by
ξ−1 : F(s, t) 7→ˆf(s, t) :=
Z
R
F(s′, iQ −t)
Gb(Q + it) e2πis(t−s′)ds′.
(5.34)
Proof. Let ω =
RR ˆf(s, t) ˆBib−1t ˆAib−1sdsdt, x =
RR
g(s, t)Aib−1sBib−1tdsdt. Then
ω(x∗)
=
⟨ξ(ω), Λ(x)⟩L
LHS
=
ZZZ
g(−s, −t)e2πistF(s′, t)Gb(Q + it)e−2πis′s−2πis′t−2πistds′dsdt
=
ZZZ
g(−s, −t)F(s′, t)Gb(Q + it)e−2πis′s−2πis′tds′dsdt
RHS
=
ZZ
g(s, t + iQ
2 )ξ(ω)(s, t + iQ
2 )dsdt
=
ZZ
g(s, t −iQ
2 )ξ(ω)(s, t + iQ
2 )dsdt
=
ZZ
g(−s, −t)ξ(ω)(−s, −t + iQ)dsdt.
Hence
ξ(ω)(s, t)
=
Z
F(s′, iQ −t)Gb(Q + i(iQ −t))e2πis′s−2πis′(iQ−t)ds′
=
Z
F(s′, iQ −t)Gb(−it)e2πis′(s+t−iQ)ds′.
We observe that ξ can be realized as
ξ = Fs ◦Pt ◦Gb(Q + it)e−2πist,
where Fs is Fourier transform on s, Ptf(t) := f(iQ −t) and Gb(Q + it)e−2πist is
just multiplication by this function. Hence we have
ξ−1 = Gb(Q + it)−1e2πist ◦P −1
t
◦F−1
s ,
or the formula desired.
Proposition 5.13. ξ is an isometry, ξ : ˆH −→H.
45
Proof. We have
⟨ξ( ˆf), ξ(ˆg)⟩L
=
Z
R
Z
R
ˆg(s′′, iQ −(t + iQ
2 ))Gb(−i(t + iQ
2 ))e2πis′′(s+(t+ iQ
2 )−iQ)
ˆf(s′, iQ −(t + iQ
2 ))Gb(−i(t + iQ
2 ))e2πis′(s+(t+ iQ
2 )−iQ)ds′ds′′dsdt
=
Z
R
Z
R
ˆg(s′′, −t + iQ
2 )Gb(Q
2 −it)e−2πis′′(s+t+ iQ
2 )
ˆf(s′, −t + iQ
2 )Gb(Q
2 −it)e2πis′(s+t−iQ
2 )ds′ds′′dsdt
=
Z
R
Z
R
ˆg(s′′, t + iQ
2 ) ˆf(s′, t + iQ
2 )e−2πis′′(s−t+ iQ
2 )e2πis′(s−t−iQ
2 )ds′ds′′dsdt
=
Z
R
Z
R
ˆg(s′′, t + iQ
2 ) ˆf(s′, t + iQ
2 )e−2πis′′(−t+ iQ
2 )e2πis′(−t−iQ
2 )e2πis(−s′′+s′)ds′ds′′dsdt
=
Z
R
Z
R
ˆg(s, t + iQ
2 ) ˆf(s, t + iQ
2 )e−2πis(−t+ iQ
2 )e2πis(−t−iQ
2 )dsdt
=
Z
R
Z
R
ˆg(s, t + iQ
2 ) ˆf(s, t + iQ
2 )e2πQsdsdt
=
Z
R
Z
R
ˆg(s, t + iQ
2 ) ˆf(s, t + iQ
2 )e2πQsdsdt
=
⟨ˆf, ˆg⟩ˆL.
Hence we conclude that
Corollary 5.14. ˆΛ(ω) := ξ(ω) gives the GNS representation for ˆ
A on H as desired.
