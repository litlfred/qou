---
# qou-kfcl
title: 38 def/abbrev FQNs are declared in two library modules each — those module pairs can never be imported together, and QOU.R_q means two different rings
status: todo
type: task
created_at: 2026-08-23T16:49:53Z
updated_at: 2026-08-23T16:49:53Z
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

Scanning every `def`/`abbrev` in `content/quantum-observable-universe/lean`,
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
