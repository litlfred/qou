import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.VdwPskew — van der Waals is the bar-odd (sinh / P_skew) channel

The Hopf link `σ₁² = q²·e₊ + q⁻²·e₋`
([`prop:hopf-link-symmetric-decomposition`](hopf-link-symmetric-decomposition.md))
splits under the **bar involution** `q ↦ q⁻¹` (the swap `q ↔ qi` of the formal
inverse `qi`) into a bar-even and a bar-odd part. Writing the (un-normalised)
bar coefficients `Ce = q² + qi²` (`= 2cosh 2λ`, `λ = ln q`) and
`Co = q² − qi²` (`= 2sinh 2λ`):

  `2·(q²·a + qi²·b) = Ce·(a+b) + Co·(a−b)`.

For the Wedderburn idempotents `a = e₊`, `b = e₋` (so `a+b = 1`,
[`van-der-waals-hopf-channel`](van-der-waals-hopf-channel.md)), this is

  `2·σ₁² = (2cosh 2λ)·𝟙 + (2sinh 2λ)·(e₊ − e₋)`.

The **bar-even** part `cosh(2λ)·𝟙` is the retained `P_avg` carrier (the trivial
identity piece); the **bar-odd** part `sinh(2λ)·(e₊ − e₋)` is the `P_skew` /
Coulomb–EM channel ([`crossing-energy-decomposition`](../observations/crossing-energy-decomposition.md):
`sinh = antisymmetric/EM`), which the canonical `P_avg` projection **discards**.
That bar-odd residual is **van der Waals** — small because discarded, sinh /
h-power suppressed, and (per [`rem-im-q-vs-p-skew`](../mass-theory/rem-im-q-vs-p-skew.md))
**real** at real `q`, not imaginary.

LaTeX label: `prop:vdw-pskew-isolation`.
**Ground ring**: any commutative ring; `q`, `qi` are independent formal
variables (the bar involution is the swap; fibre-level, no reality imposed —
matching the `alpha-em-habiro-bar-involution` convention). The identity is
pure `ring`.
-/

namespace QOU.VdwPskew

variable {R : Type*} [CommRing R]

/-- Bar-even coefficient `q² + qi²` (`= 2cosh 2λ`, `λ = ln q`, `qi = q⁻¹`). -/
def barEven (q qi : R) : R := q ^ 2 + qi ^ 2

/-- Bar-odd coefficient `q² − qi²` (`= 2sinh 2λ`). -/
def barOdd (q qi : R) : R := q ^ 2 - qi ^ 2

/-- **van der Waals = the bar-odd channel.** The Hopf weighting `q²·a + qi²·b`
    splits into a bar-even part on `a+b` and a bar-odd part on `a−b`:

      `2·(q²·a + qi²·b) = (q²+qi²)·(a+b) + (q²−qi²)·(a−b)`.

    For the idempotents (`a = e₊`, `b = e₋`, `a+b = 1`) the bar-even part is the
    retained `cosh(2λ)·𝟙` carrier and the bar-odd part is `sinh(2λ)·(e₊−e₋)` —
    the discarded P_skew / van der Waals channel. Pure-`ring`, sorry-free. -/
-- Ref: [leitner2026] information-theory/vdw-pskew-isolation
theorem hopf_bar_even_odd_decomposition (q qi a b : R) :
    2 * (q ^ 2 * a + qi ^ 2 * b)
      = barEven q qi * (a + b) + barOdd q qi * (a - b) := by
  unfold barEven barOdd
  ring

/-- The bar-odd (van der Waals) part isolated: on the idempotents with
    `a + b = 1`, the whole bar-even contribution is `barEven q qi · 1` and the
    remainder is exactly `barOdd q qi · (a − b)`. -/
-- Ref: [leitner2026] information-theory/vdw-pskew-isolation
theorem vdw_is_bar_odd_residual (q qi a b : R) (hpart : a + b = 1) :
    2 * (q ^ 2 * a + qi ^ 2 * b) - barEven q qi
      = barOdd q qi * (a - b) := by
  have h := hopf_bar_even_odd_decomposition q qi a b
  rw [h, hpart, mul_one]
  ring

end QOU.VdwPskew
