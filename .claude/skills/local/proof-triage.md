---
name: proof-triage
description: >
  Systematically triages and resolves `sorry` stubs across the Lean codebase.
  Inventories all sorry sites, orders them by dependency, attempts proofs using
  mathlib/library search, and escalates to a proof writer with similar-lemma
  suggestions when stuck.
allowed-tools: Read Write Edit Bash Grep Glob Agent
---

# Proof Triage & Resolution

## Overview

This skill examines the entire Lean codebase for unresolved `sorry` markers,
builds a dependency-ordered work list, and iteratively attempts to replace each
`sorry` with a valid proof or well-typed definition.  When a proof attempt
fails, it searches existing libraries for similar statements and presents these
to a proof writer for guidance.

## When to Use This Skill

- After a formalization pass leaves `sorry` stubs
- After a `lake build` produces sorry warnings or type errors
- When onboarding a new chapter and filling in proof obligations
- Periodically as a "proof debt" sweep

## Prerequisites

- `lake build` can be run (even if it produces sorry warnings)
- Mathlib4 and any project-specific libraries are in `lakefile.lean`
- The Lean files follow QOU naming conventions

## Workflow

### Phase 1 — Inventory

1. **Grep for `sorry`** across all `.lean` files under `lean/QOU/`
2. For each hit, classify into one of:
   - **Type stub**: `def X : Type* := sorry` — needs a concrete type or structure
   - **Proof stub**: `theorem/lemma ... := sorry` or `by sorry` — needs a proof
   - **Field stub**: a structure field defaulting to `sorry` — needs a value or proof
   - **Axiom placeholder**: `sorry` with a comment like "deferred to Ch.N" — skip for now
3. Record each sorry site:
   - File path and line number
   - Declaration name
   - Classification (type / proof / field / axiom-placeholder)
   - Statement signature (hypotheses and goal type)
   - Any `-- sorry:` or adjacent comment explaining the deferral

### Phase 2 — Dependency Ordering

1. For each sorry site, identify **what it depends on**:
   - Other definitions/structures referenced in its type signature
   - Imports from mathlib or other project files
2. Build a rough dependency DAG:
   - Glossary type stubs are leaves (no intra-project dependencies)
   - Theorem stubs depend on the structures they quantify over
   - Chapter-level theorems may depend on cross-chapter definitions
3. **Priority ordering** (work on these first → last):
   1. Standalone field proofs (e.g. `error_nonneg : 0 ≤ x`)
   2. Classical limit theorems (`q = 1` ⟹ classical)
   3. Algebraic identities provable by `ring` / `field_simp` / `linarith`
   4. Approximation lemmas requiring `norm_num` or `native_decide`
   5. Type stubs that need concrete structure definitions
   6. Deep mathematical content deferred to later chapters

### Phase 3 — Iterative Proof Attempts

For each sorry site, in priority order:

1. **Read the declaration** and its surrounding context (10 lines above/below)
2. **Identify the goal type** — what needs to be proved or constructed
3. **Search mathlib** for relevant lemmas:
   - Use `Grep` to search mathlib source for key terms in the goal
   - Check `Mathlib.Tactic` for applicable automation (`norm_num`, `positivity`,
     `field_simp`, `ring`, `linarith`, `simp`, `omega`)
   - Look for `exact?`, `apply?`-style matches by examining lemma signatures
4. **Attempt a proof**:
   - Start with the simplest tactic chain: `by simp`, `by ring`, `by linarith`
   - If those fail, try `unfold ...; simp/ring/linarith`
   - For positivity goals: `by positivity` or `by linarith` with explicit bounds
   - For approximation: `by norm_num` or `by native_decide`
   - For algebraic: `by ring` or `by field_simp; ring`
5. **Test the proof** by running `lake build` on the specific file
6. **Record the outcome**:
   - **Success**: mark as resolved, move to next
   - **Failure**: capture the error message, proceed to Phase 4

### Phase 4 — Escalation to Proof Writer

When a proof attempt fails:

1. **Document the failure**:
   - The exact declaration and goal type
   - What tactics were tried and what errors resulted
   - The specific Lean error message
2. **Search for similar statements**:
   - Grep mathlib for lemmas with similar conclusion types
   - Look for generalizations that could be specialized
   - Check if the statement holds under stronger hypotheses
3. **Present to proof writer** with:
   - The original statement
   - 2–3 similar lemmas from mathlib that are "close but not matching"
   - A suggestion of which mathlib lemma might be adaptable
   - Any missing hypotheses that would make the proof go through
4. **Iterate**: incorporate proof writer feedback, retry, repeat

### Phase 5 — Build Verification

After each batch of resolved sorries:

1. Run `lake build` on the modified files
2. Check for:
   - New type errors introduced by proof changes
   - Sorry warnings (expected for remaining stubs)
   - Successful compilation of resolved proofs
3. If a previously-resolved proof breaks:
   - Add it back to the work list
   - Re-examine dependencies that may have changed

### Phase 6 — Commit & Report

1. Commit resolved proofs in logical batches:
   - One commit per file, or per thematic group
   - Message pattern: `feat(lean): prove <theorem-names> in <File>.lean`
2. Generate a summary table:

   | Declaration | File | Status | Tactic | Notes |
   |-------------|------|--------|--------|-------|
   | `error_nonneg` | KnotTheory | Resolved | `linarith` | — |
   | `main_commutative_diagram` | QOU | Deferred | — | Ch.11 |

3. Update any tracking files (proof-objects.json if present)

## Tactic Cheat Sheet

| Goal Pattern | Try First | Then Try |
|-------------|-----------|----------|
| `0 ≤ x` | `positivity` | `linarith [hyp]` |
| `x = y` (algebraic) | `ring` | `field_simp; ring` |
| `x = y` (definitional) | `rfl` | `unfold ...; rfl` |
| `x = 0` (classical limit) | `unfold ...; rw [h]; ring` | `simp [h]` |
| `x < y` (numeric) | `norm_num` | `linarith` |
| `∃ x, P x` | `exact ⟨witness, proof⟩` | `use witness; simp` |
| `P ∧ Q` | `exact ⟨proof_P, proof_Q⟩` | `constructor <;> simp` |
| `P → Q` | `intro h; exact ...` | `fun h => ...` |
| Anything | `simp` | `aesop` |

## Feedback & Iteration Notes

- **Glossary type stubs** (`def X : Type* := sorry`) are usually not provable
  — they represent abstract types that need concrete mathematical definitions.
  Resolving these requires designing the right Lean structure, not finding a
  proof.  Treat them as **design tasks**, not proof tasks.
- **Deferred axiom placeholders** should be skipped unless the referenced
  chapter has been formalized.  Check comments for `-- deferred to Ch.N`.
- **Build errors vs sorry warnings**: A sorry warning means the file compiles
  but has holes.  A build error means something is broken.  Always fix build
  errors before attempting new proofs.
- **When stuck for >10 minutes on a single sorry**: escalate.  The iterative
  approach means it's better to move on and come back with new information than
  to grind on one proof.

## Checklist

- [ ] All `.lean` files grepped for `sorry`
- [ ] Each sorry classified (type / proof / field / axiom-placeholder)
- [ ] Dependency order established
- [ ] Easy proofs attempted first (positivity, ring, classical limits)
- [ ] Mathlib searched for similar lemmas on failed attempts
- [ ] Failed proofs documented with similar-lemma suggestions
- [ ] `lake build` passes (sorry warnings OK, errors not OK)
- [ ] Resolved proofs committed with descriptive messages
- [ ] Summary table generated
