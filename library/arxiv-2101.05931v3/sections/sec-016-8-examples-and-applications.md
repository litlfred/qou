---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-016-8-examples-and-applications
section_title: "Examples and Applications"
section_number: 8
pages: 21-23
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
8.1. Examples. We now examine three examples. The ﬁrst two consider minimal categoriﬁcations
of the adjoint representation, while the third studies the c ategoriﬁcation of the n-fold tensor product
of the standard representation of sln. For ease of presentation, we ignore gradings and consider
non-quantum categorical representations.
Example 8.1. Let’s consider the ﬁrst non-trivial example of Theorem 6.4: the minimal categori-
ﬁcation of the adjoint representation of sl2. We can model this as follows:
/CZ −mod R−mod /CZ −mod
ind res
res ind
where R = /CZ [x]/(x2) [16, Example 5.17]. Here /CZ −mod is the ±2 weight category, and R−mod is
the zero weight category. The arrows describe the E, F functors (we omit the higher structure).
Consider the Rickard complex Θ = Θ /BD
0 : Db(R−mod) → Db(R−mod). For M ∈ R−mod, we
have:
Θ(M ) = R ⊗
/CZ
M →M,
where the diﬀerential is given by the action map, and M is in cohomological degree 0. It’s an
exercise to verify that Θ( M ) is quasi-isomorphic to M ′[1], where M ′ is the twist of M by the
automorphism of R given by a +bx ↦→a −bx. This shows that Θ[ −1] is the t-exact equivalence
M ↦→M ′. □
Example 8.2. More generally, one can consider the minimal categoriﬁcati on of the adjoint repre-
sentation of a simple simply-laced Lie algebra g. This was studied by Khovanov and Huerfano in
[23], who used zigzag algebras to model this category.
For a weight α of the adjoint representation of g, the weight category Cα is taken to be /CZ −mod
as long as α ⁄= 0. However, the zero weight category is more interesting: C0 :=A−mod, where A
is the zigzag algebra associated to the Dynkin diagram I of g (cf. [23] for the precise deﬁnition).
The isomorphism classes of indecomposable projective left A-modules {Pi} and the isomorphism
classes of indecomposable projective right A-modules {Qi} are both indexed by i ∈ I. Tensoring
with these modules deﬁnes functors
Ei : C0 − → Cαi, M ↦→Qi ⊗AM,
Ei : C−αi − → C0, V ↦→Pi ⊗
/CZ
V.
22 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOB I
The functors Fi are deﬁned analogously and are biadjoint to the Ei.
The Rickard complex Θ i
/BD
0 is given by tensoring with the complex
Pi ⊗
/CZ
Qi →A
of (A,A )-bimodules, where the diﬀerential is given by the multiplic ation in A, and A sits in coho-
mological degree zero. These functors are autoequivalence s of the derived category Db(C0).
By Theorem 6.4 Θ w0
/BD
0[−n] is t-exact, where n + 1 is the Coxeter number of g. This auto-
equivalence can be explicitly described as follows: the aut omorphism of the Dynkin diagram τ :I →
I induces an automorphism ψ ofA. Then we claim that Θ w0
/BD
0[−n] is the abelian autoequivalence
of A−mod deﬁned by twisting with ψ. Indeed, since Θ w0
/BD
0[−n] is an abelian autoequivalence, it
is determined up to isomorphism by its action on simple objec ts. Moreover, the action on simple
objects can be read oﬀ from the action of W on the Grothendieck group of A−mod as follows:
[A−mod]Z is isomorphic to the Cartain subalgebra by mapping [ Li] (Li is the simple head of Pi)
to the simple root vector Hi. And on the root vectors we have that w0 ·Hi = −Hτ (i) □
Example 8.3. Let g = sln and consider then-fold tensor power of the standard representation V ⊗n.
Categoriﬁcations of V ⊗n have been well-studied, and a model C for this categorical representation
can be constructed using the BGG category O of g [38, 47]. In this model, the principal block
O0 ⊂ O appears as the zero weight category of C, and the Rickard complexes acting on Db(O0) are
the well-known shuﬄing functors.
By Theorem 6.8 Θ w0
/BD
0 :Db(O0) →Db(O0) is a perverse equivalence with respect to an isotypic
ﬁltration. In fact, this recovers the type A case of a theorem of the third named author [33],
using completely diﬀerent methods (in [33] the perversity of Θ w0 is proved using the theory of
W-algebras). We can interpret the ﬁltration of O0 arising from our perspective concretely using
the Robinson-Schensted correspondence .
Recall that the simple objects in O0 are the irreducible highest weight representations L(w),w ∈
Sn, where L(w) has highest weight wρ −ρ (ρ is the half-sum of positive roots of sln).
We view a partition λ ofn simultaneously as a dominant integral weight for sln, and as an index
for the irreducible Specht module Sλ of the symmetric group Sn. Let SYT( λ) denote the set of
standard Young tableau of shape λ, and let d(λ) = |SYT(λ)|. Recall that d(λ) = dim Sλ.
Choose an ordering of the partitions of n, λ1,...,λ r, so that if λi ≺λj in the dominance order,
then i < j. Note that the dominance order on partitions of n is equivalent to the positive root
ordering on partitions (thought of as weights for sln). By Remark 3.9 there is an isotypic ﬁltration
on C, 0 ⊂ C 1 ⊂ · · · ⊂ C N = C, where Ci/Ci−1 is an isotypic categoriﬁcation of type λi. Then Θ w0
is a perverse equivalence with respect to the ﬁltration O0,i = O0 ∩ Ci and the perversity function
p(i) = ht(λi).
We would like now to deﬁne the categories O0,i more explicitly using the Robinson-Schensted
correspondence, which recall is a bijection [42]:
RS :Sn − →
r⨆
j=1
SYT(λj) × SYT(λj), w ↦→(P (w),Q (w)).
We will use a crystal analogue of classical Schur-Weyl duali ty. This is given by a crystal isomor-
phism:
B(̟1)⊗n − →
r⨆
j=1
B(λj ) × SYT(λj). (8.4)
Now, recall that for a partition λ ofn, the underlying set of the crystal B(λ) can be chosen to be
the set of semistandard Young tableaux of shape λ with entries 1,...,n , and the weight zero subset
of B(λ) is precisely SYT( λ). The essential point is that the isomorphism (8.4) can be ch osen so
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 23
that it restricts to the map RS on the elements of weight zero ([44, Theorem 3.5]). (Note tha t the
elements of weight zero in B(̟1)⊗n are naturally identiﬁed with permutations of 1 ,...,n .)
This shows that as an element of the crystal B(̟1)⊗n, [L(w)] is in a connected component whose
highest weight is the shape of Q(w) (or equivalently P (w)). Therefore, following Remark 3.10, we
can construct the isotypic ﬁltration be deﬁning O0,i to be the Serre subcategory of O0 generated
byL(w) such that the shape of Q(w) is among λ1,...,λ i.
□
