---
# qou-t579
title: Cross-check gn2.pdf at computations/complex_volume_witness.py
status: completed
pr: 8397
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:37Z
updated_at: 2026-11-21T14:43:21Z
parent: qou-8hur
---

Specialize the paper's minimal relation for the 4_1 twist knot at t = -1 and compare with the SL(2,C) character-variety polynomial the corpus's complex-volume witness uses. A cross-check to run; if it disagrees, that is a finding, and if it agrees nothing external is adopted.

Source: `library/gn2/gn2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/gn2/  ->  [gelca-nagasato]
  Some results about the Kauffman bracket skein module of the twist knot exterior

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [gelca-nagasato] as the citation key when you do it.

In-progress in PR #8397 (`feat/qou-r6ki-sf0s-spds-ssly-t579-round67`, `QOU.QBeta.ModularDoubleSkeinRibbonRound67`, 80-dps probe `round67_modular_double_skein_ribbon_probe.py`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8397, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-21T14:43:21Z cross-check result

Probe `computations/probes/twist_knot_minimal_relation_character_variety_probe.py` (branch claude/expo-cite-xcheck-wave2-2026-11-21, commit 341bdb2c733), exact sympy, pre-registered.

- FINDING (source): Theorem 4 of [gelca-nagasato] as printed (checked against the PDF text layer, not only OCR) does not reproduce the paper's own §3 factorizations. The paper's Lemma 1 recursion composed with Lemma 3 does, for m = 0..5, and equals a corrected Theorem 4 for generic t (m = 2..8) with two coefficients changed: S_m(y) carries t^-6 + t^-2 x^2 (printed: minus), and S_{m-1}(y) carries (2 t^-4 + t^-8) x^2 - t^-4 (printed: 2 t^4). Lemma 7 holds for m = 0..8.
- The t = -1 factor Rt_m = S_m(y) - S_{m-1}(y) + x^2 sum S_i(y) vanishes on Riley's nonabelian component of b(3,1), b(5,3), b(7,5), b(9,7) (3_1, 4_1, 5_2, 6_1, up to mirror) with x = tr a, y = -tr(a b^-1). Decoy Rt_m + 1 is nonzero. So the paper's character-variety claim holds.
- Corpus check: the 4_1 A-polynomial in computations/probes/qbeta_substrate_meridian_branchpoint_probe.py, -m^4 + l(1 - m^2 - 2m^4 - m^6 + m^8) - l^2 m^4, vanishes on the Riley curve with l the longitude eigenvalue. Agrees.
- FINDING (bean premise): the named target computations/complex_volume_witness.py uses no character-variety polynomial, so there was nothing to compare there. The A-polynomial above is the only 4_1 character-variety object in computations/.
