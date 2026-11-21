---
# qou-ghc6
title: 'BUILD: Lie-algebra-valued 1-forms on a normed space from Mathlib DifferentialForm/extDeriv (replaces the NonAbelianStokes abstract carrier)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:07:55Z
updated_at: 2026-11-21T03:18:24Z
parent: qou-c8p8
---

**BUILD.** `QOU/Mathlib/NonAbelianStokes.lean:47` carries `LieValuedOneForm` as an
abstract `Prop`-shaped carrier for `Ω¹(M; 𝔤)` with no model — flagged as
self-certifying in bean `qou-ewc4`.

**A real model is available at the pin.** `Mathlib/Analysis/Calculus/DifferentialForm/Basic.lean`
(231 lines, measured 2026-09-04 against mathlib `f897ebcf72c`) represents an `n`-form as

    ω : E → E [⋀^Fin n]→L[𝕜] F

with `E` and `F` **arbitrary** normed spaces over a `NontriviallyNormedField 𝕜`
(variable block at `Basic.lean:48-53`). So with
`[NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] [LieRing 𝔤] [LieAlgebra ℝ 𝔤]`, a 𝔤-valued
1-form on a normed space is `E → E [⋀^Fin 1]→L[ℝ] 𝔤` — no new type needed. The file
also supplies `extDeriv`, linearity, and **`extDeriv_extDeriv` (`d ∘ d = 0`)**.

**Scope:** carrier + bracket-wedge `[α ∧ β]` + covariant differential
`d_α β = dβ + [α ∧ β]`. ~100-200 lines.

**What this does NOT close:** the multiplicative line/surface integral. Mathlib has
**no** holonomy, parallel transport or path-ordered exponential — measured,
`grep -rln 'holonomy\|parallel transport\|ParallelTransport\|pathOrdered' Mathlib/`
returns **0 files**. That half stays RESEARCH (Yekutieli 2015).

**Why worth doing anyway:** the file's own worked example is `M = ℝ²` (line 107), which
is a normed space, so this replaces an assertion-free carrier with a real object on
exactly the case it cares about.

Related defect: the same file at line 10 misdescribes what Mathlib holds — see the
false-claim bean filed alongside this one.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B2.

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

## 2026-11-20 — DONE (PR #8678)

`QOU/Mathlib/LieValuedForms.lean`, sorry-free, standard axioms: bracket-wedge, curvature `dα + ½[α∧α]`, covariant d; graded symmetry, bilinearity, constant-connection curvature and flatness criterion. Bracket carried as a continuous bilinear map (Mathlib has no normed Lie algebras; `toLieRing`/`toLieAlgebra` bridges). NOT done: rewiring `NonAbelianStokes.lean` onto this model, Bianchi, holonomy (absent from Mathlib).

## 2026-11-21 — NonAbelianStokes rewired (PR #8700)

The 'NOT done' above is now done: `NonAbelianStokes` carriers are `OneForm/TwoForm`, `cellBoundary` and curvature are definitions, Stokes RHS is the curvature. Integrals and Stokes still assumed (Mathlib lacks path-ordered exponential).
