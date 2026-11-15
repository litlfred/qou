---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.995
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:Introduction label="sec:Introduction"}

Holonomy $R$-matrices were used in [@Kashaev2005] to describe invariants of knots with flat connections in the complement. These $R$-matrices were introduced in [@Reshetikhin1995] to describe the braiding for the de Concini-Kac specialization of quantum groups corresponding to simple finite dimensional Lie algebras at a root of unity. In that case the quantized universal enveloping algebra is finite dimensional over the central Hopf subalgebra. Generic irreducible modules are parametrized by generic points of a finite cover of the dual Poisson Lie group with the standard Poisson-Lie structure [@DeConcini1990]. In this paper we focus on the case of $\mathfrak{sl}_2$.

It is known that when the universal $R$-matrix is evaluated in representations obtained through a certain homomorphism from quantum $\mathfrak{sl}_2$ to the $q$-Weyl algebra it factorizes into the product of four quantum dilogarithms, see for example [@Fadeev2000; @Schrader2019] and references therein. This factorization in the setting of the modular double was first observed in [@Fadeev2000]. In [@Kashaev1996] this factorization was was derived as a general consequence of homomorphisms from the Drinfeld double to the Heisenberg double of a Hopf algebra.

In [@Faddeev1994; @Bazhanov1995] a geometric version of the quantum dilogarithm was established. The geometric $q$-dilogarithm is the regular part of the asymptotic of $q$-dilogarithm when $q$ goes to a root of unity as in [@Bazhanov1995]. It was shown to satisfy the holonomy pentagon equation.

In this paper we describe the factorization of the holonomy $R$-matrix for quantum $\mathfrak{sl}_2$ [@Reshetikhin1995] into four holonomy quantum dilogarithms. We construct this factorization "from scratch", directly from the representation theory of the de Concini-Kac version of quantum $\mathfrak{sl}_2$ at a root of unity.

Our $R$-matrices are sections of a vector bundle over the space of geometric parameters and we obtain local coordinates by taking certain logarithms. We show that our $R$-matrices satisfy a holonomy Yang-Baxter relation when these log-parameters satisfy a natural geometric condition.

In [@McPhailSnyderVolume] our $R$-matrices are used to define knot and tangle invariants which are a refinement of those in [@Blanchet2018]. We expect that using the factorization that we describe here one can clearly establish the relation between invariants of knots with flat connection in the complement constructed in [@Kashaev2005] and the work [@Baseilhac2004] where similar invariants were obtained using triangulations of the complement. We also expect that our factorization is an important step in constructing the corresponding homotopy TQFT [@Turaev2010]; see also [@GeerBook].

This paper is a mix of an overview of known material and original results. We include the overview to collect material scattered over a large number of papers.

In [\[sec:q-algebra\]](#sec:q-algebra){reference-type="ref" reference="sec:q-algebra"} we establish conventions on quantum $\sla$ and its presentation in terms of Weyl algebras. is an overview of elements of representation theory of quantum $\sla$ and its braiding. In [\[sec:R-matrix\]](#sec:R-matrix){reference-type="ref" reference="sec:R-matrix"} we construct the braiding matrix (the holonomy $R$-matrix) using $q$-dilogarithms and prove it satisfies holonomy braid relations. contains some technical computations involving the $R$-matrix that we use elsewhere in the paper. [\[sec:quantum-dilogarithms\]](#sec:quantum-dilogarithms){reference-type="ref" reference="sec:quantum-dilogarithms"} has technical details on quantum dilogarithms and collects properties used throughout the paper.

### Acknowledgements

We would like to thank Nathan Geer, Rinat Kashaev, and Bertrand Patureau-Mirand for helpful discussions. The work of N. R. was supported by the Collaboration Grant "Categorical Symmetries" from the Simons Foundation, by the Changjiang fund, and by the project 075-15-2024-631 funded by the Ministry of Science and Higher Education of the Russian Federation.
