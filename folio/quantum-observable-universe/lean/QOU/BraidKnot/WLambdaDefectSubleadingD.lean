import Mathlib.Tactic

/-!
# W_λ partition-function defect — sub-leading coefficient `D(n)` (keystone, h⁴ order)

Companion to `WLambdaDefectClosedForm.lean` (the leading `C(n)`). The q-Plancherel
partition function `Z(n) = Σ_{λ⊢n} d_q(λ)²/[n]_q!` (balanced `[m]_q`, `h = q − q⁻¹`)
has the even-in-`h` defect expansion

    1 − Z(n) = C(n)·h² + D(n)·h⁴ + O(h⁶),

with the leading `C(n) = −n(n−1)(2n−13)/144` proved + cross-checked in the companion
file/probe. This file formalizes the **sub-leading** coefficient

    D(n) = n(n−1)(−100n⁴+1472n³−5273n²−203n−828) / 1036800,   1036800 = 50·144².

## Epistemic status (honest framing — read before extending)

`D(n)` is **NOT** derived here from a closed symbolic collapse the way `C(n)` is. The
companion probe
[`computations/keystone_wlambda_defect_dn_subleading.py`](../../../../../../computations/keystone_wlambda_defect_dn_subleading.py)
extracted `D(n)` **numerically** — as the `h⁴` Taylor coefficient of `1 − Z(n)` via
`mp.taylor` (method-validated: the `h²` coefficient reproduces the proved-exact `C(n)`
to `0.0`; tight `1e-25` rational tolerance), proved its degree-6 polynomiality by
constant 6th finite difference, interpolated the unique degree-6 polynomial through
`n=2..8`, and **validated it on held-out `n=9,10` (PASS, exact)**. The symbolic
expansion of the `h⁴` coefficient into named Plancherel moments — the `h⁴` analogue of
the `h²` Identity I `M(n)=n(3n−1)/2` that gives `C(n)` — is **not yet in hand**, so this
file does *not* claim to derive `D(n)` from the defect.

What is genuinely Lean-checked below (sorry-free, pure `ℤ`, no archimedean input — `q₀`
never appears, this is the `h→0` limit): the closed-form polynomial's **algebra**
(factored ↔ expanded), the shared `n(n−1)` **vanishing**, the `50·144²` **denominator**
and the `144^k` ladder of denominators, and the **value table** cross-checking the
witness's `1036800·D(n)` integers (held-out `n=9,10` included). The *derivation* of
`D(n)` from `1 − Z(n)` stays **deferred** — exactly parallel to how the companion file
defers the general-`n` Identity I (which needs the hook-length formula, absent from
Mathlib). Ref: [manuscript] docs/audits/2026-06-24-wlambda-defect-cn-closedform-crosscheck.md
-/

namespace QOU.BraidKnot.WLambdaDefect

/-- `1036800·D(n)` in **factored** form (`1036800 = 50·144²`). `D(n)` is the `h⁴`
coefficient of the `W_λ` defect `1 − Z(n)` (companion `C(n)` is the `h²` coefficient).
Stated cleared of the `/1036800` to stay in `ℤ`. Interpolation-derived + held-out
validated; see the file docstring for epistemic status. -/
def n1036800D (n : ℤ) : ℤ :=
  n * (n - 1) * (-100 * n ^ 4 + 1472 * n ^ 3 - 5273 * n ^ 2 - 203 * n - 828)

/-- **Factored = expanded.** The factored form carried in `n1036800D` agrees with the
witness's `int_coeffs_low_to_high = [0, 828, −625, 5070, −6745, 1572, −100]`
(`keystone-wlambda-defect-dn-subleading.witness.json`). Pure ring identity — this is the
machine-check that the two forms quoted across the PR/audit are the same polynomial. -/
theorem n1036800D_expanded (n : ℤ) :
    n1036800D n =
      -100 * n ^ 6 + 1572 * n ^ 5 - 6745 * n ^ 4 + 5070 * n ^ 3 - 625 * n ^ 2 + 828 * n := by
  simp only [n1036800D]; ring

/-- **Vanishing at the trivial partitions.** `D(n)` carries the same `n(n−1)` factor as
`C(n) = −n(n−1)(2n−13)/144`, so the `h⁴` defect coefficient vanishes at `n = 0, 1` —
consistent with `Z(1) = 1` exactly (no defect for the single-box partition). -/
theorem n1036800D_vanishes : n1036800D 0 = 0 ∧ n1036800D 1 = 0 := by
  refine ⟨?_, ?_⟩ <;> decide

/-- **The `144^k` denominator ladder.** Across the defect's coefficient ladder the
denominators are `m_k·144^k`: `C(n)` carries `144`, `D(n)` carries `1036800 = 50·144²`,
`E(n)` carries `21946982400 = 7350·144³` (witness `keystone-wlambda-defect-coeff-ladder`).
The Identity-I `144` recurs at every order. Pure `ℤ` arithmetic. -/
theorem denom_ladder :
    (144 : ℤ) = 144 ^ 1 ∧
    (1036800 : ℤ) = 50 * 144 ^ 2 ∧
    (21946982400 : ℤ) = 7350 * 144 ^ 3 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-- **Value table — cross-check against the witness.** `n1036800D n = 1036800·D(n)` for
`n = 2..10`; these integers equal `1036800·` the per-`n` rationals in
`keystone-wlambda-defect-dn-subleading.witness.json` (held-out `n = 9, 10` PASS). Unlike
`C(n)`, `D(n)` has no single clean sign flip — it is negative on `2..6`, positive on
`7..8`, negative on `9..10` (the quartic factor `−100n⁴+1472n³−5273n²−203n−828`). -/
theorem n1036800D_table :
    n1036800D 2 = -24300 ∧ n1036800D 3 = -103500 ∧ n1036800D 4 = -208800 ∧
    n1036800D 5 = -243360 ∧ n1036800D 6 = -105660 ∧ n1036800D 7 = 175140 ∧
    n1036800D 8 = 231840 ∧ n1036800D 9 = -920160 ∧ n1036800D 10 = -5234220 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num [n1036800D]

end QOU.BraidKnot.WLambdaDefect
