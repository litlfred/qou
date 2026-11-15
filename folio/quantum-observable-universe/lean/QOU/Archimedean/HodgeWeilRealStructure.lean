/-
# The Weil real structure `c = SWAP ∘ conj` on the explicit H¹(Bring) Hodge model

Bean `qou-l1je` (α_EM B2 τ-lift). Locks the **codomain** algebra of the explicit
Hodge model built and machine-verified in
`computations/alpha_em/hodge_lift_bring_model.py` (10/10 PASS) and written up in
`docs/audits/2026-08-02-hodge-lift-bring-h1-model.md`. That model realizes the
weight-1 Hodge structure `H¹(Bring;ℂ) = H^{1,0} ⊕ H^{0,1}` (each piece 4-dim,
`Jac(Bring) ~ E_{5τ₀}³ × E_{τ₀}`) and its two competing involutions:

| involution | matrix | linearity | swaps Hodge pieces |
|---|---|---|---|
| **Weil real structure `c`** (B2's "Hodge conjugation") | `SWAP ∘ conj` | **antilinear** | yes |
| Galois structure `F = σ*` | `SWAP` | ℂ-linear | yes |

This file proves, **sorry-free in Lean core (no Mathlib)**, the algebraic facts
the Python verified with `numpy` (checks 2a–2e):

* `c_involutive` — `c` is an involution (`c ∘ c = id`): the Weil real structure
  is a genuine real structure. (Python 2a.)
* `F_involutive` — the Galois structure is likewise an involution. (Python 2a.)
* `c_antilinear` / `F_linear` — **the essential distinction**: `c` is antilinear
  (`c(λ·v) = λ̄·c(v)`) while `F` is ℂ-linear (`F(λ·v) = λ·F(v)`). This is why
  `c`, not `F`, is the type-consistent B2 "Hodge conjugation". (Python 2c.)
* `c_ne_F_on_witness` — consequently `c ≠ F` as maps: they disagree at a concrete
  vector. (The antilinear/linear distinction has content.)
* `c_swaps_hodge` — `c` maps `H^{1,0}` into `H^{0,1}`: `c(a,0) = (0, ā)`, the
  Hodge-piece swap. (Python 2b.)
* `c_fixes_real_form` — every vector of the form `(w, w̄)` is `c`-fixed, so
  `Fix(c) ⊇ {(w, w̄) : w ∈ ℂ⁴}` is a real form of `dim_ℝ = 8 = b₁(Bring)`: `c` is
  exactly the `H¹(ℝ)` real structure (Weil). (Python 2d.)

Note (Python 2e, canonicity): `c = SWAP ∘ conj` is written with **no reference to
the moduli τ** — the same map for any moduli — so the involution match
"`ρ ↔ Hodge conjugation`" carries no arithmetic content; the open content of the
lift is the *map* `q ↦ HS`, not the involution. That is why this file is a
**codomain/structural** brick, orthogonal to the open minimal open core (the
period map `Φ`, `PeriodMapWeightReduction.lean`). **No `PeriodMapWeight` /
period-map / MOC instance is fabricated here.**

Gaussian-integer model: `H^{1,0}` and `H^{0,1}` are each modeled as
`Fin 4 → GInt` (`GInt = ℤ[i]` from `SigmaJGeometricCarrier`, a lattice of the
complex 4-space, sufficient for the *algebra* of the real structure). Scalars are
Gaussian integers; `conj` is the ambient complex conjugation restricted to the
lattice. All proofs are `rfl`/`decide`/`funext` computations — Lean core only.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
--       (Bring's Jacobian ~ E⁴, X₀(5) isogeny; the H^{1,0} = std rep of S₅.)
-/
import Init.Data.Int.Basic
import QOU.Archimedean.SigmaJGeometricCarrier

namespace QOU.Archimedean.HodgeWeilRealStructure

open QOU.Archimedean.SigmaJGeometricCarrier
open QOU.Archimedean.SigmaJGeometricCarrier.GInt

/-- One Hodge piece: a 4-dim `GInt`-lattice (the model of `H^{1,0}` or of
`H^{0,1}`, each `≅ ℂ⁴` as the three `E_{5τ₀}` factors plus the `E_{τ₀}` factor). -/
abbrev Piece := Fin 4 → GInt

/-- The 8-dim weight-1 Hodge structure `H¹(Bring) = H^{1,0} ⊕ H^{0,1}`, ordered
basis `[dz₁…dz₄ | dz̄₁…dz̄₄]`. -/
abbrev H1 := Piece × Piece

/-- Componentwise complex conjugation on one Hodge piece. -/
def conjPiece (a : Piece) : Piece := fun k => GInt.conj (a k)

/-- `SWAP` — exchanges `H^{1,0} ↔ H^{0,1}` (the ℂ-linear Galois structure `F`,
and the linear part of the Weil `c`). -/
def SWAP (v : H1) : H1 := (v.2, v.1)

/-- Coordinatewise complex conjugation on the whole `H¹` (the antilinear part). -/
def conjV (v : H1) : H1 := (conjPiece v.1, conjPiece v.2)

/-- **The Weil real structure** `c = SWAP ∘ conj` — the antilinear involution the
B2 statement names "Hodge conjugation". -/
def cWeil (v : H1) : H1 := SWAP (conjV v)

/-- **The Galois real structure** `F = σ* = SWAP` — ℂ-linear, distinguished from
`c` by linearity. -/
def FGal (v : H1) : H1 := SWAP v

/-- Scalar multiplication by a Gaussian integer (the lattice `ℂ`-action). -/
def smul (l : GInt) (v : H1) : H1 := (fun k => l * v.1 k, fun k => l * v.2 k)

/-- Complex conjugation on `GInt` is an involution: `z̄̄ = z`. -/
theorem conj_conj (z : GInt) : GInt.conj (GInt.conj z) = z := by
  cases z; simp [GInt.conj]

/-- Complex conjugation is multiplicative: `conj(x·y) = x̄·ȳ`. The one nonlinear
`ℤ`-identity behind antilinearity; proved from core `Int` lemmas (no `ring`). -/
theorem conj_mul (x y : GInt) : GInt.conj (x * y) = GInt.conj x * GInt.conj y := by
  cases x; cases y
  show GInt.conj (GInt.mul _ _) = GInt.mul (GInt.conj _) (GInt.conj _)
  simp only [GInt.mul, GInt.conj, Int.mul_neg, Int.neg_mul, Int.neg_neg, Int.neg_add]

/-- Piecewise conjugation is an involution (lifts `conj_conj`). -/
theorem conjPiece_conjPiece (a : Piece) : conjPiece (conjPiece a) = a := by
  funext k; exact conj_conj _

/-- Piecewise conjugation fixes the zero piece: `0̄ = 0`. -/
theorem conjPiece_zero : conjPiece (fun _ : Fin 4 => GInt.zero) = (fun _ => GInt.zero) := by
  funext k; show GInt.conj GInt.zero = GInt.zero; decide

/-- **`c` is an involution** — `c ∘ c = id`. The Weil `SWAP ∘ conj` is a genuine
(real) structure on `H¹`. Uses `conj_conj`; not a `rfl`. (Python check 2a.) -/
theorem c_involutive (v : H1) : cWeil (cWeil v) = v := by
  obtain ⟨a, b⟩ := v
  simp only [cWeil, SWAP, conjV, conjPiece_conjPiece]

/-- **`F` is an involution** — `F ∘ F = id`. `SWAP²  = id`. (Python 2a.) -/
theorem F_involutive (v : H1) : FGal (FGal v) = v := by
  obtain ⟨a, b⟩ := v; rfl

/-- **`c` is antilinear** — `c(λ·v) = λ̄·c(v)`. This is what makes `c` the Hodge
conjugation (an anti-linear involution), the type-consistent B2 object. Uses
`conj_mul`. (Python check 2c.) -/
theorem c_antilinear (l : GInt) (v : H1) :
    cWeil (smul l v) = smul (GInt.conj l) (cWeil v) := by
  obtain ⟨a, b⟩ := v
  simp only [cWeil, smul, SWAP, conjV, conjPiece, Prod.mk.injEq]
  refine ⟨?_, ?_⟩ <;> (funext k; exact conj_mul _ _)

/-- **`F` is ℂ-linear** — `F(λ·v) = λ·F(v)`. The Galois structure is linear,
distinguishing it from `c`. (Python check 2c.) -/
theorem F_linear (l : GInt) (v : H1) :
    FGal (smul l v) = smul l (FGal v) := by
  obtain ⟨a, b⟩ := v; rfl

/-- A concrete test vector with an imaginary entry in the `H^{0,1}` slot. -/
def v0 : H1 := (fun _ => GInt.zero, fun _ => GInt.I)

/-- **`c ≠ F`** as maps: they disagree at `v0`. `(F v0)₁(0) = i` (linear: just
swap) while `(c v0)₁(0) = ī = −i` (antilinear: swap then conjugate). The
antilinear/linear distinction therefore has content — the Weil real structure is
NOT the ℂ-linear Galois structure. -/
theorem c_ne_F_on_witness : (cWeil v0).1 0 ≠ (FGal v0).1 0 := by decide

/-- **`c` swaps the Hodge pieces** — `c(a, 0) = (0, ā)`: it maps `H^{1,0}`
(second slot zero) into `H^{0,1}` (first slot zero). (Python check 2b.) -/
theorem c_swaps_hodge (a : Piece) :
    cWeil (a, fun _ => GInt.zero) = (fun _ => GInt.zero, conjPiece a) := by
  simp only [cWeil, SWAP, conjV, conjPiece_zero]

/-- **`Fix(c)` is a real form** — every vector of the form `(w, w̄)` is `c`-fixed.
Ranging over `w ∈ GInt⁴` (the lattice model of `ℂ⁴`) this exhibits a real
subspace of `dim_ℝ = 8 = b₁(Bring)`: `c` is exactly the `H¹(ℝ)` Weil real
structure. (Python check 2d.) -/
theorem c_fixes_real_form (w : Piece) :
    cWeil (w, conjPiece w) = (w, conjPiece w) := by
  simp only [cWeil, SWAP, conjV, conjPiece_conjPiece]

end QOU.Archimedean.HodgeWeilRealStructure
