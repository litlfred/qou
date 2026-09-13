---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-007-35-the-categorical-braid-group-action
section_title: "The categorical braid group action"
section_number: 3.5
pages: 9-10
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
and i ∈I. We deﬁne a complex of functors Θ i
/BD
µ, supported in nonpositive cohomological degrees,
where for r ≥ 0 the −r component is
(Θ i
/BD
µ)−r =
{
E(−µi+r)
i F(r)
i
/BD
µ⟨−s⟩ if µi ≤ 0,
F(µi+r)
i E(r)
i
/BD
µ⟨−r⟩ if µi ≥ 0.
The diﬀerential dr : (Θ i
/BD
µ)−r → (Θ i
/BD
µ)−r+1 is deﬁned using the counits of the bi-adjunctions
relating Ei and Fi (see [8, Section 4] for details). This produces a functor Θ i
/BD
µ : Db(Cµ) →
Db(Csi(µ)), which following Chuang and Rouquier we call the Rickard complex.
It’s straightforward to verify that the Rickard complex Θ i
/BD
µ categoriﬁes Lusztig’s braid group
operators ti1µ ([8, Section 2]). On the level of categories we have the follo wing two theorems of
Chuang-Rouquier and Cautis-Kamnitzer, which are the funda mental results about Rickard com-
plexes. Note that the latter theorem was conjectured in [41, Conjecture 5.19].
Theorem 3.11. [16, Theorem 6.4] For any µ,i , Θ i
/BD
µ : Db(Cµ) →Db(Csi(µ)) is an equivalence of
triangulated categories.
10 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOB I
Theorem 3.12. [11, Theorem 6.3] The Rickard complexes satisfy the braid relations:
Θ iΘ j
/BD
µ ∼= Θ jΘ i
/BD
µ if (i,j ) = 0,
Θ iΘ jΘ i
/BD
µ ∼= Θ jΘ iΘ j
/BD
µ if (i,j ) = −1,
thereby deﬁning a weak action of B on Db(C).
This action is “weak” since we don’t make any claim on the cano nicity of the functorial iso-
morphisms. Nevertheless, for w ∈W we deﬁne Θ w
/BD
µ := Θ i1 ◦ · · · ◦ Θ iℓ
/BD
µ, where w =si1 · · ·siℓ is
a reduced expression. Thus Θ w
/BD
µ is deﬁned up to isomorphism, but not canonical isomorphism.
Luckily, everything we do in this paper only requires Θ w
/BD
µ to be deﬁned up to isomorphism.
As a consequence of their proof of Theorem 3.11, Chuang and Ro uquier show that the inverse
of Θ i
/BD
µ is its right adjoint. We denote this functor by Θ ′
i
/BD
µ : Db(Cµ) → Db(Csi(µ)), so that
Θ iΘ ′
i
/BD
µ ∼= Θ ′
iΘ i
/BD
µ ∼=
/BD
µ. As a complex of functors, Θ ′
i
/BD
µ is supported in nonnegative cohomological
degrees, where for s ≥ 0 the s component is
(Θ ′
i
/BD
µ)s =
{
E(s)
i F(µi+s)
i
/BD
µ⟨s(−2µi − 2s + 1)⟩ if µi ≥ 0,
F(s)
i E(−µi+s)
i
/BD
µ⟨s(−2µi + 2s + 1)⟩ if µi ≤ 0.
