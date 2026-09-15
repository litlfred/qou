---
# qou-hmhw
title: Three structures named FrobeniusHopfSubstrate with different field sets -- the markovZ overload defect again
status: completed
type: task
priority: normal
created_at: 2026-09-14T19:43:55Z
updated_at: 2026-09-15T06:46:24Z
---

## Measured 2026-09-14 (PR #7369, while adding the Hopf antipode axiom)

Three DIFFERENT structures carry the name `FrobeniusHopfSubstrate`, in three
files, with three different field sets. Same name, incompatible objects — the
`markovZ` overload defect (`qou-961o`) one namespace over.

| file | fields |
|---|---|
| `quantum-observable-universes/frobenius-hopf-substrate.lean` | the real one: `obj, mul, unit, comul, counit, antipode, frobeniusForm, coevaluation` + 11 laws |
| `quantum-observable-universes/categorical-reeb-derivation.lean:38` | `obj, mul, unit` |
| `quantum-observable-universes/substrate-self-duality.lean:32` | `obj, comul, frobeniusForm` |

The latter two are file-local minimal carriers that happen to reuse the name.
`categorical-reeb-derivation.lean:64` even has
`... extends FrobeniusHopfSubstrate C where`, extending its own local
three-field copy rather than the eight-field block.

### Why it matters, concretely

The 2026-09-14 antipode-axiom change (PR #7369, `ed78817432`) added eight law
fields including `antipode_left` / `antipode_right` to the REAL structure.
Neither local copy carries an antipode at all, so neither was touched — which
is correct, and is also exactly the failure mode: a reader or a later agent
asking *"does the Frobenius-Hopf substrate have an antipode axiom?"* gets a
different answer depending on which of the three they resolve, and nothing in
the name distinguishes them.

Same shape as `markovZ`: a name that spans incompatible objects keeps accreting
declarations while the question underneath it is settled in only one of them.

### Not fixed here, deliberately

Renaming touches consumers in two files outside this PR's scope, and the right
target names are a judgement call (`ReebSubstrateData`? `SelfDualityData`?
or make both `extends` the real structure, which changes their obligations).
Recorded rather than silently fixed — per AGENTS.md "ASK THE OWNER BEFORE
CHANGING THINGS", this is neither a precision increase nor corpus-derived.

### Suggested resolution, as judgement not finding

Rename the two local carriers to say what they are
(`ReebAlgebraData` / `SelfDualPairingData`), leaving the bare name meaning the
eight-field block — the same move that resolved `markovZ`. Cheap: both are
file-local with no cross-file consumers of the NAME, only of the declarations
that take them.


## 2026-09-15 — DONE. The collision was on the FULLY QUALIFIED name

Measured before renaming: all three files declare `namespace
QOU.AlgebraicSubstrate`, so all three structures are
`QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate` -- one fully qualified name,
three incompatible field sets. Latent rather than a build error only because
nothing imports two of them, and a content block's
`lean.ref: "qou:QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate"` is ambiguous
today. That is sharper than this bean's own "three structures named ...".

Renamed on owner authorisation (2026-09-15), per this bean's own suggestion:

  categorical-reeb-derivation.lean  obj, mul, unit         -> ReebAlgebraData
  substrate-self-duality.lean       obj, comul, frobForm   -> SelfDualPairingData
  frobenius-hopf-substrate.lean     8 fields + 11 laws     -> unchanged

`.lean`-only change. Neither local carrier's `.ts` referenced the colliding
name (they point at `CategoricalReebDerivation` / `substrate_self_duality`),
and `definition-index.md`'s single mention is the canonical block's.

Also withdrew the reeb file's "Keep the two in sync" note, which is what
produced the collision: they are different structures with different
obligations, so there is nothing to synchronise. Each docstring now states what
its carrier is NOT -- in particular that the antipode axioms added on
2026-09-14 (`qou-c64q`) do not reach it.

Verification: `lean` -DautoImplicit=false -s 65536, exit 0 zero warnings on
both. One `structure FrobeniusHopfSubstrate` declaration remains in the tree;
every other occurrence is prose.

PR #7413, issue #7412. Completing under the AGENTS.md rule 13a carve-out: the
whole task was mechanical (a rename), and it touches no open conjecture.
