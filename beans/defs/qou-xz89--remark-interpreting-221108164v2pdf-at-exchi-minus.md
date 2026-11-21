---
# qou-xz89
title: Remark interpreting 2211.08164v2.pdf at ex:chi-minus-six-derivation
status: completed
pr: 8435
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:21Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-aqfj
---

Step 5's parenthetical ('S_3 subset S_5 orbits on the 6 Weierstrass points of Bring's surface') is inconsistent with transitivity + simplicity (one orbit, 60 points) and with the corpus's own 2026-07-18 audit line recording 60 weight-1 Aut-transitive Weierstrass points. Flagged as needing author adjudication of what the 6 actually counts; not proposed as an automatic edit and not a claim that chi(A) = -6 is wrong.

**From the source**
- Thm 2 (Sec 4, p. 6-7); intro item (3), p. 1 — For g > 2 with simple Weierstrass points, Aut(X) acts transitively on the Weierstrass points iff g = 4 and X is Bring's curve, or g = 3 and X is C_t for some t != 0, 3; and Bring's curve is listed with Klein's quartic and Macbeath's curve among the classically known transitive examples.
  Use here: Supplies the missing source for Step 7 of ex:chi-minus-six-derivation ('the unique maximally symmetric genus-4 curve is Bring's surface') in a precise, checkable form, and simultaneously fixes the orbit structure Step 5 appeals to: transitive + simple means one orbit of 60, not an S_3-orbit decomposition of 6.
- Sec 4, remark following Thm 2 (p. 7) citing Edge, J. London Math. Soc. 18 (1978) 539-545, and Braden-Disney-Hogg arXiv:2208.13692 Sec 3.1 — The Weierstrass points of Bring's curve were determined by Edge; see also Braden-Disney-Hogg Sec 3.1.
  Use here: Names the primary source (Edge 1978) for the Bring Weierstrass-point set, which is the datum ex:chi-minus-six-derivation Step 5 is implicitly using; Braden-Disney-Hogg is already digested in the 2026-07-18 audit, so the two independently agree.

Source: `library/arxiv-2211.08164v2/2211.08164v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2211.08164v2/  ->  [reyescarocca2022]
  INFINITELY MANY RIEMANN SURFACES WITH A TRANSITIVE ACTION ON THE WEIERSTRASS POINTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [reyescarocca2022] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8435, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T13:00:00Z expo-remarks drain

Verified on main 2ae54ab40: already addressed on main (cite present at ex:chi-minus-six-derivation). Close as completed. Superseded-premise check: none found.
