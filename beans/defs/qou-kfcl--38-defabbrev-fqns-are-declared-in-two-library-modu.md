---
# qou-kfcl
title: 38 def/abbrev FQNs are declared in two library modules each — those module pairs can never be imported together, and QOU.R_q means two different rings
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T16:49:53Z
updated_at: 2026-11-16T19:05:00Z
parent: qou-rtxm
---


## Verified by compiling, not inferred

Found while trying to fix one pair of [`qou-u87j`](qou-u87j--43-content-block-lean-siblings-redefine-a-library.md),
and it is what blocked that fix.

```lean
import QOU.BraidKnot.CasimirShared
import QOU.CategoricalDqSquared
```

```
error: import QOU.CategoricalDqSquared failed, environment already contains
       'QOU.q_param' from QOU.BraidKnot.CasimirShared
```

Not a warning. **The two modules cannot both be imported by anything, ever.**

### The population

Scanning every `def`/`abbrev` in `folio/quantum-observable-universe/lean`,
tracking `namespace` / `section` / `end`: **38 fully-qualified names are
declared in more than one module.** Each is a module pair (or triple) that is
mutually un-importable.

A sample, to show it is not one corner of the tree:

| FQN | modules |
|---|---|
| `QOU.Archimedean.R_q` | `Archimedean/GroundRing.lean`, `Archimedean/WeierstrassProjection.lean` |
| `QOU.Archimedean.T_pp`, `T_nn` | `Archimedean/TransferMatrix.lean`, `Archimedean/beta_decay_transfer_matrix.lean` |
| `QOU.BraidKnot.qInt` | `BraidKnot/ZeqNRhoCorrection.lean`, `BraidKnot/wedderburn_trace_identity.lean` |
| `QOU.BraidsAndKnots.PartitionOf5` | three modules |
| `QOU.BraidsKnots.S3`, `cyclic_perm`, `resolvent` | `BraidsKnots/RamifiedDiscFusion.lean`, `QOU/scratch_fusion.lean` |

### The one that is not merely a collision — `QOU.R_q` denotes two different rings

| module | definition |
|---|---|
| `QOU/BraidKnot/CasimirShared.lean:46` | `abbrev R_q := RatFunc ℚ` |
| `QOU/CategoricalDqSquared.lean:60` | `abbrev R_q := LaurentPolynomial ℤ` |

Same fully-qualified name, **a field of rational functions in one and a Laurent
polynomial ring in the other**. Anything written "over `R_q`" in namespace `QOU`
means whichever one the importer happened to reach. `CasimirShared.lean` also
declares `QOU.Braiding.R_q := LaurentPolynomial ℤ` further down, so that one
file supplies two different `R_q`s under two namespaces.

Corpus-wide there are **100** `abbrev R_q` declarations across library and
siblings.

### Why nothing catches it

- **The whole-tree build passes.** `scripts/lean-direct-cone.sh --all` compiles
  each module against its own import cone; no *existing* module imports both
  halves of any colliding pair, so nothing ever trips. Measured 2026-08-23:
  2029/2040 modules, `err=0`. A green tree is not evidence here.
- **`check-mirror-drift` reports `duplicatesInLibrary: 0`** — it tracks
  `structure`/`class` only, so `def`/`abbrev` collisions are outside it.
- The failure appears only when someone writes a **new** module needing both,
  which is exactly how this surfaced.

### What it cost, concretely

`qou-u87j`'s `QOU.CategoricalQExtDeriv` pair needs `R_q` in
`lean/QOU/QuantumObservableUniverse/Instanton.lean`. There is no "the" `R_q` to
import: five library declarations under three namespaces, two of them
disagreeing about the ring. That fix is parked on this bean.

### Options

1. **One canonical `R_q`.** `QOU.Archimedean.GroundRing` already looks intended
   as the home (`abbrev R_q := LaurentPolynomial ℤ`, and its own docstring is
   referenced from siblings as "the compiled definition"). Point everything at
   it and delete the rest. The `RatFunc ℚ` one needs a different name — it is a
   different object, not a duplicate.
2. **Gate it.** Extend `check-mirror-drift`'s `duplicate-in-library` finding to
   `def`/`abbrev`, or add a standalone check. Cheap, and it is the only thing
   that stops 38 becoming 40.
3. **Both.** 2 first — it is small and it stops the growth while 1 is decided.

### Related

- [`qou-u87j`](qou-u87j--43-content-block-lean-siblings-redefine-a-library.md) — where this surfaced; the `CategoricalQExtDeriv` fix is blocked on it.
- `qou-ooeb` (completed) is a *different* thing: redundant `QOU.Foo.` prefixes on declarations inside `namespace QOU.Foo`, a style warning. These are hard import errors.

Not started.

## Correction and gate 2026-08-23 — 65 FQNs / 64 pairs, and the first count was wrong

**The 38 above is superseded, and so is the 80 I replaced it with.** Both came
from ad-hoc scans; the checker now exists and its figure is:

| | value |
|---|---|
| declarations scanned | 33 798 |
| **FQNs declared in >1 module** | **65** |
| **mutually un-importable module pairs** | **64** (across 70 modules) |

Three passes, three numbers, and the corrections are the interesting part:

1. **38** — first ad-hoc scan, `def`/`abbrev` only. Undercounted by ignoring
   every other declaration kind, and the import error does not care which kind
   collided.
2. **80 / 99 pairs** — all kinds, but the name capture stopped at the first dot.
   So `theorem SurrealField.IsFinite.pow` read as a redeclaration of
   `class SurrealField`, and `def SurrealField.finiteSubring` as a third. That
   manufactured a three-module collision in `AppendixSurreals` out of nothing —
   and `SurrealField` is a class this batch's own `SpectralNormalForm` work
   depends on, so it was a plausible-looking false alarm in exactly the wrong
   place.
3. **65 / 64** — dotted names captured whole. Pinned by a test.

The `QOU.R_q` / `QOU.q_param` finding survives all three unchanged, because it
was verified by compiling rather than by counting:

```
QOU.R_q      abbrev  BraidKnot/CasimirShared.lean:46      (RatFunc ℚ)
QOU.R_q      abbrev  CategoricalDqSquared.lean:60         (LaurentPolynomial ℤ)
QOU.q_param  def     BraidKnot/CasimirShared.lean:49
QOU.q_param  def     CategoricalDqSquared.lean:61
```

### Option 2 is built

**folio-assistant `scripts/check-duplicate-decls.ts`**, with 12 scanner tests.
Growth gate: `--baseline 65` (exit 3), `--max 0` for the end state, `--json` /
`--tsv` for the list. Verified: exit 2 over `--max`, 0 at `--baseline 65`, 64 on
an unknown package.

```sh
bun run <folio-assistant>/scripts/check-duplicate-decls.ts --package qou --baseline 65
```

Not yet wired into `prepare-merge`; that is a one-paragraph addition next to
§4a when someone wants it.

Documented limits, reported rather than silently filtered: `private`
declarations are counted though they do not really collide, and a declaration
head that wraps before its name is missed. **Verify any finding with the
two-line import before acting on it** — that is how the one case that mattered
was established, and it is the only method here that has not been wrong yet.

Option 1 (one canonical `R_q`) is untouched.

## Triage 2026-08-23 — 2 of 65 are mechanical, and one of those is already done

Compared the head-line definition text of every duplicated FQN:

| | count |
|---|---|
| definitions **byte-identical** — safe mechanical dedup | **2** |
| definitions differ — needs judgement | 63 |

So this bean has no mechanical subset either, which is the same conclusion
`qou-u87j` option 3 reached about mirror drift, arrived at independently. Two
scans of two different populations, same answer: **the duplication is not
clerical.**

### Done: `QOU/scratch_fusion.lean` deleted

Forty lines, literally named "scratch", imported by nothing, in no `lean.ref`,
not in the `QOU.lean` umbrella — and all five of its declarations already live
in `QOU/BraidsKnots/RamifiedDiscFusion.lean` under the same FQNs, with
docstrings and the label `prop:ramified-disc-fusion` the scratch copy lacks.

**65 → 60 duplicated FQNs, 64 → 63 pairs, 70 → 68 modules.**
`prepare-merge` §4a baseline lowered to 60 in the same change.

### Not done: `QOU.Archimedean.R_q`, and why it is not a one-liner

The other byte-identical case is `abbrev R_q := LaurentPolynomial ℤ` in both
`Archimedean/GroundRing.lean:33` and `Archimedean/WeierstrassProjection.lean:26`.
`WeierstrassProjection` also duplicates `q_param` and `q_inv_param`, and **uses**
its copies — 14 references. So it cannot simply drop them.

The obvious move, importing `GroundRing`, has a cost worth stating rather than
paying silently: `WeierstrassProjection.lean` currently has **three** Mathlib
imports, while `GroundRing.lean` pulls `Mathlib.Tactic` and
`QOU.MathlibExt.QIntegerCanonical`. Pointing a light module at a heavy one to
fix a three-line duplication is a build-cost regression, not a cleanup.

What this actually wants is a **minimal ground-ring module** — `R_q`,
`q_param`, `q_inv_param` and nothing else — that both import, with
`GroundRing.lean` keeping its tactic-heavy material on top. That is a module-
layout decision, so it is option 1 and it is the owner's, not something to
invent at the tail of a session. No cycle blocks it: `GroundRing` does not
import `WeierstrassProjection`.

Corpus-wide there are still 100 `abbrev R_q` declarations, so whatever module
gets created is the target for a much wider sweep than these two.

## 2026-08-23 — the minimal ground-ring module exists, and unblocked `qou-u87j`

The owner call this bean deferred has been taken: `QOU/GroundRingCore.lean`
is the minimal module it described — `R_q`, `q_param`, `q_inv_param`,
`q_param_mul_inv`, and **one** Mathlib import
(`Mathlib.Algebra.Polynomial.Laurent`). So pointing a light module at it costs
nothing, which was the objection to importing `Archimedean/GroundRing.lean`.

Four modules import it now: `Archimedean/WeierstrassProjection.lean` (its three
duplicate declarations are gone — the `abbrev R_q` at line 25 is a comment
recording the removal), `QuantumObservableUniverse/SubstrateParameter.lean`,
`QuantumObservableUniverse/Instanton.lean`, and `CategoricalDqSquared.lean`.

No `R_q`, `q_param` or `q_inv_param` appears in the duplicate report any more.

### Counts, re-measured against **current** `origin/main` (797db0ebf7)

| | main @797db0ebf7 | this branch |
|---|---|---|
| duplicated FQNs | 66 | **56** |
| un-importable module pairs | 65 | **61** |
| modules involved | 72 | **64** |
| total declarations scanned | 34138 | 33793 |

Earlier entries in this bean quoted 65 → 60 and 64 → 63 against the
**merge-base**; `main` has moved 1206 commits since, hence the re-measurement.
`prepare-merge` §4a baseline updated to 56 in the same change.

### Still open

`Archimedean/GroundRing.lean:33` still declares its own
`abbrev R_q := LaurentPolynomial ℤ`. It is not a *duplicate* — the FQN is
`QOU.Archimedean.R_q`, distinct from `QOU.GroundRing.R_q` — so no checker
flags it and nothing is un-importable. It is redundancy, not breakage: two
names for one ring. Corpus-wide there remain ~100 `abbrev R_q` declarations,
and `GroundRingCore` is now the module they should collapse into.

## 2026-08-23 — after merging `main`: 56 → 57, and the +1 is not ours

| | `main` @797db0ebf7 | this branch, pre-merge | merged |
|---|---|---|---|
| declarations scanned | 34 138 | 33 793 | 34 136 |
| duplicated FQNs | 66 | 56 | **57** |
| un-importable module pairs | 65 | 61 | 62 |
| modules involved | 72 | 64 | 66 |

Set-differenced the pre- and post-merge FQN lists rather than reading the
totals: **1 new, 0 gone.** The new one is
`QOU.Mathlib.Schensted.wordOfPerm_injective`, a `theorem` at both
`QOU/Mathlib/SchenstedPermInjective.lean:42` and
`QOU/Mathlib/SchenstedRSKPairInjective.lean:68`, which arrived with `main`'s
RSK–Burnside work.

`prepare-merge` §4a baseline **raised** 56 → 57 with that reason stated in the
file — a ratchet loosening should never be silent. Put it back to 56 when that
pair is resolved.


---

## RE-MEASURED 2026-08-30 — 26 compiler-confirmed pairs, not 38, and the guard is now committed (PR #6191)

**Do not quote the 38.** It was a parse-only count with one compiler
spot-check. Today's figure is **26 module pairs over 22 distinct
fully-qualified names**, every one confirmed by writing a two-line probe
that imports both modules and running `lean` on it. Propose stage offered
28; the compiler rejected 2.

**The 38 → 26 difference is NOT attributed, and it is both things at once.**
Real drain: `QOU/scratch_fusion.lean` no longer exists, so the
`QOU.BraidsKnots.S3 / cyclic_perm / resolvent` rows are gone, and the
`QOU.Archimedean.R_q` row was fixed today (PR #6140). Detector change: four
false-positive classes were found and fixed while calibrating, listed below.
I did not separate the two contributions and the numbers should not be read
as though I had.

**This bean's own headline example has drained.** `import
QOU.BraidKnot.CasimirShared` + `import QOU.CategoricalDqSquared` — quoted
above as the motivating error — **compiles clean today**. Re-run it before
citing it.

### The four detector defects, because each was a wrong count first

| class | what it did before the fix |
|---|---|
| `import` indented inside a docstring | made `GroundRingCore` look like it imported `CasimirShared`, inventing a cross-module `R_q` shadow in `WeierstrassProjection` that the compiler denies outright (`QOU.R_q` is not in scope there at all) |
| `namespace` / `abbrev` inside `/- -/` | corrupted namespace stacks |
| `section ... end` popping the namespace stack | same |
| **dotted decl name truncated at its first component** — `def A5Irrep.dim` read as `A5Irrep` | manufactured a duplicate out of every inductive's namespace; the propose stage claimed **5 live errors** on a corpus that compiles green |

The last row is the lesson: **a propose-stage count that contradicts a green
build is a bug in the detector.** It happened twice before it was believed.

### Guard

[`scripts/lean-duplicate-fqn-audit.py`](scripts/lean-duplicate-fqn-audit.py)
— `--verify` runs the compiler per pair; `--check-baseline` is a drain-only
ratchet against
[`docs/audits/lean-duplicate-fqn-baseline.json`](docs/audits/lean-duplicate-fqn-baseline.json).
Both controls run: clean baseline exits 0; removing two entries exits 1
naming exactly those two.

### Still open (what this bean now tracks)

Draining the 26. Each needs a per-pair judgement — which name is canonical,
whether the two bodies are meant to be the same object — so it was
deliberately kept out of the guard PR. None is a live error today: no module
imports both halves of any pair. They are latent, each one waiting for
whoever writes the module that needs both.


## Drain triage + the thing that was actually holding the 26 apart (2026-08-30)

[`docs/audits/2026-08-30-duplicate-fqn-drain-triage.md`](docs/audits/2026-08-30-duplicate-fqn-drain-triage.md).

**`QOU.lean` reaches 1290 of the 2389 modules under `QOU/` — 1099 (46 %) are
outside the root build.** Of the 26 pairs, **0** have both modules reachable
from it, 19 have exactly one, 7 have neither. That is the consistency test:
a pair with both sides in the root build would make `lean QOU.lean` fail, and
it exits 0. `QOU.Mathlib.addCell` is the worked case — `YoungDiagramAddable`
is imported by `QOU.lean`, `YoungDiagramAddCell` is not.

**So `lean QOU.lean` exit 0 is not a corpus-wide gate** and must not be quoted
as one. The corpus-wide measurement is `lean_cone_triage.py` over every module
(2128 up-to-date / 210 ok / 0 blocked after #6140); that is what "180 → 0"
rests on, and it is unaffected.

Drain shape: **11** names have a zero-importer side, **10** have zero
importers on both sides, and only **3** need a judgement about which
definition is canonical — `QOU.BraidKnot.writhe`, `QOU.Mathlib.addCell`,
`QOU.Mathlib.IsAddableCell`, the last two being one decision (same module
pair). Rename rather than delete: no direct importer under `QOU/` does not
mean dead, since a content-block `.lean` sibling can still resolve from it.


### WITHDRAWN: "the 21 mechanical renames are safe to batch"

Opening the first pair refutes it. `QOU.Archimedean.T_pp` exists **three**
times, not twice: the two library modules the audit reports, plus
`mass-theory/beta-decay-transfer-matrix.lean` — a **content-block sibling in
the same namespace**, drifted from the library copy (195 lines vs 97, a
bespoke `TM` vs `Matrix (Fin 2) (Fin 2) ℝ`). Its `.ts` sets
`lean: { ref: "qou:QOU.Archimedean.beta_decay_transfer_matrix", validation:
"not_checked" }`, and the sibling wins candidate-1 resolution — so the sibling
is what the block's checkers audit while the library file is what collides.

Renaming in the library file to drain a collision would push a drifted mirror
further apart. **The drain is entangled with `qou-u87j`** (mirror drift,
`check-mirror-drift.ts`, 141 same-FQN pairs / 35 drifted). Each pair needs a
content-sibling check first; there is no safe blind batch.

The audit scans `lean/QOU/` only — recorded as a SCOPE section in the script
docstring. A clean run is **not** evidence a name is unambiguous corpus-wide.


## DRAINED 2026-08-30: 26 pairs → 7

19 of 24 names gone, all library-only (no content-block sibling), which is
what the surface audit established and why the drain waited for the join.
Method: nest the enclosing namespace one level deeper in the zero-importer
module (11 modules); `NuclearGroebnerReduction` renamed `BraidWord` →
`NuclearBraidWord` instead, because a live `lean.ref` names
`QOU.Archimedean.nuclear_groebner_reduction` in that file. Compiler-verified
throughout: each module `lean`-direct exit 0 with olean rebuilt,
`lean QOU.lean` exit 0, `--verify` 26 → 7, baseline regenerated and passing.

**The 7 left are decisions.** Five entangled with a sibling (`T_pp`, `T_nn`,
`BraidKnot.heckeH`, `qInt`, `writhe`) — drain with `qou-u87j`. Two are one
call over one module pair: `addCell` / `IsAddableCell`,
`YoungDiagramAddCell` (2 importers) vs `YoungDiagramAddable` (1, in the root
build), both consumed.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Canonical Namespace & GroundRingCore Audit (PR #8157)
- Verified `QOU/GroundRingCore.lean` (`QOU.GroundRing.R_q`, `q_param`, `q_inv_param`, `q_param_mul_inv`) and isolated `QOU.Foundations.FrobeniusHopfMarkovBridge` in its own conflict-free namespace wired into `QOU.lean` (0 duplicate FQNs).
- PR: https://github.com/litlfred/qou/pull/8157 (commit `16f8c01498462170d1ad98f5b5426233d3feea7d`). Status kept `in-progress`.
