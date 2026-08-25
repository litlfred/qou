---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-004-h-lines-in-the-poincaré-model
section_title: "H-lines in the Poincaré model"
section_number: null
pages: 5-7
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
theory Poincare-Lines
imports Complex-Geometry.Unit-Circle-Preserving-Moebius Complex-Geometry.Circlines-Angle
begin
4.1 Deﬁnition and basic properties of h-lines
H-lines in the Poincaré model are either line segments passing trough the origin or segments (within the unit
disc) of circles that are perpendicular to the unit circle. Algebraically these are circlines that are represented
by Hermitean matrices of the form
H =
( A B
B A
)
,
5
for A ∈ R, and B ∈ C, and |B|2 >A 2, where the circline equation is the usual one: z∗Hz = 0, for homogenous
coordinates z.
deﬁnition is-poincare-line-cmat :: complex-mat⇒ bool where
[simp]: is-poincare-line-cmat H ←→
(let (A, B, C, D) = H
in hermitean (A, B, C, D)∧ A = D∧ (cmod B )2 > (cmod A )2)
lift-deﬁnition is-poincare-line-clmat :: circline-mat⇒ bool is is-poincare-line-cmat
done
We introduce the predicate that checks if a given complex matrix is a matrix of a h-line in the Poincaré model,
and then by means of the lifting package lift it to the type of non-zero Hermitean matrices, and then to circlines
(that are equivalence classes of such matrices).
lift-deﬁnition is-poincare-line :: circline⇒ bool is is-poincare-line-clmat
proof (transfer, transfer)
ﬁx H1 H2 :: complex-mat
assume hh: hermitean H1 ∧ H1⁄= mat-zero hermitean H2 ∧ H2⁄= mat-zero
assume circline-eq-cmat H1 H2
thus is-poincare-line-cmat H1 ←→ is-poincare-line-cmat H2
using hh
by (cases H1, cases H2 ) ( auto simp : norm-mult power-mult-distrib )
qed
lemma is-poincare-line-mk-circline:
assumes (A, B, C, D)∈ hermitean-nonzero
shows is-poincare-line (mk-circline A B C D )←→ (cmod B )2 > (cmod A )2∧ A = D
using assms
by (transfer, transfer, auto simp add : Let-def )
Abstract characterisation of is-poincare-line predicate: H-lines in the Poincaré model are real circlines (circlines
with the negative determinant) perpendicular to the unit circle.
lemma is-poincare-line-iﬀ:
shows is-poincare-line H ←→ circline-type H =−1∧ perpendicular H unit-circle
unfolding perpendicular-def
proof (simp, transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero
obtain A B C D where∗: H = ( A, B, C, D)
by (cases H, auto)
have∗∗: is-real A is-real D C = cnj B
using hh∗ hermitean-elems
by auto
hence (Re A = Re D ∧ cmod A∗ cmod A < cmod B ∗ cmod B ) =
(Re A∗ Re D < Re B ∗ Re B + Im B ∗ Im B ∧ (Re D = Re A∨ Re A∗ Re D = Re B ∗ Re B + Im B ∗ Im
B))
using∗
by (smt cmod-power2 power2-eq-square zero-power2 )+
thus is-poincare-line-cmat H ←→
circline-type-cmat H =− 1∧ cos-angle-cmat (of-circline-cmat H ) unit-circle-cmat = 0
using∗∗∗
by (auto simp add : sgn-1-neg complex-eq-if-Re-eq cmod-square power2-eq-square simp del : pos-oriented-cmat-def)
qed
The x-axis is an h-line.
lemma is-poincare-line-x-axis [simp]:
shows is-poincare-line x-axis
by (transfer, transfer) ( auto simp add : hermitean-def mat-adj-def mat-cnj-def )
The unit-circle is not an h-line.
lemma not-is-poincare-line-unit-circle [simp]:
shows¬ is-poincare-line unit-circle
by (transfer, transfer, simp)
6
