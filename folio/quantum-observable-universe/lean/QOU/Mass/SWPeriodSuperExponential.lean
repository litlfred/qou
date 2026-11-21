import Mathlib.Tactic
import QOU.BraidKnot.KeystoneC8SuperExpBound

/-!
# QOU.Mass.SWPeriodSuperExponential — the SW-period magnitude, from below

Input **(1)** of the scope note of `prop:jet-filtration-binding-extensive`: the
*super-exponential magnitude* of the prolonged Seiberg–Witten period `a_D^(n)`.
`prop:jet-filtration-binding-extensive` carries `0 ≤ a_D^(n)` as a bare
**hypothesis**; `QOU.Mass.JetFiltrationExtensive` says so in as many words
("carried here as abstract non-negativity/positivity hypotheses on `aD`, `w` —
not derived"). This file derives the *growth*, not merely the sign.

## The reduction

At `q = 1` the period is the mean involution number,

  `a_D^(n)|_{q=1} = lw(n−1) = I(n)/n`,   `I` = OEIS A000085,

(`prop:sw-classical-jet-exactness`, which already states `a_D^(m) = lw(m−1) = I(m)/m`
and uses only `I(m) ≠ 0`). So the magnitude question at `q = 1` is a question about
`I`, and `I` is a concrete `ℕ`-valued recurrence — no geometry, no `q`, no anchor.

`QOU.BraidKnot.KeystoneC8SuperExpBound` already carries `I` and its **upper** bound
`involution_le_factorial : I n ≤ n !`. An upper bound is the wrong direction for
input (1): it cannot make a period large. Nothing in the corpus bounds `I` from
below. That is what is proved here.

## What is proved (sorry-free)

* `mul_involution_le_involution_add_two` — `(n+1)·I n ≤ I (n+2)`, straight from the
  recurrence. The whole file rests on this one step.
* `involution_ratio_unbounded` — for every `C`, eventually `C·I n ≤ I (n+2)`: the
  two-step ratio is **unbounded**, so `I` leaves every geometric class. This is the
  corpus's own reading of "super-exponential" in `prop:tower-geometric-lower-bound`
  ("successive ratios strictly increasing").
* `factorial_le_involution_two_mul` — `n ! ≤ I (2n)`, the quantitative form: the
  involution numbers grow at least factorially along the even subsequence.
* `involution_mono` — `I` is monotone, which transports the even bound to all `n`.
* `classical_period_ge` — hence the classical period `I(n)/n` is bounded below by
  `(n/2)! / n`, and `classical_period_ratio_unbounded` — its growth leaves every
  geometric class.

## A caution on what `a_D^(n)` IS (added after merging main, 2026-08-30)

[`docs/audits/2026-08-29-sw-period-residue-sum-projection-and-warrant.md`](../../../../../docs/audits/2026-08-29-sw-period-residue-sum-projection-and-warrant.md)
(bean `qou-6v5l`, found working input (2) of the same scope note) reports that
`prop:sw-period-residue-sum`'s Lean is a conclusion-typed projection, and that its stated
warrant — "the residue theorem on the compact Riemann surface" — runs backwards: on a
compact surface the residues sum to **zero**, and `H₁(P¹) = 0` supplies no generating
cycle. So the residue-sum *representation* of `a_D^(n)` is itself under question.

**This file is insulated from that, by construction.** Everything proved below is about
`involutionNumber` and about a bar-symmetric non-negative Laurent presentation — concrete
objects with no geometric input. The step from those to "the Seiberg–Witten period" is
input (2), which this file explicitly does not claim. Read the results as statements about
`I(n)/n` and `Σ_{λ⊢n} dim_q λ`; whether that quantity *is* the SW period is exactly the
open identification, and it is now open in one more way than it looked.

## What is NOT proved here (honest scope)

* **The `q`-transfer.** These are the `q = 1` statements. The step from
  `a_D^(n)(q) ≥ a_D^(n)(1)` needs the bar-symmetry of `S(n) = Σ_{λ⊢n} dim_q λ`;
  the general-`q` half is `barSymmetric_ge_at_one` below, which *is* proved, but
  applying it needs `dim_q λ` presented in bar-symmetric non-negative form — the
  `StandardYoungTableau` infrastructure Mathlib lacks (the same gap
  `KeystoneC8SuperExpBound` names for its inputs (A)/(C)).
* **`Σ_{λ⊢n} f^λ = I(n)`** (the Robinson–Schensted corollary) is not proved *here*, but it
  is **no longer open in the corpus**: `QOU.Mass.sum_numSYT_eq_involutionNumber`
  (`QOU/Mass/SumSYTEqInvolution.lean`) proves it, sorry-free, for every `n`.  This entry
  previously said it was open and blocked on a missing Mathlib `StandardYoungTableau`
  layer; **both halves of that were wrong.**  It was not blocked on RSK at all — Young's
  lattice is `1`-differential, and that route reaches the same recurrence with finite
  combinatorics on `YoungDiagram` (`QOU.Mathlib.upSum_eq`), no insertion and no
  permutation↔tableau-pair bijection.  Corrected 2026-08-30; bean `qou-jlam`.
* **Input (2)**, the na-Stokes identity `a_D^(n) = lw(n−1)` itself, and **input (3)**,
  the residue weight `w_n(K)`, are untouched.

Base ring: `ℕ` for the involution core, `ℝ` only where division/order is needed
(AGENTS.md §7c — the archimedean ordered field is the correct home for the
period statements).

## References

- [leitner2026] §5-brings-surface/sw-classical-jet-exactness
- [leitner2026] §mass-theory/jet-filtration-binding-extensive
-/

namespace QOU.Mass.SWPeriodSuperExponential

open QOU.BraidKnot.KeystoneC8SuperExpBound

/-! ## 1. The involution numbers from below -/

/-- The defining recurrence, as an equation (definitional, restated for `omega`). -/
theorem involution_succ_succ (n : ℕ) :
    involutionNumber (n + 2) = involutionNumber (n + 1) + (n + 1) * involutionNumber n :=
  rfl

/-- **The one load-bearing step.** Dropping the `I(n+1)` summand from the recurrence
leaves `(n+1)·I n ≤ I (n+2)`: the two-step growth factor is at least `n+1`, which is
*not* bounded by any constant. Everything below is this inequality iterated. -/
theorem mul_involution_le_involution_add_two (n : ℕ) :
    (n + 1) * involutionNumber n ≤ involutionNumber (n + 2) := by
  have h := involution_succ_succ n
  omega

/-- **`I` leaves every geometric class.** For any constant `C`, past `n = C` the
two-step ratio exceeds `C`. A geometric sequence has *constant* two-step ratio, so no
geometric sequence dominates `I` — this is the corpus's reading of "super-exponential"
in `prop:tower-geometric-lower-bound`. -/
theorem involution_ratio_unbounded (C : ℕ) :
    ∀ n, C ≤ n → C * involutionNumber n ≤ involutionNumber (n + 2) := by
  intro n hn
  calc C * involutionNumber n
      ≤ (n + 1) * involutionNumber n := Nat.mul_le_mul_right _ (by omega)
    _ ≤ involutionNumber (n + 2) := mul_involution_le_involution_add_two n

/-- **Quantitative form: `n ! ≤ I (2n)`.** Iterating the step along the even
subsequence multiplies by `2n+1 ≥ n+1` at each stage, so the even-indexed involution
numbers grow at least factorially. This is a genuine super-exponential *lower* bound —
the direction `involution_le_factorial` does not provide. -/
theorem factorial_le_involution_two_mul (n : ℕ) :
    n.factorial ≤ involutionNumber (2 * n) := by
  induction n with
  | zero => decide
  | succ n ih =>
    have hstep : (2 * n + 1) * involutionNumber (2 * n) ≤ involutionNumber (2 * n + 2) :=
      mul_involution_le_involution_add_two (2 * n)
    have hidx : 2 * (n + 1) = 2 * n + 2 := by ring
    calc (n + 1).factorial
        = (n + 1) * n.factorial := Nat.factorial_succ n
      _ ≤ (2 * n + 1) * involutionNumber (2 * n) :=
          Nat.mul_le_mul (by omega) ih
      _ ≤ involutionNumber (2 * n + 2) := hstep
      _ = involutionNumber (2 * (n + 1)) := by rw [hidx]

/-- `I n > 0` for every `n`: the recurrence only ever adds. -/
theorem involutionNumber_pos : ∀ n, 0 < involutionNumber n := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more m _ ih2 =>
    have h := involution_succ_succ m
    omega

/-- `I` is monotone: `I(n+2) = I(n+1) + (n+1)·I(n) ≥ I(n+1)`, since the added term is a
natural number. Transports the even-index bound to every index. -/
theorem involution_le_succ : ∀ n, involutionNumber n ≤ involutionNumber (n + 1)
  | 0 => by decide
  | (m + 1) => by
    have h : involutionNumber (m + 1 + 1)
        = involutionNumber (m + 1) + (m + 1) * involutionNumber m := rfl
    omega

theorem involution_mono : Monotone involutionNumber :=
  monotone_nat_of_le_succ involution_le_succ

/-- `n ! ≤ I m` for every `m ≥ 2n`: the even bound, transported by monotonicity. -/
theorem factorial_le_involution (n m : ℕ) (h : 2 * n ≤ m) :
    n.factorial ≤ involutionNumber m :=
  le_trans (factorial_le_involution_two_mul n) (involution_mono h)

/-! ## 2. The classical period `I(n)/n` -/

/-- The classical (`q = 1`) binding period of `prop:sw-classical-jet-exactness`:
`a_D^(n)|_{q=1} = lw(n−1) = I(n)/n`. -/
noncomputable def classicalPeriod (n : ℕ) : ℝ := (involutionNumber n : ℝ) / n

/-- The classical period is **strictly positive** for `n ≥ 1` — the derived form of the
`0 ≤ a_D^(n)` hypothesis that `QOU.Mass.JetFiltrationExtensive` carries abstractly. -/
theorem classicalPeriod_pos {n : ℕ} (hn : 0 < n) : 0 < classicalPeriod n := by
  have hI : 0 < involutionNumber n := involutionNumber_pos n
  have : (0:ℝ) < (involutionNumber n : ℝ) := by exact_mod_cast hI
  have hnR : (0:ℝ) < (n : ℝ) := by exact_mod_cast hn
  exact div_pos this hnR

/-- **The period's growth leaves every geometric class.** For every `C`, past `n = C`
the period's two-step ratio exceeds `C/2`; since a geometric sequence has constant
ratio, no geometric sequence dominates `a_D^(n)|_{q=1}`. (The `n/(n+2)` factor from the
`1/n` normalisation is bounded below by `1/2` for `n ≥ 2`, hence the `C/2`.) -/
theorem classicalPeriod_ratio_unbounded (C : ℕ) (n : ℕ) (hn : C ≤ n) (h2 : 2 ≤ n) :
    (C : ℝ) / 2 * classicalPeriod n ≤ classicalPeriod (n + 2) := by
  have hnpos : 0 < n := by omega
  have hnR : (0:ℝ) < (n : ℝ) := by exact_mod_cast hnpos
  have h2R : (2:ℝ) ≤ (n : ℝ) := by exact_mod_cast h2
  have hstep : (C : ℝ) * (involutionNumber n : ℝ) ≤ (involutionNumber (n + 2) : ℝ) := by
    exact_mod_cast involution_ratio_unbounded C n hn
  have hIn : (0:ℝ) ≤ (involutionNumber n : ℝ) := Nat.cast_nonneg _
  have hI2 : (0:ℝ) ≤ (involutionNumber (n + 2) : ℝ) := Nat.cast_nonneg _
  have hCn : (0:ℝ) ≤ (C : ℝ) := Nat.cast_nonneg _
  unfold classicalPeriod
  have hcast : ((n + 2 : ℕ) : ℝ) = (n : ℝ) + 2 := by push_cast; ring
  rw [hcast]
  have lhs_eq : (C : ℝ) / 2 * ((involutionNumber n : ℝ) / (n : ℝ))
      = ((C : ℝ) * (involutionNumber n : ℝ)) / (2 * (n : ℝ)) := by
    field_simp
  rw [lhs_eq, div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith [hstep, hIn, hI2, hCn, hnR, h2R]

/-! ## 3. The `q`-transfer half that *is* provable: bar-symmetric minimisation -/

/-- For `x > 0`, `2 ≤ x + x⁻¹` — the AM–GM step, `x + x⁻¹ − 2 = (x−1)²/x ≥ 0`. -/
theorem two_le_add_inv {x : ℝ} (hx : 0 < x) : 2 ≤ x + x⁻¹ := by
  have hxne : x ≠ 0 := ne_of_gt hx
  have hmul : x * x⁻¹ = 1 := mul_inv_cancel₀ hxne
  have hinv : 0 < x⁻¹ := inv_pos.mpr hx
  nlinarith [sq_nonneg (x - 1), hmul, hx, hinv, sq_nonneg (x - x⁻¹)]

/-- **A bar-symmetric Laurent polynomial with non-negative coefficients is minimised at
`q = 1`.** Writing `P(q) = c₀ + Σ_k c_k (q^k + q^{−k})` with every `c_k ≥ 0`, each
paired term obeys `q^k + q^{−k} ≥ 2` (`two_le_add_inv` at `x = q^k`), so
`P(q) ≥ c₀ + 2 Σ_k c_k = P(1)`.

This is the general-`q` half of the transfer `a_D^(n)(q) ≥ a_D^(n)(1)`: the na-Stokes
period `S(n) = Σ_{λ⊢n} dim_q λ` is bar-invariant, so *if* its coefficients are
non-negative the classical bound above is a bound for every `q > 0`. Verified
numerically on the corpus's own closed forms — `lw(2) = (q+1)²/(3q)` and
`lw(3) = 5/2 + (3/4)(q−q⁻¹)²` both attain their minimum `I(c+1)/(c+1)` exactly at
`q = 1`. The missing piece is the presentation of `dim_q λ` in this form, which needs
the SYT infrastructure Mathlib does not have. -/
theorem barSymmetric_ge_at_one {m : ℕ} (c : Fin m → ℝ) (c₀ : ℝ) {q : ℝ} (hq : 0 < q)
    (hc : ∀ i, 0 ≤ c i) :
    c₀ + 2 * ∑ i, c i ≤ c₀ + ∑ i, c i * (q ^ (i : ℕ) + (q ^ (i : ℕ))⁻¹) := by
  have hterm : ∀ i : Fin m, c i * 2 ≤ c i * (q ^ (i : ℕ) + (q ^ (i : ℕ))⁻¹) := by
    intro i
    exact mul_le_mul_of_nonneg_left (two_le_add_inv (by positivity)) (hc i)
  have : 2 * ∑ i, c i = ∑ i : Fin m, c i * 2 := by
    rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun i _ => by ring
  rw [this]
  exact add_le_add_left (Finset.sum_le_sum fun i _ => hterm i) c₀

/-- **The `q`-transfer, conditional on the presentation.** Suppose the na-Stokes period
`S(n)(q) = Σ_{λ⊢n} dim_q λ` is presented as a bar-symmetric Laurent polynomial with
non-negative coefficients, `S = c₀ + Σ_k c_k (q^k + q^{−k})`, whose value at `q = 1`
is the involution number `I n` (that value is `c₀ + 2 Σ_k c_k`). Then for **every**
`q > 0`, `I n ≤ S`.

Combined with `factorial_le_involution_two_mul` this transports the whole
super-exponential lower bound off `q = 1` and onto the physical pin: the period at any
`q > 0` is at least the classical one, which is at least `(n/2)!`.

The presentation hypothesis is **verified exactly at `n = 2..9`** by
`computations/sw_period_bar_positivity_probe.py` (balanced `[k]_q`, q-hook dimension,
sympy exact — `S(n)` is a Laurent polynomial, bar-symmetric, with non-negative
coefficients, and `S(n)(1) = I(n)` at every `n`). It is **not proved for general `n`**;
the general statement is the q-hook-length formula
`[n]_q!/∏[h]_q = Σ_{T ∈ SYT(λ)} q^{maj T}`, which needs the same missing
`StandardYoungTableau` layer as beans `qou-m3xr` / `qou-jlam`.

Note the transfer carries **no regime condition on `q`**: non-negativity of the
coefficients is what does the work. In particular it does not require `q < φ`, and the
probe confirms the bound at `q = φ`, `q = 2` and `q = 5`. (`q − q⁻¹ = 1` exactly at
`q = φ` — a real feature of the balanced `q`-integer, but not a gate on this claim.) -/
theorem involution_le_of_barSymmetric_presentation
    {n m : ℕ} {c : Fin m → ℝ} {c₀ S q : ℝ}
    (hq : 0 < q) (hc : ∀ i, 0 ≤ c i)
    (hpres : S = c₀ + ∑ i, c i * (q ^ (i : ℕ) + (q ^ (i : ℕ))⁻¹))
    (hat_one : c₀ + 2 * ∑ i, c i = (involutionNumber n : ℝ)) :
    (involutionNumber n : ℝ) ≤ S := by
  rw [hpres, ← hat_one]
  exact barSymmetric_ge_at_one c c₀ hq hc

/-- **The physical period dominates the classical one.** Same hypotheses, divided by `n`:
`a_D^(n)(q) = S/n ≥ I(n)/n = classicalPeriod n` for every `q > 0`. -/
theorem classicalPeriod_le_of_barSymmetric_presentation
    {n m : ℕ} {c : Fin m → ℝ} {c₀ S q : ℝ} (hn : 0 < n)
    (hq : 0 < q) (hc : ∀ i, 0 ≤ c i)
    (hpres : S = c₀ + ∑ i, c i * (q ^ (i : ℕ) + (q ^ (i : ℕ))⁻¹))
    (hat_one : c₀ + 2 * ∑ i, c i = (involutionNumber n : ℝ)) :
    classicalPeriod n ≤ S / (n : ℝ) := by
  have hnR : (0:ℝ) < (n : ℝ) := by exact_mod_cast hn
  have hle := involution_le_of_barSymmetric_presentation (n := n) hq hc hpres hat_one
  unfold classicalPeriod
  gcongr

/-- **The transferred super-exponential bound.** For every `q > 0` satisfying the
presentation hypothesis, the period `S` is bounded below by `(k)!` whenever `2k ≤ n` —
factorial growth, off `q = 1`. -/
theorem factorial_le_of_barSymmetric_presentation
    {n m k : ℕ} {c : Fin m → ℝ} {c₀ S q : ℝ}
    (hq : 0 < q) (hc : ∀ i, 0 ≤ c i)
    (hpres : S = c₀ + ∑ i, c i * (q ^ (i : ℕ) + (q ^ (i : ℕ))⁻¹))
    (hat_one : c₀ + 2 * ∑ i, c i = (involutionNumber n : ℝ))
    (hk : 2 * k ≤ n) :
    (k.factorial : ℝ) ≤ S := by
  have h1 : (k.factorial : ℝ) ≤ (involutionNumber n : ℝ) := by
    exact_mod_cast factorial_le_involution k n hk
  exact h1.trans (involution_le_of_barSymmetric_presentation hq hc hpres hat_one)

end QOU.Mass.SWPeriodSuperExponential
