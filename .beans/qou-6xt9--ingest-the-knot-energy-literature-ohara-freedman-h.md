---
# qou-6xt9
title: Ingest the knot-energy literature (O'Hara, Freedman-He-Wang, survey)
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T11:56:16Z
updated_at: 2026-09-13T12:41:41Z
---

## THE PREMISE WAS WRONG, AND IT WAS MY CLAIM (2026-09-13)

I sold option A as "unblocks citation for qou-bn8e", on my own finding that the
library holds no knot-energy source. The library finding is CORRECT. The
inference from it was NOT.

MEASURED: content/schema/references.ts ALREADY CARRIES BOTH PAPERS.
  ohara1991     line 5560  "Energy of a knot", Topology 30(2) 241-247, 1991
                DOI 10.1016/0040-9383(91)90010-2
  freedman1994  line 3100  "Mobius energy of knots and unknots",
                Annals of Math 139(1) 1-50, 1994, DOI 10.2307/2946626

And MobiusEnergy.lean ALREADY CITES THEM -- `-- Ref: [freedman1994]
https://doi.org/10.2307/2946626` at line 113, `Ref: [ohara1991],
[freedman1994]` at 127, plus the header bibliography at lines 30-32.

So qou-bn8e is NOT blocked on an uncitable theorem. It can cite O'Hara today
and does. This is the negatives-rule failure in AGENTS.md, one level up: I
measured the LIBRARY SURFACE and reported a conclusion about the CORPUS's
ability to cite. Those are different claims and only the first was measured.

CONTAMINATED, and corrected: the AskUserQuestion option A description
("Unblocks citation for qou-bn8e"), option B's description ("qou-bn8e stays
blocked on an uncitable theorem"), and the chat report that accompanied them.
The bean qou-pc85 body-append and PR #7284's comment say only that the library
holds no source, which is true and is NOT contaminated.

## WHAT IS ACTUALLY MISSING (both network-blocked)

1. GREPPABLE FULL TEXT in library/. Citation works; corpus-grep path 5 cannot
   see these papers, so an agent asking "does the corpus hold the knot-energy
   literature" gets a true no. Narrower value than I claimed, still real.
2. THE ohara1991 DOI IS UNVERIFIED. Its own note carries
   "HUMAN-REVIEW: unreviewed -- DOI needs verification; an alternate candidate
   DOI 10.1016/0040-9383(91)90030-7 was seen during 2026-06-08 ingestion."
   Two candidates, flagged since June, and resolving it needs exactly the
   access that is blocked.

## EGRESS ROUTE TABLE WALKED (per local/sandbox-egress route 5)

Every academic host is connect_rejected at ORGANISATION POLICY -- proxy
reports selective:false, so this is not an allowlist an agent can extend:

  arxiv.org, www.arxiv.org             000  connect_rejected
  export.arxiv.org/api                 403
  api.openalex.org                     000
  api.semanticscholar.org              000
  api.crossref.org                     000
  doi.org                              000
  www.ams.org, projecteuclid.org       000

OPEN, and probed the documented way rather than by bare host:
  github.com /info/refs?service=git-upload-pack   200
  git ls-remote                                    works
  api.github.com                                   200
    (an earlier 403 here was GitHub's own anonymous SEARCH rate limit,
     not egress -- do not record it as a block)

Route 1 (is it on GitHub?): searched. ZERO repositories; ONE code hit, a .bib
in designbynumbers/plcurve. A bib is citation metadata, which per the section
above is the half the corpus already has -- and the MCP GitHub tool is scoped
to litlfred/*, so reading it needs the anonymous git lane, not the API.
Route 2 (bundled in a pip package): N/A, these are journal PDFs.
Route 3 (data-URL env override): N/A.

## WHAT A NETWORK-OPEN ENVIRONMENT SHOULD RUN

Nothing an agent can do here. The working route is the one this corpus has
always used for PDFs (library/arxiv-0808.1533v1 and library/helicity03mmj both
arrived this way): THE OWNER DROPS THE PDFs IN uploads/, then

  python3 scripts/migrate-uploads-to-library.py

sections them into library/<doc-id>/sections/ and corpus-grep path 5 sees them.

Targets, in the order they pay off for this arc:
  1. O'Hara, "Energy of a knot", Topology 30 (1991) 241-247
     -- also settles the DOI ambiguity above
  2. Freedman-He-Wang, "Mobius energy of knots and unknots",
     Ann. of Math. 139 (1994) 1-50 -- carries the E(K) >= 2*pi*c(K)+4
     crossing bound, which is option C's most promising discriminator
  3. a survey (O'Hara's book "Energy of knots and conformal geometry", or a
     Blatt/Reiter regularity survey) for the minimiser-existence statements

BEAN STAYS OPEN -- blocked on owner upload, not on anything derivable here.

PR #7299 merged WITHOUT this item. Still blocked on owner upload into uploads/ + scripts/migrate-uploads-to-library.py. Issue #7298 reopened to carry it.
