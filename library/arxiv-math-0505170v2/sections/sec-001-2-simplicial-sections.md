---
doc_id: arxiv-math-0505170v2
doc_title: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS AMNON YEKUTIELI"
section_id: sec-001-2-simplicial-sections
section_title: "Simplicial Sections"
section_number: 2
pages: 8-10
source_pdf: math0505170.pdf
source_sha256: 0846b74f9c7c55cb
doc_brief: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS AMNON YEKUTIELI — W e present an averaging process for sections of a torsor unde r a unipotent group."
---
In this section we show how the averaging process is used to ob tain simplicial
sections of certain bundles.
Suppose H and G are aﬃne group schemes over K, and H acts on G by auto-
morphisms. Namely there is a morphism of schemes H × G → G which for every
K-scheme Y induces a group homomorphism H(Y ) → AutGroups(G(Y )). Then
H × G has a structure of a group scheme, and we denote this group by H ⋉ G; it
is a geometric semi-direct product.
Recall that an aﬃne group scheme G is called pro-unipotent if it is isomorphic
to an inverse limit lim ←i Gi of an inverse system {Gi}i≥0 of (ﬁnite type aﬃne)
unipotent groups. One may assume that each of the morphisms G → Gi → Gi−1
is surjective. Thus Gi ∼= G/N i where Ni is a normal closed subgroup of G.
We will be concerned with the following geometric situation .
Scenario 2.1. Let H ⋉ G be an aﬃne group scheme over K. Assume G is pro-
unipotent, and moreover there exists a sequence {Ni}i≥0 of H-invariant closed
normal subgroups of G such that G ∼= lim←i G/N i and each G/N i is unipotent.
Let π : Z → X be an H ⋉ G -torsor over X which is locally trivial for the Zariski
topology of X. Deﬁne ¯Z := Z/H and let ¯π : ¯Z → X be the projection.
Theorem 2.2. Assume Scenario 2.1. Suppose U ⊂ X is an open set and
σ 0, . . . , σ q : U → ¯Z are sections of ¯π . Then there exists a morphism
σ : ∆ q
K × U → ¯Z
such that the diagram
∆ q
K × U
σ
− − − − →¯Z
p2
↓ ¯π
↓
U − − − − →X
is commutative. The morphism σ depends functorially on U and simplicially on
the sequence (σ 0, . . . , σ q). If q = 0 then σ = σ 0.
Proof. We might as well assume that U = X. Consider the quotient Z/G . Since
G is normal in H ⋉ G it follows that Z/G is a torsor under H × X. Let’s write
π H : Z → ¯Z = Z/H and π G : Z → Z/G for the projections.
Pick an open set V ⊂ X which trivializes π : Z → X. Let’s write Z|V := π−1(V ).
Because π H |V : Z|V → ¯Z|V is a trivial torsor under H × ¯Z|V , we can lift the sections
σ 0, . . . , σ q to sections ˜σ 0, . . . , ˜σ q : V → Z such that π H ◦ ˜σ j = σ j . Furthermore,
since π G : Z → Z/G is H-equivariant and Z/G is a torsor under H × X, it follows
that we can choose ˜σ 0, . . . , ˜σ q such that π G ◦ ˜σ j = τ for some section τ : V → Z/G .
Let F ⊂ Z|V be the ﬁber over τ , i.e. F := V ×Z/G Z via the morphisms π G :
Z → Z/G and τ : V → Z/G . Then F is a torsor under G × V , and ˜σ 0, . . . , ˜σ q ∈
AN A VERAGING PROCESS 9
HomX (V, F ). See diagram below.
Z
π H
/d122/d122/d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117
π
/d15/d15
π G
/d33/d33/d67/d67/d67/d67/d67/d67/d67 F
⊃/d111/d111
¯Z = Z/H
¯π
/d36/d36/d73/d73/d73/d73/d73/d73/d73/d73/d73 Z/G
/d125/d125/d123/d123/d123/d123/d123/d123/d123
X
V
⊃
/d104/d104/d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82 /d82
τ
/d88/d88/d50
/d50
/d50
/d50
/d50
/d50
/d50
˜σ i
/d79/d79/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31
/d31σ i
/d90/d90
For any i deﬁne Fi := F/N i, which is a torsor under ( G/N i)×V . Let α i : F → Fi
be the projection, so α i ◦ ˜σ j ∈ HomX (V, F i). By Theorem 1.11 we get an average
(2.3) ρ i := wavG/N i(α i ◦ ˜σ 0, . . . , α i ◦ ˜σ q) : ∆ q
K × V → Fi.
The functoriality of wav says that the ρ i form an inverse system, and we let
(2.4) ρ := lim
←i
ρ i : ∆ q
K × V → F
and
(2.5) σ := π H ◦ ρ : ∆ q
K × V → ¯Z.
We claim that the morphism σ does not depend on the choice of the section
τ : V → Z/G . Suppose τ′ : V → Z/G is another such section. Let F′ be the
ﬁber over τ′, and let ρ′ : ∆ q
K × V → F′ be the corresponding morphism as in
(2.4). Now τ′ = h ·τ for some morphism h : V → H. Then F′ = h ·F , and
h : F → F′ is a G × V -equivariant morphism of torsors, with respect to the
group-scheme automorphism Ad( h) : G × V → G × V . The new lift of σ j is
˜σ′
j := h ·˜σ j : V → F′. Deﬁne F′
i := F′/N i, and let ρ′
i : ∆ q
K × V → F′
i be the
morphism as in (2.3). Since Ni × V = Ad( h)(Ni × V ), we get a group-scheme
automorphism Ad( h) : ( G/N i) × V → (G/N i) × V , and a ( G/N i) × V -equivariant
morphism of torsors h : Fi → h·F′
i . By functoriality of wav (property 3 in Theorem
1.11) it follows that ρ′
i = h ·ρ i. Therefore ρ′ = h ·ρ , and π H ◦ ρ′ = π H ◦ ρ = σ .
Property 2 in Theorem 1.11 implies that σ depends simplicially on ( σ 0, . . . , σ q).
Finally take an open covering X = ⋃ Vj such that each Vj trivializes π : Z → X,
and let σ j : ∆ q
K × Vj → ¯Z|Vj be the morphism constructed in (2.5). Since no
choices were made we have σ j|Vj∩Vk = σ k|Vj∩Vk for any two indices. Therefore
these sections can be glued to a morphism σ : ∆ q
K × X → ¯Z. The functorial and
simplicial properties of σ are clear from its construction. □
Let X be a K-scheme, and let X = ⋃ m
i=0 U(i) be an open covering, with in-
clusions g(i) : U(i) → X. We denote this covering by U . For any multi-index
i = ( i0, . . . , i q) ∈ ∆ m
q we write Ui := ⋂ q
j=0 U(ij ), and we deﬁne the scheme
Uq := ∐
i∈∆ m
q
Ui. Given α ∈ ∆ q
p and i ∈ ∆ m
q there is an inclusion of open sets
α∗ : Ui → Uα ∗(i). These patch to a morphism of schemes α∗ : Uq → Up, making
{Uq}q∈N into a simplicial scheme. The inclusions g(i) : U(i) → X induce inclusions
gi : Ui → X and morphisms gq : Uq → X; and one has the relations gp ◦ α∗ = gq
for any α ∈ ∆ q
p.
10 AMNON YEKUTIELI
Deﬁnition 2.6. Let π : Z → X be a morphism of K-schemes. A simplicial section
of π based on the covering U is a sequence of morphisms
σ = {σ q : ∆ q
K × Uq → Z}q∈N
satisfying the following conditions.
(i) For any q the diagram
∆ q
K × Uq
σ q
− − − − →Z
p2
↓ π
↓
Uq
gq
− − − − →X
is commutative.
(ii) For any α ∈ ∆ q
p the diagram
∆ p
K × Up
σ p
/d35/d35/d71/d71/d71/d71/d71/d71/d71/d71
∆ p
K × Uq
1×α ∗ /d56/d56/d113/d113/d113/d113/d113/d113/d113/d113
α ∗×1 /d38/d38/d77/d77/d77/d77/d77/d77/d77/d77 Z
∆ q
K × Uq
σ q
/d59/d59/d119/d119/d119/d119/d119/d119/d119/d119
is commutative.
Corollary 2.7. Assume Scenario 2.1. Let U = {U(i)}m
i=0 be an open covering of
X. Suppose that for any i ∈ { 0, . . . , m } we are given some section σ (i) : U(i) → ¯Z
of ¯π . Then there exists a simplicial section
σ = {σ q : ∆ q
K × Uq → ¯Z}q∈N
based on U , such that σ 0|U(i) = σ (i) for all i ∈ {0, . . . , m }.
Proof. For any multi-index i = ( i0, . . . , i q) we have sections σ (i0), . . . , σ (iq ) : Ui →
¯Z. Let σ i : ∆ q
K × Ui → ¯Z be the morphism provided by Theorem 2.2. For ﬁxed
q these patch to a morphism σ q : ∆ q
K × Uq → ¯Z. The functorial and simplicial
properties in Theorem 2.2 imply that this is a simplicial sec tion. □
This result (with H trivial) is illustrated in Figure 1.
