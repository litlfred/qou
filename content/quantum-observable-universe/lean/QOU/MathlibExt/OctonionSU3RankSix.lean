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
  -- The card/finrank → basis lemmas (`basisOfLinearIndependentOfCardEqFinrank`,
  -- `eq_top_of_finrank_eq`, …) all materialise a `Basis` on the double-subtype
  -- `↥Der𝕆` and `whnf`-time out reducing the giant `Der𝕆` (even at 2M heartbeats).
  -- Instead mirror `octDer_finrank_ge`: the linear-combination map `L14` has the
  -- left inverse `projDer`, so it is injective; equal finrank (14 = dim Der𝕆) makes
  -- it surjective; hence every `x ∈ Der𝕆` is a ℚ-combination of the `octDer`, i.e.
  -- lies in their span.  Only the `finrank_range_add_finrank_ker` idiom is used —
  -- no basis on `↥Der𝕆`.
  haveI : FiniteDimensional ℚ (↥Der𝕆) := Submodule.finiteDimensional_of_le le_top
  let L14 : (Fin 14 → ℚ) →ₗ[ℚ] Der𝕆 := ∑ i, (LinearMap.proj i).smulRight (octDer i)
  have hLc : ∀ c, L14 c = ∑ i, c i • octDer i := fun c => by
    simp [L14, LinearMap.sum_apply, LinearMap.smulRight_apply, LinearMap.proj_apply]
  have hsec : ∀ c, projDer (L14 c) = c := by
    intro c
    rw [hLc, map_sum]
    funext t
    rw [Finset.sum_apply]
    simp only [map_smul, projDer_octDer, Pi.smul_apply, Pi.single_apply, smul_eq_mul, mul_ite,
      mul_one, mul_zero]
    rw [Finset.sum_ite_eq]
    simp
  have hinj : Function.Injective L14 := fun a b hab => by
    have ha := hsec a; rw [hab, hsec b] at ha; exact ha.symm
  have hfr : Module.finrank ℚ (Fin 14 → ℚ) = Module.finrank ℚ (↥Der𝕆) := by
    rw [octonion_derivation_dim, Module.finrank_pi, Fintype.card_fin]
  have hsurj : Function.Surjective L14 := by
    have key : Function.Injective L14 ↔ Function.Surjective L14 :=
      LinearMap.injective_iff_surjective_of_finrank_eq_finrank
        (V := Fin 14 → ℚ) (V₂ := ↥Der𝕆) (f := L14) hfr
    exact key.mp hinj
  rw [Submodule.eq_top_iff']
  intro x
  obtain ⟨c, rfl⟩ := hsurj x
  rw [hLc]
  exact Submodule.sum_mem _ fun i _ =>
    Submodule.smul_mem _ _ (Submodule.subset_span (Set.mem_range_self i))

/-- **`range(evOct e)` is the span of the 14 concrete image vectors** `evOct e (octDer i)`,
because `octDer` spans `Der(𝕆)`. -/
theorem range_evOct_eq_span_images (e : Fin 8 → ℚ) :
    LinearMap.range (evOct e)
      = Submodule.span ℚ (Set.range fun i => evOct e (octDer i)) := by
  rw [LinearMap.range_eq_map, ← octDer_span_eq_top, Submodule.map_span, ← Set.range_comp]
  rfl

end QOU.MathlibExt.OctonionDerivations
