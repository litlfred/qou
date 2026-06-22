# Lean Vacuity & Audit Remediation Plan

This document outlines the decomposition of the 199 self-assuming projections (R1) and 111 placeholder-true stubs (R2) into tasks assigned to specialized worker subteams.

## Specialized Worker Subteams & Scope

To address the findings within the limit of at most 8 concurrent active subagents (including the Project Orchestrator), the codebase is partitioned into target directories assigned to 6 specialized worker subagents:

1. **BraidKnot Swarm** (`braidknot-remediator`)
   - **Target Directories:** `lean/QOU/BraidKnot`, `lean/QOU/BraidsKnots`, `lean/QOU/Braiding`, `lean/QOU/BraidsAndKnots`
   - **Scope:** 33 self-assuming projection defects (R1) + associated placeholder-true stubs (R2).

2. **Archimedean Swarm** (`archimedean-remediator`)
   - **Target Directories:** `lean/QOU/Archimedean`, `lean/QOU/LiftingDescent`, `lean/QOU/AppendixSurreals`
   - **Scope:** 23 self-assuming projection defects (R1) + associated placeholder-true stubs (R2).

3. **Particle Swarm** (`particle-remediator`)
   - **Target Directories:** `lean/QOU/ParticleInteractions`, `lean/QOU/Interactions`, `lean/QOU/HadronicMass`, `lean/QOU/TopologicalMass`
   - **Scope:** 19 self-assuming projection defects (R1) + associated placeholder-true stubs (R2).

4. **Fluid & Torsion Swarm** (`fluid-torsion-remediator`)
   - **Target Directories:** `lean/QOU/FluidDynamics`, `lean/QOU/Torsion`, `lean/QOU/Molecular`
   - **Scope:** 9 self-assuming projection defects (R1) + associated placeholder-true stubs (R2).

5. **QOU Substrate Swarm** (`qou-substrate-remediator`)
   - **Target Directories:** `lean/QOU/AlgebraicSubstrate`, `lean/QOU/Observations`, `lean/QOU/QuantumObservableUniverse`, `lean/QOU/WedderburnMass`, `lean/QOU/Information`
   - **Scope:** 25 self-assuming projection defects (R1) + associated placeholder-true stubs (R2).

6. **General Swarm** (`general-remediator`)
   - **Target Directories:** sibling-`.lean` (under chapter directories, not under `lean/QOU/`) and miscellaneous files
   - **Scope:** 90 self-assuming projection defects (R1) + associated placeholder-true stubs (R2).

---

## Remediation Strategy

### 1. R1 (Self-Assuming Projections)
A class that carries the block's own conclusion as a field, with a theorem that merely projects it (e.g. `:= ctx.claim_foo` or `:= ⟨ctx.a, ctx.b⟩`), is a vacuous self-assuming projection.
- **Option A (Preferred):** Restate the class to carry the *hypotheses* rather than the conclusion, and derive/compose the conclusion using tactics or the constructor fields.
- **Option B (Demotion):** Demote the `theorem` to `conjecture` or `remark` if no honest derivation exists or is currently formalizable.

### 2. R2 (Placeholder-True Stubs)
Stubs of shape `: True := trivial` or `: True := by sorry` which do not have a corresponding real formalization elsewhere.
- **Option A:** State the real proposition and use `sorry` together with a citation comment `-- Ref:`.
- **Option B:** Demote the `theorem` to a `conjecture` or `remark` if the real proposition cannot be stated.

---

## Compilation & Build Workflow (R4)
All code changes must compile successfully under the native macOS environment:
- Active toolchain: `leanprover/lean4:v4.24.0` (invoked via `~/.elan/bin/lake`).
- Verification command: `~/.elan/bin/lake build`.

---

## Vacuity Verification (R5)
- Run `~/.bun/bin/bun run content/pipeline/lean-vacuity-axiom-audit.ts` to verify findings.
- The target is **0** high-confidence findings.
