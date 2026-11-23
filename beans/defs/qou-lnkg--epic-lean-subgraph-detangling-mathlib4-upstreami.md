---
# qou-lnkg
title: 'EPIC: Lean Topical Subgraph Detangling, Mathlib4 Upstreaming Preparation, KG Detangler Skill Upgrade, & Lean Libraries Annex'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:22:30Z
updated_at: 2026-11-23T23:30:34Z
parent: qou-hksc
---

## Measured Current State (`origin/main` @ `90aaaf4632d`)

QOU's Lean formalization currently spans **`~4,545` `.lean` files** (`~3,530` in `78` fragmented `lean/QOU/*/` subdirectories + `106` loose root `lean/QOU/*.lean` files + `909` chapter content `.lean` wrappers), exhibiting severe synonym fragmentation and outdated graph skills:
- **7 Braid/Knot dirs (`735` files):** `BraidKnot` (468), `BraidsAndKnots` (112), `Knot` (103), `Braiding` (35), `KnotTheory` (9), `BraidsKnots` (7), `Knots` (1).
- **7 Mass dirs (`570` files):** `Mass` (311), `MassTheory` (239), `MassEndomorphism` (9), `WedderburnMass` (5), `TopologicalMass` (3), `HadronicMass` (2), `AtomicMass` (1).
- **3 Hecke dirs (`154` files):** `Hecke` (102), `IwahoriHecke` (38), `HeckeAlgebra` (14).
- **3 Bring-curve dirs (`38` files):** `BringsSurface` (19), `Brings` (15), `HyperellipticQuintic` (4).
- **4 QOU-axiom dirs (`50` files):** `QuantumObservableUniverse` (30), `QuantumObservableUniverses` (18), `QuantumUniverse` (1), `CommutativeQOU` (1).
- **2 Eightfold dirs (`53` files):** `Eightfold` (51), `EightfoldWay` (2).
- **3+ Mathlib staging dirs (`533+` files):** `MathlibExt` (294), `Mathlib` (235), `Infra` (4), `MathlibInfra` (new), while `.claude/skills/local/lean-mathlibext-curator.md` still describes a single 5-section `QOU/MathlibExt.lean` file, `.claude/skills/local/content-graph.md` only detangles `.ts` prose blocks (with a stale `PR1` chapter table), and there is **no monograph Annex** documenting the reusable Lean libraries.

## 4-Stage Child Plan

1. **`qou-kgdt` (Stage 1 — Non-Conflicting Tooling & KG Analysis):** Upgrade `.claude/skills/local/content-graph.md`, `detangler-integration-watcher.md`, `ontologist.md`, and `lean-mathlibext-curator.md` + build `scripts/lean-kg-detangler.py` to extract the full module-import & declaration-level Knowledge Graph (`.jsonld` + DAG metrics), classify every `.lean` module as **Pure Mathlib-Candidate (`0` QOU model dependencies)** vs **QOU Framework Core** vs **Empirical/Archimedean Comparison**, detect cross-layer `QOU -> MathlibExt` leaks, and score synonym-directory merge clusters.
2. **`qou-mlib` (Stage 2 — Mathlib4 Best-Practices Audit & Upstreaming Staging Design):** Audit the `533+` `Mathlib`/`MathlibExt` files + pure-math gems inside `Hecke`, `BraidKnot`, `FrobeniusHopfData`, `Optimization`, `InformationTheory` against official `Mathlib4` upstreaming standards (`snake_case`/`UpperCamelCase`, minimal targeted `Mathlib.*` imports, `/-! ... -/` module & `/-- ... -/` decl docstrings, `@[simp]`/`@[ext]` API completeness, `#lint` `docBlame`/`simpNF`/`unusedArguments`, §7c maximal typeclass generality, zero `Real` leaks where `LinearOrderedField` suffices, zero `noncomputable` bloat), and **present concrete `AskUserQuestion` refactoring options** before moving files.
3. **`qou-lref` (Stage 3 — Post-Merge Topical Subgraph Consolidation, gated on active Lean PRs landing + owner option approval):** Execute the approved consolidation from `78` ad-hoc dirs + `106` root files into clean, strictly acyclic topical subgraphs:
   - **Pure `Mathlib`-Ready Subgraphs (`zero` QOU imports, upstream-ready PR bundles):** `Algebra.IwahoriHecke` & `Algebra.TemperleyLieb`, `RingTheory.TwistedFrobenius` & `HopfAlgebra` (Sweedler/Taft/`O_q(SU(2))`), `NumberTheory.QCalculus` (Thomae-Jackson), `AlgebraicGeometry.BringCurve` & `Algebra.OctonionG2`, `Optimization.SymmetryReducedConic` & `Combinatorics.ToricGroebner`, `Topology.CompactQuantumMetric` (Rieffel-KR) & `Topology.BraidKnot`.
   - **QOU Model Subgraphs (aligned 1-to-1 with monograph chapters):** `QOU.Core`, `QOU.LiftingDescent`, `QOU.BraidsAndKnots`, `QOU.BringsSurface`, `QOU.Confinement` (`L_0..L_4`), `QOU.EightfoldWay`, `QOU.Nuclear`, `QOU.MassTheory`, `QOU.StandardModel`, `QOU.FluidDynamics`, `QOU.InformationTheory`, `QOU.Molecular`, `QOU.Observations`, updating `.olean` caches and `lean.ref` pointers atomically.
4. **`qou-lanx` (Stage 4 — Monograph Annex on Reusable Lean 4 Libraries & Subgraph Architecture):** Author a crisp, scholarly monograph Appendix/Annex (`appendix-lean-libraries` / `tabLabel: "LEAN"`) documenting the DAG architecture, the `Mathlib4`-upstreamable pure-mathematics libraries developed for QOU (their main theorems, typeclass generality, and `Mathlib` target namespaces), and the verification boundary (`[propext, Classical.choice, Quot.sound]` only, `0 sorry`, `0 custom axioms`).


## Owner Clarification (`2026-11-23`): Two-Tier Community Contribution (`Reservoir` `lean_lib` Packages + Selective `Mathlib4` Core)

Target is **NOT** forcing every specialized mathematical theorem directly into monolithic `mathlib4` core, but structuring QOU's non-QOU-specific mathematics as **clean, `Mathlib4`-style Lean 4 Community Contributions** (Reservoir-ready standalone `lean_lib` targets depending *only* on `Mathlib` with zero `QOU.*` imports, plus selective `mathlib4` core PRs for small foundational lemmas):
1. **Tier A — Selective `Mathlib4` Core PRs:** General `List`/sort/foldl lemmas, basic Frobenius/Hopf definitions, `LinearOrderedField` inequalities, elementary `q`-calculus / Chebyshev identities.
2. **Tier B — Reservoir-Ready Lean 4 Community Contrib Libraries (`lean_lib` targets in `lakefile.toml`, extractable as standalone community repos):**
   - `HeckeTemperleyLieb` (Iwahori-Hecke, Temperley-Lieb, GS normal forms, Markov/GPMT traces, Hoefsmit representations)
   - `TwistedFrobeniusHopf` (Nakayama-twisted Frobenius, Sweedler `H_4`, Taft `T_n(zeta)`, Woronowicz `O_q(SU(2))`)
   - `ToricConicOpt` (Symmetry-reduced conic dual certificates, Perdew-Parr kinks, Sturmfels-Thomas Graver/UGB, multilevel `ConfinementLayer`)
   - `CompactQuantumMetrics` (Rieffel `Lip`-seminorms, Kantorovich-Rubinstein graph duality)
   - `QCalculus` (Thomae-Jackson `q`-calculus, `q`-IBP, quantum dilogarithms)
   - `BraidKnotOctonion` (PL knot topology & `Delta`-moves, braid invariants, Milnor `mu_123`, octonions `O` & `g_2`, Bring curve)
All Tier-A and Tier-B subgraphs enforce `Mathlib4` naming, docstring, minimal-import, `#lint`, and §7c typeclass-generality standards, and are documented in the Lean Libraries Annex (`qou-lanx`).
