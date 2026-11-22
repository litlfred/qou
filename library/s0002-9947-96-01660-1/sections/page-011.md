---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: page-011
section_title: "Page 11"
section_number: null
pages: 11-11
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
toc_source: undetermined
doc_brief: "Invariants of piecewise-linear 3-manifolds — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state sum model on a tri- angulation."
---
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS
4007
b
a
c
Figure 4
Note that, given f and a labelling of M, there is a unique compatible labelling
of N.
Now the properties of the state space of a triangle under combinatorial isomor-
phisms are described. The combinatorial isomorphisms are just permutations in
S3. For the standard triangle T(a,ˆb, c), labelled by ∂0T 7→a, ∂1T 7→ˆb, ∂2T 7→c,
the labelling is permuted by (a, b, c) 7→σ+(a, b, c) for an even permutation σ+,
and (a, b, c) 7→σ−(ˆa,ˆb, ˆc) for an odd permutation σ−. For this reason, it is more
convenient to use the notation V (a, b, c)=H(a,ˆb, c) for the state space of a labelled
triangle when the symmetry properties are considered.
There is a canonical map V (a, b, c) →V (b, c, a), i.e.,
Hom(ˆb, a ⊗c) →Hom(ˆc, b ⊗a),
deﬁned by mapping f : ˆb →a ⊗c to the following composite:
ˆc
=
−→e ⊗ˆc
ϵ(b)⊗1
−−−−→b ⊗ˆb ⊗ˆc
1⊗f⊗1
−−−−→b ⊗a ⊗c ⊗ˆc
1⊗1⊗ˆϵ(c)
−−−−−−→b ⊗a ⊗e
=
−→b ⊗a.
This corresponds to the graph in Figure 4.
There is also a canonical pairing V (a, b, c) × V (ˆc,ˆb, ˆa) →F, i.e.,
Hom(ˆb, a ⊗c) × Hom(b, ˆc ⊗ˆa) →F.
Let f : ˆb →a ⊗c and g: b →ˆc ⊗ˆa. Then the pairing is deﬁned by
⟨f, g⟩= trL(fˆg).
Equivalently, it is determined by the closed tangle in Figure 5.
Deﬁnition 3.5. For every ordered triple, (a, b, c), of elements of I and every even
permutation σ+ ∈S3, there is an isomorphism
θ(σ+): V (a, b, c) →V σ+(a, b, c).
For (a, b, c) 7→(b, c, a), this is the canonical map just deﬁned. Repeating this gives
the isomorphism for (a, b, c) 7→(c, a, b). The identity is associated to the identity.
For every ordered triple, (a, b, c), of elements of I, and every odd permutation
σ−∈S3, there is a non-degenerate pairing, ⟨−, −⟩σ−,
V (a, b, c) ⊗V σ−(ˆa,ˆb, ˆc) →F.
For σ−the odd permutation (a, b, c) 7→(c, b, a), this is the pairing deﬁned above.
The pairings for the other two odd permutations can be deﬁned by the formula
⟨v1, v2⟩σ−= ⟨v1, θ(σ+)v2⟩σ−σ+.
