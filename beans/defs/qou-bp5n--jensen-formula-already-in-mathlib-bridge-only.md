---
# qou-bp5n
title: 'BRIDGE(lean): Jensen formula + Nevanlinna counting are ALREADY in Mathlib — wire, do not rebuild'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - hadamard
    - correction
    - paper-qou
    - reorg-2026-10-04
created_at: 2026-08-08T03:30:00Z
updated_at: 2026-11-17T10:22:29Z
parent: qou-c8p8
---

## Why this bean exists at all — a correction to my own claim

On 2026-08-08 I wrote, in a commit message and to the user, that PI-5 "needs
Jensen's formula, zero-counting, and Borel-Carathéodory machinery, none of which
Mathlib v4.24.0 has in usable form."

**That is wrong for two of the three.** Enumerating the environment (not
grepping filenames) turns up:

    MeromorphicOn.circleAverage_log_norm                     -- Jensen's formula
    AnalyticOnNhd.circleAverage_log_norm_of_ne_zero          -- the nonvanishing case
    ValueDistribution.logCounting                            -- N(r, a), via
                                                             -- MeromorphicOn.divisor
    ValueDistribution.proximity, .characteristic             -- m(r,a), T(r,f)
    ValueDistribution.first main theorem lemmas

Worse: `QOU/Mathlib/HadamardFactorization.lean`'s own module docstring said so
all along — "Mathlib has Jensen's formula, the Nevanlinna value-distribution
cone (`Analysis/Complex/ValueDistribution/`)". I contradicted a correct
statement sitting in the file I was editing.

Only **Borel-Carathéodory** was genuinely absent, and it is now done
(bean qou-8cwi).

## Do

Not "add Jensen". Find out how much of the bridge is already free:

1. Read `ValueDistribution.logCounting`'s definition. It is
   `Function.locallyFinsuppWithin.logCounting (MeromorphicOn.divisor ...)`.
   Determine whether it already equals the classical `N(r) = sum_{|a_n|<r} log(r/|a_n|)`
   or needs an unfolding lemma.
2. If it does, the Hadamard step "exponent of convergence <= order" (bean
   qou-c3if) may be a short derivation rather than a build.
3. Only then write anything.

## ROAST

**"So is there any work in this bean at all?"** Possibly very little, and that is
the honest answer until step 1 is done. This bean may close as
"already-in-Mathlib, no code needed". That would be a good outcome, and it is
the reason the bean says READ FIRST rather than WRITE FIRST.

**"You are beaning your own error as if it were work."** Partly fair. The
deliverable here is a correction plus a scoping check, not a theorem. It is
beaned because the wrong claim is in a pushed commit message and would otherwise
send the next agent to rebuild machinery that already exists — the same failure
mode as the qou-fl4t "DG Section 4.5" misread, twice in one session.

**"Why did you get it wrong?"** Same root cause both times: I asserted a
structural fact about a source (DG's paper; Mathlib) without running the
one-line check. The check here is `run_cmd` over `env.constants`, and it takes
under a minute. It should precede any "Mathlib lacks X" claim, and any such
claim in this corpus that was not made that way should be treated as unverified.

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
