
## Result (2026-06-23, session nifty-cerf, PR #2649)

Actionable 22 → **12** via two background bib-verification agents over
references.ts. Full sourced findings: docs/audits/2026-06-23-bibliography-doi-verification-doth.md.

**Resolved (10):** chlouveraki2016-hdr (title + HAL URL tel-01411063);
faddeev1995 (title finding — entry data was already correct);
halverson_ram_1998 (year 1998→1996); bertsimas1997/majid1995/murasugi1996
(ISBN confirmed); abel1826/frobenius1898/rogers1907/klein1884 (pre-DOI
archival — PLACEHOLDER was mislabeled, reworded to settled).

**HIGH-VALUE BUGS FOUND (await author decision, 12 remaining markers):**
- kashiwara1990-cmp2 DOI BF02100009 → resolves to a **WITTEN** paper; correct
  is Kashiwara DMJ 73(2) 1994, DOI 10.1215/S0012-7094-94-07317-1.
- kashiwara1990-duke DOI is a spurious 1990 vol-61 slot; correct is Kashiwara
  DMJ 71 (1993) 839–858, DOI 10.1215/S0012-7094-93-07131-1.
  (Both also appear inline in 3 .lean files — needs coordinated sync.)
- wenzl1988b DOI BF01393839 → a number-theory regulator paper (not Wenzl);
  correct Wenzl DOI not found. wenzl1988c BF01388470 → unresolved.
- carter-leal-saliola-2000 is actually single-author R. J. Marsh (id is a
  misidentification; used as a cite key in 2 files).
- pawlowski-leitner-rep UNVERIFIED (no citable id); sibling leitnerpawloski2004
  also mis-recorded (math/0409565 = Unital Grobner Bases, Leitner & R. Pawloski).
- drinfeld1985/habiro2000/james1984 — not re-verified this session / edition
  ambiguity (kept flagged honestly).

CAVEAT: sandbox 403-blocked all DOI landing pages; confirmations are
link-title-level. Resolve DOIs directly before any swap lands. Pending human close.

## Update (2026-06-24) — author-authorized A+B+C applied; 12 → 9

Author OK'd Groups A (Kashiwara DOI fixes + .lean sync), B (carter→marsh2000),
and supplied arXiv math/0409565 for C. Kashiwara cmp2's DOI was resolving to a
Witten paper; both corrected. carter-leal-saliola renamed to marsh2000 (single
author R. J. Marsh). leitnerpawloski2004's fabricated title fixed to "Unital
Gröbner Bases…" (corpus + local PDF verified); pawlowski-leitner-rep kept flagged
(PDF-verified NOT math/0409565). 9 markers remain (off-sandbox DOI resolution /
author input). See docs/audits/2026-06-23-bibliography-doi-verification-doth.md.

## Update (2026-06-24) — pawlowski-leitner-rep agent-mistake corrected; 9 → 7

Author clarified there is one Pawloski-Leitner paper (the uploads arXiv =
math/0409565 = leitnerpawloski2004); pawlowski-leitner-rep was a fabricated
split. Rewired its citations to leitnerpawloski2004, fixed 6 wrong-title inline
.lean comments, deprecated the stub entry + ledger. wenzl1988b/c kept (real,
widely-cited; only DOIs wrong). schema actionable 7 remain (off-sandbox DOI /
author input).
