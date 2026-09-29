import Mathlib.LinearAlgebra.Dimension.RankNullity
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.Tactic

/-!
# QOU.MathlibExt.DerivationRankNullity

Rank–nullity reduction for the derivation space of a finite-dimensional
(not necessarily associative) algebra, targeting the octonion case
`dim Der(𝕆) = 14` (the compact `G₂`).

For a bilinear multiplication `m` on a finite-dimensional space `V`, the
**Leibniz-defect operator**

  `L : End(V) →ₗ Bil(V, V; V)`, `L(D)(x, y) = D(m x y) − m (D x) y − m x (D y)`

has `ker L = Der(V, m)` by definition of a derivation. Rank–nullity then gives

  `dim Der(V, m) + rank L = (dim V)²`,

so for an 8-dimensional algebra (`dim End = 64`, proved here as `finrank_end`)
the `G₂` dimension count reduces to a rank computation:

  `dim Der = 14 ⟺ rank L = 50`.

## What this file does NOT prove

`dim Der(𝕆) = 14` itself. That requires the octonion multiplication and a
rank-50 witness for its defect operator (the explicit-basis route); this file
supplies the exact interface such a witness must plug into, for **any**
8-dimensional algebra. No claim is made that every 8-dimensional algebra has a
14-dimensional derivation space (false — e.g. the zero multiplication has
`Der = End`, rank `L = 0`).

## Wall / base-ring note (§7c)

Everything here is linear algebra over a generic field `K` — no ordering, no
`Real.*`, nothing archimedean. The octonion instantiation over `ℝ` (where the
compact `G₂` lives) specializes `K := ℝ` downstream; the reduction itself is
field-agnostic.
-/

namespace QOU.MathlibExt.DerivationRankNullity

open Module

variable {K : Type*} [Field K]
variable {V : Type*} [AddCommGroup V] [Module K V] [FiniteDimensional K V]

/-- The **Leibniz-defect operator** of a bilinear multiplication `m` on `V`:
`leibnizDefect m D = (x, y) ↦ D (m x y) − m (D x) y − m x (D y)`, as a linear
map from endomorphisms to bilinear maps. Its kernel is the derivation space
`Der(V, m)`. -/
def leibnizDefect (m : V →ₗ[K] V →ₗ[K] V) :
    (V →ₗ[K] V) →ₗ[K] (V →ₗ[K] V →ₗ[K] V) where
  toFun D := m.compr₂ D - m.comp D - m.compl₂ D
  map_add' D₁ D₂ := by
    ext x y
    simp only [LinearMap.compr₂_apply, LinearMap.comp_apply, LinearMap.compl₂_apply,
      LinearMap.sub_apply, LinearMap.add_apply, map_add]
    abel
  map_smul' c D := by
    ext x y
    simp only [LinearMap.compr₂_apply, LinearMap.comp_apply, LinearMap.compl₂_apply,
      LinearMap.sub_apply, LinearMap.smul_apply, map_smul, RingHom.id_apply, smul_sub]

omit [FiniteDimensional K V] in
@[simp] theorem leibnizDefect_apply (m : V →ₗ[K] V →ₗ[K] V) (D : V →ₗ[K] V) (x y : V) :
    leibnizDefect m D x y = D (m x y) - m (D x) y - m x (D y) := rfl

omit [FiniteDimensional K V] in
/-- Membership in `ker (leibnizDefect m)` is exactly the Leibniz rule: the
kernel is the derivation space `Der(V, m)`. -/
theorem mem_ker_leibnizDefect_iff {m : V →ₗ[K] V →ₗ[K] V} {D : V →ₗ[K] V} :
    D ∈ LinearMap.ker (leibnizDefect m) ↔
      ∀ x y : V, D (m x y) = m (D x) y + m x (D y) := by
  simp only [LinearMap.mem_ker, LinearMap.ext_iff, leibnizDefect_apply,
    LinearMap.zero_apply, sub_sub, sub_eq_zero]

/-- **Rank–nullity for the derivation space** of any finite-dimensional
algebra: `dim Der(V, m) + rank (leibnizDefect m) = (dim V)²`. -/
theorem finrank_ker_add_finrank_range (m : V →ₗ[K] V →ₗ[K] V) :
    finrank K (LinearMap.ker (leibnizDefect m))
      + finrank K (LinearMap.range (leibnizDefect m))
      = finrank K V * finrank K V := by
  have h := (leibnizDefect m).finrank_range_add_finrank_ker
  rw [Module.finrank_linearMap] at h
  omega

section EightDimensional

variable (h8 : finrank K V = 8)
include h8

/-- The endomorphism space of an 8-dimensional space is 64-dimensional. -/
theorem finrank_end : finrank K (V →ₗ[K] V) = 64 := by
  rw [Module.finrank_linearMap, h8]

/-- **The octonion-shaped rank–nullity identity**: for any bilinear
multiplication on an 8-dimensional space, `dim Der + rank L = 64`. -/
theorem finrank_ker_add_finrank_range_eq_64 (m : V →ₗ[K] V →ₗ[K] V) :
    finrank K (LinearMap.ker (leibnizDefect m))
      + finrank K (LinearMap.range (leibnizDefect m)) = 64 := by
  have h := finrank_ker_add_finrank_range m
  rw [h8] at h
  omega

/-- **The `G₂` dimension gate.** For an 8-dimensional algebra,
`dim Der = 14 ⟺ rank (leibnizDefect) = 50`: the `dim Der(𝕆) = 14` target is
equivalent to a rank-50 computation on the 64-dimensional endomorphism
space. This is the interface an explicit-basis rank witness plugs into. -/
theorem finrank_ker_eq_14_iff_finrank_range_eq_50 (m : V →ₗ[K] V →ₗ[K] V) :
    finrank K (LinearMap.ker (leibnizDefect m)) = 14 ↔
      finrank K (LinearMap.range (leibnizDefect m)) = 50 := by
  have h := finrank_ker_add_finrank_range_eq_64 h8 m
  omega

end EightDimensional

section OctCarrier

/-- The 8-dimensional coordinate carrier for an octonion algebra over `K`
(the multiplication is a parameter of the theorems above, not fixed here). -/
abbrev OctCarrier (K : Type*) := Fin 8 → K

variable (K)

theorem finrank_octCarrier : finrank K (OctCarrier K) = 8 := by
  simp [OctCarrier]

/-- `End(OctCarrier)` is 64-dimensional — the concrete instantiation the
octonion defect operator lives in. -/
theorem finrank_end_octCarrier :
    finrank K (OctCarrier K →ₗ[K] OctCarrier K) = 64 :=
  finrank_end (finrank_octCarrier K)

variable {K}

/-- `dim Der + rank L = 64` on the concrete carrier, for any candidate
octonion multiplication `m`. -/
theorem octCarrier_finrank_ker_add_finrank_range
    (m : OctCarrier K →ₗ[K] OctCarrier K →ₗ[K] OctCarrier K) :
    finrank K (LinearMap.ker (leibnizDefect m))
      + finrank K (LinearMap.range (leibnizDefect m)) = 64 :=
  finrank_ker_add_finrank_range_eq_64 (finrank_octCarrier K) m

/-- The `G₂` gate on the concrete carrier: `dim Der = 14 ⟺ rank L = 50`. -/
theorem octCarrier_finrank_ker_eq_14_iff
    (m : OctCarrier K →ₗ[K] OctCarrier K →ₗ[K] OctCarrier K) :
    finrank K (LinearMap.ker (leibnizDefect m)) = 14 ↔
      finrank K (LinearMap.range (leibnizDefect m)) = 50 :=
  finrank_ker_eq_14_iff_finrank_range_eq_50 (finrank_octCarrier K) m

end OctCarrier

end QOU.MathlibExt.DerivationRankNullity
