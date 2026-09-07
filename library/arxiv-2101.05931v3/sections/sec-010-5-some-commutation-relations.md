---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-010-5-some-commutation-relations
section_title: "Some commutation relations"
section_number: 5
pages: 12-13
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
We ﬁx throughout a categorical representation C of Uq(g). Recall that w0 ∈ W is the longest
word, and let w0 =si1si2 · · ·sir be a reduced expression. We consider the composition of Rick ard
complexes which categoriﬁes the positive lift in B of w0:
Θ w0
/BD
λ = Θ i1 · · ·Θ ir
/BD
µ :Db(Cλ) →Db(Cw0(λ)).
In preparation for the proofs our main results in the next sec tion, we prove some commutation
relations between Θ w0 and the Chevalley functors.
5.1. Cautis’ relations. To begin, we recall some relations of Cautis (building on wor k with Kam-
nitzer [11]). Although they are stated only for type A, their proofs apply to any simply-laced Lie
algebra.
Lemma 5.1 (Lemma 4.6, [8]) . For any i ∈I,λ ∈X we have the following relations:
Θ iEi
/BD
λ ∼
= FiΘ i
/BD
λ[1]⟨λi⟩,
Θ iFi
/BD
λ ∼
= EiΘ i
/BD
λ[1]⟨−λi⟩.
Remark 5.2. The careful reader will notice that actually Cautis proves L emma 5.1 under certain
conditions on λ. For instance, the ﬁrst relation is only proven in the case wh en λi ≤ 0. To deduce
the general case from this, one can rewrite the relation as EiΘ −1
i ∼
= Θ −1
i Fi[1]⟨λi⟩. Now recall that
there is an anti-automorphism rσ on the sl2 2-category which on objects maps n ↦→ −n [30, Section
5.6]. This anti-automorphism maps Θ −1
i to Θ i, and hence applying it to the relation above we
deduce the desired relation in the case when λi ≥ 0.
Alternatively, in a recent preprint Vera proves a version of the relation between the Rickard
complex and Chevalley functors in the (bounded homotopy cat egory of the) sl2 2-category, which
of course implies it also in any 2-representation [49].
Next we recall the categorical analogues of commutators [ Ei,E j] acting on representations of
Uq(g). Given nodes i,j ∈I such that (i,j ) = −1 and λ ∈X, deﬁne complexes of functors
Eij
/BD
λ :Db(Cλ) →Db(Cλ+αi+αj ), Eij
/BD
λ = EiEj
/BD
λ⟨−1⟩ → EjEi
/BD
λ,
Fij
/BD
λ :Db(Cλ) →Db(Cλ−αi−αj ), Fij
/BD
λ = FiFj
/BD
λ → FjFi
/BD
λ⟨1⟩.
In both instances the diﬀerential is given by the element Tij arising from the KLR algebra, and the
left term of the complex is in homological degree zero [8].
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 13
Lemma 5.3 (Lemma 5.2, [8]) . Leti,j ∈I,λ ∈X and suppose (i,j ) = −1. We have the following
isomorphisms:
EijΘ i
/BD
λ ∼
=
{
Θ iEj if λi> 0,
Θ iEj[1]⟨−1⟩ if λi ≤ 0
FijΘ i
/BD
λ ∼
=
{
Θ iFj if λi ≥ 0,
Θ iFj[−1]⟨1⟩ if λi < 0
/BD
λΘ jEij ∼
=
{
EiΘ j if λj < 0,
EiΘ j[1]⟨−1⟩ if λj ≥ 0
/BD
λΘ jFij ∼
=
{
FiΘ j if λj ≤ 0,
FiΘ j[−1]⟨1⟩ if λj > 0
