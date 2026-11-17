---
# qou-0seq
title: Cross-check 1992EvansBerger.pdf at computations/deltalambda/mixed_multibond_mubar_integrality_pro…
status: in-progress
pr: 8347
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:06Z
updated_at: 2026-10-04T15:18:19Z
parent: qou-8hur
---

Evaluate Psi_ijk on the corpus's own Borromean braid word (sigma_1 sigma_2^{-1})^3 and on a mixed Hopf+Borromean multibond configuration, and compare with the mu-bar values the Magnus machinery already produces. This is a cross-check, not an adoption: any agreement is evidence about the construction, not a licence to wire a number.

**From the source**
- eq. (21)-(22), p. 6 — The one-form psi_ijk = lambda_ij d lambda_jk + lambda_jk d lambda_ki + lambda_ki d lambda_ij is closed by the Arnol'd relation, so Psi_ijk = Re integral over gamma of psi_ijk is a homotopy-invariant third-order winding number of a 3-string braid, well defined whether or not the net second-order winding numbers vanish.
  Use here: A braid-level third-order invariant that is NOT killed by a Hopf-linked spectator, unlike the mu-bar residue that MilnorIndeterminacyGate.lean collapses to ZMod 1. It is the natural candidate for the mixed-multibond shared channel that the mu-bar-idempotent probe refuted, and it lives on braid words, which is what the corpus actually manipulates.

Source: `library/1992evansberger/1992EvansBerger.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/1992evansberger/  ->  [evans-berger1992]
  A Hierarchy of Linking Integrals

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [evans-berger1992] as the citation key when you do it.
