---
# qou-lsp9
title: 'GAP: wire the net(T(2,n)) -> lepton mass map. Corpus assigns T(2,n) to generations but the Morgan-Voyce net is a normal-form coefficient, NOT a mass: net ratios 1.2455 and 1.2408 vs observed 206.8 and 16.8. Until wired, the ladder has no predictive content at n=9 to test against the LEP no-4th-lepton bound. Prerequisite to any numerical falsification.'
status: todo
pr: 8196
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-08-01T22:05:54Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

## Second pass, 2026-08-07 — generalised, and the premise corrected

Audit: `docs/audits/2026-08-07-lepton-linear-readout-rigidity.md`.
Probe: `computations/lepton_linear_readout_rigidity.py`.
Lean (sorry-free, lean-direct exit 0): `lepton_continuant_binet.lean`.

**Closed (scope-(b)).** Not just the net — EVERY *positive* linear
readout of H_2(q). The algebra is 2-dimensional, so any functional is
phi(sigma_0^w) = alpha*b_{w-1} + beta*b_w; all of them obey one two-step
law phi(n+2) = q^2 phi(n) + (-1)^n h B q^{-n} with B = alpha - beta/q, so
the (alpha,beta) choice rescales the vanishing remainder and never the
q^2. The CANONICAL Markov trace (alpha,beta) = (1, z) is included: bend
1.0394 against an observed 12.295, needing p = 64.94 to match.

**The one escape, and why it is shut.** A readout with a node just below
the electron winding CAN reproduce 206.8 -- so "no linear readout works"
is false as a bare claim. Solved exactly (quadratic in u = A/B): both
roots need beta/alpha < 0, i.e. phi(1) and phi(sigma_0) of opposite sign.
For q > 1 the continuant is positive from b_1 on, so any readout with
alpha >= 0, beta > 0 has no node at all. No trace supplies a
sign-indefinite readout. Lean: linFunctionalK_pos / markovReadout_pos.

**Premise correction (this bean's own justification was wrong).** This
bean says the mass map is a "prerequisite to any numerical falsification"
against the LEP bound. It is not. N_nu = 2.984 +/- 0.008 is a COUNT, and
the corpus's generation-count derivation (b_3 | b_9, sorry-free) is a
count prediction -- comparing 3 against 2.984 needs no mass map. The
no-4th-charged-lepton leg needs none either if the count is 3. The count
prediction is gated on the PHYSICAL BRIDGE ("normal-form-independent
winding => physical generation"), which is qou-x4qm's residual gap, NOT
on this bean. The mass map is still wanted for quantitative lepton-mass
predictions; it is not the load-bearing gate on the falsification.

**Still open.** A mass map itself. Live direction is qou-htk4: a
non-H_2-linear bridge (additive interface term, or linking/satellite
coupling T(2,n) to the hyperbolic Higgs knot 4_1). Left `todo`
deliberately -- a class was excluded, the goal was not achieved.

## Progress (2026-11-16, PR #8196)
- [x] Formalized `twoStepReadout`, `nextRecurrenceTerm`, `two_step_recurrence_expansion`, `twoStepReadout_pos_of_nonneg_weights`, and `node_requires_negative_alpha` in `folio/quantum-observable-universe/lean/QOU/Eightfold/LeptonReadoutHiggsScaleMesonSyllableAndIcosahedralOrbit.lean` + 50-dps mpmath witness (`qou_lsp9_two_step_readout_and_node_sign`) in PR #8196 (`38b68fa660bb34e2ffb7a2e1a09e5c4f5308e2cf`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8196, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-07: "lean(qou-lsp9): positivity closes the node escape the rigidity law leaves open"). The work may be partly or fully done. Read the bean before you close it.
