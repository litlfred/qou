---
name: formalizer
roles: [collaborator, owner]
description: >
  Lean 4 Formalizer — translates the logical skeleton of narrative mathematical
  proofs into Lean 4 tactic blocks.  Uses the Ontologist's glossary to resolve
  types, maps narrative proof phrases to Lean tactics, and generates sorry-bridged
  partial proofs that compile.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Lean 4 Formalizer (Narrative to Proof)

## Overview

This skill translates the **logical skeleton** of the paper into Lean 4
tactic blocks.  It depends on the Ontologist skill having already produced
a resolved glossary — every term used in theorems must have a unique type
assignment before formalization can proceed.

### Pre-flight: rebase + lean-ref migration

Before authoring or editing `.lean` siblings, the working branch must
be on the current `lean.ref` URI shape.  If the branch was rebased
or merged from upstream, run the idempotent migration **first**:

```bash
cd content && bun run migrate-lean-refs
```

When authoring the `.ts` manifest for a new block, set
`lean: { ref: "<pkg>:<Decl>" }` (never the legacy `decl:` / `file:`
shape).  Use `<pkg>` from `LEAN_PACKAGES` in
`folio-assistant/schemas/lean-packages.ts` (`qou`, `ugb`, `fred2005`,
…).  See CLAUDE.md §0a for the URI grammar and §0b for the rebase
workflow.

## When to Use This Skill

- After the Ontologist has produced `glossary.json` and `Glossary.lean`
- When translating theorem statements from LaTeX to Lean
- When filling `sorry` placeholders with actual proofs
- When `lake build` succeeds but there are remaining `sorry` warnings

## Lean MCP Tools (paper-assistant)

When the MCP server is available, **prefer MCP tools over shell commands**:

| Old workflow | MCP tool | Why better |
|-------------|----------|-----------|
| `lake build` + parse output | `lean_diagnostic_messages` | Structured errors per file, no parsing |
| `formalizer.py export-proof-state` | `lean_goal` | Live goal state at any line/column, no Python |
| Grepping Mathlib for lemmas | `lean_leansearch` / `lean_loogle` | Natural language + type-signature search across all of Mathlib |
| Guessing tactics one at a time | `lean_multi_attempt` | Try multiple tactics at a sorry position in one call |
| Manual `exact?` / `apply?` | `lean_completions` | Auto-complete with context-aware suggestions |
| Reading Mathlib source for docs | `lean_hover_info` | Hover docs for any symbol inline |
| Manual `Try this` checking | `lean_code_actions` | Get resolved edits from "Try This" suggestions |

### MCP-first tactic workflow

When filling a `sorry`:

1. **`lean_goal`** at the sorry position → read the goal state
2. **`lean_multi_attempt`** with candidate tactics from the tactic table → try all at once
3. If no tactic works, **`lean_leansearch`** with the goal in natural language
4. If leansearch finds a close match, **`lean_loogle`** with the type signature
5. **`lean_code_actions`** on the line → check for "Try This" suggestions
6. After editing, **`lean_diagnostic_messages`** → verify no new errors

### MCP-enhanced library synthesis

Instead of the Python script for import synthesis:
1. Write the theorem stub with a `sorry` body
2. **`lean_diagnostic_messages`** → see "unknown identifier" errors
3. **`lean_leansearch`** for each unknown identifier → find the right import
4. **`lean_completions`** at the import line → auto-complete module paths

## Important: Generation is agent-only

The scripts below are **proof-writing tools**. They create or modify Lean
files. They must only be run when the author has requested formalization.

- **Do not** run them during setup, session start, or routine builds.
- **`lake build`** = compile-only. Never precede it with generation scripts.
- CI workflows run them automatically — that is CI-only behavior.

## Workflow (invoke only on author request)

### 1. Library synthesis

The Formalizer identifies required Mathlib imports from the glossary:

```bash
PYTHONPATH=.github/scripts python .github/scripts/formalizer.py synthesize-imports
```

Reads `glossary.json` and outputs the import block for each chapter file.

### 2. Generate theorem stubs

```bash
PYTHONPATH=.github/scripts python .github/scripts/formalizer.py generate-theorems
```

Creates Lean theorem declarations with `sorry` bodies, using the glossary
types for the statement signatures.

### 3. Tactic translation

The Formalizer maps narrative proof phrases to Lean tactics:

| Narrative Phrase                    | Primary Tactic          | Fallbacks                       |
|-------------------------------------|-------------------------|---------------------------------|
| "By calculation"                    | `ring`                  | `field_simp`, `polyrith`        |
| "Clearly follows from..."          | `aesop`                 | `linarith`, `omega`             |
| "By induction on n..."             | `induction n with`      | `cases n`                       |
| "By the universal property of..."  | `Limits.IsLimit.lift`   | `Limits.IsLimit.hom_ext`        |
| "Diagram commutes" / "naturality"  | `aesop_cat`             | `slice_lhs`, `slice_rhs`        |
| "By contradiction"                 | `by_contra`             | `exfalso`                       |
| "By definition"                    | `rfl`                   | `unfold`, `simp only`           |

### 4. The "Sorry" Bridge

When a narrative step is too complex for immediate formalization:

1. Extract the logical structure of the proof
2. Create a `lemma` for each non-trivial step
3. Fill each lemma body with `sorry`
4. **Add a `-- Ref: [key] url` comment** before each `sorry` linking
   to the foundational reference that would resolve the gap
5. Ensure the file remains syntactically correct
6. Track the sorry count in `proof-objects.json`

```lean
/-- Intermediate step: torsion lifts through jet prolongation.
    TODO: formalize using the Frobenius-Hopf structure. -/
lemma torsion_lifts_jet (A : FrobeniusHopfAlgebra) :
    JetProlongation A → TorsionLifting A := by
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  sorry
```

**Rule**: Every `sorry` must have a `-- Ref:` annotation.  The `key`
must match a citation key in `content/schema/references.ts` exactly (case-sensitive).
(`references.bib` is auto-generated from this file — never edit `.bib` directly.)  If no
published reference exists, use `[manuscript]` and cite the chapter/section.
This is enforced by the axiom report's Theoretical Gap Report (§8).

## Library Synthesis Rules

Based on the glossary types, import the correct Mathlib modules:

| Glossary Type             | Required Mathlib Import                              |
|---------------------------|------------------------------------------------------|
| `TopologicalSpace`        | `Mathlib.Topology.Basic`                             |
| `SmoothManifold`          | `Mathlib.Geometry.Manifold.SmoothManifoldWithCorners`|
| `Category`                | `Mathlib.CategoryTheory.Category.Basic`              |
| `MonoidalCategory`        | `Mathlib.CategoryTheory.Monoidal.Basic`              |
| `Functor`                 | `Mathlib.CategoryTheory.Functor.Basic`               |
| `NatTrans`                | `Mathlib.CategoryTheory.NatTrans`                    |
| `Limits.IsLimit`          | `Mathlib.CategoryTheory.Limits.IsLimit`              |
| `Group`                   | `Mathlib.Algebra.Group.Basic`                        |
| `Ring`                    | `Mathlib.Algebra.Ring.Basic`                         |
| `Module`                  | `Mathlib.Algebra.Module.Basic`                       |
| `FundamentalGroupoid`     | `Mathlib.Topology.AlgebraicTopology.FundamentalGroupoid` |
| `ModuleCat`               | `Mathlib.Algebra.Category.ModuleCat`                 |

## Proof State Export

**Preferred (MCP):** Use `lean_goal` with the file path and line/column of the
sorry position. Returns structured goal state directly — no Python needed.

**Fallback (no MCP):** The Formalizer can export the current goal state via:

```bash
PYTHONPATH=.github/scripts python .github/scripts/formalizer.py export-proof-state \
  --file lean/QOU/Torsion.lean --line 42
```

Output follows the `ProofStateExport` schema in `folio-assistant/schemas/qou-types.ts`.

## Integration with Ontologist

1. **Before formalization**: Ontologist runs, produces resolved `glossary.json`
2. **During formalization**: Formalizer checks every term against the glossary
3. **On type mismatch**: Formalizer reports back to Ontologist for re-evaluation
4. **After `lake build`**: If build fails, Ontologist re-scans for type conflicts

## Lean Output Structure

The Lean source tree lives **per paper** under `content/<paper>/lean/`,
with the repo's root `/lakefile.toml` aggregating every package into a
single Lake workspace. See [Root Lake workspace
(standardized)](#root-lake-workspace-standardized) below for the
canonical layout, package registry, and build commands. Do **not**
create a top-level `lean/` directory — that layout is deprecated.

## Proven Patterns

### Existence Constructors for Structure Definitions

Every `structure` definition must have at least one **existence constructor**
— a `def` or `noncomputable def` that builds an instance of the structure
from its prerequisites. Without this, downstream theorems depend on
structures that may be vacuously satisfiable.

**Pattern**: The constructor takes upstream structures as parameters and
returns the target structure. The type signature makes the dependency
chain explicit — the type checker enforces it.

```lean
-- Definition: declares WHAT the structure looks like
structure WeightDecomposition (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] where
  forms : C
  proj_H : forms ⟶ forms
  proj_V : forms ⟶ forms
  complementary : proj_H + proj_V = 𝟙 forms
  ...

-- Existence constructor: proves THAT it can be built
noncomputable def WeightDecomposition.ofMaximalTorus
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
    (mt : MaximalTorus C) (forms : C) : WeightDecomposition C :=
  { forms := forms
    proj_H := sorry  -- Ref: [lusztig1993] ...
    proj_V := sorry  -- Ref: [lusztig1993] ...
    complementary := sorry  -- Ref: [lusztig1993] ...
    ... }
```

**Naming convention**: `StructureName.ofPrerequisite` (e.g.,
`CategoricalReeb.ofWeightDecomposition`,
`SubstrateParameter.ofReebDecomposition`).

**When to use each variant**:

| Situation | Pattern | Example |
|-----------|---------|---------|
| Concrete construction (no sorry) | Direct `def` | `SubstrateParameter.ofConstant q₀ hq_pos hq_ge hq_root` |
| Construction from upstream structures | `noncomputable def` with sorry | `CategoricalReeb.ofWeightDecomposition mt wd` |
| Canonical/unique choice | `instance : Inhabited T` | `instance : Inhabited (SubstrateParameter ℝ)` |
| Auto-resolved by typeclass | `class` + `instance` | `class HasSubstrateParameter M` |

**Content object requirements**: Each existence constructor gets its own
content block triple (`.ts` + `.md` + `.lean`):
- Block kind: `theorem` (label: `thm:<name>-exists`)
- `uses[]`: must list the definition it constructs AND its immediate prerequisite (the structure it's built from) — not the full transitive chain
- `.lean`: the constructor function, with sorry-annotated fields citing references

**Dependency graph rule**: If definition B's `.lean` `structure` takes a
parameter of type A (another project structure), there MUST exist a
`thm:<b>-exists` block whose `uses[]` includes `def:b` (and `def:a`
only if A is an **immediate** prerequisite of the existence theorem,
not already reachable via `def:b`'s own `uses[]`). The `uses[]` field
lists only direct neighbors — transitive deps are walked by the graph.

**Checklist for every `structure` definition**:
- [ ] At least one `.ofFoo` constructor exists in a sibling `.lean` file
- [ ] A `thm:*-exists` content block triple references it
- [ ] The constructor's parameters include all upstream structures
- [ ] Each `sorry` in the constructor has a `-- Ref:` annotation
- [ ] The chapter manifest places the existence theorem after the definition

### Subsingleton as Categorical Vanishing

Use `Subsingleton` to model vanishing conditions (e.g., `H⁰(M, Ad(P)) = 0`)
without requiring `Preadditive` or `AddCommGroup` structure:

```lean
/-- All morphisms 𝟙 → Ad(A) are equal ⟺ Hom(𝟙, Ad(A)) = 0. -/
adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)

/-- All global adjoint sections are equal ⟺ H⁰(M, Ad(P)) = 0. -/
adjoint_cohomology_vanishes : Subsingleton adjointSections
```

**Why**: In a `k`-linear category, the zero morphism always exists, so
`Subsingleton` implies the only morphism is zero — equivalent to the hom-space
vanishing.  This avoids importing `Preadditive` just for a vanishing axiom.

### Irreducibility via Subsingleton Propagation

Prove irreducibility by propagating `Subsingleton` through an injective map:

```lean
theorem irreducible_connection (cqou : CQuantumObservableUniverse)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (embed : inst.parallelAdjointSections → cqou.adjointSections)
    (h_inj : Function.Injective embed) :
    inst.IsIrreducible :=
  ⟨fun a b => h_inj (cqou.adjoint_cohomology_vanishes.allEq _ _)⟩
```

**Pattern**: Given `Subsingleton Y` and `f : X → Y` injective, conclude
`Subsingleton X` by `⟨fun a b => h_inj (inst.allEq _ _)⟩`.

### Coevaluation + Snake Identities for Exact Self-Pairing

Model non-degeneracy of a Frobenius form as a categorical self-duality
(exact pairing) using coevaluation and snake identities:

```lean
coevaluation : (𝟙_ C) ⟶ (obj ⊗ obj)
pairing_snake_left :
  (ρ_ obj).inv ≫ (obj ◁ coevaluation) ≫ (α_ obj obj obj).inv ≫
    ((mul ≫ frobeniusForm) ▷ obj) ≫ (λ_ obj).hom = 𝟙 obj
pairing_snake_right :
  (λ_ obj).inv ≫ (coevaluation ▷ obj) ≫ (α_ obj obj obj).hom ≫
    (obj ◁ (mul ≫ frobeniusForm)) ≫ (ρ_ obj).hom = 𝟙 obj
```

**Why**: Non-degeneracy of a bilinear form is hard to state categorically
without linear algebra.  The snake identities (`zig-zag`) are equivalent and
work in any monoidal category.

### Abstract Hodge Involution

Model the Hodge star as an involutive endomorphism — works at both the
categorical level and the concrete level:

```lean
-- Categorical level (any category with identity):
structure CatHodgeInvolution {C : Type u} [Category.{v} C] (X : C) where
  star : X ⟶ X
  star_sq : star ≫ star = 𝟙 X

-- Concrete level (Type):
structure HodgeInvolution (V : Type*) where
  star : V → V
  star_sq : ∀ v, star (star v) = v
```

Self-duality predicates follow as `f ≫ star = f` (categorical) or
`star v = v` (concrete).

## Adding New Dependencies

When a proof requires a library not in `lakefile.toml`:

1. Add the `[[require]]` entry to the relevant `lakefile.toml`
2. Run `lake update` — this fetches the dep into `.lake/packages/`
3. Run `lake exe cache get` if the dep has prebuilt oleans
4. Run `lake build` to verify everything compiles
5. **Only commit**: `lakefile.toml` and `lake-manifest.json`
6. **Never commit**: `.lake/`, `lake-packages/`, `build/` (all gitignored)

The MCP server will pick up new dependencies automatically after `lake build`.

### Toolchain compatibility (critical)

All `[[require]]` deps in a Lean project **must agree on the same
`lean-toolchain` version**. A mismatch causes build failures — often
cryptic Lake API errors in transitive deps like proofwidgets.

**Before adding or changing a dependency:**

1. Check the new dep's `lean-toolchain`:
   ```bash
   git ls-remote --refs <repo-url> HEAD
   # then check lean-toolchain at that commit, or:
   cat .lake/packages/<dep>/lean-toolchain
   ```
2. Compare against every other dep's toolchain:
   ```bash
   for pkg in .lake/packages/*/; do
     echo "$(basename $pkg): $(cat $pkg/lean-toolchain 2>/dev/null)"
   done
   ```
3. If they disagree, **do not proceed**. Find a compatible version.

**How to find a compatible version:**

- Check the new dep's `lake-manifest.json` for the Mathlib commit it
  was tested against:
  ```bash
  cat .lake/packages/<dep>/lake-manifest.json | grep -A3 mathlib
  ```
- Use **that same Mathlib commit hash** as `rev` in your `lakefile.toml`.
  This ensures all transitive deps (proofwidgets, batteries, aesop, etc.)
  resolve to versions tested together.

**Pin to commit hashes, not tags or branch names:**

- `rev = "master"` or `rev = "main"` — breaks when upstream updates.
- `rev = "v4.16.0"` — tag may target a different Lean version than
  you expect (Mathlib version numbers ≠ Lean version numbers).
- `rev = "f897ebcf72cd..."` — **preferred**. Reproducible and stable.

**When `lake update` changes `lean-toolchain` automatically:**

Lake overwrites `lean-toolchain` if a dep requires a different version.
This makes the file dirty and blocks `git pull`. Fix with
`git checkout lean-toolchain` before pulling, then let `lake update`
set it again.

### Recovery from broken `.lake/`

When dependency resolution is broken, **move** (don't delete) the
`.lake/` directory and re-resolve:

```bash
mv .lake /tmp/lake-backup-$(date +%s)
lake update
```

Using `mv` to `/tmp` is safer than `rm -rf` — you can recover if
the new resolution also fails.

### Root Lake workspace (standardized)

The repo is a **single Lake workspace** rooted at `/lakefile.toml`
with one `lean-toolchain` at the root.  Every paper is a Lake
**package** (`qou`, `ugb`, `fred2005`) declared via `[[require]]`.
Prefer running `lake` from the **repo root**:

```bash
lake build           # build all papers
lake build QOU       # just the QOU library
lake build UGB       # just the UGB library
lake exe cache get   # Mathlib cache for the workspace
```

Per-paper `cd content/<paper>/lean && lake build` still works as a
standalone build path, but CI, the MCP `lean_build` tool, and the
skills here all prefer the root workspace.  The registry mapping
short-form package names to paper directories lives in
`folio-assistant/schemas/lean-packages.ts`.

## Blueprint Synchronization

The Formalizer must keep Lean declarations in sync with the blueprint:

1. Every Lean declaration referenced by `\lean{}` in
   `blueprint/src/content.tex` must exist in the Lean source
2. When a `sorry` is resolved, update the blueprint entry to add `\leanok`
3. When adding new theorems, add a corresponding entry to
   `blueprint/src/content.tex` with `\lean{}` and `\uses{}` edges
4. The `-- Ref: [key]` in Lean must match `\cite{key}` in the blueprint
   where applicable, ensuring bibliography consistency across both systems

## Content Object Integration

The authoritative source of truth is the **content object** triple, not raw
LaTeX. Every formalizable block is defined by three sibling files:

```
content/<paper>/<chapter>/
  <block-name>.ts    ← Manifest: kind, label, lean.ref, uses[]
  <block-name>.md    ← Narrative (markdown + TeX snippets)
  <block-name>.lean  ← Lean formalization (when required by kind)
```

### Block kind determines Lean requirements

| Block kind | Lean required? | Completeness criteria |
|-----------|---------------|----------------------|
| `definition` | **Yes** (enforced) | `.ts` has `lean.ref` (URI form `pkg:Decl`), sibling `.lean` exists, compiles |
| `theorem`, `lemma`, `proposition`, `corollary` | **Expected** (warning) | Same as definition |
| `example`, `remark`, `conjecture` | Optional | `.lean` only if author requests |
| `prose`, `equation`, `diagram` | N/A | No Lean needed |

### Workflow with content objects

1. **Read the `.ts` manifest** to get `lean.ref` (parse with
   `parseLeanRef()` from `folio-assistant/schemas/lean-packages.ts`
   to extract `{ package, decl, module, name }`) and `uses[]`
2. **Check `uses[]`** to understand upstream dependencies — ensure they're
   formalized first (dependency DAG ordering)
3. **Write/update the sibling `.lean` file** in `content/<paper>/<chapter>/`
4. **Update the `.ts` manifest**: set `lean.ref` to the package-qualified
   URI `"<pkg>:<Decl.Path>"` (per CLAUDE.md §0a; legacy `lean.decl` /
   `lean.file` shape is removed)
5. **Run validation**: `bun run content/pipeline/validate.ts` to check
   cross-references and constraint rules

### Glossary terms in narrative `.md`

If you author or update the `.md` sibling alongside a Lean file, defined
terms (any slug in any block's `defines: [...]`) **must** be wrapped in
`:defterm[…]{#slug}` (canonical site) or `:refterm[…]{#slug}` (every
other mention). Do **not** add `\emph{}` or plain-text mentions of
defined terms. The Lean side is unaffected by this contract — Lean
declarations are linked via `lean.ref`, not glossary slugs — but the
validator will flag stray plain-text mentions in the narrative
companion. See `local/glossary-build`.

### The `uses[]` dependency graph

The `uses` field in `.ts` manifests forms a narrative dependency DAG.
**List only immediate neighbors** — if A depends on B and B depends on C,
A lists only B (not C). Transitive deps are derived by walking the graph.
Run `bun run pipeline/prune-transitive-deps.ts` to enforce this.

- When formalizing a theorem, walk the `uses[]` graph to check that all
  upstream blocks are already formalized (or have `sorry`-bridged stubs)
- The Lean import graph should mirror the `uses[]` graph
- Use `uses[]` to prioritize: formalize blocks with the most dependents first

## Post-proof simplification pass

After completing a proof (or batch of proofs), run a simplification pass
before committing. This catches verbose patterns that accumulate during
iterative proof development.

### Checklist (apply in order)

1. **`by exact X` → `X`** — drop the tactic mode wrapper when a single
   term suffices. Similarly `by rfl` → `rfl`.

2. **`unfold f; simp [...]` → `simp [f, ...]`** — `simp` can unfold
   definitions directly; the separate `unfold` is redundant.

3. **`unfold f; rw [...]` → `simp [f, ...]`** — when the rewrite chain
   is just normalization, `simp` with the definition is cleaner.

4. **Intermediate `have` → inline in `linarith`/`simp`** — if a `have`
   exists only to feed the next tactic, pass it inline:
   ```lean
   -- Before:
   have h := foo; linarith
   -- After:
   linarith [foo]
   ```

5. **Multi-line `apply; apply` → single `exact`** — chain applications:
   ```lean
   -- Before:
   apply div_pos; apply sq_pos_of_ne_zero _ h
   -- After:
   exact div_pos ... (sq_pos_of_ne_zero _ h)
   ```

6. **Tautological theorems** — never create theorems that just restate a
   structure field (`theorem foo (s : S) : ... := s.field`). Callers
   should use `s.field` directly.

7. **`@Zero.zero T inst.toZero` → `(0 : T)`** — let Lean infer instances.

8. **Retraction pattern** — when proving `(f ∘ₗ g) x = x` from
   `f ∘ₗ g = LinearMap.id`, prefer:
   ```lean
   congr_fun (congr_arg DFunLike.coe h_retraction) x
   ```
   over `rw [h]; rfl`.

9. **Dead code** — remove duplicate docstrings, stale comments, and
   unreferenced helper lemmas.

## Checklist

- [ ] All theorem statements match the `.md` narrative originals
- [ ] Import blocks are minimal and correct
- [ ] Every `sorry` is tracked in `proof-objects.json`
- [ ] Every `sorry` has a `-- Ref: [key] url` comment (citation-linked)
- [ ] All `-- Ref:` keys exist in `content/schema/references.ts`
- [ ] `lake build` succeeds (sorry warnings are expected)
- [ ] Tactic choices match the narrative proof strategy
- [ ] Proof state can be exported at every sorry site
- [ ] `blueprint/src/content.tex` entries match Lean declarations
- [ ] `\leanok` only on sorry-free declarations
