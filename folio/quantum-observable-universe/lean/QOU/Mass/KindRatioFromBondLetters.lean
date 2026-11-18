/-
Copyright (c) 2026 litlfred. All rights reserved.

# The kind-ratio `ρ_pp` in closed form, from the derived bond letters

`QOU.Mass.KindDependentBondBreaksIntegrality` states a target and a direction of
use, verbatim:

    rho_pp  =  1 + rMeasured  =  2433859 / 1483044  ≈  1.64112

    "Read RIGHT-TO-LEFT only: this is the number `qou-qqm4`'s derived `z + d_kind`
     at the `pp` interface must independently produce.  Computing `ρ_pp` from the
     left is a one-parameter fit ... Agreement would be a parameter-free
     prediction; disagreement is a real negative about the bond model."

It also records that the corpus had taken the escape it names and that **nobody
connected the two**.  `qou-qqm4` closed on 2026-09-13
(`QOU.Hecke.BondLetterIdentification`, sorry-free): the interior bond factor is
`b(t) = z − h·t` for **every** `t`, with `t = 0` at `pp`, `t = 1` at `nn`, and
`t = 1/2 − δ/4` at the production `pn` letter.  So the input exists, and this
file supplies the left-hand side as an exact rational function of `q`.

## What is proved here

With `P q = q¹⁰ − 2q⁹ + 7q⁸ − 2q⁶ + 4q⁵ + 4q⁴ + q² − 2q + 1`:

* `bPN_eq` — the production `pn` factor is `P q / (12 q⁵ (q²+1))`, which is
  **exactly** the degree-10 closed form `qbeta_bond_factors_derived_probe`
  extracted from the 2H / 3H traces.  The derived letter and the extracted
  constant are the same object, as a rational function, not to a tolerance.
* `rhoPP_eq` — `ρ_pp = b_pp / b_pn = 12 q⁸ / P q`.
* `rhoNN_eq` — `ρ_nn = b_nn / b_pn = 12 q⁴ / P q`.
* `rho_pp_div_rho_nn` — their ratio is `q⁴`, which is
  `BondLetterIdentification.nnFactor_eq_ppFactor_div_q_pow_four` seen through the
  `pn` reference; the `pn` letter cancels, so this holds whatever `t_pn` is.

## What is NOT proved here, and it is the point

**The comparison to the target is a NEGATIVE, and it is numerical, so it is not
in this file.**  At the proton-pinned `q₀`, `ρ_pp = 1.2055335007` against the
forced `1.6411239316`.  Scored on `b₃/b₂` at the minimal `³He` carrier (`ppn`:
one `pp` pair, two `pn`):

| carrier | `ρ_pp` | `b₃/b₂` | miss |
|---|---|---|---|
| uniform `ρ = 1` (the exhaustion's premise) | `1` | `0` | −100 % |
| best **integer** carrier `ρ = 2` | `2` | `1` | +55.976 % |
| **derived** | `1.2055335007` | `0.2055335007` | **−67.942 %** |
| target | `1.6411239316` | `0.6411239316` | 0 |

So the derived kind-dependence moves `b₃/b₂` off zero and *toward* the
measurement — about a third of the way — and lands **further** from it than the
integer carrier the exhaustion had already excluded.  Breaking integrality does
not buy the escape that file identifies.

**Scope (a)**: this carrier, these weights, at the minimal Brunnian counts.  No
invariant is proved, so kind-dependent weights are **not** excluded in general,
and this must not be written up as a scope-(b) exclusion.

**Which ratio, and why not the other.**  `ρ_pp` could mean the ratio of the bond
*factors* or the ratio of their *logs* (the binding is `B = −α·log μ`, so a
log-space reading is defensible).  The factor ratio is taken here **on the target
file's own wording** — it says `z + d_kind`, which is the factor — and *not*
because it scores better, which it does (the log ratio gives −143.077 %).
Selecting on the residual would be selection against the target.

Probe: `computations/qbeta/kind_dependent_rho_pp_derived_check.py` (5/5).

§7c: pure rational-function identities over a field — no ordering, no
`Real.sqrt`, no archimedean construct — so this is stated over a generic
`[Field R] [CharZero R]` with the three non-vanishing hypotheses made explicit.
`CharZero` is **mathematically required, not a tactic convenience**: `flavorDelta`
divides by `3` and `tPN` by `2` and `4`, so every statement below is false in
characteristic 2 or 3.  Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Mass.KindRatioFromBondLetters

variable {R : Type*} [Field R] [CharZero R]

/-- The convention-D Markov parameter `z = q³/(q²+1)`. -/
noncomputable def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The Hecke quadratic constant `h = q − q⁻¹`. -/
noncomputable def hq (q : R) : R := q - q⁻¹

/-- The substrate flavour split `δ = (q−1)²(1 − q⁻⁴)/3`. -/
noncomputable def flavorDelta (q : R) : R := (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3

/-- The production `pn` mixing weight, ctype `averaged_weighted`. -/
noncomputable def tPN (q : R) : R := 1 / 2 - flavorDelta q / 4

/-- `b_pp` — the `pp` bond factor, `BondLetterIdentification.tr_bond_gen` at `t = 0`. -/
noncomputable def bPP (q : R) : R := zD q

/-- `b_pn` — the production `pn` bond factor, `tr_bond_interp` at `t = 1/2 − δ/4`. -/
noncomputable def bPN (q : R) : R := zD q - hq q * tPN q

/-- `b_nn` — the `nn` bond factor, `tr_bond_ginv` at `t = 1`. -/
noncomputable def bNN (q : R) : R := zD q - hq q

/-- The degree-10 numerator that `qbeta_bond_factors_derived_probe` extracted. -/
def bondPoly (q : R) : R :=
  q ^ 10 - 2 * q ^ 9 + 7 * q ^ 8 - 2 * q ^ 6 + 4 * q ^ 5 + 4 * q ^ 4
    + q ^ 2 - 2 * q + 1

/-- **The derived `pn` letter IS the corpus's extracted constant.**

`b_pn = P q / (12 q⁵ (q²+1))` — an identity of rational functions, not an
agreement at `q₀`. The right-hand side is copied verbatim from
`computations/qbeta/qbeta_bond_factors_derived_probe.py`, which obtained it by
extraction from the 2H / 3H traces; the left-hand side is `tr_bond_interp` at the
production weight. -/
theorem bPN_eq (q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    bPN q = bondPoly q / (12 * q ^ 5 * (q ^ 2 + 1)) := by
  unfold bPN bondPoly zD hq tPN flavorDelta
  field_simp
  ring

/-- **`ρ_pp = 12 q⁸ / P q`.** The `pp` bond factor in units of the `pn` one —
the left-hand side `KindDependentBondBreaksIntegrality` asks for. -/
theorem rhoPP_eq (q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hP : bondPoly q ≠ 0) :
    bPP q / bPN q = 12 * q ^ 8 / bondPoly q := by
  rw [bPN_eq q hq0 hq2]
  unfold bPP zD
  field_simp

/-- **`ρ_nn = 12 q⁴ / P q`.** -/
theorem rhoNN_eq (q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hP : bondPoly q ≠ 0) :
    bNN q / bPN q = 12 * q ^ 4 / bondPoly q := by
  rw [bPN_eq q hq0 hq2]
  unfold bNN zD hq
  field_simp
  ring

/-- **The two like-pair kind-ratios differ by exactly `q⁴`.**

This is `BondLetterIdentification.nnFactor_eq_ppFactor_div_q_pow_four` seen
through the `pn` reference: the `pn` letter cancels, so the relation holds
**whatever** `t_pn` is — it does not depend on the production weight being
`1/2 − δ/4`, only on `pp` and `nn` being `t = 0` and `t = 1`. -/
theorem rho_pp_div_rho_nn (q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hP : bondPoly q ≠ 0) :
    (bPP q / bPN q) / (bNN q / bPN q) = q ^ 4 := by
  rw [rhoPP_eq q hq0 hq2 hP, rhoNN_eq q hq0 hq2 hP]
  field_simp

/-- **The derived weighting leaves the uniform locus.** If the two like-pair
kind-ratios coincided, the carrier would be back on the uniform premise
`BrunnianTripleExhaustion` assumes. They coincide only where `q⁴ = 1`, and the
substrate `q₀ ≈ 1.10998` is not such a point — so the escape
`KindDependentBondBreaksIntegrality` names is genuinely taken. Stated in the
direction that needs no characteristic hypothesis. -/
theorem kind_ratios_eq_of_q_pow_four_eq_one (q : R) (hq0 : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hP : bondPoly q ≠ 0) (h : q ^ 4 = 1) :
    (bPP q / bPN q) = (bNN q / bPN q) := by
  rw [rhoPP_eq q hq0 hq2 hP, rhoNN_eq q hq0 hq2 hP]
  have h8 : q ^ 8 = q ^ 4 := by
    calc q ^ 8 = q ^ 4 * q ^ 4 := by ring
    _ = q ^ 4 * 1 := by rw [h]
    _ = q ^ 4 := by ring
  rw [h8]

/-- **Vanishing difference form of `rho_pp_div_rho_nn` (`qou-306p`).**
When `q ≠ 0`, `q ^ 2 + 1 ≠ 0`, and `bondPoly q ≠ 0`,
`(bPP q / bPN q) / (bNN q / bPN q) - q ^ 4 = 0`. -/
theorem rho_pp_div_rho_nn_sub_eq_zero (q : R) (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hP : bondPoly q ≠ 0) :
    (bPP q / bPN q) / (bNN q / bPN q) - q ^ 4 = 0 :=
  sub_eq_zero.mpr (rho_pp_div_rho_nn q hq0 hq2 hP)

end QOU.Mass.KindRatioFromBondLetters
