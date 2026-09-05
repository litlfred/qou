---
# qou-9b50
title: Label every k=3 knot conclusion with the weight family it was computed under - three families give three winners, so an unlabelled claim is meaningless
status: completed
type: task
priority: normal
created_at: 2026-09-05T06:57:23Z
updated_at: 2026-09-05T07:15:24Z
---

## DONE 2026-09-05 — audit docs/audits/2026-09-05-k3-weight-family-labelling.md

SWEPT content/ (.md + .ts), docs/audits/, docs/coordination/, computations/
(docstrings + witness description/verdict), .beans/, .lean for k=3 / FR-pullback
knot conclusions and the variance figures (1.82 / 1.55 / 1.5015 / 1.05 / 1.19).

COUNTS (corrected): class (a) 17 items -- 7 files / 14 edit sites FIXED, 3
already compliant, 7 producer+witness pairs DEFERRED (see below). The first
pass of this line said "15 files / 12 sites"; both were undercounts of my own
edits (the two-per-file registry .md/.json edits and the second content-block
site were each counted once). class (b) dated
records 7 files, left as records. class (c) excluded 12 files, each with a
stated reason (complete graph K3, algebraic K_3(C), bound variable K3, a Python
multiplication `K_3*len(...)`, 6_1 braid-index/cusp geometry, a Numdam URL).

FIXED (family named, no number changed, no verdict restated):
  conj:depth-stratified-frobenius-reciprocity .md  -- "K_3*=4_1 best" labelled
    d_q^2/[n]_q! + a follow-on note giving the three-way family dependence
  DepthStratifiedFrobeniusReciprocity.lean       -- module + 2 docstrings
  DepthStratifiedFrobeniusReciprocityVariance.lean -- module + 2 docstrings; the
    1.82x baseline labelled family (1), with the (2) figure 1.19x named
  trace-convention-registry.md + .json  -- ALSO CORRECTED a stale claim: it said
    fr_pullback_k3_test.py "uses the textbook form"; that producer migrated
    2026-09-04 and now calls selfnorm_denominator, so its live output is
    d_q^2/D^2 while its committed figures are the pre-migration (1) run
  1ppb-categorical-chain.md -- dated note under "Authoritative finding (post
    #826)", which was phrased as current and named no family
  .beans/yfvb -- its "already validated / does NOT need redoing" list asserted
    "4_1 best 1.55x, paper's 6_1 NOT best"; amended, that reverses under (2)

UNDETERMINABLE (2, same defect from two sides -- a dangling citation):
  binding_depth_stratified_selfconj.py:7 -- "6_1 at k=3, the chirality channel"
    cited to prop:plancherel-term-7-formulation, which NAMES NO KNOT; and the
    script computes a self-conjugate restriction, so the 6_1 never enters its
    own arithmetic. No run behind it whose family could be read off. Recorded as
    "unrecorded provenance and unrecorded weight family" rather than guessed.
  the SAME dangling citation was in DepthStratifiedFrobeniusReciprocity.lean;
    there the family WAS recoverable (PR #826 = family (1)) so it was fixed, and
    the citation dropped.

ADJACENT FINDING (the more useful one): the corpus's two live "k=3 knot is X"
claims come from TWO DIFFERENT DERIVATIONS and only one has a weight family at
all -- the FR-pullback variance route says 4_1 (and says 6_1 or 5_2 under a
different w_lambda), while the GB-filtration route (curvature-rank-gb-
stratification-proof, confinement-curvature-rank) says 6_1 at curvature-rank 3
structurally, with no w_lambda in it. So "the paper's named 6_1" is not a
weight-family result and is not touched by any weight-family measurement. The
K_3*=6_1 that #826 overturned is a third thing (the catalog aside) and no longer
appears anywhere in content/.

NOT DONE, deliberately: no computations/*.py or *.witness.json edited. A
docstring-only edit drifts scriptHash for a byte-identical payload and flags
every witness self-stale; these are H_9/H_12 character computes (~25 min for the
4He leg) and the brief forbade re-running. Families are already determined in
the audit table, so applying them later is mechanical.

FOR THE fr_pullback_k3_test.py OWNER (file claimed by the coordinator this
session, not edited): (1) its witness description names the redistribution rule
but not the BASE MEASURE -- should say d_q^2/D^2, and that the 1.82x/1.5015x
quoted downstream are the pre-migration d_q^2/[n]_q! run; (2) one line saying
the k=3 ranking is family-dependent, since five downstream probes inherit its
framing unlabelled.

TRAP RECORDED: `bun run folio-assistant/content/pipeline/render-latex.ts <block>`
exits 0 on a NONEXISTENT block -- it is a library module with no import.meta.main,
so bun loads it and exits. I wrote that rc=0 up as a clean render before catching
it. The real render + unified-latex AST validation runs inside run-validate.ts
(validate.ts:621-622 renderBlock + validateLatexAst); use that.

VERIFIED: both .lean lean-direct exit 0, 0 sorry (docstring-only changes);
run-validate on the paper = Valid, 10 pre-existing issues, none in the changed
block; qa-sweep re-run on the block (script criteria refreshed); registry JSON
re-parses; manual math grep battery clean.
