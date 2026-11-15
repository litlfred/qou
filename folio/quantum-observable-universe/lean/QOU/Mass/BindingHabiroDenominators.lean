/-
# Binding q-Gaussian Habiro element — cyclotomic structure of the log-coefficient denominators

Follow-up to `QOU.Mass.BindingQGaussianHabiro` (which certifies the `(q−1)`-order tower of the
log-coefficient *numerators*). This file certifies the complementary, defining **Habiro-ring**
property: the *denominators* of the binding q-Gaussian log-coefficients `L_m` are products of
**cyclotomic polynomials** `Φ_d`. Membership in the cyclotomic-completion ring `ℤ[q]^` (the Habiro
ring) is exactly the statement that the relevant denominators factor over the `Φ_d` — so these
identities are the algebraic certificate of the "Habiro element" claim of the audit
`docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md` (Stage 5).

The denominators (from the exact symbolic compute
`computations/substrate/lever1_binding_habiro_qexponential.py`) are:

    den(L₂) = 2·Φ₄
    den(L₃) = 3·Φ₃·Φ₄·Φ₆
    den(L₄) = 4·Φ₄²·Φ₆·Φ₈
    den(L₅) = 5·Φ₄²·Φ₅·Φ₆·Φ₈·Φ₁₀

with the cyclotomic polynomials `Φ₃ = q²+q+1`, `Φ₄ = q²+1`, `Φ₅ = q⁴+q³+q²+q+1`,
`Φ₆ = q²−q+1`, `Φ₈ = q⁴+1`, `Φ₁₀ = q⁴−q³+q²−q+1` (the `Φ_d` here are the standard cyclotomic
polynomials; cf. `Polynomial.cyclotomic d ℤ` evaluated at `q`). The integer content `m` of
`den(L_m)` is the `1/m` from `log(1 + Σ g z^m)`.

Generic base ring `[CommRing R]` (formal fibre parameter `q`, no archimedean structure, §7c).
Sorry-free; each factorization is a machine-checked `ring` identity.

-- Ref: [leitner2026] docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md §"Stage 5"
-/
import Mathlib.Tactic

namespace QOU.Mass.BindingHabiroDenominators

variable {R : Type*} [CommRing R]

/-! ## Cyclotomic polynomials appearing in the denominators -/

/-- `Φ₃ = q² + q + 1`. -/
def Phi3 (q : R) : R := q ^ 2 + q + 1
/-- `Φ₄ = q² + 1` (the `ζ₄` residue). -/
def Phi4 (q : R) : R := q ^ 2 + 1
/-- `Φ₅ = q⁴ + q³ + q² + q + 1`. -/
def Phi5 (q : R) : R := q ^ 4 + q ^ 3 + q ^ 2 + q + 1
/-- `Φ₆ = q² − q + 1`. -/
def Phi6 (q : R) : R := q ^ 2 - q + 1
/-- `Φ₈ = q⁴ + 1`. -/
def Phi8 (q : R) : R := q ^ 4 + 1
/-- `Φ₁₀ = q⁴ − q³ + q² − q + 1`. -/
def Phi10 (q : R) : R := q ^ 4 - q ^ 3 + q ^ 2 - q + 1

/-! ## The denominators, and their cyclotomic factorizations -/

/-- Denominator of `L₂`: `2q² + 2`. -/
def L2den (q : R) : R := 2 * q ^ 2 + 2
/-- Denominator of `L₃`: `3q⁶ + 6q⁴ + 6q² + 3`. -/
def L3den (q : R) : R := 3 * q ^ 6 + 6 * q ^ 4 + 6 * q ^ 2 + 3
/-- Denominator of `L₄`: `4q¹⁰ − 4q⁹ + 12q⁸ − 8q⁷ + 16q⁶ − 8q⁵ + 16q⁴ − 8q³ + 12q² − 4q + 4`. -/
def L4den (q : R) : R :=
  4 * q ^ 10 - 4 * q ^ 9 + 12 * q ^ 8 - 8 * q ^ 7 + 16 * q ^ 6 - 8 * q ^ 5
    + 16 * q ^ 4 - 8 * q ^ 3 + 12 * q ^ 2 - 4 * q + 4
/-- Denominator of `L₅` (degree 18). -/
def L5den (q : R) : R :=
  5 * q ^ 18 - 5 * q ^ 17 + 20 * q ^ 16 - 15 * q ^ 15 + 40 * q ^ 14 - 25 * q ^ 13
    + 60 * q ^ 12 - 35 * q ^ 11 + 75 * q ^ 10 - 40 * q ^ 9 + 75 * q ^ 8 - 35 * q ^ 7
    + 60 * q ^ 6 - 25 * q ^ 5 + 40 * q ^ 4 - 15 * q ^ 3 + 20 * q ^ 2 - 5 * q + 5

/-- **`den(L₂) = 2·Φ₄`** — the `ζ₄` residue. -/
theorem L2den_cyclotomic (q : R) : L2den q = 2 * Phi4 q := by
  simp only [L2den, Phi4]; ring

/-- **`den(L₃) = 3·Φ₃·Φ₄·Φ₆`**. -/
theorem L3den_cyclotomic (q : R) : L3den q = 3 * Phi3 q * Phi4 q * Phi6 q := by
  simp only [L3den, Phi3, Phi4, Phi6]; ring

/-- **`den(L₄) = 4·Φ₄²·Φ₆·Φ₈`**. -/
theorem L4den_cyclotomic (q : R) : L4den q = 4 * (Phi4 q) ^ 2 * Phi6 q * Phi8 q := by
  simp only [L4den, Phi4, Phi6, Phi8]; ring

/-- **`den(L₅) = 5·Φ₄²·Φ₅·Φ₆·Φ₈·Φ₁₀`** — the cyclotomic tower deepens (`Φ₅`, `Φ₁₀` enter). -/
theorem L5den_cyclotomic (q : R) :
    L5den q = 5 * (Phi4 q) ^ 2 * Phi5 q * Phi6 q * Phi8 q * Phi10 q := by
  simp only [L5den, Phi4, Phi5, Phi6, Phi8, Phi10]; ring

end QOU.Mass.BindingHabiroDenominators
