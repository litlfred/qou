/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-partial derivatives of the color spectral cubic, and the branch-selection defect

Third concrete W1 ingredient (bean `qou-d8de`). The classical implicit jet on the SW
curve uses `X'(z) = −(∂_z C)/(∂_X C)`. The q-analog needs the two **q-partial
derivatives** of `C_z(X)` — computed here, exactly, using the `qDiff` operator
(`QDifferenceOperator`). Unlike the chain rule, these are single-variable q-differences
of a polynomial, so they are well-defined with **no** chain-rule obstruction.

- `qPartialX_colorCubic`: `Δ_q^{X} C = (q³−1)X³ + (q²−1)(z+1)X² + (q−1)(z²+z+1)X`.
- `qPartialZ_colorCubic`: `Δ_q^{z} C = (q−1)z·X² + ((q²−1)z²+(q−1)z)·X + ((q³−1)z³+(q²−1)z²+(q−1)z)`.

**The honest payoff — the branch-selection defect (`qPartialZ_on_curve`).** On the curve
`Σ = {C_z(X)=0}`, the z-partial collapses to

  `Δ_q^{z} C(X,z) = C_{qz}(X)`   (since `C_z(X)=0`).

This is exactly the obstruction the no-q-chain-rule discussion pointed at: `C_{qz}(X)`
measures how far the *same* `X` is from being a root over the shifted base `qz`. It is
generically nonzero — `X` does **not** stay on `Σ` under `z↦qz` — and the correction
`X ↦ X_q` (a root of `C_{qz}`) is precisely the **branch/connection datum** a genuine
q-difference prolongation `D_q` must supply. So the q-partials are computable ingredients,
but the jet-tower lift is blocked at exactly this defect: choosing the branch of the
`z↦qz` correspondence on `Σ` (the fibre root-of-unity monodromy). W1's remaining core is
this branch selection, not the calculus.

**Scope.** Exact q-partials + the on-curve defect identity. No jet-tower lift, no symbol
(W2), no `symbol=C1` claim (W3), no conjecture-class (anti-laundering). §7c: generic
`CommRing`. Sorry-free. No fit; nothing wired.

-- Ref: [leitner2026] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md (W1/G1)
-/
import QOU.MathlibExt.QDifferenceOperator
import QOU.Mass.ColorCurveQIntegerForm

namespace QOU.Mass.ColorCurveQPartials

open QOU.MathlibExt.QDifferenceOperator
open QOU.Mass.ColorCurveQIntegerForm

variable {R : Type*} [CommRing R]

/-- **q-partial in `X`** (holding `z`): `Δ_q^{X} C_z(X) = (q³−1)X³ + (q²−1)(z+1)X²
+ (q−1)(z²+z+1)X`. Each degree-`k` term picks up `q^k − 1` (the monomial action). -/
theorem qPartialX_colorCubic (q z X : R) :
    qDiff q (fun Y => colorSpectralCubic z Y) X
      = (q ^ 3 - 1) * X ^ 3 + (q ^ 2 - 1) * (z + 1) * X ^ 2
        + (q - 1) * (z ^ 2 + z + 1) * X := by
  simp only [qDiff, colorSpectralCubic]; ring

/-- **q-partial in `z`** (holding `X`): `Δ_q^{z} C_z(X) = (q−1)z·X² +
((q²−1)z²+(q−1)z)·X + ((q³−1)z³+(q²−1)z²+(q−1)z)`. -/
theorem qPartialZ_colorCubic (q z X : R) :
    qDiff q (fun W => colorSpectralCubic W X) z
      = (q - 1) * z * X ^ 2 + ((q ^ 2 - 1) * z ^ 2 + (q - 1) * z) * X
        + ((q ^ 3 - 1) * z ^ 3 + (q ^ 2 - 1) * z ^ 2 + (q - 1) * z) := by
  simp only [qDiff, colorSpectralCubic]; ring

/-- **The branch-selection defect.** On the curve `C_z(X) = 0`, the z-partial collapses
to `Δ_q^{z} C(X,z) = C_{qz}(X)` — the (generically nonzero) measure of how far `X` fails
to remain a root under `z ↦ qz`. Its vanishing would require `X` to be simultaneously a
root over `z` and `qz`; the correction to a genuine root `X_q` of `C_{qz}` is the branch
datum the q-difference prolongation must choose. This is the precise remaining W1
obstruction. -/
theorem qPartialZ_on_curve (q z X : R) (h : colorSpectralCubic z X = 0) :
    qDiff q (fun W => colorSpectralCubic W X) z = colorSpectralCubic (q * z) X := by
  simp only [qDiff_apply, h, sub_zero]

end QOU.Mass.ColorCurveQPartials
