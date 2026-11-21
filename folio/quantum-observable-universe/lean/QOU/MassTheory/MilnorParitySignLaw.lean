/-
# The Milnor-parity sign law for A-component Brunnian binding clusters
# — consolidating #4360 (A=3, proved +) and #4378 (A=4, measured −).

The length-`A` iterated commutator (e.g. `w₃ = [[A₀₁,A₁₂]]`-type Borromean at A=3,
`w₄ = [[A₀₁,A₁₂],A₂₃]` at A=4) is a genuine `A`-component **Brunnian** link: every
proper sub-link is the unlink, yet the whole is nontrivially linked.  Its trace
deficit `1 − τ_A` against the `A`-component unlink is the irreducible `A`-body
binding cluster `c_A = E₀·(1 − τ_A)`.  Two structural features are observed:

1. **Leading Milnor order = `2(A−1)`** in `h = q − q⁻¹` (the Milnor μ̄-invariant of
   the `A`-component Brunnian link has length `A`, contributing order `2(A−1)`).
2. **Deficit sign follows a parity law** `sign(1 − τ_A) = (−1)^(A−1)`:
   A=3 → `+` (deficit positive), A=4 → `−` (deficit negative).

## Epistemic status — MADE VISIBLE IN THE TYPES (STRICT honesty, do NOT launder)

The two source facts have *different* status, and this file keeps that split
explicit rather than asserting a flat general theorem:

| Order A | source | order law | sign | how proved |
|---------|--------|-----------|------|------------|
| A=3 (Borromean, #4360) | `BorromeanThreeBodyCluster.lean` | O(h⁴)=2(3−1) | `+` | **PROVED algebraically** (closed form `1−τ_Borr = h⁴(3+h²)/(h²+4) ≥ 0`) |
| A=4 (Helium, #4378) | `HeliumBrunnianDeficitMeasured.lean` | O(h⁶)=2(4−1) (n≈6.06) | `−` | **empirically MEASURED** (τ_L₄≈1.000146>1, cited witness — NOT a closed form) |

Because the A=4 sign is *measured*, a flat
`theorem general_sign_law : sign = (−1)^(A−1)` would silently restate a measured
input as a proved premise — a "conditional-proved ≠ premise-established" /
"sorry-free ≠ derived" violation.  Instead:

* the A=3 **order + sign** are re-derived here from the closed form (sorry-free);
* the A=4 values are recorded as **measured `def`s** with a `-- Ref:` citation, NOT
  as theorems;
* the general **sign law is a CONDITIONAL theorem** (`sign_law_of_crossing`): *if*
  the parity crossing pattern (`τ_A < 1` for odd A, `τ_A > 1` for even A) holds,
  *then* `sign = (−1)^(A−1)`.  The crossing pattern is an explicit hypothesis;
* the A=3 instance discharges that hypothesis by the **proved** `τ_Borr < 1`; the
  A=4 instance by the **measured** `τ_L₄ > 1` (cited);
* the general law across *all* A is a content-bearing **conjecture class** with NO
  instance (the honest open state), and `sign_law_general` is the rigorous
  conditional result verified modulo that single open input.

Free parameters introduced: **0** (no fitted constant; the crossing pattern is a
hypothesis discharged by proved/measured facts, not a wired number).

Self-contained (imports `Mathlib.Tactic` only); the two source objects are restated
as local `def`s and cited by PR number rather than imported (matches #4378 style,
avoids building sibling oleans).

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/BorromeanThreeBodyCluster.lean (#4360; A=3 proved)
-- Ref: [leitner2026] computations/deltalambda/a4-h12-brunnian-deficit-measure.witness.json (#4378; A=4 measured τ_L₄>1)
-/
import Mathlib.Tactic

namespace QOU.MassTheory.MilnorParitySignLaw

/-! ### 1. The leading Milnor order index -/

/-- Leading Milnor order of the `A`-component Brunnian trace deficit, `2(A−1)`. -/
def leadingOrder (A : ℕ) : ℕ := 2 * (A - 1)

theorem leadingOrder_three : leadingOrder 3 = 4 := rfl
theorem leadingOrder_four : leadingOrder 4 = 6 := rfl

/-! ### 2. A=3 (Borromean, #4360): order + sign PROVED from the closed form -/

/-- The Borromean `H₃` Markov-trace closed form (restated from #4360's
`QOU.MassTheory.BorromeanThreeBodyCluster.tauBorromean`):
`τ_Borr(h) = (4 + h² − 3h⁴ − h⁶)/(h²+4)`, `h = q − q⁻¹`. -/
noncomputable def tauBorromean (h : ℝ) : ℝ := (4 + h ^ 2 - 3 * h ^ 4 - h ^ 6) / (h ^ 2 + 4)

/-- **Trace-deficit closed form** (from #4360): `1 − τ_Borr = h⁴(3 + h²)/(h² + 4)`. -/
theorem one_sub_tauBorromean (h : ℝ) :
    1 - tauBorromean h = h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := by
  unfold tauBorromean
  have hd : h ^ 2 + 4 ≠ 0 := by positivity
  field_simp
  ring

/-- **A=3 order law, PROVED.**  The deficit factors as `h^(leadingOrder 3) · r(h)`
with cofactor `r(h) = (3 + h²)/(h² + 4)` — the leading power is exactly
`h^(2(3−1)) = h⁴`. -/
theorem borromean_deficit_order (h : ℝ) :
    1 - tauBorromean h = h ^ (leadingOrder 3) * ((3 + h ^ 2) / (h ^ 2 + 4)) := by
  have h1 := one_sub_tauBorromean h
  show 1 - tauBorromean h = h ^ 4 * ((3 + h ^ 2) / (h ^ 2 + 4))
  rw [h1]; ring

/-- The A=3 cofactor is strictly positive at `h = 0` (`= 3/4 ≠ 0`): the leading
Milnor order is genuine, not an accidental extra vanishing. -/
theorem borromean_cofactor_pos_at_zero :
    (0 : ℝ) < (3 + (0 : ℝ) ^ 2) / ((0 : ℝ) ^ 2 + 4) := by norm_num

/-- **A=3 sign, PROVED.**  `τ_Borr < 1` for `h ≠ 0` (physical regime `q ≠ 1`);
hence the deficit `1 − τ_Borr > 0` and the cluster sign is `+`. -/
theorem tauBorromean_lt_one {h : ℝ} (hh : h ≠ 0) : tauBorromean h < 1 := by
  have hdef : 1 - tauBorromean h = h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := one_sub_tauBorromean h
  have hh2 : 0 < h ^ 2 := by positivity
  have h4 : 0 < h ^ 4 := by nlinarith [mul_pos hh2 hh2]
  have hnum : 0 < h ^ 4 * (3 + h ^ 2) := mul_pos h4 (by positivity)
  have hden : 0 < h ^ 2 + 4 := by positivity
  have hpos : 0 < h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := div_pos hnum hden
  linarith

/-! ### 3. A=4 (Helium, #4378): the MEASURED inputs (cited, NOT proved) -/

/-- Measured genuine-Brunnian level trace at the substrate for A=4 (#4378, cited to
`a4-h12-brunnian-deficit-measure.witness.json`, `w₄ = [[A₀₁,A₁₂],A₂₃]`):
`τ_L₄ ≈ 1.000146 > 1`.  This is an empirically MEASURED input — NOT a proved
closed form.  Its arithmetic consequence (`< 1` fails, deficit `< 0`) is all that is
used below. -/
noncomputable def tauL4Measured : ℝ := 1.000145898

theorem tauL4Measured_gt_one : 1 < tauL4Measured := by unfold tauL4Measured; norm_num

/-- Measured A=4 leading Milnor order (#4378): `n ≈ 6.06`, consistent with
`leadingOrder 4 = 6 = 2(4−1)`.  MEASURED, not proved — recorded for the record; no
theorem asserts `= 6`. -/
noncomputable def tauL4MeasuredOrder : ℝ := 6.06

/-! ### 4. The parity sign value `(−1)^(A−1)` -/

/-- Parity sign value `(−1)^(A−1)` in `ℤ` (`ℕ`-subtraction; well-defined for
`A ≥ 1`): `A=3 → +1`, `A=4 → −1`. -/
def paritySign (A : ℕ) : ℤ := (-1) ^ (A - 1)

theorem paritySign_three : paritySign 3 = 1 := by unfold paritySign; norm_num
theorem paritySign_four : paritySign 4 = -1 := by unfold paritySign; norm_num

/-- Convention lemma: for odd `A`, `(−1)^(A−1) = +1`. -/
theorem paritySign_of_odd {A : ℕ} (hA : Odd A) : paritySign A = 1 := by
  unfold paritySign
  exact (Nat.Odd.sub_odd hA odd_one).neg_one_pow

/-- Convention lemma: for even `A ≥ 1`, `(−1)^(A−1) = −1`. -/
theorem paritySign_of_even {A : ℕ} (hpos : 1 ≤ A) (hA : Even A) : paritySign A = -1 := by
  unfold paritySign
  exact (Nat.Even.sub_odd hpos hA odd_one).neg_one_pow

/-! ### 5. The parity crossing pattern + the CONDITIONAL sign law -/

/-- **Parity crossing pattern** for an `A`-component Brunnian level trace `τ`: the
deficit `1 − τ` is positive for odd `A` (`τ < 1`) and negative for even `A`
(`τ > 1`).  This is the empirically-observed / hypothesized pattern — it is used
below only as an explicit HYPOTHESIS (§3b-cond), never asserted as proved. -/
def CrossingPattern (A : ℕ) (τ : ℝ) : Prop :=
  (Odd A → τ < 1) ∧ (Even A → 1 < τ)

/-- **(CONDITIONAL sign law — the star result.)**  For `A ≥ 1`, positive energy
scale `E₀`, and a level trace `τ` satisfying the parity crossing pattern, the sign
of the `A`-body Brunnian binding cluster `c_A = E₀·(1 − τ)` equals `(−1)^(A−1)`:
positive exactly when `paritySign A = 1` (odd A), negative exactly when
`paritySign A = −1` (even A).  Nothing here is assumed proved beyond the explicit
`CrossingPattern` hypothesis. -/
theorem sign_law_of_crossing {A : ℕ} {E0 τ : ℝ}
    (hpos : 1 ≤ A) (hE : 0 < E0) (hc : CrossingPattern A τ) :
    (0 < E0 * (1 - τ) ↔ paritySign A = 1) ∧
      (E0 * (1 - τ) < 0 ↔ paritySign A = -1) := by
  rcases Nat.even_or_odd A with he | ho
  · -- even A: τ > 1 ⇒ cluster < 0, paritySign = −1
    have hτ : 1 < τ := hc.2 he
    have hcl : E0 * (1 - τ) < 0 := mul_neg_of_pos_of_neg hE (by linarith)
    have hps : paritySign A = -1 := paritySign_of_even hpos he
    refine ⟨⟨fun h => ?_, fun h => ?_⟩, ⟨fun _ => hps, fun _ => hcl⟩⟩
    · exfalso; linarith
    · rw [hps] at h; norm_num at h
  · -- odd A: τ < 1 ⇒ cluster > 0, paritySign = +1
    have hτ : τ < 1 := hc.1 ho
    have hcl : 0 < E0 * (1 - τ) := mul_pos hE (by linarith)
    have hps : paritySign A = 1 := paritySign_of_odd ho
    refine ⟨⟨fun _ => hps, fun _ => hcl⟩, ⟨fun h => ?_, fun h => ?_⟩⟩
    · exfalso; linarith
    · rw [hps] at h; norm_num at h

/-! ### 6. Instances: A=3 (hypothesis PROVED) and A=4 (hypothesis MEASURED) -/

/-- A=3 discharges the crossing hypothesis by the **PROVED** `τ_Borr < 1`. -/
theorem crossing_A3 {h : ℝ} (hh : h ≠ 0) : CrossingPattern 3 (tauBorromean h) := by
  refine ⟨fun _ => tauBorromean_lt_one hh, fun he => ?_⟩
  exact absurd he (by decide)

/-- **A=3 instance.**  The Borromean cluster is positive and `paritySign 3 = +1` —
sign `+`, fully PROVED (order + sign, from #4360's closed form). -/
theorem sign_law_A3 {E0 h : ℝ} (hE : 0 < E0) (hh : h ≠ 0) :
    0 < E0 * (1 - tauBorromean h) ∧ paritySign 3 = 1 := by
  have hlaw := sign_law_of_crossing (A := 3) (by norm_num) hE (crossing_A3 hh)
  exact ⟨hlaw.1.mpr paritySign_three, paritySign_three⟩

/-- A=4 discharges the crossing hypothesis by the **MEASURED** `τ_L₄ > 1` (#4378,
cited).  This is NOT a proved closed form — the input is the measurement. -/
theorem crossing_A4 : CrossingPattern 4 tauL4Measured := by
  refine ⟨fun ho => ?_, fun _ => tauL4Measured_gt_one⟩
  exact absurd ho (by decide)

/-- **A=4 instance.**  The genuine Brunnian cluster is negative and
`paritySign 4 = −1` — sign `−`, with the crossing hypothesis discharged by
MEASUREMENT (τ_L₄ > 1), not proof.  The `(−1)^(A−1)` convention is confirmed at the
second data point. -/
theorem sign_law_A4_measured {E0 : ℝ} (hE : 0 < E0) :
    E0 * (1 - tauL4Measured) < 0 ∧ paritySign 4 = -1 := by
  have hlaw := sign_law_of_crossing (A := 4) (by norm_num) hE crossing_A4
  exact ⟨hlaw.2.mpr paritySign_four, paritySign_four⟩

/-- **Both confirmed data points together — the A=3→A=4 Milnor-parity sign flip.**
`paritySign 3 = +1` (deficit `+`, PROVED) and `paritySign 4 = −1` (deficit `−`,
MEASURED): the sign alternates with `A` per `(−1)^(A−1)` across the two orders for
which the crossing pattern is confirmed. -/
theorem parity_sign_flip_a3_a4 : paritySign 3 = 1 ∧ paritySign 4 = -1 :=
  ⟨paritySign_three, paritySign_four⟩

/-! ### 7. The general law across ALL A — OPEN conjecture (no instance) -/

/-- **(CONJECTURE, primary — OPEN.)**  The general Milnor-parity sign law, stated
for a candidate `A`-indexed Brunnian level-trace family `τ : ℕ → ℝ → ℝ`
(`τ A h` = level trace of the length-`A` iterated commutator at `h = q − q⁻¹`):
the parity crossing pattern holds at *every* Brunnian order `A ≥ 2` and every
nonzero `h`.  For the *actual* Brunnian Markov-trace family this asserts the
universal alternation `sign(1 − τ_A) = (−1)^(A−1)`.

This carrier has **NO instance** — the honest open state — because the pattern is
confirmed at only two orders (A=3 PROVED, A=4 MEASURED; #4360/#4378) and no general
topological derivation of the order law or the crossing sign exists in the corpus.
Fabricating an instance would launder the two-point pattern into a universal claim
(forbidden by the anti-laundering discipline).  The field is content-bearing (a
parameter-quantified inequality in the shape of the claim), not an empty marker. -/
class MilnorParitySignConjecture (τ : ℕ → ℝ → ℝ) : Prop where
  /-- The parity crossing pattern at every Brunnian order `A ≥ 2` and nonzero `h`. -/
  crossing : ∀ (A : ℕ), 2 ≤ A → ∀ (h : ℝ), h ≠ 0 → CrossingPattern A (τ A h)

/-- **(CONDITIONAL on the conjecture.)**  If the Milnor-parity conjecture holds for a
trace family `τ`, then at every Brunnian order `A ≥ 2` (with `E₀ > 0`, `h ≠ 0`) the
binding cluster `E₀·(1 − τ A h)` has sign `(−1)^(A−1)`.  Fully verified by Lean
modulo the single open class instance `MilnorParitySignConjecture τ` (§3b-cond
conditional result — the conjecture is the only unproved input). -/
theorem sign_law_general {τ : ℕ → ℝ → ℝ} [hc : MilnorParitySignConjecture τ]
    {A : ℕ} {E0 h : ℝ} (hA : 2 ≤ A) (hE : 0 < E0) (hh : h ≠ 0) :
    (0 < E0 * (1 - τ A h) ↔ paritySign A = 1) ∧
      (E0 * (1 - τ A h) < 0 ↔ paritySign A = -1) :=
  sign_law_of_crossing (le_trans (by norm_num) hA) hE (hc.crossing A hA h hh)

end QOU.MassTheory.MilnorParitySignLaw
