---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
1. Pivotal and spherical categories 3
2. Multiplicities in pivotal categories 5
3. Invariants of colored graphs 8
4. Pre-fusion and fusion categories 10
5. State sums on triangulated 3-manifolds 13
6. State sums on skeletons of 3-manifolds 14
7. Moves on skeletons and proof of Theorems 5.1 and 6.1 16
8. Skeletons in the relative case 22
9. The state-sum TQFT 26
10. Modular categories and categorical centers 31
11. Main theorems and applications 34
12. State sum invariants of links in 3-manifolds 35
13. Deduction of Theorems 11.1 and 11.2 from Lemma 11.3 55
14. The coend of the center 59
15. Proof of Lemma 11.3 64
Appendix. The 6 j-symbols 69
References 70
Introduction
Two fundamental constructions of 3-dimensional topological qua ntum ﬁeld the-
ories (TQFTs) are due to Reshetikhin-Turaev [RT] and Turaev-Viro [TV]. The
RT-construction is widely viewed as a mathematical realization of Witt en’s Chern-
Simons TQFT, see [Wi]. The TV-construction is closely related to the P onzano-
Regge state-sum model for 3-dimensional quantum gravity, see [ Ca]. The ﬁrst
connections between these two constructions were established b y Walker [Wa] and
Turaev [Tu]. In 1995, the ﬁrst named author conjectured a more g eneral connection
between these constructions. This connection may be formulated as the identity
|M|C = τZ(C)(M ), see below for a detailed statement. The aim of our paper is to
prove this conjecture.
Date: August 21, 2018.
2010 Mathematics Subject Classiﬁcation. 57R56.
1
2 V. TURAEV AND A. VIRELIZIER
The Turaev-Viro approach derives TQFTs from spherical fusion ca tegories. We
deﬁne a fusion category as a monoidal category with compatible left and right du-
alities such that all objects are direct sums of simple objects and th e number of
isomorphism classes of simple objects is ﬁnite. The condition of spher icity says that
the left and right dimensions of all objects are equal. A spherical fu sion category
has a numerical dimension, which we suppose to be non-zero throug hout the intro-
duction. The original TV-construction [TV] applies to categories of representations
of the quantum group Uq(sl2(C)) at roots of unity. This was extended to modu-
lar categories (i.e., to spherical fusion categories with braiding) in [T u]. At about
the same time, A. Ocneanu observed that the use of the braiding ma y be avoided.
This was formalized by Barrett and Westbury [BW1] (see also [GK]) wh o derived
a topological invariant |M|C of an arbitrary closed oriented 3-manifold M from a
spherical fusion category C. The deﬁnition of |M|C goes by considering a certain
state sum on a triangulation of M and proving that this sum depends only on M
and not on the choice of triangulation. The key algebraic ingredients of the state
sum are the so-called 6 j-symbols associated with C.
The Reshetikhin-Turaev construction of 3-manifold invariants use s as the main
algebraic ingredient a modular category B. This construction associates with every
closed oriented 3-manifold M a numerical invariant τB(M ). Its deﬁnition is based
on surgery presentations of M by links in the 3-sphere.
For every monoidal categoryC, Joyal and Street [JS] and Drinfeld (unpublished,
see Majid [Maj]) deﬁned a braided monoidal category Z(C) called the center of C.
A fundamental theorem of M¨ uger [M¨ u2] says that the center o f a spherical fusion
categoryC over an algebraically closed ﬁeld is modular. Combining with the results
mentioned above, we observe that such a C gives rise to two 3-manifold invariants:
|M|C andτZ(C)(M ). We prove in the present paper that these invariants are equal,
i.e., for all M ,
(1) |M|C =τZ(C)(M ).
This was previously known in several special cases: when C is modular [Tu, Wa],
whenC is the category of bimodules associated with a subfactor [KSW], and w hen
C is the category of representations of a ﬁnite group. For modular C, the category
Z(C) is braided equivalent to the Deligne tensor product C ⊠C, where C is the
mirror ofC, and therefore Formula (1) can be rewritten as
|M|C =τC⊠C(M ) = τC(M )τC(M ) = τC(M )τC(−M ),
where−M isM with opposite orientation. If C is a unitary modular category, then
τC(−M ) = τC(M ) and so |M|C =|τC(M )|2.
Formula (1) relates two categorical approaches to 3-manifold inva riants through
the categorical center. This relationship sheds new light on both ap proaches and
shows, in particular, that the RT-construction is more general th an the state sum
construction. For further corollaries of Formula (1), see Section 11.
The proof of Formula (1) is based on topological quantum ﬁeld theor y (TQFT).
For a modular category B, the invariants τB(M ) extend to a 3-dimensional TQFT
τB derived from B, see [RT]. The invariant |M|C also extends to a 3-dimensional
state sum TQFT |.|C which we deﬁne here in terms of state sums on skeletons of
3-manifolds. It is crucial for the proof of Formula (1) that we allow n on-generic
skeletons, i.e., skeletons with edges incident to ≥ 4 regions. In particular, we give
two diﬀerent state sums on any triangulation t of a closed oriented 3-manifold M :
the one in [TV, BW1] and a new one. In the former, the labels are attr ibuted to the
edges and the Boltzmann weights are the 6 j-symbols computed in the tetrahedra;
in the latter, the labels are attributed to the faces and the Boltzma nn weights are
computed in the vertices. The existence of two diﬀerent state sum s is due to the
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 3
fact that the triangulation t gives rise to two diﬀerent skeletons of M : the 2-skeleton
of the cellular decomposition of M dual to t and the 2-skeleton of t itself. (It is
non-obvious but true that these two state sums are equal.)
Our main theorem claims that for any spherical fusion category C over an alge-
braically closed ﬁeld, the TQFTs |.|C and τZ(C) are isomorphic:
|Σ|C≃τZ(C)(Σ) and |M|C≃τZ(C)(M )
for any oriented closed surface Σ and any oriented 3-cobordism M . The proof in-
volves a detailed study of transformations of skeletons of 3-manif olds and the com-
putation of the coend of Z(C) provided by the theory of Hopf monads in monoidal
categories due to Brugui` eres and Virelizier [BV2]. Another importa nt ingredient of
the proof is an extension of |M|C to a state sum invariant |M,L|C of aZ(C)-colored
framed link L in a 3-manifold M .
After the appearance of the present paper on arXiv, Balsam and K irillov [Ba1,
Ba2, BK] found a diﬀerent proof of (1) based on the concept of an extended TQFT.
The paper is organized as follows. Sections 1–4 deal with preliminaries on
monoidal and fusion categories and the associated invariants of co lored graphs.
In Sections 5–9 we construct the TQFT |.|C. In Sections 10 and 11 we recall the
necessary deﬁnitions from the theory of modular categories and s tate our main the-
orems. A proof of these theorems is given in Sections 12–15. Thoug h we do not
speciﬁcally use 6 j-symbols, we include for completeness an appendix summarizing
their properties.
The authors are indebted to N. Ivanov and S. Matveev for helpful discussions.
The work of V. Turaev on this paper was partially supported by the N SF grant
DMS-0904262. A. Virelizier was partially supported by the ANR grant GESAQ.
Throughout the paper, the symbol k denotes a commutative ring.
