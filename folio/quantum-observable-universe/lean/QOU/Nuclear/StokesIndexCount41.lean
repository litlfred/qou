import Mathlib.Tactic
import QOU.Nuclear.StokesQZeroDTCount

/-!
# QOU.QBeta.StokesIndexCount41 — the 4₁ Stokes constant 3 read from the 3d index

Bean `qou-vr3q` (G3 monodromy keystone). The companion brick
`QOU.QBeta.StokesQZeroDTCount` obtains `S⁺(0) = [[1,3],[0,1]]` from the GGM
Wronskian `W₋₁(0)`. This file supplies the other route: it shows that the
figure-eight Stokes matrix is the 3d-index matrix of Dimofte–Gaiotto–Gukov
conjugated by an explicit gauge, and that at `q → 0` the off-diagonal `3`
is carried by exactly two index coefficients.

## The chain (GGM, *Peacock patterns*, arXiv 2012.00062)

* eq (Sp-41): `S⁺(x;q) = P(x) · W₋₁(x⁻¹;q⁻¹) · W₋₁(x;q)ᵀ · Q(x)`.
* eq (W41rec), `m = -1`: `W₀ = K · W₋₁` with `K(x) = [[0,1],[-x³, x²+x-x³]]`.
* eq (W41xm), `m = 0`: `𝒲₀ = T₀ · W₀` with `T₀(x;q) = [[1,0],[-x⁻¹, x⁻³(1-qx²)]]`.
* eq (WW41) and its footnote: `𝒲₀(x⁻¹;q⁻¹)·𝒲₀(x;q)ᵀ = N(x;q)`, the index matrix
  `N_{ij} = (-q^{1/2})^{j-i} Ind^rot(j-i, q^{(i+j)/2}x; q)`.

Hence `S⁺ = L · N · R` with `L = P·K(x⁻¹)⁻¹·T₀(x⁻¹;q⁻¹)⁻¹` and
`R = T₀(x;q)⁻ᵀ·K(x)⁻ᵀ·Q`.

## What is proved here

* `gaugeL_spec`, `gaugeR_spec` — the closed forms `gaugeL`, `gaugeR` satisfy
  `gaugeL · T₀(x⁻¹;q⁻¹) · K(x⁻¹) = P` and `Kᵀ · T₀ᵀ · gaugeR = Q` over any field,
  for `x, q ≠ 0` and `1 - qx² ≠ 0`. So they are the gauge of the chain above.
* `stokes11_eq_index` — for **every** matrix `N`, `(L·N·R)₁₁ = N₁₁`: the
  `(1,1)` Stokes entry is the zero-flux rotated index itself (GGM eq S3Dx).
* `stokes12_eq` — `(L·N·R)₁₂ = ((1+x-qx³)·N₁₁ + x·N₁₂)/(1-qx²)`.
* `stokes12_qzero_count` — the q⁰ reading. With `[N₁₁]_{q⁰} = [I₄₁(0,0)]_{q⁰}`
  and `[N₁₂]_{q⁰} = -x⁻¹·[I₄₁(1,-2)]_{q^{1/2}}` (the only index coefficients of
  q-degree 0 in those entries), `x · S⁺₁₂(x;0) = (x+x²)·i₀₀ - i₁` with
  `i₀₀ = 1`, `i₁ = -1`, i.e. `S⁺₁₂(x;0) = x⁻¹ + 1 + x`.
* `stokes_constant_three_from_index` — at `x = 1` this is `3`, and it equals the
  `(0,1)` entry of `StokesQZeroDTCount.Splus0`: the two routes agree.

## What is NOT proved here (inputs, named)

* GGM Conjecture `conj.41M` (the region matrices, hence eq Sp-41): conjectural,
  numerically certified by GGM. The W-route brick depends on it too.
* The block factorisation (WW41) of the index: GGM state it for 4₁.
* The two index coefficients `i₀₀ = 1`, `i₁ = -1` and the absence of any other
  q⁰ contribution: computed exactly from the bare DGG eq (4.18) two-tetrahedron
  sum in `computations/probes/qbeta_g3_stokes_from_3d_index_41.py` (witness
  `qbeta-g3-stokes-from-3d-index-41`). **Now proved** in
  `QOU.QBeta.TetIndexDegree` (`stokes41_inputs_proved`,
  `stokes41_three_from_tetrahedra`) from the tetrahedron-index minimal-degree
  bound, with Garoufalidis's triality (1208.1663 Prop prop.S3) as the one cited
  input.

No measured value enters. No fit.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 (eq Sp-41, W41rec, W41xm, WW41, S0x41)
-- Ref: [dimofte-gaiotto-gukov2013] DGG 1112.5179 (eq 4.18, the 4₁ index from two tetrahedra)
-/

namespace QOU.QBeta.StokesIndexCount41

variable {K : Type*} [Field K]

/-- A `2×2` matrix as four entries (row-major). Hand-rolled to keep the
import cone small. -/
@[ext] structure M2 (K : Type*) where
  a : K
  b : K
  c : K
  d : K

namespace M2

/-- Matrix product. -/
def mul (A B : M2 K) : M2 K :=
  ⟨A.a * B.a + A.b * B.c, A.a * B.b + A.b * B.d,
   A.c * B.a + A.d * B.c, A.c * B.b + A.d * B.d⟩

/-- Transpose. -/
def tr (A : M2 K) : M2 K := ⟨A.a, A.c, A.b, A.d⟩

end M2

open M2

/-- GGM eq (Sp-41), left factor `P(x) = [[0,-1],[x⁻¹,-1-x]]`. -/
def Pm (x : K) : M2 K := ⟨0, -1, x⁻¹, -1 - x⟩

/-- GGM eq (Sp-41), right factor `Q(x) = [[0,x],[-1,-1-x⁻¹]]`. -/
def Qm (x : K) : M2 K := ⟨0, x, -1, -1 - x⁻¹⟩

/-- GGM eq (W41rec) at `m = -1`: `W₀ = K·W₋₁`, `K = [[0,1],[-x³, x²+x-x³]]`. -/
def Km (x : K) : M2 K := ⟨0, 1, -x ^ 3, x ^ 2 + x - x ^ 3⟩

/-- GGM eq (W41xm) at `m = 0`: `𝒲₀ = T₀·W₀`, `T₀ = [[1,0],[-x⁻¹, x⁻³(1-qx²)]]`. -/
def T0m (x q : K) : M2 K := ⟨1, 0, -x⁻¹, x⁻¹ ^ 3 * (1 - q * x ^ 2)⟩

/-- Closed form of `L = P·K(x⁻¹)⁻¹·T₀(x⁻¹;q⁻¹)⁻¹`. Its first row is `(-1, 0)`. -/
def gaugeL (x q : K) : M2 K :=
  ⟨-1, 0, -x⁻¹ * (1 - q * x ^ 2 - q * x ^ 3) / (1 - q * x ^ 2), q * x / (1 - q * x ^ 2)⟩

/-- Closed form of `R = T₀(x;q)⁻ᵀ·K(x)⁻ᵀ·Q`. Its first column is `(-1, 0)ᵀ`. -/
def gaugeR (x q : K) : M2 K :=
  ⟨-1, -(1 + x - q * x ^ 3) / (1 - q * x ^ 2), 0, -x / (1 - q * x ^ 2)⟩

/-- `gaugeL` is the left gauge: `gaugeL · T₀(x⁻¹;q⁻¹) · K(x⁻¹) = P(x)`. -/
theorem gaugeL_spec (x q : K) (hx : x ≠ 0) (hq : q ≠ 0) (hu : 1 - q * x ^ 2 ≠ 0) :
    mul (mul (gaugeL x q) (T0m x⁻¹ q⁻¹)) (Km x⁻¹) = Pm x := by
  have hu' : 1 - x ^ 2 * q ≠ 0 := by rwa [mul_comm]
  ext <;> simp only [mul, gaugeL, T0m, Km, Pm] <;> field_simp <;> ring

/-- `gaugeR` is the right gauge: `K(x)ᵀ · T₀(x;q)ᵀ · gaugeR = Q(x)`. -/
theorem gaugeR_spec (x q : K) (hx : x ≠ 0) (hu : 1 - q * x ^ 2 ≠ 0) :
    mul (mul (tr (Km x)) (tr (T0m x q))) (gaugeR x q) = Qm x := by
  have hu' : 1 - x ^ 2 * q ≠ 0 := by rwa [mul_comm]
  ext <;> simp only [mul, tr, gaugeR, T0m, Km, Qm] <;> field_simp <;> ring

/-- **GGM eq (S3Dx) from the gauge shape.** For every index matrix `N`, the
`(1,1)` entry of `L·N·R` is `N₁₁ = Ind^rot(0,x;q)`. -/
theorem stokes11_eq_index (x q : K) (N : M2 K) :
    (mul (mul (gaugeL x q) N) (gaugeR x q)).a = N.a := by
  simp only [mul, gaugeL, gaugeR]; ring

/-- The `(1,2)` Stokes entry in terms of the first index row:
`S⁺₁₂ = ((1+x-qx³)·N₁₁ + x·N₁₂)/(1-qx²)`. -/
theorem stokes12_eq (x q : K) (N : M2 K) :
    (mul (mul (gaugeL x q) N) (gaugeR x q)).b
      = ((1 + x - q * x ^ 3) * N.a + x * N.b) / (1 - q * x ^ 2) := by
  simp only [mul, gaugeL, gaugeR]; ring

/-- At `q = 0` the prefactors of `stokes12_eq` are `1 + x` and `x`. -/
theorem stokes12_prefactors_qzero (x : K) :
    (1 + x - (0 : K) * x ^ 3) / (1 - 0 * x ^ 2) = 1 + x ∧
      x / (1 - (0 : K) * x ^ 2) = x := by
  constructor <;> simp

/-- `[I₄₁(0,0)]_{q⁰}`: the vacuum coefficient of the zero-flux index
(DGG eq 4.18; computed exactly in the probe, input here). -/
def i00 : ℤ := 1

/-- `[I₄₁(1,-2)]_{q^{1/2}}`: the single BPS state at magnetic flux 1, electric
charge −2 that reaches q-degree 0 in `N₁₂ = -q^{1/2}·Ind^rot(1, q^{1/2}x; q)`
(DGG eq 4.18; computed exactly in the probe, input here). -/
def i1 : ℤ := -1

/-- **The q⁰ reading of `S⁺₁₂`.** With `[N₁₁]₀ = i₀₀` and
`x·[N₁₂]₀ = -i₁·x⁻¹·x`, i.e. `x²·[N₁₂]₀ = -i₁`, the polynomial
`x · S⁺₁₂(x;0) = (x + x²)·i₀₀ - i₁` equals `1 + x + x²`:
`S⁺₁₂(x;0) = x⁻¹ + 1 + x` (GGM eq S0x41), in any commutative ring. -/
theorem stokes12_qzero_count {R : Type*} [CommRing R] (x : R) :
    (x + x ^ 2) * (i00 : R) - (i1 : R) = 1 + x + x ^ 2 := by
  simp only [i00, i1]; push_cast; ring

/-- **The Stokes constant 3 as an index count.** At `x = 1`,
`S⁺₁₂(1;0) = 2·i₀₀ - i₁ = 3`: the vacuum counted with gauge weight `1+x = 2`,
plus one flux-1 BPS state. It agrees with the W-route value
`StokesQZeroDTCount.Splus0 0 1 = 3`. -/
theorem stokes_constant_three_from_index :
    2 * i00 - i1 = 3 ∧ 2 * i00 - i1 = QOU.QBeta.StokesQZeroDTCount.Splus0 0 1 := by
  refine ⟨by decide, ?_⟩
  rw [QOU.QBeta.StokesQZeroDTCount.stokes_qzero_offdiagonal]; decide

end QOU.QBeta.StokesIndexCount41
