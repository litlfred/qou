---
# qou-k6g6
title: Add reference for 0610105v2.pdf at computations/deltalambda/gap10_tjon_correlation_probe.py
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:02Z
updated_at: 2026-08-15T15:02:38Z
---

The Tjon correlation is the sole scoring observable of an active probe and of a sorry-free Lean file, and has no ref() entry and no citation anywhere in the corpus.

**From the source**
- Sect. III, Figs. 3-4 — The correlation between the three-body ground-state energy and the four-body ground and excited state energies is a universal curve (a Tjon line): approximately linear outside the threshold region, with positive curvature for a > 0 and negative curvature for a < 0.
  Use here: Sources the premise of gap10_tjon_correlation_probe.py that the 3-body/4-body correlation is a genuine convention-free observable, and gives the field's own shape (linear away from threshold, curvature sign set by sign of a) against which the operator's ladder can be scored rather than only against three AME numbers.
- Sect. II (following ref. [12]) — The four-body binding energies are computed WITHOUT an independent four-body parameter at leading order; the two- and three-body inputs suffice.
  Use here: This is the external analogue of the probe's mu4 = 0 baseline (M(4) = 4 M(3) - 6 M(2), Lean tjon_deviation_eq_mu4). It is an analogue, not a proof of that baseline: the corpus's baseline is a simplex/inclusion-exclusion form on a Hecke block trace, whereas this is a zero-range EFT statement about bosons with large scattering length. Cite it as the reason a nonzero mu4 is a meaningful signal, not as a derivation of the form.

Source: `library/arxiv-nucl-th-0610105v2/0610105v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
