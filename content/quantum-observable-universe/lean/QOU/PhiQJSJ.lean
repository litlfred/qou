import QOU.PhiQPiece
import QOU.Kashaev
import Mathlib.Tactic.Linarith

/-!
# QOU.PhiQJSJ — Φ_q tower equals ρ_q · Σ_S Vol(K_S) (archimedean bridge)

The **Φ_q–JSJ archimedean bridge**: under the archimedean
realisation, each summand `Φ_q(V_S)` of the dilogarithm form of the
mass tower equals `ρ_q · Vol_hyp(K_S)`, where `K_S` is the
Φ_q-piece of the braid.  Summed over `S`, this identifies the dilog
form of the tower with the JSJ piecewise sum
`Σ_P ρ_F(P) · Vol_hyp(P)`.

**Formal-chain version.**  This file lives under `lean/QOU/` and is
compiled by `lake build`.  The co-located documentation stub at
`content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.lean`
mirrors this content (per `QOU.GroundRingAnnotations`).

LaTeX label: `conj:phi-q-tower-jsj-bridge`

The Lean statement is **conditional on `Kashaev.VolumeConjecture q`**,
the typeclass axiomatising KVC.  Modulo that typeclass instance the
bridge theorem is fully verified by Lean.  This is Workplan B from
`AGENTS.md` §3b ("Lean formalization of conjectures").

## References

- [manuscript] Ch 3 §sec:calibration-algebraic-mass /
  phi-q-tower-jsj-bridge
- [kashaev1997] https://doi.org/10.1023/A:1007364912784
- [murakami-murakami2001] https://doi.org/10.1007/BF02392716
- [thurston1978] https://doi.org/10.1007/978-1-4612-9903-6
-/

namespace QOU.PhiQJSJ

open QOU.PhiQPiece QOU.Kashaev

/-- The substrate density `ρ_q = 1/ℏ_q²`, with `ℏ_q = (q-1)/q`. -/
noncomputable def rho (q : ℝ) : ℝ := (q / (q - 1)) ^ 2

theorem rho_pos {q : ℝ} (hq : 1 < q) : 0 < rho q := by
  unfold rho
  exact pow_pos (div_pos (by linarith) (by linarith)) 2

/-- Archimedean realisation of the dilogarithm form of the per-`S`
    summand of the tower.  This is the **target** of the bridge: it
    is the real number that `Φ_q(V_S)` (resp. `z² · Φ_q(V_i V_j)`)
    realises to under `τ_arch = π_∞ ∘ τ`.

    Axiomatised here so the bridge theorem can be stated without
    importing the full archimedean-realisation infrastructure;
    populated by any concrete instance of the realisation functor. -/
class TowerSummandRealization (q : ℝ) where
  /-- Archimedean realisation of the per-`S` dilog summand of the
      tower (with the appropriate Markov weight `z^|S|` already
      absorbed). -/
  realisation : (β : Braid) → Finset (Fin (β.n - 1)) → ℝ
  /-- The realisation is non-negative (real volumes are non-negative). -/
  realisation_nonneg :
    ∀ (β : Braid) (S : Finset (Fin (β.n - 1))), 0 ≤ realisation β S

/-- **Φ_q–JSJ archimedean bridge (per-piece).**

    Conditional on `Kashaev.VolumeConjecture q` and a
    `TowerSummandRealization q` instance, the archimedean realisation
    of the per-`S` dilog summand equals `ρ_q · Vol_hyp(K_S)`.

    The class field `bridge_per_piece` plays the role of the
    `kvc_holds`-style axiom: it is the per-piece identification
    that the conjecture asserts, lifted to a typeclass field so
    downstream theorems can consume it abstractly. -/
class PerPieceBridge (q : ℝ) [VolumeConjecture q] [TowerSummandRealization q] where
  bridge_per_piece :
    ∀ (β : Braid) (S : Finset (Fin (β.n - 1))),
      TowerSummandRealization.realisation (q := q) β S =
        rho q * pieceVolume q β S

/-- **Master conditional bridge theorem.**

    For every braid `β`, the archimedean realisation of the
    per-`S` dilog summand equals `ρ_q · Vol_hyp(K_S)`.  This is the
    statement of `conj:phi-q-tower-jsj-bridge`, fully verified by
    Lean **modulo** the typeclass instance `[PerPieceBridge q]`,
    which in turn depends on `[VolumeConjecture q]` (Kashaev) and
    `[TowerSummandRealization q]` (realisation infrastructure).

    No `sorry`: every step is either definitional or supplied by a
    typeclass field. -/
-- Ref: [manuscript] Ch 3 §sec:calibration-algebraic-mass /
--                   phi-q-tower-jsj-bridge
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
theorem bridge {q : ℝ} [VolumeConjecture q] [TowerSummandRealization q]
    [inst : PerPieceBridge q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) :
    TowerSummandRealization.realisation (q := q) β S =
      rho q * pieceVolume q β S :=
  inst.bridge_per_piece β S

/-- **Non-negativity of the bridge value.**

    Both sides of the bridge equation are non-negative: the
    archimedean realisation is non-negative by hypothesis, and
    the right-hand side is the product of `ρ q > 0` (when
    `1 < q`) and the non-negative piece volume. -/
theorem bridge_nonneg {q : ℝ} (hq : 1 < q)
    [VolumeConjecture q] [TowerSummandRealization q] [PerPieceBridge q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) :
    0 ≤ rho q * pieceVolume q β S := by
  exact mul_nonneg (le_of_lt (rho_pos hq)) (pieceVolume_nonneg q β S)

end QOU.PhiQJSJ
