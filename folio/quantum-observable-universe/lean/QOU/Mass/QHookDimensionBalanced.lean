/-
  QOU.Mass — F1 q-lift: the Gaussian ↔ balanced `[n]_q` reconciliation.

  The sibling brick `QHookDimension.lean` builds the *polynomial (Gaussian)*
  q-combinatorics `qIntPoly q n = Σ_{i<n} q^i`, `qFactPoly`, and the q-hook
  dimension `dimQ q n hooks = qFactPoly / ∏ qIntPoly(hooks)`, all with clean
  `q = 1` collapses. Its docstring records — in prose only — that corpus canon
  (`binding-period-involution-statistic.md`) uses the *balanced* quantum integer
  `[k]_bal = (q^k − q^{−k})/(q − q^{−1})`, which agrees with the polynomial form
  up to an overall `q`-monomial twist. This file turns that prose claim into a
  PROVEN lemma.

  ## What is proved

  * `qIntBal q n = (q^n − (q⁻¹)^n)/(q − q⁻¹)` — the balanced quantum integer,
    over a generic `Field` (algebraic inverse — §7c, NOT archimedean; no `ℝ`).
  * `sub_inv_mul_qIntBal` — the clean defining identity
    `(q − q⁻¹) · [n]_bal = q^n − q^{−n}` (needs `q ≠ 0`, `q^2 ≠ 1`).
  * `qIntBal_eq_twist` — the exact monomial twist relation
    `[n]_bal = q^{−(n−1)} · qIntPoly(q^2) n` (written `(q⁻¹)^(n−1) · …`).
    Verified against small `n`: `n=1 ↦ 1`, `n=2 ↦ q + q⁻¹`, in both forms.
  * `qFactPoly_bal_eq_twist` — the factorial-level twist
    `[n]_bal! = (q⁻¹)^{Σ_{i<n} i} · qFactPoly(q^2) n`.
  * `dimQ_bal` and `dimQ_bal_eq_dimQ_of_twist_cancel` — the q-hook dimension in
    the balanced normalization, and the exact condition under which its overall
    twist cancels so that `dimQ_bal q n hooks = dimQ (q^2) n hooks`.

  ## The `0/0`-at-`q = 1` subtlety (why `q^2 ≠ 1`)

  At literal `q = 1` the balanced form is the `0/0` indeterminate (`q − q⁻¹ = 0`;
  Lean's junk division makes it `0`, not `k`), so the balanced identities carry
  the hypothesis `q^2 ≠ 1` (equivalently `q − q⁻¹ ≠ 0` when `q ≠ 0`). The clean
  `q = 1` LIMIT lives on the polynomial side (`qIntPoly 1 k = k`), already proved
  in the sibling; nothing here touches those `q = 1` theorems.

  ## Ratio cancellation — the exact condition (honest scope)

  The balanced hook dimension is NOT unconditionally equal to the `q^2`-Gaussian
  one. Twisting the numerator factorial `(n` cells) and the hook denominator
  (`hooks.card` cells) leaves a residual monomial
  `dimQ_bal q n hooks = q^{E} · dimQ (q^2) n hooks`,
  `E = (Σ_{i<n} i) − (Σ_{h ∈ hooks} (h−1))`
  (numerator twist exponent minus denominator twist exponent). The twist CANCELS
  — i.e. `dimQ_bal = dimQ(q^2)` — exactly when `E = 0`, i.e. when
  `Σ_{h ∈ hooks} (h−1) = Σ_{i<n} i`. For a genuine partition `λ ⊢ n` with
  `hooks.card = n` this is `Σ h = n(n+1)/2`, which holds for hook / single-row /
  single-column shapes but NOT for every partition (e.g. `λ = (2,1)`, `n=3`:
  `Σ h = 5 ≠ 6`, so `E = −1` and `dim_bal = q^{−1} dim_poly(q^2)`). The
  cancellation theorem below states and proves the `E = 0` condition explicitly
  rather than over-claiming an unconditional identity.

  ## References
  - [stanley1999] Enumerative Combinatorics 2 (q-hook / fake degrees)
  - [leitner2026] §mass-theory/binding-period-involution-statistic

  Ground ring (§7c): every declaration is over a generic `Field` with explicit
  `q ≠ 0` / `q^2 ≠ 1` hypotheses. No `ℝ`, no ordering, no archimedean construct.
-/

import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic.Ring

namespace QOU.Mass
namespace QHookDimensionBalanced

open Finset

/-! ## Minimal restatement of the Gaussian pieces (self-contained; Mathlib-only)

These mirror `QOU.Mass.QHookDimension` so this brick needs no QOU library on the
Lean path — only Mathlib. They are the only Gaussian objects the balanced twist
relations refer to. -/

/-- The polynomial (Gaussian) q-integer `[n]_q = Σ_{i<n} q^i`. -/
def qIntPoly {R : Type*} [CommRing R] (q : R) (n : ℕ) : R :=
  ∑ i ∈ Finset.range n, q ^ i

@[simp] theorem qIntPoly_zero {R : Type*} [CommRing R] (q : R) :
    qIntPoly q 0 = 0 := by simp [qIntPoly]

/-- `(q − 1) · [n]_q = q^n − 1` — the geometric-sum relation in multiplicative
form (over any commutative ring; no division). -/
theorem sub_one_mul_qIntPoly {R : Type*} [CommRing R] (q : R) (n : ℕ) :
    (q - 1) * qIntPoly q n = q ^ n - 1 := by
  unfold qIntPoly
  rw [mul_comm]
  exact geom_sum_mul q n

/-- The q-factorial `[n]_q! = ∏_{i<n} [i+1]_q`. -/
def qFactPoly {R : Type*} [CommRing R] (q : R) (n : ℕ) : R :=
  ∏ i ∈ Finset.range n, qIntPoly q (i + 1)

@[simp] theorem qFactPoly_zero {R : Type*} [CommRing R] (q : R) :
    qFactPoly q 0 = 1 := by simp [qFactPoly]

/-- The q-hook dimension `dim_q(λ) = [n]_q! / ∏_{h ∈ hooks} [h]_q` (polynomial
normalization). -/
noncomputable def dimQ {R : Type*} [Field R] (q : R) (n : ℕ) (hooks : Multiset ℕ) : R :=
  qFactPoly q n / (hooks.map (qIntPoly q)).prod

/-! ## The balanced quantum integer `[n]_bal = (q^n − q^{−n})/(q − q^{−1})` -/

/-- The balanced quantum integer `[n]_bal = (q^n − q^{−n})/(q − q^{−1})`, over a
generic `Field`. Singular only at `q^2 = 1` (where `q − q⁻¹ = 0`); the balanced
identities below carry `q ≠ 0`, `q^2 ≠ 1`. -/
noncomputable def qIntBal {R : Type*} [Field R] (q : R) (n : ℕ) : R :=
  (q ^ n - q⁻¹ ^ n) / (q - q⁻¹)

/-- `q − q⁻¹ ≠ 0` when `q ≠ 0` and `q^2 ≠ 1`. The only place the singularity of
the balanced form is excluded. -/
theorem sub_inv_ne_zero {R : Type*} [Field R] {q : R} (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    q - q⁻¹ ≠ 0 := by
  intro h
  apply hq2
  have hqeq : q = q⁻¹ := sub_eq_zero.mp h
  have hmul : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  rw [← hqeq] at hmul
  rw [sq]
  exact hmul

/-- **Balanced defining identity**: `(q − q⁻¹) · [n]_bal = q^n − q^{−n}`. The
clean multiplicative form of the balanced quantum integer (no `0/0`), given
`q ≠ 0`, `q^2 ≠ 1`. -/
theorem sub_inv_mul_qIntBal {R : Type*} [Field R] (q : R) (n : ℕ)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    (q - q⁻¹) * qIntBal q n = q ^ n - q⁻¹ ^ n := by
  unfold qIntBal
  rw [← mul_div_assoc, mul_div_cancel_left₀ _ (sub_inv_ne_zero hq hq2)]

/-- **The exact monomial twist relation** (turns the sibling docstring's prose
claim into a lemma): `[n]_bal = q^{−(n−1)} · qIntPoly(q^2) n`, written with
`(q⁻¹)^(n−1)`. Given `q ≠ 0`, `q^2 ≠ 1`.

Verified small cases: `n=1 ↦ 1 = 1`; `n=2 ↦ q + q⁻¹ = q⁻¹ · (1 + q^2)`. -/
theorem qIntBal_eq_twist {R : Type*} [Field R] (q : R) (n : ℕ)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qIntBal q n = q⁻¹ ^ (n - 1) * qIntPoly (q ^ 2) n := by
  apply mul_left_cancel₀ (sub_inv_ne_zero hq hq2)
  rw [sub_inv_mul_qIntBal q n hq hq2]
  cases n with
  | zero => simp [qIntPoly]
  | succ m =>
      simp only [Nat.add_sub_cancel]
      have hfac : q - q⁻¹ = q⁻¹ * (q ^ 2 - 1) := by
        have h1 : q⁻¹ * q ^ 2 = q := by
          rw [sq, ← mul_assoc, inv_mul_cancel₀ hq, one_mul]
        rw [mul_sub, h1, mul_one]
      have hgeom : (q ^ 2 - 1) * qIntPoly (q ^ 2) (m + 1) = (q ^ 2) ^ (m + 1) - 1 :=
        sub_one_mul_qIntPoly (q ^ 2) (m + 1)
      rw [hfac]
      rw [show q⁻¹ * (q ^ 2 - 1) * (q⁻¹ ^ m * qIntPoly (q ^ 2) (m + 1))
            = q⁻¹ ^ (m + 1) * ((q ^ 2 - 1) * qIntPoly (q ^ 2) (m + 1)) by ring]
      rw [hgeom, mul_sub, mul_one, ← mul_pow]
      have hqq2 : q⁻¹ * q ^ 2 = q := by
        rw [sq, ← mul_assoc, inv_mul_cancel₀ hq, one_mul]
      rw [hqq2]

/-! ## Factorial-level twist and the balanced q-hook dimension -/

/-- The balanced q-factorial `[n]_bal! = ∏_{i<n} [i+1]_bal`. -/
noncomputable def qFactPoly_bal {R : Type*} [Field R] (q : R) (n : ℕ) : R :=
  ∏ i ∈ Finset.range n, qIntBal q (i + 1)

/-- **Factorial-level twist**: `[n]_bal! = q^{−Σ_{i<n} i} · qFactPoly(q^2) n`
(written `(q⁻¹)^(Σ_{i<n} i) · …`). The per-factor monomial twists accumulate to
the triangular exponent `Σ_{i<n} i = n(n−1)/2`. Given `q ≠ 0`, `q^2 ≠ 1`. -/
theorem qFactPoly_bal_eq_twist {R : Type*} [Field R] (q : R) (n : ℕ)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qFactPoly_bal q n
      = q⁻¹ ^ (∑ i ∈ Finset.range n, i) * qFactPoly (q ^ 2) n := by
  unfold qFactPoly_bal qFactPoly
  rw [← Finset.prod_pow_eq_pow_sum, ← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl (fun i _ => ?_)
  rw [qIntBal_eq_twist q (i + 1) hq hq2, Nat.add_sub_cancel]

/-- The q-hook dimension in the balanced normalization:
`dim_bal(λ) = [n]_bal! / ∏_{h ∈ hooks} [h]_bal`. -/
noncomputable def dimQ_bal {R : Type*} [Field R] (q : R) (n : ℕ) (hooks : Multiset ℕ) : R :=
  qFactPoly_bal q n / (hooks.map (qIntBal q)).prod

/-- The hook-product twist split: `∏_{h} [h]_bal = (∏_{h} q^{−(h−1)}) · ∏_{h} [h]_{q^2}`.
Given `q ≠ 0`, `q^2 ≠ 1`. -/
theorem hookprod_bal_split {R : Type*} [Field R] (q : R) (hooks : Multiset ℕ)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    (hooks.map (qIntBal q)).prod
      = (hooks.map (fun h => q⁻¹ ^ (h - 1))).prod * (hooks.map (qIntPoly (q ^ 2))).prod := by
  rw [show hooks.map (qIntBal q)
        = hooks.map (fun h => q⁻¹ ^ (h - 1) * qIntPoly (q ^ 2) h) from
      Multiset.map_congr rfl (fun h _ => qIntBal_eq_twist q h hq hq2)]
  rw [Multiset.prod_map_mul]

/-- **Balanced ↔ Gaussian hook-dimension cancellation (exact condition).** When
the accumulated hook-denominator twist matches the numerator (factorial) twist —
`∏_{h ∈ hooks} q^{−(h−1)} = q^{−Σ_{i<n} i}` — the overall balanced twist cancels
and `dim_bal(λ) = dim_{q^2}(λ)`. The hypothesis holds exactly when
`Σ_{h ∈ hooks} (h−1) = Σ_{i<n} i` (for a genuine partition `λ ⊢ n`,
`hooks.card = n`, this is `Σ h = n(n+1)/2` — true for hook / row / column shapes,
false in general, e.g. `λ = (2,1)`; see the module docstring). Given
`q ≠ 0`, `q^2 ≠ 1`. -/
theorem dimQ_bal_eq_dimQ_of_twist_cancel {R : Type*} [Field R] (q : R) (n : ℕ)
    (hooks : Multiset ℕ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (htw : (hooks.map (fun h => q⁻¹ ^ (h - 1))).prod = q⁻¹ ^ (∑ i ∈ Finset.range n, i)) :
    dimQ_bal q n hooks = dimQ (q ^ 2) n hooks := by
  unfold dimQ_bal dimQ
  rw [qFactPoly_bal_eq_twist q n hq hq2, hookprod_bal_split q hooks hq hq2, htw,
    mul_div_mul_left _ _ (pow_ne_zero _ (inv_ne_zero hq))]

end QHookDimensionBalanced
end QOU.Mass
