---
# vq28
title: 'Vacuity fix: lean/QuantumObservableUniverse (2 defects)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/QuantumObservableUniverse**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: self-assuming-projection.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/QuantumObservableUniverse/exists_axiom_1_frobenius.lean:45` - self-assuming-projection - `exists_axiom_1_frobenius`
- `lean/QOU/QuantumObservableUniverse/exists_axiom_3_chern.lean:47` - self-assuming-projection - `exists_axiom_3_chern`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
