---
# qou-i0sr
title: 'GAP WALL-3 lower bound: dH(z-axis) ≥ |log(b/a)| (FTC lower bound)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T13:02:37Z
updated_at: 2026-11-17T10:22:29Z
parent: qou-c8p8
---

T2 geodesic-uniqueness, WALL-3 LOWER bound. UPPER bound + existence LANDED
(PR #5236, HyperbolicGeodesicZAxis.lean: dH (0,0,a) (0,0,b) ≤ ofReal|log(b/a)|,
via the constant-speed vertical segment vseg, sorry-free).

OPEN: dH (zpt a) (zpt b) ≥ ofReal|log b − log a|, i.e. every admissible γ from
(0,0,a) to (0,0,b) has pathLenH γ ≥ ofReal|log(b/a)|. Combined with the upper
bound this yields the exact z-axis distance AND that vseg is an IsHypMinimizer
(its `minimal` field).

Derivation (standard, the crux):
  pathLenH γ = ∫⁻_{Icc 0 1} ofReal(‖γ'‖/z)      [z(t) := (γ t) 2]
    ≥ ∫⁻_{Icc 0 1} ofReal(|z'|/z)                [coord bound |(γ' t) 2| ≤ ‖γ' t‖]
    = ∫⁻_{Icc 0 1} ofReal(|(log∘z)'|)            [(log∘z)' = z'/z, z>0]
    ≥ ofReal|∫_0^1 (log∘z)'|                      [|∫|≤∫||  +  ofReal↔lintegral bridge]
    = ofReal|log z(1) − log z(0)| = ofReal|log b − log a|   [FTC]

Lean friction points (why it stalls, each a real Mathlib-API chunk):
 1. coord bound |(v) 2| ≤ ‖v‖ on EuclideanSpace — via abs_inner_le_norm with
    single 2 1 (EuclideanSpace.inner_single_right), or EuclideanSpace.norm_eq +
    Finset.single_le_sum. (SMALL, reusable.)
 2. z'(t) = (γ' t) 2 : z = EuclideanSpace.proj 2 ∘ γ, proj 2 is a CLM. (SMALL.)
 3. (log∘z)' = z'/z : (Real.hasDerivAt_log (z t ≠ 0)).comp. (SMALL.)
 4. ∞-length case split: if pathLenH γ = ∞ the bound is trivial; else finite
    lintegral of ‖γ'‖/z ⇒ |(log∘z)'| = |z'|/z has finite lintegral ⇒ integrable.
 5. FTC ∫_0^1 (log∘z)' = log b − log a : intervalIntegral.integral_eq_sub_of_
    hasDerivAt needs log∘z continuous on [0,1] (z continuous & >0) + interval-
    integrability of the derivative. Measurability of deriv γ on [0,1] needed.
 6. |∫_0^1 h| ≤ ∫_0^1 |h| (intervalIntegral.abs_integral_le_integral_abs) then
    ofReal(∫_0^1 |h|) = ∫⁻_{Ioc/Icc} ofReal|h| bridge
    (ofReal_integral_eq_lintegral_ofReal / MeasureTheory.integral for nonneg).

Points 4–6 are the substantial part (measurability of deriv, integrability from
finite lintegral, FTC hypotheses, Bochner↔lintegral bridge). Est. multi-hundred
lines. This is the "Mathlib has no hyperbolic geometry" reason.

File: folio/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicGeodesicZAxis.lean



---
UPDATE 2026-08-16 (PR #5253, branch claude/t2-wall-close-2026-08-16): LANDED sorry-free.
Was nearly immediate given the merged FTC lower bound dH_ge_logHeight: specialise it to
z-axis points (heights a, b). Added to HyperbolicGeodesicZAxis.lean:
  dH_zpt_ge          : ofReal|log(b/a)| ≤ dH (zpt a) (zpt b)
  dH_zpt             : dH (zpt a) (zpt b) = ofReal|log(b/a)|   (EXACT, with dH_zpt_le)
  pathLenH_vseg_eq_dH: the vertical segment is a genuine z-axis length-minimiser.
#print axioms = [propext, Classical.choice, Quot.sound]. Pending merge; human closes.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

### Progress Update (2026-11-17, Round 60 — lane-e667)
- **PR:** `litlfred/qou#8299` (`https://github.com/litlfred/qou/pull/8299`), head `7794a07bbdcd4212b670d7ed777098efe60dc9a4` (`COMMIT1 = a21b136d3f122bac6df50bab417b7232ca55064f`), labeled `ready-to-merge` + `release`, `ready: 7794a07bbdcd4212b670d7ed777098efe60dc9a4` (`https://github.com/litlfred/qou/pull/8299#issuecomment-6945265144`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/AnnulusWindingLogCountingLieCurvatureHemisphereInversionZAxisBound.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-argp`: `annulus_winding_step_and_single_zero_uniqueness`.
  - `qou-bp5n`: `radial_log_counting_decomposition_and_increment`.
  - `qou-ghc6`: `matrix_one_form_commutator_trace_and_flat_curvature`.
  - `qou-h2mb`: `hemisphere_inversion_radial_reversal_and_tangential_fix`.
  - `qou-i0sr`: `vertical_step_energy_dominance_and_telescoping_bound`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/annulus_winding_log_counting_lie_curvature_hemisphere_inversion_z_axis_bound_probe.py` + `computations/probes/annulus-winding-log-counting-lie-curvature-hemisphere-inversion-z-axis-bound.witness.json` (`scriptHash = 001b12183bba`, `scriptCommitSha = a21b136d3f122bac6df50bab417b7232ca55064f`, `allPassed = True`).
- **Adversarial Cross-Review (Round 60):** Verified `litlfred/qou#8291` (`97f9ffaed50b1b3971470d9bc651293cd4f935e3`, `0` advisories) and remediated `1 major, 1 advisory` borrowed-name findings on sibling PR `litlfred/qou#8277`, pushing `845c943537ff3112ef1cadf49f54381fb96fcb38` and posting `ready: 845c943537ff3112ef1cadf49f54381fb96fcb38` (`https://github.com/litlfred/qou/pull/8277#issuecomment-6945121466`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
