---
# vq01
title: 'Vacuity fix: braids-and-knots (2 defects)'
status: open
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **braids-and-knots**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: trivial-true.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `braids-and-knots/pentagon-uv-commutation-woronowicz.lean:149` - trivial-true - `q_commutation_grade_one_half`
- `braids-and-knots/pentagon-uv-commutation-woronowicz.lean:274` - trivial-true - `pentagon_ascension_under_woronowicz`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
