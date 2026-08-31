---
# qou-cite
title: 13 citations point at bibliography entries that do not exist — the check had never run
status: todo
type: bug
priority: high
created_at: 2026-08-30T09:55:00Z
updated_at: 2026-08-31T04:57:23Z
---

`cites-resolve` — the check that validates every content block's `cites[]`
against `content/schema/references.ts` — **has never run in this folio**, and its
first run finds **13 unresolved keys across 10 blocks**.

## Why it never ran

Two layers, and the second was invisible behind the first:

1. Until `folio-assistant#150` (merged 2026-08-30), `validate-references` and
   eight sibling scripts threw on `requirePaper()` in a multi-paper folio —
   `qou-idxg`.
2. **Independently**, `scripts/run-validate.ts` never called
   `configureReferenceRegistry`. It *imports* `references.ts` (to check it
   parses — bean `qou-3vgs`) and then does not hand it to the platform. So
   `cites-resolve` no-ops and says so, in an `ℹ` line that has been in every
   run's output for months:

   > `ℹ [(bibliography)]: no reference registry configured — cites-resolve did
   > not run, so cites[] entries were NOT validated against references`

   The gate announced its own absence on every run and nobody read it.

## The 13 keys

| key | cited by | held near-miss |
|---|---|---|
| `faddeev1996` | `inter-nucleon-channel-color-tube`, `pachner-pentagon-borromean` | `faddeev1994`, `faddeev1995` |
| `manuscript` | `categorical-proton`, `categorical-proton-properties` | — (see below) |
| `champanerkar-kofman-mullen2008` | `q-zero-stokes-region-identification` | `champanerkar2003` |
| `bokut1978` | `phi-q-tower-algebraic-stratification` | `bokut2001`, `bokut2005` |
| `feigin-hashizume2009` | `dim-master-pentagon` | — |
| `dimofte-gaiotto-gukov2014` | `mirror-3d-3d-correspondence` | `dimofte-gaiotto-gukov2013` |
| `terashima-yamazaki2011` | `mirror-3d-3d-correspondence` | `terashima-yamazaki2013` |
| `kashaev-tirkkonen2014` | `modular-s-transform-q-q-tilde` | `kashaev1995`, `kashaev1997` |
| `macdonald1971` | `quantum-langlands-dual` | `macdonald1995` |
| `lusztig1989` | `quantum-langlands-dual` | `lusztig1990`, `lusztig1993` |
| `frenkel-reshetikhin2002` | `quantum-langlands-dual` | `frenkel2004`, `frenkel2007` |

## `manuscript` is a different defect and should be fixed separately

`[manuscript]` is the placeholder AGENTS.md §1 prescribes for a Lean `-- Ref:`
when no published reference exists. It is **not** a bibliography entry, so using
it in a content block's `cites[]` can never resolve. Two blocks do. That is a
category error rather than a missing paper, and it is the one item on this list
that needs no research.

## DO NOT sweep the near-misses

The right-hand column is suggestive and is **not** a fix list. Some are probably
wrong-year typos of a held entry; others are plainly distinct works —
`macdonald1971` is *Spherical Functions on a Group of p-adic Type*, the held
`macdonald1995` is *Symmetric Functions and Hall Polynomials*; Lusztig 1989
(*Modular representations and quantum groups*) is not Lusztig 1990. **Repointing
a citation at a different paper is worse than a broken link** — it puts a claim
behind a source that does not support it, silently.

Each of the 13 needs checking against what the citing block actually claims.
That is per-citation research, not a rename sweep, and it is why this bean is
filed rather than fixed.

## What was done instead

`scripts/run-validate.ts` now configures the registry **under `--strict` only**.

- Default run: unchanged, `✓ Valid — 14`.
- `--strict`: `cites-resolve` runs and reports the 13, `✗ Invalid — 23`.

Configuring it unconditionally would take the default gate red for everyone on
an untriaged backlog. Gating it makes the check *runnable* — which it has never
been — without inflicting that. Once the 13 are resolved, move the call out of
the `if (strict)` and the check becomes permanent.

## Suggested order

1. `manuscript` ×2 — category error, no research needed.
2. The four with a same-author near-miss differing only in year
   (`dimofte-gaiotto-gukov`, `terashima-yamazaki`, `faddeev`, `champanerkar`) —
   check the citing claim, then either fix the year or add the work.
3. The rest — genuinely absent works needing real metadata.
4. Then un-gate.


--------

## VERIFIED 2026-08-31 — the gate fires; and the arithmetic that looked wrong is right

The commit that landed this (`f5ecea6e36`) said in its own message that one
thing was NOT confirmed: *that `--strict` under the GATED code actually fires
the check*. It does. Measured, three runs, platform `21498cc`:

| run | registry | verdict |
|---|---|---|
| default | not configured | `✓ Valid — 14` |
| strict, registry forced OFF (`if (false)`) | not configured | `✓ Valid — 288` |
| strict, as committed | configured | `✗ Invalid — 297` |

The committed strict run prints the line the gate was written to print —
`bibliography: 805 entries, parses; registry configured (cites-resolve ON)` —
and carries all 10 `Unresolved citations` lines with the same 13 keys.

### The 9-vs-10 discrepancy, resolved rather than waved past

297 − 288 = **9**, but there are **10** citation lines. That is one short, and
a one-off in a count is exactly the shape of a miscount, so it was chased
rather than rounded.

It is not a miscount. Configuring the registry *removes* an issue: the
`ℹ [(bibliography)]: no reference registry configured — cites-resolve did not
run` line, which is itself counted. Verified directly — the with-registry run
contains **zero** `ℹ` lines. So 288 − 1 + 10 = 297 exactly.

That self-announcement is the whole story of this bean in one line: the gate
reported its own absence on every run for months, was counted as an issue
every time, and nobody read it. It only stops being emitted at the moment it
stops being true.

### What the 288 is NOT

`--strict` also turns on `term-mention-coverage` (AGENTS.md §4c), a separate
pre-existing backlog of unwrapped glossary mentions. **288 of the 297 have
nothing to do with citations.** Do not quote 297 as the citation debt, and do
not read `Valid — 288` as an all-clear either: it is `Valid` only because
those are warnings.

**The citation debt is 13 keys across 10 blocks, unchanged.** Still not fixed
here, for the reason in the body above: repointing a citation at a
different paper is worse than a broken link.


## CORRECTED 2026-08-31 — "13 dead citations" is ONE number over TWO unrelated defects

I filed this bean, and the framing was wrong. Measured against the
bibliography module itself (`bun -e` importing `content/schema/references.ts`,
**810 entries**) rather than by grepping for a spelling:

### Class A — 10 orphaned `cites[]` keys, cited in NO prose

`faddeev1996`, `champanerkar-kofman-mullen2008`, `bokut1978`,
`feigin-hashizume2009`, `dimofte-gaiotto-gukov2014`,
`terashima-yamazaki2011`, `kashaev-tirkkonen2014`, `macdonald1971`,
`lusztig1989`, `frenkel-reshetikhin2002`.

**Every one appears ONLY in a `.ts` `cites[]` array. Zero appear in any `.md`
prose, and zero in any Lean `-- Ref:`.** Measured both ways: a bare grep for
the key across `--include=*.md`, and a grep for `\cite{...}` containing it,
both corpus-wide. So none of the ten supports a written claim — they are
`cites[]` metadata that no sentence draws on.

That materially changes the fix. It is **not** "the paper cites a work that
does not exist"; it is "a block's metadata lists further reading whose key was
never added". Nothing a reader sees is broken today.

### Class B — `manuscript`, a DOCUMENTED CONVENTION with no backing

Different defect entirely, and much larger. `AGENTS.md` §1 says: *"The `[key]`
must match an entry in `content/schema/references.ts` exactly. **If no
published reference exists, use `[manuscript]`**"*. Those two sentences are in
tension, and the corpus resolves it the wrong way:

- **`manuscript` is NOT an entry.** Absent from all 810.
- **4436 Lean `-- Ref: [manuscript]` sites use it**, exactly as §1 instructs.
- The work it means **is** held — `leitner2026`, `type: "manuscript"`,
  `note: "This manuscript"`.

So the two `cites[]` hits this bean counted are the visible tip of a
convention that instructs 4436 sites to use a key the same paragraph requires
to resolve.

### Why the count was one number

Class A is 10 keys across 8 blocks; class B is `manuscript` in 2 blocks, and
`faddeev1996` is cited by two blocks — giving 13 **citations** across 10
blocks. The arithmetic was right. The **framing** was wrong: one of those
"citations" is a corpus-wide convention failure and the other twelve are
dormant metadata.

### What I did NOT do

Research the ten. Still the right call, and the reason is now confirmed
against the held set rather than asserted: the near-misses are mostly
**distinct works**. `macdonald1971` *Spherical Functions on a Group of p-adic
Type* vs held `macdonald1995` *Symmetric Functions*; `dimofte-gaiotto-gukov2013`
(held) and a 2014 companion are separate papers, as are
`terashima-yamazaki2013` (held) and a 2011 one. Repointing any of these at its
near-miss would silently attribute a claim to the wrong paper.

Class B is a **decision, not research**, and is framed for the owner rather
than actioned unilaterally: an alias entry would make the documented
convention work at all 4436 sites with a one-entry change, but would put the
same work in the bibliography twice.
