# `voice-scholarly-default` fires on "right-trace" — 70 false positives, 1 true

**Date:** 2026-08-26 · **Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Checker:** `folio-assistant/content/pipeline/qa-checkers-voice.ts`,
`LECTURER_OPENER_RE`
**Status:** reported, **not fixed here** — the checker lives in another repo

## How it surfaced

Editing `quantum-universe.md` staled its sidecar and forced a re-sweep. The
re-run flipped `voice-scholarly-default` from `pass` to `fail` — but the cached
entry's `lean` hash had also moved (`3894942e100d` → `79f5d286827a`) without my
touching the `.lean`. So the `pass` on record had been computed against an older
`.lean`, and the failure is **pre-existing**, merely un-cached by my edit.

That is worth noting on its own: a stale sidecar was reporting a green verdict
for a file that had since changed.

## The defect

`LECTURER_OPENER_RE` is meant to catch lecture-hall discourse markers — "OK, so
…", "Right, now we …". Its `Right` branch is written

```
Right,?\b
```

with the comma **optional**. Anchored at `^\s*`, that matches any line beginning
with `right` followed by a word boundary — and `-` is a boundary. So
`right-trace`, `right-hand side`, `right-multiplication`, `right action` all
match. Same for the `OK,?\b` branch, which matches a line beginning `ok =`.

Note the same regex writes `Well,` and `Anyway,` with **mandatory** commas. Only
`OK`, `Okay`, `Alright` and `Right` have the optional one, and those four are
exactly the branches that collide with technical vocabulary.

## Blast radius, measured

Scanning every `.md` and `.lean` under `content/quantum-observable-universe`:

| | count |
|---|---:|
| lines matching the optional-comma openers | 71 |
| genuine discourse markers (comma present) | **1** |
| **false positives** (no comma) | **70**, in **62 files** |

A 70:1 false-positive rate on that branch. Representative hits, all correct
technical prose:

- `quantum-universe.lean:171` — *"right-trace on `End(A)` only …"*
- `quantum-observable-universe.lean:156` — the same sentence
- `coxeter-parabolic-transversal.md:14` — *"right-multiplication actions of $s_i$"*
- `mobius-energy-proof.md:38` — *"right-hand side remains in $\mathbb{R}$"*
- `pentagon-uv-commutation-woronowicz.lean:111` — *"right action."*
- `mba-step06-frobenius-pairing.md:49` — `ok = check_frobenius(x)`

## The fix, and why it is not applied here

Make the comma mandatory on all four, matching `Well,` and `Anyway,` in the same
alternation:

```
OK,\b | Okay,\b | Alright,\b | Right,\b
```

That keeps the one true positive and removes all seventy. The file is
`folio-assistant/content/pipeline/qa-checkers-voice.ts`, in a **different
repository**, so it cannot land on this branch.

**The prose is not reworded.** `right-trace` is the correct technical term,
paired with `left-trace`, and axiom 3 of `def:quantum-universe` is precisely the
statement that the two coincide. Rewording correct mathematics to satisfy a
buggy regex is the "make the red green by weakening" anti-pattern, and it would
also destroy the left/right pairing the axiom depends on.

So the sidecar carries an honest `fail`, and this note is the reason it is there.

## Recommended disposition

1. Fix the four branches upstream in `folio-assistant`.
2. Re-sweep the voice axis across the corpus; expect ~70 entries to flip back to
   `pass` with no content change.
3. Until then, treat `voice-scholarly-default` failures whose evidence line
   begins with `right`/`ok` as presumed false positives — check the evidence
   text before acting on one.
