/-
# The σ↦J geometric carrier on Bring — machine-verified core (brick 4)

Locks the exact facts of the α_EM correspondence attack's brick 4
(`2026-07-18-alpha-em-sigmaJ-geometric-carrier.md`, PR #3942) so the derivation
path is never re-walked:

* The Bring vertex `V = [1 : i : −1 : −i : 0]` lies on Bring's `P⁴` model
  (`H₁ = H₂ = H₃ = 0` — Gaussian-integer arithmetic, exact).
* The order-4 automorphism `U` (coordinate 4-cycle) fixes `V` projectively with
  **multiplier exactly `i`** — `U·V = i·V` componentwise. At a holomorphic fixed
  point the differential acts by the multiplier, and multiplication by `i` on the
  holomorphic tangent line IS the complex structure `J`: `dU|_V = J|_V`.
* The conjugate vertex `conj(V)` is fixed with multiplier `−i`, and complex
  conjugation swaps the two multiplier families — exactly as the bar involution
  swaps the degenerate points `q = ±i` (brick 3) and as conjugation swaps
  `spec(J)`.
* Type-correctness: `i² = −1` (the semisimplified braiding at the democratic
  points squares to `−1`, the defining property of `J`).
* The involution role-swap on the degenerate pair `{i, −i}`: the transpose
  `z ↦ −z⁻¹` (here `−conj z` for units on the circle... encoded exactly as
  `transposeUnit z = -(conj z)` since `z⁻¹ = conj z` for Gaussian units on the
  unit circle) FIXES `i` and `−i`, while `bar = conj` EXCHANGES them.

Reconciliation with the τ-correspondence obstruction (`a6d522e0a`, main): the
channel-swap is a *holomorphic* modular involution and cannot be Hodge
conjugation directly; the anti-holomorphic ingredient enters through the fibre —
which is precisely the role-swap encoded here: on the degenerate stratum the
conjugation doubling is carried by `bar = conj` (anti-holomorphic), and its
geometric realization is coordinate conjugation swapping the vertex families.

Everything is concrete Gaussian-integer arithmetic — Lean core only (no
Mathlib; `ℤ[i]` is modeled as pairs of `Int` with explicit operations; proofs
are `rfl`/`decide`-style computations).

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
--       (Prop 3.9: vertices = permutations of [1:i:−1:−i:0], fixed by order-4;
--        §4.3: the 4-cycle quotient is elliptic with j(5τ₀))
-/
import Init.Data.Int.Basic

namespace QOU.Archimedean.SigmaJGeometricCarrier

/-- Gaussian integers as pairs of `Int` (re, im), Lean-core only. -/
structure GInt where
  re : Int
  im : Int
deriving DecidableEq, Repr

namespace GInt

def add (x y : GInt) : GInt := ⟨x.re + y.re, x.im + y.im⟩
def mul (x y : GInt) : GInt := ⟨x.re * y.re - x.im * y.im, x.re * y.im + x.im * y.re⟩
def neg (x : GInt) : GInt := ⟨-x.re, -x.im⟩
def conj (x : GInt) : GInt := ⟨x.re, -x.im⟩

instance : Add GInt := ⟨add⟩
instance : Mul GInt := ⟨mul⟩
instance : Neg GInt := ⟨neg⟩

def zero : GInt := ⟨0, 0⟩
def one : GInt := ⟨1, 0⟩
def I : GInt := ⟨0, 1⟩

end GInt

open GInt

/-- The Bring vertex `V = (1, i, −1, −i, 0)` (affine representative in the
`P⁴` model). -/
def V : Fin 5 → GInt
  | 0 => one | 1 => I | 2 => neg one | 3 => neg I | 4 => zero

/-- Its complex conjugate `conj(V) = (1, −i, −1, i, 0)`. -/
def W : Fin 5 → GInt
  | 0 => one | 1 => neg I | 2 => neg one | 3 => I | 4 => zero

/-- The order-4 automorphism `U` = coordinate 4-cycle `(x₁x₂x₃x₄)` (fixes `x₅`). -/
def cyc (x : Fin 5 → GInt) : Fin 5 → GInt
  | 0 => x 1 | 1 => x 2 | 2 => x 3 | 3 => x 0 | 4 => x 4

/-- `i² = −1`: the semisimplified braiding at the democratic points is a square
root of `−1` — type-correct with the complex structure `J`. -/
theorem i_sq_eq_neg_one : I * I = neg one := by decide

/-- **G1 (power sums vanish).** `H₁(V) = Σ xᵢ = 0`: the vertex satisfies the
first Bring equation. -/
theorem H1_vanishes :
    V 0 + V 1 + V 2 + V 3 + V 4 = zero := by decide

/-- `H₂(V) = Σ xᵢ² = 0`: the second Bring equation. -/
theorem H2_vanishes :
    V 0 * V 0 + V 1 * V 1 + V 2 * V 2 + V 3 * V 3 + V 4 * V 4 = zero := by decide

/-- `H₃(V) = Σ xᵢ³ = 0`: the third Bring equation — with `H₁, H₂` this places
`V` on Bring's curve exactly. -/
theorem H3_vanishes :
    V 0 * (V 0 * V 0) + V 1 * (V 1 * V 1) + V 2 * (V 2 * V 2)
      + V 3 * (V 3 * V 3) + V 4 * (V 4 * V 4) = zero := by decide

/-- **G2 (multiplier `i`).** `U·V = i·V` componentwise: the order-4 automorphism
fixes `V` projectively with multiplier exactly `i` — the democratic `q`. Hence
`dU|_V = i = J|_V`: the (2,4,5) order-4 rotation realizes `J` at the vertex. -/
theorem cycle_multiplier_i : ∀ k : Fin 5, cyc V k = I * V k := by decide

/-- **G3a (conjugate multiplier `−i`).** `U·conj(V) = (−i)·conj(V)`: the
conjugate vertex carries the other `J`-eigenvalue. -/
theorem conj_cycle_multiplier_neg_i : ∀ k : Fin 5, cyc W k = neg I * W k := by
  decide

/-- **G3b (conjugation swaps the families).** Componentwise complex conjugation
maps `V` to `W` — conjugation exchanges the `+i`- and `−i`-multiplier vertex
families, exactly as bar exchanges the degenerate points `q = ±i` and as
conjugation exchanges `spec(J)`. -/
theorem conj_swaps_families : ∀ k : Fin 5, GInt.conj (V k) = W k := by decide

/-- **Role-swap, bar side:** `conj` (= bar on the unit circle) EXCHANGES the
degenerate pair `{i, −i}`. -/
theorem bar_exchanges_degenerate_pair :
    GInt.conj I = neg I ∧ GInt.conj (neg I) = I := by decide

/-- **Role-swap, transpose side:** the transpose `z ↦ −z⁻¹` (for circle units
`z⁻¹ = conj z`, so `transpose z = −(conj z)`) FIXES each degenerate point. -/
theorem transpose_fixes_degenerate_pair :
    neg (GInt.conj I) = I ∧ neg (GInt.conj (neg I)) = neg I := by decide

end QOU.Archimedean.SigmaJGeometricCarrier
