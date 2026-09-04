---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-017-the-gromov-witten-formulation
section_title: "The Gromov-Witten Formulation"
section_number: null
pages: 21-23
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
The description of the correlation functions of chiral Yang-Mills theory in terms of a partial
permutation algebra enables us to provide an explicit string dual by deforming the Gromov-
Witten theory. We symbolically define this deformed Gromov-Witten theory as:
LGW→L GW−tτ 1 + log ˜Ω2−2G
u , (5.13)
where the expression of the exponential distance operator at degree d in terms of Gromov-
Witten operators can be written using equation (2.18) :
˜Ωu :=
X
r
minimal
u|r|


X
l≤|dr|
s⊢l
ζr,sg|r|−|s|
s τs−1

 . (5.14)
20
On the one hand, this deformation is implemented at the level of the string theory Lagrangian.
Therefore, the factors of the string coupling gs that appeared in the parameters of the de-
formations in equation (5.3) are absorbed by the string expansion. On the other hand, the
definition of the operator Ω in terms of Gromov-Witten operators (5.14) depends on the string
coupling. This is a consequence of the fact that the dictionary of observables between com-
pleted cycles and Gromov-Witten invariants features gs factors once the genus expansion of
the string theory is taken into account (2.18). We stress furthermore that the Ω operator is
defined as a Taylor series in gs whose dominant term is
X
r
minimal
u|r|


ℓ(r)Y
i=1
(ri− 1)!

τr−1. (5.15)
Indeed, the coefficients ζr,s with|ds| <|dr| vanish unless the condition |s| <|r| is satisfied.
This can be seen by decomposing the partial permutation orbitAr in single cycles and showing
that the inequality is obeyed by each single cycle.
The need to deform the theory by an operator that includes subdominant corrections
in the string coupling suggests that a more appropriate description of the string dual to
two-dimensional Yang-Mills theory involves a new compactification of the moduli space of
the string theory which is encoded by the exponential distance operator. Moreover, this
deformation imposes that the operators be renormalized by a factor of the inverse operator
Ω−1. We denote the renormalized operators by ˆ τr := ˜Ω−1
u
Qℓ(r)
i=1τri and define corresponding
vertex operators ˆVr := gℓ(r)
s ˆτr. The correlation functions of the deformed Gromov-Witten
theory are * nY
i=1
ˆVki
+def
:=
* nY
i=1
gsτki
!
e−tτ 1 ˜Ω2−2G−n
u
+
. (5.16)
Restricted to fixed-degrees, they match the correlators of the renormalized conjugacy classes
of the deformed Hurwitz theory (3.20), up to a factor of the string coupling which is absorbed
by the genus expansion. In terms of the Gromov-Witten vertex operators, the correlation
functions of chiral Yang-Mills theory read
Z+[MG,Ui] =
X
ri
X
si :
|dsi|≤|dri|
Y
i

ari(U)ξri,si

⟨
Y
i
ˆVsi−1⟩, (5.17)
where we have rescaled the coefficients ζ to make the string coupling factors associated with
each vertex operator manifest:
ξr,s =g|dr|−|ds|
s ζr,s. (5.18)
The duality map sends a boundary holonomyU in the chiral Yang-Mills theory to the following
infinite linear combination of vertex operators in the string theory
X
r
ar(U)
X
s
ξr,s ˆVs−1. (5.19)
The existence of the map confirms that the string theory we have defined is indeed dual to
chiral two-dimensional Yang-Mills theory.
21
To conclude our description of the string dual of chiral Yang-Mills theory, we stress that on
the torus, no deformation of the moduli space of the string theory is required. Therefore, chiral
Yang-Mills theory on the torus is exactly dual to the stationary sector of a T 2 matter model
coupled to topological gravity and deformed by transposition interactions. The dictionary of
observables is given by
U↔
X
r
ar(U)
X
s
ξr,s˜Ω−1
u Vs−1. (5.20)
