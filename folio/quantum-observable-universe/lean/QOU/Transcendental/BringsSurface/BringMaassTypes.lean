import QOU.BringsSurface.BringHarmonicTypes
import QOU.BringsSurface.BringReflectionParity

/-!
# Maass (Laplace) harmonics of Bring's surface by `S₅` type — the analytic reading

Bean `qou-u81q`. This module is on the transcendental side of the boundary
(`QOU/Transcendental/`) because its **reading** is analytic: the hyperbolic Laplacian `Δ` on
`L²(B)`. Its Lean content is finite. It never names an eigenvalue: eigenvalues are opaque
labels `λ : Λ`, and no number is computed, fitted or compared.

## The analytic statement (cited, not formalised)

`Δ` on the compact hyperbolic surface `B` has discrete spectrum with finite-dimensional
eigenspaces `E_λ`, and `L²(B)` is their Hilbert sum (spectral theorem for the compact resolvent;
Buser, *Geometry and Spectra of Compact Riemann Surfaces*, ch. 7). Since `S₅` acts by
isometries and commutes with `Δ`, each `E_λ` is a finite-dimensional `S₅`-module, so
`E_λ ≅ ⊕_ρ m_ρ(λ) · ρ`. For `H ≤ S₅`, the `H`-invariant part of `E_λ` is the `λ`-eigenspace of
the orbifold `B/H`, so `d_H(λ) := dim E_λ^H = Σ_ρ dim ρ^H · m_ρ(λ)`.

## What is proved here, from `QOU/BringsSurface/BringHarmonicTypes.lean`

* **Exhaustive classification** (`eigenspace_character_expansion`): the character of every
  `E_λ` is `Σ_ρ m_ρ(λ) χ_ρ` over the seven types, uniquely. There is no other type.
* **Typed spectrum from untyped quotient spectra** (`types_from_quotient_spectra`): the
  type multiplicities `m_ρ(λ)` are integer combinations of the multiplicities of `λ` on the
  seven orbifolds `B/S₃, B/(S₃ × S₂), B/A₄, B/F₂₀, B/S₄, B/A₅, B/S₅`. Two `S₅`-spectra that
  agree on those seven orbifolds agree type by type. Six of the seven are spheres; `B/A₄` is
  a torus, and it is the only one that sees `std ⊗ sgn`.
* In particular the trivial type is the spectrum of the `(2,4,5)` triangle orbifold `B/S₅`,
  and the sign type is `d_{A₅} − d_{S₅}`: the odd part under the deck involution of `B/A₅`
  over `B/S₅`.

## Open (not claimed)

* The values of `λ` and which types occur at the bottom of the spectrum. These are
  transcendental and are not computed anywhere in the corpus. No numerical eigenvalue may
  enter a proof (owner rule).

## Reflection parity (`S₅ × C₂`, from `BringReflectionParity.lean`)

The central orientation-reversing isometry `c` (complex conjugation) acts freely, and each type
splits as `ρ⁺ ⊕ ρ⁻`. For `H ≤ S₅`, the `H × ⟨c⟩`-invariant part of `E_λ` is the `λ`-eigenspace
of the non-orientable orbifold `B/(H × ⟨c⟩)` (possibly with mirror boundary), and `(ρ ⊗ ε)^{H × ⟨c⟩} = ρ^H` for `ε = +`, `0` for
`ε = −`. So (`parity_types_from_quotient_spectra`) the fourteen multiplicities `m_ρ^±(λ)` are
integer combinations of the multiplicities of `λ` on the seven orientable quotients `B/H` and
the seven non-orientable quotients `B/(H × ⟨c⟩)`. The one-dimensional types at the bottom of the
table are boundary problems on the `(2,4,5)` triangle: `triv⁺` Neumann on all sides, `triv⁻`
Dirichlet on all sides, `sgn^±` mixed (`one_dim_boundary_conditions`).

-- Ref: [buser1992] P. Buser, *Geometry and Spectra of Compact Riemann Surfaces* (1992).
-/

namespace QOU.Transcendental.Brings.MaassTypes

open QOU.Brings.S5Char QOU.Brings.HarmonicTypes

/-- The `S₅`-type multiplicities of a spectrum, eigenvalue by eigenvalue. `Λ` is an opaque
index set of eigenvalue labels: no real number is used. -/
structure TypedSpectrum (Λ : Type*) where
  /-- `m_ρ(λ)`: how many copies of the type `ρ` the `λ`-eigenspace contains. -/
  mult : Λ → Fin 7 → ℤ

variable {Λ : Type*}

/-- The character of the `λ`-eigenspace, `Σ_ρ m_ρ(λ) χ_ρ`. -/
def TypedSpectrum.character (D : TypedSpectrum Λ) (l : Λ) (i : Fin 7) : ℚ :=
  combo (fun r => (D.mult l r : ℚ)) i

/-- The multiplicities of `λ` on the seven quotient orbifolds `B/H`,
`H = S₃, S₃ × S₂, A₄, F₂₀, S₄, A₅, S₅`: `d_H(λ) = Σ_ρ dim ρ^H · m_ρ(λ)`. -/
def TypedSpectrum.quotientMult (D : TypedSpectrum Λ) (l : Λ) : Fin 7 → ℤ :=
  quotientMatrix.mulVec (D.mult l)

/-- **Exhaustiveness.** The type multiplicities are read back from the character of the
eigenspace by the class-weighted pairing, and they are the only ones that give that
character. -/
theorem eigenspace_character_expansion (D : TypedSpectrum Λ) (l : Λ) :
    (∀ i, combo (fun r => pairQ (D.character l) r / 120) i = D.character l i) ∧
      ∀ a : Fin 7 → ℚ, (∀ i, combo a i = D.character l i) → a = fun r => (D.mult l r : ℚ) := by
  refine ⟨fun i => class_function_expansion _ i, fun a ha => ?_⟩
  have h := expansion_unique (fun r => a r - D.mult l r) (fun i => by
    have := ha i
    simp only [TypedSpectrum.character, combo] at this ⊢
    linarith)
  funext r
  have := congrFun h r
  simp only [Pi.zero_apply] at this
  linarith

/-- **The typed spectrum is determined by seven untyped quotient spectra, over `ℤ`.**
`m_ρ(λ) = Σ_H R_{ρH} d_H(λ)` with the integer matrix `recoveryMatrix`. -/
theorem types_from_quotient_spectra (D : TypedSpectrum Λ) (l : Λ) :
    recoveryMatrix.mulVec (D.quotientMult l) = D.mult l :=
  recover_types (D.mult l)

/-- Two typed spectra that agree on the seven quotient orbifolds agree type by type. -/
theorem typed_eq_of_quotient_eq (D D' : TypedSpectrum Λ) (l : Λ)
    (h : D.quotientMult l = D'.quotientMult l) : D.mult l = D'.mult l := by
  rw [← types_from_quotient_spectra D l, ← types_from_quotient_spectra D' l, h]

/-! ## Reflection parity -/

/-- The `S₅ × C₂`-type multiplicities: `m_ρ⁺(λ)` and `m_ρ⁻(λ)`. -/
structure ParitySpectrum (Λ : Type*) where
  /-- Reflection-even copies of `ρ` in the `λ`-eigenspace. -/
  plus : Λ → Fin 7 → ℤ
  /-- Reflection-odd copies of `ρ` in the `λ`-eigenspace. -/
  minus : Λ → Fin 7 → ℤ

/-- Multiplicity of `λ` on the orientable quotients `B/H` (the seven recovery subgroups). -/
def ParitySpectrum.orientableMult (D : ParitySpectrum Λ) (l : Λ) : Fin 7 → ℤ :=
  quotientMatrix.mulVec (D.plus l + D.minus l)

/-- Multiplicity of `λ` on the non-orientable quotients `B/(H × ⟨c⟩)`: only even types descend. -/
def ParitySpectrum.nonorientableMult (D : ParitySpectrum Λ) (l : Λ) : Fin 7 → ℤ :=
  quotientMatrix.mulVec (D.plus l)

/-- **The fourteen parity types are determined by fourteen untyped quotient spectra, over `ℤ`.**
`m⁺ = R d^{B/(H×c)}` and `m⁻ = R (d^{B/H} − d^{B/(H×c)})`. -/
theorem parity_types_from_quotient_spectra (D : ParitySpectrum Λ) (l : Λ) :
    recoveryMatrix.mulVec (D.nonorientableMult l) = D.plus l ∧
      recoveryMatrix.mulVec (D.orientableMult l - D.nonorientableMult l) = D.minus l := by
  refine ⟨recover_types _, ?_⟩
  simp only [ParitySpectrum.orientableMult, ParitySpectrum.nonorientableMult, ← Matrix.mulVec_sub,
    add_sub_cancel_left]
  exact recover_types _

end QOU.Transcendental.Brings.MaassTypes
