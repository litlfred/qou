import Mathlib.Tactic

/-!
# W_λ partition-function defect — third ladder rung `E(n)` (keystone, h⁶ order)

Third rung of the `W_λ` defect coefficient ladder, after `C(n)` (h², `WLambdaDefectClosedForm`)
and `D(n)` (h⁴, `WLambdaDefectSubleadingD`). The q-Plancherel defect
`1 − Z(n) = Σ_{k≥1} c_{2k}(n)·h^{2k}` (`h = q − q⁻¹`) has

    E(n) = c_6(n) = n(n−1)(−9800n⁷+231868n⁶−1736102n⁵+3569065n⁴+2984824n³+14079061n²−55086084n+68423904)
                    / 21946982400,   21946982400 = 7350·144³.

`deg E = 9 = 3·3`, completing the **`deg c_{2k}(n) = 3k`** ladder for k=1,2,3 with denominator
`m_k·144^k` (`m_k ∈ {1, 50, 7350}`) — the Identity-I `144` recurs cubed at this order
(`denom_ladder` in `WLambdaDefectSubleadingD.lean` proves all three `144^k` denominators).

## Epistemic status (honest framing — same as `D(n)`)

`E(n)` is **NOT** derived here from a symbolic moment-collapse. The companion probe
[`computations/keystone_wlambda_defect_coeff_ladder.py`](../../../../../../computations/keystone_wlambda_defect_coeff_ladder.py)
extracted `E(n)` **numerically** as the `h⁶` Taylor coefficient of `1 − Z(n)` via `mp.taylor`
(method-validated: the `h²` coefficient reproduces the proved-exact `C(n)` to `0.0`), proved its
degree-9 polynomiality by constant 9th finite difference, interpolated the unique degree-9
polynomial, and **validated it on held-out `n = 12, 13, 14` (PASS, exact)**. The `deg c_{2k} = 3k`
law itself is a **conjecture** on k=1,2,3 evidence (expected from Kerov–Olshanski / Kerov-polynomial
theory — Plancherel moments are polynomial on Young diagrams — the QOU-specific content being the
sharp `3k` degree + `144^k` denominator).

What is Lean-checked below (sorry-free, pure `ℤ`, `q₀` never used — the `h→0` limit): the closed-form
polynomial's **algebra** (factored ↔ the witness's expanded `int_coeffs_low_to_high`), the shared
`n(n−1)` **vanishing** at `n=0,1`, and the **value table** cross-checking `21946982400·E(n)` for
`n=2..14` (held-out `12,13,14` included). The *derivation* of `E(n)` from the defect stays **deferred**
— parallel to `C(n)`'s general-`n` Identity I. The Lean file formalizes the closed form's algebra and
witness cross-check, not a derivation.
Ref: [leitner2026] docs/audits/2026-06-24-wlambda-defect-cn-closedform-crosscheck.md
-/

namespace QOU.BraidKnot.WLambdaDefect

/-- `21946982400·E(n)` in **factored** form (`21946982400 = 7350·144³`). `E(n)` is the `h⁶`
coefficient (3rd ladder rung) of the `W_λ` defect `1 − Z(n)`. Stated cleared of the denominator to
stay in `ℤ`. Interpolation-derived + held-out validated (`n=12,13,14`); see the file docstring for
epistemic status. -/
def n21946982400E (n : ℤ) : ℤ :=
  n * (n - 1) *
    (-9800 * n ^ 7 + 231868 * n ^ 6 - 1736102 * n ^ 5 + 3569065 * n ^ 4 + 2984824 * n ^ 3
      + 14079061 * n ^ 2 - 55086084 * n + 68423904)

/-- **Factored = expanded.** The factored form agrees with the ladder witness's degree-9
`int_coeffs_low_to_high` for `E` (`keystone-wlambda-defect-coeff-ladder.witness.json`). Pure ring
identity — the machine-check that the factored and expanded forms are the same polynomial. -/
theorem n21946982400E_expanded (n : ℤ) :
    n21946982400E n =
      -9800 * n ^ 9 + 241668 * n ^ 8 - 1967970 * n ^ 7 + 5305167 * n ^ 6 - 584241 * n ^ 5
        + 11094237 * n ^ 4 - 69165145 * n ^ 3 + 123509988 * n ^ 2 - 68423904 * n := by
  simp only [n21946982400E]; ring

/-- **Vanishing at the trivial partitions.** `E(n)` carries the same `n(n−1)` factor as `C(n)` and
`D(n)`, so the `h⁶` defect coefficient vanishes at `n = 0, 1` — consistent with `Z(1) = 1` exactly. -/
theorem n21946982400E_vanishes : n21946982400E 0 = 0 ∧ n21946982400E 1 = 0 := by
  refine ⟨?_, ?_⟩ <;> norm_num [n21946982400E]

/-- **Denominator — 3rd rung of the `144^k` ladder.** `21946982400 = 7350·144³` (cf. `C`'s `144`,
`D`'s `50·144²`; all three collected in `WLambdaDefectSubleadingD.denom_ladder`). -/
theorem denom_E : (21946982400 : ℤ) = 7350 * 144 ^ 3 := by norm_num

/-- **Value table — cross-check against the witness.** `n21946982400E n = 21946982400·E(n)` for
`n = 2..14`; these integers equal `21946982400·` the per-`n` rationals in the ladder witness
(held-out `n = 12, 13, 14` PASS). -/
theorem n21946982400E_table :
    n21946982400E 2 = 107163000 ∧
    n21946982400E 3 = 751728600 ∧
    n21946982400E 4 = 2273443200 ∧
    n21946982400E 5 = 3614647680 ∧
    n21946982400E 6 = 2691458280 ∧
    n21946982400E 7 = -190443960 ∧
    n21946982400E 8 = 1010257920 ∧
    n21946982400E 9 = 10195476480 ∧
    n21946982400E 10 = -12713115240 ∧
    n21946982400E 11 = -265474911240 ∧
    n21946982400E 12 = -1345691128320 ∧
    n21946982400E 13 = -4700287388160 ∧
    n21946982400E 14 = -13386998210040 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num [n21946982400E]

end QOU.BraidKnot.WLambdaDefect
