---
name: lean-completeness-audit
roles: [collaborator, owner]
description: >
  Audit Lean formalization completeness across all papers: verify Lake
  project setup, check import coverage, identify missing .lean files for
  content blocks that require them, and report formalization gaps.
allowed-tools: Read Bash Grep Glob Agent
---

# Lean Completeness Audit Skill

## Role

Verify that every paper's Lean formalization is structurally complete:
correct Lake project setup, all required imports present, and content
blocks that require `.lean` files have them.

## When to Use This Skill

- "audit lean completeness"
- "check lean coverage"
- "which blocks are missing lean files?"
- "verify lean project setup"
- "formalization gaps"
- After adding a new paper or chapter
- Before tagging a release

## Audit Steps

### 1. Lake Project Discovery

Verify every paper with `.lean` files has a proper Lake project:

```bash
./scripts/lean-build-all.sh  # discovers via lean-toolchain files
```

**Required files** in each `content/<paper>/lean/`:
- `lakefile.toml` — Lake project config
- `lean-toolchain` — pinned Lean version
- Root module file (e.g., `QOU.lean`, `Fred2005.lean`)

**Cross-checks**:
- All `lean-toolchain` files pin the same Lean version
- All `lakefile.toml` files pin the same Mathlib commit hash
- `srcDir` in lakefile matches the directory structure

### 2. Import Graph Completeness

For each paper, verify the root module transitively imports all `.lean`
files in the project:

```bash
# List all .lean files
find content/<paper>/lean/ -name '*.lean' -not -path '*/.lake/*' | sort

# Check root module imports
cat content/<paper>/lean/<Root>.lean
```

Any `.lean` file not reachable from the root module won't be built.

### 3. Content Block → Lean Coverage

Cross-reference content `.ts` manifests against `.lean` files.
Per CLAUDE.md rules:

| Block kind | `.lean` required? |
|-----------|------------------|
| `definition` | **Yes** (enforced) |
| `theorem`, `lemma`, `proposition`, `corollary` | Expected (warning) |
| `conjecture`, `example`, `remark` | Optional |

For each paper:

```bash
# Find all content blocks with lean declarations
cd content/<paper>
grep -r '"lean"' --include='*.ts' -l | sort
```

Check that each `lean.decl` in a `.ts` manifest has a corresponding
declaration in the `.lean` files.

### 4. Cross-Paper Import Audit

Check for stale cross-paper imports (like the `FormalGroups` import
that was moved):

```bash
# In each paper's .lean files, find imports referencing other papers
grep -rn '^import' content/*/lean/ --include='*.lean' | grep -v '.lake'
```

Flag any import that references a module from a different paper's
namespace (these need cross-paper Lake dependencies or should be removed).

### 5. Sorry Audit

List all `sorry` occurrences and verify each has a bibliographic citation:

```bash
grep -rn 'sorry' content/*/lean/ --include='*.lean' | grep -v '.lake'
```

Per CLAUDE.md: every `sorry` must have a `-- Ref: [key]` comment.

### 6. Build Verification

Run builds for all papers:

```bash
./scripts/lean-build-all.sh
```

Report:
- Papers that build cleanly (0 errors, 0 sorry)
- Papers that build with sorry (warnings only)
- Papers that fail to build (errors)

## Output Format

```markdown
## Lean Completeness Audit

### Project Setup
| Paper | lakefile | toolchain | root module | status |
|-------|---------|-----------|-------------|--------|
| quantum-observable-universe | ✓ | v4.24.0 | QOU.lean | ✓ |
| unital-groebner-bases | ✓ | v4.24.0 | QOU.lean | ✓ |
| fred2005-formal-groups | ✓ | v4.24.0 | Fred2005.lean | ✓ |

### Build Status
| Paper | errors | warnings | sorry count |
|-------|--------|----------|-------------|

### Missing Lean Files
| Paper | Block | Kind | Label | Status |
|-------|-------|------|-------|--------|

### Stale Imports
(list any cross-paper imports that need attention)

### Sorry Without Citation
(list any sorry missing -- Ref: comment)
```

## Checklist

- [ ] All papers with .lean files have Lake projects
- [ ] All lean-toolchain files agree on version
- [ ] All lakefile.toml files pin same Mathlib commit
- [ ] Root modules import all project .lean files
- [ ] Definition blocks all have corresponding .lean files
- [ ] No stale cross-paper imports
- [ ] All sorry have bibliographic citations
- [ ] All papers build (at least with warnings)
