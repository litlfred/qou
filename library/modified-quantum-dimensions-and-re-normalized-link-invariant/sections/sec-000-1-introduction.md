---
doc_id: modified-quantum-dimensions-and-re-normalized-link-invariant
doc_title: "Modified quantum dimensions and re-normalized link invariants"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: modified-quantum-dimensions-and-re-normalized-link-invariants.pdf
source_sha256: 5447f6d5f5d6c8d7
toc_source: outline
doc_brief: "Modified quantum dimensions and re-normalized link invariants — 8 sections: Front matter; Introduction; Ribbon Ab-categories"
---
One obstruction to applications of quantum link invariants associated with a ribbon category C
stems from the fact that certain simple (irreducible) objects of C may have zero quantum
dimensions. If the dimension of a simple object V ∈Ob(C) is zero, then the quantum invariants
of all (framed oriented) links with components labeled by V are equal to zero. A well-known
topological trick allows us to derive possibly non-trivial invariants in this setting, at least in the
case of knots. Namely, one presents a V -labeled knot L as the closure of a (1, 1) tangle T and
considers the endomorphism of V associated with T. This endomorphism is the product of the
identity IdV : V →V with an element ⟨T⟩of the ground ring of C. The tangle T is determined
by L uniquely up to isotopy and therefore ⟨T⟩is an isotopy invariant of L. This invariant may
be non-trivial even when dimC(V ) = 0. Note that the usual quantum invariant of L is equal to
⟨T⟩dimC(V ).
For a link L with at least two components labeled by V , the situation is more involved
because ⟨T⟩may depend on the choice of T. In many known examples of ribbon categories, an
appropriate re-normalization of ⟨T⟩does not depend on the choice of T and yields a possibly
non-trivial invariant of L, see [ADO92, GP08b, Kas95, KS91]. A systematic explanation of this
phenomenon seems to be missing in the literature. In this paper we suggest such an explanation.
It is based on a new notion of an ambidextrous object in C. Every simple ambidextrous object
J ∈Ob(C) determines a certain set A(J) of (isomorphism classes of) simple objects of C. For all
Received 10 December 2007, accepted in ﬁnal form 4 June 2008.
2000 Mathematics Subject Classiﬁcation 81R50, 57M27, 18D10, 17B.
Keywords: knot, Lie algebra, tensor category, quantum group.
The work of the ﬁrst author has been partially supported by NSF grant DMS-0706725 and the work of the
third author has been partially supported by NSF grant DMS-0707078.
This journal is c⃝Foundation Compositio Mathematica 2009.
Modified quantum dimensions and re-normalized link invariants
simple objects V belonging to this set we deﬁne a modiﬁed (quantum) dimension depending on J.
The modiﬁed dimension may be non-zero when dimC(V ) = 0. Using the modiﬁed dimensions we
deﬁne an isotopy invariant F ′(L) for any link whose components are labeled with objects of C
under the only assumption that at least one of the labels belongs to A(J). Most of these results
extend to closed C-colored ribbon graphs (i.e. to C-colored ribbon graphs with no inputs and
no outputs).
We give three families of examples illustrating our constructions. In the ﬁrst example, C is the
category of ﬁnite-dimensional Uq(g)-modules, where Uq(g) be the Drinfeld–Jimbo C(q)-algebra
associated to a simple complex Lie algebra. In this case we recover the standard Reshetikhin–
Turaev link invariants. In the second example C is the category of topologically free Uh(g)-
modules of ﬁnite rank, where g is a Lie superalgebra of type I and Uh(g) is its quantized
universal enveloping C[[h]]-superalgebra. In this case we recover the link invariants deﬁned by
the ﬁrst two authors in [GP08b, GP08a]. These invariants generalize both the multivariable
Alexander polynomial of links and Kashaev’s link invariants. In the ﬁnal example C is the
category of ﬁnite-dimensional weight Uq(sl(2))-modules where q is a root of unity. We show that
our construction in this case gives a generalization of the invariants deﬁned by Akutsu, Deguchi
and Ohtsuki [ADO92], using a regularization of the Markov trace and nilpotent representations
of Uq(sl(2)) at a root of unity. In the later two examples the standard Reshetikhin–Turaev link
invariant coming from C is generically zero.
The paper is organized as follows. In § 2 we recall the basic results on ribbon categories. In § 3
we introduce the ambidextrous objects, the modiﬁed dimensions and the invariant F ′ of closed
C-colored ribbon graphs. In § 4 we extend F ′ to arbitrary C-colored ribbon graphs (this does not
yield a functor as in the standard theory but only a quasi-functor). In § 5 we study the basic
properties of F ′. Section 6 is devoted to the presentation of examples.
