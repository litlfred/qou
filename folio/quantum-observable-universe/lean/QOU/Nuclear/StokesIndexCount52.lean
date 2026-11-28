import Mathlib.Tactic

/-!
# QOU.QBeta.StokesIndexCount52 — the 5₂ Stokes matrix from the 3d index: the gauge

Bean `qou-vr3q`, the cross-knot companion of `QOU.QBeta.StokesIndexCount41`.

## The chain (GGM, *Peacock patterns*, arXiv 2012.00062)

* eq (Sp-52): `S⁺(x;q) = P · W₋₁(x⁻¹;q⁻¹) · W₋₁(x;q)ᵀ · Q`.
* eq (Wmatrec), `m = -1`: `W₀ = K · W₋₁`, `K = [[0,1,0],[0,0,1],[1,-s,s-q]]`,
  `s = x + x⁻¹ + 1`.
* eq (W52xm), `m = 0`: `𝒲₀ = M₀ · W₀` with GGM's printed `3×3` matrix `M₀(x;q)`.
* eq (eq:WW52): `𝒲₀(x⁻¹;q⁻¹)·𝒲₀(x;q)ᵀ` is the block bilinear, which the probe
  `computations/probes/qbeta_g3_stokes_from_3d_index_52.py` measures (40 digits,
  GGM's own blocks) to equal `E · N · E⁻¹`, `N_{ij} = Ind^rot(j-i, q^{(i+j)/2}x; q)`
  of the triangulation m015, `E = diag((-q^k x²)^k)`.

Hence `S⁺ = L · E·N·E⁻¹ · R` with `L = P·K(x⁻¹;q⁻¹)⁻¹·M₀(x⁻¹;q⁻¹)⁻¹` and
`R = M₀(x;q)⁻ᵀ·K(x;q)⁻ᵀ·Q`.

## What is proved here

* `gaugeL_spec`, `gaugeR_spec` — the closed forms `gaugeL`, `gaugeR` satisfy
  `gaugeL · (M₀(x⁻¹;q⁻¹) · K(x⁻¹;q⁻¹)) = P` and `(K(x;q)ᵀ · M₀(x;q)ᵀ) · gaugeR = Q`
  over any field, away from the zeros of `x, q, 1∓qx, 1-qx², 1-q³x²`.
* `stokes11_eq_index` — for every matrix `N`, `(L·N·R)₁₁ = N₁₁`: the `(1,1)`
  Stokes entry is the zero-flux rotated index (GGM eq S3Dx). `E₁₁ = 1`, so the
  conjugation does not touch it.
* `splus_qzero_factorisation` — the q⁰ matrix the probe obtains from the index,
  `[[1, s+1, 0],[0,1,0],[-s,-s²,1]]`, is GGM's product of three elementary Stokes
  factors (eq S0px52), and at `x = 1` its off-diagonal entries are `4`, `-3`, `-9`.

## What is NOT proved here (inputs, named)

* GGM's conjecture for the 5₂ region matrices (behind eq Sp-52), as for 4₁.
* The block-to-index identity (measured numerically in the probe, not proved).
* ~~The index coefficients themselves, and the q-expansion of `L·E·N·E⁻¹·R`.~~
  At `q⁰`, `x = 1`, for the entries `S⁺₁₂ = 4` and `S⁺₃₁ = -3`, both are now in
  Lean: `QOU.QBeta.FiveTwoIndex.stokes52_12_from_index`, `stokes52_31_from_index`
  (m015 index as a tetrahedron sum, finite support, exact arithmetic). The full
  q-expansion (checks C1–C7) is still the probe's.

No measured value enters. No fit.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 (eq Sp-52, Wmatrec, W52xm, WW52, S0px52)
-/

namespace QOU.QBeta.StokesIndexCount52

variable {F : Type*} [Field F]

/-- A `3×3` matrix as nine entries (row-major). Hand-rolled to keep the import
cone small. -/
@[ext] structure M3 (F : Type*) where
  a₁₁ : F
  a₁₂ : F
  a₁₃ : F
  a₂₁ : F
  a₂₂ : F
  a₂₃ : F
  a₃₁ : F
  a₃₂ : F
  a₃₃ : F

namespace M3

/-- Matrix product. -/
def mul (A B : M3 F) : M3 F :=
  ⟨A.a₁₁ * B.a₁₁ + A.a₁₂ * B.a₂₁ + A.a₁₃ * B.a₃₁,
   A.a₁₁ * B.a₁₂ + A.a₁₂ * B.a₂₂ + A.a₁₃ * B.a₃₂,
   A.a₁₁ * B.a₁₃ + A.a₁₂ * B.a₂₃ + A.a₁₃ * B.a₃₃,
   A.a₂₁ * B.a₁₁ + A.a₂₂ * B.a₂₁ + A.a₂₃ * B.a₃₁,
   A.a₂₁ * B.a₁₂ + A.a₂₂ * B.a₂₂ + A.a₂₃ * B.a₃₂,
   A.a₂₁ * B.a₁₃ + A.a₂₂ * B.a₂₃ + A.a₂₃ * B.a₃₃,
   A.a₃₁ * B.a₁₁ + A.a₃₂ * B.a₂₁ + A.a₃₃ * B.a₃₁,
   A.a₃₁ * B.a₁₂ + A.a₃₂ * B.a₂₂ + A.a₃₃ * B.a₃₂,
   A.a₃₁ * B.a₁₃ + A.a₃₂ * B.a₂₃ + A.a₃₃ * B.a₃₃⟩

/-- Transpose. -/
def tr (A : M3 F) : M3 F :=
  ⟨A.a₁₁, A.a₂₁, A.a₃₁, A.a₁₂, A.a₂₂, A.a₃₂, A.a₁₃, A.a₂₃, A.a₃₃⟩

end M3

open M3

/-- `s(x) = x + x⁻¹ + 1`, GGM eq (sx). -/
def sx (x : F) : F := x + x⁻¹ + 1

/-- GGM eq (Sp-52), left factor. -/
def Pm : M3 F := ⟨0, 1, 0, 0, 1, 1, -1, 0, 0⟩

/-- GGM eq (Sp-52), right factor. -/
def Qm : M3 F := ⟨0, 0, -1, 1, 1, 0, 0, 1, 0⟩

/-- GGM eq (Wmatrec) at `m = -1`. -/
def Km (x q : F) : M3 F := ⟨0, 1, 0, 0, 0, 1, 1, -sx x, sx x - q⟩

/-- GGM eq (W52xm) at `m = 0`: the printed matrix `M₀(x;q)`. -/
def M0m (x q : F) : M3 F :=
  ⟨1, 0, 0,
   -q⁻¹ * (1 - q - q * x ^ 2),
   q⁻¹ * x⁻¹ * (1 - q + x + (-q + q ^ 2) * x ^ 2 - q * x ^ 3),
   -q⁻¹ * x⁻¹ * (1 - q * x ^ 2),
   q⁻¹ ^ 5 * x⁻¹ ^ 3 * (1 + (-q + q ^ 2) * x - (q + q ^ 2 + q ^ 3) * x ^ 2
     + (q ^ 2 + q ^ 3 + q ^ 4 - q ^ 3 - 2 * q ^ 4 - q ^ 5 + q ^ 5) * x ^ 3
     + (q ^ 3 + q ^ 4 + q ^ 5) * x ^ 4
     + (-q ^ 4 - q ^ 5 - q ^ 6 + q ^ 5 + q ^ 6 + q ^ 7) * x ^ 5
     - q ^ 6 * x ^ 6 + q ^ 7 * x ^ 7),
   -q⁻¹ ^ 5 * x⁻¹ ^ 4 * (1 - q * x) * (1 + q * x) * (1 + (1 - q + q ^ 2) * x
     + (-2 * q - q ^ 3 + q ^ 2) * x ^ 2
     + (-q + q ^ 2 - q ^ 3 + q ^ 4 - 2 * q ^ 3 - q ^ 4 - q ^ 5 + q ^ 4 + q ^ 5) * x ^ 3
     + (q ^ 2 + 2 * q ^ 4 - q ^ 3 - q ^ 4 - q ^ 5) * x ^ 4
     + (q ^ 4 - q ^ 5 + q ^ 6) * x ^ 5 - q ^ 5 * x ^ 6),
   q⁻¹ ^ 5 * x⁻¹ ^ 4 * (1 - q * x) * (1 + q * x) * (1 - q * x - (q + q ^ 3) * x ^ 2
     + (q ^ 2 + q ^ 4 - q ^ 3 - q ^ 4) * x ^ 3 + q ^ 4 * x ^ 4 - q ^ 5 * x ^ 5)⟩

/-- Closed form of `L = P·K(x⁻¹;q⁻¹)⁻¹·M₀(x⁻¹;q⁻¹)⁻¹`. First row `(1,0,0)`.
Denominators: `1-q²x²`, `1-qx²`, `1-q³x²` and monomials. -/
def gaugeL (x q : F) : M3 F :=
  ⟨1, 0, 0,
   (q ^ 3 * x ^ 5 + q ^ 3 * x ^ 4 - q ^ 2 * x ^ 3 - q ^ 2 * x ^ 2 - q * x ^ 3 - q * x ^ 2 + 1)
     / (x * (1 - q ^ 2 * x ^ 2) * (1 - q * x ^ 2)),
   -(q ^ 5 * x ^ 5 - q ^ 4 * x ^ 4 - q ^ 4 * x ^ 3 + q ^ 3 * x ^ 2 - q ^ 2 * x ^ 3
       - q ^ 2 * x ^ 2 + q * x - 1)
     / (q * x ^ 2 * (1 - q * x ^ 2) * (1 - q ^ 3 * x ^ 2)),
   -q / ((1 - q ^ 2 * x ^ 2) * (1 - q ^ 3 * x ^ 2)),
   -x * (q ^ 3 * x ^ 4 - q * x ^ 2 + 1) / ((1 - q ^ 2 * x ^ 2) * (1 - q * x ^ 2)),
   -(q ^ 5 * x ^ 5 - 2 * q ^ 4 * x ^ 4 - q ^ 4 * x ^ 3 + q ^ 3 * x ^ 2 - q ^ 2 * x ^ 3
       - q ^ 2 * x ^ 2 + q * x ^ 2 + q * x - 1)
     / (q * x * (1 - q * x ^ 2) * (1 - q ^ 3 * x ^ 2)),
   -q * x / ((1 - q ^ 2 * x ^ 2) * (1 - q ^ 3 * x ^ 2))⟩

/-- Closed form of `R = M₀(x;q)⁻ᵀ·K(x;q)⁻ᵀ·Q`. First column `(1,0,0)ᵀ`. -/
def gaugeR (x q : F) : M3 F :=
  ⟨1,
   (q ^ 3 * x ^ 5 - q ^ 2 * x ^ 3 - q ^ 2 * x ^ 2 - q * x ^ 3 - q * x ^ 2 + x + 1)
     / ((1 - q * x) * (1 + q * x) * (1 - q * x ^ 2)),
   -(q ^ 3 * x ^ 4 - q ^ 2 * x ^ 2 + 1) / (x * (1 - q * x) * (1 + q * x) * (1 - q * x ^ 2)),
   0,
   x * (q ^ 5 * x ^ 5 - q ^ 4 * x ^ 4 + q ^ 3 * x ^ 3 + q ^ 3 * x ^ 2 - q ^ 2 * x ^ 3
       + q * x ^ 2 + q * x - 1) / ((1 - q * x ^ 2) * (1 - q ^ 3 * x ^ 2)),
   (q ^ 5 * x ^ 5 - q ^ 4 * x ^ 4 - q ^ 4 * x ^ 3 + q ^ 3 * x ^ 3 + q ^ 3 * x ^ 2
       - q ^ 2 * x ^ 3 + q * x ^ 2 + 2 * q * x - 1) / ((1 - q * x ^ 2) * (1 - q ^ 3 * x ^ 2)),
   0,
   -q ^ 4 * x ^ 4 / ((1 - q * x) * (1 + q * x) * (1 - q ^ 3 * x ^ 2)),
   -q ^ 4 * x ^ 3 / ((1 - q * x) * (1 + q * x) * (1 - q ^ 3 * x ^ 2))⟩

/-- `M₀(x⁻¹;q⁻¹)·K(x⁻¹;q⁻¹)` in closed form (only monomial denominators). -/
def XLm (x q : F) : M3 F :=
  ⟨0, 1, 0,
   (1 - q * x ^ 2) / x,
   (q * x ^ 3 + q * x ^ 2 - 1) / x,
   1 - q * x ^ 2,
   (q^7*x^7 - q^6*x^6 - q^6*x^5 - q^5*x^5 + q^5*x^4 - q^4*x^5 + q^4*x^3 + q^3*x^3 - q^3*x^2
     + q^2*x^3 - q*x + 1) / (q^2*x^3),
   (-q^7*x^8 - q^7*x^7 + q^6*x^7 + 2*q^6*x^6 + q^6*x^5 + q^5*x^6 + q^5*x^5 - q^5*x^4 + q^4*x^6
     + q^4*x^5 - q^4*x^4 - q^4*x^3 - q^3*x^4 - q^3*x^3 + q^3*x^2 - q^2*x^4 - q^2*x^3 + q*x^2
     + q*x - 1) / (q^2*x^3),
   (q^7*x^7 - 2*q^6*x^6 - q^6*x^5 - q^5*x^5 + q^5*x^4 - q^4*x^5 + q^4*x^4 + q^4*x^3 + q^3*x^4
     + q^3*x^3 - q^3*x^2 + q^2*x^3 - q*x^2 - q*x + 1) / (q^2*x^2)⟩

/-- `K(x;q)ᵀ·M₀(x;q)ᵀ` in closed form (only monomial denominators). -/
def XRm (x q : F) : M3 F :=
  ⟨0,
   (q*x^2 - 1) / (q*x),
   (q^7*x^7 - q^6*x^6 + q^5*x^4 - q^4*x^5 + q^4*x^4 + q^3*x^4 - q^3*x^2 + q^2*x^3 - q^2*x^2
     - q*x^2 - q*x + 1) / (q^5*x^4),
   1,
   (-q*x^3 + x + 1) / (q*x^2),
   (-q^7*x^8 + q^6*x^7 + q^6*x^6 - q^5*x^5 - q^5*x^4 + q^4*x^6 - q^4*x^5 - q^4*x^4 - q^3*x^5
     - q^3*x^4 + q^3*x^3 + q^3*x^2 - q^2*x^4 + q^2*x^3 + q^2*x^2 + q*x^3 + 2*q*x^2 + q*x - x
     - 1) / (q^5*x^5),
   0,
   (q*x^2 - 1) / (q*x^2),
   (q^7*x^7 - q^6*x^6 - q^6*x^5 + q^5*x^4 - q^4*x^5 + q^4*x^4 + q^4*x^3 + q^3*x^4 + q^3*x^3
     - q^3*x^2 + q^2*x^3 - q^2*x^2 - q*x^2 - 2*q*x + 1) / (q^5*x^5)⟩

set_option maxHeartbeats 1000000 in
/-- Step 1 (left): `M₀(x⁻¹;q⁻¹)·K(x⁻¹;q⁻¹) = XLm`. -/
theorem M0K_inv_closed (x q : F) (hx : x ≠ 0) (hq : q ≠ 0) :
    mul (M0m x⁻¹ q⁻¹) (Km x⁻¹ q⁻¹) = XLm x q := by
  ext <;> simp only [mul, M0m, Km, XLm, sx, inv_inv] <;> field_simp <;> ring

set_option maxHeartbeats 1000000 in
/-- Step 1 (right): `K(x;q)ᵀ·M₀(x;q)ᵀ = XRm`. -/
theorem KtM0t_closed (x q : F) (hx : x ≠ 0) (hq : q ≠ 0) :
    mul (tr (Km x q)) (tr (M0m x q)) = XRm x q := by
  ext <;> simp only [mul, tr, M0m, Km, XRm, sx] <;> field_simp <;> ring

set_option maxHeartbeats 1000000 in
/-- Step 2 (left): `gaugeL · XLm = P`. -/
theorem gaugeL_XL (x q : F) (hx : x ≠ 0) (hq : q ≠ 0) (hab : 1 - q ^ 2 * x ^ 2 ≠ 0)
    (hc : 1 - q * x ^ 2 ≠ 0) (hd : 1 - q ^ 3 * x ^ 2 ≠ 0) :
    mul (gaugeL x q) (XLm x q) = Pm := by
  have e1 : 1 - x ^ 2 * q ^ 3 ≠ 0 := by rwa [mul_comm] at hd
  have e2 : 1 - x ^ 2 * q ≠ 0 := by rwa [mul_comm] at hc
  have e3 : 1 - x ^ 2 * q ^ 2 ≠ 0 := by rwa [mul_comm] at hab
  ext <;> simp only [mul, gaugeL, XLm, Pm] <;> field_simp [e1, e2, e3, hab, hc, hd] <;> ring

set_option maxHeartbeats 1000000 in
/-- Step 2 (right): `XRm · gaugeR = Q`. -/
theorem XR_gaugeR (x q : F) (hx : x ≠ 0) (hq : q ≠ 0) (ha : 1 - q * x ≠ 0)
    (hb : 1 + q * x ≠ 0) (hc : 1 - q * x ^ 2 ≠ 0) (hd : 1 - q ^ 3 * x ^ 2 ≠ 0) :
    mul (XRm x q) (gaugeR x q) = Qm := by
  ext <;> simp only [mul, XRm, gaugeR, Qm] <;> field_simp <;> ring

/-- `gaugeL` is the left gauge: `gaugeL · (M₀(x⁻¹;q⁻¹) · K(x⁻¹;q⁻¹)) = P`. -/
theorem gaugeL_spec (x q : F) (hx : x ≠ 0) (hq : q ≠ 0) (ha : 1 - q * x ≠ 0)
    (hb : 1 + q * x ≠ 0) (hc : 1 - q * x ^ 2 ≠ 0) (hd : 1 - q ^ 3 * x ^ 2 ≠ 0) :
    mul (gaugeL x q) (mul (M0m x⁻¹ q⁻¹) (Km x⁻¹ q⁻¹)) = Pm := by
  rw [M0K_inv_closed x q hx hq]
  have hab : 1 - q ^ 2 * x ^ 2 ≠ 0 := by
    have h := mul_ne_zero ha hb
    convert h using 1; ring
  exact gaugeL_XL x q hx hq hab hc hd

/-- `gaugeR` is the right gauge: `(K(x;q)ᵀ · M₀(x;q)ᵀ) · gaugeR = Q`. -/
theorem gaugeR_spec (x q : F) (hx : x ≠ 0) (hq : q ≠ 0) (ha : 1 - q * x ≠ 0)
    (hb : 1 + q * x ≠ 0) (hc : 1 - q * x ^ 2 ≠ 0) (hd : 1 - q ^ 3 * x ^ 2 ≠ 0) :
    mul (mul (tr (Km x q)) (tr (M0m x q))) (gaugeR x q) = Qm := by
  rw [KtM0t_closed x q hx hq]; exact XR_gaugeR x q hx hq ha hb hc hd

/-- **GGM eq (S3Dx) from the gauge shape.** For every matrix `N`, the `(1,1)`
entry of `L·N·R` is `N₁₁`. -/
theorem stokes11_eq_index (x q : F) (N : M3 F) :
    (mul (mul (gaugeL x q) N) (gaugeR x q)).a₁₁ = N.a₁₁ := by
  simp only [mul, gaugeL, gaugeR]; ring

/-- The q⁰ matrix of the probe, `[[1, s+1, 0],[0,1,0],[-s,-s²,1]]`. -/
def splus0 (x : F) : M3 F := ⟨1, sx x + 1, 0, 0, 1, 0, -sx x, -sx x ^ 2, 1⟩

/-- **GGM eq (S0px52).** The q⁰ matrix factors as
`𝔖_{σ₃σ₁}·𝔖_{σ₃σ₂}·𝔖_{σ₁σ₂}`, and at `x = 1` its entries are `4`, `-3`, `-9`. -/
theorem splus_qzero_factorisation (x : F) :
    mul (mul (⟨1, 0, 0, 0, 1, 0, -sx x, 0, 1⟩ : M3 F) ⟨1, 0, 0, 0, 1, 0, 0, sx x, 1⟩)
        ⟨1, sx x + 1, 0, 0, 1, 0, 0, 0, 1⟩ = splus0 x ∧
      (splus0 (1 : F)).a₁₂ = 4 ∧ (splus0 (1 : F)).a₃₁ = -3 ∧ (splus0 (1 : F)).a₃₂ = -9 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · ext <;> simp only [mul, splus0] <;> ring
  all_goals simp only [splus0, sx]; norm_num

end QOU.QBeta.StokesIndexCount52
