import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.BraidKnot.per_nucleon_shift_additive_linearity — `shift(Z+1, N) − shift(Z, N) = 18`

**Proposition** ([`prop:per-nucleon-shift-additive-linearity`](../../../quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)).

*The atomic Markov-trace denominator
`D(u) = 2^{2A+1} · u^{shift} · (1 + u²)^{3A−1}` of canonical pppnnn ordering
has shift exponent satisfying the additive-linearity recurrence:*

```
  shift(Z+1, N) − shift(Z, N) = 18,
  shift(Z, N+1) − shift(Z, N) = 21,    for Z, N ≥ 1 (A ≥ 2)
```

*Together with the base case `shift(D) = shift(1, 1) = 40`, this fixes the
closed form `shift(Z, N) = 18Z + 21N + 1` on the entire `A ≥ 2` triangle.*

The per-direction increments `(18, 21)` and the base value `40` are the
categorical/computed *inputs* — derived by Hoefsmit per-irrep pole-order
analysis (witness `per-irrep-pole-{proton-h3,deuteron-h6}.witness.json`).
The **closed form** `shift(Z, N) = 18Z + 21N + 1` is *derived* here from
those inputs by induction over `(Z, N)`, exactly as in the manuscript proof —
not projected from a stored field.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
-/

namespace QOU.BraidKnot

/-- Context carrying the *inputs* of the shift recurrence: the base value
    `shift(1,1) = 40` and the constant per-direction increments `18`
    (per new proton) and `21` (per new neutron), valid for `Z, N ≥ 1`.
    The closed form is NOT a field — it is derived below. -/
class PerNucleonShiftContext where
  /-- The shift exponent `shift(Z, N) : ℤ`. -/
  shift : ℕ → ℕ → ℤ
  /-- Input — base case: `shift(1, 1) = 40` (Hoefsmit deuteron pole order). -/
  shift_base : shift 1 1 = 40
  /-- Input — per-new-proton increment is constantly `18` for `Z, N ≥ 1`. -/
  shift_proton_step : ∀ Z N : ℕ, 1 ≤ Z → 1 ≤ N →
    shift (Z + 1) N - shift Z N = 18
  /-- Input — per-new-neutron increment is constantly `21` for `Z, N ≥ 1`. -/
  shift_neutron_step : ∀ Z N : ℕ, 1 ≤ Z → 1 ≤ N →
    shift Z (N + 1) - shift Z N = 21

/-- **Per-nucleon shift additive linearity**
    ([`prop:per-nucleon-shift-additive-linearity`]).

    Restates the two constant increments — this is the input recurrence
    itself, exposed as the named theorem. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
theorem per_nucleon_shift_additive_linearity
    [ctx : PerNucleonShiftContext] (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    ctx.shift (Z + 1) N - ctx.shift Z N = 18 ∧
    ctx.shift Z (N + 1) - ctx.shift Z N = 21 :=
  ⟨ctx.shift_proton_step Z N hZ hN, ctx.shift_neutron_step Z N hZ hN⟩

/-- Auxiliary: closed form along the `N = 1` row, derived by induction on
    `Z ≥ 1` from the base case and the proton-step increment. -/
theorem per_nucleon_shift_row1 [ctx : PerNucleonShiftContext] :
    ∀ Z : ℕ, 1 ≤ Z → ctx.shift Z 1 = 18 * (Z : ℤ) + 21 * 1 + 1 := by
  intro Z hZ
  induction Z with
  | zero => omega
  | succ k ih =>
    rcases Nat.lt_or_ge 1 (k + 1) with hk | hk
    · -- k ≥ 1: use the proton step at (k, 1) and the IH.
      have hk1 : 1 ≤ k := by omega
      have hstep := ctx.shift_proton_step k 1 hk1 (le_refl 1)
      have hih := ih hk1
      push_cast
      push_cast at hih
      linarith
    · -- k + 1 = 1, i.e. Z = 1: the base case.
      have : k + 1 = 1 := by omega
      rw [this, ctx.shift_base]; norm_num

/-- **Closed form** for the shift exponent in canonical pppnnn ordering
    ([`prop:per-nucleon-shift-additive-linearity`]).  Manuscript boxed
    identity: `shift(Z, N) = 18Z + 21N + 1` for `Z, N ≥ 1`.

    **Derived** by induction: the `N = 1` row from `per_nucleon_shift_row1`,
    then induction on `N` using the neutron-step increment.  This is a
    genuine recurrence-to-closed-form derivation, not a projection. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
theorem per_nucleon_shift_closed_form
    [ctx : PerNucleonShiftContext] (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    ctx.shift Z N = 18 * (Z : ℤ) + 21 * (N : ℤ) + 1 := by
  induction N with
  | zero => omega
  | succ k ih =>
    rcases Nat.lt_or_ge 1 (k + 1) with hk | hk
    · -- k ≥ 1: use the neutron step at (Z, k) and the IH.
      have hk1 : 1 ≤ k := by omega
      have hstep := ctx.shift_neutron_step Z k hZ hk1
      have hih := ih hk1
      push_cast
      push_cast at hih
      linarith
    · -- k + 1 = 1, i.e. N = 1: the row-1 closed form.
      have hN1 : k + 1 = 1 := by omega
      rw [hN1]
      have := per_nucleon_shift_row1 (ctx := ctx) Z hZ
      push_cast at this ⊢
      linarith

end QOU.BraidKnot
