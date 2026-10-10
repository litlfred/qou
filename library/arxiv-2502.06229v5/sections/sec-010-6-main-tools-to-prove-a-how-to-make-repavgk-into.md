---
doc_id: arxiv-2502.06229v5
doc_title: "Constructing equivalences between fusion categories of quantum groups and of vertex operator algebras via quantum gauge groups"
section_id: sec-010-6-main-tools-to-prove-a-how-to-make-repavgk-into
section_title: "Main tools to prove (a): How to make Rep(A(Vgk)) into a braided tensor category with Huang-Lepowsky structure."
section_number: 6
pages: 17-19
source_pdf: 2502.06229v5.pdf
source_sha256: 3499c40ea150a617
toc_source: outline
doc_brief: "Constructing equivalences between fusion categories of quantum groups and of vertex operator algebras via quantum gauge groups — This paper establishes connections between a problem posed by"
---
tensor category with Huang-Lepowsky structure.
A second way to construct a braided tensor category structure on Rep(A) from a braided
tensor category C is useful when C has a natural faithful linear functor
F : C →Vec
given from the start and a braided tensor category structure (C, ⊗, ι, α, d) is constructed
as a second step. Then in this case it may be more natural to first consider the discrete
18
C. PINZARI
algebra A = Nat0(F) and then transfer of all the structure of C to the representation
category of A.
We discuss this transfer in Sect. 15 in [10] without the need of a weak quasi-tensor struc-
ture on F, in abstract terms. One only needs an inverse linear equivalence S : Rep(A) →C
of the Tannakian linear equivalence E : C →Rep(A). In this situation we may define a
braided tensor category structure in Rep(A) from the braided tensor category structure in
C with the property that Rep(A) is equivalent to C as a braided tensor category. The ten-
sor product, associativity morphisms, braiding morphisms of Rep(A) are explicitly defined
via the equivalence E and its inverse S.
Far-reaching historic examples of such F may be found in conformal field theories (e.g.
in the setting of models of conformal nets and in that of vertex operator algebras) as the
minimum energy functor, before the braided tensor category structure was constructed.
In these cases we refer to the braided tensor tensor category structure of modules of
vertex operator algebras by Huang and Lepowsky or to the unitary braided tensor category
structure of localized endomorphisms of conformal nets.
In the setting of vertex operator algebras, the minimum energy functor is also known
as Zhu’s functor [106]. Notably, Zhu constructed a semisimple algebra A(V ) directly from
modules of the vertex operator algebra V , naturally isomorphic to Nat0(F). This algebra is
well known, and is referred to as the Zhu algebra. He also constructed a linear equivalence
E : Rep(V ) →Rep(A(V )) and also a natural linear inverse equivalence S : Rep(A(V )) →
Rep(V ) in the same paper if the vertex operator algebra V satisfies suitable semisimplicity
conditions.
Section 15 in [10] abstracts Zhu linear equivalence and its inverse, by considering a pair
of the Tannakian linear equivalence E : C →Rep(A) associated to F : C →Vec and
a linear inverse equivalence S : Rep(A) →C and describes how to make Rep(A) into a
braided tensor category.
Thus, in the case of vertex operator algebras satisfying semisimplicity conditions, one
may reduce the analysis of the category of infinite dimensional representations of the vertex
operator algebra V to a category of finite dimensional representations of the Zhu algebra
A(V ) in a natural way. This transfer is the passage described in part (a) of the statement
of Theorem 3.1 for the affine vertex operator algebras at a positive integer level k.
We show in [10] that a weak quasi-tensor structure (F0, G0) can be associated to the
minimum energy functor F in the case of affine vertex operator algebras at positive integer
level. In other words at the end we shall construct natural weak quasi-tensor structures
(F, F0, G0), associated to the weak tensor structure of Wenzl functor of a corresponding
fusion category of a quantum group at a root of unity. Since the latter is a rigid and modular
tensor category, we in particular directly obtain rigidity and modularity of Rep(Vgk) from
the corresponding quantum group fusion category. In this way we rediscover a result by
Huang for the special case of affine vertex operator algebras at a positive integer level [56].
In the final sections of [10] we discuss in greater detail how Huang and Lepowsky theory
together with previous work by Frenkel and Zhu provides F naturally with the weak quasi-
tensor structure (F0, G0), such that F0 is the 0-grade part of Huang-Lepowsky tensor
structure map F.
19
We shall first identify a quantum group fusion category at a fixed suitable root of unity
with that of a corresponding affine VOA fusion category or conformal net fusion category
as pre-tensor categories, then we identify them with all the structure on special variables
which do not generate all the variables linearly. By analysis of a cohomological kind on
any braided tensor category with a generating representation, and further braid group
duality properties well studied in the literature for quantum groups, we shall extend this
identification to all variables.
We shall give a more detailed overview of our proof of
Theorem 3.1 in the following sections.
