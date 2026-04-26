---
name: lean-proof-review
roles: [collaborator, owner]
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

## Lean MCP Tools (paper-assistant)

When the MCP server is available, **use MCP tools for all review checks**:

| Review check | MCP tool | What it replaces |
|-------------|----------|-----------------|
| Type-checks (`lake build`) | `lean_diagnostic_messages` | Structured errors, no build needed |
| Sorry audit | `lean_diagnostic_messages` | Filter warnings for sorry count |
| Axiom dependencies | `lean_verify` | Returns axioms used + optional source scan |
| Tactic quality | `lean_profile_proof` | Identifies slow tactics in a theorem |
| Statement correctness | `lean_hover_info` | Check types of all symbols in statement |
| Cross-references | `lean_references` | Find all uses of a declaration |
| Declaration source | `lean_declaration_file` | Jump to where a symbol is defined |

### MCP-enhanced review workflow

1. **`lean_diagnostic_messages`** on the file under review → all errors/warnings
2. **`lean_verify`** on each theorem → axiom audit (no `sorry`, no `Decidable.em` surprises)
3. **`lean_profile_proof`** on complex theorems → flag tactics taking >1s
4. **`lean_hover_info`** on key terms → verify types match LaTeX intent
5. **`lean_references`** on modified declarations → check downstream impact

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

## Current Codebase State (as of 2026-03-21)

**0 active sorry** | **0 admit** | **0 axiom** | **~107 substantive proofs** | **6 trivial (rfl/simp)**

### Categorical Stubs (new 2026-03-21)

Eight new categorical structures added to `QuantumObservableUniverse.lean`:

| Lean identifier | Type | LaTeX label |
|----------------|------|-------------|
| `CategoricalQExtDeriv` | structure | `def:categorical-q-ext-deriv` |
| `CategoricalInstanton` | structure | `def:categorical-instanton` |
| `categorical_irreducible` | theorem | `lem:categorical-irreducible` |
| `categorical_self_duality` | theorem | `prop:categorical-self-duality` |
| `categorical_dq_squared` | theorem | `prop:categorical-dq-squared` |
| `CategoricalJet` | structure | `def:categorical-jet` |
| `categorical_jet_prolongation` | theorem | `prop:categorical-jet-prolongation` |
| `CategoricalTransport` | structure | `def:categorical-transport` |

### Known Patterns

- All sorry stubs have been eliminated; former sorry-bearing files
  (`FormalGroups.lean`, `PAdicQuantumGroups.lean`, `HadronicMass.lean`)
  now have complete proofs or structural placeholders (`rfl`, `True`)
- `BringsSurface.lean` trivial proofs (`by rfl`): these are definitional
  equalities for genus/euler-char/etc. — correct and appropriate

## Content Object Integration

Each Lean file under review is part of a **content object triple**: the
`.lean` sibling has a corresponding `.ts` manifest and `.md` narrative.
Reviews must cross-check all three.

**Manifest–Lean consistency.** Verify that:
- The `lean.ref` URI in the `.ts` manifest (form `"<pkg>:<Decl>"`) names
  the actual Lean declaration in the `.lean` file. Parse with
  `parseLeanRef()` from `folio-assistant/schemas/lean-packages.ts`.
- The block `kind` matches the Lean content: `definition` blocks should
  contain `def` or `structure`; `theorem`/`lemma` blocks should contain
  `theorem` or `lemma`.
- The `label` prefix is correct for the kind (`def:`, `thm:`, `lem:`,
  `prop:`, `cor:`).

**Dependency satisfaction.** The `uses[]` array in the `.ts` manifest
lists content object labels this block depends on. Verify that the `.lean`
file imports or references the Lean declarations corresponding to those
dependencies. Missing imports suggest incomplete formalization.

**Status accuracy.** Formalization status is derived at build time from
`.lean` file content — agents do not need to update any status field.

## Checklist

- [ ] All modified Lean files compile (`lake build`)
- [ ] Review records include `reviewer_id`, `verdict`, `confidence`
- [ ] Critical issues block merge
- [ ] `sorry` count is accurately tracked (current: 0 active)
- [ ] Linked LaTeX content is consistent with Lean statements
- [ ] All sorry stubs have bibliographic citations or blocking-reason comments
