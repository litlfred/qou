---
# qou-c9uj
title: Cross-check 9612303v1.pdf at computations/gmo_meson_crosscheck.py
status: todo
pr: 8355
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:55Z
updated_at: 2026-11-21T15:15:34Z
parent: qou-8hur
---

Run the folio's own meson machinery against the charged-neutral pion splitting that defeated the single-q route, and record the result whichever way it comes out. This is a cross-check of a published negative, not an import of any number from it.

Source: `library/arxiv-hep-ph-9612303v1/9612303v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-ph-9612303v1/  ->  [kleinkreisler1996]
  The q-deformed quark model : quantum isospin and q-hadrons

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [kleinkreisler1996] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8355, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T15:15:34Z premise check (wave-2 cite/x-check drain) — NOT run, left open

The comparison was not run, because there is no current framework machinery to run.

- The named target, computations/gmo_meson_crosscheck.py, is marked SUPERSEDED 2026-08-07 in its own docstring (the GMO comparison is a category error: gmo_identity in QOU/Eightfold/GellMannOkuboIdentity.lean shows GMO cannot discriminate, and the 3.3% figure is a quantum dimension, not a mass splitting).
- The corpus has no derived pi+/pi0 splitting term. The nearest is computations/meson_em_residual_alpha_em.py, an order-of-magnitude EM estimate built on hadronic scales (f_pi, the condensate) and the measured 134.9768 MeV. That is imported data, not a framework prediction, so running it against the paper's negative would compare two non-derivations.
- Owner ruling 2026-11-16 (re-confirmed 2026-11-21): virtual photons do not exist in QOU. The textbook pi+/pi0 splitting is an EM self-energy (virtual-photon exchange), so any framework route must first be recast as prior entangled photons or unseen intermediary emitters. No such route exists yet.
- What the source gives the corpus now: [kleinkreisler1996] shows that a single q of U_q(sl2) on the isospin doublet cannot fit the charged-neutral pion splitting. The corpus also has one substrate q0, so any future route that puts this splitting into a U_q(sl2) isospin deformation at q0 alone meets the same negative. That is a constraint on routes, not a test of a prediction.
- Unblocks when: a derived isospin-splitting term exists for the meson sector, consistent with the no-virtual-photon ruling.
