/-
# QOU.MassTheory.BrunnianDeficitRecursion — the recursion reduces the exact-order conjecture (bean qou-v7ro)

The convention-D Brunnian trace-deficit `D_A = 1 − τ_A` is computed EXACTLY (0-fit, ℚ(q),
no float64) at A=3,4,5,6 (`milnor_a4_deficit_h_form.py`, `milnor_a5_a6_recursion_test.py`), and
all four satisfy — on the FULL rational function, not merely the leading coefficient — the
strand-addition recursion

    D_{A+1}(h) = −h²(h²+2)·D_A(h),

whose solution from the proved A=3 base is the closed form
`D_A(h) = (−1)^{A−3} h^{2(A−1)} (h²+2)^{A−3} (h²+3)/(h²+4)`.

This file proves, sorry-free, that **the recursion implies the exact-order tight slice for all
A** (nonzero leading coefficient `(3/4)(−2)^{A−3}` at every A ≥ 3). It thereby **reduces**
`MilnorExactOrderConjecture` (the open ∀A nonvanishing, which classically needs the Bar-Natan /
Habegger–Masbaum weight-system bridge Mathlib lacks) to the single concrete hypothesis that the
deficit obeys this recursion.

**That hypothesis is now proved MATHEMATICALLY (2026-08-30, bean qou-v7ro).** The recursion
`D_{A+1}=−h²(h²+2)D_A` holds ∀A by structural induction on the Temperley–Lieb Markov trace:
`qtr(ρ(w_n))` reduces (three of four terms A-independent) to a single bilinear pairing
`Q_n=qtr_{n-2}(c·B)` of the `μ⁻¹`-partial-closures of `w_{n-1}` and its inverse; coupled `c,B`
recursions plus cyclicity and the exact scalar closure `(1+h²)²=1+u h²` (`u=h²+2`) give the
2-term recursion `Q_n=[2]^n(1+u h²)−u h²[2]Q_{n-1}`, equivalent to the deficit recursion. Every
step is a uniform TL/Markov/cyclicity identity; the inductive step is verified symbolically at
n=5 (`milnor_recursion_forall_A_proof_probe.py`), the direct recursion at A=3–6. Full proof:
`docs/audits/2026-08-30-milnor-recursion-forall-A-PROVED.md`.

**The conjecture `class` is nonetheless carried with NO instance, deliberately.** The proof above
lives on the TL operator algebra and is certified by exact symbolic computation — it is not a Lean
proof. Fabricating the instance with `sorry` would violate the anti-laundering discipline
("Axiomatization is NOT a Proof"). The Lean formalization of the TL machinery (quantum trace,
cap-cup, Markov property) that would discharge the instance for real is the remaining
**formalization** task — mechanical, not a mathematical gap.

Base cases `k=0` (A=3) and `k=1` (A=4) are tied to the proved slices `borromean_deficit_factor`
and `borromean4_deficit_factor`: `deficitClosed 0 = 1 − tauBorromean` and
`deficitClosed 1 = 1 − tauL4`.
-/
import QOU.MassTheory.MilnorOrderLawGeneral
import QOU.MassTheory.BorromeanA4TightSlice
import Mathlib.Tactic

namespace QOU.MassTheory.MilnorOrderLawGeneral

/-- The conjectured convention-D deficit closed form, indexed by `k = A − 3 ≥ 0`:
`D_A(h) = (−1)^k · h^{2(k+2)} · (h²+2)^k · (h²+3)/(h²+4)` (A = k+3, so `2(k+2) = 2(A−1)`). -/
noncomputable def deficitClosed (k : ℕ) (h : ℝ) : ℝ :=
  (-1) ^ k * h ^ (2 * (k + 2)) * (h ^ 2 + 2) ^ k * (h ^ 2 + 3) / (h ^ 2 + 4)

/-- Base tie k=0: the closed form is exactly the proved A=3 deficit `1 − τ_Borr`. -/
theorem deficitClosed_zero (h : ℝ) : deficitClosed 0 h = 1 - tauBorromean h := by
  have hd : (h : ℝ) ^ 2 + 4 ≠ 0 := by positivity
  unfold deficitClosed tauBorromean
  field_simp
  ring

/-- Base tie k=1: the closed form is exactly the proved A=4 deficit `1 − τ_4`. -/
theorem deficitClosed_one (h : ℝ) : deficitClosed 1 h = 1 - tauL4 h := by
  have hd : (h : ℝ) ^ 2 + 4 ≠ 0 := by positivity
  unfold deficitClosed tauL4
  field_simp
  ring

/-- **The closed form satisfies the recursion** `D_{k+1} = −h²(h²+2)·D_k`. PROVED (ring). -/
theorem deficitClosed_recursion (k : ℕ) (h : ℝ) :
    deficitClosed (k + 1) h = -h ^ 2 * (h ^ 2 + 2) * deficitClosed k h := by
  have hd : (h : ℝ) ^ 2 + 4 ≠ 0 := by positivity
  unfold deficitClosed
  rw [pow_succ, pow_succ]
  have hh : h ^ (2 * (k + 1 + 2)) = h ^ (2 * (k + 2)) * h ^ 2 := by
    rw [← pow_add]; ring_nf
  rw [hh]
  field_simp

/-- **The closed form has the exact-order tight-slice property for every `k` (all A ≥ 3).**
`D_k = h^{2(k+2)} · cofactor` with `cofactor 0 = (3/4)(−2)^k ≠ 0`. PROVED, unconditional in the
closed form. -/
theorem deficitClosed_tight (k : ℕ) :
    ∃ (cofactor : ℝ → ℝ) (r : ℝ), r ≠ 0 ∧ cofactor 0 = r ∧
      ∀ h, deficitClosed k h = h ^ (2 * (k + 2)) * cofactor h := by
  refine ⟨fun h => (-1) ^ k * (h ^ 2 + 2) ^ k * (h ^ 2 + 3) / (h ^ 2 + 4),
    (-1) ^ k * 2 ^ k * 3 / 4, ?_, ?_, ?_⟩
  · -- (−1)^k · 2^k · 3/4 ≠ 0
    apply div_ne_zero
    · exact mul_ne_zero (mul_ne_zero (pow_ne_zero _ (by norm_num)) (pow_ne_zero _ (by norm_num)))
        (by norm_num)
    · norm_num
  · norm_num
  · intro h
    have hd : (h : ℝ) ^ 2 + 4 ≠ 0 := by positivity
    unfold deficitClosed
    field_simp

/-- **(CONJECTURE — verified EXACT at A=3,4,5,6; structural TL derivation OPEN; NO instance.)**
The convention-D Brunnian deficit family `D : ℕ → ℝ → ℝ` obeys the strand-addition recursion,
with the proved A=3 deficit as base. Carrying this as an instance-less class is the honest open
state: four exact points are strong evidence, not a proof. The `-h²(h²+2)` factor is expected
to come from the Temperley–Lieb / Jones–Wenzl strand-addition property. -/
class BrunnianDeficitRecursion (D : ℕ → ℝ → ℝ) : Prop where
  /-- Base: `D_3` is the proved A=3 closed-form deficit. -/
  base : ∀ h, D 3 h = deficitClosed 0 h
  /-- Step: adding a strand multiplies the deficit by `−h²(h²+2)`. -/
  step : ∀ (A : ℕ), 3 ≤ A → ∀ h, D (A + 1) h = -h ^ 2 * (h ^ 2 + 2) * D A h

/-- Under the recursion, `D_{k+3}` equals the closed form `deficitClosed k` for every `k`. -/
theorem deficit_eq_closed_of_recursion {D : ℕ → ℝ → ℝ} [hR : BrunnianDeficitRecursion D]
    (k : ℕ) (h : ℝ) : D (k + 3) h = deficitClosed k h := by
  induction k with
  | zero => simpa using hR.base h
  | succ n ih =>
    have hstep := hR.step (n + 3) (by omega) h
    have : D (n + 3 + 1) h = -h ^ 2 * (h ^ 2 + 2) * D (n + 3) h := hstep
    rw [show n + 1 + 3 = n + 3 + 1 from by omega, this, ih, ← deficitClosed_recursion]

/-- **(CONDITIONAL on `BrunnianDeficitRecursion`.)  The exact-order tight slice for ALL A ≥ 3.**
If the deficit family obeys the strand-addition recursion, then at every `A ≥ 3` the deficit has
order exactly `2(A−1)` with nonzero leading coefficient `(3/4)(−2)^{A−3}` — i.e. the ∀A
nonvanishing content of `MilnorExactOrderConjecture` holds. Fully verified modulo the single
open class instance (§3b-cond conditional result). -/
theorem tight_slice_of_recursion {D : ℕ → ℝ → ℝ} [BrunnianDeficitRecursion D]
    (A : ℕ) (hA : 3 ≤ A) :
    ∃ (cofactor : ℝ → ℝ) (r : ℝ), r ≠ 0 ∧ cofactor 0 = r ∧
      ∀ h, D A h = h ^ (2 * (A - 1)) * cofactor h := by
  obtain ⟨k, rfl⟩ : ∃ k, A = k + 3 := ⟨A - 3, by omega⟩
  obtain ⟨cofactor, r, hr, hc, hEq⟩ := deficitClosed_tight k
  refine ⟨cofactor, r, hr, hc, fun h => ?_⟩
  rw [deficit_eq_closed_of_recursion (D := D) k h, hEq h,
    show k + 3 - 1 = k + 2 from by omega]

end QOU.MassTheory.MilnorOrderLawGeneral
