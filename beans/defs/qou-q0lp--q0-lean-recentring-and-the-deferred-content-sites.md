---
# qou-q0lp
title: 'q₀: re-centre the 79 Lean statements, plus 8 content sites deferred from the legibility pass'
status: in-progress
pr: 8188
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:55:00Z
updated_at: 2026-11-16T20:23:00Z
parent: qou-2002
---

The 2026-08-21 legibility + prose pass (option 3 + 2 of
[`docs/audits/2026-08-21-three-reconciliations.md`](../docs/audits/2026-08-21-three-reconciliations.md))
relabelled 22 `(50 dps)` sites, corrected 13 mis-rounded prose values and
one digit transposition. What it deliberately did not touch:

## 1. The Lean layer — the bulk of the problem

`1.1097` appears **110 times in `.lean`**, **79 of them inside statements**
rather than comments:

```lean
q_approx : |q - 1.1097| < 0.001
cfl_gap 1.1097 > 2 ∧ cfl_gap 1.1097 < 2.1 := by
diquark_binding_per_baryon 1.1097 < 4 := by
```

None of these is false — `|1.10998 − 1.1097| = 0.00028`, so the slack
absorbs the error — but each discharges at a point that is not the
substrate. Re-pointing them changes proof obligations, so it needs a
working Lean build; the container that found this could not build Lean.

Do it as one pass with the build available, not opportunistically: the
statements are load-bearing for the observations chapter, and a half-done
re-centring leaves the corpus with three centres instead of two.

## 2. Content sites held back, and why

- **`observations/local-substrate-q.md`** — `q|_U = 1.1097 ± 0.001` has a
  `.lean` sibling carrying the same numbers. Fixing the prose alone would
  desync the pair, so it belongs with item 1.
- **`unital-groebner-bases/.../jet-stratified-reduction.md`** — its
  `q = 1.1097` is keyed on by
  [`content/pipeline/witness-substitution-audit.ts`](../content/pipeline/witness-substitution-audit.ts)
  (lines 439, 846), which names the literal and the 29 witnesses carrying
  it. Change the two together or the audit's cover computation goes stale.
- **Five `mass-theory` blocks** still carrying `(50 dps)` on the 16-digit
  muon value (`mass-tower-coefficient-stratification-proof`,
  `frobenius-gram-matrix-context`, `exterior-square-borromean-proof`,
  `derived-mass-formula-light-isotopes-proof`, `-context`). Skipped only
  because audit agents held those files at the time; a mechanical follow-up.

## 3. An open question for the owner, not a defect

`appendix-qvalues/proton-mass-substrate-identity-derivation` is a
**production identity** whose q₀ digits (`…97859555`) identify the *muon*
pin, while the standing directive makes the proton pin the compute default.
The transposition in it is fixed and the pin is now labelled, so the text is
no longer misleading — but whether a production identity should evaluate at
the ideal-layer pin is a layer question, and the block does not say.

## Why the label, not the value, was the reported harm

`1.109978595554181` is **not** a corrupt string: it is the CAL-2 solution
for CODATA-2018 `m_μ/m_e`, verified here as `1.1099785955541805753…`, and
it sits 0.0028 ppb from the current muon pin against 11.53 ppb for the
proton pin — the μ–p substrate tension itself. Its defect was always
presentational: 16 digits labelled "(50 dps)", with no statement of which
pin it is. That is what the pass fixed.

## Progress Update (2026-11-16, PR #8188)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/CodataTruncationAndQ0AnchorRecentering.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/codata_truncation_and_q0_anchor_recentering_probe.py` and stamped witness `computations/probes/codata-truncation-and-q0-anchor-recentering.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 4f0055fd85b9bb82232f9b87ef757139e895bd6d`).
- [ ] Awaiting merge of PR [`litlfred/qou#8188`](https://github.com/litlfred/qou/pull/8188) (`548ed6acbe88e5772065a0fdb4d623f3472d3430`).

