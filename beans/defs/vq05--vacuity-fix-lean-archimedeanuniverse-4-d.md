---
# vq05
title: 'Vacuity fix: lean/ArchimedeanUniverse (4 defects)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/ArchimedeanUniverse**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: self-assuming-projection.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/ArchimedeanUniverse/brings_euler_characteristic.lean:51` - self-assuming-projection - `brings_euler_characteristic`
- `lean/QOU/ArchimedeanUniverse/brings_riemann_hurwitz.lean:53` - self-assuming-projection - `brings_riemann_hurwitz`
- `lean/QOU/ArchimedeanUniverse/heisenberg_commutator.lean:63` - self-assuming-projection - `heisenberg_commutator`
- `lean/QOU/ArchimedeanUniverse/mi_sw_cartan_reduction.lean:49` - self-assuming-projection - `mi_sw_cartan_reduction`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
