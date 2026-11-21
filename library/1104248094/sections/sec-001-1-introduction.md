---
doc_id: 1104248094
doc_title: "Hochschild and cyclic homology of quantum groups"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1104248094.pdf
source_sha256: c1fdb4791afcad3b
toc_source: inferred
doc_brief: "Hochschild and cyclic homology of quantum groups — For an arbitrary complex linear semisimple Lie group G, we consider Hopf algebras of the deformations of the formal and algebraic functions on G."
---
481
2. Definitions of Hochschild and Cyclic Homology 
484
3. Quantum Groups 
488
4. A Spectral Sequence 
493
5. The Lie Algebra Homology 
500
5.1. Formal Functions 
501
5.2. Algebraic Functions 
502
6. Hochschild and Cyclic Homology of Quantum Groups 
505
6.1. Quantum Formal Groups 
506
6.2. Quantum Algebraic Groups 
506
Appendix A. Notations about Calculus on Lie Groups 
515
Appendix B. Example G = SL(2, C) 
516
1. Introduction
According to Gelfand, the category of locally compact topological spaces is
equivalent to the category of commutative C*-algebras. Also, the category of affine
The main result of this paper was announced at the AMS meeting at University Park in
April 1990
* Supported by Department of Energy under Grant DE-FG02-88ER25062
** Supported by Harvard Prize Fellowship. Address after July, 1990: Department of
Mathematics, Pennsylvania State University, University Park, PA 16802, USA
482 
P. Feng and B. Tsygan
schemes of finite type over a field is equivalent to the category of finitely generated
algebras over the field. Since the study of commutative algebras is the same as
that of spaces, it is reasonable to interpret the study of non-commutative algebras
as studying some "non-commutative spaces," and try to generalize the methods
for spaces to be applicable to algebras. Cyclic (co)homology [8,44,14,27] generalizes
the de Rham cohomology to the non-commutative case, and it is sometimes
referred to as non-commutative differential geometry.
In this paper we compute the Hochschild and cyclic homology of quantum
groups, i.e., the quantized rings of functions on semi-simple Lie groups. This is
interesting in several aspects. First it enriches the study of non-commutative
differential geometry. Even though cyclic homology had been invented as
generalized differential geometry and has found many applications, there is still a
lack of interesting examples. Previously the only quantum spaces (in the spirit of
Manin [31]) whose cyclic homologies were known were non-commutative tori
[8, 43], quantum affme spaces [32] and SUh(2) [33]. However quantum groups
[11,21] present some of the most interesting examples of non-commutative spaces.
Quantized universal enveloping algebras, which are more or less dual to what we
are studying in this paper, were discovered in the course of studying integrable
systems. They have been shown to have intimate relations with many other areas
of mathematics and physics, e.g., link invariants [23], conformal field theories
[1, 34, 30]. But most of what we know about quantized universal enveloping
algebras concerns their representations, and their relations with other fields are
simply observed without being explained. The knowledge of the structure of
quantum groups is likely necessary to understand all these. A study of
non-commutative differential geometry will provide much needed insight into the
geometrical and topological properties of quantum groups.
The main phenomenon concerning the Hochschild and cyclic homology of
quantum groups is the following. As is well-known, any deformation of the
multiplicative structure of the algebra of functions on a manifold gives rise to a
Poisson structure on the manifold; the symplectic leaves of this Poisson structure are
in many senses good analogues of the "points of the non-commutative spectrum"
of the deformed algebra. It has been established in several works that the
non-commutative algebraic geometry of quantum spaces is very close to the
geometry of "the space of symplectic leaves," i.e., the geometry of the quasi-
classical limit of the quantum spaces, if the value of the deformation parameter is
generic. We should mention the work of S. Levendorski, Y. Soibelman and L.
Vaksman [26, 41, 42] which asserts that the set of unitary representations of the
quantized ring of functions on a compact semisimple Lie group is naturally
isomorphic to the set of symplectic leaves of the Poisson structure. Also the
approach to non-commutative algebraic geometry suggested by A. Rosenberg
seems to give analogous results (in computed examples) [36]. Recall that the
Hochschild homology of the algebra of algebraic functions on a non-singular affme
variety is isomorphic to the space of differential forms on the variety. Thus the
Hochschild homology of quantum groups may be viewed as the space of quantized
differential forms. Our main result is that when the value of the deformation
parameter is generic this Hochschild homology is equal to the space of "forms"
on the "space of symplectic leaves" of the Poisson structure. The structure of
symplectic leaves is of course well-known. When G is a compact Lie group with
Hochschild and Cyclic Homology of Quantum Groups 
483
maximal torus T, the Poisson structure on G descends to the one on G/Γ, and its
symplectic leaves are the Bruhat cells [39]. When G is complex semi-simple the
answer is similar.
Note that while the Hochschild homological dimension of C[G] is of course
the dimension of the group, the analogous dimension for the quantized C[G] is
the rank of the group. As has been mentioned by A. Connes, this phenomenon
might give a more appropriate version of his approach to the various models of
filed theory as "non-commutative Yang-Mills 
models" because when the
Hochschild homological dimension drops, we get rid of various divergences [9].
Note also that the Hochschild and cyclic homology of the rings which are
deformations of the commutative rings is a very interesting subject. In all reasonable
cases the same phenomenon takes place: the non-commutative geometry is
isomorphic to the geometry of the quasi-classical limit, for example, the
(ρseudo)differential operators on a manifold [2,4,46], universal enveloping algebra
[15, 22], and non-commutative tori [8, 43]. But the explicit form of this
isomorphism is highly non-trivial. For the ring of differential operators on a
manifold, this explicit isomorphism implies the Riemann-Roch theorem; for the
ring of symbols of pseudo-differential operators, the analogous statement is very
likely to imply the index theorem [16, 46]. We hope that these statements are the
partial cases of a conjectural generalized Riemann-Roch theorem which measures
the "non-triviality" of the isomorphism of Hochschild and cyclic homology of
the quasi-classical limit and that of the quantum limit. In this respect, the quantum
groups (or rather the quantum homogeneous spaces) may provide another
non-trivial partial case.
The paper is organized as follows. In Sect. 2 we recall the definition and basic
properties of Hochschild and cyclic homology. Here we give a new complex for
computing the Hochschild homology of Hopf algebras. Section 3 describes the
quantum groups we are going to study. The rest of the paper is mainly devoted
to the computation of the Hochschild homology of quantum groups. In Sect. 4
we introduce a spectral sequence, which converges to Hochschild homology
of quantum groups. Its E
2 term is the Brylinski homology of the group regarded
as a Poisson manifold. It is then identified with Lie algebra homology of g*,
the dual of the Lie algebra g of the corresponding group G of the quantum group,
with coefficient in the functions on G. The geometrical meaning of the action is
given, and it is shown that it is related to the standard Lie algebra action on some
very simple induced representations. We compute this Lie algebra homology for
both formal and algebraic functions in Sect. 5. We then show in Sect. 6 that for
both formal and algebraic cases the spectral sequence of Sect. 4 is degenerate at
E
2. This means the quantum limit is determined by the quasiclassical limit. Thus
the Lie algebra homology actually yields the Hochschild homology. After this the
cyclic homology is readily obtained. In Appendix A we give some of our conventions
about the calculus on Lie groups. Appendix B contains various explicit calculations
for G = SL(2,C).
We are grateful to J. L. Brylinski, A. Connes, V. G. Drinfeld, B. Enriquez,
E. Getzler, M. Goulian, N. Yu. Reshetikhin for helpful discussions. We are especially
indebted to W. Schmid for consultation on the n-homology of Harish-Chandra
modules. In our first draft there was a gap in the proof of the degeneracy of a
spectral sequence. We wish to express our deep gratitude to J. Block and E. Getzler
484 
P. Feng and B. Tsygan
for pointing that out to us. P. F. would like to thank A. Jaffe for his encouragement
and support.
