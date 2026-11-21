import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Finset.Prod
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The all-pairs charge insertion with coloured strands (bean `qou-99qc`)

The scored two-term object on `main` is the permutation-complete charge insertion
`Q_pair = Σ_{i<j} Q_i Q_j`, projected onto the braid-covariant commutant, with its scalar part on
each weight space removed (`NucleonWeightSpaceQTrace.deltaT_allPairs_connected_eq_zero`). This
file records what happens to it once strands of different charge type share a braid.

**§1. The pair-sum identity** (any commutative ring, any finite index set):
`Σ_{(i,j) ∈ offDiag} f i f j = (Σ f)² − Σ f²` (`offDiag_sum_eq`). The ordered off-diagonal sum is
`2·Q_pair`.

**§2. One charge type ⇒ the insertion is a function of the total weight** (`pairSum_eq_of_total_eq`).
If every strand carries `Q_i = t_i + y` with the same offset `y` and `t_i² = c` for all `i`, two
configurations with the same total `Σ t_i` have the same `Q_pair`. So `Q_pair` is a scalar on every
total-weight space, and its connected part vanishes against every word, for every number of strands.
This is the general-`N` form of `deltaT_allPairs_connected_eq_zero`.

**§3. Two charge types ⇒ it is not** (`pairSum_sub_of_total_eq`). With per-strand offsets `y_i`,
two configurations with the same total differ by `−2·Σ y_i (t_i − t'_i)`.

**§4. The minimal case, covariant projection included.** One quark and one lepton strand
(`Q_quark = (2/3, −1/3)`, `Q_lepton = (0, −1)` on `(u, d)`), weight space `span(ud, du)`, Jimbo
crossing `Ř = !![0,1;1,h]`. The expectation onto the commutant (`P_s`, `P_a` the isotypic
idempotents) keeps a non-scalar part: `E(Q) − (tr Q/2)·1 = κ·(P_s − P_a)` with
`κ = (q²−1)/(3(q²+1))` (`covariant_coeff_s`, `covariant_coeff_a`). Against the crossing and its
square the connected trace is `h/3` and `h²/3` (`trace_conn_crossing`, `trace_conn_crossing_sq`);
against `1` it is `0`. With two quark strands the same projection gives `0` (`quarkquark_scalar`).

Nothing here chooses the charge of a lepton strand: the lepton charges are the P4/N2 "C-lep"
assumption (a second doublet in the same `V`), stated as hypotheses of §4 by construction of `Qql`.
No numerical value enters.
-/

namespace QOU.QBeta.BetaRoutesTwoTerm

open Matrix Finset

/-! ## 1. The pair-sum identity -/

theorem offDiag_sum_eq {ι R : Type*} [DecidableEq ι] [CommRing R] (s : Finset ι) (f : ι → R) :
    ∑ p ∈ s.offDiag, f p.1 * f p.2 = (∑ i ∈ s, f i) ^ 2 - ∑ i ∈ s, f i ^ 2 := by
  have hprod : (∑ i ∈ s, f i) ^ 2 = ∑ p ∈ s ×ˢ s, f p.1 * f p.2 := by
    rw [sq, Finset.sum_mul_sum, Finset.sum_product]
  have hdiag : ∑ p ∈ s.diag, f p.1 * f p.2 = ∑ i ∈ s, f i ^ 2 := by
    rw [Finset.diag, Finset.sum_filter]
    rw [Finset.sum_product]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.sum_ite_eq]
    simp [sq, *]
  have hsplit : ∑ p ∈ s ×ˢ s, f p.1 * f p.2 =
      ∑ p ∈ s.diag, f p.1 * f p.2 + ∑ p ∈ s.offDiag, f p.1 * f p.2 := by
    rw [← Finset.sum_union (Finset.disjoint_diag_offDiag s), Finset.diag_union_offDiag]
  rw [hprod, hsplit, hdiag]; ring

/-! ## 2. One charge type -/

/-- The ordered pair sum with a common offset `y` and constant squares `t i ^ 2 = c` is an explicit
polynomial in the total `Σ t`. -/
theorem pairSum_uniform {ι R : Type*} [DecidableEq ι] [CommRing R] (s : Finset ι)
    (t : ι → R) (y c : R) (ht : ∀ i ∈ s, t i ^ 2 = c) :
    ∑ p ∈ s.offDiag, (t p.1 + y) * (t p.2 + y) =
      (∑ i ∈ s, t i + s.card * y) ^ 2 -
        (s.card * c + 2 * y * ∑ i ∈ s, t i + s.card * y ^ 2) := by
  rw [offDiag_sum_eq s (fun i => t i + y)]
  have h1 : ∑ i ∈ s, (t i + y) = ∑ i ∈ s, t i + s.card * y := by
    rw [Finset.sum_add_distrib]; simp
  have h2 : ∑ i ∈ s, (t i + y) ^ 2 = s.card * c + 2 * y * ∑ i ∈ s, t i + s.card * y ^ 2 := by
    have : ∀ i ∈ s, (t i + y) ^ 2 = c + 2 * y * t i + y ^ 2 := by
      intro i hi; rw [← ht i hi]; ring
    rw [Finset.sum_congr rfl this, Finset.sum_add_distrib, Finset.sum_add_distrib,
      ← Finset.mul_sum]
    simp only [Finset.sum_const, nsmul_eq_mul]
    try ring
  simp only [h1, h2]

/-- **One charge type: the all-pairs insertion is a function of the total weight.** Two
configurations with the same total have the same pair sum, so the insertion is a scalar on every
total-weight space and its connected part is zero against every word. -/
theorem pairSum_eq_of_total_eq {ι R : Type*} [DecidableEq ι] [CommRing R] (s : Finset ι)
    (t t' : ι → R) (y c : R) (ht : ∀ i ∈ s, t i ^ 2 = c) (ht' : ∀ i ∈ s, t' i ^ 2 = c)
    (hS : ∑ i ∈ s, t i = ∑ i ∈ s, t' i) :
    ∑ p ∈ s.offDiag, (t p.1 + y) * (t p.2 + y) =
      ∑ p ∈ s.offDiag, (t' p.1 + y) * (t' p.2 + y) := by
  rw [pairSum_uniform s t y c ht, pairSum_uniform s t' y c ht', hS]

/-! ## 3. Two charge types -/

/-- **Per-strand offsets: the insertion detects how the weight is distributed.** -/
theorem pairSum_sub_of_total_eq {ι R : Type*} [DecidableEq ι] [CommRing R] (s : Finset ι)
    (t t' y : ι → R) (c : R) (ht : ∀ i ∈ s, t i ^ 2 = c) (ht' : ∀ i ∈ s, t' i ^ 2 = c)
    (hS : ∑ i ∈ s, t i = ∑ i ∈ s, t' i) :
    ∑ p ∈ s.offDiag, (t p.1 + y p.1) * (t p.2 + y p.2) -
        ∑ p ∈ s.offDiag, (t' p.1 + y p.1) * (t' p.2 + y p.2) =
      -2 * ∑ i ∈ s, y i * (t i - t' i) := by
  rw [offDiag_sum_eq s (fun i => t i + y i), offDiag_sum_eq s (fun i => t' i + y i)]
  have hsq : ∀ (u : ι → R), (∀ i ∈ s, u i ^ 2 = c) →
      ∑ i ∈ s, (u i + y i) ^ 2 = ∑ i ∈ s, (c + 2 * (y i * u i) + y i ^ 2) := by
    intro u hu
    refine Finset.sum_congr rfl fun i hi => ?_
    rw [← hu i hi]; ring
  have hA : ∑ i ∈ s, (t i + y i) = ∑ i ∈ s, (t' i + y i) := by
    rw [Finset.sum_add_distrib, Finset.sum_add_distrib, hS]
  rw [hA, hsq t ht, hsq t' ht']
  have hXY : ∑ i ∈ s, (c + 2 * (y i * t i) + y i ^ 2) - ∑ i ∈ s, (c + 2 * (y i * t' i) + y i ^ 2)
      = 2 * ∑ i ∈ s, y i * (t i - t' i) := by
    rw [← Finset.sum_sub_distrib, Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring
  linear_combination -hXY

/-! ## 4. One quark strand and one lepton strand -/

variable {R : Type*} [Field R]

/-- The Jimbo crossing on `span(ud, du)` (columns are images: `ud ↦ du`, `du ↦ ud + h·du`). -/
def crossing (q : R) : Matrix (Fin 2) (Fin 2) R := !![0, 1; 1, q - q⁻¹]

/-- `Q_pair` on `(ud, du)` for strand 1 quark, strand 2 lepton: `(2/3)(−1)` and `(−1/3)·0`. -/
def Qql : Matrix (Fin 2) (Fin 2) R := !![-2 / 3, 0; 0, 0]

/-- `Q_pair` on `(ud, du)` for two quark strands: `(2/3)(−1/3)` on both. -/
def Qqq : Matrix (Fin 2) (Fin 2) R := !![-2 / 9, 0; 0, -2 / 9]

/-- Symmetric (`q`-eigenspace) and antisymmetric (`−q⁻¹`) idempotents of the crossing:
`P_s = (Ř + q⁻¹)/(q + q⁻¹)`, `P_a = (q − Ř)/(q + q⁻¹)`, written out. -/
def Ps (q : R) : Matrix (Fin 2) (Fin 2) R :=
  !![q⁻¹ / (q + q⁻¹), 1 / (q + q⁻¹); 1 / (q + q⁻¹), q / (q + q⁻¹)]
def Pa (q : R) : Matrix (Fin 2) (Fin 2) R :=
  !![q / (q + q⁻¹), -1 / (q + q⁻¹); -1 / (q + q⁻¹), q⁻¹ / (q + q⁻¹)]

theorem two_qd_ne (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : q + q⁻¹ ≠ 0 := by
  have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [this]; exact div_ne_zero hq2 hq

theorem Ps_def (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    Ps q = (q + q⁻¹)⁻¹ • (crossing q + q⁻¹ • (1 : Matrix (Fin 2) (Fin 2) R)) := by
  have h := two_qd_ne q hq hq2
  ext i j; fin_cases i <;> fin_cases j <;> simp [Ps, crossing] <;> field_simp <;> ring_nf

theorem Pa_def (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    Pa q = (q + q⁻¹)⁻¹ • (q • (1 : Matrix (Fin 2) (Fin 2) R) - crossing q) := by
  have h := two_qd_ne q hq hq2
  ext i j; fin_cases i <;> fin_cases j <;> simp [Pa, crossing] <;> field_simp <;> ring_nf

theorem Ps_add_Pa (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : Ps q + Pa q = 1 := by
  have h := two_qd_ne q hq hq2
  rw [Ps, Pa, Matrix.one_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp <;> ring_nf

theorem Ps_idem (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : Ps q * Ps q = Ps q := by
  have h := two_qd_ne q hq hq2
  rw [Ps, Matrix.mul_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp <;> ring_nf

theorem crossing_Ps (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    crossing q * Ps q = q • Ps q := by
  have h := two_qd_ne q hq hq2
  rw [Ps, crossing, Matrix.mul_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp <;> ring_nf

theorem crossing_Pa (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    crossing q * Pa q = (-q⁻¹) • Pa q := by
  have h := two_qd_ne q hq hq2
  rw [Pa, crossing, Matrix.mul_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp <;> ring_nf

theorem trace_Ps (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : trace (Ps q) = 1 := by
  have h := two_qd_ne q hq hq2
  rw [Ps, Matrix.trace_fin_two]; simp; field_simp; ring

theorem trace_Pa (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : trace (Pa q) = 1 := by
  have h := two_qd_ne q hq hq2
  rw [Pa, Matrix.trace_fin_two]; simp; field_simp

/-- The covariant (commutant) coefficient of the quark–lepton insertion on the symmetric block,
minus the weight-space mean `tr Q / 2 = −1/3` (needs `2 ≠ 0`). -/
theorem covariant_coeff_s (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : R) ≠ 0)
    (h3 : (3 : R) ≠ 0) :
    trace (Qql * Ps q) / trace (Ps q) - trace (Qql : Matrix (Fin 2) (Fin 2) R) / 2 =
      (q ^ 2 - 1) / (3 * (q ^ 2 + 1)) := by
  have h := two_qd_ne q hq hq2
  rw [trace_Ps q hq hq2, Qql, Ps, Matrix.mul_fin_two, Matrix.trace_fin_two, Matrix.trace_fin_two]
  simp; field_simp; ring

theorem covariant_coeff_a (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : R) ≠ 0)
    (h3 : (3 : R) ≠ 0) :
    trace (Qql * Pa q) / trace (Pa q) - trace (Qql : Matrix (Fin 2) (Fin 2) R) / 2 =
      -((q ^ 2 - 1) / (3 * (q ^ 2 + 1))) := by
  have h := two_qd_ne q hq hq2
  rw [trace_Pa q hq hq2, Qql, Pa, Matrix.mul_fin_two, Matrix.trace_fin_two, Matrix.trace_fin_two]
  simp; field_simp; ring

/-- The connected covariant insertion `κ·(P_s − P_a)`, `κ = (q²−1)/(3(q²+1))`. -/
def connQL (q : R) : Matrix (Fin 2) (Fin 2) R :=
  ((q ^ 2 - 1) / (3 * (q ^ 2 + 1))) • (Ps q - Pa q)

/-- Against the identity the connected insertion is traceless (it is a connected part). -/
theorem trace_conn_one (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trace (connQL q) = 0 := by
  rw [connQL, trace_smul, trace_sub, trace_Ps q hq hq2, trace_Pa q hq hq2]; simp

/-- **One quark–lepton crossing: the covariant connected term is `h/3`, not `0`.** -/
theorem trace_conn_crossing (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (connQL q * crossing q) = (q - q⁻¹) / 3 := by
  have h := two_qd_ne q hq hq2
  rw [connQL, Ps, Pa, crossing, Matrix.smul_mul, trace_smul, Matrix.sub_mul, trace_sub,
    Matrix.mul_fin_two, Matrix.mul_fin_two, Matrix.trace_fin_two, Matrix.trace_fin_two]
  simp; field_simp; ring

/-- **The lepton strand wrapping the quark strand once (the pure braid `σ²`): `h²/3`.** -/
theorem trace_conn_crossing_sq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (connQL q * (crossing q * crossing q)) = (q - q⁻¹) ^ 2 / 3 := by
  have h := two_qd_ne q hq hq2
  rw [connQL, Ps, Pa, crossing, Matrix.mul_fin_two, Matrix.smul_mul, trace_smul, Matrix.sub_mul,
    trace_sub, Matrix.mul_fin_two, Matrix.mul_fin_two, Matrix.trace_fin_two, Matrix.trace_fin_two]
  simp; field_simp; ring

/-- **Two quark strands: the same projection is a scalar, so the connected part is `0`.** -/
theorem quarkquark_scalar (h2 : (2 : R) ≠ 0) :
    (Qqq : Matrix (Fin 2) (Fin 2) R) - (trace (Qqq : Matrix (Fin 2) (Fin 2) R) / 2) • 1 = 0 := by
  rw [Qqq, Matrix.trace_fin_two, Matrix.one_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp <;> ring

end QOU.QBeta.BetaRoutesTwoTerm
