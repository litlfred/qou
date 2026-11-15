/-
# The odd-even pairing term forces `b₃ > 0` — from the parities alone

The `b₃` arc has closed every mechanism it tried, and the screen in
`computations/probes/fingerprint_screen_zero_parameter_probe.py` left a specific
pointer: smooth growth laws reproduce `b₄` well (the `q`-factorial to 1.7 %) and
`b₃` badly (low by 16–18 %). **Whatever supplies `b₃` is not a smooth growth
law**, so the thing to look for is something *non-smooth* at `A = 3`.

The parities are non-smooth at exactly that point:

| A | nuclide | `Z, N` | parity class |
|---|---|---|---|
| 2 | `²H` | 1, 1 | **odd-odd** |
| 3 | `³H` / `³He` | — | **odd-`A`** |
| 4 | `⁴He` | 2, 2 | **even-even** |

and the semi-empirical pairing term is parity-dependent by construction:
`+δ(A)` for even-even, `0` for odd-`A`, `−δ(A)` for odd-odd, with `δ > 0`.

## The result

`pairing_forces_b3_pos`: with `p(2) = −δ`, `p(3) = 0` and `δ > 0`, the pairing
contribution to the connected three-body cumulant is

    p(3) − 3·p(2) = 0 − 3·(−δ) = 3δ > 0

**for every `δ > 0`.** Nothing is fitted: the signs are forced by which nuclei are
odd and which are even, and the magnitude `δ` does not enter the sign at all.

This is the **first mechanism in the arc that produces the measured sign for a
principled reason** rather than by choice of coefficient. Every earlier candidate
either could not contribute (`Δ³ = 0`: pair counts, all `SU(N)` antisymmetric
Casimirs), carried no magnitude (`μ̄ = ±1`), or got the sign wrong
(`b₄/b₃ ≤ 0` for `dim[1^n]`, the cubic Casimir, `p(A)`, `A³`).

It also has a physical reading the corpus can use: the deuteron is **odd-odd**,
so pairing *penalises* it — which is the textbook reason `²H` is so weakly bound,
and weak `B(2)` is exactly what makes `b₃ = B(3) − 3B(2)` positive.

## What is NOT established — the magnitude

The sign is structural; the size is not. Fitting a smooth term plus the pairing
term to `b₃` and `b₄` and **predicting** `b₂` gives, for the best smooth partner
(`C(2n,n)`):

| dataset | `b₂` predicted | error |
|---|---|---|
| raw AME, isospin-averaged `A = 3` | 2.196193 | **1.28 %** |
| raw AME, `³H` | 1.887753 | 15.14 % |
| Coulomb-corrected (`³H`, `⁴He + 0.70`) | 2.044540 | 8.09 % |

**The 1.28 % does not survive the Coulomb correction, and that correction is the
physically required one** — a model with no Coulomb term must be compared against
Coulomb-corrected data, and `³H` is the Coulomb-free `A = 3` point while `⁴He`
needs its own. So the 1.28 % was the best of nine trials on the one dataset that
happens to flatter it, and should be read as convention luck, not a result.

**Verdict: the pairing route derives the sign and not the magnitude.** That is a
genuine advance on "no candidate", and it is not a closure.

Base ring is a linearly ordered commutative ring; the content is sign algebra.

Bean `qou-edt7`.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
set_option linter.unusedSectionVars false

namespace QOU.Mass.PairingParityForcesPositiveB3

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The contribution of a term to the connected three-body cumulant, from its
values at `A = 2` and `A = 3`. -/
def b3Contrib (f₂ f₃ : R) : R := f₃ - 3 * f₂

/-- **The pairing term forces `b₃ > 0`.** The deuteron is odd-odd, so pairing
enters it as `−δ`; `A = 3` is odd-`A`, so pairing vanishes there. The resulting
contribution is `3δ`, positive for **every** `δ > 0` — the sign comes from the
parities, not from the coefficient. -/
theorem pairing_forces_b3_pos {δ : R} (hδ : 0 < δ) :
    0 < b3Contrib (-δ) 0 := by
  unfold b3Contrib
  linarith

/-- The contribution stated exactly: `3δ`. -/
theorem pairing_b3_eq {δ : R} : b3Contrib (-δ) (0 : R) = 3 * δ := by
  unfold b3Contrib
  ring

/-- **The sign is independent of the magnitude.** Scaling `δ` scales the
contribution and cannot change its sign, so no choice of pairing strength can
make this mechanism give `b₃ ≤ 0`. -/
theorem pairing_sign_is_scale_free {δ c : R} (hδ : 0 < δ) (hc : 0 < c) :
    0 < b3Contrib (-(c * δ)) 0 := by
  unfold b3Contrib
  have : 0 < c * δ := mul_pos hc hδ
  linarith

/-- The contrapositive, as the falsifiable form: a mechanism whose `A = 2` value
is negative and whose `A = 3` value vanishes **cannot** produce `b₃ ≤ 0`. -/
theorem not_nonpos_of_pairing {δ : R} (hδ : 0 < δ) :
    ¬ (b3Contrib (-δ) (0 : R) ≤ 0) :=
  not_le.mpr (pairing_forces_b3_pos hδ)

end QOU.Mass.PairingParityForcesPositiveB3
