---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
2. Division Algebras and the Standard Model 3
2.1. Motivation 3
2.2. Historical Overview 4
2.3. The Normed Division Algebras 6
2.4. The Associative Multiplication Algebras of O 7
2.5. Connection to the Standard Model 8
3. Causal Fermion Systems 10
3.1. Causal Fermion Systems and the Reduced Causal Action Principle 10
3.2. Spacetime Structures 11
3.3. Dynamical Equations in Spacetime 12
3.4. Connection to the Standard Model 12
3.5. Connection to Quantum Field Theory 15
3.6. Connection to Quantum Geometry and Quantum Gravity 16
4. Comparison 16
4.1. Foundations of the Approaches 16
4.2. Connection to the Gauge Group of the Standard Model 18
4.3. Describing the Three Generations in the Standard Model 19
5. Outlook and Directions of Future Research 21
5.1. Connection with the Exceptional Lie Groups and Jordan Algebras 21
5.2. Chiral Symmetry Breaking 22
Appendix A. Description of Majorana Spinors in Causal Fermion Systems 30
References 31
1
arXiv:2403.00360v2  [math-ph]  15 Sep 2024
2 F. FINSTER, N.G. GRESNIGT, J.M. ISIDRO, A. MARCIAN `O, C.F. PAGANINI, AND T.P. SINGH
1. Introduction
This article is part of a series of papers comparing the structures and ideas of
different approaches to fundamental physics that was started with [42, 44] and will be
continued in [73, 45]. Each of these papers contains an introduction to the theories
under consideration including an overview of their accomplishments. These overviews
serve as a starting point for a reader familiar with one of the approaches to engage
with the other approach. The papers proceed with a detailed comparison of these two
theories. Ultimately, the goal is to motivate the community to establish an extensive
collection of such articles as a sort of “Rosetta stone” for approaches to fundamental
physics. The hope is that such a set of dictionaries facilitates the exchange of ideas
across approaches and thereby catalyzes progress in the foundations of physics. This
addresses a distinctly different goal from overview articles such as [80, 83, 28] or [6] that
try to cover the development across many approaches simultaneously. By focusing on
two sets of ideas at a time, a greater level of depth can be achieved and more specific
issues can be addressed.
The present article resulted from discussions of the authors with the wish of connect-
ing two different approaches to fundamental physics: The approach relating octonions
(or division algebras in general, although we restrict ourselves in the present articles
to octonions and use the term octonions and division algebras synonymously) with
fundamental physics on one side and causal fermion systems on the other. Our report
uncovers many surprising similarities and analogies, but also points to differences and
discusses open research questions. One of our key findings is that octonions (more
generally, tensor products of division algebras) come up naturally to describe sym-
metries or approximate symmetries of the vacuum configuration of a causal fermion
system. Likewise, the interactions of a causal fermion system can be described in terms
of algebras of endomorphisms acting on the octonions. In this way, the approaches
connecting division algebras, in particular octonions, to the standard model (see for ex-
ample [34, 59, 103, 82]) may give a more fundamental understanding for the structure
of the vacuum of the causal fermion system and for the form of possible interactions.
On the other hand, the theory of causal fermion systems may provide the octonionic
theories with additional structures needed for developing them into full physical the-
ories. In particular, causal fermion systems give rise to spacetime structures (like
causality and geometry) and equations describing the dynamics (via the causal action
principle). In this way, the octonionic theories and causal fermion systems comple-
ment each other. Moreover, there are interesting and inspiring connections between
the ideas underlying the approaches. Studying these connections further should, on
the one hand, provide a dynamical framework for division algebraic descriptions of the
standard model and, on the other hand, give restrictions for possible matter models
which can be realized as causal fermion systems.
Since the pioneering work of G¨ uynadin and G¨ ursey in the 1970s describing the SU(3)
color symmetry of quarks using octonions, attempts using octonions, together with the
remaining three normed division algebras, to explain the structure, gauge groups, and
particle multiplets of the standard model have grown in popularity. The extensive
works of Dixon, culminated in the book [34], demonstrate how many of the math-
ematical features of the standard model, including its gauge symmetries to which a
single generation of fermions and leptons are subject, together with the correct multi-
plets into which they fall, are inherent in the 64 real dimensional composition algebra
CAUSAL FERMION SYSTEMS AND OCTONIONS 3
T = R⊗ C⊗ H⊗ O. In a closely related approach, Furey focuses on the Clifford al-
gebras which are generated by linear operators acting on (tensor products of) division
algebras via composition. She describes the particle multiplets in terms of minimal
left ideals of these algebras and the gauge groups as the subgroups of the Clifford al-
gebra’s spin group that preserve the structure of these minimal left ideals [59, 62, 63].
Many other authors, not cited here, have contributed to these and related approaches.
Such division algebraic constructions offer a number of attractive features, most no-
tably a derivation of the standard model gauge groups from a minimal mathematical
framework, together with the correct chiral fermion representations.
The theory of causal fermion systems is a recent approach to fundamental physics
(see the basics in Section 3, the reviews [53, 40, 47], the textbooks [39, 52] or the
website [1]). In this approach, spacetime and all objects therein are described by a
measure ρ on a set F of linear operators on a Hilbert space ( H,⟨.|.⟩H). The physical
equations are formulated by means of the so-called causal action principle, a nonlinear
variational principle where an actionS is minimized under variations of the measureρ.
In different limiting cases, causal fermion systems give rise to the standard model of
particle physics and gravity on the level of classical field theory [39] as well as to
quantum field theory [50, 51, 27].
The connection between causal fermion systems and octonionic theories is estab-
lished by analyzing the symmetry properties of the causal fermion system describing
the Minkowski vacuum. In order to describe the Minkowski vacuum by a causal fermion
system, one needs to specify the configuration of the fermions. By doing this ad hoc
in a specific way, the causal action principle yields the gauge groups and couplings of
the standard model (for more details see Section 3.4). As we shall see, the vacuum
configuration can be described naturally using octonions. Likewise, the symmetries
are described by the associative multiplication algebras generated from the octonions.
Even more, the interaction as described by the causal action principle can be written
using automorphism groups of octonions and the exceptional Jordan algebra. In this
manner, one uncovers close connections between causal fermion systems and octonionic
theories. The main part of this paper is devoted to working out these connections in
detail (see Section 4 and Section 5.1). A related question is whether octonions pro-
vide a better and more systematic understanding for how the vacuum is to be chosen.
Here we explore the possibility that the chiral asymmetry is no longer built in from
the beginning, but instead arises dynamically by a chiral symmetry breaking effect
(Section 5.2). Analyzing these questions in more detail should also give new insight
into the rigidity of the particle model in the theory of causal fermion systems.
The paper is organized as follows. We begin by giving short but self-contained
reviews of octonionic theories (Section 2) and to causal fermion systems (Section 3).
In Section 4 we compare these approaches. Section 5 gives an outlook and spells out
several directions for future research. Moreover, as Majorana spinors are important
for certain aspects of octonionic theories, in Appendix A we explain how Majorana
spinors can be described by a causal fermion system.
