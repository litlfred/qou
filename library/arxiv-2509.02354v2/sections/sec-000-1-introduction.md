---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomyR-matrix of quantumsl2 at a root of unity."
---
2. Quantum sl2 and Weyl algebras 3
2.1. The braiding for quantum sl2 3
2.2. The braiding for Uq(sl2) 3
2.3. Representation into the Weyl algebra 4
3. Specialization to a root of unity 5
3.1. Central subalgebras at roots of unity 5
3.2. Uξ-modules. 6
3.3. The braiding on characters 6
3.4. The homomorphism from Uq to the Weyl algebra at root of unity 7
3.5. Braiding of Uξ-modules. 9
3.6. Wξ-modules 11
4. The R-matrix in the Fourier dual basis 12
4.1. Recursions for the R-matrix coefficients 12
4.2. The normalized R-matrix 14
4.3. Factorization of the R-matrix 15
4.4. The holonomy Yang-Baxter equation 17
5. R-matrix computations 23
5.1. Log-parameter dependence 23
5.2. The pinched limit of theR-matrix 25
5.3. The determinant of theR-matrix 28
5.4. The Fourier transform of theR-matrix 29
Appendix A. Quantum dilogarithms 33
A.1. Basic definitions 33
A.2. Fusion identities 36
A.3. Fourier transform identities 37
References 39
2020 Mathematics Subject Classification.Primary 17B37, secondary 57K16.
Key words and phrases.quantum groups, holonomy braiding, quantum dilogarithm.
1
arXiv:2509.02354v2  [math.QA]  29 Apr 2026
2 CAL VIN MCPHAIL-SNYDER AND NICOLAI RESHETIKHIN
1. Introduction
HolonomyR-matrices were used in [15] to describe invariants of knots with flat connections
in the complement. TheseR-matrices were introduced in [27] to describe the braiding for the
de Concini-Kac specialization of quantum groups corresponding to simple finite dimensional
Lie algebras at a root of unity. In that case the quantized universal enveloping algebra is finite
dimensional over the central Hopf subalgebra. Generic irreducible modules are parametrized
by generic points of a finite cover of the dual Poisson Lie group with the standard Poisson-Lie
structure [5]. In this paper we focus on the case ofsl2.
It is known that when the universalR-matrix is evaluated in representations obtained
through a certain homomorphism from quantumsl2 to theq-Weyl algebra it factorizes into
the product of four quantum dilogarithms, see for example [7, 28] and references therein.
This factorization in the setting of the modular double was first observed in [7]. In [17] this
factorization was was derived as a general consequence of homomorphisms from the Drinfeld
double to the Heisenberg double of a Hopf algebra.
In [9, 2] a geometric version of the quantum dilogarithm was established. The geometric
q-dilogarithm is the regular part of the asymptotic ofq-dilogarithm whenq goes to a root of
unity as in [2]. It was shown to satisfy the holonomy pentagon equation.
In this paper we describe the factorization of the holonomyR-matrix for quantumsl2 [27]
into four holonomy quantum dilogarithms. We construct this factorization “from scratch”,
directly from the representation theory of the de Concini-Kac version of quantumsl2 at a
root of unity. OurR-matrices are sections of a vector bundle over the space of geometric
parameters and we obtain local coordinates by taking certain logarithms. We show that our
R-matrices satisfy a holonomy Yang-Baxter relation when these log-parameters satisfy a
natural geometric condition.
In [21] ourR-matrices are used to define knot and tangle invariants which are a refinement
of those in [3]. We expect that using the factorization that we describe here one can clearly
establish the relation between invariants of knots with flat connection in the complement
constructed in [15] and the work [1] where similar invariants were obtained using triangulations
of the complement. We also expect that our factorization is an important step in constructing
the corresponding homotopy TQFT [29]; see also [12].
This paper is a mix of an overview of known material and original results. We include the
overview to collect material scattered over a large number of papers.
In Section 2 we establish conventions on quantumsl2 and its presentation in terms of
Weyl algebras. Section 3 is an overview of elements of representation theory of quantumsl2
and its braiding. In Section 4 we construct the braiding matrix (the holonomyR-matrix)
using q-dilogarithms and prove it satisfies holonomy braid relations. Section 5 contains
some technical computations involving theR-matrix that we use elsewhere in the paper.
Appendix A has technical details on quantum dilogarithms and collects properties used
throughout the paper.
Acknowledgements. We would like to thank Nathan Geer, Rinat Kashaev, and Bertrand
Patureau-Mirand for helpful discussions. The work of N. R. was supported by the Collabora-
tion Grant “Categorical Symmetries” from the Simons Foundation, by the Changjiang fund,
and by the project 075-15-2024-631 funded by the Ministry of Science and Higher Education
of the Russian Federation.
THE HOLONOMY BRAIDING FOR Uξ(sl2) 3
