---
# vq07
title: 'Vacuity fix: lean/BraidKnot (8 defects)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T00:00:00Z
updated_at: 2026-06-28T00:00:00Z
parent: vqep
---

Fix the genuine vacuity defects in **lean/BraidKnot**. Follow `docs/audits/vacuity-fix-playbook.md` (env, the 3 verified fix patterns, mandatory verify loop). Categories: trivial-true.

Pattern guide: self-assuming-projection -> try **B** (genuine-formalize via Mathlib) else **C** (name `def : Prop`); trivial-true -> **A** (derive the real computable prop) else **C**; placeholder-stub -> real formalisation/ref else A/C.

Files (file:line - category - decl):
- `lean/QOU/BraidKnot/BraneTowerNStar.lean:202` - trivial-true - `betaDecayRecoveryTarget_1ppb_remains_conjectural`
- `lean/QOU/BraidKnot/IwahoriHeckeAPI.lean:239` - trivial-true - `wedderburn_decomposition_generic`
- `lean/QOU/BraidKnot/Li2qUniqueness.lean:64` - trivial-true - `briggs_klein_is_neg_li2q`
- `lean/QOU/BraidKnot/Li2qUniqueness.lean:104` - trivial-true - `li2q_unique_from_ftc`
- `lean/QOU/BraidKnot/QBetaCategoricalPrecisionLadder.lean:363` - trivial-true - `qbeta_inductive_categorical_closure_conjecture`
- `lean/QOU/BraidKnot/QSchurWeightsGeneral.lean:54` - trivial-true - `contentSum_add_cell`
- `lean/QOU/BraidKnot/QSchurWeightsGeneral.lean:74` - trivial-true - `qSchur_weight_by_induction`
- `lean/QOU/BraidKnot/QSchurWeightsGeneral.lean:85` - trivial-true - `qSchur_normalisation`

**Done when:** every file `lake build <Module>` green AND vacuity audit 0 flags; commit + push to `claude/ree-epsilon-lean-explain-knl2p0`.
