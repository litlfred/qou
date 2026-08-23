---
# qou-kcii
title: habiro-coefficients-extended.witness.json exists twice, with different q0Anchor
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:05:02Z
updated_at: 2026-08-23T08:52:47Z
---

Found 2026-08-21 diagnosing qou-3zby (the red L1 tr_M gate).

  computations/habiro-coefficients-extended.witness.json        q0Anchor=ambiguous
  computations/habiro/habiro-coefficients-extended.witness.json q0Anchor=ABSENT

Identical payload (json-equal 'data') and identical scriptHash 6fdad0d63cff,
both computedAt 2026-07-18. They differ ONLY in the anchor field.

Why it matters beyond tidiness: which copy you get depends on how you
resolve the name. The gate uses _path_bridge.witness_path and gets the
top-level one. A probe I wrote used rglob and got the OTHER one, and
reported the wrong q0Anchor for its headline input until I caught it. Two
files with the same name, the same hash, and different provenance metadata
is a trap for exactly the kind of audit that reads witnesses by stem -- and
several do.

Not fixed in that PR: deciding which copy is canonical (and whether
'ambiguous' or absent is the right label for it) is the Habiro arc's call,
not a bystander's. Note the anchor question is live -- Habiro's values are
measured at the PROTON pin (qou-3zby), so 'ambiguous' may itself be wrong.

Cheap check for whoever takes it: are there OTHER duplicated witness stems?
The one-liner is a find | basename | sort | uniq -d over computations/.


## MEASURED: it is 25 stems, not one — and none is a harmless copy

  duplicated witness stems in computations/ (excl. _deprecated) : 25
    payload identical, same anchor  :  0
    payload identical, anchor differs: 0
    PAYLOAD DIFFERS                 : 25

Every single duplicated stem holds two DIFFERENT results under one name.
Contradictory anchors are common among them:

  alpha-k-jones-markov-h3        None      vs proton
  alpha-k-jones-markov-h4        None      vs proton
  geom-leading-alt-q-locality    None      vs proton
  pentagon-to-borromean-h4       ambiguous vs proton
  per-knot-density-borromean-h4  None      vs proton
  habiro-coefficients-extended   ambiguous vs None
  q0-consistency-audit           None      vs None
  e0-calibration-audit           None      vs None

Note e0-calibration-audit and q0-consistency-audit are in the list: two of
the AUDIT witnesses are themselves duplicated with differing payloads.

CORRECTION to my own first measurement. I initially reported habiro's two
copies as 'identical payload' -- that compared only the  block. A
whole-document comparison (excluding computedAt/commitSha/durationMs/
scriptHash/engineVersion/environment) shows they differ. My first classifier
then had a second bug: it left q0Anchor INSIDE the payload comparison, so
the 'anchor differs' bucket was unreachable and everything fell into
'payload differs' for the wrong reason. Both fixed; the 25 stands under the
corrected classifier.

Reproduce:
  find computations -name '*.witness.json' -not -path '*_deprecated*' \
    | xargs -n1 basename | sort | uniq -d

Which copy a consumer gets depends on how it resolves the name --
_path_bridge.witness_path vs rglob vs a hardcoded path. That is not a
theoretical risk: it already produced one wrong reading (qou-3zby probe,
caught pre-commit).


## Correction: the two copies are NOT payload-identical (2026-08-23)

Commit `667c9ab3f6`, which flagged this duplicate, describes the two files
as having *"identical payload and scriptHash but different q0Anchor"*. The
scriptHash half is right; **the payload half is wrong**, and it is wrong on
the field that matters.

Measured on both files:

    same scriptHash   : True   (6fdad0d63cff)
    payload identical : False
    file size         : 23857 B  (computations/)  vs  1892 B  (computations/habiro/)

    only in A         : q0Anchor
    only in B         : engineVersion
    shared keys DIFFERING: results, commitSha, computedAt, engine, scriptCommitSha

**`results` differs.** So this is not a benign copy that merely disagrees
about its anchor label — the two files disagree about the numbers, while
advertising the same producer hash. A consumer resolving the wrong path gets
different mathematics, not just a different label, and `scriptHash` gives no
warning because it matches.

That raises the priority of this bean: the duplicate is a correctness hazard,
not a tidiness issue. It also means whichever copy is regenerated to drain the
pin straddle (`qou-3zby` / `qou-dau6`), the OTHER copy stays stale and
silently wrong.

Note the 12x size difference suggests one is a truncated or partial write
rather than a full second run — worth establishing which is authoritative
before deleting either.


## The second copy is not data at all — it is a PRE-FIX FAILED RUN (2026-08-23)

Sharpens the correction above. `computations/habiro/habiro-coefficients-extended.witness.json`
does not hold different numbers; it holds **no numbers**. All four isotope
keys are error records:

    D (deuteron, A=2)  {'error': 'ValueError: LaurentQ.from_sympy: non-Laurent factor ...'}
    T (triton, A=3)    same
    3He (helion, A=3)  same
    4He (alpha, A=4)   same

That is why it is 1892 B against the top-level copy's 23857 B — it is a
**failed regeneration attempt that got committed**, not a second successful run.

**Dating it: this predates PR #5376.** Per `qou-iayk`, the LaurentQ parser
fix landed in #5376 and the producer then runs **4/4 clean**. So this file
captures the failure mode that fix removed. It is stale in the strongest
sense — not merely out of date, but a record of an error that no longer
occurs.

**Consequence for the disposition.** The earlier note asked which copy is
authoritative before deleting either. That question is now answered: the
top-level copy is the only one carrying data, and the `habiro/` copy has no
recoverable content to preserve. It still must not be deleted casually — a
consumer may resolve that path (the `667c9ab3f6` probe did exactly that,
via `rglob`) and would then read an error record as though it were a
witness. Fix the resolution, then remove the artifact.

**Not the regeneration blocker.** Do not read this as the reason Habiro
cannot be regenerated. Per `qou-iayk` the parser error is FIXED; the live
blocker is that the fresh values contradict a landed D(u) closed-form law
that the old witness satisfies exactly. Different problem, different bean.


## The MECHANISM is undetected: 6 sites bypass the resolver (2026-08-23)

`duplicate_witness_stem_audit` measures the duplication and, better, the
7 consumer-splitting stems. It does **not** detect the mechanism by which the
incident in its own docstring happened — *"a probe used `rglob` instead of
the resolver, read the other copy, and reported the wrong q0Anchor"*. Its
only `rglob` references are that narrative and its own sweeps.

So a recurrence would not be caught. Six sites resolve a witness or producer
**recursively by name and take one**, without calling
`_path_bridge.witness_path`:

    computations/q0_muon_reproduction_sweep.py    L105   return w      (first match)
    computations/witness_padding_provenance.py    L209   hits[0]
    computations/producer_repad_sweep.py          L159   hits[0]
    computations/witness_provenance_audit.py      L356   return cand   (first match)
    computations/q0_repin_sweep.py                L332   break         (first non-deprecated)
    scripts/convention-c-taint.py                 L108   return first

Spot-verified on three of them: none references `witness_path` at all.

**Why 'first match' is not a tie-break.** `Path.rglob` yields in
`os.scandir` order — filesystem-dependent, and **not** sorted. Several of
these sites do not wrap it in `sorted()`. So the copy chosen is not merely
*a* deterministic wrong one; it can differ between machines and between runs
after unrelated file churn. That is the worst failure shape for a witness
read: silent, and not reproducible from the source.

**Scope, honestly.** This is the *capability* to pick wrong. I have NOT
established that any of the six currently resolves one of the 25 ambiguous
stems — that needs per-call-site tracing of what names reach each. Read it as
'the guard rail is absent here', not as six live defects. Four of the six are
sweep/audit drivers, where a wrong pick corrupts a report rather than a
published number; `witness_provenance_audit` is itself an audit.

**Cheapest fix, if wanted:** route these through `witness_path`, which
already implements the prefer-dir search order. Failing that, `sorted()` at
minimum, and a hard error on `len(hits) > 1` rather than a silent `[0]`.

Not building a detector for this here — if it should be gated, the existing
`duplicate_witness_stem_audit` is its natural home rather than a second
script scanning the same tree.
