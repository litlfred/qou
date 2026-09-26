---
# qou-mre6
title: Cross-check [braden-northover-2012] at QOU.Archimedean.BringHauptmodulGate
status: todo
type: task
created_at: 2026-08-08T23:34:52Z
updated_at: 2026-08-08T23:34:52Z
---

This document gives tau_0 ~ -0.5 + 0.185576i while BringHauptmodulGate.lean:41 records -0.5 + 0.186676i from braden-disney-hogg-2022. Determine which is the corrected value and note the supersession in the Lean, so the gate's numeric context does not silently carry two different tau_0.

**From the source**
- eq. (4.3) + footnote 5, §4 — tau_0 is defined by j(tau_0) = -29^3 x 5/2^5 = -121945/32 and j(5 tau_0) = -25/2; the earlier literature swaps these two equations, which the authors believe to be a typographical error.
  Use here: The corrected labelling the Bring hauptmodul gate depends on, and the source of the -121945/32 constant in its exact-rational sextic-root theorem.

Source: `library/sigma12-065/sigma12-065.pdf` (`braden-northover-2012`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
