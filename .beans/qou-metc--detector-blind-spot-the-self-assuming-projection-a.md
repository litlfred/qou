---
# qou-metc
title: 'DETECTOR BLIND SPOT: the self-assuming-projection audit cannot see an APPLIED single projection — 26 counted becomes 42, and the tuple case was already fixed this way'
status: todo
type: bug
priority: normal
created_at: 2026-09-13T17:33:19Z
updated_at: 2026-09-14T06:07:06Z
---

## MEASURED 2026-09-13 on the QOU Lean tree (2870 .lean files)

    proof-no-self-assuming-projection, live detector      26
    same run, one regex added                             42
                                                      -------
    invisible to the live detector                        16

All 16 come out COUNTED, not exempt — so they pass the detector's own PRIMARY
signal (the `CONCLUSION_FIELD` name gate: the author named the field
`claim_*`, `*_eq`, `holds`, …). They are invisible for one reason only: no
pattern matches the body SHAPE.

## THE SHAPE, and why it is the one that matters

`detectSelfAssuming` recognises four bodies:

    ctx.field                      PROJECTION_BODY
    by exact ctx.field             EXACT_PROJECTION
    <ctx.a, ctx.b>                 TUPLE_PROJECTION
    <ctx.a x, ctx.b x>             APPLIED_TUPLE_PROJECTION

and not the fifth:

    ctx.field s t hst              -- an APPLIED SINGLE projection

`PROJECTION_BODY` is `/^([a-z][\w']*)\.([A-Za-z_][\w']*)\s*$/` — it ends at
the field name, so any argument after it kills the match. `pat` then stays
undefined and `detectSelfAssuming` RETURNS BEFORE reaching its own structural
fallback, `projectionTypeMatchesConclusion`, which exists precisely to catch a
projection whose field name escapes the convention. The strongest check the
detector has is unreachable for this shape.

**This is the subclass that matters, not a corner case.** A class field
carrying a conclusion is almost always `∀ … → …`; to produce the conclusion
the theorem MUST apply it to the binders. So a self-assuming projection whose
conclusion is universally quantified is invisible BY CONSTRUCTION, and a
universally quantified conclusion is the normal case.

## 🛑 AND THE SAME FIX WAS ALREADY MADE, ONE ARITY OVER

`APPLIED_TUPLE_PROJECTION` exists, and its own comment says why:

    // An *applied*-field tuple `<ctx.impl_x ctx.active, ctx.impl_y ctx.active>`:
    // each component is a field `word.field` optionally APPLIED to further
    // `word[.field]` arguments. The `TUPLE_PROJECTION` regex above rejects the
    // trailing argument, so these placeholder-canonical projections escaped the

So "the regex rejects the trailing argument" was diagnosed, understood, and
repaired — **for the tuple case only**. The one-field analogue of the same bug
was left. That is what makes this a taxonomy row rather than a bug report: the
author had the right model of the failure and applied it at one arity.

## HOW IT WAS FOUND — by fixing an instance the detector never reported

`QOU/BraidsKnots/mobius_frobenius_kernel.lean`, body
`ctx.classical_limit s t hst`, class field `classical_limit` stating the
theorem's conclusion verbatim, under a class docstring reading *"All fields
are inputs; none is the conclusion."* A textbook §3b-cond item 5 projection.
The audit reported **0 defect candidates** on that subtree BEFORE the fix as
well as after — measured by stashing the change and re-running, not assumed.

Its field name escapes `CONCLUSION_FIELD`, so had the shape matched it would
have landed EXEMPT via the structural gate rather than COUNTED. It is a 17th
case, of a different kind from the 16.

## CONSEQUENCE FOR qou-z9ws's SIZING

`qou-z9ws` sized the population from detector output: 112 entries, ~102
independent defects, 0 of 12 sampled legitimate. **That 112 is a floor, not a
count** — it cannot include any applied single projection. Do not quote it as
the size of the problem.

## WHAT IS NOT CLAIMED

That the 16 are 16 defects. They are candidates surfaced by a deliberately
loose probe regex
(`/^(?:by\s+exact\s+)?([a-z][\w']*)\.([A-Za-z_][\w']*)(?:\s+[A-Za-z_][\w'.]*)+\s*$/`)
and each still needs the agent adjudication the review ledger demands. The
measurement establishes that the detector cannot SEE them, which is a
statement about the detector; whether each is a genuine defect is a statement
about the file and has not been made.

Nor is a fix proposed here as a side effect. The detector's own comments say
promoting newly-covered patterns to hard failures is *"a deliberate follow-up,
not a silent side effect of closing the blindspot"*, and 26 → 42 is a 62 %
rise in a critical-severity criterion. The probe patch was applied in a
scratch copy and reverted; `git diff` on the detector is clean.


## LANDED 2026-09-13 — and finding the fix surfaced a WORSE defect

Both are now taxonomy rows: 42 (this one) and 43 (the ledger).

### Row 42 — the pattern, landed EXEMPT

APPLIED_PROJECTION added beside the tuple form it is the one-field analogue of.
Measured, QOU Lean tree, 2871 .lean:

  counted (total_defects)      34 -> 34     gate stays green
  this criterion, counted      26 -> 26
  total_exempt                 42 -> 58     +16
  files_flagged                61 -> 76
  applied-field-projection      0 -> 16

All 16 land EXEMPT, as the two prior coverage expansions did, and all 16 enter
the review ledger so --check-ledger demands an agent verdict on each.
Promoting them to hard failures is issue #7329 and is NOT done here.

No regression: no previously-counted finding moved into the new exempt bucket
(counted unchanged while exempt rose by exactly the 16 new entries).
--selftest-docstring-sorry passes.

### 🛑 Row 43 — I DESTROYED 106 COMMITTED ADJUDICATIONS FINDING IT

Seeding the ledger for those 16, scoped to
content/quantum-observable-universe/lean, rewrote
docs/audits/lean-vacuity-review-ledger.json -863/+67 and deleted 106 of 329
entries. Caught in the git diff and reverted; nothing committed. NO CHECK WOULD
HAVE CAUGHT IT -- the run prints only "N candidate(s)".

The deletion loop already carries a guard for the SAME confusion one axis over:
it distinguishes "fixed" from "not produced by this scanner", added 2026-08-30
after a run deleted 116 of 268 entries. It does not distinguish "fixed" from
"NOT SCANNED". All 106 were in categories this audit DOES produce, so that
guard preserved none of them. The ledger spans 22 roots across two papers; only
223 entries live under the subtree scanned.

And the --json path three hundred lines up ALREADY REFUSES a partial scan, in
those words. The ledger is the other write path of the same API and never got
the rule -- row 33 (qou-3ral) a second time.

Fixed by SCOPING the deletion, not refusing the run: a partial scan still
resolves stale entries inside what it looked at, and cannot touch what it did
not. Regression test: the exact destructive command now preserves 210
foreign-category and 45 unscanned-file entries.

### WHAT IS STILL OPEN

1. Adjudicating the 16. They are candidates from a deliberately conservative
   regex, not verdicts. qou-z9ws measured 0 of 12 legitimate on the PREVIOUSLY
   VISIBLE population -- evidence about that population, not this one.
2. Whether to promote applied-field-projection from EXEMPT to COUNTED. Issue
   #7329; an owner call, since it turns a critical gate red on 16 files.
3. Seeding the ledger for the 16. Needs a CORPUS-WIDE scan across all 22 roots,
   not the subtree scan that caused row 43. Deliberately not run here.
4. qou-z9ws's 112-entry sizing is a FLOOR. Not re-sized.


## Item 1 DONE — PR #7341 (2026-09-13)

**The population was 21, not 16** (the 16 counted only `lean/QOU/`; five more
are content-block siblings under `mass-theory/`), and **none of the 21 were
reaching the ledger at all** — #7332 exempted them with the reason
`"tracked; derivation pending"` while `--review-ledger` seeds only on the
literal `triage pending`. Measured corpus-wide: 0 of 21 seeded. Taxonomy row 44.

**Verdicts: 15 genuine / 5 advisory / 1 legit.** Discriminator applied was
`qou-z9ws`'s — a projection is the accessor idiom only when something builds
the bundle — and **13 of the 14 carriers have zero builders**; the 14th's only
builder is a documented content-free zero skeleton. The `legit` is
`dH_verticalReflection`, where `dH_eq` is a *theorem* on a bundle constructed
in the same file.

Whole corpus: **56 → 71** defect candidates, 80 → 65 exempt, 26 → 41 promoted.
`--check-ledger` exit 0, zero `needs-agent`.

## Item 2 DISSOLVES

It was framed as a blanket "promote the pattern EXEMPT → COUNTED". The audit
has no such switch: promotion is per-candidate via `adjudicatedGenuine`, which
already accounts for 26 of the pre-existing defects. The only decision was the
adjudication, and it is in #7341 with per-candidate evidence.

## Item 3 is BIGGER than it looked

A full-corpus `--review-ledger` run would delete **33** entries whose candidates
no longer fire (spot-checked three — all genuinely repaired by `qou-9yt9` /
`qou-ghy5`, so the deletions are correct) and reset **~20** more on file-sha
drift, each needing re-adjudication. `--check-ledger` reads green on `main` only
because nobody has re-run `--review-ledger` whole-corpus. Budget for ~20
re-adjudications, not for a mechanical sweep.

## Item 4 unchanged

`qou-z9ws`'s 112-entry sizing is still a floor.

## New, filed separately

- `qou-vh1o` — the 13 candidates on the two OTHER exemption arms, still
  invisible, with file:line list and the four steps to close.


## Items 3 and 4 DONE (2026-09-14, commit 617677b8b8)

### Item 3 — corpus-wide seeding

Ledger **350 → 321**. `--check-ledger` exit 0 over all **108** candidates;
re-run changes 0 entries; `--selftest-docstring-sorry` exit 0.
Defects **71 → 72**, promoted **41 → 42**.

**14 of the 18 `needs-agent` were NOT adjudication.** `file_sha` is a
whole-file hash, so a verdict expires on any edit to its file, however far from
the declaration. `scripts/lean-vacuity-ledger-reverify.py` compares the
DECLARATION instead: **IDENTICAL=14, CHANGED=0, NOT-FOUND=0, UNADJUDICATED=4**
across three categories. Those 14 were restored with a dated re-verification
line, not re-decided.

Its docstring carries the trap that made me use it rather than hand-read:
*IDENTICAL means nothing without a prior verdict* — a past run reported a clean
22/22 where 21 had never been adjudicated, so "21 of those greens were about
nothing". It refused to restore the 4 below, correctly.

**The 4 genuinely unadjudicated:** `volume_perturbation` **genuine** (field IS
the conclusion; zero builders; the class docstring says "All fields are
*inputs*" and then concedes the field was added "to repair the refutable
encoding" — that repair made a refutable statement an assumed one);
`ordering_extends` **advisory** (`P → P`, but a fully disclosed tombstone whose
docstring opens by saying so and leaves the real claim open);
`decoy_premise_irrelevant` **legit** (the detector flagged the file written to
*prove* the detector's finding — `ProofHygiene/SelfAssumingContexts.lean`; the
`True` in the witness IS the content); `proton_neutron_indistinguishable`
**genuine** (`f 3 = f 3`, the exact `X = X := rfl` form rule 5 bans; fix is to
take the counts as hypotheses).

Side finding for the convention arc (`qou-961o` / `qou-cxjq`), not part of any
verdict: `VolumePerturbationContext.z_def` is **convention C**
(`1/(√q + 1/√q)` ≈ 0.4993), not canonical D (≈ 0.6127). Same sqrt-variable
spelling in `wenzl-qmn-synergy.lean:116,134` and
`QBetaPerBlockChiClosedForms.lean:1267`.

### Item 4 — `qou-z9ws` re-sized, and its "112" is NOT what a fresh measurement returns

🛑 **The current ledger yields 112 for a DIFFERENT population, and reporting
that as confirmation would have been wrong.**

- **`qou-z9ws`'s metric** is *"the 112 `genuine` `proof-no-self-assuming-projection`
  entries"* — one category, `genuine` only. Its own record closes a drain at
  **112 → 90**.
- **Today that metric is 56**, of which **15 are this session's
  `applied-field-projection` verdicts** — so it stood at **41** before this
  tranche. The 90 → 41 movement is **not** explained by this session (only 1 of
  my 33 deletions was in that category) and I did not measure its cause.
- **The coincidental 112** is *all verdicts across the seven self-assuming
  patterns*: `field-projection` 48, `applied-field-projection` 21,
  `decoy-hypothesis` 17, `prop-universe-field` 13, `tuple-projection` 10,
  `exact-field-projection` 3 — 85 genuine / 21 legit / 6 advisory.

So the bean's headline number and a naive re-measurement agree numerically and
disagree about everything else. Quote the metric with its scope, or a reader
concludes nothing has moved when it has more than halved.

### Bean stays `in-progress`

All four items are done, but the work is unmerged: it rides #7341, which is
parked on the owner for the 56 → 71 (now 72) decision.
