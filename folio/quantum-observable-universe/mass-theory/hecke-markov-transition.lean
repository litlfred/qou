import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.GroupWithZero.Finset
import Mathlib.Data.Fintype.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring


/-!
# QOU.Braiding.HeckeMarkovTransition — Hecke generator as stochastic transition

The spectral idempotents of the Hecke generator T_i decompose
each crossing into symmetric (eigenvalue q) and antisymmetric
(eigenvalue −q⁻¹) channels.  Normalising the eigenvalues to
probabilities gives p₊ = q/(q + q⁻¹), p₋ = q⁻¹/(q + q⁻¹),
with p₊ + p₋ = 1 and p₊/p₋ = q².

The Markov trace property tr_M(x T_n) = z · tr_M(x) is then
memorylessness: the transition at generator n depends only on the
crossing type at σ_n, not on the history x ∈ H_{n−1}(q).

LaTeX label: `prop:hecke-markov-transition`

## References

- [diaconis-ram2000] https://doi.org/10.1307/mmj/1030132713
- [jones1987] https://doi.org/10.2307/1971403
- [bufetov2020] https://arxiv.org/abs/2003.02730
-/

namespace QOU.Braiding

/-! ## Part (i): Spectral idempotents -/

/-- Spectral idempotent data for a single Hecke generator T_i.

    Given the quadratic relation (T_i − q)(T_i + q⁻¹) = 0, the two
    eigenvalues are λ₊ = q and λ₋ = −q⁻¹.  The spectral projectors are:

      e₊ = (T_i + q⁻¹) / (q + q⁻¹)     (projects onto the q-eigenspace)
      e₋ = (q − T_i) / (q + q⁻¹)        (projects onto the −q⁻¹-eigenspace)

    We work at the level of eigenvalues (scalars), which suffices for
    the transition probability computation. -/
-- Ref: [diaconis-ram2000] Diaconis & Ram, "Analysis of systematic scan Metropolis algorithms using Iwahori-Hecke algebra techniques," Ann. Appl. Probab. 12 (2000), arXiv:math/0401318
structure SpectralIdempotentData where
  /-- Deformation parameter q. -/
  q : ℝ
  /-- q > 0. -/
  q_pos : 0 < q
  /-- q ≠ 1 (non-classical). -/
  q_ne_one : q ≠ 1

/-- The spectral gap q + q⁻¹. -/
noncomputable def SpectralIdempotentData.gap (d : SpectralIdempotentData) : ℝ :=
  d.q + d.q⁻¹

/-- The spectral gap is positive. -/
theorem SpectralIdempotentData.gap_pos (d : SpectralIdempotentData) :
    0 < d.gap := by
  unfold gap
  have hq : 0 < d.q := d.q_pos
  have : 0 < d.q⁻¹ := inv_pos.mpr d.q_pos
  linarith

/-- The spectral gap is nonzero. -/
theorem SpectralIdempotentData.gap_ne_zero (d : SpectralIdempotentData) :
    d.gap ≠ 0 :=
  ne_of_gt d.gap_pos

/-! ## Part (ii): Transition probabilities -/

/-- The symmetric (q-eigenvalue) transition probability:
    p₊ = q / (q + q⁻¹) = q² / (q² + 1). -/
noncomputable def SpectralIdempotentData.p_plus (d : SpectralIdempotentData) : ℝ :=
  d.q / d.gap

/-- The antisymmetric (−q⁻¹-eigenvalue) transition probability:
    p₋ = q⁻¹ / (q + q⁻¹) = 1 / (q² + 1). -/
noncomputable def SpectralIdempotentData.p_minus (d : SpectralIdempotentData) : ℝ :=
  d.q⁻¹ / d.gap

/-- **p₊ + p₋ = 1**: the transition probabilities form a probability
    distribution.  This is the normalisation of eigenvalues to a
    stochastic operator. -/
-- Ref: [diaconis-ram2000] Diaconis & Ram, "Analysis of systematic scan Metropolis algorithms using Iwahori-Hecke algebra techniques," Ann. Appl. Probab. 12 (2000), arXiv:math/0401318
theorem SpectralIdempotentData.prob_sum_one (d : SpectralIdempotentData) :
    d.p_plus + d.p_minus = 1 := by
  unfold p_plus p_minus gap
  rw [← add_div]
  exact div_self d.gap_ne_zero

/-- p₊ > 0. -/
theorem SpectralIdempotentData.p_plus_pos (d : SpectralIdempotentData) :
    0 < d.p_plus := by
  unfold p_plus
  exact div_pos d.q_pos d.gap_pos

/-- p₋ > 0. -/
theorem SpectralIdempotentData.p_minus_pos (d : SpectralIdempotentData) :
    0 < d.p_minus := by
  unfold p_minus
  exact div_pos (inv_pos.mpr d.q_pos) d.gap_pos

/-- **Boltzmann ratio**: p₊/p₋ = q².

    The ratio of transition probabilities equals q², the Boltzmann
    weight for a single crossing.  Note that `K_i = p₊·id + p₋·s_i` is
    doubly stochastic (`s_i` is a permutation matrix), so its stationary law
    is the uniform measure, not the Mallows measure: q² here is a one-step
    ratio, not the fugacity of a stationary distribution. -/
-- Ref: [diaconis-ram2000] Diaconis & Ram, "Analysis of systematic scan Metropolis algorithms using Iwahori-Hecke algebra techniques," Ann. Appl. Probab. 12 (2000), arXiv:math/0401318
theorem SpectralIdempotentData.boltzmann_ratio (d : SpectralIdempotentData) :
    d.p_plus / d.p_minus = d.q ^ 2 := by
  unfold p_plus p_minus
  have hq : d.q ≠ 0 := ne_of_gt d.q_pos
  have hgap : d.gap ≠ 0 := d.gap_ne_zero
  field_simp

/-- p₊ > p₋ when q > 1 (the symmetric channel is favoured). -/
theorem SpectralIdempotentData.p_plus_gt_p_minus
    (d : SpectralIdempotentData) (hq : d.q > 1) :
    d.p_plus > d.p_minus := by
  unfold p_plus p_minus
  apply div_lt_div_of_pos_right _ d.gap_pos
  exact lt_of_lt_of_le (inv_lt_one_of_one_lt₀ hq) (le_of_lt hq)

/-- p₊ = p₋ = 1/2 at q = 1 would give the classical fair walk.
    Here we record the identity: at any q, p₊ − p₋ = (q − q⁻¹)/(q + q⁻¹). -/
theorem SpectralIdempotentData.bias (d : SpectralIdempotentData) :
    d.p_plus - d.p_minus = (d.q - d.q⁻¹) / d.gap := by
  unfold p_plus p_minus gap
  rw [← sub_div]

/-! ## Part (iii): Markov property as memorylessness -/

/-- The Markov chain transition data at a single crossing.

    The Markov trace property tr_M(x T_n) = z · tr_M(x) says that
    the expectation value of generator n is independent of the history
    x ∈ H_{n−1}(q).  The vertex volume V̂_i = z · a_i + b_i is the
    one-step conditional expectation. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
structure MarkovTransitionStep where
  /-- Hecke reduction coefficient a_i (coefficient of T_i). -/
  a : ℝ
  /-- Hecke reduction constant b_i. -/
  b : ℝ
  /-- Markov parameter z. -/
  z : ℝ
  /-- z ≠ 0. -/
  z_ne_zero : z ≠ 0

/-- The vertex volume = one-step conditional expectation:
    V̂_i = z · a_i + b_i.

    Under the Markov trace, tr_M(a_i T_i + b_i) = z · a_i + b_i
    because tr_M(T_i) = z (Markov property) and tr_M(1) = 1
    (normalisation). -/
noncomputable def MarkovTransitionStep.vertexVolume (s : MarkovTransitionStep) : ℝ :=
  s.z * s.a + s.b

/-! ## Part (iv): Independence and factorization -/

/-- **Product factorization from independence.**

    Given n−1 independent transition steps, the total Markov trace
    is the product of vertex volumes:

      tr_M(ρ(β)) = ∏_{i=0}^{n−2} V̂_i

    Each V̂_i depends only on the local crossing data (a_i, b_i),
    not on the other generators.  This holds for words that use each
    generator once (one step per generator, as indexed by `Fin (n-1)`
    here).  It fails when a generator repeats: tr_M(σ₁σ₂σ₁) = h z² + z,
    not z³ (corrected 2026-11-16).  The product is a definition here
    (`MarkovChainFactorization.totalTrace`); its identification with
    the Markov trace of the grouped word is not proved in this file.
    (Until 2026-11-16 `totalTrace` was a free field and the product
    formula a structure field, so the structure assumed the formula.) -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [diaconis-ram2000] Diaconis & Ram, "Analysis of systematic scan Metropolis algorithms using Iwahori-Hecke algebra techniques," Ann. Appl. Probab. 12 (2000), arXiv:math/0401318
structure MarkovChainFactorization where
  /-- Number of strands. -/
  n : ℕ
  /-- At least two strands. -/
  n_ge : n ≥ 2
  /-- The transition steps, one per generator. -/
  steps : Fin (n - 1) → MarkovTransitionStep

/-- The product of the vertex volumes, `∏ᵢ V̂ᵢ`. -/
noncomputable def MarkovChainFactorization.totalTrace
    (mcf : MarkovChainFactorization) : ℝ :=
  Finset.univ.prod (fun i => (mcf.steps i).vertexVolume)

/-- The product is nonzero when all vertex volumes are nonzero. -/
theorem MarkovChainFactorization.trace_ne_zero
    (mcf : MarkovChainFactorization)
    (h : ∀ i, (mcf.steps i).vertexVolume ≠ 0) :
    mcf.totalTrace ≠ 0 :=
  Finset.prod_ne_zero_iff.mpr (fun i _ => h i)

/-! ## Connecting spectral data to transition steps -/

/-- A single crossing, fully described: spectral data + Hecke reduction.

    The Hecke reduction a_i T_i + b_i evaluated through the spectral
    idempotents gives:
      a_i · (q · e₊ − q⁻¹ · e₋) + b_i
    and the Markov trace picks out the expectation V̂_i = z a_i + b_i. -/
structure CrossingData where
  /-- Spectral data (q parameter). -/
  spectral : SpectralIdempotentData
  /-- Hecke reduction at this generator. -/
  step : MarkovTransitionStep

/-- The probability-weighted expectation of the crossing eigenvalues:

    E[eigenvalue] = p₊ · q + p₋ · (−q⁻¹) = q − q⁻¹

    This is the spectral content of the Markov parameter:
    the expected eigenvalue under the stochastic transition operator. -/
-- Ref: [diaconis-ram2000] Diaconis & Ram, "Analysis of systematic scan Metropolis algorithms using Iwahori-Hecke algebra techniques," Ann. Appl. Probab. 12 (2000), arXiv:math/0401318
theorem eigenvalue_expectation (d : SpectralIdempotentData) :
    d.p_plus * d.q + d.p_minus * (-d.q⁻¹) =
    d.q - d.q⁻¹ := by
  unfold SpectralIdempotentData.p_plus SpectralIdempotentData.p_minus
    SpectralIdempotentData.gap
  have hq : d.q ≠ 0 := ne_of_gt d.q_pos
  have hgap : d.q + d.q⁻¹ ≠ 0 := d.gap_ne_zero
  field_simp
  ring

/-! ## Existence -/

/- **Existence of Markov chain factorization.**

    Given a braid β ∈ B_n with Hecke reduction at each generator,
    the Markov trace factors as a product of vertex volumes.  The
    proof is the recursive application of the Markov property
    (Jones 1987, Theorem 5.1) — formalized in `markov-trace-product.lean`.

    The axiom below marks the inductive step that references the Markov
    trace machinery (an external proof). -/
/-- **The former axiom `markov_chain_factorization_axiom` was false**
    (removed 2026-11-15, with its wrapper `markov_chain_factorization_exists`).
    It quantified `totalTrace : ℝ` universally, so it asserted that every
    real number equals the product of vertex volumes. The intended statement
    needs `totalTrace` to be the Markov trace of the braid, which this file
    does not define; recorded as open in bean `qou-n2un`. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
theorem not_markov_chain_factorization_unconstrained :
    ¬ ∀ (n : ℕ) (_hn : n ≥ 2)
      (steps : Fin (n - 1) → MarkovTransitionStep)
      (totalTrace : ℝ)
      (_h_markov : ∀ i, (steps i).z = (steps ⟨0, by omega⟩).z),
        totalTrace = Finset.univ.prod (fun i => (steps i).vertexVolume) := by
  intro h
  let st : MarkovTransitionStep := ⟨0, 0, 1, one_ne_zero⟩
  have := h 2 le_rfl (fun _ => st)
    ((Finset.univ.prod (fun _ : Fin (2 - 1) => st.vertexVolume)) + 1) (fun _ => rfl)
  linarith

end QOU.Braiding
