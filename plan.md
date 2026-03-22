# Migration Plan: Lean Content from `lean/` to `content/` Blocks

## Problem

Lean formalization lives in large monolithic files under `lean/QOU/` (e.g., `QuantumObservableUniverse.lean` at 1207 lines with 40+ declarations). The content-object architecture expects `.lean` files co-located as siblings alongside `.ts` and `.md` files under `content/`.

**Current**: 50 content blocks reference Lean declarations, but all actual code lives in ~23 centralized files under `lean/QOU/`.

**Target**: Each content block that needs Lean has its own `<block-name>.lean` file alongside `<block-name>.ts` and `<block-name>.md`.

## Architecture Decision: No Symlinks, Archive Old

- **Rename** `lean/` → `lean-archive/` (preserved for audit/QC reference)
- **Content-block `.lean` files** are the new authoritative source
- **Lake build integration** will be set up separately in a future phase
- No symlinks, no bridge — clean separation

### Directory layout after migration

```
lean-archive/                        ← renamed from lean/ (read-only reference)
  QOU/
    QuantumObservableUniverse.lean    ← original monolithic files preserved
    Torsion.lean
    ...

content/quantum-observable-universe/
  ch1-quantum-observable-universe/
    categorical-action.ts
    categorical-action.md
    categorical-action.lean          ← NEW: authoritative Lean source
  ch3-lifting-of-quantum-torsion/
    jet-prolongation.ts
    jet-prolongation.md
    jet-prolongation.lean            ← NEW: extracted from Torsion.lean
  ...
```

## Migration Steps

### Phase 1: Archive

1. `git mv lean lean-archive`
2. Update any references to `lean/` in CI, scripts, configs

### Phase 2: Create content-block `.lean` files (one chapter at a time)

For each content block with a `lean:` reference:

1. **Extract** the relevant declaration(s) from the corresponding `lean-archive/` file
2. **Create** `<block-name>.lean` in the content block's directory
3. **Add proper imports** — the extracted file must import its dependencies
4. **Wrap in correct namespace** — maintain `QOU.*` namespace
5. **Add `-- Ref:` citation** if any `sorry` is present (per CLAUDE.md rules)

**Order**: Process chapters in dependency order — ch1 definitions first (most depended on), then ch2-ch12.

**Chapter 1 (44 blocks)** — the bulk of the work, mostly from `QuantumObservableUniverse.lean`:
- Structures: FrobeniusHopfData, QuantumUniverse, QuantumObservableUniverse, etc.
- Theorems: categorical_dq_squared, categorical_irreducible, etc.
- Examples: CRManifoldData, InstantonConnection, etc.

**Chapter 2 (1 block)**: categorical-transport from `Elaboration.lean`
**Chapter 4 (1 block)**: knot-eigenbasis-complete from `PathIntegrals.lean`
**Chapter 11 (2 blocks)**: skein-mass-relation, terminal-resolution from `HadronicMass.lean`

### Phase 3: Update content manifests

For each migrated block's `.ts` file:
1. **Remove** explicit `file:` field (if present) — let sibling resolution find the `.lean`
2. **Update** `status:` to reflect actual proof state
3. **Update** `validation:` if it changed during extraction

### Phase 4: Verify

1. **Run** content validation pipeline (`content_validate`)
2. **Diff** extracted `.lean` against `lean-archive/` originals to confirm no code was lost
3. **Verify** no content block with `lean:` is missing its sibling `.lean` file

## Declarations NOT migrated (stay only in `lean-archive/`)

These files contain infrastructure not tied to content blocks:
- `Basic.lean` — foundational definitions
- `Glossary.lean` — term glossary
- `KnotTheory.lean`, `KnotRegistry.lean` — knot infrastructure
- `Calculations.lean`, `MassDerivation.lean` — computation support
- `GrobnerShirshov/*` — algebraic infrastructure
- `FormalGroups.lean` — supporting theory
- `Fred2005/` — external library

## Estimated Scope

- **50 content-block `.lean` files** to create
- **6 monolithic files** to split (QuantumObservableUniverse, Torsion, HadronicMass, PathIntegrals, Elaboration, + potentially others)
- **50 `.ts` manifests** to update
- **~7,000 lines** of Lean code to reorganize
