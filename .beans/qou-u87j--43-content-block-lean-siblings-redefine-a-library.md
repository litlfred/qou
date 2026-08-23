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

> **Every count in this section is superseded.** Read §Final figures at the
> bottom, not this one: on `main` it is 147 / 101 / **46** / 39, and on the
> `qou-n1dj` branch 148 / 103 / **45** / 38. The middle §Correction section is
> also one revision behind. The filename still carries the old `43-` slug
> because a beans title change does not rename the file; resolve this bean by
> `ls .beans/ | grep u87j`, never by slugifying the title.

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

## Final figures 2026-08-23 — measured on `origin/main`, in a worktree

An eighth parser bug turned up while checking the baseline, and it is the one
that matters most for reading this bean: `EXTENDS` split its clause on commas
**before** stripping `.{u, v}`, so `extends B.{u, v} R` became the two entries
`B.{u` and `v} R` and compared unequal against a plain `extends B R`. Every
mirror that spells its universes explicitly was reported as drift.

That is a false positive, and it had swallowed a real result: it hid the fact
that the `qou-n1dj` branch actually *fixes* one of these. Corrected numbers,
each measured by running the checker against the tree named:

| | `origin/main` | `claude/n1dj-volume-iso-reading-2026-08-22` |
|---|---|---|
| same-FQN pairs | 147 | 148 |
| identical (faithful mirrors) | 101 | 103 |
| **drifted** | **46** | **45** |
| distinct files | 39 | 38 |
| drifted pairs masking a `lean.ref` | 46 (= all) | 45 (= all) |

`QOU.QuantumObservableUniverse` is the difference. On `main` the sibling carries
a `volumeForm_epi` field the library never had; the `qou-n1dj` branch resyncs
it, and with universes normalised the pair is now genuinely identical rather
than "identical except `.{u, v}`". So the earlier note in §Notable entries about
"a 44th on main" was right in substance and wrong in count — it is one of the
46, not an extra one.

Baseline to use: **46 on `main` today, 45 once #5498 lands.**

### Option 1 is wired, not just built

`.claude/commands/prepare-merge.md` **§4a. Mirror-drift gate (BLOCKING on
growth)** runs it at `--baseline 46`. It sits in `prepare-merge` rather than
`.github/workflows/` because every workflow in this repo is
`workflow_dispatch`-only under the 2026-06-30 Actions-billing directive — §4b
already says the same thing about the precision gates. Treat the baseline as a
ratchet: lower it as the backlog drains, or the next regressions go unnoticed.

Options 2–4 remain open, and option 2 (reorder `lean.ref` resolution so the
Lake tree wins) would make most of option 3's hand-resync moot — worth deciding
before anyone spends a day on the 46.

## Option 2 measured 2026-08-23 — and it has to be split in two

Option 2 was written as one thing ("reorder `lean.ref` resolution so the Lake
tree wins"). Measured, it is two, and only one of them is viable.

Classification of every block `walkBlocks` yields under
`content/quantum-observable-universe`, with candidates 2–3 resolved through the
**canonical resolver** (`resolveCanonicalLean`, with a `LakeTreeCache`) rather
than a hand-rolled matcher — the `qou-2u26` lesson:

| | blocks |
|---|---|
| sibling **and** Lake candidate, resolving to **different** files | **338** |
| sibling and Lake candidate, same file (reorder is a no-op) | 0 |
| **sibling only** — no Lake candidate at all | **569** |
| Lake only, no sibling (unaffected either way) | 353 |
| neither | 2226 |
| total walked | 3486 |

- **2a — reorder, sibling demoted to last resort.** The 338 start being audited
  against the library declaration instead of the sibling; the 569 keep
  resolving, because the sibling is still in the chain. Viable.
- **2b — drop candidate 1 outright.** The same 338 move, *and* **569 blocks go
  unresolved**. Not viable, and worth stating plainly because "the Lake tree
  wins" reads like 2b.

**338 is the review surface, not 46.** The drift checker only compares
`structure`/`class` declarations that appear on both sides under the same
fully-qualified name; 46 of those disagree. The other ~292 of the 338 change
which file is audited without a *known* disagreement — and "no known
disagreement" here means "no same-FQN structure pair was found", which is not
the same as "the two files agree". Several of the 338 point at a Lake file that
is plainly not a mirror at all: `def:so3-generators`, `def:su2-basis` and
`prf:knot-eigenbasis-complete` all resolve to `lean/QOU/PathIntegrals.lean`, a
large multi-declaration module, via the basename/decl-name fallback.

So 2a is not a free win either: it would repoint 338 blocks' audits at files
nobody has checked are the right target. It fixes the masking and inherits a
different question.

**Do not read 2226 as a backlog.** `walkBlocks` yields every block kind, and
prose, remarks, tables and algorithms are not expected to carry Lean. That row
is "has no Lean on either route", not "is missing Lean it owes".

Reproduce: `scripts/` has no home for this yet — the measurement script is
`measure-option2.ts` in the session scratchpad. If option 2 goes anywhere it
should be re-run and committed alongside the change.

### One documentation bug found on the way

`BlockPaths.root` in `content/pipeline/qa-utils.ts` is documented as
*"Root name shared by all sibling files (e.g. `carbon-valence`)"*. The value is
the **full path stem** — `/abs/path/to/carbon-valence`. Joining it onto
`dirname(b.ts)`, as the docstring invites, doubles the path and matches nothing:
the first run of this measurement reported **0 siblings across 3486 blocks** and
looked plausible enough to nearly publish. Worth a one-line docstring fix in
folio-assistant.

## Option 2a graded 2026-08-23 — **the evidence does not support it. Recommendation withdrawn.**

I wrote above that 2a was "viable" and said in session that it was the one I'd
take. Grading the 338 says otherwise, and I am withdrawing that.

Two independent gradings of the 338 blocks whose audited file 2a would change:

**Which candidate produced the Lake target.** Candidate 2 is the direct module
path spelled in `lean.ref` — an author's deliberate pointer. Candidate 3 is the
basename / decl-name fallback the resolver reaches for when that module path
does not exist — a guess.

**The label test.** Does the file carry the block's `\label{…}` in a docstring?
This is the test that found four broken refs earlier in this batch when no
name-based index could. Presence is strong evidence; absence is weak, because
plenty of library files carry no labels at all.

| | both | lake-only | sib-only | neither | total |
|---|---|---|---|---|---|
| **cand 2** — deliberate module path | 2 | **4** | **4** | 24 | **34** |
| **cand 3** — basename guess | 33 | 24 | 44 | 203 | **304** |
| total | 35 | **28** | **48** | 227 | 338 |

Three things follow, and they point the same way:

1. **304 of 338 are candidate-3 guesses.** 2a would repoint nine out of ten of
   these audits at a file the resolver picked by basename, not at a target
   anyone chose.
2. **Where the label test speaks at all, it favours the sibling: 48 to 28.**
   Those 48 are blocks whose `\label` appears *only* in the sibling — 2a would
   move the audit off the one file demonstrably about that block.
3. **Even the strongest subset is a tie.** Among the 34 deliberate candidate-2
   refs, lake-only and sib-only are **4 and 4**, with 24 silent. There is no
   subgroup here where the evidence favours the Lake target — not even the one
   built out of the author's own pointers.

`cand3 / neither` alone is **203 blocks, 60 % of the population**: a guessed
target, and no label anywhere to adjudicate it.

### So what should happen

**Not a resolution reorder, in any global form.** The masking is real — 46
drifted pairs, all masking a `lean.ref` — but reordering treats 338 blocks to
fix 46, and on the only available evidence it would regress more of them than it
improves.

- **Option 1 (the gate) is the right primary fix** and is done: `prepare-merge`
  §4a, `--baseline 46`. It stops the population growing without touching
  resolution at all.
- **Option 3 (resync the 46) is now the natural follow-up**, not the fallback it
  was written as. It is bounded, it is exactly the defect, and it needs no
  decision about resolution order.
- **Option 4 (stop mirroring)** remains the root-cause fix and remains the
  largest.

The `cand3 / neither` 203 are worth their own look — a block whose `lean.ref`
resolves only by basename guess, to a file carrying nobody's label, is a
different defect from drift and is adjacent to `qou-2u26` / `qou-cu0a`. Not
opened as a bean here; measured and recorded so whoever wants it has the number.

Scripts: `measure-option2.ts` and `sample-338.ts` in the session scratchpad.
Both use the canonical resolver; re-run before quoting.

## Option 3 characterised 2026-08-23 — **there is no clerical subset. Do not batch this.**

Option 3 reads as the boring one: copy the right field set across, 46 times.
Started it, on the `quantum-observable-universes/` seven where this session
already had context, and stopped after two. It is not clerical, and the reason
generalises.

### Direction of drift is not readable from the field diff

Classifying the 45 pairs on this branch by which side has fields the other lacks:

| | pairs |
|---|---|
| **both** sides have fields the other lacks | **28** |
| library-only fields — *looks* like the sibling is behind | 12 |
| sibling-only fields — *looks* like the library is behind | 4 |
| order / rename only | 1 |

The 12 look like the clerical bucket. **They are not**, and
`QOU.SubstrateParameter` — two of them — shows why.

### Worked case: `QOU.SubstrateParameter`, where the library is the stale side

| | fields |
|---|---|
| library `lean/QOU/QuantumObservableUniverse/SubstrateParameter.lean:23` | `field : M → ℝ`, `field_pos`, `field_ge_one`, `not_root_of_unity` |
| siblings `substrate-parameter.lean:72`, `quantum-gauge-group.lean:44` | `field : M → R_q` |

The field diff says "library-only: `field_pos field_ge_one not_root_of_unity`",
i.e. sibling behind, add three fields. **The opposite is true.** The sibling's
own docstring:

> the archimedean properties (`q(p) > 0`, `q(p) ≥ 1`, not a root of unity) live
> on `ArchimedeanSubstrateField` below, **after the substrate→archimedean wall
> (AGENTS.md §7c)**.

The siblings have been migrated to the two-layer §7c shape — categorical
`SubstrateParameter` over the un-ordered `R_q`, archimedean properties on a
separate `ArchimedeanSubstrateField`. The library never was. And the **block is
the authority**: `substrate-parameter.md` defines
`q ∈ End(𝟙)` — categorical, no ordering, no `q ≥ 1`. The siblings match the
block; the library does not.

So "resync the sibling to the library" here would **undo a §7c migration**.

Note the checkers do not catch it: `check-wall-side` and `check-base-ring` both
**PASS** on the library file, because it is *wholly* archimedean rather than
mixed. Passing the wall gate means "not mixed", not "on the right side of the
wall".

### What doing it properly costs

The same split as `MassIdentity` → `ArchimedeanMassIdentity` (PR #5458), on a
much bigger object: **22 library files mention `SubstrateParameter`, with 85
field-access sites**, and it is the carrier of `q₀` — every mass number in the
corpus is downstream. Not started. It wants its own bean, its own branch, and a
numerical no-change check.

### Consequence for planning

- **No batch pass.** Every one of the 45 needs a judgement about which side is
  right, and the field-set diff does not supply it. The block's `.md` does, and
  reading it is the per-case work.
- **The 12 "library-only" are the trap, not the quick win** — that is precisely
  the bucket the `SubstrateParameter` pair sits in.
- **Sequence it as: block prose → decide the correct shape → fix whichever side
  is wrong.** Sometimes that is the library, and then it is not a resync at all.
- Option 1's gate stands regardless, and is the reason none of this is urgent:
  the population cannot grow while the baseline holds.

## New axis 2026-08-23 — §7c regime, and 7 pairs the field comparison called faithful

`check-mirror-drift.ts` now also compares which **side of the §7c wall** each
copy sits on, judged by the corpus's own `ARCHIMEDEAN_TYPE_RE` applied to field
*types*. Two mirrors can agree on every field **name** and still be on opposite
sides. Before this, the checker scored those as faithful mirrors.

On `main`: 147 pairs, **94** faithful (was 101), **46** drifted, plus

| | count |
|---|---|
| **`regime`-only** — same fields, opposite sides of the wall | **7** across 5 files |
| drifted pairs that **also** cross the wall | **10** |
| **total pairs with a §7c disagreement** | **17** |

Counted on its own axis, not folded into `drifted`, so the `--baseline 46` gate
in `prepare-merge` §4a is unchanged and a §7c figure will not move when someone
drains the drift backlog.

### The 7 that were invisible

| declaration | sibling | library | direction |
|---|---|---|---|
| `QOU.ArchimedeanObservation` | `quantum-observable-universes/observation.lean:74` | `…/GaugeTheory.lean:250` | lib archimedean |
| `QOU.QReebFlow` | `…/q-torsion-leaf.lean:55` | `…/Particles.lean:93` | lib archimedean |
| `QOU.QReebFlow` | `…/q-reeb-flow.lean:44` | `…/Particles.lean:93` | lib archimedean |
| `QOU.QTorsionLeaf` | `…/q-torsion-leaf.lean:65` | `…/Particles.lean:102` | lib archimedean |
| `QOU.ReebDecomposition` | `models-of-qous/reeb-decomposition.lean:46` | `…/Particles.lean:18` | lib archimedean |
| `QOU.BraidKnot.GBResidueSpectralSum` | `mass-theory/gb-residue-spectral-sum.lean:74` | `…/GBResidueSpectralSum.lean:67` | **sib** archimedean |
| `QOU.BraidKnot.RootOfUnity` | `mass-theory/gb-residue-spectral-sum.lean:49` | `…/GBResidueSpectralSum.lean:52` | **sib** archimedean |

**Five have the library on the archimedean side and the sibling algebraic** —
the `qou-6ome` shape, where the §7c migration reached the siblings and not the
library. Two go the other way. Direction is per-case; do not assume.

### The 10 drifted pairs that also cross the wall

`QOU.BraidsKnots.FibreFunctor`, `QOU.CRManifoldData` ×2, `QOU.CategoricalMobiusEnergy`,
`QOU.CategoricalQExtDeriv`, `QOU.ClassicalMobiusEnergy`, `QOU.KnotEmbedding`,
`QOU.SubstrateParameter` ×2, `QOU.Torsion.VacuumState`.

For these a field resync is not the fix, and the checker now says so in the
finding: *"a field resync will not fix this, a wall split will."* That is the
trap from §Option 3, made machine-visible.

### The good news: 17 pairs, ~9 library files

They cluster hard:

| library file | pairs |
|---|---|
| `QuantumObservableUniverse/Particles.lean` | 4 |
| `MobiusEnergy.lean` | 3 |
| `QuantumObservableUniverse/SubstrateParameter.lean` | 2 (`qou-6ome`) |
| `QuantumObservableUniverse/CRRealisation.lean` | 2 |
| `BraidKnot/GBResidueSpectralSum.lean` | 2 |
| `GaugeTheory.lean`, `MotivesArchimedean.lean`, `Instanton.lean`, `Torsion/BraneTower.lean` | 1 each |

So the §7c backlog is a **file-sized** job, not a pair-sized one — and
`Particles.lean` alone accounts for four. `SubstrateParameter.lean` is the one
with 22 downstream files behind it; the others are much smaller and are the
sensible place to learn the pattern before touching q₀.

### Why this axis had to be added rather than assumed covered

`check-wall-side` and `check-base-ring` **PASS** on every one of these files.
They fire on a file that *mixes* regimes; a declaration wholly on the wrong side
is not mixed. Passing the wall gate means "not mixed", not "on the right side of
the wall". Recorded at length on `qou-6ome`.
