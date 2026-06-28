---
# vq25
title: 'Vacuity fix: lean/ParticleInteractions (4 defects)'
status: open
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/ParticleInteractions**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: placeholder-stub, self-assuming-projection.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/ParticleInteractions/neutron_qvalue_symbolic.lean:1` - placeholder-stub - ``
- `lean/QOU/ParticleInteractions/operator_selection_lp.lean:103` - self-assuming-projection - `operator_selection_lp`
- `lean/QOU/ParticleInteractions/parity_regime_selection.lean:78` - self-assuming-projection - `parity_regime_selection`
- `lean/QOU/ParticleInteractions/transfer_matrix_identities.lean:58` - self-assuming-projection - `transfer_matrix_identities`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
