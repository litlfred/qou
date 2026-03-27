---
name: remark-audit
roles: [reader, collaborator, owner]
description: >
  Audit remarks for provable backing. Every remark must interpret a
  proposition, lemma, theorem, or definition — no "dangling" remarks
  that make mathematical claims without formal support.
allowed-tools: Read Grep Glob Bash Agent
---

# Remark Audit Skill

## Principle: No Dangling Remarks

Every remark block (`rem:*`) in the paper must satisfy one of two roles:

1. **Interpretive remark** — interprets a provable block (definition,
   proposition, lemma, theorem, corollary, conjecture). The `interprets`
   field in the `.ts` manifest names the label of the block being
   interpreted. The `.md` content provides physical interpretation,
   examples, motivation, or simulation context for the formal result.

2. **Glossary remark** — a terminological wrapper around a Mathlib type
   (Ch 8 only). Tagged `"glossary"`, label pattern `rem:glossary-*`.
   No `interprets` field needed.

A remark that is **neither interpretive nor glossary** is a **dangling
remark** — it makes mathematical or physical claims without formal
backing. Dangling remarks must be resolved by one of:

- **Promoting** the remark's core claim to a proposition/lemma and
  linking the remark via `interprets`
- **Demoting** the remark to `prose` (if it has no logical content)
- **Merging** the remark into an existing provable block's
  interpretation chain

## Block Lifecycle

The correct authoring flow is:

```
definition / proposition / lemma / theorem  (Lean: formal statement)
  └→ proof block                            (Lean: formal proof)
       └→ remark block                      (Markdown: interpretation)
            └→ example / simulator          (concrete instances)
```

Each layer depends on the one above:
- The **provable block** has a `.lean` file with the formal statement
- The **proof block** has a `.lean` file with the formal proof
- The **remark** has `interprets: "prop:foo"` linking to the provable
  block, and a `.md` file with physical interpretation
- **Examples** and **simulators** illustrate the remark's interpretation

## The `interprets` Field

Added to `RemarkBlock` in the schema:

```typescript
export interface RemarkBlock extends BlockBase {
  kind: "remark";
  lean?: LeanRef;
  /** Label of the provable block this remark interprets. */
  interprets?: string;
}
```

### Rules

| Situation | `interprets` | Tags | Action |
|-----------|-------------|------|--------|
| Remark interprets a theorem | Required | — | Set `interprets: "thm:foo"` |
| Glossary remark (Ch 8) | Not needed | `["glossary"]` | Tag suffices |
| Remark makes a mathematical claim | **Missing** | — | **Dangling** — promote claim to prop/lem |
| Pure prose (no logical content) | Not needed | — | Demote to `prose` block |

### Constraint rule

The `remark-interprets` constraint warns when a remark has neither
`interprets` nor a `"glossary"` tag. The `interprets-resolve` constraint
errors when `interprets` names a label that doesn't exist.

## Audit Procedure

### 1. Inventory all remarks

```bash
cd content && bun run pipeline/find-dangling-remarks.ts
```

Or manually:

```bash
grep -r '"kind": "remark"' content/ --include='*.ts' -l
```

### 2. Classify each remark

For each `rem:*` block, determine:

| Question | If yes | If no |
|----------|--------|-------|
| Does the `.md` contain a provable mathematical statement? | Promote to prop/lem | Continue |
| Does it interpret an existing prop/lem/thm/def? | Add `interprets` | Continue |
| Is it a glossary entry (Mathlib synonym)? | Add `"glossary"` tag | Continue |
| Is it pure exposition (no logical claim)? | Demote to `prose` | **Dangling** |

### 3. Resolution patterns

**Pattern A: Promote + Interpret**

Before (dangling):
```typescript
// crossing-energy-decomposition.ts
export default remark({
  label: "rem:crossing-energy-decomposition",
  title: "Crossing energy decomposes into strong and Coulomb channels",
  ...
});
```

After (backed):
```typescript
// crossing-energy-decomposition.ts  → proposition
export default proposition({
  label: "prop:crossing-energy-decomposition",
  title: "Crossing energy decomposes into strong and Coulomb channels",
  lean: { decl: "QOU.CrossingEnergy.strong_coulomb_decomposition" },
  ...
});

// crossing-energy-decomposition-interpretation.ts  → remark
export default remark({
  label: "rem:crossing-energy-decomposition-interpretation",
  title: "Physical interpretation of the strong/Coulomb decomposition",
  interprets: "prop:crossing-energy-decomposition",
  ...
});
```

**Pattern B: Link existing**

When the claim is already proved elsewhere:
```typescript
export default remark({
  label: "rem:q-laplacian-interpretation",
  title: "The q-Laplacian as quantum averaging",
  interprets: "def:q-harmonic-form",  // ← add this
  ...
});
```

**Pattern C: Demote to prose**

When there's no logical content:
```typescript
// Before
export default remark({ label: "rem:cp-violation-evidence", ... });
// After
export default prose({ label: "sec:cp-violation-evidence", ... });
```

### 4. Ambiguous terms audit

Watch for physics terms used as if they were categorical:

| Physics term | Categorical equivalent | Check |
|-------------|----------------------|-------|
| "force" | Morphism in force category? | Is there a def? |
| "energy" | Crossing energy (def:crossing-energy) | Ensure `uses` |
| "particle" | q-harmonic form (def:q-harmonic-form) | Ensure `uses` |
| "observable" | Fibre functor (def:quantum-observable-universe) | Ensure `uses` |
| "measurement" | Observation morphism (def:observation) | Ensure `uses` |
| "degeneration" | Frobenius form non-degeneracy failure | Is there a def? |
| "time reversal" | Fiber adjoint involution (prop:fiber-adjoint-involution) | Ensure `uses` |
| "virtual particle" | Tower excitation at level A_n (n≥1) | Is there a def? |

If a physics term appears in a remark without a corresponding categorical
definition, either:
- Define the categorical concept (new `definition` block)
- Link to an existing definition via `uses[]`
- Flag as **ambiguous** and defer to the author

## Integration

- **Runs after** `content-block-review` (which checks structural integrity)
- **Feeds into** `proof-triage` (promoted propositions need Lean)
- **Feeds into** `formalizer` (new Lean declarations needed)
- Complements `content-validation` (which checks schema + AST)

## Output Format

```
## Remark Audit: <paper-name>

### Dangling Remarks (no `interprets`, not glossary)
- **rem:foo** (<file>): Claims X without formal backing
  - Suggested resolution: Promote core claim to prop:foo
  - Ambiguous terms: "energy", "degeneration"

### Backed Remarks (have `interprets`)
- **rem:bar** → interprets **prop:baz** ✓

### Glossary Remarks
- **rem:glossary-qux** (Ch 8) ✓

### Summary
- Total remarks: N
- Backed: N | Glossary: N | Dangling: N
- Ambiguous physics terms found: N
```
