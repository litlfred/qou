---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-015-53-the-gns-description
section_title: "The GNS description"
section_number: 5.3
pages: 44-46
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Given our multiplicative unitary
W =e
i
2πb 2 log A−1⊗log ˆAgb(B⊗q ˆB ˆA−1)∈M (A⊗B (H)), (5.28)
the space ˆA⊂B (H) is originally deﬁned to be
ˆA ={(ω⊗ 1)W :ω∈A ∗}norm closure. (5.29)
In order to ﬁnd the GNS representation ˆΛ of ˆA on the original space HL, we
introduce the contraction map λ [24, (8.2)] which relates A∗ to the deﬁnition of
ˆA above using the multiplicative unitary, and the ξ map [24, Notation 8.4], which
relatesA∗ to the original GNS representation space HL ofA by the Riesz’s theorem
for Hilbert spaces. Then ˆΛ is just the composition of the two maps, which is
naturally compatible with the previous GNS construction for A.
Deﬁnition 5.10. Forω∈A ∗,x∈A , we deﬁne
λ : A∗−→ ˆA
λ(ω) = ( ω⊗ 1)W. (5.30)
and
ξ : A∗−→H L
ω(x∗) = ⟨ξ(ω), Λ(x)⟩L (5.31)
Then the GNS map ˆΛ is given by
ˆΛ : ˆA−→H L
ˆΛ(λ(ω)) = ξ(ω). (5.32)
Proposition 5.11. λ is the identity map from A∗ to ˆA as elements in B(H).
Proof. Using the second form (4.62) for W , and the integral form (4.58) for gb, we
get
W =
( ∫
R+i0
Bib−1τA−ib−1τ⊗ ˆBib−1τ
Gb(Q +iτ ) dτ
)
e
i
2πb 2 log A−1⊗log ˆA.
By the pairing (5.21) we have
λ(ω) =
( ∫∫
ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt⊗ 1
)
(W )
=
∫∫
ˆf (s,t ) (q2ib−1s)−ib−1t
Gb(Q +it) Gb(Q +it)e−2πist ˆBib−1t ˆA
i
2πb 2 (2πbs)dsdt
=
∫∫
ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt.
44
Proposition 5.12. The map ξ :A∗⊂ ˆH−→H is given by:
ξ : ˆf (s,t )↦→F (s,t ) :=
∫
R
ˆf (s′,iQ−t)Gb(−it)e2πis′(s+t−iQ)ds′, (5.33)
it naturally extends to an invertible map ξ : ˆH−→H with the inverse given by
ξ−1 :F (s,t )↦→ˆf (s,t ) :=
∫
R
F (s′,iQ−t)
Gb(Q +it) e2πis(t−s′)ds′. (5.34)
Proof. Let ω =
∫∫ ˆf (s,t ) ˆBib−1t ˆAib−1sdsdt,x =
∫∫
g(s,t )Aib−1sBib−1tdsdt. Then
ω(x∗) = ⟨ξ(ω), Λ(x)⟩L
LHS =
∫∫∫
g(−s,−t)e2πistF (s′,t )Gb(Q +it)e−2πis′s−2πis′t−2πistds′dsdt
=
∫∫∫
g(−s,−t)F (s′,t )Gb(Q +it)e−2πis′s−2πis′tds′dsdt
RHS =
∫∫
g(s,t + iQ
2 )ξ(ω)(s,t + iQ
2 )dsdt
=
∫∫
g(s,t− iQ
2 )ξ(ω)(s,t + iQ
2 )dsdt
=
∫∫
g(−s,−t)ξ(ω)(−s,−t +iQ)dsdt.
Hence
ξ(ω)(s,t ) =
∫
F (s′,iQ−t)Gb(Q +i(iQ−t))e2πis′s−2πis′(iQ−t)ds′
=
∫
F (s′,iQ−t)Gb(−it)e2πis′(s+t−iQ)ds′.
We observe that ξ can be realized as
ξ =Fs◦Pt◦Gb(Q +it)e−2πist,
whereFs is Fourier transform on s, Ptf (t) := f (iQ−t) and Gb(Q +it)e−2πist is
just multiplication by this function. Hence we have
ξ−1 =Gb(Q +it)−1e2πist◦P −1
t ◦F −1
s ,
or the formula desired.
Proposition 5.13. ξ is an isometry, ξ : ˆH−→H .
45
Proof. We have
⟨ξ( ˆf ),ξ (ˆg)⟩L
=
∫
R
∫
R
ˆg(s′′,iQ− (t + iQ
2 ))Gb(−i(t + iQ
2 ))e2πis′′(s+(t+ iQ
2 )−iQ)
ˆf (s′,iQ− (t + iQ
2 ))Gb(−i(t + iQ
2 ))e2πis′(s+(t+ iQ
2 )−iQ)ds′ds′′dsdt
=
∫
R
∫
R
ˆg(s′′,−t + iQ
2 )Gb(Q
2−it)e−2πis′′(s+t+ iQ
2 )
ˆf (s′,−t + iQ
2 )Gb(Q
2−it)e2πis′(s+t− iQ
2 )ds′ds′′dsdt
=
∫
R
∫
R
ˆg(s′′,t + iQ
2 ) ˆf (s′,t + iQ
2 )e−2πis′′(s−t+ iQ
2 )e2πis′(s−t− iQ
2 )ds′ds′′dsdt
=
∫
R
∫
R
ˆg(s′′,t + iQ
2 ) ˆf (s′,t + iQ
2 )e−2πis′′(−t+ iQ
2 )e2πis′(−t− iQ
2 )e2πis(−s′′+s′)ds′ds′′dsdt
=
∫
R
∫
R
ˆg(s,t + iQ
2 ) ˆf (s,t + iQ
2 )e−2πis(−t+ iQ
2 )e2πis(−t− iQ
2 )dsdt
=
∫
R
∫
R
ˆg(s,t + iQ
2 ) ˆf (s,t + iQ
2 )e2πQsdsdt
=
∫
R
∫
R
ˆg(s,t + iQ
2 ) ˆf (s,t + iQ
2 )e2πQsdsdt
= ⟨ ˆf, ˆg⟩ˆL.
Hence we conclude that
Corollary 5.14. ˆΛ(ω) := ξ(ω) gives the GNS representation for ˆA onH as desired.
