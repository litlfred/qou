---
# qou-m8xt
title: 'BUILD: retype IdealTetrahedron over Mathlib UpperHalfPlane (ℍ) — 62 QOU files hand-roll 0 < im, zero use ℍ'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:08Z
updated_at: 2026-11-17T10:33:06Z
parent: qou-c8p8
---

**BUILD.** `QOU/MathlibExt/IdealTriangulation.lean:66-70` is

    structure IdealTetrahedron where
      shape : ℂ
      im_pos : 0 < shape.im

That is `Mathlib.Analysis.Complex.UpperHalfPlane.ℍ`, spelled out.

**Measured 2026-09-04** (mathlib `f897ebcf72c`, `grep -rn 'UpperHalfPlane' QOU/`):
`UpperHalfPlane` occurs in **2** QOU files and in **zero** QOU declarations — both hits
are audit prose (`Archimedean/HyperbolicVolumeMeasure.lean:9`,
`Eightfold/HyperbolicVolumeFormType.lean:137`). Meanwhile **62** QOU files carry a
hand-rolled `im_pos` / `0 < _.im`.

**What retyping over `ℍ` buys**, all present at the pin:
* `UpperHalfPlane.im_pos`, `ne_zero`, `normSq_pos`, `re_add_im`, `ext'`;
* the `positivity` extensions `evalUpperHalfPlaneIm` / `evalUpperHalfPlaneCoe`, so
  `0 < z.im` side goals discharge automatically;
* the `{x : ℝ // 0 < x}` scaling and `ℝ`-translation actions (`posRealAction`,
  `AddAction ℝ ℍ`);
* `MoebiusAction.lean` (389 lines) — the `GL(2,ℝ)⁺` and `SL(2,R)` Möbius actions, the
  natural home for the shape-parameter cycle `z ↦ 1/(1−z) ↦ 1 − 1/z`;
* `Metric.lean` (341 lines) — the hyperbolic distance on ℍ², `Dist ℍ`, `dist_eq`,
  `cosh_dist`, and isometries including `ModularGroup.S`.

**Size: small-to-medium.** Mechanically it is a retype plus `.coe` insertions, but it
touches a load-bearing structure (`IdealTetrahedron.volume`, `volume_rotate`, the
gluing equations, `ManifoldVolumeBridge`, `ManifoldVolumePositive`) so it needs a real
`lean`-direct pass, not a sed.

**Sequence:** do the `BlochWigner_unit_circle` build first — it is ~5 lines and free.

**Scope note:** this is ℍ², i.e. the 2-dimensional layer only. It does **not** touch
the ℍ³ gap (`qou-5gai`), which is real and unaffected.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B4, §H1.

### Progress Update (2026-11-17, Round 61 — lane-e667)
- **PR:** `litlfred/qou#8303` (`https://github.com/litlfred/qou/pull/8303`), head `2a91d843d44db15a0190138e20fb1878634fbbeb` (`COMMIT1 = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`), labeled `ready-to-merge` + `release`, `ready: 2a91d843d44db15a0190138e20fb1878634fbbeb` (`https://github.com/litlfred/qou/pull/8303#issuecomment-6945508253`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/AlternatingThreeFormPrimaryFactorUpperHalfPlaneCatalanClausenSymmetry.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-jvua`: `alternating_three_form_antisym_diag_and_unit_frame`.
  - `qou-kp89`: `primary_factor_linear_cancellation_and_cubic_remainder`.
  - `qou-m8xt`: `upper_half_plane_shifted_modulus_pos_and_cyclic_closure`.
  - `qou-mame`: `quarter_turn_even_vanishing_and_odd_alternation`.
  - `qou-u4mx`: `termwise_periodic_and_odd_two_harmonic_sum`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/alternating_three_form_primary_factor_upper_half_plane_catalan_clausen_symmetry_probe.py` + `computations/probes/alternating-three-form-primary-factor-upper-half-plane-catalan-clausen-symmetry.witness.json` (`scriptHash = 0ee532c9f9a2`, `scriptCommitSha = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`, `allPassed = True`).
- **Adversarial Cross-Review (Round 61):** Verified `litlfred/qou#8285` (`250465c60a6cea44d9f569e88cc79ee2c8d8051b`, `0` advisories on all 5 added theorems, valid witness `39a564805d3e`) and `litlfred/qou#8299` (`7794a07bbdcd4212b670d7ed777098efe60dc9a4`, `0` advisories, valid witness `001b12183bba`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
