---
# qou-8ava
title: 'GAP: what is a ''polarization generator''? (sigma0,sigma1) is not an orthogonal pair under any H3 automorphism'
status: todo
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:24:51Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u (owner D1), PR #7825, QOU/StandardModel/PolarizationActionHecke.lean. Proved: SU(2) acts transitively on orthogonal polarization pairs (cone, orth_pair_eq_leftMul_std). Conjugation in the (2,1) block of H3 is an inner automorphism preserving the Hecke and braid relations, and moves the q/-q^-1 eigenline pair of ONE letter to any pair. But generators attached to (v, v-perp) commute (eigenAxis_commute), sigma0 and sigma1 do not (s_noncomm), so no automorphism sends (sigma0,sigma1) to an orthogonal pair (no_automorphism_to_orthogonal_pair, scope (b) given the modelling step). Their q-lines sit at Bloch cos = -(q^4+1)/(q^2+1)^2 (120 deg at q=1). The linear mix a sigma0 + b sigma1 satisfies the Hecke quadratic only for (1,0),(0,1) (L+-/L- coefficients force ab=0). OPEN: the BW block's 'horizontal/vertical = sigma0/sigma1' reading has no derivation; the derivable polarization pair is the L/R eigenline pair of a single letter.

## Progress (PR #8443)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/BarParityReadoutPartitionWeightBraidedTraceSurfaceGenusPolarizationPair.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_2djn_2joi_4khc_51l1_8ava_probe.witness.json` (`Commit 1` = `76eb5ed3bb589e3c0713062c1916ff3df6e16b60`, `HEAD` = `bd4d50a998e0b0519e966f309ff7ef17c810abac`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8443, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
