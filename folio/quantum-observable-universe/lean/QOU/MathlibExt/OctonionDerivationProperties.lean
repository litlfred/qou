import QOU.MathlibExt.OctonionDerivations

/-!
# QOU.MathlibExt.OctonionDerivationProperties — derivations preserve `𝕆 = ℝ·1 ⊕ Im 𝕆`

Structural properties of the octonion derivation algebra `Der𝕆` (from
`QOU.MathlibExt.OctonionDerivations`), connecting `dim Der(𝕆) = 14 = dim 𝔤₂` to the
`G₂ = Aut(𝕆)` mechanism used in the genus-4 octonion-recovery analysis
(`docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md`).

* `octMul_one_left` / `octMul_one_right` — `e₀ = Pi.single 0 1` is the two-sided unit.
* **`derivation_annihilates_one`** — every octonion derivation kills the identity,
  `D 1 = 0`. This is the *infinitesimal* shadow of `no_fixed_unit`
  (`QOU.BringsSurface.OctonionObstruction`, "an algebra automorphism fixes `1`"):
  a derivation is the tangent to a one-parameter family of automorphisms, and
  differentiating `φ_t(1) = 1` at `t = 0` gives `D 1 = 0`. Hence `Der(𝕆)` preserves
  the splitting `𝕆 = ℝ·1 ⊕ Im 𝕆`, acting trivially on `ℝ·1` and (as the 14-dimensional
  `𝔤₂`) on the 7-dimensional `Im 𝕆` where `G₂` acts irreducibly.

Base ring ℚ (the derivation-dimension count needs char ≠ 2, 3); nothing archimedean.
-/

namespace QOU.MathlibExt.OctonionDerivations

open Matrix QOU.MathlibExt.DerivationRankNullity

/-- `e₀ = Pi.single 0 1` is a left unit for the octonion product. -/
theorem octMul_one_left (v : Fin 8 → ℚ) : octMul (Pi.single 0 1) v = v := by
  funext k; fin_cases k <;> simp [octMul, Pi.single_apply]

/-- `e₀ = Pi.single 0 1` is a right unit for the octonion product. -/
theorem octMul_one_right (v : Fin 8 → ℚ) : octMul v (Pi.single 0 1) = v := by
  funext k; fin_cases k <;> simp [octMul, Pi.single_apply]

/-- **Every octonion derivation annihilates the identity:** `D 1 = 0`.

The infinitesimal form of "an algebra automorphism fixes `1`"
(`QOU.BringsSurface.OctonionObstruction.no_fixed_unit`): applying the Leibniz rule to
`1 = 1·1` gives `D 1 = D 1 + D 1`, so `D 1 = 0`. Consequently every derivation preserves
the octonion splitting `𝕆 = ℝ·1 ⊕ Im 𝕆`. -/
theorem derivation_annihilates_one {D : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)} (hD : D ∈ Der𝕆) :
    D (Pi.single 0 1) = 0 := by
  rw [Der𝕆, mem_ker_leibnizDefect_iff] at hD
  have h := hD (Pi.single 0 1) (Pi.single 0 1)
  simp only [octMulₗ_apply, octMul_one_right, octMul_one_left] at h
  linear_combination -h

/-- The 14 explicit `𝔤₂` derivations all annihilate the identity. -/
theorem octDer_annihilates_one (i : Fin 14) : (octDer i).1 (Pi.single 0 1) = 0 :=
  derivation_annihilates_one (octDer i).2

end QOU.MathlibExt.OctonionDerivations
