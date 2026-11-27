/-
# No linear functional of the crossing counts can be a Coulomb term

Owner question, 2026-08-30: *"add an explicit EM term at level 3"*, with the
falsifiable target being the Coulomb displacement energy's `A`-scaling
(`qou-vudb`).

The EM term is **already there**, and this file says why no choice of its
coefficient can do the job.

## The setting

`qou-toul` (2026-08-29) derived the crossing-energy split from
`def:crossing-energy`'s own weights, `E = n₊ q - n₋ q⁻¹`, by solving
`E = A (q + q⁻¹) + B (q - q⁻¹)`:

* `A` — symmetric, **strong** — is the writhe `(n₊ - n₋)/2`;
* `B` — antisymmetric, **Coulomb** — is the crossing count `(n₊ + n₋)/2`.

Measured on the canonical atomic braids
(`computations/probes/level3_em_channel_parity_probe.py`, 12 nuclei to `A = 39`,
matching `mba-sidecar-mirror-cancellation`):

    n₊ = 5A - 1 + 2Z        n₋ = 5A - 1 - 2Z

so the **Coulomb** channel is `5A - 1` — depending on `A` alone, hence identical
across a mirror pair — and the **strong** channel is `2Z`, carrying all of the
charge dependence. That is the reverse of physics, and it is why `qou-vudb`
measured the model's mirror asymmetry as a *strong*-channel constant.

## What is proved here

Both `n₊` and `n₋` are **affine** in `(A, Z)`, so every `a·n₊ + b·n₋ + c` is
affine in `Z` at fixed `A`. The Coulomb energy of a nucleus is carried by the
number of **proton pairs**, `Z(Z-1)`, which is quadratic.

`secondDiff` is the discrete second difference in `Z`. It annihilates every
affine function (`secondDiff_affine_eq_zero`, hence
`secondDiff_crossing_combination_eq_zero` for any coefficients at all) and
returns the constant `2` on `Z(Z-1)` (`secondDiff_protonPairs`). Since `2 ≠ 0`
in `ℤ`, the two can never agree — `no_crossing_combination_is_protonPairs`.

The exclusion is therefore over **all** coefficients simultaneously, not one
fit at a time: it is a statement about **degree**, not about magnitudes.

## Scope

Scope **(b)** with the invariant named: degree. It does **not** say the
framework cannot have a Coulomb term — it says such a term cannot be a linear
functional of these crossing counts, so it has to come from somewhere the
crossing counts do not reach. Nothing here refutes `qou-toul`'s correction; this
builds on it.

Base ring is a generic `CommRing` for the two second-difference lemmas (AGENTS.md
§7c); only the final non-existence step descends to `ℤ`, where it needs
`(2 : ℤ) ≠ 0`.

Beans `qou-vudb`, `qou-toul`, `qou-1pig`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.MassTheory.CrossingCountAffine

variable {R : Type*} [CommRing R]

/-! ## 1. The measured crossing counts -/

/-- `n₊ = 5A - 1 + 2Z`, the positive-crossing count of the canonical atomic
braid, as measured. -/
def nPlus (A Z : R) : R := 5 * A - 1 + 2 * Z

/-- `n₋ = 5A - 1 - 2Z`, the negative-crossing count. -/
def nMinus (A Z : R) : R := 5 * A - 1 - 2 * Z

/-- The **Coulomb** (antisymmetric) channel multiplicity, `(n₊ + n₋)/2`, stated
without the division as the identity `n₊ + n₋ = 2(5A - 1)`. It depends on `A`
alone — this is the mirror-blindness. -/
theorem coulomb_channel_charge_free (A Z : R) :
    nPlus A Z + nMinus A Z = 2 * (5 * A - 1) := by
  unfold nPlus nMinus; ring

/-- The **strong** (symmetric) channel multiplicity, `(n₊ - n₋)/2 = 2Z`, stated
as `n₊ - n₋ = 4Z`. All of the charge dependence sits here. -/
theorem strong_channel_carries_charge (A Z : R) :
    nPlus A Z - nMinus A Z = 4 * Z := by
  unfold nPlus nMinus; ring

/-! ## 2. The discrete second difference in `Z` -/

/-- The second difference of `f` at `Z`. It annihilates affine functions and
detects a quadratic's leading coefficient. -/
def secondDiff (f : R → R) (Z : R) : R := f (Z + 2) - 2 * f (Z + 1) + f Z

/-- **The second difference kills every affine function.** -/
theorem secondDiff_affine_eq_zero (u v : R) :
    ∀ Z : R, secondDiff (fun Z => u * Z + v) Z = 0 := by
  intro Z; unfold secondDiff; ring

/-- **Every linear functional of the crossing counts is annihilated.** For any
coefficients `a b c` whatsoever, and at any fixed `A`. -/
theorem secondDiff_crossing_combination_eq_zero (a b c A : R) :
    ∀ Z : R, secondDiff (fun Z => a * nPlus A Z + b * nMinus A Z + c) Z = 0 := by
  intro Z; unfold secondDiff nPlus nMinus; ring

/-- The number of proton pairs, `Z(Z-1)` — what a Coulomb term must count. -/
def protonPairs (Z : R) : R := Z * (Z - 1)

/-- **The second difference of `Z(Z-1)` is the constant `2`.** -/
theorem secondDiff_protonPairs : ∀ Z : R, secondDiff protonPairs Z = 2 := by
  intro Z; unfold secondDiff protonPairs; ring

/-! ## 3. The exclusion -/

/-- **No linear functional of the crossing counts is the proton-pair count.**
Over `ℤ`, where `2 ≠ 0`. The quantifier order is the point: the coefficients
`a, b, c` are chosen *first* and the contradiction follows for every choice, so
this excludes the whole family at once rather than one fit at a time. -/
theorem no_crossing_combination_is_protonPairs (a b c A : ℤ) :
    ¬ (∀ Z : ℤ, a * nPlus A Z + b * nMinus A Z + c = protonPairs Z) := by
  intro hEq
  have h0 : secondDiff (fun Z => a * nPlus A Z + b * nMinus A Z + c) 0 = 0 :=
    secondDiff_crossing_combination_eq_zero a b c A 0
  have h2 : secondDiff protonPairs (0 : ℤ) = 2 := secondDiff_protonPairs 0
  rw [show (fun Z : ℤ => a * nPlus A Z + b * nMinus A Z + c) = protonPairs from
    funext hEq] at h0
  rw [h2] at h0
  exact absurd h0 (by decide)

/-- **The mirror form.** The Coulomb channel takes the same value on `(Z, N)` and
on `(N, Z)`, so whatever coefficient multiplies it contributes **zero** to every
mirror splitting. Stated at fixed `A`, which is what a mirror pair shares. -/
theorem coulomb_channel_mirror_invariant (A Z W : R) :
    nPlus A Z + nMinus A Z = nPlus A W + nMinus A W := by
  rw [coulomb_channel_charge_free, coulomb_channel_charge_free]

/-- And the strong channel is **not** mirror-invariant: its values differ by
`4(Z - W)`. So the charge dependence the mirror splitting needs is present in
the model — in the wrong channel. -/
theorem strong_channel_mirror_difference (A Z W : R) :
    (nPlus A Z - nMinus A Z) - (nPlus A W - nMinus A W) = 4 * (Z - W) := by
  rw [strong_channel_carries_charge, strong_channel_carries_charge]; ring


/-! ## 4. Linearity of `secondDiff` and quadratic reconstruction of `protonPairs` (`qou-dhsn`) -/

/-- **Linearity of the discrete second difference (`qou-dhsn`).** -/
theorem secondDiff_linear_comb (f g : R → R) (α β Z : R) :
    secondDiff (fun x => α * f x + β * g x) Z = α * secondDiff f Z + β * secondDiff g Z := by
  unfold secondDiff
  ring

/-- **Quadratic crossing-difference reconstruction of `protonPairs` (`qou-dhsn`).**
While no *linear* combination of `(nPlus, nMinus)` can equal `protonPairs Z`, the
quadratic polynomial `(nPlus A Z - nMinus A Z) * (nPlus A Z - nMinus A Z - 4)` in the
strong-channel crossing difference equals `16 * protonPairs Z` identically. -/
theorem crossing_diff_quadratic_eq_sixteen_protonPairs (A Z : R) :
    (nPlus A Z - nMinus A Z) * (nPlus A Z - nMinus A Z - 4) = 16 * protonPairs Z := by
  unfold nPlus nMinus protonPairs
  ring

end QOU.MassTheory.CrossingCountAffine
