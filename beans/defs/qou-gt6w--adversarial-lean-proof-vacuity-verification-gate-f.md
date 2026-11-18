---
# qou-gt6w
title: Adversarial Lean proof & vacuity verification gate for all Two-Term Epic modules (qou-qmoh, qou-zhjs, qou-dl1k)
status: completed
type: task
priority: high
tags:
    - adversarial-audit
    - lean
created_at: 2026-11-18T19:52:24Z
updated_at: 2026-11-18T20:19:51Z
parent: qou-7xl8
---

Adversarial red-team check on every Lean 4 module produced under Epic qou-7xl8 (`qou-qmoh`, `qou-zhjs`, `qou-dl1k`):
1. Verify each file imports the real `QOU.*` and `Mathlib.*` modules (zero import-free `Int`/`Bool` wrapper structs).
2. Run `scripts/lean-verify.sh <file.lean>` (`-DautoImplicit=false`), `#print axioms` (only `propext`, `Classical.choice`, `Quot.sound`), `scripts/lean-borrowed-name-audit.py --strict`, `scripts/lean-definition-collapsed-audit.py --strict`, `scripts/lean-vacuous-theorem-scan.py`, and `scripts/lean-self-assuming-audit.py`.
3. Check every theorem statement line-by-line against the narrative claim and the cited `library/<doc-id>/blocks/<block-id>` node to ensure zero `X - X = 0` definitional-subtraction laundering or self-assuming projections.
4. If any proof has an open step, verify that it fails honestly (`sorry` with `-- Ref:` + complete handoff note on the bean with exact `lean_goal` state).



## Completion Record (2026-11-18)
- Independent adversarial red-team & vacuity audit completed by `lane-7b4f` across all three Lean 4 modules (`NucleonWeightSpaceTwoTerm.lean`, `NucleonIdempotentModifiedTrace.lean`, `CategoricalLagrangianTwoTermBridge.lean`).
- Added machine-checked 11-crossing word fold bridge theorems `protonWord_foldl_eq_protonCoord` and `neutronWord_foldl_eq_neutronCoord` to `NucleonIdempotentModifiedTrace.lean`.
- All 7 static/semantic audit scripts + `lean-verify.sh` + `#print axioms` passed with `0` defects.
