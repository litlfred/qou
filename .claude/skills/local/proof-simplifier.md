---
name: proof-simplifier
description: >
  Analyse small clusters (2–4) of connected proofs to find
  simplifications: shared lemmas, redundant constructions, factored
  abstractions, or shorter proof paths through the dependency graph.
allowed-tools: Read Edit Bash Grep Glob Agent
---

# Proof Simplifier

## Role

Review existing proofs in small connected clusters (2–4 declarations that
depend on each other) and identify simplifications across them.

## Lean MCP Tools (lean-lsp-mcp)

When the MCP server is available, use it for analysis and alternatives:

| Task | MCP tool | How it helps |
|------|----------|-------------|
| Identify slow tactics | `lean_profile_proof` | Pinpoint which tactic takes >1s |
| Try simpler alternatives | `lean_multi_attempt` | Test shorter tactic chains at the same position |
| Find shared lemmas | `lean_local_search` | Search project for reusable declarations |
| Find Mathlib shortcuts | `lean_leansearch` / `lean_loogle` | May find a single Mathlib lemma replacing 10 lines |
| Check "Try This" | `lean_code_actions` | `simp?` / `exact?` suggestions → minimal proof |
| Verify after simplification | `lean_diagnostic_messages` | Quick check without full `lake build` |
| Check axiom impact | `lean_verify` | Ensure simplification doesn't change axiom deps |

### MCP-first simplification

1. **`lean_profile_proof`** on each theorem in the cluster → identify slow spots
2. **`lean_multi_attempt`** at slow tactic positions → try simpler alternatives
3. **`lean_leansearch`** for the goal → maybe one Mathlib lemma replaces a chain
4. **`lean_code_actions`** with `simp?` → get the minimal simp lemma set
5. **`lean_verify`** after edit → confirm axiom soundness unchanged

## When to use

- After a batch of proofs has been filled in or reviewed
- When `proof-triage` flags a cluster as high-complexity
- When the author asks to simplify or streamline a proof network
- Proactively after any chapter-level editing pass

## Workflow

1. **Select a cluster.** Pick 2–4 declarations that form a connected
   subgraph of the proof dependency graph (e.g.\ a definition, its key
   lemma, and the theorem that uses both).

2. **Read all proofs.** Load the full LaTeX (and Lean, if formalised) for
   every declaration in the cluster.

3. **Check for simplifications.** Look for:

   | Pattern | Action |
   |---------|--------|
   | **Shared construction** — two proofs build the same intermediate object | Extract a shared lemma |
   | **Redundant hypothesis** — a condition assumed in one proof is already implied by another in the cluster | Remove the redundant hypothesis; add a remark |
   | **Shorter path** — a proof can invoke a result from the cluster directly instead of re-deriving it | Replace the derivation with a citation |
   | **Factored abstraction** — a common argument pattern appears across the cluster | Abstract into a named lemma or tactic |
   | **Unused generality** — a proof works in more generality than needed, making it longer | Specialise to the case actually used |
   | **Duplicate notation** — two proofs introduce the same local notation differently | Unify notation across the cluster |

4. **Propose changes.** For each simplification found:
   - State the pattern (from the table above)
   - Show the before/after for the affected declarations
   - Estimate the reduction in proof length (lines or steps)
   - Flag any downstream declarations that would need updating

5. **Confirm with the author.** Present simplifications as multiple-choice
   options (the author cannot type easily). Never apply a simplification
   that changes mathematical content without approval.

6. **Apply approved changes.** Edit LaTeX (and Lean stubs if they exist).
   Run `latex-validation` afterward to check cross-references.

## Interaction with other skills

| Skill | Interaction |
|-------|-------------|
| `formalizer` | After simplifying LaTeX, update Lean stubs if formalised |
| `lean-proof-review` | Re-review any Lean proofs affected by the simplification |
| `proof-status-tracking` | Update `proof-objects.json` if declarations are added or removed |
| `category-theory` | Consult for categorical simplifications (adjunction/naturality shortcuts) |
| `proof-triage` | Feeds clusters to this skill based on complexity scores |

## Constraints

- Never merge or delete declarations without author approval
- Keep all label/ref identifiers stable (or update all cross-references)
- Prefer fewer, simpler lemmas over clever one-liners
- Document the simplification in a `% Simplified from ...` comment
