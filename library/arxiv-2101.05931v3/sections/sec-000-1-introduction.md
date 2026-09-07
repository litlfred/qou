---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
In their seminal work, Chuang and Rouquier introduced sl2 categoriﬁcations on abelian categories
[16]. Their deﬁnition mirrors the notion of an sl2 representation on a vector space: weight spaces
are replaced by weight categories, Chevalley generators ac ting on them are replaced by Chevalley
functors, and Lie algebra relations are replaced by isomorp hisms of functors. But, crucially, these
isomorphisms are part of the “higher data” of categoriﬁcati on.
The richness of this theory was immediately evident. As a cor ollary of an sl2 categoriﬁcation
on representations of symmetric groups in positive charact eristic, Chuang and Rouquier proved
Broue’s abelian defect conjecture in that case. The essenti al tool allowing them to do this is the
Rickard complex, which is a categorical lifting of the reﬂec tion matrix in SL2, and provides a
derived equivalence between opposite weight categories.
Subsequently, Rouquier and Khovanov-Lauda vastly general ised this theory to quantum sym-
metrisable Kac-Moody algebras Uq(g) [28, 29, 41]. Let /CZ be any ﬁeld. A graded abelian /CZ -linear
category C endowed with a categorical representation of Uq(g) possesses a family of Rickard com-
plexes Θ i, indexed by the simple roots of g, acting on the derived category Db(C).
Henceforth let g be a semisimple simply-laced Lie algebra of ﬁnite type with D ynkin diagram I,
W its Weyl group, and B its Artin braid group. Let C be a categorical representation of Uq(g) as
in the previous paragraph. Cautis and Kamnitzer proved that Rickard complexes satisfy the braid
relations, as conjectured by Rouquier [11]. This deﬁnes an a ction of B on Db(C), and is our main
object of study.
Categorical braid group actions deﬁned via Rickard complex es have many signiﬁcant applications.
For example, in low dimensional topology, the type A link hom ology theories (in particular Kho-
vanov homology) emerge as a byproduct of these types of categ orical braid group actions [9, 10, 31].
In mirror symmetry, the theory of spherical twists plays an i mportant role, and these all arise from
categorical sl2 representations [43].
1
2 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOBI
To describe our ﬁrst theorem, recall that minimal categoriﬁ cations are certain distinguished
categoriﬁcations of simple representations. On these the R ickard complex Θ i is t-exact up to shift
[16, Theorem 6.6]. Notice that this is a result about sl2 categoriﬁcations, and in fact, this is one of
Chuang-Rouquier’s key technical results which they use to p rove the derived equivalence.
We generalise this result to Uq(g), where we show that the composition of Rickard complexes
corresponding to a positive lift of the longest element w0 ∈W is t-exact up to shift on any isotypic
categoriﬁcation. More precisely:
Theorem A. [Theorem 6.4 & Corollary 6.7] Let C be a categorical representation of Uq(g) cate-
gorifying an isotypic representation of type λ, where λ is a dominant integral weight. Let µ be any
weight, and let n be the height of µ −w0(λ). Then the derived equivalence
Θ w0
/BD
µ[n] : Db(Cµ) →Db(Cw0(µ))
is t-exact.
This theorem is the technical heart of the paper. In order to p rove it we introduce a new
combinatorial notion of “marked words” (Section 5). This al lows us to use relations between Θ i
and Chevalley functors established by Cautis and Kamnitzer to deduce the commutation relations
involving Θ w0 (Proposition 5.9). We then use these relations to prove the t heorem by induction on
n.
Our second theorem describes Θ w0 on an arbitrary categorical representation of Uq(g), also
generalising a result of Chuang-Rouquier in the case g = sl2. Indeed, their study of the Rickard
complex on an sl2 categoriﬁcation led them to deﬁne the notion of a “perverse e quivalence” [15].
Consider an equivalence of triangulated categories F : T → T ′ with t-structures [4]. Suppose
further that T (respectively T ′) is ﬁltered by thick triangulated subcategories
0 ⊂ T 0 ⊂ · · · ⊂ T r = T, 0 ⊂ T ′
0 ⊂ · · · ⊂ T ′
r = T ′,
and F is compatible with these ﬁltrations (cf. Section 4.1 for pre cise deﬁnitions). Then, roughly
speaking, F is a perverse equivalence if on each subquotient F : Ti/Ti−1 → T ′
i/T ′
i−1 is t-exact up to
shift.
Since their introduction, perverse equivalences have prov en useful in various contexts (e.g. rep-
resentations of ﬁnite groups [14], geometric representati on theory and mirror symmetry [1], and
algebraic combinatorics [48]). Our second theorem shows th at perverse equivalences are ubiquitous
in categorical representation theory:
Theorem B. [Theorem 6.8] Let C be a categorical representation of Uq(g), and let µ be any weight.
The derived equivalence Θ w0
/BD
µ : Db(Cµ) → Db(Cw0(µ)) is a perverse equivalence with respect to a
Jordan-H¨ older or isotypic ﬁltration of C.
Note that if J ⊆I is a subdiagram, and wJ
0 is corresponding longest element, then this theorem
implies that Θ wJ
0
/BD
µ is a perverse equivalence for any J. We also remark that our argument go
through in the ungraded setting, where C is a categorical representation of g.
Let us explain the ﬁltration arising in Theorem B more precis ely. We apply Rouquier’s Jordan-
H¨ older theory for representations of 2-Kac-Moody algebra s to our setting [41]. We thus obtain a
ﬁltration of C by Serre subcategories,
0 ⊂ C 0 ⊂ · · · ⊂ C r = C,
such that each factor Ci is a subrepresentation, and each subquotient Ci/Ci−1 categoriﬁes either a
simple module (Theorem 3.6) or an isotypic component (Remar k 3.9). Then Θ w0
/BD
µ is a perverse
equivalence with respect to the ﬁltration whose i-th ﬁltered component consists of complexes in
Db(Cµ) with cohomology supported in Ci.
We remark that in the case g = sl2 this gives a more conceptual proof of a result of Chuang-
Rouquier [15, Proposition 8.4]. If C is the tensor product categoriﬁcation of the n-fold tensor
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 3
product of the standard representation of sln, we recover a theorem of the third author [33]. We
explain this in Example 8.3, where we show how to interpret th e ﬁltration on the principal block
of the BGG category O using the Robinson-Schensted correspondence.
In fact, the third author and Bezrukavnikov formulated a pri nciple that suitable categorical braid
group representations should have a “crystal limit” [5, Sec tion 9]. As an application of our results
we can make this precise in the setting of categorical repres entations of Uq(g).
Recall that to an integrable representation V ofUq(g), Kashiwara associated its crystal basis BV
[27], which is closely related to Lusztig’s canonical basis [20]. If V is categoriﬁed by C then there
is a natural identiﬁcation BV = Irr(C), the set of isomorphism classes of simple objects in C up to
shift (cf. Proposition 3.4) .
One of the most important features of the theory is the existe nce of a tensor product, endowing
the category of crystals with a monoidal structure. The comm utator of crystals is controlled by a
group called the cactus group, just as B controls the commutator in the category of representations
ofUq(g) [22]. There is also an internal cactus group action, mirror ing Lusztig’s internal braid group
action on V . Indeed, there is a cactus group C associated to g (or rather to its Dynkin diagram
I), which can be presented by generators cJ indexed by connected subdiagrams J ⊆I (cf. Section
7.1). Then C acts on BV via the so-called Sch¨ utzenberger involutions (cf. Theore m 7.3).
