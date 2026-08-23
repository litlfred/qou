---
# qou-u87j
title: 46 content-block .lean siblings mirror a library structure with a different field set, and all 46 mask its lean.ref
status: todo
type: task
priority: normal
created_at: 2026-08-23T07:55:37Z
updated_at: 2026-08-23T08:05:53Z
---


## Measured 2026-08-23, branch `claude/n1dj-volume-iso-reading-2026-08-22`

> **Every count in this section is superseded** — see §Correction below. The
> real figures are 148 / 102 / 46 / 39, from `check-mirror-drift.ts`. The
> filename still carries the old `43-` slug because a beans title change does
> not rename the file; resolve this bean by `ls .beans/ | grep u87j`, never by
> slugifying the title.

Found while doing `qou-n1dj` item 3, where **one** instance of this appeared:
`quantum-observable-universes/quantum-observable-universe.lean` turned out to be
a second definition of `QuantumObservableUniverse`, not a stub importing the
library one — and its field set had drifted, carrying a `volumeForm_epi` the
library never had. That looked like a one-off. It is not.

### The population

Over `content/quantum-observable-universe/**/*.lean`, comparing every
`structure`/`class` declared in a co-located sibling against a library
declaration of the **same name under the same namespace**:

| | count |
|---|---|
| same-namespace duplicate definitions (sibling mirrors library) | **167** |
| field lists identical — faithful mirrors | 117 |
| field lists **drifted** | **50** |
| distinct sibling *files* carrying at least one drifted mirror | **43** |
| of those, files that are a content-block sibling (`<stem>.ts` exists) | **43 — all of them** |

The last row is the finding. A co-located `<block>.lean` wins **candidate 1** of
`lean.ref` resolution in `walkBlocks`, unconditionally and before the Lake-tree
candidates. So for all 43, the block's checkers audit the drifted copy and never
look at the declaration `lake build` actually compiles.

### Mirroring is deliberate; drift is not

`su2-emergence.lean` states the reason in its own docstring: *"content-sibling
`.lean` files compile standalone and cannot import one another"*, so a sibling
that needs a library type restates it. 117 of the 167 do that faithfully. This
bean is about the 50 that no longer do.

### It is not cosmetic — worked example

`QOU.CRManifoldData`, library `lean/QOU/QuantumObservableUniverse/CRRealisation.lean`
vs siblings `c-quantum-observable-universe.lean` and `c-quantum-universe.lean`:

- **library only:** `n_pos : 0 < n`
- **sibling only:** `contact_nondeg : ∃ p, contactForm p ≠ 0`,
  `reeb_preserves_contact : ∀ p, contactForm (reebField p) = contactForm p`

Each side carries an anti-vacuity condition the other lacks. The library's
version admits a contact form that is identically zero; the sibling's admits
`n = 0`. Whichever one a reader or a checker happens to reach, it is not the
one the other half of the corpus is talking about.

Hand-verified against both files — this is not a parser artifact.

### Method and its limits

Regex scan (`structure|class` head, then indented `field :` lines until
dedent), namespace tracked via `namespace`/`end`. Limits, stated so the number
is not over-read:

- Fields whose type spans lines before the `:` are missed; a `where`-clause
  default on its own line is not counted as a field.
- Name+namespace collision is treated as "same declaration". Two genuinely
  unrelated declarations that happen to share a fully-qualified name would be
  counted as drift — but that is itself a defect worth the same bean.
- **117/167 identical is the control.** A parser that mis-read fields at random
  would not produce a 70 % exact-match rate, so the 50 are drift rather than
  noise.

### Notable entries

`quantum-universes/quantum-universe.lean` (`def:quantum-universe`),
`c-quantum-observable-universe.lean`, `c-quantum-universe.lean`,
`lifting-and-descent/motivic-galois-character.lean` (the class `qou-s0ip` is
about), `spin-labels.lean`, `substrate-parameter.lean`,
`quantum-observable-universes/quantum-gauge-group.lean`.

A **44th** existed on `main`: `quantum-observable-universes/quantum-observable-universe.lean`,
resynced by the `qou-n1dj` branch. Re-measure against `main` if that PR has not
landed.

### Relation to neighbouring beans

- **`cscb`** (epic, content-sibling compile breakage) and **`qou-lsib`** are
  about siblings that *do not compile*. These 43 compile fine. Different defect:
  a file can be green and still be the wrong definition.
- **`qou-cu0a`** / **`qou-2u26`** are about `lean.ref`s that resolve to the wrong
  place or nowhere. This is the inverse: the ref resolves *successfully*, to a
  file that disagrees with the library.

### Options, for an owner call

1. **Gate it.** A checker comparing each sibling mirror's field set against the
   same-named library declaration, erroring on drift. Cheapest durable fix, and
   it is the only one that stops the 117 faithful mirrors from becoming the next
   50. Belongs in folio-assistant next to `check-wall-side`.
2. **Reorder `lean.ref` resolution** so the Lake tree wins over a co-located
   sibling when both exist. Removes the masking outright, but changes resolution
   for every block in the corpus and would need its own measurement first.
3. **Resync the 50 by hand.** Fixes today and not tomorrow.
4. **Stop mirroring** — give siblings a way to import library modules. Addresses
   the root cause; much the largest change.

Options 1 and 2 are complementary, not alternatives. Not started.

## Correction 2026-08-23 — the figures above are from an ad-hoc scan; use the checker's

The counts in the previous section (167 / 117 / 50 / 43) came from a throwaway
script written to test whether the `QuantumObservableUniverse` case was isolated.
It answered that question and should not be quoted further. There is now a real
checker — **folio-assistant `scripts/check-mirror-drift.ts`** — and its numbers
supersede them:

| | ad-hoc scan | `check-mirror-drift.ts` |
|---|---|---|
| declarations, Lake trees / block siblings | — | 1214 / 841 |
| same-FQN pairs | 167 | **148** |
| identical (faithful mirrors) | 117 | **102** |
| **drifted** | 50 | **46** |
| distinct sibling files carrying drift | 43 | **39** |
| drifted pairs that mask a block's `lean.ref` | 43 (= all) | **46 (= all)** |
| duplicate FQNs inside the Lake tree | not measured | **0** |

Four mistakes the ad-hoc scan made, each now a test case in
`scripts/tests/check-mirror-drift.test.ts`:

1. **Named sections.** `section Foo … end Foo` is indistinguishable from a
   namespace at the regex level. The old scan only popped on `end <name>` and
   kept one stack for namespaces alone, so every declaration after the first
   named section got the wrong namespace — inventing collisions and hiding real
   ones. An anonymous `section` did the same damage through a bare `end`. The
   checker keeps namespaces and sections on one stack and pops whichever is on
   top.
2. **Docstrings and comments.** The old scan read `field :` lines inside `/-- … -/`
   as fields. The checker tracks docstring state.
3. **`extends`.** Not parsed before, so a pair differing only in whether it
   inherits or inlines a parent looked like field drift; a clause wrapped onto
   its own line was dropped entirely. Now compared separately and reported as
   `extends differs` (1 case).
4. **A lowercase-only field pattern.** `M : Type*`, `C : Type u` and
   `Target : Place → Type*` are all real fields here, and both scans dropped
   them at first — so a pair differing *only* in such a field read as
   "identical". This one moved the count **up**, 45 → 46, and it is the reason
   the first run of the checker was still slightly wrong.

Three of those four surfaced only because the tests were written; the checker's
first run reported 45 / 103 / 38. Numbers from a parser nobody tested are worth
about what the ad-hoc scan's were.

**What does not change** is the finding. `46 / 46` of the drifted pairs sit in a
file that is a content-block sibling, so every one of them masks a `lean.ref`.
The faithful-mirror rate is 69 %, essentially unchanged, and that ratio remains
the parser's control. The `QOU.CRManifoldData` example is reproduced verbatim by the checker,
including both anti-vacuity fields.

**Reproduce:** `bun run <folio-assistant>/scripts/check-mirror-drift.ts --package qou`
from the qou repo root. `--tsv` for one row per pair, `--json` for the totals.

### Option 1 is now built, not proposed

`check-mirror-drift.ts` exists on folio-assistant branch
`claude/gracious-dijkstra-0ijp2l`. It exits 0 by default — a gate that fails CI
on a 46-item backlog only teaches people to pass `--warn-only`. Wire it as
`--baseline 46` so it fires on *growth*, which is what keeps the 102 faithful
mirrors from becoming the next 46. `--max 0` is the end state once the backlog
is drained.

Verified: exit 2 over `--max`, exit 3 over `--baseline`, 0 with `--warn-only`,
64 on an unknown package, and 0 with an all-zero report when run from the
platform repo with no content injected. `eslint` clean.

Options 2–4 are untouched.
