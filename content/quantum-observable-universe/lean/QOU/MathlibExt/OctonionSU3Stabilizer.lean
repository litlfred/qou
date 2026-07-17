import QOU.MathlibExt.OctonionDerivationProperties
import QOU.MathlibExt.OctonionDerivationsUpperBound
import Mathlib.LinearAlgebra.Dimension.RankNullity

/-!
# QOU.MathlibExt.OctonionSU3Stabilizer — colour `𝔰𝔲(3) ⊂ 𝔤₂ = Der(𝕆)`

The **stabilizer of a unit imaginary octonion** inside the derivation algebra
`𝔤₂ = Der(𝕆)` (`dim = 14`, `octonion_derivation_dim`). Fix `e : 𝕆` and evaluate a
derivation there:

`evOct e : Der(𝕆) →ₗ[ℚ] 𝕆,  D ↦ D(e)`,   `su3 e := ker (evOct e)`.

`su3 e` is the subalgebra of derivations fixing `e`. For a **unit imaginary** `e`
this is the **Günaydin–Gürsey colour `SU(3) ⊂ G₂ = Aut(𝕆)`** (the "fix an
imaginary direction → `Im 𝕆 = 1 ⊕ 3 ⊕ 3̄`" subgroup), with

`dim 𝔰𝔲(3) = 14 − rank(ev_e) = 14 − 6 = 8 = dim SU(3)`,  so
`14 − 8 = 6 = dim S⁶ = dim G₂/SU(3)`.

This file lands the **rank–nullity reduction** `finrank su3 = 14 − rank(ev_e)`
and the gate `finrank su3 = 8 ⟺ rank(ev_e) = 6` — sorry-free, on the corpus's own
`Der𝕆` — mirroring the sibling `dim = 14 ⟺ rank = 50` gate
(`DerivationRankNullity.octCarrier_finrank_ker_eq_14_iff`). The value `rank = 6`
is established by exact rational linear algebra
([`computations/octonion_su3_stabilizer_probe.py`](../../../../../computations/octonion_su3_stabilizer_probe.py),
witness `octonion-su3-stabilizer.witness.json`, merged), and its explicit Lean
proof (a `6×6` image minor + the `⟨e₀,e⟩^⊥` bound from `derivation_annihilates_one`
and norm-preservation) is the follow-up. Base ring ℚ; nothing archimedean.

**Verification status.** Sorry-free; the proofs are `rfl`/`omega` reductions over
the corpus's own `Der𝕆`. These were **not** machine-validated in the authoring
sandbox: the sole nontrivial dependency `octonion_derivation_dim`
(`finrank ℚ Der𝕆 = 14`) lives in the `decide`-heavy
`OctonionDerivationsUpperBound` (50×50 `decide`, prohibitively slow to compile
in-sandbox), so **CI `lake build QOU` is the gate**. The `evOct` `map_add'` /
`map_smul' := rfl` proofs are sound because `Der𝕆` is a submodule of *linear
maps* (`(Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)`), whose `+`/`•` act pointwise, so `D.1 e`
is honest linear-map application and the module operations are definitional.

-- Ref: [manuscript] docs/audits/2026-07-17-octonion-su3-stabilizer-in-g2.md
-/

namespace QOU.MathlibExt.OctonionDerivations

open Module

/-- **Evaluation of a derivation at a fixed octonion `e`**: `D ↦ D(e)`, linear in
`D`. The stabilizer `𝔰𝔲(3)` is its kernel. -/
def evOct (e : Fin 8 → ℚ) : Der𝕆 →ₗ[ℚ] (Fin 8 → ℚ) where
  toFun D := D.1 e
  map_add' D D' := rfl
  map_smul' c D := rfl

@[simp] theorem evOct_apply (e : Fin 8 → ℚ) (D : Der𝕆) : evOct e D = D.1 e := rfl

/-- **The colour stabilizer `𝔰𝔲(3) = {D ∈ Der(𝕆) : D(e) = 0}`** — the derivations
fixing `e`. For a unit imaginary `e` this is the Günaydin–Gürsey colour
`SU(3) ⊂ G₂ = Aut(𝕆)`. -/
def su3 (e : Fin 8 → ℚ) : Submodule ℚ Der𝕆 := LinearMap.ker (evOct e)

theorem mem_su3_iff {e : Fin 8 → ℚ} {D : Der𝕆} : D ∈ su3 e ↔ D.1 e = 0 :=
  LinearMap.mem_ker

/-- **Rank–nullity for the stabilizer:** `dim 𝔰𝔲(3) = 14 − rank(ev_e)`, using
`dim Der(𝕆) = 14`. -/
theorem finrank_su3 (e : Fin 8 → ℚ) :
    finrank ℚ (su3 e) = 14 - finrank ℚ (LinearMap.range (evOct e)) := by
  have h := (evOct e).finrank_range_add_finrank_ker
  rw [octonion_derivation_dim] at h
  simp only [su3]
  omega

/-- **The `S⁶ = G₂/SU(3)` gate:** the colour stabilizer is `8`-dimensional (the
Lie algebra of `SU(3)`) **iff** the evaluation has rank `6` (`= dim S⁶`). The
`rank = 6` value is exact-arithmetic certified (merged probe); this is the clean
Lean reduction. -/
theorem finrank_su3_eq_8_iff_rank_eq_6 (e : Fin 8 → ℚ) :
    finrank ℚ (su3 e) = 8 ↔ finrank ℚ (LinearMap.range (evOct e)) = 6 := by
  have h := finrank_su3 e
  have hle : finrank ℚ (LinearMap.range (evOct e)) ≤ 14 := by
    have := (evOct e).finrank_range_add_finrank_ker
    rw [octonion_derivation_dim] at this
    omega
  omega

end QOU.MathlibExt.OctonionDerivations
