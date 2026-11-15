import Mathlib.Tactic

/-!
# QOU.QBeta.StokesQZeroDTCount — the q→0 Stokes/DT constant of 4₁ is exactly 3

This is the **base-case (q→0) brick** of the G3 Stokes keystone (bean `qou-ujmw`):
it proves, by a *decidable integer-matrix computation*, that the figure-eight
Stokes constant `A_ω` read at the semiclassical limit `q → 0` is the integer **3**
— the Donaldson–Thomas / rotated-3d-index invariant of `T[4₁]`, **not** an
assumed value.

## What is proved here (and what is NOT)

The Garoufalidis–Gu–Mariño ("Peacock patterns…", 2012.00062) Stokes matrix of the
figure-eight knot is the eq-(59a) sandwich `S⁺ = ±½·A·W₋₁·B·W₋₁ᵀ·C`, where
`W₋₁(q)` is the fundamental-solution matrix of the GGM q-difference equation
(Theorem 9) and `A,B,C` are small integer matrices whose glyph-verified magnitudes
are `|A|=[[0,1],[1,1]]`, `|B|=[[0,1],[1,0]]`, `|C|=[[0,1],[1,2]]`. At the
semiclassical limit the q-series `W₋₁(q)` collapses to the **exact integer matrix**
`W₋₁(0) = [[0,-2],[1,1]]` (its determinant `2` is GGM Theorem 9 at q→0,
`det W_m = 2`), and the whole sandwich evaluates to `-2·S⁺(0)` with
`S⁺(0) = [[1,3],[0,1]]` (GGM eq 60). The off-diagonal entry — the q→0 Stokes /
DT constant — is exactly **3**.

* `detW0` — `det W₋₁(0) = 2`. Falsifiable base of GGM Theorem 9 at q→0.
* `ggm_sandwich_qzero` — every entry of the eq-(59a) sandwich
  `A·W₋₁·B·W₋₁ᵀ·C` at q→0 equals `-2·S⁺(0)` with `S⁺(0)=[[1,3],[0,1]]`.
* `sandwich_offdiagonal_qzero` — its `(0,1)` entry is `-6 = (-2)·3`; with the
  `-½` normalization the Stokes/DT constant is `3`.

**Scope (honest, anti-laundering).** This brick *verifies GGM eq 60 as a
decidable computation from the DT building blocks* — it reduces "`A_ω = 3` at
q→0" to the single concrete input `W₋₁(0) = [[0,-2],[1,1]]` (a certified q→0
evaluation of the GGM/DGG q-series, `computations/probes/qbeta_g3_ggm_stokes_41.py`,
`det = 2`). It does **NOT** derive `3` from the 13 QOU categorical drivers — that
internal derivation stays open (`qou-qnnq`; `docs/audits/2026-08-01-3bp8-…` §4).
It also does not carry the q-dependent extension: that the full q-series symmetry
constant `(S₁₂+S₂₁)/S₁₁ = 3` holds at *every* q is the companion conditional lemma
`QOU.QBeta.StokesSymmetryConstant.symmetryConstant_const`; this file supplies its
unconditional q→0 base value. The value→observable normalization
(`Im 𝔙_q → N_odd`, magnitude `A′ ≈ 2.37`) is separately open (`qou-2cvs`).

Matrices are hand-rolled `Fin 2 → Fin 2 → ℤ` (elementary, `decide`-checkable);
`Mathlib.Data.Matrix.Notation` is deliberately avoided so the file verifies on the
minimal restored olean set.

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (eq 59a sandwich, eq 60 S⁺(0), Thm 9 det W_m = 2)
-- Ref: [leitner2026] docs/audits/2026-08-01-ujmw-aomega-dt-index-derivation.md
-/

namespace QOU.QBeta.StokesQZeroDTCount

/-- A `2×2` integer matrix as an explicit function of its indices. -/
abbrev M2 := Fin 2 → Fin 2 → ℤ

/-- Explicit `2×2` integer-matrix product (no Mathlib `Matrix` dependency). -/
def mul (A B : M2) : M2 := fun i j => A i 0 * B 0 j + A i 1 * B 1 j

/-- Explicit `2×2` transpose. -/
def tr (A : M2) : M2 := fun i j => A j i

/-- Explicit `2×2` integer determinant. -/
def det (A : M2) : ℤ := A 0 0 * A 1 1 - A 0 1 * A 1 0

/-- The q→0 evaluation of the GGM fundamental-solution matrix `W₋₁` for 4₁,
computed exactly from the integer q-series `G⁰_m, G¹_m` (GGM eqs 51a/51b):
`G⁰₋₁(0)=0, G¹₋₁(0)=-2, G⁰₀(0)=1, G¹₀(0)=1`. -/
def W0 : M2 := ![![0, -2], ![1, 1]]

/-- Glyph-verified GGM eq-(59a) integer matrix `A` (magnitude `[[0,1],[1,1]]`). -/
def Amat : M2 := ![![0, 1], ![1, 1]]

/-- Glyph-verified GGM eq-(59a) integer matrix `B` (the swap, `[[0,1],[1,0]]`). -/
def Bmat : M2 := ![![0, 1], ![1, 0]]

/-- Glyph-verified GGM eq-(59a) integer matrix `C` (magnitude `[[0,1],[1,2]]`,
sign row fixed by the q→0 filter). -/
def Cmat : M2 := ![![0, 1], ![-1, -2]]

/-- The extracted q→0 Stokes matrix, GGM eq 60: `S⁺(0) = [[1,3],[0,1]]`. -/
def Splus0 : M2 := ![![1, 3], ![0, 1]]

/-- The eq-(59a) sandwich `A·W₋₁·B·W₋₁ᵀ·C` at q→0. -/
def sandwich : M2 := mul (mul (mul (mul Amat W0) Bmat) (tr W0)) Cmat

/-- **GGM Theorem 9 at q→0.** `det W₋₁(0) = 2`. -/
theorem detW0 : det W0 = 2 := by decide

/-- **The q→0 GGM sandwich yields the integer 3.** Every entry of the eq-(59a)
product `A·W₋₁·B·W₋₁ᵀ·C` at q→0 equals `-2·S⁺(0)` with `S⁺(0)=[[1,3],[0,1]]`.
So `S⁺(0) = -½·(A·W₋₁(0)·B·W₋₁(0)ᵀ·C)`, and its off-diagonal — the DT/Stokes
constant `A_ω` at the semiclassical limit — is exactly `3`. Decidable integer
arithmetic; not an assumption. -/
theorem ggm_sandwich_qzero : ∀ i j, sandwich i j = (-2 : ℤ) * Splus0 i j := by
  decide

/-- **The q→0 Stokes/DT constant is `3`.** Reading the extracted `S⁺(0)`, its
`(0,1)` entry (the figure-eight DT invariant governing the geometric Borel
singularity at `ω = Vol(4₁)/π`) is `3`. -/
theorem stokes_qzero_offdiagonal : Splus0 0 1 = 3 := by decide

/-- The q→0 sandwich `(0,1)` entry is `-6`; combined with the `-½` normalization
this is the constant `3`. Records the numeric link. -/
theorem sandwich_offdiagonal_qzero : sandwich 0 1 = -6 := by decide

end QOU.QBeta.StokesQZeroDTCount
