---
name: prepare-for-merge
roles: [collaborator, owner]
description: >
  Pre-merge checklist for feature branches.  Before merging new content
  into main, check what changed upstream, identify related content, and
  apply placement and density principles to ensure the merge result is
  structurally sound.
allowed-tools: Read Edit Write Bash Grep Glob Agent
---

# Prepare for Merge — Feature Branch Integration Skill

## Purpose

When a feature branch introduces new or significantly changed content
blocks, merging blindly can create forward references, section bloat,
cross-chapter coupling, and topic incoherence.  This skill ensures that
**before** a branch merges into `main`, the agent checks upstream for
related content and applies the placement and density principles.

## When to Use

- "prepare for merge" / "ready to merge" / "merge checklist"
- "check before merging" / "pre-merge review"
- Before any PR merge that adds or moves content blocks
- When a feature branch has been open long enough that `main` may have
  diverged with new related content

## Pre-Merge Workflow

### Step 1 — Identify new/changed content blocks on the branch

```bash
# List content .ts files changed vs main
git diff origin/main...HEAD --name-only -- 'content/**/*.ts' \
  | grep -v '/rendered/' | grep -v 'schema/' | grep -v 'pipeline/'
```

For each changed file, extract labels and `uses[]` dependencies:

```bash
for f in $(git diff origin/main...HEAD --name-only -- 'content/**/*.ts' \
  | grep -v '/rendered/' | grep -v 'schema/' | grep -v 'pipeline/'); do
  label=$(grep -oP "label:\s*['\"]\\K[^'\"]+" "$f" 2>/dev/null || echo "")
  uses=$(grep -oP "uses:\s*\[([^\]]*)\]" "$f" 2>/dev/null || echo "")
  if [ -n "$label" ]; then echo "$label  $uses  ($f)"; fi
done
```

### Step 2 — Check upstream for related new content

Fetch `main` and find content blocks added to `main` since the branch
point that are **related** to the feature branch's changes:

```bash
# Fetch latest main
git fetch origin main

# Find content blocks added on main since branch point
MERGE_BASE=$(git merge-base HEAD origin/main)
git diff "$MERGE_BASE"...origin/main --name-only -- 'content/**/*.ts' \
  | grep -v '/rendered/' | grep -v 'schema/' | grep -v 'pipeline/'
```

For each new upstream block, check whether it:

1. **Shares a `uses[]` dependency** with any block on the feature branch
   (same parent definition or theorem).
2. **Lives in the same section** as a block being added or moved.
3. **Addresses the same topic** (check `.md` content keywords against
   the chapter topic map in `content-graph` PR1).

If related upstream blocks exist, the agent must review them **before**
finalising placement of the feature branch's blocks.

### Step 3 — Apply placement principles (content-graph PR1–PR7)

Run the full placement checklist from `content-graph`:

1. □ Identify the primary topic → select home chapter (PR1)
2. □ Check `uses[]` deps appear earlier in document order (PR2)
3. □ Check target section has 3–18 blocks after insertion (PR3)
4. □ Verify no new forward cross-chapter edges (PR4)
5. □ Verify block is single-topic; split if not (PR5)
6. □ Extract tables > 5 rows to `table` blocks (PR6)
7. □ Update `docs/reorganization-map.md` if anything moved (PR7)

Pay special attention to PR2 and PR4 — a feature branch written against
an older `main` may create forward references or cross-chapter edges
that didn't exist when the branch was started but do now.

### Step 4 — Apply density principles (block-density R1–R4)

For every new or changed block, verify:

- **R1 — Single-topic coherence**: block addresses one topic only.
- **R2 — Block length**: block is ≤ 40 non-blank lines; if longer,
  review for splitting.
- **R3 — Table extraction**: no inline tables with > 5 data rows.
- **R4 — Child placement**: if the block was split from a parent,
  each child is in its topically correct chapter/section.

### Step 5 — Run the analysis script

```bash
cd content && python3 pipeline/content-graph-analysis.py
```

Confirm:
- Zero new forward references (H1)
- No section exceeds 18 blocks or drops below 3 (H4, H5)
- No new isolated blocks (H6)

### Step 6 — Resolve conflicts with upstream content

If Step 2 found related upstream blocks:

- **Duplicate content**: If both the branch and upstream added similar
  content, keep the more complete version.  Move the other to a
  `remark` interpreting it, or remove it.
- **Ordering conflicts**: If an upstream block should come before a
  branch block (or vice versa), reorder in the section manifest.
- **Dependency conflicts**: If both blocks need each other, refactor
  to break the cycle — extract the shared dependency into its own
  block.

### Step 7 — Final confirmation

Before approving the merge:

- [ ] All new blocks pass the placement checklist (Steps 3–4)
- [ ] `content-graph-analysis.py` reports no new HIGH findings
- [ ] `docs/reorganization-map.md` updated if blocks moved
- [ ] Branch rebased or merged with latest `main`
- [ ] Content validates: `cd content && bun run validate`

## Integration with other skills

| Situation | Skill to use |
|-----------|-------------|
| Placement decisions | `content-graph` PR1–PR7 — placement checklist |
| Block coherence / table extraction | `block-density` R1–R4 — density audit |
| Schema validation after merge | `content-validation` — structural integrity |
| Cross-chapter dependency analysis | `critical-path-analysis` — trace dependency chain |
| Forward reference diagnosis | `content-graph` H1 + `chapter-complexity-review` |
| Post-merge change report | `diff` — per-block change report with viewer links |
| Reorganisation tracking | `docs/reorganization-map.md` (PR7) |
