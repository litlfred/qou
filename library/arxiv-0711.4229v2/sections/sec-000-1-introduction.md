---
doc_id: arxiv-0711.4229v2
doc_title: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0711.4229v2.pdf
source_sha256: 2e6cc61069016627
toc_source: outline
doc_brief: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS — In this paper we give a re-normalization of the Reshetikhin-Turaev quantum invariants of links, by modiﬁed quantum dimensions."
---
One obstruction to applications of quantum link invariants associated with a ribbon category
C stems from the fact that certain simple (irreducible) objects of C may have zero quantum
dimensions. If the dimension of a simple object V ∈Ob(C) is zero, then the quantum invariants
of all (framed oriented) links with components labeled by V are equal to zero. A well known
topological trick allows to derive possibly non-trivial invariants in this setting, at least in the
case of knots. Namely, one presents a V -labeled knot L as the closure of a (1, 1) tangle T and
considers the endomorphism of V associated with T . This endomorphism is the product of the
identity IdV : V →V with an element ⟨T ⟩of the ground ring of C. The tangle T is determined
by L uniquely up to isotopy and therefore ⟨T ⟩is an isotopy invariant of L. This invariant may
be non-trivial even when dimC(V ) = 0. Note that the usual quantum invariant of L is equal to
⟨T ⟩dimC(V ).
For a link L with ≥2 components labeled by V , the situation is more involved because ⟨T ⟩
may depend on the choice of T . In many known examples of ribbon categories, an appropriate
re-normalization of ⟨T ⟩does not depend on the choice of T and yields a possibly non-trivial
invariant of L, see [5], [1], [4], [2]. A systematic explanation of this phenomenon seems to be
missing in the literature. In this paper we suggest such an explanation. It is based on a new
notion of an ambidextrous object in C. Every simple ambidextrous object J ∈Ob(C) determines
a certain set A(J) of (isomorphism classes of) simple objects of C. For all simple objects V
belonging to this set we deﬁne a modiﬁed (quantum) dimension depending on J. The modiﬁed
dimension may be non-zero when dimC(V ) = 0. Using the modiﬁed dimensions we deﬁne an
isotopy invariant F ′(L) for any link whose components are labeled with objects of C under the
only assumption that at least one of the labels belongs to A(J). Most of these results extend to
closed C-colored ribbon graphs (i.e., to C-colored ribbon graphs with no inputs and no outputs).
Date: November 9, 2018.
1
2
NATHAN GEER, BERTRAND PATUREAU-MIRAND, AND VLADIMIR TURAEV
We give three families of examples illustrating our constructions. One example: C is the
category of ﬁnite dimensional Uq(g)-modules, where Uq(g) be the Drinfeld-Jimbo C(q)-algebra
associated to a simple complex Lie algebra. In this case we recover the standard Reshetikhin-
Turaev link invariants. In the second example C is the category of topologically free Uh(g)-
modules of ﬁnite rank, where g is a Lie superalgebra of type I and Uh(g) is its quantized
universal enveloping C[[h]]-superalgebra. In this case we recover the link invariants deﬁned by
the ﬁrst two authors in [2, 3]. These invariants generalize both the multivariable Alexander
polynomial of links and Kashaev’s link invariants. In the ﬁnal example C is the category of
ﬁnite dimensional weight Uq(sl(2))-modules where q is a root of unity. We will show that our
construction in this case gives a generalization of the invariants deﬁned by Akutsu, Deguchi
and Ohtsuki [1], using a regularization of the Markov trace and nilpotent representations of
Uq(sl(2)) at a root of unity. In the later two examples the standard Reshetikhin-Turaev link
invariant coming from C is generically zero.
The paper is organized as follows. In Section 2 we recall the basic results on ribbon categories.
In Section 3 we introduce the ambidextrous objects, the modiﬁed dimensions and the invariant
F ′ of closed C-colored ribbon graphs. In Section 4 we extend F ′ to arbitrary C-colored ribbon
graphs (this does not yield a functor as in the standard theory but only a quasi-functor). In
Section 5 we study the basic properties of F ′. Section 6 is devoted to the examples.
