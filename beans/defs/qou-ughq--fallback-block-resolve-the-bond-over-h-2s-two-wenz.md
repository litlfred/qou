---
# qou-ughq
title: 'Fallback: block-resolve the bond over H_2''s two Wenzl blocks (3S1 vs 1S0)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T06:48:04Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---


**FALLBACK.** Opened 2026-09-04 alongside `qou-oooq` (tower) and `qou-onfk`
(saturation), to be picked up only if those fail.

`H_2` under convention D has exactly two blocks, `(2)` and `(1,1)` — symmetric
and antisymmetric. That is precisely the `3S1` / `1S0` split: Pauli lets
identical nucleons use only one channel, while `pn` can use both. The current
bond constant Wenzl-averages over them,

    tr_2(sigma + d) = w+ (q + d) + w- (-1/q + d),   w+ = [3]_q/([3]_q+1),

collapsing the channel structure into a scalar. The relaxation keeps a 2-vector
per bond instead.

The two blocks order OPPOSITELY in `d` (block `(2)` gives `q + d`, block `(1,1)`
gives `-1/q + d`), so the freedom to put `pn` at an extreme genuinely exists
here, unlike in the averaged scalar.

## Why it is a fallback and not the lead

**The Wenzl weights are what make the functional a Markov trace.** Dropping them
very likely forfeits the Markov property, and with it every link-invariant
statement in the corpus — the connected-sum theorem, Jones factorisation, the
whole `qou-m3sh` arc. That is a large price for an isospin channel, and it
should only be paid if `qou-oooq` and `qou-onfk` both fail.

- [ ] Determine whether a block-resolved bond can preserve the Markov property
      at all, or whether the two are strictly incompatible. If incompatible,
      close this bean negative immediately — the price is not payable.
- [ ] Only if compatible: check whether `pn` can be made extremal.

## Implementation & Witness Progress (PR #8261)
- Branch: `qou-10v9-d5e8-lq6k-tqfm-ughq-vvv4` (`215564fea0bbd17193637e08e9f87df6e0ac73b7`), PR: `litlfred/qou#8261`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/BoltzmannExtensivityMilnorAntisymmetryShiftInertnessWenzlMarkovLockAndHadronicMeltOrdering.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/boltzmann_extensivity_milnor_antisymmetry_shift_inertness_wenzl_markov_lock_and_hadronic_melt_ordering_probe.py` -> `computations/probes/boltzmann-extensivity-milnor-antisymmetry-shift-inertness-wenzl-markov-lock-and-hadronic-melt-ordering.witness.json` (`allPassed: true`, `scriptHash: 6d6a6f5a2d13`, `scriptCommitSha: 83f7ff931c7cc699e6338421bf57c15a92f557d2`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8261, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
