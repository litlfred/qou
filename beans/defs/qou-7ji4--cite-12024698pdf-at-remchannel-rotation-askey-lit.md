---
# qou-7ji4
title: Cite 1202.4698.pdf at rem:channel-rotation-askey-lit
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:51Z
updated_at: 2026-10-10T07:26:04Z
parent: qou-19m0
---

rem:channel-rotation-askey-lit item 2 currently supports the b <-> 1/b 6j-level rotation claim with the 2001 Clebsch-Gordan/Racah paper alone; the normalisation-fixed b-6j symbol and its new integral representations belong at the same sentence.

**From the source**
- Sec 2 (normalisations) with eq (2.28) and Appendix B; second derivation in Sec 5, eq (5.17) — Natural normalisation conditions for the b-6j symbol are identified -- one of them shown to define a quantisation of Fenchel-Nielsen coordinates -- and new integral representations are derived from Spiridonov elliptic hypergeometric identities; Sec 5 then re-derives the volume asymptotics as the generating function of the canonical transformation between the (l_s, k_s) and (l_t, k_t) Darboux coordinates.
  Use here: rem:channel-rotation-askey-lit item 2 asserts that 'the map b <-> 1/b drives the 6j-level rotation' and that this is what divides Phi_q (Faddeev, non-compact) from Li_2^q (Rogers, compact), citing only `ponsot-teschner2001`. This supplies the normalisation-fixed version of that 6j object plus a second, coordinate-change derivation of its classical limit -- the natural companion citation at the same sentence.

Source: `library/arxiv-1202.4698v3/1202.4698.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1202.4698v3/  ->  [terashima-yamazaki2013]
  6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [terashima-yamazaki2013] as the citation key when you do it.


## 2026-10-10 — pointer

Tracked under carrier M14 (qou-9w2m) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## 2026-10-10 — Done in issue litlfred/qou#7552: `channel-rotation-askey-lit.md` item 2 cites `\cite[\S2.1, \S2.3]{terashima-yamazaki2013}` for the b <-> 1/b self-duality, and notes the source writes q~ = e^{+i pi/b^2}, the complex conjugate of the block's. The entry's AUTHORS were wrong: the held PDF is J. Teschner and G. S. Vartanov; corrected in references.ts, id kept.
