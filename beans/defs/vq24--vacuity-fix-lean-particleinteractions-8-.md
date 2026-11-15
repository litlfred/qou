---
# vq24
title: 'Vacuity fix: lean/ParticleInteractions (8 defects)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/ParticleInteractions**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: self-assuming-projection.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/ParticleInteractions/SpectatorNormalization.lean:52` - self-assuming-projection - `SpectatorNormalization`
- `lean/QOU/ParticleInteractions/atomic_nf_witness.lean:105` - self-assuming-projection - `atomic_nf_witness`
- `lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean:84` - self-assuming-projection - `confinement_frobenius_reciprocity`
- `lean/QOU/ParticleInteractions/deuterium_derived_binding.lean:131` - self-assuming-projection - `deuterium_derived_binding`
- `lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean:57` - self-assuming-projection - `four_term_pair_nucleon`
- `lean/QOU/ParticleInteractions/ground_state_ordering.lean:64` - self-assuming-projection - `ground_state_ordering`
- `lean/QOU/ParticleInteractions/lp_dual_stability.lean:93` - self-assuming-projection - `lp_dual_stability`
- `lean/QOU/ParticleInteractions/mass_categorical_descent.lean:62` - self-assuming-projection - `mass_categorical_descent`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
