import Mathlib.Tactic
import Mathlib.Data.Matrix.Basic

/-!
# QOU.QuantumObservableUniverse.fai_projector_coadjoint_orbit

Canonical Lean for content block
[`lem:fai-projector-coadjoint-orbit`](../../../quantum-observable-universe/quantum-observable-universes/fai-projector-coadjoint-orbit.md):
*Rank-1 projectors embed $\mathbb{P}(V)$ as a coadjoint orbit in
$\mathrm{Ad}(A)$*.

## Disposition (2026-07-03, bean qsb2 — restructured from a projection stub)

The previous encoding carried the entire lemma as a context-class field
(`twice_sigma_eq_id_of_projector`) and the "theorem" merely applied that
field to another field — the self-assuming projection forbidden by
AGENTS.md §3b-cond item 5.  The involution identity is **genuinely
provable**, so the class is gone and the claim is now *proved outright,
sorry-free*:

- **Formalised and proved**: for an idempotent `ρ` (`ρ * ρ = ρ`) in any
  ring, `(2ρ - 1)² = 1`.  Over a `ℚ`-algebra `2(ρ - ½·id) = 2ρ - 1`, so
  this is exactly the manuscript's involution claim
  `(2σ(ρ))² = id_V` for the traceless component
  `σ(ρ) = ρ - ½·id_V` of a projector.  The identity needs only
  idempotency, so per AGENTS.md §7c it is stated over a generic
  (noncommutative) `[Ring R]`; the 2-dimensional standard-representation
  instance is the `Matrix (Fin 2) (Fin 2) ℝ` corollary below.
- **Not formalised (narrative only)**: the second half of the `.md`
  lemma — that `σ` identifies `ℙ(V) ≅ G/T` with a *closed coadjoint
  orbit* in `Ad(A)` — is differential-geometric (orbit topology,
  `G/T` identification) and remains in the narrative proof block
  `prf:fai-projector-coadjoint-orbit`; no `sorry` is carried for it
  here.
-/

namespace QOU.QuantumObservableUniverse

/-- **Involution identity for projectors** — if `ρ` is idempotent
    (`ρ * ρ = ρ`) in a (not necessarily commutative) ring, then
    `(2ρ - 1)² = 1`.

    This is the algebraic core of
    [`lem:fai-projector-coadjoint-orbit`]: writing
    `σ(ρ) = ρ - ½·id_V` for the traceless component of a rank-1
    projector on the categorical-dimension-2 standard representation,
    `2σ(ρ) = 2ρ - 1` and the claim `(2σ(ρ))² = id_V` is exactly this
    identity.  Proof: expand `(2ρ - 1)² = 4ρ² - 4ρ + 1` (numerals are
    central, so `noncomm_ring` normalises), rewrite `ρ² = ρ`, and the
    linear terms cancel. -/
theorem twice_sigma_sq_eq_one {R : Type*} [Ring R] {ρ : R}
    (hρ : ρ * ρ = ρ) : (2 * ρ - 1) ^ 2 = 1 := by
  have h : (2 * ρ - 1) ^ 2 = 4 * (ρ * ρ) - 4 * ρ + 1 := by noncomm_ring
  rw [h, hρ]
  noncomm_ring

/-- **Lemma** ([`lem:fai-projector-coadjoint-orbit`], involution part) —
    resolving declaration for the `lean.ref` URI
    `qou:QOU.QuantumObservableUniverse.fai_projector_coadjoint_orbit`.

    For any idempotent `ρ` in a ring, `(2ρ - 1)² = 1`: the doubled
    traceless component of a projector is an involution.  Proved
    sorry-free via `twice_sigma_sq_eq_one`; the coadjoint-orbit
    identification `ℙ(V) ≅ G/T` of the `.md` statement is narrative
    (see module docstring). -/
theorem fai_projector_coadjoint_orbit {R : Type*} [Ring R] {ρ : R}
    (hρ : ρ * ρ = ρ) : (2 * ρ - 1) ^ 2 = 1 :=
  twice_sigma_sq_eq_one hρ

/-- The concrete 2-dimensional instance: a projector `ρ` on the
    standard representation `V ≅ ℝ²` (as a `2 × 2` real matrix)
    satisfies `(2ρ - 1)² = 1`, where `1` is the identity matrix
    `id_V`.  Immediate from the generic ring statement. -/
theorem fai_projector_coadjoint_orbit_matrix
    (ρ : Matrix (Fin 2) (Fin 2) ℝ) (hρ : ρ * ρ = ρ) :
    (2 * ρ - 1) ^ 2 = 1 :=
  fai_projector_coadjoint_orbit hρ

end QOU.QuantumObservableUniverse
