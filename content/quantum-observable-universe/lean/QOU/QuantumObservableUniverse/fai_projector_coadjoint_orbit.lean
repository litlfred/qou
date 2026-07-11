import Mathlib.Tactic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Spectrum

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
- **Proved sorry-free (2026-07-11)**: the second half of the `.md`
  lemma — that `σ` identifies `ℙ(V) ≅ G/T` with a *closed coadjoint
  orbit* in `Ad(A)` — is proved at the archimedean matrix level as
  `fai_projector_coadjoint_orbit_orbit`: the traceless component `σ(ρ)`
  of every rank-1 projector (Hermitian idempotent of trace 1) on
  `τ(V) = ℂ²` is unitarily conjugate to the single base point
  `σ₀ = ½·diag(1, −1)`, so the `σ`-image of `ℙ(V)` is one
  `U(2)`-adjoint orbit.  The proof runs Mathlib's spectral theorem
  (`Matrix.IsHermitian.spectral_theorem`) and pins the two eigenvalues
  via the proved char-poly invariants `fai_projector_sigma_trace`
  (`tr σ = 0`) and `fai_projector_sigma_det` (`det σ = −¼`); the
  eigenvalue ordering is resolved by a `u = U` / `u = U·swap` case
  split.  The full differential-geometric content (orbit topology, the
  `G/T` identification as a *smooth* homogeneous space) remains in the
  narrative proof block `prf:fai-projector-coadjoint-orbit`.
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
    that pin the coadjoint orbit.)

    Purely algebraic (no archimedean structure), so per AGENTS.md §7c it
    is stated over a generic `[CommRing R]`; the `ℂ` orbit lives in the
    `_orbit` corollary below. -/
theorem fai_projector_det_eq_zero {R : Type*} [CommRing R]
    (ρ : Matrix (Fin 2) (Fin 2) R) (hidem : ρ * ρ = ρ) (htr : ρ.trace = 1) :
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

/-- Helper: a scalar multiple of the identity is the constant diagonal
    matrix, `c • 1 = diagonal (fun _ => c)`.  Used to split `σ(ρ)` through
    the spectral decomposition of `ρ`. -/
theorem smul_one_diag (c : ℂ) :
    c • (1 : Matrix (Fin 2) (Fin 2) ℂ) = Matrix.diagonal (fun _ => c) := by
  ext i j; by_cases h : i = j <;> simp [h]

/-- **Orbit invariant — trace of the traceless component.**  For any
    rank-1 projector `ρ` (`tr ρ = 1`), the traceless component
    `σ(ρ) = ρ − ½·id` has `tr σ(ρ) = 0` — it lands in `Ad(A) = 𝔰𝔲(2)`
    (the traceless Hermitian matrices), as the manuscript's `σ` requires.
    Matches `tr σ₀ = 0`.

    The `½` needs `2` invertible, so per §7c this is stated over a generic
    characteristic-zero field `[Field R] [CharZero R]` (the natural setting
    for `σ(ρ) ∈ 𝔰𝔲(2)`); `_orbit` specialises it to `ℂ`. -/
theorem fai_projector_sigma_trace {R : Type*} [Field R] [CharZero R]
    (ρ : Matrix (Fin 2) (Fin 2) R) (htr : ρ.trace = 1) :
    (ρ - (2 : R)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) R)).trace = 0 := by
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
    conjugacy step below.

    Stated over a generic characteristic-zero field per §7c (the `½`, `¼`
    need `2` invertible); `_orbit` specialises it to `ℂ`. -/
theorem fai_projector_sigma_det {R : Type*} [Field R] [CharZero R]
    (ρ : Matrix (Fin 2) (Fin 2) R) (hidem : ρ * ρ = ρ) (htr : ρ.trace = 1) :
    (ρ - (2 : R)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) R)).det = -(4 : R)⁻¹ := by
  have hdet0 : ρ.det = 0 := fai_projector_det_eq_zero ρ hidem htr
  have htr' : ρ 0 0 + ρ 1 1 = 1 := by
    simpa [Matrix.trace, Matrix.diag, Fin.sum_univ_two] using htr
  have hdet' : ρ 0 0 * ρ 1 1 - ρ 0 1 * ρ 1 0 = 0 := by
    rw [Matrix.det_fin_two] at hdet0; exact hdet0
  rw [Matrix.det_fin_two]
  simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply,
    smul_eq_mul]
  norm_num
  linear_combination hdet' - (2 : R)⁻¹ * htr'

/-- **Lemma** ([`lem:fai-projector-coadjoint-orbit`], coadjoint-orbit
    half) — **proved sorry-free**.

    The traceless component `σ(ρ) = ρ − ½·id_V` of every rank-1
    projector on the categorical-dimension-2 standard representation —
    archimedean realisation: a Hermitian idempotent of trace 1 on
    `τ(V) = ℂ²` — is unitarily conjugate to the single base point
    `σ₀ = ½·diag(1, −1)`.  Hence the `σ`-image of `ℙ(V)` is one
    `U(2)`-adjoint orbit, and `σ` identifies
    `ℙ(V) ≅ G/T = U(2)/(U(1) × U(1))` with a closed coadjoint orbit in
    `Ad(A)` (the `.md` lemma's second half).

    Proof (spectral theorem, no `sorry`).  By `Matrix.IsHermitian.spectral_theorem`,
    `ρ = U · diagonal(eigenvalues) · U⋆` with `U` unitary, so
    `σ(ρ) = U · diagonal(μ) · U⋆` for `μ = eigenvalues − ½` (using
    `U U⋆ = 1`).  Conjugation preserves trace and determinant, so the two
    proved invariants `fai_projector_sigma_trace` (`tr σ(ρ) = 0`) and
    `fai_projector_sigma_det` (`det σ(ρ) = −¼`) give `μ₀ + μ₁ = 0` and
    `μ₀ μ₁ = −¼`; hence `{μ₀, μ₁} = {½, −½}`.  In the case `μ = (½, −½)`,
    `diagonal μ = σ₀` and `u = U`; in the case `μ = (−½, ½)`,
    `diagonal μ = P σ₀ P` for the swap permutation `P = !![0,1;1,0]`
    (unitary), and `u = U · P`.  Either way `σ(ρ) = u · σ₀ · star u`. -/
-- Formalised via Mathlib `Matrix.IsHermitian.spectral_theorem` (no `sorry`).
theorem fai_projector_coadjoint_orbit_orbit
    (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hidem : ρ * ρ = ρ)
    (hherm : ρ.conjTranspose = ρ) (htr : ρ.trace = 1) :
    ∃ u ∈ Matrix.unitaryGroup (Fin 2) ℂ,
      ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)
        = u * sigmaBasePoint * star u := by
  -- The two coadjoint-orbit invariants (proved above).
  have htr0 : (ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)).trace = 0 :=
    fai_projector_sigma_trace ρ htr
  have hdet : (ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)).det = -(4 : ℂ)⁻¹ :=
    fai_projector_sigma_det ρ hidem htr
  -- Spectral decomposition of the Hermitian `ρ`.
  have hH : ρ.IsHermitian := hherm
  have hspec := hH.spectral_theorem
  set Um : Matrix (Fin 2) (Fin 2) ℂ := ↑hH.eigenvectorUnitary with hUm
  set ev : Fin 2 → ℂ := RCLike.ofReal ∘ hH.eigenvalues with hev
  have hUsU : star Um * Um = 1 := Matrix.UnitaryGroup.star_mul_self _
  have hUUs : Um * star Um = 1 := hH.eigenvectorUnitary.2.2
  set μ : Fin 2 → ℂ := fun i => ev i - (2 : ℂ)⁻¹ with hμ
  -- σ(ρ) = Um · diagonal μ · star Um.
  have hσ : ρ - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)
      = Um * Matrix.diagonal μ * star Um := by
    have hdm : Matrix.diagonal μ
        = Matrix.diagonal ev - (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
      rw [smul_one_diag, Matrix.diagonal_sub]
    rw [hdm, Matrix.mul_sub, Matrix.sub_mul, ← hspec,
        show Um * ((2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ)) * star Um
              = (2 : ℂ)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) ℂ) from by
          rw [Matrix.mul_smul, Matrix.smul_mul, mul_one, hUUs]]
  -- Trace and determinant of `diagonal μ` (conjugation-invariant).
  have hsum : μ 0 + μ 1 = 0 := by
    have h : (Matrix.diagonal μ).trace = 0 := by
      have h2 := htr0
      rw [hσ, Matrix.trace_mul_cycle, hUsU, Matrix.one_mul] at h2; exact h2
    rwa [Matrix.trace_diagonal, Fin.sum_univ_two] at h
  have hprod : μ 0 * μ 1 = -(4 : ℂ)⁻¹ := by
    have h : (Matrix.diagonal μ).det = -(4 : ℂ)⁻¹ := by
      have h2 := hdet
      rw [hσ, Matrix.det_mul, Matrix.det_mul,
          show Um.det * (Matrix.diagonal μ).det * (star Um).det
                = (Matrix.diagonal μ).det * (Um.det * (star Um).det) from by ring,
          ← Matrix.det_mul, hUUs, Matrix.det_one, mul_one] at h2
      exact h2
    rwa [Matrix.det_diagonal, Fin.prod_univ_two] at h
  -- `{μ₀, μ₁} = {½, −½}`.
  have h0 : μ 0 = - μ 1 := by linear_combination hsum
  have hsq : (μ 1 - (2 : ℂ)⁻¹) * (μ 1 + (2 : ℂ)⁻¹) = 0 := by
    have h := hprod; rw [h0] at h; linear_combination -h
  -- The swap permutation `P` is unitary and self-adjoint.
  have hstarP : star (!![0, 1; 1, 0] : Matrix (Fin 2) (Fin 2) ℂ) = !![0, 1; 1, 0] := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.star_apply]
  have hP : (!![0, 1; 1, 0] : Matrix (Fin 2) (Fin 2) ℂ)
      ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, hstarP]
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two]
  rcases mul_eq_zero.mp hsq with h | h
  · -- μ = (−½, ½): `diagonal μ = P σ₀ P`, `u = Um · P`.
    have hμ1 : μ 1 = (2 : ℂ)⁻¹ := by linear_combination h
    have hμ0 : μ 0 = -(2 : ℂ)⁻¹ := by rw [h0, hμ1]
    refine ⟨Um * !![0, 1; 1, 0], Submonoid.mul_mem _ hH.eigenvectorUnitary.2 hP, ?_⟩
    have hσ0' : sigmaBasePoint = !![(2 : ℂ)⁻¹, 0; 0, -(2 : ℂ)⁻¹] := by
      ext i j; fin_cases i <;> fin_cases j <;> simp [sigmaBasePoint]
    have hconj : Matrix.diagonal μ
        = (!![0, 1; 1, 0] : Matrix (Fin 2) (Fin 2) ℂ) * sigmaBasePoint * !![0, 1; 1, 0] := by
      rw [hσ0']
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [Matrix.mul_apply, Fin.sum_univ_two, hμ0, hμ1,
              Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons]
    rw [hσ, hconj, Matrix.star_mul, hstarP]
    simp only [Matrix.mul_assoc]
  · -- μ = (½, −½): `diagonal μ = σ₀`, `u = Um`.
    have hμ1 : μ 1 = -(2 : ℂ)⁻¹ := by linear_combination h
    have hμ0 : μ 0 = (2 : ℂ)⁻¹ := by rw [h0, hμ1]; ring
    refine ⟨Um, hH.eigenvectorUnitary.2, ?_⟩
    have hdσ : Matrix.diagonal μ = sigmaBasePoint := by
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [sigmaBasePoint, hμ0, hμ1]
    rw [hσ, hdσ]

end QOU.QuantumObservableUniverse
