import QOU.QBeta.BetaRoutesTwoTerm
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic.FinCases

/-!
# The H₂ bond with the ruled electron σ₀σ₁σ₀: two structural facts (issue #8821)

Owner rulings used (`docs/coordination/owner-rulings.md`): the electron is `σ₀σ₁σ₀ ∈ B₃`
(2026-11-21), and the two-term Lagrangian trace is used (2026-11-21).

**§1. The electron's standard-block character vanishes for every `q`.** In the two-dimensional
irreducible representation of `H₃(q)` (shape `(2,1)`), with `σ ↦ q` and `σ ↦ −q⁻¹` as the two
eigenvalues, `tr ρ(σ₀σ₁σ₀) = 0` (`trace_electron_std`). So the electron passes reading 3 on its own
three strands only with equality on the `(2,1)` block. This holds for every admissible `q`, so it is
not a property of the proton pin. The matrices are checked to satisfy the quadratic relation and the
braid relation (`std_quadratic_one`, `std_quadratic_two`, `std_braid`).

**§2. The derived lepton insertion is a function of the total weight and the species counts.** The
lepton two-term insertion of PR #8743 is all pairs plus `(2/3)·Σ_ℓ Q_ℓ²`, with `Q = t + 1/6` on a
quark strand and `Q = t − 1/2` on a lepton strand, and `t² = 1/4`. Its `t`-linear terms cancel
(`derived_insertion_closed_form`). So on `V^{⊗N}` it is a scalar on every total-weight space,
whichever positions carry the leptons, and its connected part is `0` on every braid word
(`derived_insertion_eq_of_total_eq`). In particular the two-term trace of every H₂ word equals its
one-term trace. The strand charges are the "C-lep" assumption, entered here as the offsets.

No numerical value enters.

-- Ref: [manuscript] prop:ilp-covalent-bond; issue #8821; PR #8743
-/

namespace QOU.Molecular.H2RuledElectron

open Matrix Finset

variable {K : Type*} [Field K] {ι : Type*}

/-! ## 1. The standard representation of `H₃(q)` and the electron word -/

/-- `ρ(σ₀)` on the `(2,1)` block. -/
def stdOne (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 0; 0, -q⁻¹]

/-- `ρ(σ₁)` on the `(2,1)` block (a non-symmetric normalisation, so no square root is needed). -/
def stdTwo (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![-1 / (q * (q ^ 2 + 1)), 1; (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1)]

theorem std_quadratic_one (q : K) (_hq : q ≠ 0) :
    stdOne q * stdOne q = (q - q⁻¹) • stdOne q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [stdOne, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem std_quadratic_two (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    stdTwo q * stdTwo q = (q - q⁻¹) • stdTwo q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [stdTwo, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem std_braid (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    stdOne q * stdTwo q * stdOne q = stdTwo q * stdOne q * stdTwo q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [stdOne, stdTwo, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- **The electron's `(2,1)` character is `0` for every `q`.** -/
theorem trace_electron_std (q : K) (_hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trace (stdOne q * stdTwo q * stdOne q) = 0 := by
  simp [stdOne, stdTwo, Matrix.trace, Fin.sum_univ_two]
  field_simp
  ring

/-! ## 2. The derived lepton insertion -/

variable [CharZero K]

/-- Charge offset: `1/6` on a quark strand, `−1/2` on a lepton strand. -/
def offset (lep : Finset ι) [DecidableEq ι] (i : ι) : K :=
  1 / 6 - 2 / 3 * (if i ∈ lep then 1 else 0)

/-- The derived insertion of #8743: the unordered pair sum (half the ordered off-diagonal sum)
plus `(2/3)·Σ_ℓ Q_ℓ²`. -/
def derivedInsertion [DecidableEq ι] (s lep : Finset ι) (t : ι → K) : K :=
  (1 / 2) * ∑ p ∈ s.offDiag, (t p.1 + offset lep p.1) * (t p.2 + offset lep p.2) +
    2 / 3 * ∑ i ∈ lep, (t i + offset lep i) ^ 2

theorem sum_offset [DecidableEq ι] (s lep : Finset ι) (hl : lep ⊆ s) :
    ∑ i ∈ s, (offset lep i : K) = s.card / 6 - 2 / 3 * lep.card := by
  simp only [offset, Finset.sum_sub_distrib, Finset.sum_const, nsmul_eq_mul, ← Finset.mul_sum,
    Finset.sum_ite_mem, Finset.inter_eq_right.mpr hl]
  simp; ring

theorem sum_offset_mul [DecidableEq ι] (s lep : Finset ι) (hl : lep ⊆ s) (t : ι → K) :
    ∑ i ∈ s, offset lep i * t i = (∑ i ∈ s, t i) / 6 - 2 / 3 * ∑ i ∈ lep, t i := by
  have h : ∀ i, offset lep i * t i = 1 / 6 * t i - 2 / 3 * (if i ∈ lep then t i else 0) := by
    intro i; simp only [offset]; split_ifs <;> ring
  simp only [h, Finset.sum_sub_distrib, ← Finset.mul_sum, Finset.sum_ite_mem,
    Finset.inter_eq_right.mpr hl]
  ring

theorem sum_offset_sq [DecidableEq ι] (s lep : Finset ι) (hl : lep ⊆ s) :
    ∑ i ∈ s, (offset lep i : K) ^ 2 = (s.card - lep.card) / 36 + lep.card / 4 := by
  have h : ∀ i, (offset lep i : K) ^ 2 = 1 / 36 + (2 / 9) * (if i ∈ lep then 1 else 0) := by
    intro i; simp only [offset]; split_ifs <;> ring
  simp only [h, Finset.sum_add_distrib, Finset.sum_const, nsmul_eq_mul, ← Finset.mul_sum,
    Finset.sum_ite_mem, Finset.inter_eq_right.mpr hl]
  simp
  ring

/-- **Closed form.** With `t_i² = 1/4`, the derived insertion depends on the configuration only
through the total `T = Σ t_i`, the number of strands `n` and the number of lepton strands `ℓ`. -/
theorem derived_insertion_closed_form [DecidableEq ι] (s lep : Finset ι) (hl : lep ⊆ s)
    (t : ι → K) (ht : ∀ i ∈ s, t i ^ 2 = 1 / 4) :
    derivedInsertion s lep t =
      (1 / 2) * ((∑ i ∈ s, t i) + s.card / 6 - 2 / 3 * lep.card) ^ 2
        - s.card / 8 - (∑ i ∈ s, t i) / 6
        - (1 / 2) * ((s.card - lep.card) / 36 + lep.card / 4) + lep.card / 3 := by
  have hpair := QOU.QBeta.BetaRoutesTwoTerm.offDiag_sum_eq s (fun i => t i + offset lep i)
  have htot : ∑ i ∈ s, (t i + offset lep i) = (∑ i ∈ s, t i) + s.card / 6 - 2 / 3 * lep.card := by
    rw [Finset.sum_add_distrib, sum_offset s lep hl]; ring
  have hsq : ∑ i ∈ s, (t i + offset lep i) ^ 2 =
      s.card / 4 + 2 * ((∑ i ∈ s, t i) / 6 - 2 / 3 * ∑ i ∈ lep, t i)
        + ((s.card - lep.card) / 36 + lep.card / 4) := by
    have e : ∀ i ∈ s, (t i + offset lep i) ^ 2 = 1 / 4 + 2 * (offset lep i * t i)
        + offset lep i ^ 2 := by
      intro i hi; rw [← ht i hi]; ring
    rw [Finset.sum_congr rfl e, Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum,
      sum_offset_mul s lep hl, sum_offset_sq s lep hl]
    simp only [Finset.sum_const, nsmul_eq_mul]
    ring
  have hlep : ∑ i ∈ lep, (t i + offset lep i) ^ 2 = lep.card / 2 - ∑ i ∈ lep, t i := by
    have e : ∀ i ∈ lep, (t i + offset lep i) ^ 2 = 1 / 2 - t i := by
      intro i hi
      have h1 : t i ^ 2 = 1 / 4 := ht i (hl hi)
      simp only [offset, if_pos hi]
      linear_combination h1
    rw [Finset.sum_congr rfl e, Finset.sum_sub_distrib]; simp; ring
  unfold derivedInsertion
  rw [hpair, htot, hsq, hlep]
  ring

/-- **Scalar on every weight space.** Two configurations with the same total weight give the same
value, whichever strands are leptons, as long as the lepton count agrees. So the connected part of
the derived insertion is `0` against every braid word, and the two-term trace equals the one-term
trace on every H₂ word. -/
theorem derived_insertion_eq_of_total_eq [DecidableEq ι] (s lep lep' : Finset ι)
    (hl : lep ⊆ s) (hl' : lep' ⊆ s) (hc : lep.card = lep'.card) (t t' : ι → K)
    (ht : ∀ i ∈ s, t i ^ 2 = 1 / 4) (ht' : ∀ i ∈ s, t' i ^ 2 = 1 / 4)
    (hT : ∑ i ∈ s, t i = ∑ i ∈ s, t' i) :
    derivedInsertion s lep t = derivedInsertion s lep' t' := by
  rw [derived_insertion_closed_form s lep hl t ht, derived_insertion_closed_form s lep' hl' t' ht',
    hT, hc]

end QOU.Molecular.H2RuledElectron
