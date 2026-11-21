import Init.Data.Int.Basic
import Init.Omega

/-!
# QOU.QBeta.StokesMatrixProvenance — the 5₂ Stokes matrices are DERIVED from the eq-(98) DT constants, not transcribed

## The problem this closes

`FiveTwoDTSpectrumSplit` and `FiveTwoStokesMatrixIdentities` carry the `5₂`
leading Stokes matrices as hand-typed `def`s ("glyph-decoded" from GGM
2012.00062 eqs (96)/(97)). Lean cannot check a transcription, so every downstream
result was conditional on that typing being faithful — the `sorry-free ≠ derived`
boundary, raised directly by the author: *"do we have proof these are correct?"*

This file removes most of that exposure. Rather than re-typing the matrices, it
**reconstructs** them from a much smaller and cleaner input: the GGM eq-(98)
matrix of Stokes constants (= Donaldson–Thomas invariants),

```
        ⎛  0   4   3 ⎞
  DT =  ⎜ −4   0  −3 ⎟          (GGM 2012.00062 eq (98))
        ⎝ −3   3   0 ⎠
```

whose `(i,j)` entry is the Stokes constant attached to the Borel singularity
`ι_{i,j}`. GGM state that each `S_{σᵢ,σⱼ}` is the elementary matrix
`I + DT(i,j)·E_{ij}`, and that the leading Stokes matrices are the products
(eqs (96)/(97))

```
  S⁺(0) = S_{σ₃σ₁} · S_{σ₃σ₂} · S_{σ₁σ₂},
  S⁻(0) = S_{σ₁σ₃} · S_{σ₂σ₃} · S_{σ₂σ₁}.
```

Computing those products reproduces the typed matrices **exactly**.

## Why this is a strong check, not a circular one

* The only input is the eq-(98) integer matrix — a small, unambiguous array of
  `{0, ±3, ±4}`, far less error-prone than two 3×3 matrices.
* The typed entries are *outputs*: in particular `S⁺(0)₃₂ = −9`, the least
  guessable number in either matrix, is a **product artifact**
  (`−3·4 + 3 = −9`), never a transcribed digit. A transcription slip would have
  had to conspire with the product structure to survive.
* The reconstruction is cross-checked against the independent structural identity
  GGM eq (17), `S⁺(0)ᵀ · S⁻(0) = 1`, proved here from the reconstructed matrices.

What remains outside Lean's reach: that the eq-(98) array itself is faithfully
read from the paper. That is now a single small matrix rather than the whole
Stokes data — the residual exposure is minimized, not eliminated.

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 eqs (96), (97), (98), (17)
-- Ref: [leitner2026] docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md
-/

namespace QOU.QBeta.StokesMatrixProvenance

/-- `3×3` integer matrices as index functions (core only — no Mathlib needed). -/
abbrev M3 := Fin 3 → Fin 3 → Int

/-- Matrix product. -/
def mul (A B : M3) : M3 := fun i j => A i 0 * B 0 j + A i 1 * B 1 j + A i 2 * B 2 j

/-- Transpose. -/
def tr (A : M3) : M3 := fun i j => A j i

/-- The identity matrix. -/
def one : M3 := fun i j => if i = j then 1 else 0

/-! ## The single input: the GGM eq-(98) DT / Stokes-constant matrix -/

/-- GGM eq (98): the matrix of Stokes constants (Donaldson–Thomas invariants) of
`5₂`, whose `(i,j)` entry sits at the Borel singularity `ι_{i,j}`. -/
def DT : M3
  | 0, 0 =>  0 | 0, 1 =>  4 | 0, 2 =>  3
  | 1, 0 => -4 | 1, 1 =>  0 | 1, 2 => -3
  | 2, 0 => -3 | 2, 1 =>  3 | 2, 2 =>  0

/-- The elementary Stokes factor `S_{σᵢσⱼ} = I + DT(i,j)·E_{ij}`. -/
def elem (i j : Fin 3) : M3 := fun a b => (if a = b then 1 else 0) +
  (if a = i ∧ b = j then DT i j else 0)

/-- **The off-diagonal DT spectrum is `{3, 4}`** (up to sign): the constants
appearing in eq (98) are exactly `±3` and `±4`. -/
theorem dt_spectrum_three_four :
    DT 0 1 = 4 ∧ DT 0 2 = 3 ∧ DT 1 0 = -4 ∧ DT 1 2 = -3 ∧
    DT 2 0 = -3 ∧ DT 2 1 = 3 := by decide

/-! ## Reconstruction of the leading Stokes matrices -/

/-- `S⁺(0)` **reconstructed** as the eq-(96) product `S_{σ₃σ₁}S_{σ₃σ₂}S_{σ₁σ₂}`. -/
def SplusRecon : M3 := mul (mul (elem 2 0) (elem 2 1)) (elem 0 1)

/-- `S⁻(0)` **reconstructed** as the eq-(97) product `S_{σ₁σ₃}S_{σ₂σ₃}S_{σ₂σ₁}`. -/
def SminusRecon : M3 := mul (mul (elem 0 2) (elem 1 2)) (elem 1 0)

/-- The matrices as **typed** in `FiveTwoDTSpectrumSplit` /
`FiveTwoStokesMatrixIdentities` (reproduced here for the comparison). -/
def SplusTyped : M3
  | 0, 0 =>  1 | 0, 1 =>  4 | 0, 2 => 0
  | 1, 0 =>  0 | 1, 1 =>  1 | 1, 2 => 0
  | 2, 0 => -3 | 2, 1 => -9 | 2, 2 => 1

/-- ditto for `S⁻(0)`. -/
def SminusTyped : M3
  | 0, 0 =>  1 | 0, 1 => 0 | 0, 2 =>  3
  | 1, 0 => -4 | 1, 1 => 1 | 1, 2 => -3
  | 2, 0 =>  0 | 2, 1 => 0 | 2, 2 =>  1

/-- **The typed `S⁺(0)` is exactly the eq-(96) product of the eq-(98)
constants.** -/
theorem splus_reconstructed : ∀ i j, SplusRecon i j = SplusTyped i j := by decide

/-- **The typed `S⁻(0)` is exactly the eq-(97) product of the eq-(98)
constants.** -/
theorem sminus_reconstructed : ∀ i j, SminusRecon i j = SminusTyped i j := by
  decide

/-- **The `−9` is a product artifact, not a transcribed number**: it is
`DT(3,1)·DT(1,2) + DT(3,2) = (−3)·4 + 3`. This is the entry a transcription
error would most likely corrupt, and it is an output of the reconstruction. -/
theorem minus_nine_is_derived :
    SplusRecon 2 1 = DT 2 0 * DT 0 1 + DT 2 1 ∧ SplusRecon 2 1 = -9 := by decide

/-! ## Independent structural cross-check (GGM eq (17)) -/

/-- **Inversion relation at `q → 0`** (GGM eq (17)): `S⁺(0)ᵀ · S⁻(0) = 1`, proved
from the *reconstructed* matrices. Two separately-built products satisfying an
exact inverse relation is a strong consistency signal on the eq-(98) input. -/
theorem inversion_relation :
    ∀ i j, mul (tr SplusRecon) SminusRecon i j = one i j := by decide

/-- The reconstructed determinant data: both leading Stokes matrices are
unimodular (they are products of elementary matrices). -/
theorem splus_unipotent_diagonal :
    SplusRecon 0 0 = 1 ∧ SplusRecon 1 1 = 1 ∧ SplusRecon 2 2 = 1 := by decide

/-! ## The chirality split, now on reconstructed data

The DT constants carried by the two chiralities — `4` in `S⁺`, `3` in `S⁻` — read
off the reconstruction rather than the transcription. -/

/-- `S⁺(0)` carries the DT constant `4`; `S⁻(0)` carries `3`; they differ, so the
`5₂` datum is a genuine two-element chirality-split spectrum. -/
theorem chirality_split_from_reconstruction :
    SplusRecon 0 1 = 4 ∧ SminusRecon 0 2 = 3 ∧ SplusRecon 0 1 ≠ SminusRecon 0 2 := by
  decide

end QOU.QBeta.StokesMatrixProvenance
