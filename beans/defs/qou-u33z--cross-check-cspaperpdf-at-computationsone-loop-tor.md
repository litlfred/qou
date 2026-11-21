---
# qou-u33z
title: Cross-check cspaper.pdf at computations/one_loop_torsion.py
status: completed
pr: 8404
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:22Z
updated_at: 2026-11-21T14:38:56Z
parent: qou-8hur
---

Check whether the parity condition of Theorem 2 is the normalisation the corpus records as the dropped flattening monomial, by comparing the resulting ambiguity lattice against the unit-group-of-the-trace-field characterisation already recorded in one-loop-ambiguity-group.witness.json. A match would explain the observed ambiguity; a mismatch is equally informative. No external constant may be adopted either way.

**From the source**
- Theorem 2 (with the parity condition; Theorem 2.4 / Sects. 4-6) — Integral solutions satisfying a parity condition exist, and for such solutions the constant alpha of Theorem 1 is independent of the solution modulo an explicit lattice; dropping the parity condition weakens the conclusion.
  Use here: Directly addresses the corpus's live problem of a triangulation-dependent constant in the one-loop / det J chain. What would need checking before claiming more: whether Neumann's parity condition is the same normalisation as the Dimofte-Garoufalidis flattening monomial the corpus records as dropped, and whether it says anything about the multi-cusp per-cusp factor that borromean_nz_adjoint_torsion.py flags as unpinned at c >= 2. Proposed as compute-check plus remark, NOT aid-proof, because neither of those has been verified.

Source: `library/cspaper/cspaper.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/cspaper/  ->  [neumann-cspaper]
  Combinatorics of triangulations and the Chern-Simons invariant for hyperbolic 3-manifolds

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [neumann-cspaper] as the citation key when you do it.

In-progress in PR #8404 (`feat/qou-t8mi-tcgv-tiwv-u33z-u8cp-round68`, `QOU.QBeta.PoincareFalseThetaDilogPentagonRound68`, 80-dps probe `round68_poincare_false_theta_dilog_pentagon_probe.py`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8404, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-21T14:38:56Z cross-check result

Probe `computations/probes/one_loop_torsion_crosscheck_probe.py` (branch claude/expo-cite-xcheck-wave2-2026-11-21, commit 95bd2c24cdc), pre-registered, mpmath 70 dps, ALL PASS. cspaper (Dimofte-Garoufalidis, flattening conditions C1, C2): |tau| independent of the flattening choice and of the triangulation, measured on 5_2 over 8 triangulations with 4 to 6 tets: |tau(5_2)| = 1.16116273813391007312872008056, relative deviation 6.2e-71. Parity condition C3 is not needed for |tau|.

F3 resolution (the "three disagreeing |tau(4_1)|"): sqrt(3)/2 is tau_mu, 3 is tau_lambda (torsion_nu_sdp_probe labels it T_mu, which is a mislabel), sqrt(3) is the known factor-2 bug. No disagreement once the curve is named.
