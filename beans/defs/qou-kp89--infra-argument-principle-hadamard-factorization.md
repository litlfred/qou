---
# qou-kp89
title: 'Infra: argument principle + Hadamard factorization'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T01:39:43Z
updated_at: 2026-11-20T20:55:32Z
parent: qou-c8p8
---

Blocks: EllipticDivisorDegree (1 — argument principle), HadamardFactorization (3 — Weierstrass factor bound, multipliability, factorization theorem). Need Mathlib residue theorem / contour integration.

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


## 2026-11-20 — W10

Argument-principle half DONE: annulus argument principle with ℤ orders (`QOU/Mathlib/ArgumentPrincipleAnnulus.lean`) and Liouville third theorem proved (PR #8604). Hadamard factorization (`HasHadamardFactorization`) remains open — multi-session.

## 2026-11-20 — PI-5 ingredients proved (PR #8651); Hadamard itself still OPEN

Proved, sorry-free: exponent of convergence ≤ order (`ExponentOfConvergence`), Jensen zero-count (`JensenZeroCounting`), canonical product entire + order ≤ σ (`CanonicalProductGrowth`, Borel), zero-free finite-order ⇒ exp(poly) (`HadamardZeroFree`). REMAINING for `HasHadamardFactorization`: divisor → zero sequence with multiplicity; f/P entire and zero-free; minimum-modulus lower bound on |P| giving f/P order ≤ ρ (the hard step).

## 2026-11-20 — DONE: Hadamard factorization PROVED (PR #8651)

`QOU.Mathlib.HadamardAssembly.hadamard_factorization_unconditional : HasHadamardFactorization`, sorry-free, standard axioms. Chain: ExponentOfConvergence, CanonicalProductGrowth, HadamardZeroFree, HadamardQuotient (enumeration with multiplicity, f/P entire zero-free), HadamardMinimumModulus (lower bound on |P| on separated circles), HadamardAssembly (countable index incl. finite/empty). The argument principle half was closed earlier (qou-z4jb / qou-nuxb). NOT addressed: genus minimality; applicability to phiBProd (a ratio; see qou-c3if).
