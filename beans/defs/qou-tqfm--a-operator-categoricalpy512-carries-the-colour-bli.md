---
# qou-tqfm
title: a_operator_categorical.py:512 carries the colour-blind -h/2 under an I_pn label
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T22:07:20Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

3dcf933c5d colour-weighted the physical p-n interface (-h/2 -> -h(1-delta/4)/2) at five sites in a_operator_gauge_align.py. Two consumer sites were missed. One (cyclic_intertwiner_verify.py:67) was a real bug and is fixed in the branch claude/cyclic-intertwiner-colour-blind-interface-2026-08-23. The other, a_operator_categorical.py:512 inside verify_operator_decomposition_exact, is MEASURED INERT: that function uses I_iface on both sides of its own comparison, so the assertion operator_interface_decomposition_exact_1e-25 passes at 1.8495342e-49 whatever shift is used. Left unedited rather than making a change with no observable effect. The label is nevertheless wrong by 3dcf933c5d's own stated criterion (it says I_pn is the physical p-n bridge and must carry the colour weighting), so it is a latent inconsistency: if that operator ever becomes load-bearing, it disagrees with every other p-n interface in the subsystem. Decide: align the constant (no numeric effect today), or relabel it as a shift-agnostic test operator.

## Implementation & Witness Progress (PR #8261)
- Branch: `qou-10v9-d5e8-lq6k-tqfm-ughq-vvv4` (`215564fea0bbd17193637e08e9f87df6e0ac73b7`), PR: `litlfred/qou#8261`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/BoltzmannExtensivityMilnorAntisymmetryShiftInertnessWenzlMarkovLockAndHadronicMeltOrdering.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/boltzmann_extensivity_milnor_antisymmetry_shift_inertness_wenzl_markov_lock_and_hadronic_melt_ordering_probe.py` -> `computations/probes/boltzmann-extensivity-milnor-antisymmetry-shift-inertness-wenzl-markov-lock-and-hadronic-melt-ordering.witness.json` (`allPassed: true`, `scriptHash: 6d6a6f5a2d13`, `scriptCommitSha: 83f7ff931c7cc699e6338421bf57c15a92f557d2`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8261, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
