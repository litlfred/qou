---
# qou-qc6s
title: def:mass-identity — categorical-trace mass over R is unformalised; audit corpus for conflated 'categorical mass' terminology
status: completed
type: task
parent: qou-ywyq
priority: normal
created_at: 2026-08-15T23:26:00Z
updated_at: 2026-08-15T23:29:36Z
---

## RESOLVED 2026-08-15 — the ref pointed at the wrong declaration entirely

`mass-endomorphism/mass-identity.ts` carried `qou:QOU.categoricalMass`. That is not this block's declaration, and it never was.

**The canonical declaration is `QOU.Torsion.MassIdentity`** (`QOU/Torsion/MassIdentity.lean:17`), which carries the block's **own LaTeX label**:

```lean
/-- **Mass Identity**: `m = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖ = ‖Hol_{∇_A}(γ; 𝔊)‖`.
    LaTeX: `\label{def:mass-identity}` -/
structure MassIdentity (M : Type*) where
```

Corroborated by the sibling blocks in the same chapter, which already point into this family: `mass-identity-C.ts` → `QOU.MassIdentityC`, `mass-identity-exists.ts` → `QOU.MassIdentity.exists`, `mass-identity-unique.ts` → `QOU.MassIdentity.unique`. This block was the odd one out. Repointed to `qou:QOU.Torsion.MassIdentity` (namespace-accurate; verified through the canonical resolver → `QOU/Torsion/MassIdentity.lean`).

Why no earlier pass caught it: every matcher keyed on the ref's own name (`categoricalMass`), so it searched for the wrong thing. The label was the evidence, not the name.

## Terminology audit — "categorical mass" names **four** distinct constructs

The conflation the owner suspected is real. In the Lean tree:

| declaration | what it is | ring |
|---|---|---|
| `QOU.PhotonThreading.categoricalMass` | `m_H = (q−1)²·E_H` from crossing energy | `ℝ` |
| `QOU.BraidKnot.MassFormulaCategorical.categoricalMass` | `M(T_w) = ρ·m_e·|tr_M(T_w)|` (cat units) | `ℝ` |
| `QOU.Torsion.CategoricalMassDecomposition` | decomposition structure (`TopologicalMass.lean`) | — |
| `QOU.CategoricalMassMarkov` | Markov-trace mass **endomorphism** carrier | generic `[Ring A]` |

Plus `categoricalMassMeV`, `categorical_mass_ge_descended`, `categorical_mass_pos_of_transient`. **Nothing is wrong with any of them individually** — they are different objects in different namespaces, so Lean sees no clash. The hazard is referential: a `lean.ref` (or a reader) saying "categorical mass" does not identify a declaration, which is exactly how this block acquired a wrong ref that then resolved to the import aggregator and passed vacuously.

`QOU.CategoricalMassMarkov` is already the canonical declaration for a *different* block (`mass-endomorphism/categorical-mass-markov-trace-endomorphism-intro.ts`, per its own docstring), so it was never a candidate here.

## Open, recorded — a §7c gap between this block and its Lean

The block's `.md` is explicit that the pre-archimedean mass is **valued in the generic ground ring `R`** ("the Frobenius norm `‖x‖_F = ⟨x,x⟩_F` stays in `R`"), with a named post-τ realisation `R → ℝ`. The Lean `MassIdentity` structure is `ℝ`-valued (`connectionGradient : M → ℝ`, `leviCurvatureCoupling : M → ℝ`), and the `.md`'s named identifiers `frobeniusMass` / `scalarMass` **do not exist** in the tree (only `frobeniusMassSquared` in `HeckeMassElement.lean`).

So the ref is now correct, but the formalisation is a **different formulation** (nonabelian multiplicative integration) from the one the prose defines (Frobenius–Hopf categorical trace), and it sits on the wrong side of §7c relative to the prose. Recorded, not silently reconciled — closing that gap is a formalisation task, not a ref edit.
