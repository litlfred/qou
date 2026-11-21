---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-101-c3-matricial-description-of-filtered-difference
section_title: "Matricial description of filtered difference modules"
section_number: C.3
pages: 149-151
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
Pi = (Gi, Ψi) (1 ≤i ≤k) be diﬀerence modules such that each K-module Gi is
free of ﬁnite rank ri . For each Gi, choose a basis Di, and write Bi ∈GLri(K)
the invertible matrix such that Ψi(Di) = DiBi.
Let M be a ﬁnitely ﬁltered diﬀerence module with associated graded module
P = P1 ⊕· · · ⊕Pk; more precisely, M = (0 = M0 ⊂M1 ⊂· · · ⊂Mk = M) is
equipped with an isomorphism u = (ui : Mi/Mi−1 ≃Pi)1≤i≤k from grM to P.
Letting Mi = (Ei, Φi), one builds a basis Bi of Ei by induction on i = 1, . . . , k
in such a way that Bi−1 ⊂Bi and that B′
i := Bi \ Bi−1 lifts Di via ui (showing
by the way that K-modules Ei are free of ﬁnite ranks r1 + · · · + ri). Write
Φi (resp. Φi) the semi-linear automorphism induced by Φ (resp. by Φi) on
Ei (resp. on Ei/Ei−1), and Ci the basis of Ei/Ei−1 induced by B′
i, one draws
from equality ui ◦Φi = Ψi ◦ui (due to the fact that ui is a morphism) the
relation: Φi(Ci) = CiBi, then, from the latter, the relation:
Φi(B′
i) ≡B′
iBi
(mod Ei−1).
Last, one gets that the matrix of Φ in basis B is block upper-triangular:
Φ(B) = B



B1
⋆
⋆
0
...
⋆
0
0
Bk


.
144
APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFERENCE MODULES
As in A.3.2, we identify Pi (1 ≤i ≤k) with (Kri, ΦAi), where Ai := B−1
i
∈
GLri(K).
Likewise, P is identiﬁed with (Kn, ΦA0) and M with (Kn, ΦA),
where n := r1 + · · · + rk and:
A0 =



A1
0
0
0
...
0
0
0
Ak



et A =



A1
⋆
⋆
0
...
⋆
0
0
Ak


.
Note that these relations implicitly presuppose that a ﬁltration on M is given,
as well as an isomorphism from grM to P.
If moreover M′ = (Kn, ΦA′),
where A′ has the same form as A (i.e. M′ is ﬁltered and equipped with an
isomorphism from grM′ to P), then, a morphism from M to M′ respecting
ﬁltrations (i.e. sending each Mi into M′
i) is described by a matrix F in the
following block upper triangular form; and the induced endomorphism of P ≃
grM ≃grM′ is described by the corresponding block diagonal matrix F0
F =



F1
⋆
⋆
0
...
⋆
0
0
Fk



et F0 =



F1
0
0
0
...
0
0
0
Fk


.
In particular, a morphism inducing identity on P (thus ensuring that the ﬁl-
tered modules M, M′ belong to the same class in F(P1, . . . , Pk)) is represented
by a matrix in G(K), where we denote G the algebraic subgroup of GLn de-
ﬁned by the following shape:



Ir1
⋆
⋆
0
...
⋆
0
0
Irk


.
(The unipotent algebraic group G was previously introduced in paragraph
2.3.3, page 26.)
Now write AU the block upper triangular matrix with block diagonal com-
ponent A0 and with upper triangular blocks the Ui,j ∈Matri,rj(K) (1 ≤i <
j ≤k); here, U is an abrevation for the family (Ui,j). For all F ∈G(K), the
matrix F[AU] is equal to AV for some family of Vi,j ∈Matri,rj(K). Thus, the
group G(K) operates on the set
Q
1≤i<j≤k
Matri,rj(K). The above discussion
can be summarised as follows:
