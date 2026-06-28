---
# vq29
title: 'Vacuity fix: mass-theory (7 defects)'
status: open
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **mass-theory**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: trivial-true.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `mass-theory/atom-knot-mass-derivation-proof.lean:24` - trivial-true - `categorical_leg_to_markov_trace`
- `mass-theory/atom-knot-mass-derivation-proof.lean:36` - trivial-true - `archimedean_realization_to_mev`
- `mass-theory/atom-knot-mass-derivation-proof.lean:45` - trivial-true - `post_archimedean_naming_borrowed`
- `mass-theory/atom-knot-mass-derivation-proof.lean:63` - trivial-true - `atom_knot_mass_derivation_proof`
- `mass-theory/eigenvalue-product-expansion.lean:33` - trivial-true - `geometric_sum_is_qint`
- `mass-theory/markov-trace-product.lean:274` - trivial-true - `degree_bound`
- `mass-theory/vertex-is-exceptional-divisor.lean:33` - trivial-true - `vertex_is_exceptional_divisor`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
