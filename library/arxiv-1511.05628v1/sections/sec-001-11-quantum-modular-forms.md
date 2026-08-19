---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-001-11-quantum-modular-forms
section_title: "Quantum modular forms"
section_number: 1.1
pages: 1-4
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
1.2. Zagier’s Quantum Modularity Conjecture 3
2. The deﬁnition of φγ,ζ 4
2.1. Ideal triangulations and Neumann-Zagier data 4
2.2. The 1-loop invariant at level k 6
2.3. The n-loop invariants at level k for n≥ 2 7
2.4. Feynman diagrams for the n-loop invariant 8
2.5. The 2-loop invariant in detail 9
2.6. The 3-loop invariant 11
2.7. Matching with the numerical asymptotics of the Kashaev invariant 11
2.8. Topological invariance 11
3. Proofs 12
3.1. Proof of Theorem 2.6 12
3.2. Some identities of the cyclic dilogarithm 14
3.3. Proof of Theorem 2.2 14
4. Complex Chern-Simons theory 15
4.1. Basic structure 15
Date: November 17, 2015.
Key words and phrases: knots, quantum modular forms, quantum modularity conjecture, cusped hyperbolic
manifolds, volume, complex Chern-Simons theory, Kashaev invariant, gluing equations, Neumann-Zagier
equations, Neumann-Zagier datum, Nahm series, hyperbolic geometry, ideal triangulations, 1-loop, torsion,
quantum dilogarithm, state-integral, perturbation theory, Feynman diagrams, formal Gaussian integration,
cyclic quantum dilogarithm, number ﬁeld.
1
arXiv:1511.05628v1  [math.GT]  18 Nov 2015
2 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
4.2. A singular limit 16
4.3. State integrals 17
4.4. Derivation of the torsion 19
4.5. Ambiguities 20
5. Computations 20
5.1. How the data was computed 20
5.2. A sample computation 21
6. Data 22
6.1. The 4 1 knot 22
6.2. The 5 2 knot and its partner, the (−2, 3, 7) pretzel knot 25
6.3. The 6 1 knot 32
6.4. The ( −2, 3,−3) and the (−2, 3, 9) partner pretzel knots 35
6.5. The 9 12 knot 38
Acknowledgements 39
References 39
1. Introduction
1.1. Quantum modular forms. Quantum modular forms are fascinating objects intro-
duced by Zagier [Zag10]. In the simplest formulation, a quantum modular form is a complex
valued function f on the set of complex roots of unity that comes equipped with a suitable
formal power series expansion φζ(ℏ)∈ C[ [ℏ] ] at each complex root of unity ζ. Usually f is
given explicitly. On the other hand, the power series φζ, although uniquely determined by
f, are not easy to obtain.
One of the most interesting examples of quantum modular forms is conjectured to be
the logarithm of the Kashaev invariant of a knot. This is Zagier’s Quantum Modularity
Conjecture [Zag10]. Evidence for this conjecture includes ample numerical computations
performed by Zagier and the ﬁrst author [GZ] as well as a proof in the case of the 4 1
knot [GZ].
Our goal is to construct an explicit formula for the power series that appear in the Quantum
Modularity Conjecture of a knot. We highlight some features of our results.
(a) The formulas for our series φγ,ζ(ℏ) use as input a complex root of unity ζ and Neumann-
Zagier datum γ, i.e., an ideal triangulation of a knot complement and a geometric solution
to the gluing equations. Such a datum is readily available from SnapPy.
(b) Our series have arithmetically interesting coeﬃcients; see Theorems 2.2 and 2.6.
(c) Our series lead to exact computations that match the numerically computed asymptotics
of the Kashaev invariant at various roots of unity. The details of our computations are given
in Section 5.
(d) Our construction is motivated by the analysis of singular limits in complex Chern-Simons
theory, with gauge groupSL(2, C). Complex Chern-Simons theory depends on two coupling
constants or levels (k,σ )∈ (Z, C) [Wit91], and the series φγ,ζ(ℏ) at ζ =e2πi/k is obtained by
sending σ→ k (while keeping k ﬁxed). We describe this limit in greater detail in Section
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY 3
4, after introducing the deﬁnition of φγ,ζ(ℏ) and proving its number-theoretic properties in
Sections 2-3.
1.2. Zagier’s Quantum Modularity Conjecture. The Kashaev invariant of a knotK is
a sequence of complex numbers ⟨K⟩N indexed by a positive integer N [Kas95]. Murakami-
Murakami [MM01] identiﬁed the Kashaev invariant with an evaluation of the colored Jones
polynomial JK,N(q)∈ Z[q±1] colored by the N-dimensional irreducible representation of sl2:
⟨K⟩N =JK,N(e
2πi
N ).
Identifying the set of complex roots of unity withQ/Z, the Kashaev invariant can be extended
to a translation-invariant function on Q by
(1) J0
K : Q−→ C, α ↦→J0
K(α) =JK,den(α)(e2πiα)
where den(a/c) =c whenc> 0 anda,c are coprime. Obviously, we haveJ0
K(α) =J0
K(α + 1)
for α∈ Q.
The Quantum Modularity Conjecture [Zag10] predicts for each complex root of unity ζ
the existence of a formal power series φK,ζ(ℏ)∈ C[ [ℏ] ] with the following property. Choose
any
(
a b
c d
)
∈ SL(2, Z) with c> 0 such that ζ = exp( 2πia
c ). Let X→∞ in a ﬁxed coset of
Q/Z, and set ℏ = 2πi/(cX +d). Then there is an asymptotic expansion
(2) J0
K
(aX +b
cX +d
)
∼J0
K(X)
( 2πi
ℏ
)3/2
eV/(cℏ)φK,ζ(ℏ)
whereV is the complex volume ofK. Furthermore, the coeﬃcients ofφK,ζ(ℏ) are conjectured
to be algebraic integers of the following form:
(a) The coeﬃcients of φ+
K,ζ(ℏ) = φK,ζ(ℏ)/φK,ζ(0) should be elements of the ﬁeld FK(ζ),
where FK is the trace ﬁeld of K.
(b) The constant term (under some mild assumptions onFK(ζ)) should factor as follows:
(3) φK,k(0) =φK,1(0) k√εKβK,k
whereφK,1(0)2∈FK(ζ),εK is a unit (i.e., an algebraic integer of norm ±1) in FK(ζ)
that depends only on the element of the Bloch group ofK (andζ), andβK,k∈FK(ζ).
The above unit is studied in [CGZ]. For a detailed discussion of the Quantum Modularity
Conjecture, we refer the reader to [Zag10] and also [GZ] where a proof for the case of the 4 1
knot (the simplest hyperbolic knot) is given.
The Quantum Modularity Conjecture includes the Volume Conjecture of Kashaev [Kas95]
and its reﬁnement to all orders of 1 /N conjectured by Gukov [Guk05] and by the second
author [Gar08]. Indeed, when ( a b
c d) = ( 0−1
1 0 ) and X =N∈ N, we obtain that
(4) ⟨K⟩N =J0
K
(
− 1
N
)
∼N 3/2eNV/ (2πi)φK,1
(2πi
N
)
.
The second author and Zagier numerically computed the Kashaev invariant and its asymp-
totics, exposing several coeﬃcients of the seriesφK,ζ(ℏ) for many knots, and giving numerical
conﬁrmation of the Modularity Conjecture. The results are summarized in [GZ].
4 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
A deﬁnition of the power series φK,ζ(ℏ) in the Quantum Modularity Conjecture was miss-
ing, though. Motivated by this problem, in an earlier publication [DG13a] (inspired by
[DGLZ09]) the authors assigned to a Neumann-Zagier datum γ (i.e., to an ideal triangula-
tion of the knot complement, a geometric solution to the gluing equations and a ﬂattening)
a power series φγ,1(ℏ) and conjectured that it coincides with the series φK,1(ℏ). One advan-
tage of the series φγ,1(ℏ) is the exact computation of its coeﬃcients using standard SnapPy
methods [CDW], together with ﬁnite sums of Feynman diagrams. In all cases we matched
those coeﬃcients with the numerically computed values of [GZ]. In [DG13a], it was shown
that the constant term of φγ,1(ℏ) is a topological invariant, but to date the full topological
invariance ofφγ,1(ℏ) is unknown.
Finally, we ought to point out a close connection between our series φγ,ζ(ℏ) and
• The radial asymptotics of Nahm sums at complex roots of unity. This connection
was observed atζ = 1 during conversations of the second author and Zagier in Bonn
in the spring of 2012.
• The evaluations of one-dimensional state-integrals at rational points [GK13, GK14].
• The formula for an algebraic unit attached to an element of the Bloch group of a
number ﬁeld and a complex root of unity, appearing in (3) [CGZ].
These connections are not a coincidence; rather, they close a circle of ideas motivated by
several years of work on asymptotics of hypergeometric sums, quantum invariants, and their
geometry and physics.
2. The definition of φγ,ζ
