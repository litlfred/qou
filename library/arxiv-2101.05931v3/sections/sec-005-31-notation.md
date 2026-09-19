---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-005-31-notation
section_title: "Notation"
section_number: 3.1
pages: 5-7
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
of [36], ti = t′′
i,−1. (Note that the formula given in [36] is more complicated. Th is simpler form
was initially observed in [16] in the non-quantum setting, a nd generalised in [12] to the quantum
setting.). The assignment θi ↦→ti deﬁnes an action of B onV , and so we can unambiguously write
tw for any w ∈W .
3. Categorical representations of Uq(g)
3.1. Notation. Fix a ﬁeld /CZ of any characteristic. In this paper we will be concerned mos tly with
abelian /CZ -linear categories C. We will assume throughout that each block of C is a ﬁnite abelian
category [39, Deﬁnition 1.8.6].
Recall that a category A is graded if it is equipped with an auto-equivalence ⟨1⟩ : A → A called
the “shift functor”. We let ⟨ℓ⟩ be the auto-equivalence obtained by applying the shift func tor ℓ
times. We denote by Irr(A) the set of equivalence classes of simple objects of A up to shift.
A functor F : A → A ′ between graded categories is graded if it commutes with the s hift functors.
We denote by [ A]Z the Grothendieck group of an abelian category A. If A is graded we denote
by [ A]Z[q,q −1] the quotient of [ A]Z ⊗Z Z[q,q −1] by the additional relation q[M ] = [ M ⟨−1⟩]. This
quotient is naturally a Z[q,q −1]-module. Set
[A]C = [A]Z ⊗Z C,
[A]C(q) = [A]Z[q,q −1] ⊗Z[q,q −1] C(q).
6 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOBI
For a /CZ -algebra A, we let A−mod be the category of ﬁnitely generated A-modules, and if A
is Z-graded, we let A−modZ be the category of ﬁnitely generated Z-graded modules. These are
naturally /CZ -linear abelian categories.
3.2. Deﬁnition. In this section we introduce our main objects of study: repre sentations of the
2-quantum group on abelian categories, which we refer to as “ categorical representations” of Uq(g).
This deﬁnition of the categoriﬁed quantum groups and their c ategorical actions is originally due to
Rouquier and Khovanov-Lauda [28, 29, 41].
In the literature, there are a number of slightly diﬀerent-lo oking examples of 2-representations,
depending not just on whether or not one is working with the Kh ovanov-Lauda or Rouquier 2-
categories, but also depending on whether or not one is inter ested in categoriﬁcations of repre-
sentations of Uq(g) or of U (g). At the categorical level, the diﬀerence between Uq(g) or of U (g)
arises from grading considerations; in categoriﬁcations o f representations of Uq(g), one works with
categories enriched in graded vector spaces, whereas in cat egoriﬁcations of representations of U (g)
no such grading is needed.
Fortunately, the diﬀerent notions of categorical represent ations - and in particular relationships
between the Rouquier and Khovanov-Lauda frameworks in both graded and ungraded settings, have
been brought in line by work of Cautis-Lauda, who proved that in the graded setting, integrable
2-representations of the Rouquier 2-category induce 2-rep resentations of the Khovanov-Lauda 2-
category [13], and by work of Brundan [6], who proved that the underlying ungraded 2-categories
of Rouquier and Khovanov-Lauda are equivalent.
The important point for us is that all our theorems, includin g our main results (Theorem 6.4
and Theorem 6.8), remain true in any 2-representation of the Khovanov-Lauda-Rouqier 2-category,
in either the graded or ungraded setting. Since the compatib ility of the internal grading with the
braid group is of some independent combinatorial interest, we elect to keep track of the gradings
in the rest of the paper, and leave it to the reader to verify th at the arguments go through while
ignoring the gradings and working in the setup of, e.g. Brund an [6]. To that end, we have chosen
to follow the notation and conventions of Cautis-Lauda belo w.
A categorical representation of Uq(g) consists of the following data:
• A family of graded abelian /CZ -linear categories Cµ indexed by µ ∈ X. We refer to each Cµ
as a weight category .
• Exact graded functors Ei
/BD
µ : Cµ → C µ+αi and Fi
/BD
µ : Cµ → C µ−αi, for i ∈I and µ ∈X. We
refer to Ei, Fi as Chevalley functors .
• A collection of natural transformations between these func tors. We won’t be using directly
these natural transformations in this work, so refer the rea der to [13, Deﬁnition 1.1] for
their deﬁnition.
This data is subject to the conditions spelled out in items (1 )-(5) of [13, Deﬁnition 1.1]. We only
record those that are relevant for us:
(1) The functors Ei
/BD
µ and Fi
/BD
µ are biadjoint up to a speciﬁed degree shift (see (3.1) below) .
(2) The powers of Ei carry an action of the KLR algebra associated to Q, where Q denotes a
choice of units (tij)i⁄=j∈I in /CZ
×. These units satisfy some restrictions which are not releva nt
for us.
(3) We have the following isomorphisms:
FiEi
/BD
µ ∼= EiFi
/BD
µ ⊕[−⟨hi,µ⟩]
/BD
µ, if ⟨hi,µ ⟩ ≤ 0,
EiFi
/BD
µ ∼= FiEi
/BD
µ ⊕[⟨hi,µ⟩]
/BD
µ, if ⟨hi,µ ⟩ ≥ 0,
EiFj
/BD
µ ∼= FjEi
/BD
µ.
This notation is explained as follows: for a Laurent polynom ialf = ∑ faqa, ⊕fA is a direct
sum over a ∈ Z of fa copies of A⟨a⟩, and [n] := qn−1 +qn−3 + · · · +q1−n.
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 7
Usually we just say that C = ⨁
µ Cµ is a categorical representation of Uq(g) (the remaining data
is implicit). Given an integrable Uq(g)-module V , we say that C is a categoriﬁcation of V if C is a
categorical representation of Uq(g) such that [ C]C(q) ∼=V as Uq(g)-modules.
An additive categoriﬁcation is a categorical representation on a graded additive /CZ -linear
category V satisfying the same conditions as above, except the Chevall ey functors are of course
only required to be additive. We let V i be the idempotent completion of V.
Given an abelian category C, we consider the additive category C−proj deﬁned as the full sub-
category of projective objects in C. Note that if C is a categorical representation of Uq(g), then
C−proj naturally inherits the structure of an additive catego riﬁcation.
As a consequence of this deﬁnition, and in particular condit ion (2), there exist divided power
functors E(r)
i
/BD
λ ⊂ Er
i
/BD
λ, F(r)
i
/BD
λ ⊂ Fr
i
/BD
λ which categorify the usual divided powers on the level of
the quantum group. Again, we refer the reader to [13] and refe rences therein for further details.
We note that their adjoints are related as follows:
(E(r)
i
/BD
λ)R ∼= F(r)
i
/BD
λ+rαi⟨r(λi +r)⟩, (3.1)
(E(r)
i
/BD
λ)L ∼= F(r)
i
/BD
λ+rαi⟨−r(λi +r)⟩. (3.2)
