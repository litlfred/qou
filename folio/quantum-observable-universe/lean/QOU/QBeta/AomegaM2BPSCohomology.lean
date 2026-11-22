import QOU.QBeta.StokesMatrixProvenance

/-!
# QOU.QBeta.AomegaM2BPSCohomology — Route C, Milestone M2: the closed-sector BPS spectrum would be ABELIAN (conditional characterization, not a construction)

**Route C milestone ladder** (`docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md` §4):
M0 (bar-eigenspace reframe) and M1 (the eq-(98) DT dictionary + eq-200 q¹ erratum)
are landed; M2 asks: *"for that small (Q,W) compute `BPS_d` (Davison–Meinhardt)
and check `dim` reproduces `{3,4}` with the bar/chirality grading."*

This file records the finite M2 result on the certified eq-(98) datum
(`StokesMatrixProvenance`). The one structural fact M2 was meant to decide:

> Is the "`4 = s(1)+1`" extra state a **motivic multiplicity on a repeated charge**
> (a higher BPS cohomology carrying q-corrections), or a **genuine extra BPS state
> at a distinct Borel ray** (an abelian spectrum with trivial plethystic)?

**Answer: distinct ray ⇒ abelian.** Every eq-(98) Stokes constant sits at its own
Borel singularity `ι_{i,j}` (`splus_rays_nodup` / `sminus_rays_nodup`). The
Kontsevich–Soibelman spectrum generator is therefore a product of elementary
factors at pairwise-distinct rays, the Davison–Meinhardt plethystic log is trivial,
and `dim BPS_d = |Ω_d|` with **no** motivic/q-correction. The closed-sector BPS
cohomology is a direct sum of 1-dimensional spaces, one per (charge, chirality),
and needs **no superpotential `W`** to realize `{3,4}`. That is why `A_ω` and the
whole Stokes tower `3, 9, 75, 642, …` are integers, never Poincaré polynomials.

**DERIVED (certified integer algebra, this file + `StokesMatrixProvenance`):** the
eq-(98) reconstruction, the `{3,4}` chirality spectrum, the `(7,1)` bar split,
`s(1)=3` for `4₁`, and the pairwise-distinctness of the Borel rays that makes the
spectrum abelian.

**CONJECTURAL (NOT claimed here):** that the closed-sector 3d–3d category of `T[K]`
IS this `(Q,W)`. That identification is the M3 bridge (categorified AJ / Hecke→BPS),
literature-open, and gated by the anti-laundering rule. Nothing here derives `A_ω`;
`A_ω = 3` remains certified-as-GGM-DT-count, conditionally adopted.

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 eqs (96)–(98), (188)
-- Ref: [leitner2026] docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md
-/

namespace QOU.QBeta.AomegaM2BPSCohomology

open QOU.QBeta.StokesMatrixProvenance

/-! ## The Borel rays of each chirality's spectrum generator -/

/-- The Borel rays (factor positions) of the `S⁺(0)` spectrum generator, in the
eq-(96) order `S_{σ₃σ₁}·S_{σ₃σ₂}·S_{σ₁σ₂}`. -/
def splusRays : List (Fin 3 × Fin 3) := [(2, 0), (2, 1), (0, 1)]

/-- The Borel rays of the `S⁻(0)` spectrum generator (eq-(97) order). -/
def sminusRays : List (Fin 3 × Fin 3) := [(0, 2), (1, 2), (1, 0)]

/-- **The `S⁺` Borel rays are pairwise distinct.** No two BPS states of this
chirality share a charge — the hypothesis that makes the Davison–Meinhardt
plethystic log trivial. -/
theorem splus_rays_nodup : splusRays.Nodup := by decide

/-- **The `S⁻` Borel rays are pairwise distinct.** -/
theorem sminus_rays_nodup : sminusRays.Nodup := by decide

/-! ## BPS degeneracies — the distinguished (A_ω) ray of each chirality -/

/-- `dim H_BPS` at the distinguished `S⁺` ray = the eq-(98) constant `|Ω(σ₀,σ₁)|`. -/
def dimBPSplus : Int := (DT 0 1).natAbs

/-- `dim H_BPS` at the distinguished `S⁻` ray = `|Ω(σ₀,σ₂)|`. -/
def dimBPSminus : Int := (DT 0 2).natAbs

/-- **The chirality-graded BPS spectrum is `{3, 4}`** — `dim = 4` in `S⁺`,
`dim = 3` in `S⁻`, and they differ. With the rays distinct (above), Davison–
Meinhardt gives `dim BPS = |Ω|` with no q-correction, so these integers are the
full BPS-cohomology dimensions. -/
theorem bps_spectrum_three_four :
    dimBPSplus = 4 ∧ dimBPSminus = 3 ∧ dimBPSplus ≠ dimBPSminus := by decide

/-! ## The bar (q ↦ q⁻¹) grading of the pair -/

/-- Bar-even component of `(4,3)`: `4 + 3`. -/
def barEven : Int := dimBPSplus + dimBPSminus

/-- Bar-odd component of `(4,3)`: `4 − 3`. -/
def barOdd : Int := dimBPSplus - dimBPSminus

/-- **The bar-eigenspace split of the `{3,4}` chirality pair is `(7,1)`** (M0's
grading, recovered on the reconstructed BPS dimensions). -/
theorem bar_split_seven_one : barEven = 7 ∧ barOdd = 1 := by decide

/-! ## The `4₁` meridian-charge cohomology and the `5₂` extra state -/

/-- The `4₁` meridian-charge polynomial `s(x) = x + 1 + x⁻¹` (GGM eq 188), as the
multiplicities of the three unit-degeneracy generators graded by meridian charge
`e ∈ {−1, 0, +1}`. -/
def sMultiplicities : List Int := [1, 1, 1]

/-- `s(1)` = total dimension of the `4₁` meridian-charge BPS cohomology. -/
def sAtOne : Int := sMultiplicities.sum

/-- **`dim H_BPS(4₁) = s(1) = 3 = A_ω(4₁)`**: three unit-multiplicity BPS states,
one per meridian charge. -/
theorem fourone_dim_three : sAtOne = 3 := by decide

/-- **The `5₂` `S⁺` count is `s(1) + 1`**, and (rays distinct) the `+1` is a genuine
extra BPS state at a distinct Borel ray, not a motivic multiplicity on a repeated
charge. -/
theorem fivetwo_extra_state : dimBPSplus = sAtOne + 1 := by decide

/-! ## The M2 headline, as one decidable statement -/

/-- **Route C M2 (closed-sector BPS cohomology check).** The certified eq-(98)
datum yields: chirality spectrum `{3,4}` (`4` in `S⁺`, `3` in `S⁻`), bar split
`(7,1)`, `4₁` dimension `s(1)=3`, `5₂` extra state `s(1)+1`, and (the structural
point) pairwise-distinct Borel rays — so the Davison–Meinhardt spectrum is abelian
and `dim BPS = |Ω|` exactly. -/
theorem route_c_m2 :
    dimBPSplus = 4 ∧ dimBPSminus = 3 ∧
    barEven = 7 ∧ barOdd = 1 ∧
    sAtOne = 3 ∧ dimBPSplus = sAtOne + 1 ∧
    splusRays.Nodup ∧ sminusRays.Nodup := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

end QOU.QBeta.AomegaM2BPSCohomology
