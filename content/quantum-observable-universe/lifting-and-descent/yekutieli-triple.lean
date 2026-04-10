/-!
# QOU.YekutieliTriple — Yekutieli triple mapping

The Yekutieli triple at level n consists of objects (local
trivialisations), 1-morphisms (transition automorphisms), and
2-morphisms (deformation parameters in the band).

Note: The structure `YekutieliTriple` is already defined in
cosimplicial-crossed-groupoid.lean. This file provides the mapping
version used in the definition block.

## References

- [yekutieli2010] Central Extensions of Gerbes, §3
- [manuscript] §3
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- The Yekutieli triple mapping: assigns a triple (x, g, a) to each
    level n and intersection Uᵢ ∩ Uⱼ of the brane tower.

    LaTeX: `\label{def:yekutieli-triple}` -/
-- Ref: [yekutieli2010] §3, [manuscript] §3
structure YekutieliTripleMapping (M : Type*) where
  /-- Level in the brane tower. -/
  level : ℕ
  /-- Objects: local trivialisations. -/
  objects : M → M
  /-- 1-morphisms: transition automorphisms gᵢⱼ. -/
  transitions : M → ℝ
  /-- 2-morphisms: deformation parameters aᵢⱼ in the band. -/
  deformations : M → ℝ
  /-- The 2-morphisms are invertible (in 𝒪_M×). -/
  deformations_ne_zero : ∀ p : M, deformations p ≠ 0

end QOU
