---
# qou-kcii
title: habiro-coefficients-extended.witness.json exists twice, with different q0Anchor
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:05:02Z
updated_at: 2026-08-23T08:14:21Z
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
