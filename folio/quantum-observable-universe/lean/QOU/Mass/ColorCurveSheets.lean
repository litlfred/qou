/-
Copyright (c) 2026 litlfred. All rights reserved.

# Sheet structure of the q-shift correspondence — framing the branch-selection wall

Fourth concrete W1 ingredient (bean `qou-d8de`). The branch-selection obstruction
localized by `ColorCurveQPartials.qPartialZ_on_curve` (on `Σ`, `Δ_q^z C(X,z) = C_{qz}(X)`)
is a choice of one of the **three sheets** over the shifted base `qz`. This file frames
that choice exactly, in Galois / symmetric-function terms, and shows what the defect
measures.

- **`colorCubic_from_sheets`** — Vieta reconstruction: the three sheets `X₁,X₂,X₃` over
  `z`, through their elementary symmetric functions (`e₁ = −(z+1) = −[2]_z`,
  `e₂ = z²+z+1 = [3]_z`, `e₃ = −(z³+z²+z+1) = −[4]_z` — the q-integers), reconstruct the
  curve `∏(X−Xᵢ) = C_z(X)`. So the sheets are governed **collectively** by the q-integer
  coefficients; a branch choice **breaks** this S₃ symmetry.
- **`defect_eq_shifted_sheet_product`** — on `Σ`, the q-shift defect equals the product
  of gaps to the three **shifted** sheets `Y₁,Y₂,Y₃` (roots of `C_{qz}`):
  `Δ_q^z C(X,z) = (X−Y₁)(X−Y₂)(X−Y₃)`. Hence the branch is **coherent** (defect `= 0`)
  iff `X` already coincides with one shifted sheet — and the prolongation `D_q` must
  *select* that sheet.

**The honest wall.** Which sheet `Yᵢ` continues `X`, single-valuedly, is the
**monodromy** of the 3-sheeted cover around the branch points (the `branchSextic` zeros).
That monodromy is the fibre root-of-unity datum; its `(−1)ⁿ` parity is already proved on
main (`Brings.RamificationParityMonodromy`). Turning "a coherent choice exists locally"
into a **global single-valued** algebraic `D_q` is the genuine transcendental core — not
closed here, beaned (`qou-d8de`). This file supplies the exact algebraic frame around it;
it asserts **no** single-valued selection and **no** `symbol = C1` (anti-laundering).

**Scope.** Exact symmetric-function frame. Sorry-free, §7c generic `CommRing`. No fit;
nothing wired.

-- Ref: [leitner2026] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md (W1/G1)
-/
import QOU.Mass.ColorCurveQPartials

namespace QOU.Mass.ColorCurveSheets

open QOU.MathlibExt.QDifferenceOperator
open QOU.Mass.ColorCurveQIntegerForm
open QOU.Mass.ColorCurveQPartials

variable {R : Type*} [CommRing R]

/-- **Vieta reconstruction.** If `X₁,X₂,X₃` are the three sheets over `z` — i.e. their
elementary symmetric functions are the (q-integer) coefficients of `C_z` — then they
reconstruct the curve: `(X−X₁)(X−X₂)(X−X₃) = C_z(X)`. The sheets are governed collectively
by the q-integer symmetric functions; branch selection breaks this S₃ symmetry. -/
theorem colorCubic_from_sheets (z X X₁ X₂ X₃ : R)
    (h1 : X₁ + X₂ + X₃ = -(z + 1))
    (h2 : X₁ * X₂ + X₁ * X₃ + X₂ * X₃ = z ^ 2 + z + 1)
    (h3 : X₁ * X₂ * X₃ = -(z ^ 3 + z ^ 2 + z + 1)) :
    (X - X₁) * (X - X₂) * (X - X₃) = colorSpectralCubic z X := by
  have expand : (X - X₁) * (X - X₂) * (X - X₃)
      = X ^ 3 - (X₁ + X₂ + X₃) * X ^ 2
        + (X₁ * X₂ + X₁ * X₃ + X₂ * X₃) * X - X₁ * X₂ * X₃ := by ring
  rw [expand, h1, h2, h3, colorSpectralCubic]; ring

/-- **The defect is the product of gaps to the shifted sheets.** On `Σ` (`C_z(X)=0`), if
`Y₁,Y₂,Y₃` are the sheets over the shifted base `qz` (`C_{qz}(Y)=∏(Y−Yᵢ)` at `Y=X`), then
the q-shift defect is `Δ_q^z C(X,z) = (X−Y₁)(X−Y₂)(X−Y₃)`. Thus the branch is coherent
(defect `0`) iff `X` equals one shifted sheet; selecting that sheet is the branch datum
`D_q` must provide. -/
theorem defect_eq_shifted_sheet_product (q z X Y₁ Y₂ Y₃ : R)
    (hcurve : colorSpectralCubic z X = 0)
    (hfac : colorSpectralCubic (q * z) X = (X - Y₁) * (X - Y₂) * (X - Y₃)) :
    qDiff q (fun W => colorSpectralCubic W X) z = (X - Y₁) * (X - Y₂) * (X - Y₃) := by
  rw [qPartialZ_on_curve q z X hcurve, hfac]

end QOU.Mass.ColorCurveSheets
