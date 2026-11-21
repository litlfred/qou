---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER
COHOMOLOGY
MASAHICO SAITO AND EMANUELE ZAPPALA
Abstract. Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari-
ants. More recently, cohomology theories for YBOs have been independently developed, drawing
inspiration from analogous theories for quandles and other discrete algebraic structures. Quandle
cohomology, in particular, gives rise to cocycle invariants for knots via 2-cocycles, which are closely
related to quandle extensions, and knotted surfaces via 3-cocycles. These quandle cocycle knot
invariants have also been shown to admit interpretations as quantum invariants.
Similarly, 2-cocycles in Yang-Baxter cohomology can be interpreted in terms of deformations
of YBOs. Building on these parallels, we introduce quantum cocycle invariants of knots using 2-
cocycles of Yang–Baxter cohomology, from the perspective of deformation theory. In particular,
we demonstrate that the quandle cocycle invariant can be interpreted in this framework, while the
quantum version yields stronger invariants in certain examples.
We develop our theory along two primary approaches to quantum invariants: via trace con-
structions and through (co)pairings. Explicit examples are provided, including those based on the
Kauffman bracket. Furthermore, we show that both the Jones and Alexander polynomials can be
derived within this framework as invariants arising from higher-order formal Laurent polynomial
deformations via Yang-Baxter cohomology.
Contents
1.
Introduction
1
2.
Preliminaries
3
3.
Yang-Baxter cohomology
5
4.
Quantum cocycle invariants via traces
8
5.
Examples via traces
12
6.
Quantum cocycle invariants via maxima/minima
19
7.
Examples via maxima/minima
21
8.
Higher order invariants
26
9.
The Jones and Alexander polynomials as higher order invariants
29
References
33
1. Introduction
The Jones polynomial was originally introduced using von Neumann algebras [10], and this was
later reformulated using Yang-Baxter operators (YBOs), and combinatorial techniques on knot
diagrams [12]. This discovery has lead to a new area of quantum topology.
Quandles [11, 15] are discrete self-distributive systems with additional conditions, that have
been introduced before the Jones polynomial. Quandle cocycle invariants [4] of knots and knotted
surfaces have been defined since then, and brought a new light to quandles.
Quandle cocycle
1
arXiv:2509.04267v3  [math.GT]  14 Nov 2025
2
MASAHICO SAITO AND EMANUELE ZAPPALA
invariants were defined using 2-cocycles of quandle cohomology theory, in a form of state sum with
2-cocycles as weights, though the states are limited to quandle colorings. Applications to various
properties of knots and knotted surfaces followed. Algebraic aspects of quandle homology theory,
such as extensions [2], have also been explored, in parallel to group cohomology theory. It was
shown [9] that they can be interpreted as quantum invariants, i.e. as the trace of suitable operators
associated to a braid form of a knot.
Quandle homology theory has been generalized to homology theory of set-theoretic Yang-Baxter
operators [3], and further to general Yang-Baxter operators [6,7,14,17]. Homology and cohomology
theories for categorical self-distributivity are also developed [1,8]. Another cohomology theory for
YBOs was defined in [18] in such a way that it is unified with Hochschild cohomology, and that
follows deformation theory of braided algebras. This point of view from deformation theory parallels
the fact that quandle 2-cocycles can be used to define extensions of quandles.
Since quandle structures induce YBOs, it is a natural question whether quandle cocycle knot
invariants can be generalized to a quantum version, in the sense that it is defined using YBOs instead
of discrete structures. This is the goal of the current paper. We construct knot invariants using
deformation 2-cocycles from Yang-Baxter cohomology, which we call quantum cocycle invariamnts.
There are two main methods to construct knot invariants from YBOs, (1) by using closed braid
form and taking trace, and (2) fixing a height function and assign maps corresponding to local
maxima and minima. We seek both approaches. For (1), well-definedness requires to verify Markov
trace property, that ensures invariance under Markov stabilizations, and for (2), maps assigned to
maxima and minima need to satisfy additional Reidemeister moves involving them.
Specifically, for both approaches, let R be a given YBO that defines by braid group representation
a knot invariant. Take a YBO 2-cocycle ϕ of the YB cohomology for R and the deformation R+ℏϕ
(see below). For (1) we take the trace and show that it gives rise to an invariant (Theorem 4.3), and
for (2) we use height function to show well definedness (Theorem 6.1) and present requirements for
the 2-cocycles to satisfy for well definedness. For both approaches, we provide explicit examples of
this construction starting from well known R, such as tensorized version of quandle operations and
Kauffman bracket.
We consider higher order deformations of YBOs, where the YB 2-cocycle is integrable, and
construct associated invariants from YBOs of type R + Pn
i=1 ℏiϕi, where ϕi are cochains that clear
the deformation obstruction in the third YB cohomology group, as described in Section 8. This
result is formulated in Theorem 8.3.
In addition, the approach of generalizing quandle cocycle invariants by means of YB cohomology
allows us to answer another natural question. Namely, whether there is an underlying common
structure behind quandle cocycle invariants and the Alexander and Jones polynomials. We show
that they are all interpreted as the YB cocycle invariants introduced and studied in this article.
In fact, we introduce a suitable generalization of the aforementioned higher order invariants to
Laurent polynomial series, and then show that it is possible to find pre-YB operators, along with
suitable cohomology classes and higher order deformations such that the Jones and Alexander poly-
nomials are the Laurent quantum cocycle invaraints arising from them. The results are formalized
in Theorem 9.5 and Theorem 9.6.
This paper also adds a new relation between algebraic deformation cohomology theories and
knot theory. Diagrammatic methods in knot theory have been applied to algebraic deformation
theories. For example, in [1] diagrams are used to construct cohomology theories for categorical self-
distributive structures, and in [18,19] Yang-Baxter and Hochschild cohomology theories are unified
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY
3
with extensive use of knot and graph diagrams. In this paper, the opposite direction is proposed,
namely applying deformation cohomology theories to the construction of knot invariants. Since a
number of knot invariants are defined using algebraic systems, the idea of using their deformation
cohomology for constructions of new knot invariants may be applicable to such invariants as well,
therefore providing more general applicability of our current results.
This article is organized as follows. Section 2 reviews the two approaches of defining quantum
invariants as mentioned above. In Section 3, we review the Yang-Baxter homology theory for low
dimensions with diagrammatic conventions, and then describe a definition in all higher dimensions.
The definition of the quantum cocycle invariant using the trace approach is given in Section 4,
following Turaev’s formulation. Concrete examples, including the tensorized quandle cocycle in-
variant, are presented in Section 5. The definition for the second approach using maxima and
minima is given in Section 6, and developed in Section 7 for the bracket polynomial with diagram-
matic computations. Up to this section the invarian uses infinitesimal deformation, that is of degree
up to 1 with respect to the deformation parameter ℏ. The invariant is extended to higher order
invariant in Section 8, extending degrees with respect to ℏ. In Section 9, the higher order invariant
is further extended to negative degrees to allow Laurent polynomial expansions, which provides an
interpretation of Jones and Alexander polynomials as such quantum cocycle invariants.
Throughout the paper, the results apply to either a knot or a link, so that we use the convention
that a knot K means either a knot or a link.
