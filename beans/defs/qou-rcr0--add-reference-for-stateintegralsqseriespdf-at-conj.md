---
# qou-rcr0
title: Add reference for state.integrals.qseries.pdf at conj:stokes-dt-bps-bridge
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:37Z
updated_at: 2026-08-21T17:03:54Z
---

The factorization theorem underlying the corpus's entire GK bilinear-block programme (4_1 and 5_2 both worked) has no bibliography entry, while the downstream GK and GGM papers do.

**From the source**
- Thm. 1.1 — The one-dimensional state integral I_{A,B}(b) equals a finite sum of products of a q-series and a q-tilde-series, obtained by residues from the factorized form of Phi_b, with generating series F_{A,B}(q,x).
  Use here: The theorem that licenses the bilinear block form Z = sum M B_sigma(q) B-tilde_{sigma'}(q-tilde) on which the 5_2 GK-bridge attack's 440 pre-registered entry comparisons and its block-row-selection successor are built; currently used with no citation for the factorization itself.
- Cor. 1.7 and Cor. 1.8 — Explicit q / q-tilde factorizations of the state-integral invariants of the 4_1 and 5_2 knots.
  Use here: The 4_1 and 5_2 block series the corpus's bilinear-bridge probes construct and compare against the Habiro-face targets; the corpus's gate for the 4_1 case currently cites the b=1 closed form of GK 1411.6062 instead.

Source: `library/stateintegralsqseries/state.integrals.qseries.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/stateintegralsqseries/  ->  [garoufalidis2013]
  FROM STATE INTEGRALS TO q-SERIES

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
