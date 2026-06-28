---
# vq21
title: 'Vacuity fix: lean/Interactions (2 defects)'
status: open
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/Interactions**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: self-assuming-projection.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/Interactions/UniversalILP.lean:49` - self-assuming-projection - `UniversalILP`
- `lean/QOU/Interactions/inductiveGBReduction.lean:83` - self-assuming-projection - `inductiveGBReduction`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
