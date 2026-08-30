# The orphan `.lean` siblings are 4, not 8 — and two are stale copies

**Date:** 2026-08-29 · **Bean:** `qou-hjf4`
**Corrects:** [`2026-08-24-sibling-duplication-is-partly-mandated.md`](2026-08-24-sibling-duplication-is-partly-mandated.md) §Method note
**Tool:** [`scripts/duplicate-class-declaration-census.py`](../../scripts/duplicate-class-declaration-census.py) `--json`

---

## Two corrections to my own earlier claims, both measurement errors

### 1. "8 collision groups have a `.lean` sibling with no `.ts` at all" — it is 4

That figure came from classifying 437 sibling-side files by block kind, where
8 fell into a *no-`.ts`* bucket. Re-measured directly against `main` on
2026-08-29 by taking every file in every same-namespace collision group and
testing `Path(f).with_suffix('.ts').exists()`:

| | count |
|---|---|
| collision files with no `.ts` | 134 |
| …of which are library modules under `/lean/QOU/` (a `.ts` is not expected) | 130 |
| **…of which are content-tree orphans** | **4** |

The old bucket did not separate library modules from content siblings, so it
was counting a different thing. 4 is the number of files that are neither a
content block nor a library module.

### 2. "The ledger has 268 entries and none of them are library files"

Wrong, and wrong in a way worth naming because it is the recurring class in
this arc: I queried `entry.get("file")`, **a field the entries do not have**.
The path is the ledger *key* (`<path>::<decl>::<criterion>`), so every lookup
returned `None` and the distinct-file count came out as 1.

Re-measured off the keys, `lean-vacuity-review-ledger.json` covers **187
files, 144 of them under `/lean/QOU/`**. Library coverage is its main
business.

**The consequence is the opposite of what I said.** I had proposed asking
whether the ledger is intended to cover library files at all. It plainly is,
so there is no scope question — and the absence of `ConditionalClasses.lean`
(0 entries) and `PvsNPQou` (0 entries) is a detector gap *inside* scope, not a
boundary. Recorded as `qou-sycn`; `core-levi-form` does have 2 entries.

## The four, read

| file | what it is |
|---|---|
| `quantum-universes/topological-mass-formula.lean` | **stale copy** — the live block triple is `mass-theory/topological-mass-formula.{ts,md,lean}` |
| `quantum-observable-universes/reeb-gauge-group.lean` | **left behind by a demotion** — its block is now a glossary `remark` |
| `braids-and-knots/frobenius-antipode-lean-stub.lean` | free-standing toy model, self-described stub |
| `mass-theory/qbeta_c3_keystone_interaction.lean` | free-standing, hardcoded decimal literals |

### `topological-mass-formula` — a same-name, same-namespace, *different-kind* clash

The live block is `mass-theory/topological-mass-formula.ts`, which declares
`label: "prop:topological-mass-formula"` and has `.md` + `.lean` siblings. The
orphan sits two chapters away in `quantum-universes/` with no `.ts` and no
`.md`. Both open `namespace QOU.Torsion`, and both declare
`ArchimedeanMassFormula` — as **different kinds**:

```
STRAY  62: structure ArchimedeanMassFormula (M : Type*) extends TopologicalMassDecomposition M
LIVE   67: theorem   ArchimedeanMassFormula
```

Five `.ts` files reference `prop:topological-mass-formula` (four via
`interprets`, two via `uses`); all of them resolve to the live block.

### `reeb-gauge-group` — the block was demoted, the Lean was not removed

The file's own header records `LaTeX label: def:reeb-gauge-group`. **No `.ts`
anywhere declares that label.** What exists is
`glossary/glossary-reeb-gauge-group.ts`, a `remark` with
`label: "rem:glossary-reeb-gauge-group"` and `defines: ["reeb-gauge-group"]`.

Per AGENTS.md §4b a glossary block is a `remark` and requires no Lean file. So
this is a `definition` block that became a glossary entry, leaving its sibling
behind. Its `structure ReebGaugeGroup (R : Type u) [CommRing R]` is clean
generic-`R` under §7c; the file is not wrong, it is unowned.

### The two free-standing files

`frobenius-antipode-lean-stub.lean` (169 lines) names itself a stub and
declares a toy `structure HeckeAlgebra (_n : ℕ) (_q : ℝ) where coeff : ℝ` — a
one-real-number model that discards both its index and its parameter (note the
underscore-prefixed binders), with `markovTrace _ _ a := a.coeff`. It is
honest about being a stub in its docstring, but it puts `HeckeAlgebra`,
`markovTrace`, `heckeMul`, `heckeSigma` into the tree as names of a model that
is not the Hecke algebra. `HeckeAlgebra` is declared in 6 files corpus-wide.

`qbeta_c3_keystone_interaction.lean` (35 lines) defines
`Vol_4_1 : ℝ := 2.029883212819307` and `substrate_u : ℝ := 0.008505403136757`
as decimal literals. Those are witnessed quantities elsewhere in the corpus;
carrying them as literals in an unowned file is the shape
`local/witnessed-values` exists to prevent. Not adjudicated here.

## Scope — what "collision" does and does not mean here

`content/<paper>/lean/lakefile.toml` declares the `QOU` library with
`srcDir = "."` (i.e. `content/quantum-observable-universe/lean/`) and
`globs = ["QOU", "QOU.+"]`. **Content-block siblings live outside that
`srcDir`**, so they are not Lake modules and are never simultaneously
imported. `lake build QOU` does not compile them; the sibling QA gate and
`lean`-direct do.

So the `ArchimedeanMassFormula` clash is **latent, not build-breaking** —
the same scoping the `core-levi-form` note recorded. Stating it as an import
collision would be an over-claim, and this section exists so the next reader
does not make it.

## Disposition

Nothing in `content/` changed. Two are clearly resolvable and two are
judgement calls:

1. **`quantum-universes/topological-mass-formula.lean`** — a stale copy of a
   block that lives elsewhere, unreferenced and unimported. Deleting it is the
   §0a disposition ("do not keep a stub when the real formalisation exists"),
   but it is a content deletion and is left for the author.
2. **`quantum-observable-universes/reeb-gauge-group.lean`** — either re-home it
   under `lean/QOU/` as a library module (the structure is sound and generic),
   or delete it as part of the demotion that orphaned it.
3. **`frobenius-antipode-lean-stub.lean`** — authorial: is the toy Hecke model
   wanted at all, and if so should it be namespaced away from the real one?
4. **`qbeta_c3_keystone_interaction.lean`** — route the two decimal literals to
   their witnesses, or record why an unowned file holds them.
