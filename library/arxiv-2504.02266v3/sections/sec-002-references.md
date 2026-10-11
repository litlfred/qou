---
doc_id: arxiv-2504.02266v3
doc_title: "Knizhnik-Zamolodchikov equations in Deligne categories"
section_id: sec-002-references
section_title: "References"
section_number: null
pages: 1-2
source_pdf: 2504.02266v3.pdf
source_sha256: a12193f740b6ee53
toc_source: inferred
---
19
1. Introduction
The Knizhnik-Zamolodchikov (KZ) connection is an important object in representation
theory of affine Lie algebras and quantum groups. Namely, for an arbitrary simple Lie
algebra g we may consider a connection ∇𝐾𝑍on a base space
C𝑟∖
⋃︁
1≤𝑖<𝑗≤𝑟
{𝑧∈C𝑟|𝑧𝑖−𝑧𝑗= 0}
(1.1)
given by
∇𝐾𝑍= 𝑑−ℏ
∑︁
1≤𝑖<𝑗≤𝑟
𝑑(𝑧𝑖−𝑧𝑗)
𝑧𝑖−𝑧𝑗
Ω𝑖𝑗,
(1.2)
where ℏ∈C and Ω𝑖𝑗∈𝑈(g)⊗𝑟is equal to
Ω𝑖𝑗=
∑︁
1≤𝑎≤dim(g)
1(1)⊗· · ·⊗1(𝑖−1)⊗𝑒(𝑖)
𝑎⊗1(𝑖+1)⊗· · ·⊗1(𝑗−1)⊗𝑒𝑎(𝑗)⊗1(𝑗+1)⊗· · ·⊗1(𝑟) (1.3)
1
arXiv:2504.02266v3  [math.RT]  30 Jun 2026
2
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
and 𝑒𝑎, 𝑒𝑎are dual bases in g. The Knizhnik-Zamolodchikov connection admits an obvious
generalization to the case of general linear Lie algebras gl𝑛.
Instead of working with 𝑈(g)⊗𝑟as a fiber of the trivial vector bundle with the base
(1.1), we choose to work with g-modules 𝑉1, . . . , 𝑉𝑟. We may choose a Cartan subalgebra
h for g. Then, since the action of g on 𝑉1 ⊗· · · ⊗𝑉𝑟commutes with Ω𝑖𝑗and since the
operators Ω𝑖𝑗have weight 0 with respect to g, it makes sense to restrict the connection
to a weight space
(𝑉1 ⊗· · · ⊗𝑉𝑟)[𝜇] ⊂𝑉1 ⊗· · · ⊗𝑉𝑟,
𝜇∈h*.
(1.4)
If we slightly deform the KZ connection and look for the flat sections of ∇𝐾𝑍on (1.4),
one can write a system of compatible dynamical equations and integral solutions which
satisfy both the KZ and the dynamical equations (see [17][Theorems 3.1, 3.2]).
The Deligne categories Rep(𝐺𝐿𝑡), Rep(𝑂𝑡) for a parameter 𝑡∈C are certain inter-
polations of the representation categories of the classical algebraic groups 𝐺𝐿𝑛and 𝑂𝑛
respectively ([6, 12]). It is possible to produce a pencil of KZ connections in the setting of
Deligne categories depending on the parameter 𝑡([15][Section 5.1.4]). Therefore, we may
look for the flat sections of the KZ equations in this case as well. A direct application of
the approach in [17] fails since there are no weight spaces (1.4) in Deligne categories. Nev-
ertheless, it is possible to find a certain (gl𝑚, gl𝑛)-duality which allows us to write integral
formulas for the solutions to the KZ equations for all noninteger and large enough integer 𝑡.
In the case of Rep(𝑂𝑡), we can produce a similar (so𝑚, so2𝑛)-duality.
It gives us a
new flat connection (5.19) which can be obtained by a suitable reduction of the boundary
Casimir connection in [3][Formula (10.9)]. However, finding flat sections of the orthogonal
KZ for Deligne categories or the new connection is an open problem.
Conjecturally (see [15]), all periodic pencils should admit integral formulas for solu-
tions. Indeed, since they are quasi-geometric for rational values of parameters, Simpson
conjectures ([24]) imply that they are actually geometric. Also, they have nilpotent 𝑝-
curvature at rational parameters, so Andr´e-Bombieri-Dwork conjectures ([1, 4, 11]) would
imply that the periodic pencils are geometric. Although, there are examples where such
formulas aren’t known (e.g. Dunkl connections for exceptional groups). In particular,
we check that for KZ equations in Deligne categories the Simpson and Andr´e-Bombieri-
Dwork conjectures indeed hold.
The Drinfeld-Kohno theorem (e.g. see [9, 10, 14]) states that one can compute the mon-
odromy of the KZ equations in terms of quantum 𝑅-matrices. We show that this result
can be generalized in the context of Deligne categories and their quantizations known as
skein categories.
A starting point of this project was an observation in [25] that the asymptotics of
hypergeometric integrals, as their dimension tends to infinity, can be analyzed in some
examples using the steepest descent method applied to other hypergeometric integrals of
fixed dimension.
