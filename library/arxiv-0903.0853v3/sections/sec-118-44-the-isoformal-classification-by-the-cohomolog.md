---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-118-44-the-isoformal-classification-by-the-cohomolog
section_title: "THE ISOFORMAL CLASSIFICATION BY THE COHOMOLOGY OF THE S TOKES SHEAF65"
section_number: 4.4
pages: 71-73
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
whence a natural bijective mapping:
F(M0)→H 1(
Eq; ΛI(M0)
)
.
Proof. — The map λ
Let U := (Ui)i∈I be a good open covering of Eq.
Let ˆF ∈ GLM0
n ⊂ GLn
(
C[[z]]
)
; by deﬁnition there exists an unique A∈
GLn
(
C{z}
)
such that ˆF[A0] =A.
For alli∈I, there exists gi∈ GLn
(
A(Ui)
)
asymptotic to ˆF onUi (cf. theo-
rem 4.2.1). The coboundary (gij) of the cochain (gi) belongs toZ 1(U, ΛI(M0))
(the reason for that is lemma 4.2.7 which can be applied because the condition
of good covering implies that the open sets are adequate); it does not change
if we multiply ˆF on the right by an element of GL n
(
C{z}
)
. If we change the
representativesgi, we get another cochain inZ 1(U, ΛI(M0)) inducing the same
element of H 1(U, ΛI(M0)). We thus get a natural map:
λ : GLM0
n
(
C[[z]]
)
/GLn
(
C{z}
)
→H 1(
Eq; ΛI(M0)
)
.
This map is injective.
Surjectivity of λ
Let U := (Ui)i∈I be a good open covering of Eq; assume
moreover that the compact covering (U i)i∈I is good and that the Ui are small
parallelograms.
Let γ ∈ H 1(Eq; ΛI(M0)); we can represent it by an element g ∈
Z 1(U; ΛI(M0), U = (Ui)i∈I being a good open covering of Eq. Moreover
we can choose U such that the compact covering ( U i)i∈I is good and such
that the Ui are small parallelograms.
As in section 4.3.1, usingg, we can build a germ of analytic manifoldMg and
a holomorphic ﬁbration π : Mg→ (C, 0). But now there is a new ingredient:
we have a holomorphic automorphism Θ 0 : (C, 0)× Cn→ (C, 0)× Cn of the
trivial bundle
(
(C, 0)× Cn,π 0, (C, 0)
)
deﬁned by:
(z,X )↦→(qz,A 0X).
It induces, for all i∈ I a holomorphic automorphism of ﬁbre bundles Θ 0,i :
Ui× Cn→Ui.
By deﬁnition the gij∈ ΛI(M0)(Uij) commute with Θ 0, therefore the auto-
morphisms Θ0,i glue together into a holomorphic automorphism Ψ of the germ
of ﬁbered manifold
(
Mg,π, (C,{0})
)
. The map Ψ is linear on the ﬁbers and
the map on the basis is the germ of z↦→qz.
We choose a holomorphic trivialisation H of the germ of ﬁber bundle(
Mg,π, (C, 0)
)
: π0◦H = π. The map Φ := H◦ Ψ◦H −1 is a holomorphic
66 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
automorphism of the germ of trivial bundle
(
(C, 0)× Cn,π 0, (C, 0)
)
, it cor-
responds to an element A∈ GLn
(
C{z}
)
. Using the results and notations of
section 4.3.1, we see that there exists an element ˆ ϕ∈ GLn
(
C{z}
)
such that
g↦→ˆϕ−1 induces the inverse of the natural map GL n
(
C[[z]]
)
/GLn
(
C{z}
)
→
H 1(
Eq; ΛI
)
. If we set ˆF := ˆϕ−1, it is easy to check that ˆF[A0] =A. We have
ˆF∈ GLM0
n and λ( ˆF) =g, therefore λ is surjective.
CHAPTER 5
SUMMATION AND ASYMPTOTIC THEORY
To ﬁnd analytic solutions having a given formal solution as a symptotic
expansion is a rather old subject in the theory of q-diﬀerence equations: see
for instance the paper [55] by Trjitzinsky in 1933. The ﬁrst author had already
suggested in [37] the use of the gaussian function to formulate aq-analogue for
Laplace transform; this allowed to ﬁnd in [ 58] the Gq-summation, a q-analog
of the exponential summation method of Borel-Laplace. In [ 31], the Gq-
summation was extended to the case of multiple levels, and it was shown that
any formal power series solution of a linear equation with an alytic coeﬃcients
isGq-multisummable, and thus can be seen as the asymptotic expansion of an
analytical solution in a sector with inﬁnite opening in the R iemann surface of
the logarithm. The work in [ 43] [42], [61], [59] was undertaken with the goal
of obtaining a summation over the elliptic curve, or a ﬁnite c overing of it (1).
