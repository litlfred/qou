---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-001-01-on-the-subject
section_title: "On the Subject"
section_number: 0.1
pages: 7-9
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
and J.-L.Verdier around 1960, and were ﬁrst published in the book [62] by R.
Hartshorne. The basic idea was as follows. They had realized that the derived
functors of classical homological algebra, namely the functorsRqF, LqF : M→N
derived from an additive functorF : M→N between abelian categories, are too
limited to allow several rather natural manipulations. Perhaps the most impor-
tant operation that was lacking was the composition of derived functors; the best
approximation of it was a spectral sequence.
The solution to the problem was to invent a new category, starting from a given
abelian categoryM. The objects of this new category are the complexes of objects of
M. These are the same complexes that play an auxiliary role in classical homological
algebra, as resolutions of objects ofM. The complexes form a categoryC(M), but
this category is not suﬃciently intricate to carry in it the information of derived
functors. So it must be modiﬁed.
A morphismφ:M→N in C(M) is called aquasi-isomorphism if in each degree
q the cohomology morphismHq(φ) : Hq(M)→Hq(N) in M is an isomorphism. The
modiﬁcation that is needed is to make the quasi-isomorphisms invertible. This is
done by a formal localization procedure, and the resulting category (with the same
objects as C(M)) is the derived categoryD(M). There is a functor Q : C(M)→
D(M), which is the identity on objects, and it has a universal property (it is initial
among the functors that send the quasi-isomorphisms to isomorphisms). A theorem
(analogous to Ore localization in noncommutative ring theory) says that every
morphism θin D(M) can be written as a simple left or right fraction:
(0.1.1) θ= Q(ψ0)−1◦Q(φ0) = Q(φ1)◦Q(ψ1)−1,
where φi and ψi are morphisms inC(M), andψi are quasi-isomorphisms.
The cohomology functors Hq : D(M)→M, for allq∈Z, are still deﬁned. It
turns out that the functorM→D(M), that sends an objectM to the complexM
concentrated in degree0, is fully faithful.
The next step is to say what is a left or a right derived functor of an additive
functor F : M→N. The functor F can be extended in an obvious manner to a
functor on complexesF : C(M)→C(N). A right derived functorof F is a functor
(0.1.2) RF : D(M)→D(N),
together with a morphism of functorsηR : QN◦F→RF◦QM. The pair (RF,ηR)
has to beinitial among all such pairs. The uniqueness of such a functorRF, up to a
unique isomorphism, is relatively easy to prove (using the language of2-categories).
As for existence ofRF, it relies on the existence of suitable resolutions (like the
injective resolutions in the classical situation). If these resolutions exist, and if the
original functorF is left exact, then there is a canonical isomorphism of functors
(0.1.3) RqF∼= Hq◦RF : M→N
for everyq≥0.
The left derived functor
(0.1.4) LF : D(M)→D(N)
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
7
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is deﬁned similarly. When suitable resolutions exist, and whenF is right exact,
there is a canonical isomorphism of functors
(0.1.5) LqF∼= H−q◦LF : M→N
for everyq≥0.
There are several variations:F could be a contravariant additive functor; or it
could be an additive bifunctor, contravariant in one or two of its arguments. In all
these situations the derived (bi)functorsRF and LF can be deﬁned.
The derived categoryD(M) is additive, but it is not abelian. The notion of short
exact sequence (in M and in C(M)) is replaced by that ofdistinguished triangle,
and thus D(M) is a triangulated category. The derived functors RF and LF are
triangulated functors, which means that they send distinguished triangles inD(M)
to distinguished triangles inD(N).
Already in classical homological algebra we are interested in the bifunctors
Hom(−,−) and (−⊗−). These bifunctors can also be derived. To simplify matters,
let’s assume thatA is a commutative ring, andM = N = ModA, the category of
A-modules. We then have bifunctors
HomA(−,−) : ( ModA)op×ModA→ModA
and
(−⊗A−) : ModA×ModA→ModA,
where the superscript “op” denotes the opposite category, that encodes the con-
travariance in the ﬁrst argument of Hom. In this situation all resolutions exist, and
we have the right derived bifunctor
(0.1.6) RHomA(−,−) : D(ModA)op×D(ModA)→D(ModA)
and the left derived bifunctor
(0.1.7) (−⊗L
A−) : D(ModA)×D(ModA)→D(ModA).
The compatibility with the classical derived bifunctors is this: there are canonical
isomorphisms
(0.1.8) Extq
A(M,N )∼= Hq(
RHomA(M,N )
{
and
(0.1.9) TorA
q (M,N )∼= H−q(M⊗L
AN)
for allM,N ∈ModA and q≥0.
This is what derived categories and derived functors are. As to what can be
done with them, here are some of the things we will explore in our book:
•Dualizing complexes and residue complexes over noetherian commutative
rings. Besides the original treatment from [62], that we present in detail
here, we also includeVan den Bergh rigidityin the commutative setting,
that gives rise torigid residue complexes.
•Perfect DG modulesand tilting DG bimodules over noncommutative DG
rings, and a few variants ofderived Morita Theory, including theRickard-
Keller Theorem.
•Derived torsionandbalanced dualizing complexesover connected graded NC
rings, andrigid dualizing complexesover NC rings, including a full proof of
the Van den Bergh Existence Theoremfor NC rigid dualizing complexes.
A topic that is beyond the scope of this book, but of which we provide an outline
here, is:
•The rigid approach to Grothendieck Duality on noetherian schemes and
Deligne-Mumford stacks.
8
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Derived categories have important roles in several areas of mathematics; below
is a partial list. We will not be able to talk about any of these topics in our book,
so instead we give some references alongside each topic.
.D-modules, perverse sheaves, and representations of algebraic groups and
Lie algebras. See [16] and [27]. More recently the focus in this area is on
the Geometric Langlands Correspondence, that can only be stated in terms
of derived categories (see the survey [50]).
. Algebraic analysis, including diﬀerential, microdiﬀerential and DQ mod-
ules (see [74], [134], [77]) and microlocal sheaf theory (see [75]), with its
application to symplectic topology (see [149], [110]).
. Representations of ﬁnite groups and quivers, includingcluster algebrasand
the Broué Conjecture. See [59], [84], [43].
. Birational algebraic geometry. This includesFourier-Mukai transformsand
semi-orthogonal decompositions. See the surveys [64] and [103], and the
book [70].
. Homological mirror symmetry. It relates the derived category of coherent
sheaves on a complex algebraic varietyX to thederived Fukaya categoryof
the mirror partnerY, which is a symplectic manifold. See Remark 3.8.22
and the online reference [88].
. Derived algebraic geometry. Here not only the category of sheaves is de-
rived, but also the underlying geometric objects (schemes or stacks). See
Example 6.2.35, Remark 6.2.38, and the references [99] and [152].
