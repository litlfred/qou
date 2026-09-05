---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-007-4-c-weak-hopf-algebras-31
section_title: "C∗-Weak Hopf Algebras 31"
section_number: 4
pages: 2-3
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
4.1 First consequences of the C∗-structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2 The Haar measure and selfduality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.3 The canonical grouplike element . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
A Appendix: The Weak Hopf Algebra B ⊗Bop 38
References 39
1 Introduction
Weak Hopf algebras have been proposed recently [2, 20, 14] as a new generalization of ordinary
Hopf algebras that replaces Ocneanu’s paragroup [16], in th e depth 2 case, with a concrete
”Hopf algebraic” object. The earlier proposals of face algebras [8] or quantum groupoids [17]
are actually weak Hopf algebras even if not the most general o nes. Also, the (ﬁnite dimensional)
generalized Kac algebras of T. Yamanouchi [25] are weak Hopf algebras in our sense [14] , albeit
with an involutive antipode.
In contrast to other Hopf algebraic constructions such as th e quasi Hopf algebras [6] or
the weak quasi Hopf algebras and rational Hopf algebras [11, 22, 7] weak Hopf algebras are
coassociative. This allows one to deﬁne actions, coactions, and crossed pr oducts as easily as in
the Hopf algebra case. On the other hand weak Hopf algebras ha ve ”weaker” axioms related
to the unit and counit: The comultiplication is non-unital, ∆(1) ⁄= 1 ⊗ 1 (like in weak quasi
Hopf algebras) and the counit is only ”weakly” multiplicati ve, ε(xy) = ε(x1(1))ε(1(2)y). This
kind of ”weakness” is the ”strength” of weak Hopf algebras be cause it allows (even in the ﬁnite
dimensional and semisimple case) the weak Hopf algebra to po ssess non-integral (quantum)
dimensions.
Thus weak Hopf algebras are not special cases of weak quasi Ho pf algebras and also not
more general than them. Nevertheless, in situations where o nly the representation category of
the quantum group matters, these two concepts are equivalen t. This is, of course, not surprising
in view of MacLane’s Theorem on the equivalence of relaxed an d strict monoidal categories
[12]. In fact not all of the potential of this theorem is utili zed by weak Hopf algebras because
their representation category is not quite strict: Only the associator is trivial but not the left
and right isomorphisms of the monoidal unit. Although a gene ral analysis clarifying the role
2
of representation categories of weak Hopf algebras within t he set of monoidal categories is still
missing the examples constructed in [2] using Ocneanu’s coc ycle suggest that they play a rather
fundamental role, as long as they can accomodate to arbitrar y 6j-symbols.
So far weak Hopf algebras have been considered only under the additional assumption of
ﬁnite dimensionality. Although a good deal of the results ca n be generalized to the inﬁnite
dimensional case, ﬁnite dimension is particularly attract ive because it implies selfduality. Just
like ﬁnite Abelian groups or ﬁnite dimensional Hopf algebra s, the ﬁnite dimensional weak Hopf
algebras (WHA) are selfdual in the following sense. If A is a WHA then its dual space ˆA is
canonically equipped with a weak Hopf algebra structure. Fu rthermore this duality is reﬂexive,
( ˆA)ˆ ∼= A. This is a feature which makes WHAs more natural objects of st udy than either
ﬁnite (non-Abelian) groups or ﬁnite dimensional (weak) qua si Hopf algebras.
The main motivation for studying WHAs comes from quantum ﬁel d theory and operator
algebras and consists roughly of the following two symmetry problems.
I. IfN ⊂M is an inclusion of algebras satisfying certain conditions t hen ﬁnd a (unique) ”quan-
tum group” G and an action of G on M such that N =MG, the invariant subalgebra.
