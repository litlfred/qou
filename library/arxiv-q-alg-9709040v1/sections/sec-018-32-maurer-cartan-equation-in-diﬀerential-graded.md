---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-018-32-maurer-cartan-equation-in-diﬀerential-graded
section_title: "Maurer-Cartan equation in diﬀerential graded Lie alge bras"
section_number: 3.2
pages: 7-8
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
This part is essentially standard (see [GM], [HS1], [SS], .. .).
Let g be a diﬀerential graded Lie algebra over ﬁeld k of characteristic zero. Below we recall the list of
structures and axioms:
g =
⨁
k∈Z
gk[−k], [ , ] : gk⊗ gl−→gk+l, d : gk−→gk+1,
d(d(γ)) = 0, d[γ1,γ 2] = [dγ1,γ 2] + (−1)γ 1[γ1,dγ 2], [γ2,γ 1] =−(−1)γ 1·γ 2[γ1,γ 2],
[γ1, [γ2,γ 3]] + (−1)γ 3·(γ 1+γ 2)[γ3, [γ1,γ 2]] + (−1)γ 1·(γ 2+γ 3)[γ2, [γ3,γ 1]] = 0 .
In formulas above symbols γi∈ Z mean the degrees of homogeneous elements γi, i.e. γi∈ gγ i .
In other words, g is a Lie algebra in the tensor category of complexes of vector spaces over k. If we
forget about the diﬀerential and the grading on g, we obtain a Lie superalgebra.
7
We associate with g a functor Defg on the category of ﬁnite-dimensional commutative associat ive
algebras over k, with values in the category of sets. First of all, let us assu me that g is a nilpotent Lie
superalgebra. We deﬁne set MC(g) (the set of solutions of the Maurer-Cartan equation modulo the gauge
equivalence) by the formula
MC(g) :=
{
γ∈ g1|dγ + 1
2 [γ,γ ] = 0
} /
Γ 0
where Γ 0 is the nilpotent group associated with the nilpotent Lie alg ebra g0. The group Γ acts by aﬃne
transformations of the vector space g1. The action of Γ 0 is deﬁned by the exponentiation of the inﬁnitesimal
action of its Lie algebra:
α∈ g0↦→( ˙γ =dα + [α,γ ]) .
Now we are ready to introduce functor Defg. Technically, it is convenient to deﬁne this functor on the
category of ﬁnite-dimensional nilpotent commutative asso ciative algebras without unit. Let m be such an
algebra, mdim(m)+1 = 0. The functor is given (on objects) by the formula
Defg(m) =MC(g⊗ m) .
In the conventional approach m is the maximal ideal in a ﬁnite-dimensional Artin algebra with unit
m′ := m⊕ k· 1 .
In general, one can think about commutative associative alg ebras without unit as about objects dual to spaces
with base points. Algebra corresponding to a space with base point is the algebra of functions vanishing at
the base point.
One can extend the deﬁnition of the deformation functor to al gebras with linear topology which are
projective limits of nilpotent ﬁnite-dimensional algebra s. For example, in the deformation quantization we
use the following algebra over R:
m := ¯hR[[¯h]] = lim
←
(
¯hR[¯h]/¯hkR[¯h]
)
as k →∞ .
