---
id: qou-lanx
title: "Lean KG Stage 4: Author Monograph Annex Describing Reusable Mathlib-Ready Lean Libraries & QOU Formalization Subgraphs"
status: todo
type: feature
priority: high
parent: qou-lnkg
blocked_by:
  - qou-lref
created_at: 2026-11-23T20:22:30Z
updated_at: 2026-11-23T20:22:30Z
---

## Deliverables
Create and wire a dedicated monograph Appendix/Annex (`appendix-lean-libraries`) presenting:
1. The layered Knowledge-Graph DAG (`Mathlib4` -> Pure-Math Reusable Subgraphs -> QOU Categorical Core -> Archimedean/Empirical Comparison Boundary).
2. Catalog of QOU's general-purpose `Mathlib4`-upstreamable libraries (Iwahori-Hecke & Temperley-Lieb GS/Markov/Hoefsmit, Nakayama-Twisted Frobenius & Sweedler/Taft/`O_q(SU(2))` Hopf algebras, Thomae-Jackson `q`-calculus, Bring curve & Octonion `G_2`, Symmetry-Reduced Conic Duality & Sturmfels-Thomas Toric Gröbner bases, Finite Rieffel Quantum Metric Spaces, PL Knot Topology).
3. Trust & axiom boundary (`[propext, Classical.choice, Quot.sound]` only, `0 sorry`, `0 custom axioms`, §7c base-ring stratification).


## Updated Scope (`2026-11-23`): Community Contrib Libraries Annex
Describe both Tier-A (`Mathlib4` core upstreaming lemmas) and Tier-B (the 6 standalone Reservoir-ready Lean 4 community contribution libraries `HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`) in `appendix-lean-libraries`, including `lakefile.toml` dependency DAG, public API surface, and `Mathlib4` linter/axiom guarantees.
- **Consolidation Note (`qou-anx0`):** Evolve and consolidate existing `folio/quantum-observable-universe/appendix-formalisation-notes/` (`25` blocks) directly into this Annex rather than creating a second Lean appendix.
