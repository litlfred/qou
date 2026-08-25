---
# qou-07m1
title: Cross-check 2302.08363v2.pdf at computations/probes/fourone_stokes_series_selfcheck.py
status: todo
type: task
priority: normal
created_at: 2026-08-09T00:10:49Z
updated_at: 2026-08-21T17:04:38Z
---

Extend the existing 4_1 Stokes-series self-check with the independently published eq (4.5) coefficients and record the verified relation M_1 = g_0 * 2G_0 through q^4 (and the absence of a comparable form for M_2). Cross-check only; nothing to wire, and the relation is a consistency test between two sources' notations, not a QOU observable.

**From the source**
- Sec 4, eq (4.5) — M_1(q) = 1 - 8q - 9q^2 + 18q^3 + 46q^4 + O(q^5) and M_2(q) = -9q - 3q^2 + 39q^3 + 69q^4 + O(q^5), the power series in q~ multiplying the two 4_1 instanton towers, stated to be convergent with radius of convergence R = 1 and with exact expressions attributed to its ref [41].
  Use here: Independent published values for the same 4_1 object that computations/probes/fourone_stokes_series_selfcheck.py already self-checks from the `fantini-wheeler2024` eq (74) blocks g_0(q) = 1 - q - 2q^2 - 2q^3 - 2q^4 + ... and 2G_0(q) = 1 - 7q - 14q^2 - 8q^3 - 2q^4 + ... . Verified during this triage by exact rational power-series arithmetic: M_1 = g_0 * 2G_0 exactly through the printed order q^4 (product coefficients 1, -8, -9, 18, 46 reproduce eq (4.5) term by term). M_2 has no comparable factorisation at this order: M_2/g_0 = -9q - 12q^2 + 9q^3 + 36q^4, M_2/(g_0 * 2G_0) = -9q - 75q^2 - 642q^3 - 5580q^4. This turns the existing single-source self-check into a genuine cross-source consistency test between two independent papers' notations for the 4_1 Stokes data. Scope: 4 non-trivial coefficients matched, which is evidence of the identity, not a proof of it.

Source: `library/arxiv-2302.08363v2/2302.08363v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2302.08363v2/  ->  [arxiv-2302.08363v2]
  On the structure of trans-series in quantum field theory

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-2302.08363v2] as the citation key when you do it.
