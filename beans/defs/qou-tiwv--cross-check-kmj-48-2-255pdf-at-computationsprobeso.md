---
# qou-tiwv
title: Cross-check KMJ-48-2-255.pdf at computations/probes/one_loop_ohtsuki_5_2_crosscheck_probe.py
status: in-progress
pr: 8404
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:58Z
updated_at: 2026-11-18T15:18:29Z
parent: qou-8hur
---

Evaluate the explicit two-bridge formula for 5_2 = S(7,3) and compare with the corpus's existing 5_2 cross-check probe. This verifies an existing witness with an independent formula; no external number is adopted, and a disagreement is the finding.

**From the source**
- Sec. 1 and the main formula for J_{S(p,t)}(n) — An explicit formula is given for the colored Jones polynomial of the 2-bridge knot S(p,t) in Schubert notation, specialising to a more explicit form for twist knots.
  Use here: Enables a direct colored-Jones computation for 5_2 and 6_2 -- the corpus's one-loop cross-check knot and its deuteron closure -- where the corpus currently has only a literature dependency and no compute.

Source: `library/kmj-48-2-255/KMJ-48-2-255.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/kmj-48-2-255/  ->  [takata2008]
  A formula for the colored Jones polynomial of 2-bridge knots

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [takata2008] as the citation key when you do it.

In-progress in PR #8404 (`feat/qou-t8mi-tcgv-tiwv-u33z-u8cp-round68`, `QOU.QBeta.PoincareFalseThetaDilogPentagonRound68`, 80-dps probe `round68_poincare_false_theta_dilog_pentagon_probe.py`).
