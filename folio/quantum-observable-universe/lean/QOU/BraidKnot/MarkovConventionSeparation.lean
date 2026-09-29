/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Conventions C and D are separated by the range of the Markov kernel

Bean `qou-cxjq` step 3. Before migrating any convention-C definition, this file
settles the structural question that governs how the migration must be done.

## The two conventions share one rational kernel

Write `g u = u / (u ^ 2 + 1)`. Then, exactly,

* **convention C**  `z_C q = √q / (q + 1) = g (√q)`,
* **convention D**  `z_D q = q ^ 3 / (q ^ 2 + 1) = q ^ 2 * g q`.

So D is *not* C with a different letter in it: C is `g` **evaluated** at a square
root, D is `g` evaluated at `q` and then **rescaled** by `q ^ 2`.

## The separation

`g` is bounded: `g u ≤ 1 / 2` for every real `u`, with equality exactly at
`u = 1` (immediately from `0 ≤ (u - 1) ^ 2`). Meanwhile
`z_D q - 1 / 2 = (q - 1) * (2 * q ^ 2 + q + 1) / (2 * (q ^ 2 + 1))`, whose
second factor is positive for every real `q`, so

    1 < q  →  1 / 2 < z_D q .

Hence for every `q > 1` there is **no** real `u` at all with `g u = z_D q`
(`no_kernel_instantiation_is_conventionD`). At `q = 1` the two coincide, both
equal to `1 / 2` — the classical coincidence, and the *only* point of contact.

## Why this is the gate on the migration, not a remark

Three consequences, in increasing order of how much work they save:

1. **"Never substitute `s ^ 2 = q`" is now a theorem, not a caution.** The
   substitution cannot work, because it asks for a `u` that provably does not
   exist above `q = 1`. The substrate sits at `q₀ ≈ 1.11 > 1`.

2. **The Tier-2 migration baked convention C in structurally.** Replacing
   `Real.sqrt q` by a generic `markovZ (u : R) := u / (u ^ 2 + 1)` was carried
   out to remove the square root, and it did. But the *shape* it migrated to has
   a real range of `[-1/2, 1/2]`, which excludes `z_D q` for every `q > 1`. So
   the generic form is not convention-neutral: no choice of `u` makes it D.
   It removed the square root and made the convention harder to see, which is
   the opposite of what a convention migration should do.

3. **Therefore the 9 `C-sqrtvar` sites cannot be repaired by re-instantiating.**
   The definition *shape* has to change — from `g` to `q ^ 2 * g q`. A site that
   merely re-parameterises stays in C no matter what is passed to it.

Everything here is archimedean (an ordering and a `Real.sqrt`), so it lives on
the ℝ side of the AGENTS.md §7c wall by necessity, not by accident: the
separation *is* an inequality, and there is nothing to state over a generic
commutative ring.
-/

namespace QOU.BraidKnot

/-- The rational kernel both conventions are built from: `g u = u / (u² + 1)`.
This is the generic Tier-2 `markovZ`, stated here over `ℝ` because the whole
point of this file is an inequality.

**This is a convention-C object, deliberately, and it is here for comparison
only** — it is the thing convention D is separated *from*, and every theorem
below is about the gap between it and `markovZD`. Do not consume it as a Markov
parameter; `markovZD` is canonical (owner ruling R1, 2026-08-15).

Recorded because `scripts/lean-markov-convention-audit.py` flagged this very
declaration as actionable C on the run right after it was written — correct by
its rules, and the right fix is for the site to announce itself rather than for
the detector to special-case a filename. -/
noncomputable def markovKernel (u : ℝ) : ℝ := u / (u ^ 2 + 1)

/-- Convention **D**, the canonical one (owner ruling R1, 2026-08-15). -/
noncomputable def markovZD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- Convention **C**, excised. Kept here only as the object being separated. -/
noncomputable def markovZC (q : ℝ) : ℝ := Real.sqrt q / (q + 1)

/-- The denominator never vanishes. -/
theorem sq_add_one_pos (u : ℝ) : 0 < u ^ 2 + 1 := by positivity

/-- **The kernel is bounded above by `1/2`.** Immediate from `0 ≤ (u - 1)²`. -/
theorem markovKernel_le_half (u : ℝ) : markovKernel u ≤ 1 / 2 := by
  rw [markovKernel, div_le_iff₀ (sq_add_one_pos u)]
  nlinarith [sq_nonneg (u - 1)]

/-- The kernel is bounded below by `-1/2`, so its real range is `[-1/2, 1/2]`. -/
theorem neg_half_le_markovKernel (u : ℝ) : -(1 / 2) ≤ markovKernel u := by
  rw [markovKernel, le_div_iff₀ (sq_add_one_pos u)]
  nlinarith [sq_nonneg (u + 1)]

/-- **Convention D exceeds `1/2` for every `q > 1`.**
`z_D q - 1/2` has numerator `(q - 1) * (2q² + q + 1)`, and the second factor is
positive for every real `q`. -/
theorem half_lt_markovZD {q : ℝ} (hq : 1 < q) : 1 / 2 < markovZD q := by
  rw [markovZD, lt_div_iff₀ (sq_add_one_pos q)]
  nlinarith [sq_nonneg q, sq_nonneg (q - 1), sq_nonneg (q + 1)]

/-- **The separation.** For `q > 1` no real `u` whatsoever sends the kernel to
convention D — so D is outside the kernel's range, not merely at a different
point of it. -/
theorem no_kernel_instantiation_is_conventionD {q : ℝ} (hq : 1 < q) :
    ¬ ∃ u : ℝ, markovKernel u = markovZD q := by
  rintro ⟨u, hu⟩
  have h1 : markovKernel u ≤ 1 / 2 := markovKernel_le_half u
  have h2 : 1 / 2 < markovZD q := half_lt_markovZD hq
  rw [hu] at h1
  exact absurd h1 (not_le.mpr h2)

/-- The two conventions agree at `q = 1`, both equal to `1/2`: the classical
coincidence, and by the theorem above the only point of contact. -/
theorem markovZD_one : markovZD 1 = 1 / 2 := by norm_num [markovZD]

theorem markovZC_one : markovZC 1 = 1 / 2 := by
  norm_num [markovZC]

/-- Convention C **is** the kernel evaluated at `√q` — the exact statement of
what the Tier-2 generic form is, for `0 ≤ q`. -/
theorem markovZC_eq_kernel_sqrt {q : ℝ} (hq : 0 ≤ q) :
    markovZC q = markovKernel (Real.sqrt q) := by
  rw [markovZC, markovKernel, Real.sq_sqrt hq]

/-- Convention D is the kernel at `q`, **rescaled by `q²`** — a different
construction, not a different argument. -/
theorem markovZD_eq_sq_mul_kernel (q : ℝ) :
    markovZD q = q ^ 2 * markovKernel q := by
  rw [markovZD, markovKernel]
  field_simp

/-- **Corollary for the migration.** At any substrate point above `q = 1` the
two conventions are unequal, so a file that defines its Markov parameter through
the kernel is convention C and stays convention C however it is instantiated. -/
theorem markovZC_ne_markovZD {q : ℝ} (hq : 1 < q) (hq0 : 0 ≤ q) :
    markovZC q ≠ markovZD q := by
  intro h
  exact no_kernel_instantiation_is_conventionD hq
    ⟨Real.sqrt q, by rw [← markovZC_eq_kernel_sqrt hq0, h]⟩

end QOU.BraidKnot
