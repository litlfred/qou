# Migration Plan: Lean Content from `lean/` to `content/` Blocks

## Problem

Lean formalization lives in large monolithic files under `lean/QOU/` (e.g., `QuantumObservableUniverse.lean` at 1207 lines with 40+ declarations). The content-object architecture expects `.lean` files co-located as siblings alongside `.ts` and `.md` files under `content/`.

**Current**: 50 content blocks reference Lean declarations, but all actual code lives in ~23 centralized files under `lean/QOU/`.

**Target**: Each content block that needs Lean has its own `<block-name>.lean` file alongside `<block-name>.ts` and `<block-name>.md`.

## Key Constraints

1. **Lake build must still work** — Lake expects source files under `lean/` with `srcDir = "."` in `lakefile.toml`
2. **Import graph** — Declarations depend on each other; splitting requires careful import management
3. **Namespace preservation** — All declarations stay under `QOU.*` namespace
4. **Existing validation** — The `lean-file-exists` constraint already checks for sibling `.lean` files
5. **Non-content Lean code** — Some `.lean` files (Basic.lean, Glossary.lean, GrobnerShirshov/, Fred2005/) contain infrastructure not tied to content blocks

## Architecture Decision: Symlink Bridge

**Approach**: Content-block `.lean` files are authoritative. Symlinks under `lean/QOU/ContentBlocks/` point back to them so Lake can discover and build them.

Why symlinks over alternatives:
- **vs. copy script**: Symlinks are live — no stale copies, no build step
- **vs. changing srcDir**: Lake's srcDir can't span `lean/` and `content/` simultaneously
- **vs. moving everything to content/**: Infrastructure Lean files (Basic, Glossary, GrobnerShirshov) don't map to content blocks

### Directory layout after migration

```
content/quantum-observable-universe/
  ch1-quantum-observable-universe/
    categorical-action.ts
    categorical-action.md
    categorical-action.lean          ← NEW: authoritative Lean source
  ch3-lifting-of-quantum-torsion/
    ...

lean/QOU/
  Basic.lean                         ← stays (infrastructure)
  Glossary.lean                      ← stays (infrastructure)
  GrobnerShirshov/                   ← stays (infrastructure)
  ContentBlocks/                     ← NEW: symlink directory
    Ch1/
      CategoricalAction.lean → ../../../../content/.../categorical-action.lean
    Ch3/
      ...
  QuantumObservableUniverse.lean     ← DELETED after extraction
  Torsion.lean                       ← DELETED after extraction
```

## Migration Steps

### Phase 0: Preparation

0a. **Create the branch** `claude/migrate-lean-content-tOeTV`
0b. **Build a declaration → content-block mapping** by cross-referencing:
    - All 50 `.ts` files with `lean.decl` fields
    - All top-level declarations in the 23 `.lean` files
    - Identify declarations that do NOT map to any content block (keep in `lean/`)
0c. **Identify dependency order** — which declarations depend on which (via imports and type references)

### Phase 1: Create content-block `.lean` files (one chapter at a time)

For each content block with a `lean:` reference:

1. **Extract** the relevant declaration(s) from the monolithic `.lean` file
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

### Phase 2: Create symlink bridge for Lake

1. **Create** `lean/QOU/ContentBlocks/` directory structure mirroring chapters
2. **Create symlinks** from `lean/QOU/ContentBlocks/Ch<N>/<CamelCase>.lean` → content block `.lean` files
3. **Create** a `lean/QOU/ContentBlocks.lean` barrel import file
4. **Update** `lean/QOU.lean` root import to include `ContentBlocks`
5. **Update** `lakefile.toml` if needed (shouldn't be — symlinks are transparent to Lake)

### Phase 3: Update content manifests

For each migrated block's `.ts` file:
1. **Remove** explicit `file:` field (if present) — let sibling resolution find the `.lean`
2. **Update** `status:` to reflect actual proof state
3. **Update** `validation:` if it changed during extraction

### Phase 4: Remove extracted code from monolithic files

1. **Remove** extracted declarations from `QuantumObservableUniverse.lean`, `Torsion.lean`, etc.
2. **Replace** with imports from the new content-block modules
3. **Delete** any monolithic file that becomes empty after extraction
4. **Update** all remaining cross-references

### Phase 5: Verify

1. **Run** `lean_diagnostic_messages` on all new `.lean` files
2. **Run** content validation pipeline (`validate.ts`)
3. **Run** `lean_verify` on key theorems
4. **Check** that `lake build` succeeds end-to-end
5. **Verify** no orphaned declarations remain

## Declarations NOT migrated (stay in `lean/`)

These files contain infrastructure or declarations not tied to content blocks:
- `Basic.lean` — foundational definitions
- `Glossary.lean` — term glossary
- `KnotTheory.lean`, `KnotRegistry.lean` — knot infrastructure
- `Calculations.lean`, `MassDerivation.lean` — computation support
- `GrobnerShirshov/*` — algebraic infrastructure
- `FormalGroups.lean` — supporting theory
- `Fred2005/` — external library

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Circular imports after splitting | Map dependency DAG before splitting; process in topological order |
| Symlinks break on Windows | Add `.gitattributes` for symlink handling; document requirement |
| Lake can't follow symlinks | Test with single symlink first before full migration |
| Shared helper defs used by multiple blocks | Keep shared helpers in `Basic.lean` or create `Common.lean` |
| Git treats symlinks as text files | Use `git config core.symlinks true`; add to setup script |

## Estimated Scope

- **50 content-block `.lean` files** to create
- **6 monolithic files** to split (QuantumObservableUniverse, Torsion, HadronicMass, PathIntegrals, Elaboration, + potentially others)
- **50 symlinks** to create
- **50 `.ts` manifests** to update
- **~7,000 lines** of Lean code to reorganize
