---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETR Y"
section_id: sec-002-21-algebraic-geometry-over-algebraic-systems
section_title: "Algebraic geometry over algebraic systems"
section_number: 2.1
pages: 5-13
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
school. The section 2.1 is devoted to this approach. In conne ction with this approach,
Plotkin’s problem about the automorphism of semigroups of endomorphisms of free algebra
and categories (and also of groups of automorphisms) arose. The section 2.2 is devoted
to Plotkin’s problem of endomorphisms and automorphisms. T he problem of describing
automorphisms for groups of polynomial symplectomorphism s and automorphisms of the
Weyl algebra is extremely important, both from the point of v iew of mathematical physics
and from the point of view of the Jacobian conjecture. Sectio n 2.3 is dedicated to this
problem.
2.1. Algebraic geometry over algebraic systems.
2.1.1. Three versions of logical rigidity. Questions we are going to illuminate in this
section are concentrated around the interaction between al gebra, logic, model theory and
geometry.
The main question behind further considerations is as follo ws. Suppose we have two
algebras equipped with a sort of logical description.
Problem 2.1. When the coincidence of logical descriptions provides an is omorphism
between algebras in question?
With this aim we consider diﬀerent kinds of logical equivale nces between algebras.
Some of the notions we are dealing with are not formally deﬁne d in the text. For precise
deﬁnitions and references use [23], [67], [79], [81], [86], [90], [91].
6 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKIN , YU, AND ZHANG
2.1.2. Between syntax and semantics. By syntax we will mean a language intended
to describe a certain subject area. In syntax we ask question s, express hypotheses and
formulate the results. In syntax we also build chains of form al consequences. For our
goals we use ﬁrst-order languages or their fragments. Each l anguage is based on some
ﬁnite set of variables that serve as the alphabet, and a numbe r of rules that allow us to
build words based on this alphabet. In general, its signatur e includes Boolean operations,
quantiﬁers, constants, and also functional symbols and pre dicate symbols. The latter ones
are included in atomic formulas and, in fact, determine the f ace of a particular language.
Atomic formulas will be called words. Words together with lo gical operations between
them will be called formulas.
By semantics we understand the world of models, or in other wo rds, the subject area
of our knowledge. This world exists by itself, and develops a ccording to its laws.
Fix a variety of algebras Θ. Let W (X), X = {x1, . . . , x n} denote the ﬁnitely generated
free algebra in Θ. By equations in Θ we mean expressions of the form w ≡ w′, where
w, w′ are words in W (X) for some X. This is our ﬁrst syntactic object. Next, let
˜Φ = (Φ( X), X ∈ Γ) be the multi-sorted Halmos algebra of ﬁrst order logical f ormulas
based on atoms w ≡ w′, w, w′ in W (X), see [86], [87], [91]. There is a special procedure
to construct such an algebraic object which plays the same ro le with respect to First
Order Logic as Boolean algebras do with respect to Propositi onal calculus. One can view
elements of ˜Φ = (Φ( X), X ∈ Γ) just as ﬁrst order formulas over w ≡ w′.
Let X = {x1, . . . , x n} and let H be an algebra in the variety Θ. We have an aﬃne
space H X of points µ : X → H. For every µ we have also the n-tuple ( a1, . . . , a n) = ¯a
with ai = µ (xi). For the given Θ we have the homomorphism
µ : W (X) → H
and, hence, the aﬃne space is viewed as the set of homomorphis ms
Hom(W (X), H ).
The classical kernel Ker( µ ) corresponds to each point µ : W (X) → H. This is exactly the
set of equations for which the point µ is a solution. Every point µ has also the logical kernel
LKer(µ ), see [90], [82], [87]. Logical kernel LKer( µ ) consists of all formulas u ∈ Φ( X) valid
on the point µ . This is always an ultraﬁlter in Φ( X).
So we deﬁne syntactic and semantic areas where logic and geom etry operate, respec-
tively. Connect them by a sort of Galois correspondence.
Let T be a system of equations in W (X). The set A in the aﬃne space Hom( W (X), H )
consisting of all solutions of the system T corresponds to T . Sets of such kind are called
algebraic sets. Vice versa, given a set A of points in the aﬃne space consider all equations
T having A as the set of solutions. Sets T of such kind are called closed congruences over
W .
We can do the same correspondence with respect to arbitrary s ets of formulas. Given a
set T of formulas in algebra of formulas (set of elements) Φ( X), consider the set A in the
aﬃne space, such that every point of A satisﬁes every formula of Φ. Sets of such kind are
called deﬁnable sets . Points of A are called solutions of the set of formulas T . Conversely,
given a set A of points in the aﬃne space consider all formulas (elements) T having A as
the set of solutions. Sets T of such kind are closed ﬁlters in Φ( X).
Let us formalize the Galois correspondence described above .
2.1.3. Galois correspondence in the Logical Geometry. Let us start with a partic-
ular case when the set of formulas T in Φ( X) is a set of equations of the form w = w′,
w, w ′ ∈ W (X), X ∈ Γ.
We set
A = T ′
H = {µ : W (X) → H | T ⊂ Ker (µ )}.
Here A is an algebraic set in Hom( W (X), H ), determined by the set T .
SOME LOGICAL ASPECTS 7
Let, further, A be a subset in Hom( W (X), H ). We set
T = A′
H =
⋂
µ ∈A
Ker (µ ).
Congruences T of such kind are called H-closed in W (X). We have also Galois-closures
T ′′
H and A′′
H.
Let us pass to the general case of logical geometry. Let now T be a set of arbitrary
formulas in Φ( X). We set
A = T L
H = {µ : W (X) → H | T ⊂ LKer(µ )}.
We have also
A =
⋂
u∈T
ValX
H (u).
Here A is called a deﬁnable set in Hom( W (X), H ), determined by the set T . We use the
term ”deﬁnable” for A of such kind, meaning that A is deﬁned by some set of formulas T .
For the set of points A in Hom( W (X), H ) we set
T = AL
H =
⋂
µ ∈A
LKer(µ ).
We have also
T = AL
H = {u ∈ Φ( X) | A ⊂ ValX
H (u)}.
Here T is a Boolean ﬁlter in Φ( X) determined by the set of points A. Filters of such
kind are Galois-closed and we can deﬁne the Galois-closures of arbitrary sets T in Φ( X)
and A in Hom( W (X), H ) as T LL and ALL.
Remark 2.2. The principal role in all considerations plays the value hom omorphism
Val : ˜Φ → HalΘ , where HalΘ is a special Halmos algebra associated with the vector space
Hom(W (X), H ), see [87], [91]. Its meaning is to make the procedure of veriﬁcation whether
a point satisﬁes the formula a homomorphism.
2.1.4. Logical similarities of algebras. Now we are in a position to introduce several
logical equivalences between algebras. Since the Galois co rrespondence yields the duality
between syntactic and semantic objects, every deﬁnition of equivalence between algebras
formulated in terms of formulas, that is logically, has its s emantical counterpart, that is a
geometric formulation, and vice versa.
All algebraic sets constitute a category with special ratio nal maps as morphisms [91].
The same is true with respect to deﬁnable sets [91]. So, we can formulate logical closeness
of algebras geometrically.
Deﬁnition 2.3. We call algebras H1 and H2 geometrically similar if the categories of
algebraic sets AGΘ (H1) and AGΘ (H2) are isomorphic.
By Galois duality between closed congruences and algebraic sets, H1 and H2 are ge-
ometrically similar if and only if the corresponding catego ries CΘ (H1) and CΘ (H2) of
closed congruences over W (X) are isomorphic.
Deﬁnition 2.4. We call algebras H1 and H2 logically similar, if the categories of deﬁnable
sets LGΘ (H1) and LGΘ (H2) are isomorphic.
By Galois duality between closed ﬁlters in Φ( X) and deﬁnable sets, H1 and H2 are
logically similar if and only if the corresponding categori es FΘ (H1) and FΘ (H2) of closed
ﬁlters in F (X) are isomorphic.
We will be looking for conditions A on algebras H1 and H2 that provide geometrical
or logical similarity.
Let two algebras H1 and H2 subject to some condition A be given. Here A is any
condition of logical or, dually, geometrical character, fo rmulated in terms of closed sets of
formulas or deﬁnable sets.
8 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKIN , YU, AND ZHANG
Deﬁnition 2.5. We call the condition A rigid (or A-rigid) if two algebras H1 and H2
subject to A are isomorphic.
2.1.5. Geometric equivalence of algebras.
Deﬁnition 2.6. Algebras H1 and H2 are called AG-equivalent, if for every X and every
system of equations T holds T ′′
H1 = T ′′
H2 .
AG-equivalent algebras are called also geometrically equivalent algebras, see [91], [90],
[82]. The closure T ′′
H is called, sometimes, a radical of T with respect to H. This is a normal
subgroup and an ideal in cases of groups and associative (Lie ) algebras, respectively.
The meaning of Deﬁnition 2.6 is as follows. Two algebras H1 and H2 are AG-equivalent
if they have the same solution sets with respect to any system of equations T . We have
the following criterion, see [91].
Proposition 2.7. If algeras H1 and H2 are AG-equivalent, then they are AG-similar.
So, geometric equivalence of algebras provides their geome trical similarity. The next
statement describes geometrically equivalent algebras. A ssume, for simplicity, that our
algebras are geometrically noetherian (see [82], [67]), wh ich means that every system of
equations T is equivalent to a ﬁnite subsystem T ′ of T . Then, see [88],
Proposition 2.8. Geometrically noetherian algebras H1 and H2 are AG-equivalent if and
only if they generate the same quasi-variety.
Hence, two algebras H1 and H2 are AG-equivalent if and only if they have the same
quasi-identities. If we drop the condition of geometrical n oetherianity, then algebras H1
and H2 are AG-equivalent if they have the same inﬁnitary quasi-ide ntities.
Let Θ be the variety of all groups. Now the question of AG-rigidity for groups reduces
to the question when two groups generating one and the same qu asi-variety are isomorphic.
Of course the condition on groups to have one and the same quas i-identities is very weak
and the rigidity of such kind can happen if both groups belong to a very narrow class of
groups. In general, such a condition does not seem sensible.
Geometrical equivalence of algebras gives a suﬃcient condi tion for AG-similarity. It
turns out that for some varieties Θ this condition is also suﬃ cient.
Theorem 2.9. Let V ar(H1) = V ar(H2) = Θ . Let Θ be one of the following varieties
• Θ = Grp, the variety of groups,
• Θ = Jord , the variety of Jordan algebras,
• Θ = Semi, the variety of semigroups,
• Θ = Inv , the variety of inverse semigroups,
• Θ = Nd, the variety of nilpotent groups of class d.
Categories AGΘ (H1) and AGΘ (H2) are isomorphic if and only if the algebras H1 and H2
are geometrically equivalent (see [19]) [64], [108], [107]).
Let Θ 0 be the category of all free algebras of the variety Θ. The foll owing proposition
is the main tool in the proof of Theorem 2.9.
Proposition 2.10 ([84]). If for the variety Θ every automorphism of the category Θ 0
is inner, then two algebras H1 and H2 are geometrically similar if and only if they are
geometrically equivalent.
So, studying automorphisms of Θ 0 plays a crucial role. The latter problem is treated by
means of Reduction Theorem (see [86], [43], [59], [93]). Thi s theorem reduces investigation
of automorphisms of the whole category Θ 0 of free in Θ algebras to studying the group
Aut(End(W (X))) associated with a single object W (X) in Θ 0. Here, W (X) is a ﬁnitely
generated free in Θ hopﬁan algebra, which generates the whol e variety Θ. In fact, if all
automorphisms of the endomorphism semigroup of a free algeb ra W (X) are close to being
SOME LOGICAL ASPECTS 9
inner, then all automorphisms of Θ 0 possess the same property. More precisely, denote by
Inn(End(W (X))) the group of inner automorphisms of Aut(End( W (X))). Then the group
of outer automorphisms Aut(End( W (X)))/Inn (End(W (X))) measures, in some sense, the
diﬀerence between the notions of geometric similarity and g eometric equivalence.
2.1.6. Elementary equivalence of algebras. As we saw in the previous section AG-
equivalence of algebraic sets reduces to coincidence of qua si-identities of algebras. This is
a weak invariant, a small part of elementary theory, and, of c ourse, coincidence of quasi-
identities does not imply isomorphism of algebras. Hence AG-equivalence does not make
much sense from the point of view of rigidity. Now we recall a m ore powerful logical
invariant of algebras.
Given algebra H, its elementary theory T h(H) is the set of all sentences (closed formu-
las) valid on H. We modify a bit this deﬁnition and adjust it to the Galois cor respondence.
Fix X = {x1, . . . , x n}. Deﬁne X-elementary theory T hX (H) to be the set of all formulas
u ∈ Φ( X) valid in every point of the aﬃne space Hom( W (X), H ). In general we have a
multi-sorted representation of the elementary theory
T h(H) = ( T hX (H), X ∈ Γ) ,
where Γ is a certain system of sets.
Deﬁnition 2.11. Two algebras H1 and H2 are said to be elementarily equivalent if their
elementary theories coincide.
Remark 2.12. From the geometric point of view this deﬁnition does not make diﬀer-
ence between diﬀerent points of the aﬃne space. Given algebra s H1 and H2, we col-
lect all together formulas valid in every point of the aﬃne sp aces Hom(W (X), H 1) and
Hom(W (X), H 2), and declare algebras H1 and H2 elementarily equivalent if these sets
coincide.
Importance of the elementary classiﬁcation of algebraic st ructures goes back to the
famous works of A.Tarski and A.Malcev. The main problem is to ﬁgure out what are the
algebras elementarily equivalent to a given one. Very often we ﬁx a class of algebras C
and ask what are the algebras elementarily equivalent to a gi ven algebra inside the class
C. So, the rigidity question with respect to elementary equiv alence looks as follows.
Problem 2.13. Let a class of algebras C and an algebra H ∈ C be given. Suppose that
the elementary theories of algebras H and A ∈ C coincide. Are they elementarily rigid,
that is, are H and A isomorphic?
Remark 2.14. What we call elementary rigidity has diﬀerent names. This not ion ap-
peared in the papers by A. Nies [69] under the name of quasi deﬁnability of groups. The
corresponding name used in [1] is ﬁrst order rigidity. For some reasons which will be clear
in the next section we use another term.
In other words we ask for which algebras their logical charac terization by means of
the elementary theory is strong enough and deﬁne the algebra in the unique, up to an
isomorphism, way?
We restrict our attention to the case of groups, and, moreove r, assume quite often that
our groups are ﬁnitely generated. Elementary rigidity of gr oups occurs not very often.
Usually various extra conditions are needed. Here is the inc omplete list of some known
cases:
Theorem 2.15. We will consider the following cases
• Finitely generated abelian groups are elementarily rigid i n the class of such groups,
see [104], [17].
10 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
• Finitely generated torsion-free class 2 nilpotent groups a re elementarily rigid in
the class of ﬁnitely generated groups, see [24], [72] (this is wrong for such groups
of class 3 and for torsion groups of class 2, see [114] ).
• If two ﬁnitely generated free nilpotent groups are elementa rily equivalent, then they
are isomorphic, that is a free ﬁnitely generated nilpotent g roup is elementarily rigid
in the class of such groups, see [97], [56].
• If two ﬁnitely generated free solvable groups are elementar ily equivalent, then they
are isomorphic, that is a free ﬁnitely generated solvable gr oup is elementarily rigid
in the class of such groups, see [97], [56].
• Baumslag-Solitar group BS( 1, n ) is elementarily rigid in the class of countable
groups, see [13]. General Baumslag-Solitar groups BS( m, n ) are elementarily rigid
in the class of all Baumslag-Solitar groups, see [13].
• Right-angled Coxeter group is elementarily rigid in the cla ss of all right-angled
Coxeter groups, see [12].
• A good rigidity example is provided by proﬁnite groups: if tw o ﬁnitely generated
proﬁnite groups are elementarily equivalent (as abstract g roups), then they are
isomorphic [31].
Consider, separately, examples of elementary rigidity for linear groups. First of all, a
group which is elementarily equivalent to a ﬁnitely generat ed linear group is a residually
ﬁnite linear group [57]. The rigidity cases are collected in the following theorem.
Theorem 2.16. We will consider the following cases.
• Historically, the ﬁrst result was obtained by Malcev [58]. If two linear groups
GLn(K) and GLm(F ), where K and F are ﬁelds, are elementarily equivalent,
then n = m and the ﬁelds K and F are elementarily equivalent.
• This result was generalized to the wide class of Chevalley gr oups. Let G1 =
Gπ (Φ , R ) and G2 = Gµ (Ψ , S ) be two elementarily equivalent Chevalley groups.
Here Φ , Ψ denote the root systems of rank ≥ 1, R and S are local rings, and π , µ
are weight lattices. Then root systems and weight lattices o f G1 and G2 coincide,
while the rings are elementarily equivalent. In other words Chevalley groups over
local rings are elementarily rigid in the class of such group s modulo rigidity of the
ground rings [11].
• Let Gπ (Φ , K ) be a simple Chevalley group over the algebraically closed ﬁe ld K.
Then Gπ (Φ , K ) is elementarily rigid in the class of all groups (cardinalit y is ﬁxed).
This result can be deduced from [115]. In fact, this is true for a much wider
class of algebraic groups over algebraically closed ﬁelds a nd, modulo elementary
equivalence of ﬁelds, over arbitrary ﬁelds [115].
• Any irreducible non-uniform higher-rank characteristic z ero arithmetic lattice is
elementarily rigid in the class of all groups, see [1]. In particular, SLn(Z), n > 2
is elementarily rigid.
• Recently, the results of [1] have been extended to a much more wide class of lattices,
see [2].
• Let O be the ring of integers of a number ﬁeld, and let n /greaterorequalslant3. Then every group G
which is elementarily equivalent to SLn(O) is isomorphic to SLn(R), where the
rings O and R are elementarily equivalent. In other words SLn(O) is elementarily
rigid in the class of all groups modulo elementary equivalen ce of rings. The similar
results are valid with respect to GLn(O) and to the triangular group Tn(O) [102] .
These results intersect in part with the previous items, sin ce the ring R = Z is
elementarily rigid in the class of all ﬁnitely generated rin gs [69], and thus SLn(Z)
is elementarily rigid in the class of all ﬁnitely generated g roups.
• For the case of arbitrary Chevalley groups the results simil ar to above cited are
obtained in [98] by diﬀerent machinery for a wide class of ground rings. Suppos e
the Chevalley group G = G(Φ , R ) of rank /greaterorequalslant2 over the ring R is given. Suppose
SOME LOGICAL ASPECTS 11
that the ring R is elementarily rigid in the class C of rings. Then G = G(Φ , R )
is elementarily rigid in the corresponding class C1 of groups if R is a ﬁeld, R is
a local ring and G is simply connected, R is a Dedekind ring of arithmetic type,
that is the ring of S-integers of a number ﬁeld, R is Dedekind ring with at least
4 units and G is adjoint. In particular, if a ring of such kind is ﬁnitely ge nerated
then it gives rise to elementary rigidity of G = G(Φ , R ) in the class of all ﬁnitely
generated groups. If R of such kind is not elementarily rigid then G = G(Φ , R )
is elementarily rigid in the class of all groups modulo eleme ntary equivalence of
rings.
Absolutely free groups lie on the other side of the scale of gr oups. It was Tarski who
asked whether one can distinguish between ﬁnitely generate d free groups by means of
their elementary theories. This formidable problem has bee n solved in aﬃrmative, that
is all free groups have one and the same elementary theory [46 ], [99]. In fact, the variety
of all groups is the only known variety of groups, such that a f ree in this variety ﬁnitely
generated group is not rigid in the class of all such groups.
Problem 2.17. Construct a variety of groups diﬀerent from the variety of all groups such
that all free ﬁnitely generated groups in this variety have o ne and the same elementary
theory.
2.1.7. Logical equivalence of algebras. In this Section we introduce the notion of
logical equivalence of algebras which can be viewed as ﬁrst o rder equivalence. We proceed
following exactly the same scheme which was applied in Secti on 2.1.5 with respect to the
deﬁnition of geometric equivalence of algebras.
Let H1 and H2 be two algebras. We will be looking for semantic logical inva riant of
these algebras, that is compare the deﬁnable sets over H1 and H2. Recall that according
to Deﬁnition 2.4 two algebras H1 and H2 are logically similar, if the categories of deﬁnable
sets LGΘ (H1) and LGΘ (H2) are isomorphic.
Using the duality provided by Galois correspondence from Se ction 2.1.3 we will raise
logical similarity to the level of syntax. The principal Deﬁ nition 2.18 is the ﬁrst order
counterpart of Deﬁnition 2.6.
Deﬁnition 2.18. Algebras H1 and H2 are called LG-equivalent (aka logically equivalent),
if for every X and every set of formulas T in Φ( X) the equality T LL
H1 = T LL
H2 holds .
It is easy to see that
Proposition 2.19. If algebras H1 and H2 are LG-equivalent then they are elementarily
equivalent.
Now we want to understand what is the meaning of logical equiv alence.
Deﬁnition 2.20. Two algebras H1 and H2 are called LG-isotypic if for every point µ :
W (X) → H1 there exists a point ν : W (X) → H2 such that LKer(µ ) = LKer( ν) and,
conversely, for every point ν : W (X) → H2 there exists a point µ : W (X) → H1 such that
LKer(ν) = LKer( µ ).
The meaning of Deﬁnition 2.20 is the following. Two algebras are isotypic if the sets of
realizable types over H1 and H2 coincide. So, by some abuse of language these algebras
have the same logic of types. Some references for the notion o f isotypic algebras are
contained in [89], [88], [90], [91], [92], [111]. Note that t he notion was introduced in [92],
[89] while [91] gives the most updated survey.
The main theorem is as follows, see [111].
Theorem 2.21. Algebras H1 and H2 are LG-equivalent if and only if they are LG-
isotypic.
12 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
Now we are in a position to study rigidity of algebras with res pect to isotypicity prop-
erty. It is clear, that since isotypicity is stronger than el ementary equivalence, this phe-
nomenon can occur quite often. Let us state this problem expl icitly.
Problem 2.22. Let a class of algebras C and an algebra H ∈ C be given. Suppose that
algebras H ∈ C and A ∈ C are isotypic. Are they isotypically rigid, that is are H and A
isomorphic?
Remark 2.23. In many papers from the list above isotypically rigid algebr as are called
logically separable [91], [88], or type deﬁnable [68].
Theorem 2.24. We will consider the following cases of rigidity:
• Finitely generated free abelian groups are isotypically ri gid in the class of all
groups, see [111].
• Finitely generated free nilpotent groups of class at most n are isotypically rigid in
the class of all groups [111].
• Finitely generated metabelian groups are isotypically rig id in the class of all groups
[68].
• Finitely generated virtually polycyclic groups are isotyp ically rigid in the class of
all groups [68].
• Finitely generated free solvable groups of derived length d > 1 are isotypically rigid
in the class of all groups [68].
• All surface groups, which are not non-orientable surface gr oups of genus 1,2 or 3
are isotypically rigid in the class of all groups [68].
• Finitely generated absolutely free groups are isotypicall y rigid in the class of all
groups, see [101] based on [74] (also follows from [73], [25], [113]).
• Finitely generated free semigroups are isotypically rigid in the class of semigroups,
see [111].
• Finitely generated free inverse semigroups are isotypical ly rigid in the class of
inverse semigroups, see [111].
• Finitely generated free associative algebras are isotypic ally rigid in the class of
such algebras [113].
The number of examples can be continued to co-Hopf groups, so me Burnside groups,
etc.
In fact, using either logical equivalence of algebras, or wh at is the same, the isotypicity
of algebras, we compare the possibilities of individual poi nts in the aﬃne space to deﬁne
the sets of formulas (in fact ultraﬁlters in Φ( X)) which are valid in these points. Given
a point µ in the aﬃne space, the collection of formulas valid on the poi nt µ is a type of
µ . If these individual types are, roughly speaking, the same f or both algebras, then these
algebras are declared isotypic. Thus, for isotypic algebra s we compare types of formulas
realizable on these algebras. Of course, this is signiﬁcant ly stronger than elementary
equivalence, where the individuality of points disappeare d and we compare only formulas
valid in all points of the aﬃne space.
The following principal problem was stated in [91] and is wid ely open.
Problem 2.25 (Rigidity problem) . Is it true that every two isotypic ﬁnitely generated
groups are isomorphic?
We will ﬁnish with the one more tempting problem of the same sp irit.
Problem 2.26. What are the isotypicity classes of ﬁelds? When two isotypic ﬁelds are
isomorphic?
The elementary equivalence of ﬁelds was one of motivating en gines for Tarski to develop
the whole model-theoretic staﬀ related to elementary equiv alence. Problem 2.26, in a
sense, takes us back to the origins of the theory.
SOME LOGICAL ASPECTS 13
2.2. Plotkin’s problem: automorphisms of endomorphism semigro ups and
groups of polynomial automorphisms. In the light of B.I. Plotkin’s activity on cre-
ation of algebraic geometry over algebraic systems, he drew a special attention to studying
the groups of their automorphisms, see [80]. Later on he emph asized that automorphisms
of categories of free algebras of the varieties play here a ro le of exceptional importance.
This role was underlined in Proposition 2.10 of Section 2.1. The meaning of Reduction
Theorem (see [86], [43], [59], [93]) was explained just afte r this proposition. Reduction
Theorem reduces investigation of automorphisms of the whol e category Θ 0 of free in the
variety Θ algebras to studying the group Aut(End( W (X))) associated with a single ob-
ject W (X) in Θ 0. Here, W (X) is a ﬁnitely generated free in Θ algebra. In fact, if all
automorphisms of the endomorphism semigroup of a free algeb ra W (X) are close to being
inner, then all automorphisms of Θ 0 possess the same property.
This philosophy forms a clear basis for investigation of aut omorphisms of the semi-
group of polynomial endomorphisms and the group of polynomi al automorphisms. The
automorphisms of the endomorphism semigroup of a free assoc iative algebra A were given
by Belov, Berzins and Lipyanski, (see [40] for details and de ﬁnitions of semi-inner and
mirror automorphisms):
Theorem 2.27. The group Aut(End(A)) is generated by semi-inner and mirror automor-
phisms of End(A). Correspondingly, the group of automorphisms of the catego ry of free
associative algebras is generated by semi-inner and mirror automorphisms of this category.
In the same spirit, the description of an endomorphism semig roup of the ring of com-
mutative polynomials A is given by Belov and Lipyanski in [41]:
Theorem 2.28. Every automorphism of the group Aut(End(A)) is semi-inner.
The automorphisms of the group of polynomial automorphisms on free associative
algebras and commutative algebras at the level of Ind-schemes were obtained by Belov,
Elishev and J.-T.Yu in [42]. Let K[x1, . . . , x n] and K⟨x1, . . . , x n⟩ be the free commutative
polynomial algebra and the free associative algebra with n generators, respectively. Denote
by NAut the group of nice automorphisms, i.e., the group of automorphisms which can
be approximated by tame ones. One can prove that in character istic zero case every
automorphism is nice.
Theorem 2.29. Any Ind-scheme automorphism ϕ of NAut(K[x1, . . . , x n]) for n /greaterorequalslant3 is
inner, i.e., it is a conjugation via some automorphism of K[x1, . . . , x n]. Any Ind-scheme
automorphism ϕ of NAut(K⟨x1, . . . , x n⟩) for n /greaterorequalslant3 is semi-inner (see [42] for the precise
deﬁnition).
Here, the Ind-scheme is deﬁned as follows:
Deﬁnition 2.30. An Ind-variety M is the direct limit of algebraic varieties M =
lim
− →{M1 ⊆ M2 · · · }. An Ind-scheme is an Ind-variety which is a group such that the group
inversion is a morphism Mi → Mj(i) of algebraic varieties, and the group multiplication
induces a morphism from Mi × Mj to Mk(i,j ). A map ϕ is a morphism of an Ind-variety
M to an Ind-variety N , if ϕ (Mi) ⊆ Nj(i) and the restriction ϕ to Mi is a morphism for
all i. Monomorphisms, epimorphisms and isomorphisms are deﬁned similarly in a natural
way.
