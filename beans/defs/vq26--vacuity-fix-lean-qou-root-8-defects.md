---
# vq26
title: 'Vacuity fix: lean/QOU-root (8 defects)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/QOU-root**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: trivial-true.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/LightningPath.lean:76` - trivial-true - `lightning_path_synthesis`
- `lean/QOU/MassComputationChainRoadmap.lean:142` - trivial-true - `additive_wedderburn_recurrence_matches_std_rep_trace`
- `lean/QOU/MassComputationChainRoadmap.lean:168` - trivial-true - `typed_crossings_encoding_unique`
- `lean/QOU/MassComputationChainRoadmap.lean:188` - trivial-true - `phi_q_converges_absolutely`
- `lean/QOU/MassComputationChainRoadmap.lean:218` - trivial-true - `n_star_existence_conjecture`
- `lean/QOU/MassComputationChainRoadmap.lean:241` - trivial-true - `wedderburn_weights_H3`
- `lean/QOU/MassComputationChainRoadmap.lean:294` - trivial-true - `per_nucleon_shift_additive`
- `lean/QOU/MassComputationChainRoadmap.lean:304` - trivial-true - `per_nucleon_shift_at_A1`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
