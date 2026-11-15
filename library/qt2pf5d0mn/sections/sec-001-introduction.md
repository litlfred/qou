---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 10-15
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
The notion of a topological quantum ﬁeld theory (TQFT) was invented by E. Witten
based on path integrals in physics [1]. M. Atiyah gave a mathematical formulation of
TQFTs [2]. Since then there has been a vast study of TQFTs both from the physics
side and mathematics side. Roughly speaking, a (d + 1)-TQFT associates to every d-
manifold a Hilbert space and to every (d + 1)-manifold a vector in the Hilbert space
corresponding to the boundary of the (d+1)-manifold. These assignments should satisfy
certain compatible properties as speciﬁed by the axioms. Each (d+1)-TQFT produces a
scalar invariant, called the partition function, for smooth closed (d + 1)-manifolds. This
is particularly useful in topology as it may have the power to detect smooth structures
on a given manifold.
The study of TQFTs is closely related to higher category theories [3][4]. In general,
an n-TQFT is to be described by the data of an n-category. On one hand, strict n-
categories are well-deﬁned for any n [5] [6], but this is not enough for the purpose of
constructing TQFTs since many important higher categories are not strict and can not
be strictiﬁed either [7]. On the other hand, weak n-categories are only rigorously deﬁned
for small n (like n = 1, 2, 3, 4), and it is still controversial what should be the right notion
1
CHAPTER 1. INTRODUCTION
of weak n-categories for higher n, although there have been many eﬀorts in this direction
[8] [9] [10]. In the following, by n-categories we mean weak n-categories. Special n-
categories can be constructed from k-categories with certain extra structures for k < n.
For instance, a monoidal 1-category is a 2-category and a braided monoidal 1-category
is a 3-category. When constructing TQFTs, especially (2 + 1)- and (3 + 1)-TQFTs, one
usually utilize these special n-categories to bypass the barrier of the poor deﬁnition of
general n-categories. We give a brief overview of some categorical constructions of (2+1)-
and (3 + 1)-TQFTs below.
There has been a signiﬁcant amount of achievements in (2+1)-TQFTs. N. Reshetikhin
and V. Turaev constructed an invariant of 3-manifolds (Reshetikhin-Turaev invariant)
using modular tensor categories, which is believed to be the mathematical realization of
Witten’s TQFT from non-abelian Chern-Simon theories [11]. V. Turaev and O. Viro gave
a state-sum invariant of 3-manifolds (Turaev-Viro invariant) with the data from a ribbon
fusion category [12]. Later this invariant was generalized by J. Barrett and B. Westbury
so that it takes a spherical fusion category as input [13]. The Reshetikhin-Turaev in-
variant with the center of a spherical fusion category C as input is shown to equal the
Turaev-Viro invariant with C as input [14] [15] [16]. Apart from these categorical con-
structions of TQFTs, another approach is by using certain Hopf algebras, among which
the Kuperberg invariant [17] and the Hennings invariant [18] [19] are non-semisimple
generalizations of the Turaev-Viro invariant and the Reshetikhin-Turaev invariant, re-
spectively. A special case of the Kuperberg invariant reduces to the Dijkgraaf-Witten
theory [20].
The study of (2 + 1)-TQFTs has had great eﬀects on quantum groups,
3d topology and knot theories. For example, the Turaev-Viro invariant can distinguish
certain manifolds which are homotopy equivalent.
Going one dimensional higher. The theory of (3 + 1)-TQFTs, however, is not under-
stood as well as its counter-part in (2 + 1) dimension. The Dijkgraaf-Witten invariant
2
CHAPTER 1. INTRODUCTION
[20] in (3 + 1) dimension, as well as in other dimensions, measures the number of group
morphisms from the fundamental group of a 4-manifold to a given ﬁnite group. L. Crane
and I. Frankel constructed a 4-manifold invariant out of some algebraic structure, called
Hopf categories, and they also proposed a construction of a family of Hopf categories [21].
In [22], L. Crane and D. Yetter gave a state-sum invariant of 4-manifolds (Crane-Yetter
invariant) using a semi-simple sub-quotient of the category of representations of Uq(sl2)
for q a certain principal root of unity. L. Crane, L. Kauﬀman and D. Yetter generalized
the construction for a ribbon fusion category [23].1 The Walker-Wang model in [24] is a
Hamiltonian realization in 3d of the Crane-Yetter invariant. The modular Crane-Yetter
invariant, which is obtained from a modular tensor category, turns out to be a function of
the Euler characteristics and the signature [25], and thus is a classical invariant. From a
diﬀerent direction, D. Yetter gave a construction of (3+1)-TQFT from homotopy 2-types
[26], which is equivalent to a crossed module or a categorical group. Along a similar line,
A. Kapustin [27] and M. Mackaay [28] obtained 4-manifold invariants from 2-groups with
some additional structures. More recently, R. Kashaev produced a (3 + 1)-TQFT out
of a cyclic group ZN [29]. Although simple and elementary, it is not clear if Kashaev’s
invariant is related with those from categorical constructions.
Now we focus a little more on categorical state-sum constructions of TQFTs.
In
(2+1) dimension, the typical state-sum model (Turaev-Viro invariant) involves a spherical
fusion (1-)category. Thus in (3 + 1) dimension, one would expect there to be a ‘spherical
fusion 2-category’ and all known categorical constructions of 4d-invariants should be
a special case.
Modoidal 2-categories are deﬁned in [30], and monoidal 2-categories
with duals are given in [31]. In [32], M. Mackaay proposed a deﬁnition of spherical 2-
categories by introducing certain extra structures based on monoidal 2-categories with
1In [23], it was called a semi-simple tortile category. The generalized invariant is still called in the
Crane-Yetter invariant.
3
CHAPTER 1. INTRODUCTION
duals. However, as explained later, his deﬁnition is too restrictive and excluded many
interesting examples. Therefore, the question of what should be a ‘good’ deﬁnition of
spherical fusion 2-categories is still open.
Here we will not try to deﬁne spherical 2-categories. Rather, we consider a special
class, but still more general than those studied in literature along this line, of ‘properly
deﬁned spherical 2-categories’. The main result of this thesis is a state-sum construction
of 4-manifold invariants out of a G-crossed braided spherical fusion category (G-BSFC)
C×
G for G a ﬁnite group. G-crossed braided (spherical) fusion categories were studied
in [33][34][35][36] and also have applications in condensed matter physics [37]. Roughly
speaking, a G-BSFC is a G-graded spherical fusion category with a G-action and a G-
crossed braiding which satisfy certain compatible conditions. Note that a G-BSFC is
in general not a braided tensor category. Our construction is a state-sum model and a
natural generalization of the Tuaev-Viro invariant from (2 + 1) to (3 + 1). Although in
this thesis, we only describe the invariants for closed 4-manifolds, it is straight forward
to extend it to 3-manifolds and produce a (3 + 1)-TQFT.
It can be shown that out of a G-BSFC one can construct a monoidal 2-category with
some extra structures (See Section 2.3). One might claim that these extra structures
make it into a ‘spherical fusion 2-category’. However, they violate some conditions in
the deﬁnition of a spherical 2-category given in [32]. This suggests that the deﬁnition
of spherical 2-categories might need to be revised. Also it means that our result is not
included in [32].
The invariant from a G-BSFC generalizes most known categorical invariants in liter-
ature. If G is the trivial group, then C×
G is just a ribbon fusion category and the invariant
we get is just the Crane-Yetter invariant. If C×
G is obtained from a crossed module (See
Section 3.3.2), then we get the Yetter’s invariant from homotopy 2-types, a special case
of which is the untwisted Dijkgraaf-Witten invariant. Our invariant also includes some
4
CHAPTER 1. INTRODUCTION
cases of the invariant in [28][27]. Moreover, if the G-grading is concentrated on the trivial
sector, namely, only the sector indexed by the trivial group element is non-trivial, then
a 4-cocycle in H4(G, U(1)) can be introduced into the construction to produce another
invariant, which reduces to the twisted Dijkgraaf-Witten invariant as a special case. It
remains to see if the invariant from G-BSFCs are strictly stronger than those invariants
and if it has the power to detect smooth structures.
Lastly, G-BSFCs are not rare. In [35][38][39], it was proved that equivalent classes of
G-BSFCs are in one-to-one correspondence, by equivariatization and de-equivariatization,
with equivalent classes of spherical braided categories containing Rep(G) as a subcate-
gory. Also, given a group morphism from G to the group of automorphisms of a unitary
braided fusion category C, if certain obstructions vanish, then C can be extended to a
unitary G-crossed braided fusion category, which is also a G-BSFC, with C as the sector
indexed by the trivial group element [33].
The structure of the thesis is organized as follows. In Chapter 2, we give a review
of category theories. We start from monoidal categories and then introduce diﬀerent
structures including dual, braiding, G-action, etc. (Section 2.1). G-BSFCs are discussed
in Section 2.2. In Section 2.3, it is shown that with a G-BSFC one can construct a
monoidal 2-category with duals and certain extra structures. In Chapter 3, we deﬁne
the invariant of 4-manifolds out of a G-BSFC.
Section 3.1 provides three equivalent
deﬁnitions of the invariant, which are deﬁned on triangulated 4-manifolds. In Section
3.2, a formula of the invariant is expressed in terms of the data of a G-BSFC such as the
F-symbols, R-symbols, etc. In Section 3.3, several examples are discussed. In particular,
it shows that some of known invariants arise naturally as special cases of our invariant.
Section 3.4 gives a variation of the invariant. Chapter 4 contains a complete proof that
the invariant deﬁned above is indeed an ‘invariant’. Finally, in Chapter 5 we point out
some open questions/directions for future study.
5
Chapter 2
