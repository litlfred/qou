---
# qou-cp1x
title: Cross-check 1104.0755v2.pdf at computations/probes/awzero_asymptotics_probe.py
status: todo
type: task
created_at: 2026-08-08T16:13:04Z
updated_at: 2026-08-08T16:13:04Z
---

Evaluate both sides of the Theorem numerically at the substrate-relevant w and a spread of x, and check the zeros predicted by the theta factor against the tropical corners w^{1-2n} the probe computes. A mismatch would indicate the corpus's normalisation of A_w differs from Morita's; agreement independently validates the refuted-triangulation-free style of check the audit currently lacks.

**From the source**
- Theorem, §1 p.4 (proved in §4) — For all x in C*, A_{q^2}(-q^3/x^2) = (1/(q,-1;q)_infinity) * { theta(x/q) Ai_q(-x) + theta(-x/q) Ai_q(x) }, where theta is the Jacobi theta function and Ai_q the q-Painleve q-Airy function.
  Use here: An exact closed-form theta factorisation of the Ramanujan function A_q, valid for all x in C*. The corpus's Rouche argument compares A_w against a theta LIMIT obtained by recentring; this identity is the exact statement that comparison approximates, so the zero asymptotics zeta_n = w^{1-2n}(1 + O(w^n)) can be read off the theta zero lattice with the error controlled by the Ai_q factors rather than by a hand-built limit. Hypotheses check out: 0 < |q| < 1 matches the corpus's 0 < w < 1 (set q^2 = w), and the series definitions coincide exactly.

Source: `library/arxiv-1104.0755v2/1104.0755v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
