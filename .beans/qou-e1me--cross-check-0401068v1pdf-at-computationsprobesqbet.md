---
# qou-e1me
title: Cross-check 0401068v1.pdf at computations/probes/qbeta_nz_even_series_fourone_probe.py
status: todo
type: task
priority: normal
created_at: 2026-08-08T16:12:45Z
updated_at: 2026-08-21T17:04:53Z
---

The probe's tau extraction currently reads the CCGLS A-polynomial without a cited value; check the probe's A_{4_1} against Takata's A_{K_{-1}} seed coefficient-by-coefficient.

**From the source**
- Thm 3.1 (quoting Hoste-Shanahan), eqs. after (6) — A_{K_p}(l,m) obeys the two-term recursion A_{K_p} = c A_{K_{p-1}} - d A_{K_{p-2}} with c = -l + l^2 + 2lm^2 + m^4 + 2lm^4 + l^2 m^4 + 2lm^6 + m^8 - lm^8, d = m^4 (l+m^2)^4, and explicit seeds A_{K_1} = l + m^6 (trefoil), A_{K_{-1}} = -l + lm^2 + m^4 + 2lm^4 + l^2 m^4 + lm^6 - lm^8 (figure-eight).
  Use here: Independent published source for the 4_1 A-polynomial that qbeta_nz_even_series_fourone_probe.py uses to recognise the leading longitude coefficient tau = (0, -+1, 1); lets the probe cite a value instead of asserting it, and supplies the whole twist-knot family if the tau extraction is ever run past 4_1.

Source: `library/arxiv-math-0401068v1/0401068v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0401068v1/  ->  [takata2004]
  THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [takata2004] as the citation key when you do it.
