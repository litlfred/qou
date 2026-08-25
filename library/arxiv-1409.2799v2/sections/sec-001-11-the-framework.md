---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-001-11-the-framework
section_title: "The framework"
section_number: 1.1
pages: 1-5
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
1.2. An outline of the paper 5
2. The tilting category T 5
2.1. Quantum groups at roots of unity 5
2.2. Weyl modules, dual Weyl modules and simple modules 6
2.3. Tilting modules and the tilting category T 8
2.4. The linkage principle and blocks 10
2.5. Translation functors 14
3. The Khovanov-Seidel quiver algebra and gradings 17
3.1. The quiver algebras Qm and Q∞ 17
3.2. Combinatorics of the graded, right Qm- and Q∞-modules 19
3.3. Endofunctors on pModgr-Qm and pModgr-Q∞ 20
3.4. Q∞ and the tilting category T 22
3.5. The tilting category T and its graded counterpart Tgr 27
4. Diagrams for the graded tilting category Tgr 31
4.1. The basics: diagrammatic categories, additive closur es and Karoubi envelopes 31
4.2. The dihedral cathedral D(∞) 32
4.3. The quotient QD(∞) 37
4.4. QD(∞) and the tilting category Tgr 41
4.5. Diagram categories for pEnd(Tgr
λ ) 46
References 48
1. I NTRODUCTION
1.1. The framework. In this paper we study the quantum group Uq = Uq(sl2), where q is a root
of unity, its category of tilting modules T and the category of projective endofunctors pEnd(T)
combinatorially and diagrammatically.
The authors were partially supported by the center of excell ence grant “Centre for Quantum Geometry of Moduli
Spaces (QGM)” from the “Danish National Research Foundation (DNRF)”.
1
Everything we do is completely explicit and “down to earth”, but motivated and deduced from
a general machinery that comes, from the side of representat ion theory, from pioneering work of
Soergel [53], Beilinson-Ginzburg-Soergel [7], Kazhdan-Lusztig [29] and Stroppel [57], and from
the side of combinatorics and diagrammatics, from work of So ergel [55], Khovanov-Lauda [33]
and Elias-Khovanov [19].
Let us motivate and explain our approach.
1.1.1. Quantum groups at roots of unity: non-semisimplicity, modu lar representation theory and
afﬁne Weyl groups. Fix a simple complex Lie algebra g. Then the ﬁnite-dimensional 1 represen-
tation theory of the quantum deformation Uv(g) of U(g) is, for generic parameter v, semisimple
and very similar to the classical representation theory for U(g).
This drastically changes when specializing v to an l-th (we allow any l > 2 throughout the
paper) root of unity q: the representation theory of Uq(g) is non-semisimple. This is mostly due to
the fact that the so-called Weyl modules at roots of unity are, in general, not simple and ﬁltrations
by Weyl modules do not necessarily split. A lot of questions remain open about the representation
theory at roots of unity. In fact, the representation theory of Uq(g) over C has many similarities to
the representation theory of a corresponding almost simple , simply connected algebraic group G
over an algebraically closed ﬁeld K of prime characteristic, see for example [3] or [40].
It turns out, when studying the representation theory of Uq(g), a certain category of tilting
modules T comes up naturally. The category T is inspired by the corresponding category of tilting
modules for reductive algebraic groups due to Donkin [17] (see also Ringel [49]) and shares most
of its properties, see for example [1]. It is our main object under study in this paper.
Note that the “combinatorics” (the irreducible characters ) of G and Uq(g) was conjectured by
Lusztig (see [42] for G and [40] for Uq(g)) to be related to values at 1 of the Kazhdan-Lusztig
polynomial associated to the afﬁne Weyl group for g. In addition, Kazhdan and Lusztig proved
later that the category of ﬁnite-dimensional Uq(g)-modules (of type 1) is equivalent to a category
of modules for the corresponding afﬁne Kac-Moody algebra, see [29].
This combined with the solution of Kashiwara and Tanisaki [28] of the Kazhdan-Lusztig conjec-
ture in the afﬁne Kac-Moody case then solved the above mentio ned conjecture for the irreducible
characters of Uq(g). Even closer related to our work: Soergel ﬁrst conjectured i n [54] and later
proved in [52] a corresponding statement about indecomposa ble tilting modules. In our little sl2
case we do not need these deep results because we can work out b oth, the irreducible characters
and the indecomposable tilting modules, “by hand”.
1.1.2. Categoriﬁcation and graded categories. A ground-breaking development towards giving
an algebraic proof of the Kazhdan-Lusztig conjectures was initiated by Soergel in [55]. He deﬁnes
a combinatorial category S consisting of objects that are bimodules over a polynomial r ing R.
These bimodules are nowadays commonly called Soergel bimodules and are indecomposable direct
summands of tensor products of certain algebraically/combinatorially deﬁned R-bimodules.
His category is additive, monoidal and graded and he proves t hat its Grothendieck group K0 is
isomorphic to an integral form of the Hecke algebra Hv(W ) associated to the Weyl group W of
the simple Lie algebra g in question. Here the grading and the corresponding shifting functors give
on the level of Grothendieck groups rise to the indeterminat e v of Hv(W ). Thus, we can say that
1If not otherwise stated: modules in this paper are assumed to be ﬁnite-dimensional. There are only few exceptions
in this paper, e.g. Tq(∞ ) from Deﬁnition 2.25. We hope it is clear from the context.
2
Soergel’s hascategoriﬁed Hv(W ) (actually, the categoriﬁcation works for any Coxeter group W
and its associated Hecke algebra Hv(W )).
In fact, in the spirit of categoriﬁcation outlined by Crane and Frenkel in the mid-nineties,graded
categories C (or graded 2-categories) give rise to a structure of aZ[v, v−1]-module on K0(C) (where
“shifting decategoriﬁes” to multiplication by v). Many examples of this kind of categoriﬁcation
are known. For example, Khovanov’s categoriﬁcation of the J ones polynomial (sometimes also
called sl2-polynomial) [30], Khovanov-Rozansky’s categoriﬁcation of the sln-polynomial in [35]
(all of these, although originally deﬁned differently, can be obtained using 2-functors on graded
2-categories), or Khovanov-Lauda and Rouquier’s categoriﬁcation of Uv(g) and its highest weight
modules, see for example [33] and [50] using the so-called Khovanov-Lauda Rouquier algebra, are
among the more popular ones and have opened new directions of research.
Thus, it is natural to ask if we can introduce a non-trivial grading on T as well. We do this
in Section 3 by using an argument pioneered by Soergel (see [5 3]) in the ungraded and Stroppel
(see [57]) in the graded case for category O. Namely, the usage of Soergel’s combinatorial functor
V that gives rise to an equivalence of a block ofO (for g) and a certain full subcategory ofMod-A.
The algebra A is the endomorphism ring of the anti-dominant projective in the block and it can be
explicitly (when the block is regular) identiﬁed with the algebra of coinvariants for the Weyl group
associated to g. This algebra can be given aZ-grading and, as Stroppel explains in [57], this set-up
gives rise to graded versions of blocks of category O and the categories of graded endofunctors
on these blocks. In fact, as Stroppel explains in [57], her approach is a combinatorial alternative to
the approach of Beilinson, Ginzburg and Soergel given in [7].
As in the other cases above, the grading is the crucial point: in category O the multiplicity
[∆ q(λ) : Lq(µ)] of the simple module Lq(µ) inside of the Verma ∆ q(λ) is given by evaluating the
corresponding Kazhdan-Lusztig polynomial at 1. The Kazhdan-Lusztig polynomial is a polyno-
mial and not just a number and the grading ofO “explains” now theindividual coefﬁcients of these
polynomials as well.
In our case the role of A is, as we explain in Section 3, played by an “inﬁnite version” Q∞ of a
quiver algebra Qm that Khovanov and Seidel introduced in [36] in their study ofFloer homology2.
Its “Koszul version” appears in various contexts related tosymplectic topology, algebraic geometry
and representation theory. In particular, it appears as a subquotient of Khovanov’s arc algebra that
he introduced in [31] to give an algebraic structure underly ing Khovanov homology and whose
representation theory is known to be highly interesting as outlined in a series of papers by Brundan
and Stroppel, see [12], [13], [14], [15] and [11]. The gradin g can be seen as coming from the
corresponding grading of some Khovanov-Lauda Rouquier algebra and we use it to introduce the
grading on T (for each block Tλ) and we obtain a graded category Tgr.
We stress that this grading is a “root of unity phenomenon”: the category of ﬁnite-dimensional
Uv-modules is semisimple and has therefore no interesting grading. On the other hand, the grading
on Tgr is non-trivial and gives for example rise (as mentioned abov e) to a grading for similar
modules of reductive algebraic groups over algebraical closed ﬁelds K of prime characteristic.
Thus, an intriguing question is if one can use the grading on Tgr to obtain new information
about link invariants or about the Witten-Reshetikhin-Turaev invariants of 3-manifolds that can be
deduced from T, see [1] or [61]. Note that, as we deduce in Remark 3.29, each b lock Tgr
λ of Tgr
2Around the same time this quiver algebra was considered independently by Braden in [10]. We stay with Khovanov
and Seidel’s formulation (but writeQm instead of Am as they do) because the functors they considered on the category
of representations of this algebra are closely connected to translation functors in our context.
3
decategoriﬁes to the Burau representation of the braid grou p B∞ with ∞-many strands (the split
Grothendieck group K ⊕
0 carries an action of B∞), which already gives a hint how these topological
invariants could be related to our work.
1.1.3. Diagram categories, biadjoint functors and diagrammatic categoriﬁcation. Khovanov and
Lauda have categoriﬁed Uv(slk), see [33]. Their approach, that has turned out to be very frui tful,
was to use diagrammatic categoriﬁcation: they deﬁned a certain 2-category U(slk) consisting of
a certain type of so-called string diagrams whose (split) Gr othendieck group K ⊕
0 (U(slk)) gives
the idempotented, integral form ˙Uv(slk)Z of Uv(slk). One of their main observations was that
the E’s and F ’s of ˙Uv(slk)Z behave like biadjoint induction and restriction functors o n certain
categories. As outlined in an even more general framework by Khovanov in [32] (although it
was folklore knowledge for some years and appears in a more ri gorous form in for example [27]
or [46]), biadjoint functors have a “built-in topology” since, roughly, biadjointness means that we
can straighten out diagrams.
Let us denote by Bi the bimodules from Soergel’s categoriﬁcation of the Hecke algebra Hv(W )
from above. A main feature of the Bi’s is that tensoring withBi is a self-adjoint endofunctor and,
even stronger, a Frobenius object, i.e. there are morphisms
Bi → R, R → Bi, B i → Bi ⊗R Bi and Bi ⊗R Bi → Bi
pictured as (we read from bottom to top and right to left)
R
Bi
,
Bi
R
,
Bi ⊗ Bi
Bi
,
Bi ⊗ Bi
Bi
that satisfy the Frobenius relations(plus reﬂections of these)
Frob1 : = , Frob2 : = =
It is tempting to ask if one can give a diagrammatic categoriﬁcation in the spirit of Uv(sln)-string
diagrams of Khovanov-Lauda (see [33]) for Soergel’s catego riﬁcation as well. The observations
from above, as Khovanov explains in [32, Section 3], were the main reason why Elias and Kho-
vanov started to look for such a description.
They were (very) successful in their search and their diagrammatic categoriﬁcation given in [19]
(in fact, the diagrams above are the ones they use) has inspir ed many successive works. Most
mentionable for this paper: Elias’ categoriﬁcation D(∞) of the Hecke algebra Hv(D∞) (where
D∞ is the inﬁnite dihedral group) from [18] called the dihedral cathedral or, alternatively, the
presentation in terms of generators and relations of the same category given by Libedinsky [39].
This has already led to seminal results: as Elias and Williamson explain in [23, Subsection 1.3],
their algebraic proof that the Kazhdan-Lusztig polynomials have positive coefﬁcients forarbitrary
Coxeter systems was discovered using the diagrammatic framework from [21] and [22].
In our context: the combinatorics of the blocks Tλ, as explained in Subsection 2.5, is mostly
governed by two functors Θ s and Θ t called translation through the s and t-wall respectively. Here
s and t are the two reﬂections that generate theafﬁne Weyl groupWl ∼= D∞ of sl2. These functors,
motivated from the category O analogs, are biadjoint and satisfy Frobenius relations. Moreover,
we show in Lemma 3.8 and Theorem 3.12 that this still holds in the graded setting. Thus, it seems
4
reasonable to expect thatTgr
λ and its category of (graded) projective endofunctorspEnd(Tgr
λ ) have
a diagrammatic description as well. And, since Wl ∼= D∞, it seems reasonable to expect a relation
to Elias’ dihedral cathedral D(∞) from [18]. We prove this in Section 4 by introducing certain
quotients of D(∞) giving rise to a diagrammatic presentation of Tgr
λ and pEnd(Tgr
λ ).
