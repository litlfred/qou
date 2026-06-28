---
# vq27
title: 'Vacuity fix: lean/QOU-root (8 defects)'
status: open
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/QOU-root**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: self-assuming-projection, trivial-true.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/MassComputationChainRoadmap.lean:327` - trivial-true - `frobenius_co_casimir_universal_high_n`
- `lean/QOU/MassComputationChainRoadmap.lean:353` - trivial-true - `wenzl_bridge_atomic_tr_M`
- `lean/QOU/MassDerivation.lean:73` - self-assuming-projection - `topological_mass_formula`
- `lean/QOU/MathlibExt.lean:134` - self-assuming-projection - `List.prod_eq_of_perm`
- `lean/QOU/PhotonThreading.lean:91` - trivial-true - `crossing_energy_gauge_invariant`
- `lean/QOU/orbital_fourier_decomposition.lean:121` - self-assuming-projection - `orbital_fourier_decomposition`
- `lean/QOU/qou_canonical_action.lean:105` - self-assuming-projection - `qou_canonical_action`
- `lean/QOU/variational_equations.lean:107` - self-assuming-projection - `variational_equations`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
