---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
arXiv:math/0006057v2  [math.QA]  10 Jun 2000
FINITE QUANTUM GROUPOIDS AND THEIR APPLICATIONS
DMITRI NIKSHYCH AND LEONID VAINERMAN
Abstract. We give a survey of the theory of ﬁnite quantum groupoids (weak
Hopf algebras), including foundations of the theory and applications to ﬁnite
depth subfactors, dynamical deformations of quantum groups, and invariants
of knots and 3-manifolds.
Contents
1.
Introduction
2
2.
Deﬁnitions and Examples
3
2.1.
Deﬁnition of the quantum groupoid
3
2.2.
Counital maps and subalgebras
4
2.3.
Properties of the antipode
5
2.4.
The dual quantum groupoid
7
2.5.
Examples : groupoid algebras and their duals
7
2.6.
Examples : quantum transformation groupoids
8
2.7.
Examples : Temperley-Lieb algebras
8
2.8.
Other versions of a quantum groupoid
9
3.
Integrals and semisimplicity
10
3.1.
Integrals in quantum groupoids
10
3.2.
Hopf modules
11
3.3.
Maschke’s Theorem
12
4.
Actions and smash products
13
4.1.
Module and comodule algebras
13
4.2.
Smash products
13
4.3.
Duality for actions
14
5.
Representation category of a quantum groupoid
14
5.1.
Deﬁnition of Rep(H)
14
5.2.
Quasitriangular quantum groupoids
16
5.3.
The Drinfeld double
19
5.4.
Ribbon quantum groupoids
20
5.5.
Towards modular categories
21
6.
Twisting and dynamical quantum groups
22
6.1.
Twisting of quantum groupoids
23
6.2.
Dynamical twists of Hopf algebras
24
6.3.
Dynamical twists for Uq(g) at roots of 1
25
Date: June 7, 2000.
The ﬁrst author thanks P. Etingof for numerous stimulating discussions on quantum groupoids
and to MIT for the hospitality during his visit.
The second author is grateful to M. Enock, V. Turaev and J.-M. Vallin for many valuable
discussions and to l’Universit´e Louis Pasteur (Strasbourg) for the kind hospitality during his work
on this survey.
1
2
DMITRI NIKSHYCH AND LEONID VAINERMAN
7.
Semisimple and C∗-quantum groupoids
27
7.1.
Deﬁnitions
27
7.2.
Existence of the Haar integral
28
7.3.
C∗-quantum groupoids
29
7.4.
C∗-quantum groupoids and unitary modular categories
31
8.
C∗-quantum groupoids and subfactors : the depth 2 case
31
8.1.
Actions of C∗-quantum groupoids on von Neumann algebras
32
8.2.
Construction of a C∗-quantum groupoid from a depth 2 subfactor
33
8.3.
Action on a subfactor
35
9.
C∗-quantum groupoids and subfactors : the ﬁnite depth case
36
9.1.
A Galois correspondence
37
9.2.
Bimodule categories
38
9.3.
Principal graphs
41
References
42
1. Introduction
By quantum groupoids we understand weak Hopf algebras introduced in [BNSz],
[BSz1], [N]. These objects generalize Hopf algebras (in fact, many Hopf-algebraic
concepts can be extended to the quantum groupoid case) and usual ﬁnite groupoids
(see [NV1] for discussion). Every quantum groupoid has two canonical subalgebras
that play the same role as the space of units in a groupoid and projections on these
subalgebras generalizing the source and target maps in a groupoid. We use the
term “quantum groupoid” instead of “weak Hopf algebra” to stress this similarity
that leads to many interesting constructions and examples.
Our initial motivation for studying quantum groupoids in [NV1], [NV2],[N1]
was their connection with depth 2 von Neumann subfactors, ﬁrst mentioned in
[O2], which was also one of the main topics of [BNSz], [BSz1], [BSz2], [NSzW]. It
was shown in [NV2] that quantum groupoids naturally arise as non-commutative
symmetries of subfactors, namely if N ⊂M ⊂M1 ⊂M2 ⊂. . . is the Jones
tower constructed from a ﬁnite index depth 2 inclusion N ⊂M of II1 factors, then
H = M ′ ∩M2 has a canonical structure of a quantum groupoid acting outerly on
M1 such that M = M H
1
and M2 = M1>⊳H, moreover bH = N ′ ∩M1 is a quantum
groupoid dual to H.
In [NV3] we extended this result to show that quantum groupoids give a de-
scription of arbitrary ﬁnite index and ﬁnite depth II1 subfactors via a Galois cor-
respondence and explained how to express subfactor invariants such as bimodule
categories and principal graphs in quantum groupoid terms. Thus, in this respect
quantum groupoids play the same role as Ocneanu’s paragroups [O1], [D].
Quantum groupoids also appear naturally in the theory of dynamical deforma-
tions of quantum groups [EV], [Xu]. It was shown in [EN] that for every simple Lie
algebra g the corresponding Drinfeld-Jimbo quantum group Uq(g) for q a primitive
root of unity has a family of dynamical twists that give rise to self-dual ﬁnite quan-
tum groupoids. To every such a twist one can associate a solution of the quantum
dynamical Yang-Baxter equation [ES].
FINITE QUANTUM GROUPOIDS AND THEIR APPLICATIONS
3
As in the case of Hopf algebras, the representation category Rep(H) of a quantum
groupoid H is a monoidal category with duality. Existence of additional (quasitrian-
gular, ribbon, or modular) structures on H makes Rep(H), respectively, braided,
ribbon, or modular [NTV]. It is well known [RT], [T], that such categories give rise
to invariants of knots and 3-manifolds.
The survey is organized as follows.
In Section 2 we give basic deﬁnitions and examples of ﬁnite quantum groupoids,
discuss their fundamental properties (following [BNSz] and [NV1]) and relations
with other versions of quantum groupoids.
The exposition of the theory of integrals in Section 3 follows [BNSz] and is
similar to the Hopf algebra case [M]. The main results here are extensions of the
fundamental theorem for Hopf modules and the Maschke theorem. The latter gives
an equivalence between existence of normalized integrals and semi-simplicity of a
quantum groupoid.
In Section 4 we deﬁne the notions of action and smash product and extend
the well known Blattner-Montgomery duality theorem for Hopf algebra actions to
quantum groupoids (see [N2]).
In Section 5 we describe monoidal structure and duality on the representation
category of a quantum groupoid ([BSz2] and [NTV]). Then we distinguish special
cases of quantum groupoids leading to braided, ribbon, and modular categories of
representations.
We also develop the Drinfeld double construction and emphasize the role of fac-
torizable quantum groupoids in producing modular categories (see [NTV]). Section
6 contains an extension of the Drinfeld twisting procedure to quantum groupoids
and construction of a quantum groupoid via a dynamical twisting of a Hopf algebra.
Important concrete examples of such twistings are dynamical quantum groups at
roots of 1 [EN].
Semisimple and C∗-quantum groupoids are analyzed in Section 7.
Following
[BNSz], our discussion is concentrated around the existence of the Haar integral in
connection with a special implementation of the square of the antipode.
Sections 8 and 9 are devoted to the description of ﬁnite index an ﬁnite depth
subfactors via crossed products of II1 factors with C∗-quantum groupoids. These
results were obtained in [NV2], [NV3] and partially in [N1], [NSzW].
2. Definitions and Examples
In this section we give deﬁnitions and discuss basic properties of ﬁnite quantum
groupoids. Most of the material presented here can be found in [BNSz] and [NV1].
Throughout this paper we use Sweedler’s notation for comultiplication, writing
∆(b) = b(1) ⊗b(2). Let k be a ﬁeld.
