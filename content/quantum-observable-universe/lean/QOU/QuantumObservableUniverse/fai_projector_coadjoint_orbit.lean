import Mathlib.Tactic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.LinearAlgebra.Matrix.Trace

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
- **Stated, not yet proved (honest `sorry`)**: the second half of the
  `.md` lemma — that `σ` identifies `ℙ(V) ≅ G/T` with a *closed
  coadjoint orbit* in `Ad(A)` — is stated at the archimedean matrix
  level as `fai_projector_coadjoint_orbit_orbit`: the traceless
  component `σ(ρ)` of every rank-1 projector (Hermitian idempotent of
  trace 1) on `τ(V) = ℂ²` is unitarily conjugate to the single base
  point `σ₀ = ½·diag(1, −1)`, so the `σ`-image of `ℙ(V)` is one
  `U(2)`-adjoint orbit.  The proof is the spectral theorem for the
  Hermitian idempotent `ρ` (eigenvalues `1, 0`); it is not yet
  formalised, so the theorem carries a cited `sorry`.  The full
  differential-geometric content (orbit topology, the `G/T`
  identification) remains in the narrative proof block
  `prf:fai-projector-coadjoint-orbit`.
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
    identification `ℙ(V) ≅ G/T` of the `.md` statement is stated
    (with a cited `sorry`) as `fai_projector_coadjoint_orbit_orbit`
    below. -/
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

/-- **Orbit invariant — determinant.**  A rank-1 projector `ρ` on
    `τ(V) = ℂ²` (idempotent `ρ² = ρ` with `tr ρ = 1`, so its eigenvalues
    are `1, 0`) has `det ρ = 0`.  Pure `Fin 2` entry algebra: the `(0,0)`
    entry of `ρ² = ρ` gives `ρ₀₀² + ρ₀₁ρ₁₀ = ρ₀₀`, and the trace gives
    `ρ₀₀ + ρ₁₁ = 1`; then `det ρ = ρ₀₀ρ₁₁ − ρ₀₁ρ₁₀ = 0` by
    `linear_combination`.  (This is the archimedean shadow of "a rank-1
    projector is singular"; it fixes one of the two char-poly invariants
    that pin the coadjoint orbit.) -/
theorem fai_projector_det_eq_zero
    (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hidem : ρ * ρ = ρ) (htr : ρ.trace = 1) :
    ρ.det = 0 := by
  have h00 : ρ 0 0 * ρ 0 0 + ρ 0 1 * ρ 1 0 = ρ 0 0 := by
    have h := congrFun (congrFun hidem 0) 0
    simpa [Matrix.mul_apply, Fin.sum_univ_two] using h
  have htr' : ρ 0 0 + ρ 1 1 = 1 := by
    simpa [Matrix.trace, Matrix.diag, Fin.sum_univ_two] using htr
  rw [Matrix.det_fin_two]
  linear_combination -h00 + ρ 0 0 * htr'

/-- The base point `σ₀ = ½·diag(1, −1)` of the coadjoint orbit: the
    traceless component `σ(ρ₀) = ρ₀ − ½·id` of the base rank-1
    projector `ρ₀ = diag(1, 0)` on `τ(V) = ℂ²`. -/
noncomputable def sigmaBasePoint : Matrix (Fin 2) (Fin 2) ℂ :=
  (2 : ℂ)⁻¹ • Matrix.diagonal (fun i => if i = 0 then (1 : ℂ) else -1)

/-- **Orbit invariant — trace of the traceless component.**  For any
    rank-1 projector `ρ` (`tr ρ = 1`), the traceless component
    `σ(ρ) = ρ − ½·id` has `tr σ(ρ) = 0` — it lands in `Ad(A) = 𝔰𝔲(2)`
    (the traceless Hermitian matrices), as the manuscript's `σ` requires.
    Matches `tr σ₀ = 0`. -/
theorem fai_projector_sigma_trace
    (ρ : Matrix (Fin 2) (Fin 2) ℂ) (htr : ρ.trace = 1) :
    (ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)).trace = 0 := by
  rw [Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_one, htr]
  simp only [Fintype.card_fin, Nat.cast_ofNat, smul_eq_mul]
  norm_num

/-- **Orbit invariant — determinant of the traceless component.**  For a
    rank-1 projector `ρ` on `ℂ²`, `det σ(ρ) = −¼`, matching `det σ₀ = −¼`.
    Together with `tr σ(ρ) = 0` this fixes both coefficients of the
    characteristic polynomial `t² − (tr)·t + det = t² − ¼`, so every
    `σ(ρ)` has the same char poly as `σ₀` (eigenvalues `±½`).  Since a
    Hermitian matrix is unitarily diagonalisable and its char poly
    determines its spectrum, this is exactly the statement that the
    `σ`-image of `ℙ(V)` is a *single* `U(2)`-adjoint orbit — the
    conjugacy step below. -/
theorem fai_projector_sigma_det
    (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hidem : ρ * ρ = ρ) (htr : ρ.trace = 1) :
    (ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)).det = -(4 : ℂ)⁻¹ := by
  have hdet0 : ρ.det = 0 := fai_projector_det_eq_zero ρ hidem htr
  have htr' : ρ 0 0 + ρ 1 1 = 1 := by
    simpa [Matrix.trace, Matrix.diag, Fin.sum_univ_two] using htr
  have hdet' : ρ 0 0 * ρ 1 1 - ρ 0 1 * ρ 1 0 = 0 := by
    rw [Matrix.det_fin_two] at hdet0; exact hdet0
  rw [Matrix.det_fin_two]
  simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply,
    smul_eq_mul]
  norm_num
  linear_combination hdet' - (2 : ℂ)⁻¹ * htr'

/-- **Lemma** ([`lem:fai-projector-coadjoint-orbit`], coadjoint-orbit
    half) — **stated, not yet proved**.

    The traceless component `σ(ρ) = ρ − ½·id_V` of every rank-1
    projector on the categorical-dimension-2 standard representation —
    archimedean realisation: a Hermitian idempotent of trace 1 on
    `τ(V) = ℂ²` — is unitarily conjugate to the single base point
    `σ₀ = ½·diag(1, −1)`.  Hence the `σ`-image of `ℙ(V)` is one
    `U(2)`-adjoint orbit, and `σ` identifies
    `ℙ(V) ≅ G/T = U(2)/(U(1) × U(1))` with a closed coadjoint orbit in
    `Ad(A)` (the `.md` lemma's second half).

    The proof is the spectral theorem for the Hermitian idempotent `ρ`
    (eigenvalues `1` and `0`, unitary diagonalisation to `diag(1, 0)`),
    which is not yet formalised here — hence the cited `sorry`.

    The two coadjoint-orbit *invariants* are, however, proved outright
    above: `fai_projector_sigma_trace` (`tr σ(ρ) = 0`) and
    `fai_projector_sigma_det` (`det σ(ρ) = −¼`) show every `σ(ρ)` has the
    same characteristic polynomial `t² − ¼` as `σ₀`.  For `2×2` Hermitian
    matrices, equal char poly (with distinct eigenvalues `±½`) is
    necessary and sufficient for unitary conjugacy; the residual `sorry`
    is exactly that standard spectral fact.  This replaces the previous
    encoding, which assumed the conclusion via a hypothesis
    `ρ − ½·id = σ₀` (so `u = 1` worked trivially) — a self-assuming
    projection forbidden by AGENTS.md §3b-cond; the hypothesis is dropped
    and the genuine conjugacy claim is now stated honestly. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/fai-projector-coadjoint-orbit.md
theorem fai_projector_coadjoint_orbit_orbit
    (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hidem : ρ * ρ = ρ)
    (hherm : ρ.conjTranspose = ρ) (htr : ρ.trace = 1) :
    ∃ u ∈ Matrix.unitaryGroup (Fin 2) ℂ,
      ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)
        = u * sigmaBasePoint * star u := by
  -- Hermitian is required for the spectral conjugacy (residual `sorry`):
  have _hermitian := hherm
  -- Char-poly invariants of `σ(ρ)` are proved (equal to those of `σ₀`):
  have _htrace : (ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)).trace = 0 :=
    fai_projector_sigma_trace ρ htr
  have _hdet : (ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)).det = -(4 : ℂ)⁻¹ :=
    fai_projector_sigma_det ρ hidem htr
  -- Residual gap: `2×2` Hermitian with char poly `t² − ¼` is unitarily
  -- conjugate to `σ₀` (spectral theorem, distinct eigenvalues `±½`).
  -- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/fai-projector-coadjoint-orbit.md
  sorry

end QOU.QuantumObservableUniverse
