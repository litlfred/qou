---
# vq09
title: 'Vacuity fix: lean/BraidsAndKnots (2 defects)'
status: open
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/BraidsAndKnots**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: trivial-true.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/BraidsAndKnots/UnitModulusEigenvalue.lean:66` - trivial-true - `borromean_trace_21_eq_neg_two`
- `lean/QOU/BraidsAndKnots/UnitModulusEigenvalue.lean:90` - trivial-true - `all_positive_trace_positive`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
