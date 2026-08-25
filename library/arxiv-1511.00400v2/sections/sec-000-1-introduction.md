---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
2 Combinatorial and analytic torsions 4
2.1 Combinatorial torsion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.1.1 Torsion of a chain complex . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.1.2 Twisted chain complexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Geometric properties of combinatorial torsion . . . . . . . . . . . . . . . . . . . . . 7
2.2.1 Mayer-Vietoris . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.2 Polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.3 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3 Analytic torsion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3 T orsion of hyperbolic three-manifold with representatio ns in SL2( C) 15
3.1 Torsions from lifts of the holonomy representation . . . . . . . . . . . . . . . . . . 16
3.1.1 Lifts of the holonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.1.2 Torsions for closed 3-manifolds . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.1.3 Cusped hyperbolic 3-manifolds . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.1.4 The twisted polynomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.2 Torsion on the variety of characters . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.2.1 The distinguished curve of characters . . . . . . . . . . . . . . . . . . . . . 19
3.2.2 Torsion on the distinguished curve of characters . . . . . . . . . . . . . . . 20
3.2.3 Dehn ﬁlling space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2.4 Torsion for Dehn ﬁllings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.2.5 Branched coverings on the ﬁgure eight . . . . . . . . . . . . . . . . . . . . . 25
∗Partially supported by Mineco through grant MTM2012-34834
1
4 T orsions for higher dimensional representations of hyper bolic three-manifolds 26
4.1 Representations of SL 2( C) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2 Higher torsions for closed manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3 Functions on the variety of characters . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.3.1 Generic cohomology on the distinguished component . . . . . . . . . . . . 29
4.3.2 Higher torsions on the variety of characters . . . . . . . . . . . . . . . . . . 30
4.4 Evaluation at the holonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.4.1 Cohomolgy at the character of the holonomy . . . . . . . . . . . . . . . . . 32
4.4.2 Torsion at the characters of the holonomy . . . . . . . . . . . . . . . . . . 33
4.4.3 Dehn ﬁlling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.5 Quantum invariants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5 Representations in PSLn+ 1( C) and the adjoint 36
5.1 Local parameters and change of curve . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.2 An example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.2.1 Computations for X( M 3,PSL2( C)) . . . . . . . . . . . . . . . . . . . . . . 42
5.2.2 Computations for X( M 3,PSL3( C)) . . . . . . . . . . . . . . . . . . . . . . 43
Appendix A Not approximating the trivial representation 44
Appendix B Cohomology on the variety or characters 45
B.1 The complete structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
B.1.1 The ﬁnite volume case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
B.1.2 A basis in cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
B.2 Generic representations in the distinguished componen t. . . . . . . . . . . . . . . 49
1 Introduction
The goal of this paper is to survey some results on Reidemeister tor sions of
orientable, hyperbolic three-manifolds of ﬁnite volume. Torsions ar e viewed
as invariants of hyperbolic manifolds and also as functions on the var iety of
SL2(C)-characters.
The paper uses combinatorial torsion, though some relevant deve lopments
described here are proved using analytic torsion, which is brieﬂy men tioned.
No details on other kinds of torsion are provided, like L2-torsion. There are
remarkable recent surveys on twisted Alexander polynomials [69, 3 3] and on
abelian torsions [59]. There are also the classical surveys of Milnor [68 ] and
Turaev [95], as well as the books by Turaev [96, 97] and Nicolaescu [8 0].
Besides Section 2 (devoted to general tools on torsions), only orie ntable hy-
perbolic three-manifolds M 3 of ﬁnite volume are considered. The hyperbolic
structure is unique, by Mostow-Prasad theorem, so their holonom y is unique up
to conjugacy. It lifts to a representation in SL 2(C). The lift is naturally associ-
ated to a spin structure σ and it is acyclic, by a theorem of Raghunathan. Thus
this yields a topological invariant of the oriented manifold with a spin st ructure
(Deﬁnition 3.4 in the closed case and Deﬁnition 3.10 in the non-compact case):
τ (M 3, σ) ∈ C∗.
Its main properties are described, in particular, its behavior by Deh n ﬁlling
allows to construct sequences of closed manifolds whose volume sta ys bounded
but the torsion converges to inﬁnity (Corollary 3.28). This must be c ompared
with Theorem 3.7 (due to Bergeron and Venkatesh) on the asympto tic behavior
of torsions by coverings, that yields sequences of coverings M 3
n → M 3 so that
/divides.⊗lt1τ (M 3
n, σ)/divides.⊗lt1grows with the exponential of the volume of M 3
n. For those sequences
2
the injectivity radius converges to inﬁnity. Some results suggest t hat short
geodesics may play a role in the behavior of this torsion, for instance the surgery
formula, Proposition 3.25.
Additionally, the paper deals with ﬁnite dimensional irreducible repres enta-
tions of SL 2(C). Their composition with the lift of the holonomy provides a
family of invariants of a closed hyperbolic manifold, oriented and with a spin
structure. A remarkable theorem of M¨ uller relates the asymptot ic behavior of
those invariants with the volume (Theorem 4.5).
For simplicity, ﬁnite volume hyperbolic three-manifolds are assumed t o have
a single cusp. I am interested in the torsion as a function on the varie ty of
characters. The distinguished component is the component of the variety of
SL2(C)-characters that contains a lift of the holonomy of the complete st ructure.
It is easy to see that the torsion is a rational (meromorphic) funct ion on this
curve. It is shown here that for a knot exterior (more generally, f or a manifold
with ﬁrst Betti number 1), this torsion is a regular function (it has n o poles) on
the distinguished component.
The paper also discusses the functions obtained by composing the r epresen-
tation with the irreducible representations of SL 2(C). In particular the torsion
for the adjoint representation occurs in the volume conjecture, which is also
quickly mentioned but not analyzed.
Finally I describe the torsion of the adjoint representation as a fun ction on
the variety of characters in PSL n+1(C). I considered the case for PSL 2(C) in
[82] and Kitayama and Terashima discuss the general case for PSL n+1(C) in [55].
The relevant fact for this torsion is a result of Andr´ e Weil, that iden tiﬁes the
tangent space to the variety of characters with the ﬁrst cohomo logy group with
coeﬃcients twisted by the adjoint representation (under generic hypothesis). In
this way this torsion is related to local parameterizations of the def ormation
space, which amounts to choose peripheral curves. In particular , a formula for
the change of curve is provided, and this allows to deﬁne a volume for m under
some circumstances (not at the holonomy of the complete structu re, but for
instance for characters in SU (n)), as done by Witten for surfaces and Dubois for
knot exteriors and SU (2). In addition Weil’s interpretation allows to compute
the torsion for surface bundles from the tangent map of the mono dromy on the
deformation space of the ﬁbre.
The paper is organized as follows. Section 2 is devoted to the prelimina ries
