---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
---
2
2.
Preliminaries
3
2.1.
Galois-stability
3
2.2.
Exponentially bounded holomorphic functions
4
2.3.
Generically periodic holomorphic maps up to G-action
4
2.4.
Algebraic independence of exponentials
5
2.5.
Geometric local systems
5
3.
Periodic families and pencils of ﬂat connections
6
3.1.
Polynomial families and pencils of ﬂat connections
6
3.2.
Jumping loci of families of ﬂat connections
7
3.3.
Periodic families and pencils of ﬂat connections
8
3.4.
Families and pencils with periodic monodromy
8
3.5.
Quantum connections
9
4.
Quasi-motivic families and pencils of ﬂat connections
10
4.1.
Quasi-motivic families
10
4.2.
Jumping loci of quasi-motivic pencils
11
4.3.
Poles of shift operators for quasi-motivic pencils
11
4.4.
Endomorphism algebras of quasi-motivic pencils
12
4.5.
Semisimplicity loci of quasi-motivic pencils
12
4.6.
Motivic families
13
4.7.
A speculative digression: quasi-geometric connections
14
4.8.
Pseudo-pencils
17
1
2
PAVEL ETINGOF AND ALEXANDER VARCHENKO
5.
Examples of periodic pencils
18
5.1.
KZ connections
18
5.2.
Dunkl connections
22
5.3.
Casimir connections
25
5.4.
Irreducibility
27
5.5.
Unitarity and generic semisimplicity
27
References
27
1. Introduction
In this paper we introduce a new notion of a periodic pencil of ﬂat connections.
Namely, a pencil of ﬂat connections is a family
∇(s) = d −s1B1 −... −snBn
of ﬂat connections on the trivial rank N vector bundle over a smooth irreducible variety X
over a ﬁeld k, where Bj ∈Ω1(X) ⊗MatN(k) for 1 ≤j ≤n. Such a pencil is said to be
periodic1 if it admits shift operators
Aj ∈GLN(k(s)[X])
such that
∇(s + ej) ◦Aj(s) = Aj(s) ◦∇(s), 1 ≤j ≤n.
There are many interesting examples of periodic pencils, falling into three large classes:
Knizhnik-Zamolodchikov (KZ) connections, Dunkl connections, and Casimir connections.
Another important source of examples (often belonging to one of these classes) is equivariant
quantum connections of conical symplectic resolutions of singularities with ﬁnitely many
torus ﬁxed points.
At the same time, periodic pencils enjoy many remarkable properties, especially when
they have regular singularities. We call periodic pencils with regular singularities quasi-
motivic. For example, we show that quasi-motivic pencils give rise to local systems deﬁned
over Q in both de Rham and Betti realizations, and their singularities can only occur on an
arrangement of hyperplanes.
In a follow-up paper [EV2], we describe the spectrum of the p-curvature of a periodic pencil
in characteristic p. When applied to equivariant quantum connections for conical resolutions
with ﬁnitely many torus ﬁxed points, this has applications to symplectic geometry, since
it has been shown in [Lee] that the p-curvature of such a connection coincides with the
equivariant version of Fukaya’s quantum Steenrod operation (at least up to a nilpotent
correction that does not aﬀect the spectrum).
