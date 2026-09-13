---
# qou-6xt9
title: Ingest the knot-energy literature (O'Hara, Freedman-He-Wang, survey)
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T11:56:16Z
updated_at: 2026-09-13T14:52:46Z
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


## LARGELY RESOLVED 2026-09-13 — owner uploaded, ingest run, DOI settled

Owner dropped 13 PDFs in uploads/ (commit 29880e8900). Both pipeline steps
run clean: pdf-structure.py 13 ok / 0 failed; migrate-uploads-to-library.py
--selftest PASS, --apply moved 13, --verify reports 0 library dirs without
structure.json and 0 PDFs left flat.

DELIVERED, both halves this bean existed for:

1. GREPPABLE FULL TEXT. Path 5 previously returned ZERO on this arc's own
   subject. It now returns 13 files for "energy of a knot", 9 for
   "Möbius energy", 2 for "Palais-Smale", 9 for "self-repulsive".
   O'Hara 1991 plus ten modern regularity/existence papers, including
   "On the Palais-Smale condition in geometric knot theory" — which is the
   minimiser-existence gate option C could not stateimi.

2. THE ohara1991 DOI IS SETTLED, against the full text rather than a
   registry. The PDF is the Elsevier export for PII 0040938391900102 =
   10.1016/0040-9383(91)90010-2; page 1 reads ENERGY OF A KNOT / JUN
   O'HARA, 7 pages, matching Topology 30(2) 241-247. The recorded DOI is
   RIGHT; the alternate candidate ...(91)90030-7 is WRONG and is dropped
   with a do-not-reinstate note. HUMAN-REVIEW flag cleared after 3 months.

## 🛑 WHY THIS STAYS OPEN: FREEDMAN-HE-WANG 1994 WAS NOT UPLOADED

No Annals of Mathematics PDF is among the 13. So the crossing bound
E(K) >= 2*pi*c(K)+4 still has no full text here. Its CITATION works and is
unaffected (freedman1994, DOI 10.2307/2946626, not flagged) — only the
text is missing.

Scope that honestly: the bound is NOT statable against LinkEmbedding today
regardless, because that structure carries no crossing number, so a Lean
statement of it would be true by vacuity. FHW's text is therefore wanted
for READING, not for an immediate formalisation. Low urgency; the bean
stays open so it is not forgotten.

Candidate source if wanted: https://www.jstor.org/stable/2946626

## FINDING THAT CAME OUT OF THE ACCEPTANCE TEST

Taxonomy row 41: corpus-grep path 5 typed in ASCII misses typographic
Unicode, BIDIRECTIONALLY. `O'Hara` ASCII 0 vs Unicode 48; but `Poincare`
ASCII 190 vs Unicode 145, where ASCII wins. Search both forms; do not
normalise one way. My first reading (`use Unicode`) was wrong and the row
records it.


## 🟩 THE FHW CROSSING BOUND IS NOW IN THE LIBRARY — via the BAMS announcement

This bean stays open on one item: *"FREEDMAN-HE-WANG 1994 WAS NOT UPLOADED … the
crossing bound `E(K) ≥ 2πc(K)+4` still has no full text here."*

**The bound is now here.** The owner's second drop (2026-09-13 14:42, 7 PDFs)
includes `arxiv-math-9301212v1` =

> **Bryson, Freedman, He & Wang, "Möbius Invariance of Knot Energy",
> Bull. Amer. Math. Soc. 28(1), January 1993, 99–103.**

Its **Theorem D** is verbatim the bound this bean wants, quoted from the ingested
section text:

```
Theorem D. If γ is topologically tame, let c([γ]) denote the (topological) crossing
          2πc([γ]) + 4 ≤ E(γ).
Since an essential knot must have three or more crossings, we obtain the following…
          c([γ]) ≤ c(γ) ≤ E(γ)/2π
```

The abstract also delivers this bean's **target 3** (minimiser-existence
statements): *"round circles are precisely the absolute minima for energy; there
is a minimum energy threshold below which knotting cannot occur; minimizers
within prime knot types exist and are regular"*, plus the estimate on the number
of knot types below energy `M`.

### 🛑 Scope it honestly — this is the ANNOUNCEMENT, not the Annals paper

`math/9301212v1` is **5 pages** and announces results; Freedman–He–Wang, *Möbius
energy of knots and unknots*, Ann. of Math. **139** (1994) 1–50 is **50 pages**
and carries the proofs. So:

* **Reading and citing the bound: unblocked.** Theorem D is stated, with its
  corollaries, in greppable text.
* **The proof of the bound: still not held.** If this arc ever needs to follow
  the argument rather than invoke the statement, the Annals paper is still
  wanted (`https://www.jstor.org/stable/2946626`).

**Left open deliberately**, for two reasons: the distinction above is real, and
this is your bean — the stated blocker ("blocked on owner upload") is discharged
but the Annals text is not here, so the close is yours to call, not mine.

### Also in the second drop, same arc

| doc-id | work |
|---|---|
| `52036` | Kim & Kusner, *Torus Knots Extremizing the Möbius Energy* |
| `1-s20-s0166864101002632-main` | Rawdon & Simon, *Möbius energy of thick knots* |
| `arxiv-math-0108215v1` | Rawdon, *Möbius Energy of Thick Knots* |
| `s00526-018-1443-6` | Blatt & Vorderobermeier, *Analyticity of critical points of the Möbius energy*, Calc. Var. **58**:16 (2019) |
| `arxiv-1011.4891v1` | Sossinsky, *Mechanical Normal Forms of Knots and Flat Knots* |
| `funaba-2014-j-phys-conf-ser-544-012019` | J. Phys. Conf. Ser. 544 012019 |

`s00526-018-1443-6` is **not** a duplicate of `arxiv-1904.13129v1` — checked
rather than assumed: different title and a different author set (Blatt &
Vorderobermeier vs Vorderobermeier solo).

### Credit and a correction to my own framing

I ingested the first 13 in parallel with you, not knowing this bean existed
(it arrived in my merge). **Your pass did more than mine** — the `ohara1991` DOI
settled against full text, clearing a HUMAN-REVIEW flag open since June, and the
egress route table. My marginal contribution is the `doc_brief` propagation (the
merge showed your section files lacked it — 97 add/add hunks, every one
ours-adds-`doc_brief` / theirs-empty), the `INDEX.md` regeneration, and the
Chen–Chen–Zhong duplicate adjudication.

**And your correction applies to me.** I wrote that the `qou-pc85` arc was
"reasoning about O'Hara energies with the literature invisible to it". Your bean
already records the sharper truth: `references.ts` carries `ohara1991` and
`freedman1994`, and `MobiusEnergy.lean` already cites them — so **citation was
never blocked**; only greppable full text was missing. My PR body is corrected.

### State after the second drop

```
library dirs 705, INDEX rows 683, gap 22 = duplicates 21 + containers 1   (exact)
migrate --verify: 0 dirs without structure.json, 0 PDFs flat in uploads/
```
