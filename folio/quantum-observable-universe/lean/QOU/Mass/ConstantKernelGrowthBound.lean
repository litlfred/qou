/-
# A constant-kernel recurrence grows at most exponentially

Two statements in the corpus cannot both hold, and this file makes the
incompatibility machine-checked rather than argued.

* `prop:prolonged-periods-fixed-depth` asserts that the prolongation periods
  satisfy `a (n + d) = Σ_{j < d} c j * a (n + j)` with an **`n`-independent**
  kernel `c`, for every `n`, with `d ≤ rank V ≤ 2g = 8` on the genus-4 Bring
  curve — obtained by Cayley–Hamilton on the jet-prolongation operator.

* `QOU.Mass.SWPeriodSuperExponential` (PR #6052) proves `a_D^(n)|_{q=1} =
  lw (n-1) = I n / n` grows at least factorially: `factorial_le_involution_two_mul`
  gives `n ! ≤ I (2n)`.

**Cite that lemma, not the ratio one.** It is tempting to reach for
`involution_ratio_unbounded` ("`I` leaves every geometric class") instead, and it
does **not** carry the contradiction: a geometric *upper* bound does not forbid
unbounded two-step ratios, since a sequence may dip far below `K ^ n` at some `n`
and jump back, making `a (n+2) / a n` arbitrarily large while never exceeding
`M * K ^ n`. `SuperExponential` below is the negation of the geometric bound
itself, which is the property that actually conflicts. (This correction is
#6088's, made against its own earlier claim; an earlier revision of this header
repeated the same slip and cited the ratio lemmas here.)

A linear recurrence with constant coefficients admits only solutions
`Σ p_i n * λ_i ^ n`, which are at most exponential. This file proves the
elementary form of that bound directly — `|a n| ≤ M * K ^ n` — and derives the
contradiction.

**The tell is in their own load-bearing step.** `involution_succ_succ` reads
`I (n + 2) = I (n + 1) + (n + 1) * I n`: a depth-2 recurrence whose coefficient
`(n + 1)` is `n`-**dependent**, which is exactly what the fixed-depth
proposition forbids. The `n`-dependence is in plain view, in the coefficient.

**What this file does NOT do.** It does not decide *which* side gives. Three
candidates, and the corpus does not settle between them here:

  (a) the identification `a_D^(n) = I n / n` (`prop:sw-classical-jet-exactness`);
  (b) `a_D^(n) = φ (M ^ n v₀)` for a fixed finite-rank `M`
      (`prop:mi-sw-abelianisation`) — super-exponential growth cannot be the
      orbit of a fixed finite-rank operator, whatever `V`'s rank;
  (c) the word "`n`-independent" in the fixed-depth proposition.

By the super-exponential side's **own** scope note, (a) is the cheapest suspect:
its docstring records that `Σ_{λ ⊢ n} f^λ = I n` (RSK) is open in this corpus
(beans `qou-m3xr`, `qou-jlam`, both blocked on the missing Mathlib
`StandardYoungTableau` layer). That is their scoping, not a preference of mine.

This is the second independent crack in the fixed-depth picture. The first,
`QOU.MassTheory.BodyOrderRecurrenceDepth.no_equivariant_prolongation` (merged),
reaches it from equivariance (Schur on `H¹(Bring)`) rather than from growth.

## Overlap with `QOU.MassTheory.FixedDepthGrowthBound` (#6088) — read this first

That file landed on its branch before this one and proves the same geometric
bound (`abs_le_geometric`) plus the factorial case (`not_factorial_growth`).
**It has priority; this file is the generalisation, not a re-derivation.** The
increment here is that the growth hypothesis is `SuperExponential` — *exceeds
every geometric sequence* — rather than factorial specifically, so the
contradiction covers growth classes between exponential and factorial, where no
`n !` bound is available. **The bridge between the two is NOT formalised here.** Factorial growth on the
even indices does imply `SuperExponential`, since `K ^ n / n !` tends to zero for
every `K` — but that argument belongs in #6088's file, next to the factorial
lemma it discharges, and is stated here only so the relationship is on the
record. It is deliberately not a `sorry` in this file: nothing below needs it,
because the theorems are stated for the general predicate directly. If the
maintainers of #6088 prefer a single home, this file should be folded into
theirs and deleted.

Ground ring `ℝ`: the claim is about magnitudes and unboundedness, so it is
archimedean by nature and `ℝ` is the correct specialisation under AGENTS.md §7c.

Beans `qou-9nt7` (this unit), `qou-9yqb` (the finding).
-/
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic

namespace QOU.Mass.ConstantKernelGrowthBound

open Finset

variable {d : ℕ} {c : Fin d → ℝ} {a : ℕ → ℝ}

/-- `a` satisfies a depth-`d` linear recurrence with the **constant** (that is,
`n`-independent) kernel `c`. This is the hypothesis
`prop:prolonged-periods-fixed-depth` asserts of the prolongation periods. -/
def IsConstKernelRec (d : ℕ) (c : Fin d → ℝ) (a : ℕ → ℝ) : Prop :=
  ∀ n : ℕ, a (n + d) = ∑ j : Fin d, c j * a (n + (j : ℕ))

/-- `a` grows **super-exponentially**: it eventually exceeds every geometric
sequence. This is the shape of `classical_period_ratio_unbounded`. -/
def SuperExponential (a : ℕ → ℝ) : Prop :=
  ∀ M K : ℝ, ∃ n : ℕ, M * K ^ n < |a n|

/-- The kernel's `ℓ¹` norm, and the base of the geometric bound. Taking the max
with `1` is what makes the bound monotone in the exponent. -/
noncomputable def kernelBound (c : Fin d → ℝ) : ℝ := max 1 (∑ j : Fin d, |c j|)

lemma one_le_kernelBound (c : Fin d → ℝ) : 1 ≤ kernelBound c := le_max_left _ _

lemma sum_abs_le_kernelBound (c : Fin d → ℝ) :
    (∑ j : Fin d, |c j|) ≤ kernelBound c := le_max_right _ _

lemma kernelBound_nonneg (c : Fin d → ℝ) : 0 ≤ kernelBound c :=
  le_trans zero_le_one (one_le_kernelBound c)

/-- **The bound.** Every solution of a depth-`d` constant-kernel recurrence is
dominated by a geometric sequence whose base is the kernel's `ℓ¹` norm (or `1`,
whichever is larger) and whose constant depends only on the `d` initial values.

This is the elementary form of "constant-coefficient recurrences have solutions
`Σ p_i n * λ_i ^ n`" — stated as a bound so that it can be contradicted by a
growth hypothesis without needing the characteristic-root decomposition. -/
theorem exists_exponential_bound (hd : 0 < d) (h : IsConstKernelRec d c a) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ n : ℕ, |a n| ≤ M * kernelBound c ^ n := by
  classical
  set K := kernelBound c with hK
  have hK1 : (1 : ℝ) ≤ K := one_le_kernelBound c
  have hK0 : (0 : ℝ) < K := lt_of_lt_of_le zero_lt_one hK1
  -- `M` dominates every one of the `d` initial values, divided by its own power.
  set M := (range d).sup' (nonempty_range_iff.2 hd.ne') (fun i => |a i|) with hM
  have hM0 : 0 ≤ M := by
    have : |a 0| ≤ M := le_sup' (f := fun i => |a i|) (by simp [hd])
    exact le_trans (abs_nonneg _) this
  refine ⟨M, hM0, ?_⟩
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    by_cases hn : n < d
    · -- initial segment: `M` dominates directly, and `K ^ n ≥ 1`.
      have h1 : |a n| ≤ M := le_sup' (f := fun i => |a i|) (mem_range.2 hn)
      have h2 : (1 : ℝ) ≤ K ^ n := one_le_pow₀ hK1
      calc |a n| ≤ M := h1
        _ = M * 1 := (mul_one M).symm
        _ ≤ M * K ^ n := by exact mul_le_mul_of_nonneg_left h2 hM0
    · -- recurrence range: write `n = m + d` and bound the sum termwise.
      push_neg at hn
      obtain ⟨m, rfl⟩ : ∃ m, n = m + d := ⟨n - d, by omega⟩
      have hterm : ∀ j : Fin d, |c j * a (m + (j : ℕ))| ≤ |c j| * (M * K ^ (m + d - 1)) := by
        intro j
        have hj : (j : ℕ) < d := j.isLt
        have hlt : m + (j : ℕ) < m + d := by omega
        have hIH : |a (m + (j : ℕ))| ≤ M * K ^ (m + (j : ℕ)) := ih _ hlt
        have hpow : K ^ (m + (j : ℕ)) ≤ K ^ (m + d - 1) :=
          pow_le_pow_right₀ hK1 (by omega)
        have : |a (m + (j : ℕ))| ≤ M * K ^ (m + d - 1) :=
          le_trans hIH (mul_le_mul_of_nonneg_left hpow hM0)
        rw [abs_mul]
        exact mul_le_mul_of_nonneg_left this (abs_nonneg _)
      have hsum : |a (m + d)| ≤ (∑ j : Fin d, |c j|) * (M * K ^ (m + d - 1)) := by
        rw [h m]
        calc |∑ j : Fin d, c j * a (m + (j : ℕ))|
            ≤ ∑ j : Fin d, |c j * a (m + (j : ℕ))| := Finset.abs_sum_le_sum_abs _ _
          _ ≤ ∑ j : Fin d, |c j| * (M * K ^ (m + d - 1)) :=
              Finset.sum_le_sum (fun j _ => hterm j)
          _ = (∑ j : Fin d, |c j|) * (M * K ^ (m + d - 1)) := by rw [← Finset.sum_mul]
      have hMK : 0 ≤ M * K ^ (m + d - 1) := mul_nonneg hM0 (pow_nonneg hK0.le _)
      have hstep : (∑ j : Fin d, |c j|) * (M * K ^ (m + d - 1)) ≤ K * (M * K ^ (m + d - 1)) :=
        mul_le_mul_of_nonneg_right (sum_abs_le_kernelBound c) hMK
      have hcollapse : K * (M * K ^ (m + d - 1)) = M * K ^ (m + d) := by
        have he : K ^ (m + d) = K ^ (m + d - 1) * K := by
          rw [← pow_succ]
          congr 1
          omega
        rw [he]; ring
      calc |a (m + d)| ≤ (∑ j : Fin d, |c j|) * (M * K ^ (m + d - 1)) := hsum
        _ ≤ K * (M * K ^ (m + d - 1)) := hstep
        _ = M * K ^ (m + d) := hcollapse

/-- **The contradiction.** No super-exponentially growing sequence satisfies a
depth-`d` recurrence with a constant kernel, for any depth and any kernel.

Applied to the corpus: `prop:prolonged-periods-fixed-depth` (constant kernel,
`d ≤ 8`) and `classical_period_ratio_unbounded` (super-exponential) cannot both
hold of `a_D^(n)`. Which one gives is not decided here — see the file header. -/
theorem not_isConstKernelRec_of_superExponential (hd : 0 < d)
    (hs : SuperExponential a) : ¬ IsConstKernelRec d c a := by
  intro h
  obtain ⟨M, _, hbound⟩ := exists_exponential_bound hd h
  obtain ⟨n, hn⟩ := hs M (kernelBound c)
  exact absurd (hbound n) (not_le.2 hn)

/-- Contrapositive in the direction a reader holding the fixed-depth proposition
will want it: if the periods really do satisfy a constant-kernel recurrence,
they are **not** super-exponential — so the identification with `I n / n` fails,
or the abelianisation does. -/
theorem not_superExponential_of_isConstKernelRec (hd : 0 < d)
    (h : IsConstKernelRec d c a) : ¬ SuperExponential a :=
  fun hs => not_isConstKernelRec_of_superExponential hd hs h

end QOU.Mass.ConstantKernelGrowthBound
