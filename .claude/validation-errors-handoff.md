# Content Validation Errors — Handoff Summary

Branch: `claude/analyze-critical-path-GEao2`
Date: 2026-03-22
Previous work: Lean stubs, categorical proof rewrites, critical-path skill

## Validation Results (150 errors, 39 warnings)

### Error Categories

#### 1. Chapter manifest schema (9 errors — all chapters)

Every chapter manifest (`ch*-*.ts`) fails with:
```
Schema: kind: Invalid discriminator value.
Expected 'definition' | 'theorem' | ... | 'diagram'
```

**Root cause**: `chapter` is not in the Zod discriminated union in
`folio-assistant/cat-harness/schemas/types.ts`. The `chapter()` builder exists but the
schema's block-level discriminator doesn't include it.

**Fix**: Either add `'chapter'` to the block kind discriminator, or
restructure chapter manifests to use a separate schema (they're not
really "blocks" — they're containers).

**Files**: `folio-assistant/cat-harness/schemas/types.ts` (discriminator union),
`folio-assistant/cat-harness/schemas/constraints.ts` (Zod schemas)

#### 2. Unresolved cross-chapter references (~80 errors)

Blocks in ch3–ch11 reference definitions/remarks from other chapters
that the per-chapter validator can't resolve. Most common:

| Referenced label | Defined in | Referenced from |
|-----------------|-----------|----------------|
| `def:quantum-observable-universe` | ch1 | ch3 (15×), ch4, ch5, ch6 |
| `def:substrate-parameter` | ch1 | ch3 (4×), ch5, ch6, ch11 |
| `def:projective-line-object` | ch1 | ch3 (5×), ch4 |
| `def:c-quantum-observable-universe` | ch1 | ch3 (3×), ch5, ch6 |
| `def:quantum-planck-constant` | ch1 | ch4, ch5, ch11 |
| `def:q-reeb-vector-field` | ch1 | ch3 (2×), ch5 |
| `def:q-reeb-flow` | ch1 | ch3, ch5, ch11 |
| `def:categorical-point` | ch1 | ch3 (2×) |
| `def:categorical-q-reeb-flow` | ch1 | ch3 |
| `def:quantum-universe` | ch1 | ch3, ch5, ch6 |
| `def:fermion` / `def:boson` | ch2? | ch3, ch6 |
| `def:instanton` | ch1 | ch1 (2×) |
| `def:briggs-klein-chart` | ch5 | ch3 |
| `thm:qu-to-qou` | ch3 | ch5, ch6 |

**Root cause**: `content_validate` checks within a single chapter.
Cross-chapter `uses[]` references only resolve at build time.

**Fix options**:
1. Make validator resolve across chapters (preferred)
2. Add a `--cross-chapter` flag to `content_validate`
3. Accept these as expected warnings (they resolve at build time)

#### 3. Missing Lean files for definitions (14 errors)

Definitions that require `.lean` files but don't have them:

| Block | Chapter |
|-------|---------|
| `def:descent-involution` | ch3 |
| `def:mass-identity` | ch3 |
| `def:bundle-isotopy-equivalence` | ch3 |
| `def:brane-boundary` | ch3 |
| `def:descent` | ch3 |
| `def:recursive-brane-tower` | ch3 |
| `def:localized-hadron` | ch3 |
| `def:hadron-fibre-embedding` | ch3 |
| `def:quantum-characteristic-classes` | ch3 |
| `def:yekutieli-lifting-condition` | ch3 |
| `def:direct-limit-algebra` | ch3 |
| `def:yekutieli-triple` | ch3 |
| `def:exceptional-divisor` | ch6 |
| `def:categorical-q-torsion-leaf` | ch1 |

**Fix**: Create `.lean` stub files for each. Some already have
partial formalizations in `content/quantum-observable-universe/lean/QOU/Torsion.lean` that
could be copied/adapted.

#### 4. Missing Lean declarations (39 warnings)

Propositions/theorems/corollaries without Lean formalizations.
These are warnings, not errors. Lower priority.

### Priority Order

1. **Schema fix** (9 errors) — single change to `types.ts`
2. **Cross-chapter resolution** (80 errors) — validator enhancement
3. **Lean definition stubs** (14 errors) — create `.lean` files
4. **Lean theorem stubs** (39 warnings) — nice to have

### Files to Read First

- `folio-assistant/cat-harness/schemas/types.ts` — block kind discriminator
- `folio-assistant/cat-harness/schemas/constraints.ts` — Zod validation schemas
- `content/pipeline/validate.ts` — validation pipeline
- `content/quantum-observable-universe/lean/QOU/Torsion.lean` — existing torsion formalizations
