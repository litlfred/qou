---
name: lean-proof-review
description: >
  Review Lean 4 proofs for correctness, style, and completeness.
  Tracks review scores from multiple reviewers (human and agentic) in
  proof-objects.json.  Integrates with the agent-review pipeline.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Lean Proof Review

## Overview

This skill defines how Lean proofs are reviewed by human and agentic reviewers.
Reviews are stored as structured records in `proof-objects.json`, attached to
individual proof objects.  The skill integrates with the existing agent-review
workflow.

## When to Use This Skill

- When reviewing a PR that modifies `lean/QOU/*.lean` files
- When reviewing LaTeX changes that affect theorem statements
- When running the agent-review pipeline with Lean content
- When a Gemini code review touches files linked to proof objects

## Review Types

### 1. Lean Proof Check (`lean-proof-check`)

Verifies:
- Declaration type-checks (`lake build` passes)
- No unexpected `sorry` usage
- Correct use of mathlib tactics and lemmas
- Style conformance (naming, documentation)

### 2. Mathematical Rigor (`mathematical-rigor`)

Verifies:
- The Lean statement faithfully captures the LaTeX theorem
- Proof strategy is sound (not just type-correct but mathematically meaningful)
- Dependencies are correctly modeled

### 3. Scientific Accuracy (`scientific-accuracy`)

Existing review type — extended to cover Lean formalization:
- Does the formal statement match the mathematical intent?
- Are physical/mathematical assumptions correctly encoded?

## Review Record Schema

Each review is stored in `proof-objects.json` under the object's `reviews` array:

```json
{
  "reviewer_id": "claude-opus-4",
  "reviewer_type": "agentic",
  "review_type": "lean-proof-check",
  "timestamp": "2026-03-19T12:00:00Z",
  "verdict": "APPROVE",
  "confidence": 0.85,
  "severity_counts": { "critical": 0, "major": 0, "minor": 1 },
  "issues": [],
  "lean_status": {
    "sorry_count": 0,
    "type_checks": true
  },
  "commit_sha": "abc1234"
}
```

### Verdicts

| Verdict | Meaning |
|---------|---------|
| `APPROVE` | Proof is correct and complete |
| `REQUEST_CHANGES` | Issues found that must be fixed |
| `NEEDS_DISCUSSION` | Reviewer is uncertain; human input needed |

### Confidence Scores

For agentic reviewers:
- **0.9–1.0**: High confidence (straightforward proof, well-known techniques)
- **0.7–0.9**: Moderate confidence (complex proof, reviewer can follow the logic)
- **0.5–0.7**: Low confidence (advanced techniques, reviewer may miss subtleties)
- **< 0.5**: Very low confidence (flag for human review)

## Integration with Agent Review Pipeline

The `agent_review.py` script includes a `LEAN_REVIEW_SYSTEM` prompt for
reviewing Lean proofs.  When a commit touches `lean/QOU/*.lean` files:

1. The diff is sent to all configured LLMs with the Lean review prompt
2. Each LLM produces a structured review
3. Reviews are stored in `proof-objects.json`
4. The coordinator synthesizes results

## Integration with Gemini Code Review

Google Gemini code review triggers on PRs.  To make it proof-aware:

1. `proof-objects.json` is in the repo — Gemini sees it in diffs
2. When `chapters/*.tex` changes, the JSON shows which Lean files are linked
3. `.github/copilot-instructions.md` instructs Gemini to check linked Lean
   declarations when reviewing LaTeX changes

## Current Codebase State (as of 2026-03-20)

**27 active sorry** | **0 admit** | **0 axiom** | **~99 substantive proofs** | **6 trivial (rfl/simp)**

### Known Sorry Patterns

All 27 sorry stubs follow a consistent pattern:
- Each has a bibliographic citation (e.g., `[fred2005, Theorem 4.12]`)
- No orphaned or unexplained sorry statements
- `FormalGroups.lean` has an explicit file-header doc block explaining that all
  dissertation-referenced theorems are left as `sorry` by design

### Review Considerations

- **`FormalGroups.lean` + `PAdicQuantumGroups.lean`** (15 sorry): treat as
  "external results" — review the *statements* for faithfulness to
  [fred2005], not the missing proofs
- **`HadronicMass.lean`** (2 sorry): numerically verified but blocked by
  `Real.rpow` evaluation — flag for tactic-level resolution, not mathematical
  review
- **`BringsSurface.lean`** trivial proofs (`by rfl`): these are definitional
  equalities for genus/euler-char/etc. — correct and appropriate, not
  placeholders

## Checklist

- [ ] All modified Lean files compile (`lake build`)
- [ ] Review records include `reviewer_id`, `verdict`, `confidence`
- [ ] Critical issues block merge
- [ ] `sorry` count is accurately tracked (current: 27 active)
- [ ] Linked LaTeX content is consistent with Lean statements
- [ ] All sorry stubs have bibliographic citations or blocking-reason comments
