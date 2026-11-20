---
# qou-dx7g
title: 'GAP: axiom-field scanner cited by qou-dxbw is missing from the repo'
status: in-progress
type: task
priority: high
tags:
    - lean
    - axiom-field-audit
    - reproducibility
created_at: 2026-11-20T08:12:14Z
updated_at: 2026-11-20T14:26:55Z
parent: qou-dxbw
---

Epic `qou-dxbw` and all eight child features give their counts (1803 carriers, 1336 uninstantiated, per-cluster tables, "Top Priority" lists) as coming from:

- `computations/audits/lean_axiom_field_and_mathlib_gap_audit.py`
- `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`

**Measured 2026-11-20 on main `917b69399`:** neither file exists. `git ls-remote origin` shows no branch with a matching name. A grep of `computations/`, `scripts/` and `docs/` finds no other reference.

**Consequence.** The counts cannot be reproduced. "Rank features by which axiom-fields each would discharge" cannot be re-measured. At least one classification looks wrong: `SkewStandardYoungTableau` is listed TOY_ONLY with 27 consumers, but it is a data structure with genuine counted inhabitants (see the `qou-ltwg` note).

**Next honest step.** Find the session that produced the epic (created 2026-11-19 08:19Z) and recover the script. Failing that, rewrite it with an explicit definition of "instantiated" that a reviewer can check. A carrier counts as instantiated when an `instance` or a term of the structure type exists anywhere in the Lean tree, not only in the same file. Also run the existing `folio/pipeline/lean-vacuity-axiom-audit.ts` and compare.

## 2026-11-20 — rewritten (PR #8571, W7 session_01VQDpPfKSC33hwjyKMw3EHV)

The scanner is rewritten at the cited path, with explicit definitions and a 4-case `--selftest` calibration. Result: 1560 carriers, 1040 uninhabited, 3 toy-only, 517 inhabited. This does not match the epic's 1803 / 1336, because the epic's definitions could not be recovered.

**Still open:** no satisfiability verdict. Parameter bundles (`HeckeParams`, 354 consumers) top the ranking even though they are trivially inhabitable. The bean stays in-progress until a per-carrier agent verdict separates hypotheses from axiom-fields.

## 2026-11-20T21:28:46Z — the 21 VACUOUS triage carriers worked (PRs #8691 part A, #8690 part B)

Owner instruction: repair, don't close or delete. Part A: 4 encode the claim, 2 partial, 5 GAP.
Part B: 0 full, 8 partial/GAP, DiscreteVortex left to main's #8180 repair. Residuals: qou-k7ra,
qou-k7rb. Bean stays in-progress (per-carrier verdicts for the rest of the 1007 still open).
