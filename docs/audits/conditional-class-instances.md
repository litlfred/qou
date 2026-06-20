# Discharge paths for upstream conjectural class instances

Five class-axiomatised conjectural inputs in
`particle-interactions/` and `braids-and-knots/` follow the
AGENTS.md §3b-cond pattern: each isolates a single conjecture as
a Lean class with one `sorry`-instance, and downstream conditional
theorems have no `sorry` in their proof bodies.  This audit tracks
the discharge path for each instance — what it would take to
instantiate the class.

## Inventory

| Class | File | Conjecture | Instance discharge target |
|-------|------|------------|---------------------------|
| `CrystalGraphRealization n q` | confinement-grading-correspondence-conditional.lean | conj:crystal-graph-realization (Brundan–Kleshchev intertwining + LP-shadow-price = KLR-grading) | Mathlib KLR algebra + cyclotomic Hecke quotient + explicit grading on QOU LP-shadow-price filtration |
| `HasThurstonTriangulation M hypVol` | thurston-volume-additivity.lean | classical [thurston1978] existence-of-ideal-triangulation for hyperbolic 3-manifolds | Mathlib hyperbolic 3-manifold infrastructure + Thurston's geometrization or Epstein–Penner convex-hull construction |
| `ConfinementSDPDuality` | confinement-sdp.lean | [boyd-vandenberghe-2004] strong duality for SDPs (Slater-strict feasibility ⇒ y₀* ≥ 0) | Mathlib SDP duality theorem (currently absent; would need a port of the cone-programming machinery) |
| `MassVolumeFactorization K n` | mass-volume-factorization.lean | mass = ρ_F · V_hyp factorisation of the categorical mass endomorphism | atom→atomic-link map + ρ_F · V_hyp gap closure (see rho-f-volume-binding-gap audit) |
| `SymmetricCrystalPairProduction n` | bar-involution-invariance.lean | conj:symmetric-crystal-pair-production (Type-B fold pair production = bar-invariance) | Brundan–Kleshchev + KLR canonical-basis bar-involution + explicit fold construction |

## Per-instance discharge analysis

### 1. `CrystalGraphRealization`

Hardest of the five.  Three independent inputs needed:

1. **Cyclotomic KLR algebra in Mathlib.**  Currently absent.  The
   Khovanov–Lauda–Rouquier algebra `R_α^Λ` would need a Mathlib
   formalisation of its diagrammatic generators + relations.

2. **Brundan–Kleshchev isomorphism.**  Theorem 1.1 of
   [brundankleshchev2009] establishes
   `H_n^Λ(R, q) ≅ R_α^Λ` as graded algebras.  The structural
   tests in `brundan_kleshchev_audit.py` (dim, Z(H_n)
   dimension, Jucys–Murphy content separation, bar-invariant
   Plancherel sum) all check empirically; a constructive proof
   in Mathlib is the discharge path.

3. **Identification with QOU LP-shadow-price filtration.**
   The conjectural QOU-specific input: the filtration on
   `H_n(R, q)` coming from the LP shadow-price ordering of
   knot-operator energies coincides on-the-nose with the KLR
   grading filtration.  Empirical evidence: every atomic knot at
   `k_max ≤ 7` is consistent (witness:
   `confinement-operator-selection.witness.json`,
   `lp-confinement-nf-forcing.witness.json`).

### 2. `HasThurstonTriangulation`

Closest to "land-in-Mathlib".  The full Thurston decomposition
theorem is decades old.  Mathlib has analytic-manifold
infrastructure but currently lacks hyperbolic 3-manifold
classification.  Likely discharge path:

- Wait for Mathlib's hyperbolic-geometry development.
- Or: provide an explicit triangulation per atomic-link
  complement.  Since `IdealTriangulation` is already a finite-
  list-of-shape-parameters structure, instantiating the class
  for a finite catalog of atomic links (figure-eight, Borromean,
  three-twist, etc.) is tractable today.

### 3. `ConfinementSDPDuality`

The standard SDP strong-duality theorem is well-known
([boyd-vandenberghe-2004] §5.3.1, §5.5.3).  Mathlib does not yet
have it.  Discharge path:

- Mathlib: port the convex-cone duality theory.
- Or: instantiate the class directly for the specific QOU SDP
  (single optimisation problem on a finite-dimensional space)
  using a hand-rolled dual-feasibility argument.

### 4. `MassVolumeFactorization`

This is the QOU paper's content claim.  Discharge requires:

- The atom→atomic-link map from
  `rem:frobenius-packing-density` made explicit.
- For each isotope, computation of `V_hyp(K)` via SnapPy.
- For each isotope, identification of `ρ_F(K)` from Type-B
  fold-orbit closure of populated Wedderburn blocks.
- Verification that ρ_F · V_hyp matches AME2020 Δ_binding to
  some declared tolerance.

The `rho_f_volume_binding_gap.py` script provides the inversion
table needed for the last bullet — currently no single primitive
matches at canonical ρ_F ∈ {m_e, 2 m_e}.

### 5. `SymmetricCrystalPairProduction`

Same upstream KLR + Brundan–Kleshchev infrastructure as
`CrystalGraphRealization`.  Once those are in Mathlib, the
bar-invariance instance follows from the KLR canonical basis's
intrinsic bar-involution.

## Cross-cutting infrastructure

The biggest single accelerator would be **Mathlib KLR + cyclotomic
Hecke**.  That single dependency unlocks 3 of the 5 instances
(CrystalGraphRealization, SymmetricCrystalPairProduction, and
indirectly MassVolumeFactorization once V_hyp/ρ_F values land).

The two SDP/Thurston instances are independent and would be
discharged separately as Mathlib develops convex-cone /
hyperbolic-geometry support.

## Status (post PR #577)

All five class instances remain `sorry`-valued by design.  The
empirical evidence for each is recorded in audit witnesses:

- `brundan-kleshchev-audit.witness.json` — 20/20 structural tests pass.
- `lp-confinement-nf-forcing.witness.json` + `confinement-operator-selection.witness.json` — KLR-grading correspondence at k_max ≤ 7.
- `rho-f-volume-binding-gap.witness.json` — ρ_F · V_hyp inversion gap analysis.
- `cross-check-trM-1ppb.witness.json` — Markov-trace consistency at 1 ppb.

Until upstream Mathlib infrastructure lands, the §3b-cond
class-conditional pattern is the right structural commitment:
each conditional theorem is `sorry`-free in its body, and the
entire stack of conjectural assumptions is auditable from a
single inventory.

## Appendix: shared-partition-module dedup (pending Mathlib)

Three particle-interactions block-Lean files
(`cpt-orbit-closure-density`, `mass-volume-factorization`,
`bar-involution-invariance`) each declare their own `Partition`
constant + `partitionTranspose`.  The duplication is intentional
(import-order independence) but should eventually consolidate.

**Target consolidation path:** once Mathlib's
`Mathlib.Combinatorics.Young.YoungDiagram` is mature, all three
files migrate to:

```lean
import Mathlib.Combinatorics.Young.YoungDiagram
namespace QOU.ParticleInteractions
abbrev Partition (n : ℕ) := YoungDiagram  -- with cardinality n
def partitionTranspose : Partition n → Partition n :=
  YoungDiagram.transpose  -- or similar Mathlib function
```

This is preferred over creating a `QOU.ParticleInteractions.PartitionShared`
intermediate module, since the Mathlib type is the long-term
target and adding an intermediate would just need to be migrated
again.  Until then, the local `constant Partition` declarations
are kept in each block file with a clarifying comment.

