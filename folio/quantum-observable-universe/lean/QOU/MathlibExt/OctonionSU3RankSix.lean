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

-- Ref: [leitner2026] docs/audits/2026-07-17-octonion-su3-stabilizer-in-g2.md
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
  have hinj : Function.Injective L14 := Function.LeftInverse.injective hsec
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

/-! ### `rank(ev_{e₁}) = 6` at the concrete unit imaginary `e₁ = Pi.single 1 1`

The 14 images `evOct e₁ (octDer i) = (octDerMat i) ·ᵥ e₁` are the 1st columns of the
`octDerMat i`; a direct evaluation gives `±e₂, …, ±e₇` for the nine non-stabilizer
derivations and `0` for the five in `su3 e₁`.  Hence `range(evOct e₁)` is exactly the
span of `{e₂, …, e₇}` — the 6-dimensional coordinate subspace `{v : v₀ = v₁ = 0}`. -/

/-- The index embedding `{0,…,5} ↪ {2,…,7} ⊂ Fin 8`. -/
private def embE1 : Fin 6 → Fin 8 := ![2, 3, 4, 5, 6, 7]

/-- The 6 standard basis vectors `e₂, …, e₇` spanning `range(evOct e₁)`. -/
private def wE1 (j : Fin 6) : Fin 8 → ℚ := Pi.single (embE1 j) 1

private theorem wE1_linearIndependent : LinearIndependent ℚ wE1 := by
  have hemb : Function.Injective embE1 := by decide
  have hwb : wE1 = ⇑(Pi.basisFun ℚ (Fin 8)) ∘ embE1 := by
    funext j; fin_cases j <;> simp [wE1, embE1, Pi.basisFun_apply]
  rw [hwb]
  exact (Pi.basisFun ℚ (Fin 8)).linearIndependent.comp embE1 hemb

/-- **The rank of the color evaluation at `e₁` is 6** — `range(evOct e₁)` is the span of
the six images `±e₂, …, ±e₇`, an independent set.  Together with the `#3860` gate this
closes `finrank (su3 e₁) = 8 = dim SU(3)`. -/
theorem finrank_range_evOct_e1 :
    Module.finrank ℚ (LinearMap.range (evOct (Pi.single 1 1))) = 6 := by
  have hspan : LinearMap.range (evOct (Pi.single 1 1)) = Submodule.span ℚ (Set.range wE1) := by
    rw [range_evOct_eq_span_images]
    apply le_antisymm
    · rw [Submodule.span_le]
      rintro _ ⟨i, rfl⟩
      dsimp only
      fin_cases i
      -- i=0 : +e₅ = wE1 3
      · have hv : evOct (Pi.single 1 1) (octDer 0) = wE1 3 := by
          show (octDerMat 0).mulVec (Pi.single 1 (1:ℚ)) = wE1 3
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨3, rfl⟩
      -- i=1 : +e₄ = wE1 2
      · have hv : evOct (Pi.single 1 1) (octDer 1) = wE1 2 := by
          show (octDerMat 1).mulVec (Pi.single 1 (1:ℚ)) = wE1 2
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨2, rfl⟩
      -- i=2 : -e₃ = -wE1 1
      · have hv : evOct (Pi.single 1 1) (octDer 2) = -wE1 1 := by
          show (octDerMat 2).mulVec (Pi.single 1 (1:ℚ)) = -wE1 1
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.neg_mem _ (Submodule.subset_span ⟨1, rfl⟩)
      -- i=3 : +e₆ = wE1 4
      · have hv : evOct (Pi.single 1 1) (octDer 3) = wE1 4 := by
          show (octDerMat 3).mulVec (Pi.single 1 (1:ℚ)) = wE1 4
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨4, rfl⟩
      -- i=4 : -e₃ = -wE1 1
      · have hv : evOct (Pi.single 1 1) (octDer 4) = -wE1 1 := by
          show (octDerMat 4).mulVec (Pi.single 1 (1:ℚ)) = -wE1 1
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.neg_mem _ (Submodule.subset_span ⟨1, rfl⟩)
      -- i=5 : +e₂ = wE1 0
      · have hv : evOct (Pi.single 1 1) (octDer 5) = wE1 0 := by
          show (octDerMat 5).mulVec (Pi.single 1 (1:ℚ)) = wE1 0
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨0, rfl⟩
      -- i=6 : 0 (stabilizer)
      · have hv : evOct (Pi.single 1 1) (octDer 6) = 0 := by
          show (octDerMat 6).mulVec (Pi.single 1 (1:ℚ)) = 0
          funext k; fin_cases k <;>
            simp [octDerMat, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.zero_mem _
      -- i=7 : 0
      · have hv : evOct (Pi.single 1 1) (octDer 7) = 0 := by
          show (octDerMat 7).mulVec (Pi.single 1 (1:ℚ)) = 0
          funext k; fin_cases k <;>
            simp [octDerMat, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.zero_mem _
      -- i=8 : +e₇ = wE1 5
      · have hv : evOct (Pi.single 1 1) (octDer 8) = wE1 5 := by
          show (octDerMat 8).mulVec (Pi.single 1 (1:ℚ)) = wE1 5
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨5, rfl⟩
      -- i=9 : 0
      · have hv : evOct (Pi.single 1 1) (octDer 9) = 0 := by
          show (octDerMat 9).mulVec (Pi.single 1 (1:ℚ)) = 0
          funext k; fin_cases k <;>
            simp [octDerMat, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.zero_mem _
      -- i=10 : 0
      · have hv : evOct (Pi.single 1 1) (octDer 10) = 0 := by
          show (octDerMat 10).mulVec (Pi.single 1 (1:ℚ)) = 0
          funext k; fin_cases k <;>
            simp [octDerMat, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.zero_mem _
      -- i=11 : 0
      · have hv : evOct (Pi.single 1 1) (octDer 11) = 0 := by
          show (octDerMat 11).mulVec (Pi.single 1 (1:ℚ)) = 0
          funext k; fin_cases k <;>
            simp [octDerMat, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.zero_mem _
      -- i=12 : -e₂ = -wE1 0
      · have hv : evOct (Pi.single 1 1) (octDer 12) = -wE1 0 := by
          show (octDerMat 12).mulVec (Pi.single 1 (1:ℚ)) = -wE1 0
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.neg_mem _ (Submodule.subset_span ⟨0, rfl⟩)
      -- i=13 : +e₄ = wE1 2
      · have hv : evOct (Pi.single 1 1) (octDer 13) = wE1 2 := by
          show (octDerMat 13).mulVec (Pi.single 1 (1:ℚ)) = wE1 2
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨2, rfl⟩
    · rw [Submodule.span_le]
      rintro _ ⟨j, rfl⟩
      fin_cases j
      -- wE1 0 = e₂ = evOct e₁ (octDer 5)
      · have hv : wE1 0 = evOct (Pi.single 1 1) (octDer 5) := by
          show wE1 0 = (octDerMat 5).mulVec (Pi.single 1 (1:ℚ))
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨5, rfl⟩
      -- wE1 1 = e₃ = -evOct e₁ (octDer 2)
      · have hv : wE1 1 = -evOct (Pi.single 1 1) (octDer 2) := by
          show wE1 1 = -(octDerMat 2).mulVec (Pi.single 1 (1:ℚ))
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1,
              Matrix.of_apply]
        exact hv ▸Submodule.neg_mem _ (Submodule.subset_span ⟨2, rfl⟩)
      -- wE1 2 = e₄ = evOct e₁ (octDer 1)
      · have hv : wE1 2 = evOct (Pi.single 1 1) (octDer 1) := by
          show wE1 2 = (octDerMat 1).mulVec (Pi.single 1 (1:ℚ))
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨1, rfl⟩
      -- wE1 3 = e₅ = evOct e₁ (octDer 0)
      · have hv : wE1 3 = evOct (Pi.single 1 1) (octDer 0) := by
          show wE1 3 = (octDerMat 0).mulVec (Pi.single 1 (1:ℚ))
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨0, rfl⟩
      -- wE1 4 = e₆ = evOct e₁ (octDer 3)
      · have hv : wE1 4 = evOct (Pi.single 1 1) (octDer 3) := by
          show wE1 4 = (octDerMat 3).mulVec (Pi.single 1 (1:ℚ))
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨3, rfl⟩
      -- wE1 5 = e₇ = evOct e₁ (octDer 8)
      · have hv : wE1 5 = evOct (Pi.single 1 1) (octDer 8) := by
          show wE1 5 = (octDerMat 8).mulVec (Pi.single 1 (1:ℚ))
          funext k; fin_cases k <;>
            simp [octDerMat, wE1, embE1, Matrix.mulVec, dotProduct,
              Matrix.of_apply, Pi.single_apply]
        exact hv ▸Submodule.subset_span ⟨8, rfl⟩
  rw [hspan, finrank_span_eq_card wE1_linearIndependent, Fintype.card_fin]

/-- **`dim 𝔰𝔲(3) = 8` unconditionally** at `e₁`: combine the `#3860` rank–nullity gate
`finrank (su3 e) = 8 ↔ rank(evOct e) = 6` with `rank(evOct e₁) = 6`.  This is the
`S⁶ = G₂/SU(3)` dimension count, fully in Lean. -/
theorem finrank_su3_e1 : Module.finrank ℚ (su3 (Pi.single 1 1)) = 8 :=
  (finrank_su3_eq_8_iff_rank_eq_6 (Pi.single 1 1)).mpr finrank_range_evOct_e1

end QOU.MathlibExt.OctonionDerivations
