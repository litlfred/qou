---
# qou-hmhw
title: Three structures named FrobeniusHopfSubstrate with different field sets -- the markovZ overload defect again
status: todo
type: task
priority: normal
created_at: 2026-09-14T19:43:55Z
updated_at: 2026-09-14T19:44:26Z
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
