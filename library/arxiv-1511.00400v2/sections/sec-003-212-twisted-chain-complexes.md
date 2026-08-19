---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-003-212-twisted-chain-complexes
section_title: "Twisted chain complexes"
section_number: 2.1.2
pages: 6-7
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Let K be a ﬁnite CW-complex. This paper is mostly interested in 3-manifolds
but also in surfaces and in S1, for which there is a canonical choice of PL-
structure. Let
ρ∶ π1K → SLn(F )
be a representation of its fundamental group. Consider the chain complex of
vector spaces
C∗(K; ρ) ∶= F n ⊗ρ C∗( ̃K; Z)
where C∗( ̃K; Z) denotes the simplicial complex of the universal covering and ⊗ρ
means that one takes the quotient of F n⊗Z C∗( ̃K; Z) by the Z-module generated
by
ρ(γ)tv ⊗ c − v ⊗ γ ⋅ c,
where v ∈F , γ ∈π1K and c ∈C∗( ̃K; Z), and t stands for transpose. Namely
v ⊗ γ ⋅ c = ρ(γ)tv ⊗ c ∀γ ∈π1K.
Instead of the transpose, one could use the inverse. For some re presentations
the inverse and transpose are the same or conjugate, but this is n ot true in
general, and here this is relevant for duality with cohomology.
The boundary operator is deﬁned by linearity and ∂(v ⊗ c) = v ⊗ ∂c, for v ∈F
and c ∈C∗( ̃K; Z). The homology of this complex is denoted by
H∗(K; ρ).
Analogously, one considers the cocomplex of cochains
C∗(K; ρ) ∶= homπ1K(C∗( ̃K; Z), F n)
that has a natural coboundary operator to deﬁne the cohomolog y
H ∗(K; ρ).
Then C∗(K; ρ) is a cocomplex of ﬁnite dimensional F -vector spaces. Choose
{v1, . . . , vn} a F -basis for F n and let {ei
1, . . . , ei
ji } denote the set of i-cells of K.
Then ci = {vr ⊗ ˜ei
s /divid⟩s.alt0r ≤n, s ≤ji} is a F -basis for Ci(K; ρ).
Let hi be a basis for Hi(K; ρ). One can now deﬁne the torsion by means of
chain complexes:
Deﬁnition 2.5. The torsion of (K, ρ, {hi}) is
tor(K, ρ, {hi}) = tor(C∗(K; ρ), {ci}, {hi}) ∈F ∗/slash.l⟩ft{±1}.
Remark 2.6. (a) This torsion does not depend on the lifts of the cells ˜ei nor
the basis {v1, . . . , vn} of F n.
(b) It does not depend either on the conjugacy class of ρ, taking care that the
bases for the homology are in correspondence via the natural isom orphism
between the homology groups of the conjugate representations .
Remark 2.7 (Sign indeterminacy) . The torsion lies in F ∗/slash.l⟩ft{±1}, but there are
ways to avoid the sign indeterminacy:
6
(a) When both the Euler characteristic χ(K) and n = dim ρ are even, then the
sign of this torsion is also well deﬁned, i.e. it lives in F ∗.
(b) When χ(K) is even but n = dim ρ is odd, the ordering of the cells is relevant:
If two cells are permuted in the construction, then the sign of the t orsion
is changed. To overcome this and to get an invariant in F ∗, Turaev [95]
noticed that given an ordering of the basis in homology with constant real
coeﬃcients, H∗(K; R), there is a natural way to order the cells of K, (so
that the torsion with trivial coeﬃcients is then positive). So if one ha s an
orientation of the the homology H∗(K; R), then there is a choice for the
sign of the torsion.
Remark 2.8. It is a topological invariant but not in its relative version, cf [80,
Remark 2.12]. Namely:
(a) It is an invariant of the simple homotopy type of K. Hence, by Chapman’s
theorem [12], tor (K, ρ, {hi}) is invariant by homeomorphisms.
Working with manifolds of dimension ≤3, uniqueness of the triangulation
up to subdivision is an alternative to Chapman’s theorem.
(b) However there is a well deﬁned notion of torsion of a pair of CW-c omplexes
(K, L), but then the torsion is not a topological invariant of a pair. In fact
Milnor used Reidemeister torsion of a pair to distinguish two homeomor phic
simplicial complexes that are not combinatorially equivalent [66].
We deal now with the construction using cohomology. Consider eleme nts
(˜ei
r)⋆ ⊗ v∶ Ci( ˜K; Z) → F n as the morphism of π1K-modules deﬁned by
/par⟩nl⟩ft.alt1(˜ei
r)⋆ ⊗ v/par⟩nright.alt1 (˜ei
s) = /brac⟩l⟩ft.alt4 v if s = r,
0 if s ≠r.
Then ci = {(˜ei
r)⋆ ⊗ vj}j≤n, r ≤ni is a basis for Ci(K; ρ). Using this basis, one
may deﬁne the torsion of the cocomplex C∗(K; ρ), {ci}, and {hi} a basis in
cohomology. Remarks 2.6, 2.7, and 2.8, also hold true for the torsion deﬁned
from cohomology. By using Lemma 2.4, we have:
Remark 2.9. The complexes C∗(K; ρ) and C∗(K; ρ) are dual. In addition
tor(C∗(K; ρ), {ci}, {(hi)⋆}) = tor(C∗(K; ρ), {ci}, {hi}).
Hence both homology or cohomology can be used to deﬁne the torsio n.
Here Poincar´ e duality and duality between homology and cohomology is not
discussed even if it is used, see [82] for instance.
