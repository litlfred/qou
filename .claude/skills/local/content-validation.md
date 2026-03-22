---
name: content-validation
roles: [reader, collaborator, owner]
---

# Content Validation Skill

## Role

Validate content objects (`.ts` manifests + `.md` content + `.lean` files)
for structural integrity, constraint compliance, and LaTeX AST correctness.

## Content-object infrastructure

| Path | Purpose |
|------|---------|
| `content/schema/types.ts` | TypeScript types for all block kinds |
| `content/schema/constraints.ts` | Zod schemas + constraint rules |
| `content/schema/builders.ts` | Builder functions (`definition()`, `theorem()`, etc.) |
| `content/pipeline/validate.ts` | Validation pipeline (schema + constraints + AST) |
| `content/pipeline/render-latex.ts` | Block → LaTeX rendering + AST validation |
| `content/pipeline/build.ts` | Full document build (all chapters) |

## Directory convention

```
content/
  <paper-name>/
    <paper-name>.ts                    — Paper manifest (ChapterRef[])
    <chapter-dir>/
      <chapter-dir>.ts                 — Chapter manifest (sections, block refs)
      <block-name>.ts                  — Block manifest (kind, label, lean, constraints)
      <block-name>.md                  — Narrative content (markdown + TeX snippets)
      <block-name>.lean                — Lean formalization (when required by kind)
```

## Validation levels

### Level 1: Zod schema validation
- Block kind matches discriminated union
- Label prefix matches kind (def: for definitions, thm: for theorems, etc.)
- Required fields present (e.g. definitions MUST have `lean`)
- Status enum values are valid

### Level 2: Constraint rules
- **md-exists**: Every block has a sibling `.md` file
- **lean-file-exists**: Definitions have a sibling `.lean` or `lean.file` reference
- **uses-resolve**: All labels in `uses[]` exist in the document
- **provable-lean-warning**: Theorems/lemmas without Lean get warnings

### Level 3: AST validation
- Rendered LaTeX parses through unified-latex without errors
- Environment balance (\begin matches \end)
- No malformed macro syntax
- No unbalanced braces

## Running validation

```bash
# Validate all objects in a paper
cd content && bun run pipeline/validate.ts quantum-observable-universe/ch1-quantum-observable-universe

# Full build with validation
cd content && bun run pipeline/build.ts quantum-observable-universe/quantum-observable-universe.ts
```

## When to validate

1. **Before commit**: Run validation on changed content objects
2. **After editing .md files**: Ensure LaTeX rendering still valid
3. **After adding new blocks**: Check constraints (lean file exists, labels resolve)
4. **After modifying schema**: Run validation across all content

## Adding custom constraints

Add rules to `CONSTRAINT_RULES` array in `content/schema/constraints.ts`:

```typescript
CONSTRAINT_RULES.push({
  id: "my-rule",
  description: "Custom constraint",
  appliesTo: ["definition", "theorem"],
  check: (block, ctx) => {
    // Return error message string or null
    return null;
  },
});
```

## Mandatory fallback participation

This skill is invoked automatically by the editor's **content-change fallback**
(see `editor.md § Content-change fallback`). Whenever any content is modified
during a session, the editor runs `content_validate` on affected chapters
before the task is considered complete.

## Integration with test-engineer

The content-validation skill produces `ValidationResult` objects that the
test-engineer skill can consume in unit tests:

```typescript
import { validateObjects } from "../../content/pipeline/validate";

test("all content objects valid", async () => {
  const result = await validateObjects("content/quantum-observable-universe/ch1-...");
  expect(result.valid).toBe(true);
});
```
