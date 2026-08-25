---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-001-11-chernsimons-theory-with-compact-and-complex-g
section_title: "Chern–Simons theory with compact and complex gauge group"
section_number: 1.1
pages: 1-4
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
1.2. Resurgence and the Stokes automorphism 3
1.3. A q-holonomic module of the partition function and its descendants 4
1.4. Perturbative series and their resurgence 6
1.5. Disclaimers 8
1.6. Further directions 9
Acknowledgements 9
2. Borel resummation and Stokes automorphisms 9
2.1. Borel resummation 9
2.2. Stokes automorphism 10
3. A summary of the story whenu = 0 12
3.1. The 41 knot whenu = 0 12
3.2. The 52 knot whenu = 0 17
4. Holonomic and elliptic functions inside and outside the unit disk 24
5. The 41 knot 25
5.1. Asymptotic series 25
5.2. Holomorphic blocks 27
5.3. Taylor series expansion atu = 0 32
5.4. Stokes matrices near u = 0 36
Date: 7 April 2021.
Key words and phrases:Chern-Simons theory, holomorphic blocks, state-integrals, knots, 3-manifolds,
resurgence, perturbative series, Borel resummation, Stokes automorphisms, Stokes constants,q-holonomic
modules, q-diﬀerence equations, DT-invariants, BPS states, peacocks, meromorphic quantum Jacobi forms.
1
arXiv:2012.00062v3  [math.GT]  7 Apr 2022
2 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
5.5. The Borel resummations of the asymptotic seriesΦ 39
5.6. Stokes matrices for realu 41
5.7. Numerical veriﬁcation 43
6. The 52 knot 45
6.1. Asymptotic series 45
6.2. Holomorphic blocks 47
6.3. Taylor series expansion atu = 0 54
6.4. Stokes matrices near u = 0 56
6.5. The Borel resummations of the asymptotic seriesΦ 60
6.6. Numerical veriﬁcation 61
7. One-dimensional state-integrals and their descendants 62
References 65
1. Introduction
1.1. Chern–Simons theory with compact and complex gauge group.Chern–Simons
gauge theory, introduced by Witten in his seminal paper [Wit89] as a quantum ﬁeld theory
proposal of the Jones polynomial [Jon87], remains one of the most fascinating quantum ﬁeld
theories. It gives a powerful framework to study the quantum topology of knots and three-
manifolds, and at the same time it provides a rich yet tractable model to explore general
aspects of quantum ﬁeld theories.
In [Wit89], Witten analyzed in detail Chern–Simons gauge theory with a compact gauge
group (such as SU(2)). Its partition function on a 3-manifold M with torus boundary
components depends on a quantized versionk∈ Z of Planck’s constant (or equivalently, on
a complex root of unitye2πik), as well as a discrete color (a ﬁnite dimensional irreducible
representation of SU(2)) per boundary component ofM. A more powerful Chern–Simons
theory with complex gauge group (such as SL(2, C )) was introduced by Witten [Wit91]
and developed extensively by Gukov [Guk05]. A key feature of complex Chern–Simons
theory is that the partition function ZM(u;τ) for a 3-manifold M with torus boundary
components depends analytically on a complex parameterτ (where τ = 1/k in the Chern–
Simons theory with compact gauge group) as well as on a complex parameteru per each
boundary component ofM that plays the role of the holonomy of a peripheral curve. The
analytic dependence ofZM(u;τ) on the parametersu andτ allows one to formulate questions
of complex analysis and complex geometry which would be diﬃcult, or impossible, to do in
Chern–Simons theory with compact gauge group.
There is a key diﬀerence between Chern–Simons theory with compact versus complex
gauge group: the former is an exactly solvable theory, meaning that the partition function
can be computed by a ﬁnite state-sum, a consequence of the fact that it is a TQFT in 3
dimensions. On the other hand, the situation with complex Chern–Simons theory is more
mysterious. For reasons that are not entirely understood, the partition functionZM(u;τ)
for manifolds with torus boundary components reduces to a ﬁnite-dimensional integral (the
so called-state integral) whose integrand is a product of Faddeev’s quantum dilogarithm
functions [Fad95], assembled out of an ideal triangulation of the manifold. This was the
approach taken by Andersen-Kashaev [AK14, AK18] and Dimofte [Dim17] following prior
ideas of [Hik07, DGLZ09]. Focusing for simplicity on the case of a 3-manifold with a single
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 3
torus boundary component (such as the complement of a hyperbolic knot inS3), the state-
integralZM(u;τ) is a holomorphic function ofτ∈ C ′ = C \ (−∞, 0] andu∈ C that satisﬁes
a pair of linearq-diﬀerence equations. The existence of these equations for a state-integral
follows from the closure properties of Zeilberger’s theory ofq-holonomic functions and the
the quasi-periodicity properties of Faddeev’s quantum dilogarithm, in much the same way
as theq-holonomicity of the colored Jones polynomial of a knot follows from a state-sum
formula [GL05]. In fact, it is conjectured that the linearq-diﬀerence equation satisﬁed by
the colored Jones polynomial of a knot coincides with the linearq-diﬀerence equations of
ZM(u;τ) (see e.g. [AM17] and Sections 5 and 6 below for examples).
1.2. ResurgenceandtheStokesautomorphism. Theglobalfunction ZM(u;τ)givesrise
to a vectorΦ(x;τ) of perturbative series inτ whose coeﬃcients are meromorphic functions
of u. These series are typically factorially divergent and a key question is a description
of the analytic continuation of their Borel transform in Borel plane, their trans-series and
their Stokes automorphisms. This is a typical question in perturbative quantum ﬁeld theory
whereresurgenceaimstoreproduceanalyticfunctionsfromfactoriallydivergentseries(foran
introduction to resurgence, see for instance [MS16, ABS19, Mn14, Mn15]), and where Chern–
Simons theory with a compact or complex gauge group is an excellent case to analyze. Some
aspects of resurgence in Chern–Simons theory were studied in [Gar08, CG11, Mn14, GMnP,
GH18, GZa, GZb]. The multi-valuedness of the complex Chern-Simons action dictates that
the transseries are assembled out of monomials in˜x and ˜q where ˜q = e−2πi/τ and ˜x = eu/τ.
Our discoveries are summarized as follows:
• The singularities of the seriesΦ(x;τ) in Borel plane are arranged in horizontal lines
2πi apart, and within these lines in ﬁnitely many pointslogx apart. This deﬁnes a
collection of Stokes lines in a peacock-like pattern (see Figure 1) whose corresponding
Stokes automorphisms satisfy a unique factorization property with integer Stokes
constants.
• The Stokes automorphismS(x; q) along a half-plane is a fundamental matrix solution
to a (dual) linear q-diﬀerence equation, hence fully computable.
• The functionZM(u;τ) is one entry of a matrix-valued collection of descendant par-
tition functions which are a fundamental solution to aq-holonomic system in two
variables.
The arrangement of the singularities in Borel plane is reminiscent of a “stability datum” of
Kontsevich-Soibelman [KS11, KS, KS14] where the corresponding integers are often called
DT-invariants or BPS degeneracies. The Stokes automorphisms along half-planes are analo-
gous to the spectrum generators in Gaiotto-Moore-Neitzke [GMN10, GMN13, GMN12]. Our
integers are locally constant functions of a complex parameterx and their jumping along a
wall-crossing will be the topic of a subsequent publication.
Our paper gives a concrete realization of these abstract ideas of perturbative series and
their resurgence, Stokes automorphisms and their wall-crossing formulas for the case of
complex Chern–Simons theory, and illustrate our results with the 3-manifolds of the two
simplest hyperbolic knot complements, the complements of the41 and the 52 knots.
4 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
· · ·· · ·
· · ·· · ·
Figure 1. A peacock arrangement of Stokes rays in the complex Borel plane.
