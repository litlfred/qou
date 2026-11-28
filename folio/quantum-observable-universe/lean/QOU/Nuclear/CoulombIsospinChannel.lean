import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.Prod
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# The Coulomb (EM, rank ≤ 2) channel on the nucleus block — gap G3

Audit `docs/audits/2026-11-27-coulomb-isospin-channel.md`. Bean `qou-tcl3`. This is gap **G3**
of the term-completeness ledger (`docs/audits/2026-11-27-term-completeness-ledger.md`, PR #9658):
the binding formula had no `em` entry at level `3A`. The ledger's cap table says the `em`
channel is the two-body charge operator `Σ_{i<j} Q_i Q_j`, with ranks `r = 0, 1, 2`, and that a
multiplet's `T_z` dependence is therefore `a + b·T_z + c·T_z²`. This file computes `a`, `b`, `c`.

Convention: `T_z = (Z − N)/2` (proton `+½`), the convention of
`BraidKnotOctonion/DeltaLambdaIMME.lean`, whose `imme a b c T₃ = a + b·T₃ + c·T₃²` is restated
here as `imme` (same definition) so that this file depends on Mathlib only.

## What is proved (generic field, no measured value)

* `pairSum_eq`: the ordered pair sum `Σ_{i ≠ j} x_i x_j = (Σ x)² − Σ x²` over any finset.
* `pairSum_of_idem`: if every charge is `0` or `1` (`x² = x`), it is `Z² − Z`, with `Z = Σ x`.
  So the nucleon-level charge operator has eigenvalue `Z(Z − 1)/2` on unordered pairs.
* `chargePairs_imme`: with `A = Z + N`, `T_z = (Z − N)/2`,
  `Z(Z − 1)/2 = a + b·T_z + c·T_z²` with
  `a = A(A − 2)/8`, `b = (A − 1)/2`, `c = 1/2`.
  These are exact rationals in `A`: **the charge structure of all three entries is derived**.
* `quark_pairSum_split`: on `n = 3A` quark strands, the quark pair sum splits exactly into the
  nucleon pair sum of the block charges plus one internal term per nucleon.
  `proton_internal`, `neutron_internal`: with the model charges `2/3, −1/3` the internal
  (ordered) terms are `0` (uud) and `−2/3` (udd). The internal piece is the nucleon's own EM
  self-energy (gap G1, the `m_n − m_p` EM piece); it is linear in `N` and does not enter the
  inter-nucleon binding.
* `emEnergy_imme`: with **one** EM pair weight `ε` (its own scale, not the strong map `E`),
  the EM channel is `ε·a + ε·b·T_z + ε·c·T_z²`. So one number `ε` sizes all three entries, and
  the ratios `b/c = A − 1`, `a/c = A(A − 2)/4` are fixed (`emB_eq`, `emA_eq`).
* `emEnergy_mirror`: the mirror split is `ε·(A − 1)·T_z`; at `A = 3`, `T_z = ½` it is `ε`.
* `imme_rank_split`, `rank_one_multiplet_sum`, `rank_two_multiplet_sum`: inside an isospin
  multiplet `T = d/2` (`T_z = k − d/2`, `k = 0..d`), `T_z² = (T_z² − T(T+1)/3) + T(T+1)/3`;
  the rank-1 and rank-2 pieces sum to zero over the multiplet (characteristic 0), so the rank-0
  (multiplet-average) EM entry is `ε·(a + T(T+1)/6)`. The EM channel therefore also feeds the block term
  `T(T+1)` (gap G2).

## What is not proved, and is named

* The single pair weight `ε` is the Hartree reading: one spatial pair expectation for every
  proton pair. Pair-isospin-dependent weights (exchange, correlation) would give the three
  ranks separate weights. That residual is a named summand, not a free parameter here.
* `ε = 2 f α ħc / r_rms`: `f` is the q-Hankel shape factor (PR #9665), `α` is derived
  (conditional on the unproved CS Gram-ratio identification, bean `qou-wkgp`; the old Witten-κ Gram `sorry` was refuted and removed 2026-11-20), and `r_rms` is **open**: the corpus has no
  derived energy-to-length map (bean `qou-mbfv`, `qou-usft`). Nothing here fixes it.
-/

namespace QOU.Nuclear.CoulombIsospinChannel

open Finset

variable {K : Type*} [Field K]

section PairSum

variable {ι : Type*} [DecidableEq ι]

/-- The ordered pair sum `Σ_{i ∈ s} Σ_{j ∈ s, j ≠ i} x_i x_j` (twice the unordered sum). -/
def pairSum (s : Finset ι) (x : ι → K) : K :=
  ∑ i ∈ s, ∑ j ∈ s.erase i, x i * x j

/-- `Σ_{i ≠ j} x_i x_j = (Σ x)² − Σ x²`. -/
theorem pairSum_eq (s : Finset ι) (x : ι → K) :
    pairSum s x = (∑ i ∈ s, x i) ^ 2 - ∑ i ∈ s, x i ^ 2 := by
  unfold pairSum
  have h : ∀ i ∈ s, ∑ j ∈ s.erase i, x i * x j = x i * (∑ j ∈ s, x j) - x i ^ 2 := by
    intro i hi
    rw [← Finset.mul_sum, Finset.sum_erase_eq_sub hi]
    ring
  rw [Finset.sum_congr rfl h, Finset.sum_sub_distrib, ← Finset.sum_mul]
  ring

/-- Charges in `{0, 1}` (`x² = x`): the ordered pair sum is `Z² − Z`, `Z = Σ x`. -/
theorem pairSum_of_idem (s : Finset ι) (x : ι → K) (hx : ∀ i ∈ s, x i ^ 2 = x i) :
    pairSum s x = (∑ i ∈ s, x i) ^ 2 - ∑ i ∈ s, x i := by
  rw [pairSum_eq, Finset.sum_congr rfl hx]

end PairSum

section QuarkLevel

variable {β : Type*} [DecidableEq β]

/-- On `3A` quark strands (`β` labels nucleons, `Fin 3` the strands of one nucleon), the quark
pair sum is the pair sum of the nucleon charges plus one internal term per nucleon. -/
theorem quark_pairSum_split (s : Finset β) (x : β × Fin 3 → K) :
    pairSum (s ×ˢ (univ : Finset (Fin 3))) x
      = pairSum s (fun b => ∑ k, x (b, k)) + ∑ b ∈ s, pairSum univ (fun k => x (b, k)) := by
  simp only [pairSum_eq, Finset.sum_product, Finset.sum_sub_distrib]
  ring

/-- Internal pair sum of a `uud` block with charges `2/3, 2/3, −1/3`: zero. -/
theorem proton_internal [CharZero K] :
    pairSum (univ : Finset (Fin 3)) (![2/3, 2/3, -1/3] : Fin 3 → K) = 0 := by
  rw [pairSum_eq]
  simp [Fin.sum_univ_three]
  norm_num

/-- Internal (ordered) pair sum of a `udd` block with charges `2/3, −1/3, −1/3`: `−2/3`. -/
theorem neutron_internal [CharZero K] :
    pairSum (univ : Finset (Fin 3)) (![2/3, -1/3, -1/3] : Fin 3 → K) = -2/3 := by
  rw [pairSum_eq]
  simp [Fin.sum_univ_three]
  norm_num

end QuarkLevel

section IMME

/-- The IMME polynomial `a + b·T_z + c·T_z²` (same as `QOU.BraidKnot.imme`). -/
def imme (a b c Tz : K) : K := a + b * Tz + c * Tz ^ 2

/-- Mirror difference isolates the linear coefficient (as `QOU.BraidKnot.imme_mirror_diff`). -/
theorem imme_mirror_diff (a b c Tz : K) : imme a b c Tz - imme a b c (-Tz) = 2 * b * Tz := by
  unfold imme; ring

/-- Isoscalar EM charge coefficient `a = A(A − 2)/8`. -/
def emA (A : K) : K := A * (A - 2) / 8
/-- Isovector EM charge coefficient `b = (A − 1)/2`. -/
def emB (A : K) : K := (A - 1) / 2
/-- Isotensor EM charge coefficient `c = 1/2`. -/
def emC : K := 1 / 2

/-- **The EM charge structure is IMME, with derived coefficients.**
`Z(Z − 1)/2 = A(A − 2)/8 + (A − 1)/2 · T_z + 1/2 · T_z²` for `A = Z + N`, `T_z = (Z − N)/2`. -/
theorem chargePairs_imme [CharZero K] (Z N A Tz : K) (hA : A = Z + N) (hT : Tz = (Z - N) / 2) :
    Z * (Z - 1) / 2 = imme (emA A) (emB A) emC Tz := by
  subst hA hT
  unfold imme emA emB emC
  field_simp
  ring

/-- `b = (A − 1)·c`. -/
theorem emB_eq (A : K) : emB A = (A - 1) * emC := by
  unfold emB emC; ring

/-- `a = A(A − 2)/4 · c`. -/
theorem emA_eq [CharZero K] (A : K) : emA A = A * (A - 2) / 4 * emC := by
  unfold emA emC; field_simp; ring

/-- The EM channel with one pair weight `ε`: `ε·Z(Z − 1)/2`. -/
def emEnergy (ε Z : K) : K := ε * (Z * (Z - 1) / 2)

/-- **One EM scale sizes all three entries.** -/
theorem emEnergy_imme [CharZero K] (ε Z N A Tz : K) (hA : A = Z + N) (hT : Tz = (Z - N) / 2) :
    emEnergy ε Z = imme (ε * emA A) (ε * emB A) (ε * emC) Tz := by
  rw [emEnergy, chargePairs_imme Z N A Tz hA hT]
  unfold imme
  ring

/-- **Mirror split.** `E(T_z) − E(−T_z) = ε·(A − 1)·T_z`. -/
theorem emEnergy_mirror [CharZero K] (ε A Tz : K) :
    imme (ε * emA A) (ε * emB A) (ε * emC) Tz - imme (ε * emA A) (ε * emB A) (ε * emC) (-Tz)
      = ε * (A - 1) * Tz := by
  rw [imme_mirror_diff]
  unfold emB
  field_simp

/-- At `A = 3` (³H/³He), the mirror split is exactly one pair weight `ε`. -/
theorem emEnergy_mirror_A3 [CharZero K] (ε : K) :
    imme (ε * emA 3) (ε * emB 3) (ε * emC) (1 / 2)
      - imme (ε * emA 3) (ε * emB 3) (ε * emC) (-(1 / 2)) = ε := by
  rw [emEnergy_mirror]
  field_simp
  ring

end IMME

section RankSplit

/-- **Rank split inside a multiplet of isospin `T`.**
`a + b T_z + c T_z² = (a + c·T(T+1)/3) + b·T_z + c·(T_z² − T(T+1)/3)`:
rank 0, rank 1, rank 2. -/
theorem imme_rank_split (a b c T Tz : K) :
    imme a b c Tz = (a + c * (T * (T + 1)) / 3) + b * Tz + c * (Tz ^ 2 - T * (T + 1) / 3) := by
  unfold imme
  ring

theorem two_mul_sum_range (n : ℕ) : 2 * ∑ k ∈ range n, (k : K) = n * (n - 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    push_cast
    ring

theorem six_mul_sum_range_sq (n : ℕ) :
    6 * ∑ k ∈ range n, (k : K) ^ 2 = n * (n - 1) * (2 * n - 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    push_cast
    ring

/-- **The rank-1 piece averages to zero over a multiplet.** `T = d/2`, `T_z = k − d/2`. -/
theorem rank_one_multiplet_sum [CharZero K] (d : ℕ) :
    ∑ k ∈ range (d + 1), ((k : K) - d / 2) = 0 := by
  have h1 := two_mul_sum_range (K := K) (d + 1)
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  push_cast at h1 ⊢
  linear_combination h1 / 2

/-- **The rank-2 piece averages to zero over a multiplet.** `T = d/2`, `T_z = k − d/2`:
`Σ_k ((k − d/2)² − T(T+1)/3) = 0`. -/
theorem rank_two_multiplet_sum [CharZero K] (d : ℕ) :
    ∑ k ∈ range (d + 1),
      (((k : K) - d / 2) ^ 2 - ((d : K) / 2) * ((d : K) / 2 + 1) / 3) = 0 := by
  have h1 := two_mul_sum_range (K := K) (d + 1)
  have hsq := six_mul_sum_range_sq (K := K) (d + 1)
  have e : ∀ k ∈ range (d + 1),
      (((k : K) - d / 2) ^ 2 - ((d : K) / 2) * ((d : K) / 2 + 1) / 3)
        = (k : K) ^ 2 - d * (k : K) + (((d : K) / 2) ^ 2 - ((d : K) / 2) * ((d : K) / 2 + 1) / 3) := by
    intro k _; ring
  rw [Finset.sum_congr rfl e, Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum,
    Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  push_cast at h1 hsq ⊢
  linear_combination hsq / 6 - (d : K) * h1 / 2

/-- **Multiplet-average EM entry.** With one pair weight `ε`, the rank-0 EM entry of the block
`T` is `ε·(A(A − 2)/8 + (1/2)·T(T + 1)/3)`, i.e. `ε·(a + c·T(T+1)/3)`. -/
theorem em_rank_zero (ε A T : K) :
    ε * emA A + ε * emC * (T * (T + 1)) / 3
      = ε * (A * (A - 2) / 8 + 1 / 2 * (T * (T + 1)) / 3) := by
  unfold emA emC
  ring

end RankSplit

end QOU.Nuclear.CoulombIsospinChannel
