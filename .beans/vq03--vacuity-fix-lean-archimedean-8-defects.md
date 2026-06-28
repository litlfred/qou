---
# vq03
title: 'Vacuity fix: lean/Archimedean (8 defects)'
status: open
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/Archimedean**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: self-assuming-projection.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/Archimedean/archimedean_hartree_derivation.lean:72` - self-assuming-projection - `archimedean_hartree_derivation`
- `lean/QOU/Archimedean/beta_decay_transfer_matrix.lean:128` - self-assuming-projection - `beta_decay_transfer_matrix`
- `lean/QOU/Archimedean/borromean_hopf_energy_crossover.lean:132` - self-assuming-projection - `borromean_hopf_energy_crossover`
- `lean/QOU/Archimedean/eos_borromean_cfl.lean:165` - self-assuming-projection - `eos_borromean_cfl`
- `lean/QOU/Archimedean/genus_filtration_ideal.lean:111` - self-assuming-projection - `genus_filtration_ideal`
- `lean/QOU/Archimedean/genus_maximal_descent.lean:55` - self-assuming-projection - `genus_maximal_descent`
- `lean/QOU/Archimedean/gram_weighted_qvalue.lean:139` - self-assuming-projection - `gram_weighted_qvalue`
- `lean/QOU/Archimedean/knot_operator_selection.lean:85` - self-assuming-projection - `knot_operator_selection`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
