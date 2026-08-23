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
