---
name: remark-audit
roles: [reader, collaborator, owner]
description: >
  Audit remarks for provable content. Every remark must interpret a
  categorical/mathematical statement that can be formalized in Lean.
  Detects dangling remarks (no `interprets` link), ambiguous physics
  terms, and missing formalization.
allowed-tools: Read Grep Glob Bash Agent
---

# Remark Audit Skill

## Principle

**No dangling remarks.** Every `remark` block must be the interpretive
layer of a provable mathematical statement. The provable statement lives
in a `proposition`, `lemma`, `theorem`, or `corollary` block with Lean
formalization. The remark provides physical interpretation, examples,
simulations, and narrative — but cannot exist without the formal backbone.

### Block structure hierarchy

```
proposition/lemma/theorem/corollary  ← Lean formalization (provable)
  └── proof                          ← Lean proof
  └── remark (interprets: label)     ← Physical interpretation, examples
        └── simulator (optional)     ← Interactive visualization
        └── prose (optional)         ← Reader-facing narrative

prose                                ← No logical content (intros, abstracts)
```

### The two kinds of narrative

| Block kind | Has provable content? | Example |
|------------|----------------------|---------|
| `remark`   | **Yes** — interprets a prop/lem/thm | "The q-Laplacian as quantum averaging" |
| `prose`    | **No** — reader-facing only | Chapter introduction, abstract, notation conventions |

**Decision rule**: If the text makes a claim that could in principle be
stated as a Lean `theorem` or `proposition`, it belongs in a `remark`
with an `interprets` link to the formal statement. If it is purely
expository (no falsifiable claim), it is `prose`.

## What `interprets` means

The `interprets` field on a `RemarkBlock` is the label of the
provable block that this remark interprets. It establishes a formal
dependency:

```typescript
remark({
  label: "rem:crossing-energy-decomposition",
  interprets: "prop:crossing-energy-cosh-sinh",  // ← the formal statement
  title: "Crossing energy decomposes into strong and Coulomb channels",
  uses: ["def:crossing-energy", "def:substrate-parameter"],
});
```

The remark's `.md` file contains the physical interpretation, examples,
tables, and narrative. The proposition's `.lean` file contains the
Lean proof. They are complementary views of the same mathematical fact.

## Audit procedure

### Phase 1: Find dangling remarks

```bash
# List all remark blocks
cd content && grep -rl '"remark"' --include='*.ts' | sort

# For each remark, check if it has `interprets` field
# If not → DANGLING (needs formalization or reclassification)
```

A dangling remark is one that:
1. Has no `interprets` field, AND
2. Makes claims that could be formalized (not pure glossary or notation)

### Phase 2: Classify each dangling remark

For each dangling remark, determine:

| Classification | Action |
|---------------|--------|
| **Has provable content** | Extract the formal statement → create prop/lem/thm + Lean stub → add `interprets` link |
| **Pure glossary** (Ch 8 terminology wrapper) | Keep as remark with tag `"glossary"` — no `interprets` needed |
| **Pure exposition** (no falsifiable claim) | Reclassify as `prose` |
| **Speculative** (interesting but unproved) | Reclassify as `conjecture` |

### Phase 3: Formalize the provable content

For each remark upgraded to have an `interprets` target:

1. **State the proposition** in categorical terms (no physics jargon).
   Identify exactly which objects, morphisms, and properties are involved.

2. **Create the Lean stub** with `sorry` and `-- Ref:` citation.

3. **Write the `.md` for the proposition** — pure math, no interpretation.

4. **Keep the remark `.md`** — physical interpretation, examples, simulations.

### Phase 4: Physics ↔ Category audit

For each remark, check for **ambiguous terms** that conflate physics
and category theory:

| Physics term | Categorical term | Check |
|-------------|-----------------|-------|
| "energy" | Frobenius form value, crossing weight | Is it defined categorically? |
| "particle" | q-harmonic form, knot type | Which definition is referenced? |
| "force" | Skein channel (sym/antisym) | Is the decomposition proved? |
| "time reversal" | Fiber adjoint involution | Is σ² = id proved in Lean? |
| "chirality" | Knot mirror operation σ | Is it Jones polynomial or categorical? |
| "observation" | Morphism O_p on germs | Is the morphism defined? |
| "degeneration" | Frobenius non-degeneracy failure | Is there a formal definition? |
| "classical limit" | q → 1 specialization | Is the limit formalized? |
| "Big Bang" | Initial object? Bundle initial condition? | Is this defined categorically? |
| "heat death" | Terminal object? Cocommutativity? | Is this defined categorically? |
| "virtual particle" | Tower excitation at level A_n | Is the projection formalized? |
| "pair creation" | Exceptional divisor morphism | Is this a defined operation? |

Flag any physics term used without a cross-reference to its categorical
definition.

## Constraint rule

The following constraint is added to `constraints.ts`:

```typescript
{
  id: "remark-interprets",
  description: "Remark should have `interprets` linking to a provable block",
  appliesTo: ["remark"],
  severity: "warning",
  check: (block, ctx) => {
    // Skip glossary remarks (Ch 8 terminology wrappers)
    if (block.tags?.includes("glossary")) return null;
    // Skip if interprets is set
    if (block.interprets) return null;
    return `Remark "${block.label}" has no \`interprets\` field. ` +
      `Either add a provable block it interprets, reclassify as prose, ` +
      `or add tag "glossary" if it's a terminology wrapper.`;
  },
}
```

## Output format

```
## Remark Audit: <paper-name>

### Dangling Remarks (no `interprets`)
- **rem:foo** — <classification>: <action needed>

### Ambiguous Terms
- **rem:bar** uses "energy" without categorical definition → needs ref to def:crossing-energy

### Reclassifications
- **rem:baz** → prose (no provable content)
- **rem:qux** → conjecture (speculative, not proved)

### Summary
- Remarks audited: N
- Dangling: N | Glossary: N | Prose candidates: N | Conjecture candidates: N
- Fully linked: N / N
```

## Integration

- Runs **after** `content-block-review` (which checks structural integrity)
- Feeds into `formalizer` (dangling remarks become formalization targets)
- Feeds into `proof-triage` (prioritize provable content extraction)
- Complements `content-validation` (which checks schema + AST)
