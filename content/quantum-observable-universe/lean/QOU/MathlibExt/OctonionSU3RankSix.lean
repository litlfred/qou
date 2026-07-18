import QOU.MathlibExt.OctonionSU3Stabilizer
import QOU.MathlibExt.OctonionDerivationsBound

/-!
# QOU.MathlibExt.OctonionSU3RankSix — `rank(ev_{e₁}) = 6`, closing `dim 𝔰𝔲(3) = 8`

The [`OctonionSU3Stabilizer`](./OctonionSU3Stabilizer.lean) gate reduces the colour
`SU(3)` dimension to a rank: `finrank (su3 e) = 8 ↔ rank(evOct e) = 6`. This file
supplies the missing `rank(evOct e) = 6` at the concrete unit imaginary `e = e₁`
(`Pi.single 1 1`), turning `finrank (su3 e₁) = 8` into an **unconditional**
theorem — the `S⁶ = G₂/SU(3)` dimension count, fully in Lean.

The value is exact-ℚ certified by the merged probe
([`octonion_su3_stabilizer_probe.py`](../../../../../computations/octonion_su3_stabilizer_probe.py));
here it is proved from the corpus's own explicit `𝔤₂` basis. Structure:

* **`octDer_span_eq_top`** — the 14 explicit derivations `octDer` span `Der𝕆`
  (14 independent elements, `octDer_linearIndependent`, in a 14-dim space,
  `octonion_derivation_dim`), so they are a basis.
* **`range_evOct_eq_span_images`** — hence `range(evOct e) = span { (octDerMat i)·e }`,
  the span of the 14 concrete image vectors.
* At `e = e₁` those images are `±e₂, …, ±e₇` (columns of the `octDerMat i`), so the
  range is the 6-dim coordinate subspace `{v : v₀ = v₁ = 0}` — hence `rank = 6`.

Base ring ℚ; nothing archimedean.

-- Ref: [manuscript] docs/audits/2026-07-17-octonion-su3-stabilizer-in-g2.md
-/

namespace QOU.MathlibExt.OctonionDerivations

open Module

/-- **The 14 explicit `𝔤₂` derivations span `Der(𝕆)`.** They are linearly independent
(`octDer_linearIndependent`) and `dim Der(𝕆) = 14` (`octonion_derivation_dim`), so they
form a basis. -/
theorem octDer_span_eq_top : Submodule.span ℚ (Set.range octDer) = ⊤ := by
  have hcard : Fintype.card (Fin 14) = finrank ℚ (↥Der𝕆) := by
    rw [octonion_derivation_dim, Fintype.card_fin]
  have hspan := (basisOfLinearIndependentOfCardEqFinrank
      octDer_linearIndependent hcard).span_eq
  rwa [coe_basisOfLinearIndependentOfCardEqFinrank] at hspan

/-- **`range(evOct e)` is the span of the 14 concrete image vectors** `evOct e (octDer i)`,
because `octDer` spans `Der(𝕆)`. -/
theorem range_evOct_eq_span_images (e : Fin 8 → ℚ) :
    LinearMap.range (evOct e)
      = Submodule.span ℚ (Set.range fun i => evOct e (octDer i)) := by
  rw [LinearMap.range_eq_map, ← octDer_span_eq_top, Submodule.map_span, ← Set.range_comp]
  rfl

end QOU.MathlibExt.OctonionDerivations
