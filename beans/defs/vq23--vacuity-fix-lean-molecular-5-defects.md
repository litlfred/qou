---
# vq23
title: 'Vacuity fix: lean/Molecular (5 defects)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/Molecular**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: placeholder-stub.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/Molecular/benzene_threading_emergence.lean:1` - placeholder-stub - ``
- `lean/QOU/Molecular/ch4_lp_dual_binding.lean:1` - placeholder-stub - ``
- `lean/QOU/Molecular/co2_lp_dual_binding.lean:1` - placeholder-stub - ``
- `lean/QOU/Molecular/co_lp_dual_binding.lean:1` - placeholder-stub - ``
- `lean/QOU/Molecular/h2_lp_dual_binding.lean:1` - placeholder-stub - ``

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
