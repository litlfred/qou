/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# The chirality-summed photon vertex pair is the scalar `-h²` (bean `qou-l4t2`)

Convention D fixes every Hecke generator by `(σ - q)(σ + q⁻¹) = 0`, i.e.
`σ² = h σ + 1` with `h = q - q⁻¹`. Over a coefficient ring `R` acting centrally
on an algebra `A` (here `h` enters through `algebraMap R A`), this module proves:

1. `skein_scalar`: for every such generator, `σ - σ⁻¹ = h` (as a scalar of `A`).
   The two-vertex skein `S = σ - σ⁻¹` is therefore central and position-blind.
2. `four_topology_eq_neg_skein_product`: the signed sum over the four chiral
   2-vertex histories `(ε₁, ε₂)` with bar-Hermitian sign `-ε₁ε₂`, taken at **any**
   two generators `σ`, `τ` (same strand pair or different ones), equals
   `-(σ - σ⁻¹)(τ - τ⁻¹)`; with (1) it is `-h²` (`vertexPair_eq_neg_hsq`).
   This contains the same-position and cross-position identities of
   `EmFermionLoopFourTopology` as the two special cases `τ = σ` and `τ = σ'`.
3. `vertexPair_chain`: a product of `k` chirality-summed vertex pairs, at any
   positions, equals `(-h²)^k`; under any `R`-linear moment `m` with `m 1 = 1`
   its moment is `(-h²)^k` (`moment_vertexPair_chain`). No moment data survive.
4. `skeinChain_two_loop_coeff`: in the skein-chain polarisation
   `Π(α) = H α Σ_{k ≤ K} N_k (-h²α)^k` the `α²` coefficient is `-N₁ h² H`.

Reading (prose, not a theorem): every coefficient the chirality-summed Hecke
skein can contribute lies in `ℤ[h]·H`. A trilogarithm / Bloch-`B₃` value
(`ζ(3) - Li₃(q⁻²)`) cannot come from the vertex algebra; if it is present it has
to come from a two-loop **measure** (period), which the corpus does not yet
define. No measured value and no transcendental constant enter this file.
-/

set_option autoImplicit false

namespace QOU.MassTheory
namespace EmVertexPairScalarChain

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- A convention-D Hecke generator in `A` with skein parameter `h : R`:
an invertible `σ` (two-sided inverse `σinv`) with `σ² = h σ + 1`. -/
structure HeckeGen (h : R) where
  σ : A
  σinv : A
  mul_inv : σ * σinv = 1
  inv_mul : σinv * σ = 1
  quad : σ ^ 2 = algebraMap R A h * σ + 1

/-- **Skein is scalar.** `σ - σ⁻¹ = h` for every convention-D Hecke generator. -/
theorem skein_scalar {h : R} (g : HeckeGen (A := A) h) :
    g.σ - g.σinv = algebraMap R A h := by
  -- `σinv = σinv * σ² - h σinv σ = σ - h`.
  have hc : Commute (algebraMap R A h) g.σinv := Algebra.commutes h g.σinv
  have key : g.σinv * g.σ ^ 2 = g.σinv * (algebraMap R A h * g.σ + 1) := by
    rw [g.quad]
  have lhs : g.σinv * g.σ ^ 2 = g.σ := by
    rw [pow_two, ← mul_assoc, g.inv_mul, one_mul]
  have rhs : g.σinv * (algebraMap R A h * g.σ + 1)
      = algebraMap R A h + g.σinv := by
    rw [mul_add, mul_one, ← mul_assoc, ← hc.eq, mul_assoc, g.inv_mul, mul_one]
  rw [lhs, rhs] at key
  rw [key]; abel

/-- The signed four-topology sum at generators `x`, `y` (inverses `xi`, `yi`):
`Σ_{ε₁,ε₂} (-ε₁ε₂) x^{ε₁} y^{ε₂}`. -/
def fourTopology (x xi y yi : A) : A :=
  x * yi + xi * y - x * y - xi * yi

/-- The four-topology sum is minus the product of the two skeins. Pure ring
identity: no Hecke relation is used. -/
theorem four_topology_eq_neg_skein_product (x xi y yi : A) :
    fourTopology x xi y yi = -((x - xi) * (y - yi)) := by
  unfold fourTopology; noncomm_ring

/-- The chirality-summed photon vertex pair at any two convention-D generators. -/
def vertexPair {h : R} (g g' : HeckeGen (A := A) h) : A :=
  fourTopology g.σ g.σinv g'.σ g'.σinv

/-- **Every vertex pair is `-h²`**, whatever the two positions. -/
theorem vertexPair_eq_neg_hsq {h : R} (g g' : HeckeGen (A := A) h) :
    vertexPair g g' = algebraMap R A (-h ^ 2) := by
  unfold vertexPair
  rw [four_topology_eq_neg_skein_product, skein_scalar, skein_scalar]
  rw [map_neg, map_pow, pow_two]

/-- **Chains.** A product of `k` vertex pairs (any positions) is `(-h²)^k`. -/
theorem vertexPair_chain {h : R} (l : List (HeckeGen (A := A) h × HeckeGen (A := A) h)) :
    (l.map fun p => vertexPair p.1 p.2).prod = algebraMap R A ((-h ^ 2) ^ l.length) := by
  induction l with
  | nil => simp
  | cons p l ih =>
    rw [List.map_cons, List.prod_cons, ih, vertexPair_eq_neg_hsq, List.length_cons,
      ← map_mul]
    congr 1; ring

/-- **Moment independence.** For any `R`-linear moment `m` with `m 1 = 1`, the moment
of a `k`-pair chain is `(-h²)^k`: no single-vertex tadpole data survive. -/
theorem moment_vertexPair_chain {h : R} (m : A →ₗ[R] R) (hm : m 1 = 1)
    (l : List (HeckeGen (A := A) h × HeckeGen (A := A) h)) :
    m (l.map fun p => vertexPair p.1 p.2).prod = (-h ^ 2) ^ l.length := by
  rw [vertexPair_chain, Algebra.algebraMap_eq_smul_one, m.map_smul, hm, smul_eq_mul, mul_one]

/-- **Two-loop coefficient of the skein chain.** With one-loop factor `H`, and
`N₁` placements of a single vertex pair on the fermion loop, the order-`α²` term of
`H α (1 + N₁ (-h²) α + N₂ (-h²)² α² )` is `-N₁ h² H`. Stated as an exact polynomial
identity so the coefficient can be read off. -/
theorem skeinChain_two_loop_coeff (H h α N₁ N₂ : R) :
    H * α * (1 + N₁ * (-h ^ 2) * α + N₂ * (-h ^ 2) ^ 2 * α ^ 2)
      = H * α + (-(N₁ * h ^ 2 * H)) * α ^ 2 + (N₂ * h ^ 4 * H) * α ^ 3 := by
  ring

/-- With one placement (`N₁ = 1`) the skein chain gives exactly the corpus Form B
`α²` term `-H h²`: Form B's two-loop slot is the derived skein value, with no
additional (`c₂`) term from the vertex algebra. -/
theorem formB_is_skein_two_loop (H h α : R) :
    H * α * (1 + 1 * (-h ^ 2) * α) = H * α * (1 - h ^ 2 * α) := by
  ring

end EmVertexPairScalarChain
end QOU.MassTheory
