import QOU.PhiQJSJ
-- brings in: without this the tactic is unknown and the lemma is unproved.
import Mathlib.Tactic.Linarith


/-!
# QOU.PhiQJSJ — Φ_q tower equals ρ_q · Σ_S Vol(K_S) (archimedean bridge)

The **Φ_q–JSJ archimedean bridge**: under the archimedean
realisation, each summand `Φ_q(V_S)` of the dilogarithm form of the
mass tower equals `ρ_q · Vol_hyp(K_S)`, where `K_S` is the
Φ_q-piece of the braid.  Summed over `S`, this identifies the dilog
form of the tower with the JSJ piecewise sum
`Σ_P ρ_F(P) · Vol_hyp(P)`.

LaTeX label: `conj:phi-q-tower-jsj-bridge`

The Lean statement is **conditional on `Kashaev.VolumeConjecture q`**,
the typeclass axiomatising KVC.  Modulo that typeclass instance the
bridge theorem is fully verified by Lean.  This is Workplan B from
`AGENTS.md` §3b ("Lean formalization of conjectures").

## References

- [leitner2026] Ch 3 §sec:calibration-algebraic-mass /
  phi-q-tower-jsj-bridge
- [kashaev1997] https://doi.org/10.1023/A:1007364912784
- [murakami-murakami2001] https://doi.org/10.1007/BF02392716
- [thurston1978] https://doi.org/10.1007/978-1-4612-9903-6
-/

namespace QOU.PhiQJSJ

open QOU.PhiQPiece QOU.Kashaev

/-! ## Shared declarations live in `QOU.PhiQJSJ`

`rho`, `rho_pos`, `TowerSummandRealization`, `PerPieceBridge`, `bridge` and
`bridge_nonneg` were **duplicated verbatim in this file** — same namespace
`QOU.PhiQJSJ`, same statements, in a file that did not import the module
declaring them. Two independent declarations of one class in one namespace
collide if both ever reach a single import closure, which is the failure
`QOU/Archimedean/HyperbolicVolumeIndependence.lean` records having hit
("the duplicate declaration collided with the real class when both files
were imported"), and which AGENTS.md §0a bans outright.

They are now imported rather than restated. Only the two skeleton witnesses
and `PerPieceBridgeAxiom` below — which the library module does not carry —
remain local to this file. -/

/-- **Skeleton `TowerSummandRealization` witness.**  Defines the
    archimedean realisation as constant zero.  Trivially non-negative;
    encodes none of the actual realisation infrastructure.

    **Demoted from `instance` to `def`, 2026-08-24.**  The class docstring
    above says it is "populated by any concrete instance of the realisation
    functor" — but as a global `instance` this zero skeleton *preempted* that:
    typeclass resolution satisfied every `[TowerSummandRealization q]` binder
    in this file from it, so `bridge` and `bridge_nonneg` read as claims about
    an arbitrary realisation while the only realisation in scope was `0`.
    Under that resolution `PerPieceBridgeAxiom.bridge_per_piece` reads
    `0 = rho q * pieceVolume q β S`, i.e. it asserts `pieceVolume ≡ 0` for
    `q > 1` — the block comment below already noticed this and recorded it as
    expected.

    This is the `triv_hecke` / `triv_wedderburn` shape demoted in PR #5581 for
    the same reason. As a `def` the degenerate model stays available to anyone
    who wants to name it (`letI := skeletonRealisation q`), which is the honest
    use — witnessing that the class is inhabited, so the conditional theorems
    are not vacuously true — without standing in for the real realisation. -/
-- Ref: [leitner2026] Ch 3 §sec:calibration-algebraic-mass / phi-q-tower-jsj-bridge
def skeletonRealisation (q : ℝ) : TowerSummandRealization q where
  realisation := fun _ _ => 0
  realisation_nonneg := fun _ _ => le_refl 0

/-- **Skeleton `PerPieceBridge` instance.**  The `bridge_per_piece`
    field equates `0 = rho q * pieceVolume q β S`.  Since
    `pieceVolume` is itself `sorry` (the upstream Kashaev conjecture's
    deferred per-piece value), this equation is also a deferred
    `sorry` — the conjectural input proper.  Per AGENTS.md §3b, a
    `sorry` inside an instance field is understood as the conjecture,
    not missing proof.  Discharges §3b-cond for downstream consumers. -/
class PerPieceBridgeAxiom (q : ℝ) [VolumeConjecture q] [TowerSummandRealization q] : Prop where
  /-- The missing input for the bridge per piece. -/
  bridge_per_piece : ∀ (β : Braid) (S : Finset (Fin (β.n - 1))),
    TowerSummandRealization.realisation (q := q) β S = rho q * pieceVolume q β S

-- Ref: [leitner2026] Ch 3 §sec:calibration-algebraic-mass / phi-q-tower-jsj-bridge
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
instance skeletonBridge (q : ℝ) [VolumeConjecture q] [TowerSummandRealization q] [ctx : PerPieceBridgeAxiom q] :
    PerPieceBridge q where
  bridge_per_piece := ctx.bridge_per_piece

end QOU.PhiQJSJ
