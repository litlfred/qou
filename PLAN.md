# Plan: Per-block Lean files in content directory

## Goal
Move Lean formalization from monolithic `lean/QOU/*.lean` files into per-block
`.lean` files alongside their `.ts` + `.md` siblings in `content/`.

### Before
```
lean/QOU/QuantumObservableUniverse.lean   ← 74 declarations, 1 file
content/.../rigid-monoidal-category.ts
content/.../rigid-monoidal-category.md
```

### After
```
content/.../rigid-monoidal-category.ts    ← lean.file: "rigid-monoidal-category.lean"
content/.../rigid-monoidal-category.md
content/.../rigid-monoidal-category.lean  ← extracted declaration(s)
```

## Architecture

### Lean build integration
Lake expects `.lean` files under its `srcDir`. We add a **symlink forest** step:
- `lean/QOU/Content/` directory with symlinks → `content/**/*.lean`
- Pre-build script generates symlinks from content manifests
- Each content `.lean` file has `namespace QOU` and proper imports
- `lean/QOU/Content.lean` auto-generated to import all content lean files

### Block `.lean` file convention
```lean
-- Auto-generated header (do not edit above this line)
import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Basic

namespace QOU

/-- Rigid monoidal category... -/
structure RigidMonoidalCategory where
  ...

end QOU
```

### Content `.ts` manifest
```typescript
export default definition({
  label: "def:rigid-monoidal-category",
  lean: {
    decl: "QOU.RigidMonoidalCategory",
    file: "rigid-monoidal-category.lean",  // relative to block dir
  },
});
```

### Source resolution
- Viewer/export: `lean.file` resolved relative to the block's directory
- Lean build: symlinked into `lean/QOU/Content/` namespace

## Migration priority

### Phase 1: Infrastructure (do first)
1. Update source resolvers (MCP server, export-json) to find `.lean` in content dir
2. Create `scripts/sync-lean.sh` to generate symlink forest
3. Update `lakefile.toml` if needed
4. Update `.gitignore` for symlinks

### Phase 2: High-value blocks (definitions with lean)
Extract from monolithic files, highest dependency count first:
- `QuantumObservableUniverse.lean` → 74 decls across ch1 blocks
- `HadronicMass.lean` → 48 decls across ch11 blocks
- `Torsion.lean` → 45 decls across ch3 blocks

### Phase 3: Proof blocks
- Move lean from proof blocks that already have `lean.decl`
- 7 proof blocks currently have lean refs

### Phase 4: Remaining files
- `PathIntegrals.lean` → ch4 blocks
- `BringsSurface.lean` → ch5 blocks
- `Elaboration.lean` → ch2 blocks
- `DescartesUniverse.lean` → ch6 blocks
- Smaller files (< 10 decls each)

## Risks
- **Import graph**: declarations may depend on each other within a file.
  Need to track and replicate imports in per-block files.
- **Shared infrastructure**: `Basic.lean`, `Glossary.lean` contain shared
  types/notation used across many blocks — these stay in `lean/QOU/`.
- **Build time**: many small files may be faster (parallel) or slower (import overhead).
  Test with a few blocks first.
