---
# qou-9e7p
title: '§7c checker: an inherited archimedean construct reads as gratuitous R'
status: todo
type: task
priority: normal
created_at: 2026-08-23T16:45:03Z
updated_at: 2026-08-23T22:10:56Z
---

## The false positive

`scripts/check-sidecars.sh` classifies a standalone library Lean file by looking
for archimedean constructs **in that file**. A file whose `R` is forced by an
IMPORTED archimedean construction therefore reads as
*'R in type but NO archimedean construct -> likely gratuitous'*.

Worked case (2026-08-23, PR #5558):
`QOU/SchurWeyl/HeckeProductSurjective.lean`. Every R in it comes from
`seminormalRep`, which is R-only because `OffDiagNonvanishing.sq_geom_lt` is an
inequality in an ORDERED field (`0 < y`, `nlinarith`). Nothing built on
`seminormalRep` can be generalised to a bare `[Field R]`, so the flag is
un-actionable as stated — the suggested fix (`generalize to {R}/[Field R]`) is
impossible.

## Why this matters rather than being cosmetic

The gate's instruction is 'act on the warning lines before commit'. A warning
that cannot be acted on trains agents to wave the gate through, which is exactly
how a REAL gratuitous-R would get past it. The 7c rule earned its place after a
gratuitous `(q : R)` landed on an algebraic tau-kernel lemma; the checker's value
depends on its warnings being actionable.

## Options, not a prescription

1. Follow the import graph one hop and treat an archimedean construct in a
   directly-imported QOU module as justifying the importer's R. Cheap, and
   catches this class; may over-forgive a file that imports something
   archimedean but does not depend on it.
2. Recognise an explicit in-file justification marker, so a file can say 'the R
   is inherited from X' and be classified accordingly. Auditable, but only as
   honest as the marker.
3. Leave it and accept the class as known noise — in which case say so in the
   skill doc, so agents know which warnings are expected to be un-actionable.

I did not implement any of these: this is the qou-0h5k session and the checker
is not its scope. The file carries a header paragraph explaining the
justification instead; see PR #5558.


## A SECOND false-positive class in the same checker, measured (2026-08-23, PR #5575)

The bean above is the `base-ring-minimal` branch (ℝ present, archimedean
construct one import away).  The **`MIXED generic + archimedean`** branch has an
independent defect, in the opposite direction: it fires on files with **no ℝ at
all**.

Worked case: `QOU/SchurWeyl/OcneanuWeight.lean` — a generic `[Field R]`
definition, zero code-level ℝ.  Flagged MIXED.  The single hit is
`c.2 ≤ d.2`, an ordering on `ℕ` inside a `Finset.filter`.  `MIXED` is by its own
name a *both* claim, and here the archimedean half does not exist: there is
nothing to split into two files.

Cause: `JUST` mixes strong markers (`Real.sqrt`, `LinearOrdered`, `CODATA`,
`MeV`) with **bare order symbols** (`0 <`, `< 1`, `≤`, `≥`) and order *tactics*
(`linarith`, `positivity`, `nlinarith`).  The bare symbols carry no type
information, so they fire on `ℕ`, `Fin`, list indices, `Finset` bounds.  This is
the same shape as the `norm_num` marker the script's own comment records
removing.

### Measured, on repo-authored standalone library Lean (excluding `.lake/`)

| | count |
|---|---|
| standalone library `.lean` under `content/` | 2133 |
| hit the MIXED branch (before the `_real`-pair filter) | 263 |
| of those, no ℝ under `RTYPE` **and** no strong marker | 165 (63 %) |
| of those 165, mention `ℝ`/`Real` **nowhere** in the file at all | **88** |
| of those 165, mention `ℝ`/`Real` somewhere (docstring, or a code form `RTYPE` misses) | 77 |

### Why I did NOT change the checker

The obvious fix — require `hasR` or a strong marker for MIXED — reclassifies
165 files, and I can only defend 88 of them.  The other 77 mention `ℝ`/`Real`
somewhere the `RTYPE` regex does not match; without opening each one I cannot
tell a correctly-ignored docstring from a code form the regex misses, and
downgrading a genuinely archimedean file is the worse error.  So: **88 confirmed
false positives, 77 needing per-file adjudication, no regex flip.**

(First measurement of this was contaminated — it swept the vendored Mathlib
under `content/**/.lake/packages/`, which `check-sidecars.sh` never sees because
it only reads *changed* files, and reported 1349/964.  Those numbers are wrong;
the table above excludes `.lake/`.)

### Next step

Adjudicate the 77 (cheap: `grep -n 'ℝ\|Real' <f>` per file, decide
docstring-only vs code), then either widen `RTYPE` or split `JUST` into
strong/weak and gate MIXED on strong.  The 88 are safe either way.


## The §7c classifier's exact firing token, on a file with literally zero ℝ

`YoungDiagramAddCell.lean` — pure ℕ × ℕ combinatorics, `grep -E 'ℝ|Real|sqrt|rpow|log|exp|linarith|positivity'`
returns **nothing** — is reported by `check-sidecars.sh` as

    [library Lean — archimedean construct present, ℝ justified]

The cause is in `JUST` (line 142): the alternation includes bare `≤` and `≥` and `0\s*<`. Every
`b.1 ≤ a.1` on ℕ in a lower-set proof matches. So `hasR = 0, hasJ = 1` and the file takes the
`elif [ "$hasR" = 1 ] || [ "$hasJ" = 1 ]` branch — which prints "archimedean construct present"
about a file that contains no ℝ at all.

Non-blocking (that branch does not set `action`), so this is noise rather than a false gate. But
it is the concrete instance behind the 165-file measurement already recorded here: the marker is
not "archimedean", it is "any inequality". Checker still NOT changed.
