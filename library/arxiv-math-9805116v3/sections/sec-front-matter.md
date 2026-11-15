---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
arXiv:math/9805116v3  [math.QA]  8 Jun 1999
Weak Hopf Algebras
I. Integral Theory and C∗-structure
Gabriella B¨ohm 1, Florian Nill 2, Korn´el Szlach´anyi 3
Abstract
We give an introduction to the theory of weak Hopf algebras proposed recently as a
coassociative alternative of weak quasi-Hopf algebras. We follow an axiomatic approach
keeping as close as possible to the ”classical” theory of Hopf algebras. The emphasis is put
on the new structure related to the presence of canonical subalgebras AL and AR in any
weak Hopf algebra A that play the role of non-commutative numbers in many respects. A
theory of integrals is developed in which we show how the algebraic properties of A, such
as the Frobenius property, or semisimplicity, or innerness of the square of the antipode,
are related to the existence of non-degenerate, normalized, or Haar integrals. In case of
C∗-weak Hopf algebras we prove the existence of a unique Haar measure h ∈A and of a
canonical grouplike element g ∈A implementing the square of the antipode and factorizing
into left and right elements g = gL g−1
R , gL ∈AL, gR ∈AR. Further discussion of the
C∗-case will be presented in Part II.
To appear in J. Algebra
1 Research Institute for Particle and Nuclear Physics, Budapest, H-1525 Budapest 114, P.O.B. 49, Hungary
E-mail: BGABR@rmki.kfki.hu
Supported by the Hungarian Scientiﬁc Research Fund, OTKA – T 016 233
2 Institut f¨ur Theoretische Physik, FU–Berlin Arnimallee 14, D-14195 Berlin, Germany
E-mail: NILL@mail.physik.fu-berlin.de
Supported by the DFG, SFB 288 ”Diﬀerentialgeometrie und Quantenphysik”
3 Research Institute for Particle and Nuclear Physics, Budapest, H-1525 Budapest 114, P.O.B. 49, Hungary
E-mail: SZLACH@rmki.kfki.hu
Supported by the Hungarian Scientiﬁc Research Fund, OTKA – T 020 285.
Contents
1
Introduction
2
The Weak Hopf Calculus
4
2.1
The axioms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.2
Weak bialgebras
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.3
Weak Hopf algebras
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.4
The ”trivial” representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3
Weak Hopf Modules and Integral Theory
14
3.1
Integrals in weak Hopf algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
3.2
Weak Hopf modules
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
3.3
Restrictions on the algebraic structure . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
3.4
Non-degenerate integrals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
3.5
2-sided non-degenerate integrals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.6
Haar integrals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
4
C∗-Weak Hopf Algebras
31
4.1
First consequences of the C∗-structure . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
4.2
The Haar measure and selfduality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
4.3
The canonical grouplike element
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
A Appendix: The Weak Hopf Algebra B ⊗Bop
38
References
39
1
Introduction
Weak Hopf algebras have been proposed recently [2, 20, 14] as a new generalization of ordinary
Hopf algebras that replaces Ocneanu’s paragroup [16], in the depth 2 case, with a concrete
”Hopf algebraic” object. The earlier proposals of face algebras [8] or quantum groupoids [17]
are actually weak Hopf algebras even if not the most general ones. Also, the (ﬁnite dimensional)
generalized Kac algebras of T. Yamanouchi [25] are weak Hopf algebras in our sense [14], albeit
with an involutive antipode.
In contrast to other Hopf algebraic constructions such as the quasi Hopf algebras [6] or
the weak quasi Hopf algebras and rational Hopf algebras [11, 22, 7] weak Hopf algebras are
coassociative. This allows one to deﬁne actions, coactions, and crossed products as easily as in
the Hopf algebra case. On the other hand weak Hopf algebras have ”weaker” axioms related
to the unit and counit: The comultiplication is non-unital, ∆(1)̸ = 1 ⊗1 (like in weak quasi
Hopf algebras) and the counit is only ”weakly” multiplicative, ε(xy) = ε(x1(1))ε(1(2)y). This
kind of ”weakness” is the ”strength” of weak Hopf algebras because it allows (even in the ﬁnite
dimensional and semisimple case) the weak Hopf algebra to possess non-integral (quantum)
dimensions.
Thus weak Hopf algebras are not special cases of weak quasi Hopf algebras and also not
more general than them. Nevertheless, in situations where only the representation category of
the quantum group matters, these two concepts are equivalent. This is, of course, not surprising
in view of MacLane’s Theorem on the equivalence of relaxed and strict monoidal categories
[12]. In fact not all of the potential of this theorem is utilized by weak Hopf algebras because
their representation category is not quite strict: Only the associator is trivial but not the left
and right isomorphisms of the monoidal unit. Although a general analysis clarifying the role
2
of representation categories of weak Hopf algebras within the set of monoidal categories is still
missing the examples constructed in [2] using Ocneanu’s cocycle suggest that they play a rather
fundamental role, as long as they can accomodate to arbitrary 6j-symbols.
So far weak Hopf algebras have been considered only under the additional assumption of
ﬁnite dimensionality. Although a good deal of the results can be generalized to the inﬁnite
dimensional case, ﬁnite dimension is particularly attractive because it implies selfduality. Just
like ﬁnite Abelian groups or ﬁnite dimensional Hopf algebras, the ﬁnite dimensional weak Hopf
algebras (WHA) are selfdual in the following sense. If A is a WHA then its dual space ˆA is
canonically equipped with a weak Hopf algebra structure. Furthermore this duality is reﬂexive,
( ˆA)ˆ ∼= A. This is a feature which makes WHAs more natural objects of study than either
ﬁnite (non-Abelian) groups or ﬁnite dimensional (weak) quasi Hopf algebras.
The main motivation for studying WHAs comes from quantum ﬁeld theory and operator
algebras and consists roughly of the following two symmetry problems.
I. If N ⊂M is an inclusion of algebras satisfying certain conditions then ﬁnd a (unique) ”quan-
tum group” G and an action of G on M such that N = MG, the invariant subalgebra.
II. The dual problem is to ﬁnd a ”quantum group” ˆG acting on N such that M is isomorphic
to the crossed product N >⊳ˆG.
Of course, determining the appropriate notion of ”quantum group”, as well as its action, is
part of the problem. If N ⊂M is a ﬁnite index irreducible depth 2 inclusion of von Neumann
factors then the answer is known by [10] to be a ﬁnite dimensional C∗-Hopf algebra. In [15]
we will show that if we allow the inclusion to be reducible and N and M to have arbitrary
ﬁnite dimensional centers then the appropriate ”quantum group” is a C∗-weak Hopf algebra.
Even in case of inclusions of certain associative (non-∗) algebras the notion of a WHA over an
arbitrary ﬁeld K, introduced in this paper, may provide a useful invariant.
In Section 2 we introduce the axioms of weak bialgebras and weak Hopf algebras over
a ﬁeld K and discuss their consequences. If K =
|C, the complex ﬁeld, then these axioms
are equivalent to those of [20]. The present axioms have the advantage of being manifestly
selfdual and almost each of them having an ancestor among the Hopf algebra axioms which
it generalizes.
In discussing the consequences particular attention is paid to the canonical
subalgebras AL and AR present in any WHA both of which reducing to the scalars K1 if A
is a Hopf algebra. From many point of views these subalgebras behave like non-commutative
generalizations of numbers. Just to mention some: 1. AL and AR are separable K-algebras. 2.
The trivial left A-module is a representation on the K-space AL (or on AR). 3. The dual weak
Hopf algebra ˆA have left and right subalgebras ˆAL and ˆAR that are isomorphic to AR and AL,
respectively. Of course, in order to realize the idea of AL and AR being ”non-commutative
numbers” one should completely get rid of the ﬁeld K from the outset. As yet we have no
concrete proposal for this scenario.
Section 3 is devoted to the study of integrals in weak Hopf algebras. Using the notion of
weak Hopf modules which is a generalization of the Hopf modules [1, 19] we show that non-zero
integrals exist. A weak Hopf version of Maschke’s Theorem characterizes semisimple WHAs
as those possessing normalized integrals. An other important class of WHAs are those which
are Frobenius algebras. They are characterized by possessing non-degenerate left integrals.
This class is a selfdual class by the Duality Theorem of non-degenerate integrals. We conclude
with giving necessary and suﬃcient criteria for the existence of Haar integrals, i.e. normalized
non-degenerate 2-sided integrals in a WHA.
Section 5 contains the basic properties of weak C∗-Hopf algebras such as the existence of
a Haar integral h and a canonical grouplike element g ≥0 implementing S2 and the modular
automorphism of the Haar measure. As a consequence of the existence of Haar measures the
dual of a C∗-weak Hopf algebra is a C∗-weak Hopf algebra again. Further analysis of C∗-WHAs
will be given in Part II where we discuss the representation category and a notion of dimension
which turns out to be non-commutative in case of solitonic representations [3] .
2
The Weak Hopf Calculus
