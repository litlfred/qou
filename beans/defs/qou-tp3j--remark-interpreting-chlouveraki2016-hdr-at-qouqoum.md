---
# qou-tp3j
title: Remark interpreting [chlouveraki2016-hdr] at qou:QOU.MassTheory.wenzl_bridge_applicability_qou
status: todo
type: task
created_at: 2026-08-08T23:35:23Z
updated_at: 2026-08-08T23:35:23Z
---

The Lean -- Ref: at wenzl-bridge-applicability-qou.lean:82/:106 cites 'HDR Theorem 6.20' without noting that the printed theorem is for Yokonuma-Hecke Y_{d,n}(q) and that the Hecke uniqueness used here is its d=1 case. Record the specialisation so a reader does not have to re-derive it from the PDF.

**From the source**
- Thm 6.20 — Unique linear Markov trace on the Yokonuma-Hecke tower Y_{d,n}(q) fixed by cyclicity, normalisation and the Markov/framing rules; at d=1 it is the Ocneanu trace on H_n(q).
  Use here: Backs the uniqueness hypothesis MarkovTraceFamilyOneDim that wenzl_bridge_applicability_qou consumes; the d=1 sentence is the exact Hecke specialisation the corpus needs.

Source: `library/hdr/HDR.pdf` (`chlouveraki2016-hdr`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
