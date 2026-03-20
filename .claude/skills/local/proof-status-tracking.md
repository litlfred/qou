---
name: proof-status-tracking
description: >
  Maintain the proof-objects.json manifest tracking formalization status,
  review records, and LaTeX-to-Lean linkages.  Generate status dashboards
  and enforce review policies.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Proof Status Tracking

## Overview

This skill manages the `proof-objects.json` manifest — the single source of
truth for which mathematical objects have been formalized, reviewed, and
approved.  Lean declarations are referenced by URL (doc-gen4 pages), not
duplicated in JSON.

## When to Use This Skill

- After extracting proof objects from LaTeX
- After updating Lean proofs
- When generating status reports
- When checking review coverage before publication
- When linking proof objects to mathlib4 declarations

## Proof-Objects Manifest

**File:** `proof-objects.json`
**Schema:** `schemas/proof-objects.schema.json`

### Formalization Status Flow

```
not_started ──► stated ──► has_sorry ──► proved ──► mathlib_ok
    │              │           │            │
    │              │           │            └── Merged into mathlib4
    │              │           └── Lean decl exists, some sorry remaining
    │              └── Lean decl exists, fully sorry
    └── No Lean declaration yet
```

### Review Consensus

Multiple reviewers (human + agentic) contribute reviews.  Consensus rules:

1. **Any critical issue** → `REQUEST_CHANGES` regardless of other reviews
2. **All APPROVE with confidence ≥ 0.7** → consensus APPROVE
3. **Mixed verdicts** → `NEEDS_DISCUSSION`
4. **Human APPROVE overrides** agentic NEEDS_DISCUSSION

### Scripts

| Script | Purpose |
|--------|---------|
| `extract_proof_objects.py` | Parse LaTeX → proof-objects.json |
| `generate_lean_stubs.py` | proof-objects.json → lean stub files |
| `update_proof_status.py` | Lean build log → update statuses |

### GitHub Actions Integration

The `lean-build.yml` workflow:
1. Runs `extract_proof_objects.py`
2. Runs `generate_lean_stubs.py`
3. Runs `lake build`
4. Runs `update_proof_status.py`
5. Commits updated `proof-objects.json` (automated commit by `github-actions[bot]`)

## Status Dashboard

The proof status is published to GitHub Pages alongside the paper.
Key metrics:

- Total objects / formalized / proved / reviewed
- Objects with critical review issues
- Dependency graph (which proofs are blocked)
- Coverage by review type

## Review Policy

| Criterion | Requirement |
|-----------|-------------|
| Minimum reviewers per object | 2 (at least 1 human for theorems) |
| Required review types | scientific-accuracy, lean-proof-check |
| Maximum sorry for publication | 0 in core theorems |
| Confidence threshold | ≥ 0.7 average across agentic reviewers |

## Current Snapshot (as of 2026-03-20)

| Metric | Value |
|--------|-------|
| Total .lean files | 18 |
| Total declarations | ~133 |
| Substantive proofs | ~99 |
| Active sorry stubs | 27 |
| Trivial proofs (rfl/simp) | 6 |
| Axiom declarations | 0 |
| Admit statements | 0 |

### Sorry distribution

- `FormalGroups.lean`: 11 (external [fred2005])
- `PAdicQuantumGroups.lean`: 4 (external [fred2005])
- `QuantumObservableUniverse.lean`: 2 (core theory)
- `HadronicMass.lean`: 2 (tactic limitation — `Real.rpow`)
- `BringsSurface.lean`: 2 (deep math)
- `DescartesUniverse.lean`: 1 (Tannaka–Krein rigidity)
- `Torsion.lean`: 1 (commented out — inactive)

### Consistency notes

- All sorry stubs carry bibliographic citations — no orphaned stubs
- No `axiom` or `admit` hacks masquerading as proofs
- `FormalGroups.lean` documents its sorry-by-design policy in a file header

## Checklist

- [ ] `proof-objects.json` validates against `schemas/proof-objects.schema.json`
- [ ] All theorem/lemma/proposition objects have at least one review
- [ ] No critical issues in any review
- [ ] Formalization status matches actual Lean build output
- [ ] Sorry count matches current inventory (27 active)
- [ ] Dependency edges are complete (all `\uses{}` captured)
