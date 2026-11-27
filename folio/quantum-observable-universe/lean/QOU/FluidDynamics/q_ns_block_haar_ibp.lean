import QOU.FluidDynamics.q_ns_block_weight_lap
import QOU.FluidDynamics.q_ns_haar_field_invariance

/-!
# QOU.FluidDynamics.q_ns_block_haar_ibp — integration by parts on the weight blocks

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), part (a), last step: the
Haar integration-by-parts identity on the weight block `B_s = (αγ)^s · K[ζ]`, `s ≥ 1`.

On the Cartan block `s = 0` this is `haarState_budget_poly`:
`h(X₊ a · X₋ b) = −q⁻² h(a · L b)`. For `s ≥ 1` the Haar state vanishes on `B_s`
(nonzero torus weight), so `b ∈ B_s` pairs with `a` in the opposite block
`K[ζ] · (βδ)^s`.

Write `A = αγ`, `D = βδ`, `ζ = βγ`, `L = X₊ ∘ X₋` (`lap`), and `ev P = P(ζ)`.

## Results (over a field `K`, `q : Kˣ`, `[n]_{q²} ≠ 0` for all `n`)

* `ev_mul_alphaGamma`, `betaDelta_mul_ev`: `K[ζ]` moves past `A` and `D` up to a
  rescaling of the polynomial.
* `betaDelta_pow_mul_alphaGamma_pow`: `D^n A^n ∈ K[ζ]`.
* `block_pair_mem`: `ev P · D^{r+1} · A^r · ev Q ∈ K[ζ] · D`.
* `fieldMinus_block_mem`: `X₋(A^{r+1} ev Q) ∈ A^r K[ζ]`.
* `haarState_block_ibp`: for `s = r + 1 ≥ 1`,
  `h(X₊(ev P · D^s) · X₋(A^s ev Q)) = −q^{2(s−1)} h(ev P · D^s · L(A^s ev Q))`.

The proof is the Leibniz rule for `X₊` plus `h ∘ X₊ = 0` on `K[ζ] · D`
(`haarState_fieldPlus_ev_betaDelta`, #9713). The twist scales `A^{s-1} K[ζ]` by
`q^{-2(s-1)}`, which is the factor.

## Not established

* `h ∘ X₊ = 0` on all of `O_q(SU(2))`. Only the blocks needed here are covered.
* That the pairing `B_s × K[ζ]D^s → K` is nondegenerate, or that `L` is symmetric for
  it. With `lap_block` (#9707) those would give the little q-Jacobi orthogonality on
  each block.
* That this budget is the q-NS transport budget (bean `qou-pa7n`).

Everything is algebraic. No empirical value enters any proof.

-- Ref: [woronowicz1987-twisted-su2] (the relations of `S_μU(2)`)
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.BlockLadder

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.HaarFieldInvariance

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-- `P(ζ) αγ = αγ P'(ζ)`. -/
theorem ev_mul_alphaGamma (P : Polynomial K) :
    ∃ P' : Polynomial K, ev q P * (α q * γ q) = (α q * γ q) * ev q P' := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ =>
    obtain ⟨Q₁, e₁⟩ := h₁; obtain ⟨Q₂, e₂⟩ := h₂
    exact ⟨Q₁ + Q₂, by rw [map_add, add_mul, e₁, e₂, map_add, mul_add]⟩
  | monomial n c =>
    refine ⟨Polynomial.monomial n (c * (qi * qi) ^ n), ?_⟩
    rw [ev_monomial, ev_monomial, smul_mul_assoc, zetaB_pow_alphaGamma, smul_smul,
      mul_smul_comm]

/-- `βδ ζ^n = q^{-2n} ζ^n βδ`. -/
theorem betaDelta_zeta_pow (n : ℕ) :
    (β (R := K) q * δ q) * zetaB q ^ n = (qi * qi) ^ n • (zetaB q ^ n * (β q * δ q)) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', ← mul_assoc, betaDelta_zeta, smul_mul_assoc, mul_assoc, ih, mul_smul_comm,
      smul_smul, ← mul_assoc, ← pow_succ', pow_succ' (qi * qi) n]

/-- `βδ P(ζ) = P'(ζ) βδ`. -/
theorem betaDelta_mul_ev (P : Polynomial K) :
    ∃ P' : Polynomial K, (β q * δ q) * ev q P = ev q P' * (β q * δ q) := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ =>
    obtain ⟨Q₁, e₁⟩ := h₁; obtain ⟨Q₂, e₂⟩ := h₂
    exact ⟨Q₁ + Q₂, by rw [map_add, mul_add, e₁, e₂, map_add, add_mul]⟩
  | monomial n c =>
    refine ⟨Polynomial.monomial n (c * (qi * qi) ^ n), ?_⟩
    rw [ev_monomial, ev_monomial, mul_smul_comm, betaDelta_zeta_pow, smul_smul,
      smul_mul_assoc, mul_comm c]

/-- `βδ αγ ∈ K[ζ]`. -/
theorem betaDelta_alphaGamma_ev :
    (β q * δ q) * (α q * γ q) =
      ev q (Polynomial.X + Polynomial.C qi * Polynomial.X ^ 2) := by
  rw [betaDelta_alphaGamma, map_add, map_mul, ev, Polynomial.aeval_X, Polynomial.aeval_C,
    map_pow, Polynomial.aeval_X, Algebra.smul_def, pow_two]

/-- `(βδ)^n (αγ)^n ∈ K[ζ]`. -/
theorem betaDelta_pow_mul_alphaGamma_pow (n : ℕ) :
    ∃ P : Polynomial K, (β q * δ q) ^ n * (α q * γ q) ^ n = ev q P := by
  induction n with
  | zero => exact ⟨1, by rw [pow_zero, pow_zero, mul_one, map_one]⟩
  | succ n ih =>
    obtain ⟨P, hP⟩ := ih
    obtain ⟨P', hP'⟩ := ev_mul_alphaGamma q P
    refine ⟨(Polynomial.X + Polynomial.C qi * Polynomial.X ^ 2) * P', ?_⟩
    calc (β q * δ q) ^ (n + 1) * (α q * γ q) ^ (n + 1)
        = (β q * δ q) * ((β q * δ q) ^ n * (α q * γ q) ^ n) * (α q * γ q) := by
          rw [pow_succ', pow_succ]; simp only [mul_assoc]
      _ = (β q * δ q) * (α q * γ q) * ev q P' := by
          rw [hP, mul_assoc, hP', ← mul_assoc]
      _ = _ := by rw [betaDelta_alphaGamma_ev, map_mul]

/-- **The pairing lands in `K[ζ] · βδ`.** `P(ζ) (βδ)^{r+1} (αγ)^r Q(ζ) = P'(ζ) βδ`. -/
theorem block_pair_mem (r : ℕ) (P Q : Polynomial K) :
    ∃ P' : Polynomial K,
      ev q P * (β q * δ q) ^ (r + 1) * ((α q * γ q) ^ r * ev q Q) = ev q P' * (β q * δ q) := by
  obtain ⟨P₀, h₀⟩ := betaDelta_pow_mul_alphaGamma_pow q r
  obtain ⟨P₁, h₁⟩ := betaDelta_mul_ev q (P₀ * Q)
  refine ⟨P * P₁, ?_⟩
  calc ev q P * (β q * δ q) ^ (r + 1) * ((α q * γ q) ^ r * ev q Q)
      = ev q P * ((β q * δ q) * (((β q * δ q) ^ r * (α q * γ q) ^ r) * ev q Q)) := by
        rw [pow_succ']; simp only [mul_assoc]
    _ = ev q (P * P₁) * (β q * δ q) := by
        rw [h₀, ← map_mul, h₁, map_mul, mul_assoc]

/-- **`X₋` maps `(αγ)^{r+1} K[ζ]` into `(αγ)^r K[ζ]`.** -/
theorem fieldMinus_block_mem (r : ℕ) (Q : Polynomial K) :
    ∃ Q' : Polynomial K, fieldMinus q ((α q * γ q) ^ (r + 1) * ev q Q) =
      (α q * γ q) ^ r * ev q Q' := by
  have hb : ∀ (m m' : ℕ) (c₁ c₂ : K),
      c₁ • ((α (R := K) q * γ q) ^ r * zetaB q ^ m) + c₂ • ((α q * γ q) ^ r * zetaB q ^ m') =
        (α q * γ q) ^ r * ev q (Polynomial.monomial m c₁ + Polynomial.monomial m' c₂) := by
    intro m m' c₁ c₂
    rw [map_add, ev_monomial, ev_monomial, mul_add, mul_smul_comm, mul_smul_comm]
  induction Q using Polynomial.induction_on' with
  | add Q₁ Q₂ h₁ h₂ =>
    obtain ⟨R₁, e₁⟩ := h₁; obtain ⟨R₂, e₂⟩ := h₂
    exact ⟨R₁ + R₂, by rw [map_add, mul_add, map_add, e₁, e₂, map_add, mul_add]⟩
  | monomial n c =>
    have hn : ∃ Q' : Polynomial K, fieldMinus q ((α q * γ q) ^ (r + 1) * zetaB q ^ n) =
        (α q * γ q) ^ r * ev q Q' := by
      rcases n with _ | k
      · have := hb 0 1 (jk (qi * qi) (r + 1))
          (((q : K) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1))
        rw [pow_zero, pow_one, mul_one] at this
        rw [pow_zero, mul_one, fieldMinus_alphaGamma_pow]
        exact ⟨_, this⟩
      · rw [fieldMinus_block]
        exact ⟨_, hb _ _ _ _⟩
    obtain ⟨Q', hQ'⟩ := hn
    exact ⟨c • Q', by rw [ev_monomial, mul_smul_comm, map_smul, hQ', map_smul, mul_smul_comm]⟩

/-- The twist fixes `K[ζ]`. -/
theorem tw_ev (P : Polynomial K) :
    torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ (ev q P) = ev q P := by
  have h : (torusScaleAlgHom q q⁻¹ q⁻¹⁻¹).comp (ev q) = ev q :=
    Polynomial.algHom_ext (by simp only [AlgHom.comp_apply, ev, Polynomial.aeval_X, tw_zeta])
  exact congrArg (fun f => f P) h

/-- **Integration by parts on the weight block `B_{r+1}`.** For `a = P(ζ)(βδ)^{r+1}` and
`b = (αγ)^{r+1} Q(ζ)`, `h(X₊ a · X₋ b) = −q^{2r} h(a · L b)`. -/
theorem haarState_block_ibp (hq : ∀ n, qSqNum q n ≠ 0) (r : ℕ) (P Q : Polynomial K) :
    haarState q (fieldPlus q (ev q P * (β q * δ q) ^ (r + 1)) *
        fieldMinus q ((α q * γ q) ^ (r + 1) * ev q Q)) =
      -(((q : K) * q) ^ r) *
        haarState q (ev q P * (β q * δ q) ^ (r + 1) * lap q ((α q * γ q) ^ (r + 1) * ev q Q)) := by
  obtain ⟨Q', hQ'⟩ := fieldMinus_block_mem q r Q
  obtain ⟨P', hP'⟩ := block_pair_mem q r P Q'
  rw [lap_apply, hQ']
  set a := ev q P * (β q * δ q) ^ (r + 1)
  set y := (α q * γ q) ^ r * ev q Q'
  have htw : torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ y = (qi * qi) ^ r • y := by
    simp only [y]
    rw [map_mul, map_pow, tw_alphaGamma, tw_ev, smul_pow, smul_mul_assoc]
  have hL : fieldPlus q (a * y) = fieldPlus q a * torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ y +
      a * fieldPlus q y := field_leibniz q 0 1 0 a y
  have h0 : haarState q (fieldPlus q (a * y)) = 0 := by
    rw [hP']; exact haarState_fieldPlus_ev_betaDelta q hq P'
  rw [hL, htw, mul_smul_comm, map_add, map_smul, smul_eq_mul] at h0
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have hu : ((q : K) * q) ^ r * (qi * qi) ^ r = 1 := by
    rw [← mul_pow, qi_eq_inv]; field_simp; simp
  linear_combination ((q : K) * q) ^ r * h0 - haarState q (fieldPlus q a * y) * hu

end QOU.FluidDynamics.BlockLadder
