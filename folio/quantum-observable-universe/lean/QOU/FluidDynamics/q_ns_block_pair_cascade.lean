import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi

/-!
# QOU.FluidDynamics.q_ns_block_pair_cascade — the X₊/X₋ pair product on the Cartan block
# only moves weight upward, with a coupling that does not degenerate as `q → 1`

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), triad-transfer front.

On the torus-invariant block `K[ζ]`, `ζ = βγ`, the two off-diagonal fields of
`OqSU2BudgetLittleQJacobi` leave the block: `X₊ζ^{j+1}` has weight `αγ` and `X₋ζ^{k+1}`
has weight `βδ`. Their product has weight zero again, so it lies back in `K[ζ]`. This is
the quadratic weight-zero coupling `(a, b) ↦ X₊a · X₋b` whose Haar value is the
off-diagonal budget (`haarState_budget_poly`). This file computes it on monomials.

## Results

Write `[n] = 1 + x + ⋯ + x^{n−1}` with `x = q²` (`jk (q*q) n`).

* `pair_zetaB_pow`:
  `X₊ζ^{j+1} · X₋ζ^{k+1} = [j+1][k+1] · (q ζ^{j+k+1} + q² ζ^{j+k+2})`.
  So two monomials of degrees `j+1` and `k+1` couple **only** to degrees `j+k+1` and
  `j+k+2`. Nothing goes to lower degree: as a selection rule, the coupling is a forward
  cascade in the `ζ`-degree.
* `pair_coeff_ge`: for `1 ≤ q` both coefficients are at least `(j+1)(k+1)`. At `q = 1`
  they equal `(j+1)(k+1)` (`jk_one_eq`). So the coupling does not vanish as `q → 1⁺`.
  This is a statement about coefficients only, with no limit taken.

## Not established

* That `(a, b) ↦ X₊a · X₋b` is the q-NS advection term. The corpus defines no
  `∇_q` on `O_q(SU(2))` (see `q_ns_twisted_transport`), so this is a candidate triad
  coupling, not the q-NS nonlinearity.
* The coupling in the eigenbasis of `L` (the little q-Jacobi polynomials), as opposed to
  monomials. The degree statement transfers (each eigenpolynomial `p_n` has degree `n`),
  but the coefficients do not.
* Any energy-transfer rate, any lower bound on transfer into high modes along a
  solution, and Part A itself.

Everything is algebraic (ordered field, no limits), so the file stays out of
`QOU/Transcendental/`. No empirical value enters any proof.

-- Ref: [woronowicz1987-twisted-su2] (the relations of `S_μU(2)`)
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.BlockPairCascade

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

section Ring

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- **The pair product on monomials of the block.**
`X₊ζ^{j+1} · X₋ζ^{k+1} = [j+1]_{q²}[k+1]_{q²} · (q ζ^{j+k+1} + q² ζ^{j+k+2})`. -/
theorem pair_zetaB_pow (j k : ℕ) :
    fieldPlus q (zetaB (R := R) q ^ (j + 1)) * fieldMinus q (zetaB q ^ (k + 1)) =
      (jk ((q : R) * q) (j + 1) * jk ((q : R) * q) (k + 1)) •
        ((q : R) • zetaB q ^ (j + k + 1) + ((q : R) * q) • zetaB q ^ (j + k + 2)) := by
  have hqq : ((q : R) * q) * ((((q⁻¹ : Rˣ) : R)) * (((q⁻¹ : Rˣ) : R))) = 1 := by
    rw [mul_mul_mul_comm, Units.mul_inv, one_mul]
  have hrev := jk_reverse hqq k
  have hq1 : (((q⁻¹ : Rˣ) : R)) * (q : R) = 1 := by simp
  rw [fieldPlus_zeta_pow, fieldMinus_zeta_pow, smul_mul_smul_comm]
  have hprod : zetaB (R := R) q ^ j * (α q * γ q) * (zetaB q ^ k * (β q * δ q)) =
      ((q : R) * q) ^ k •
        (((q : R) * q) • zetaB q ^ (j + k + 1) + ((q : R) * q * q) • zetaB q ^ (j + k + 2)) := by
    calc zetaB (R := R) q ^ j * (α q * γ q) * (zetaB q ^ k * (β q * δ q))
        = zetaB q ^ j * ((α q * γ q) * zetaB q ^ k) * (β q * δ q) := by
          simp only [mul_assoc]
      _ = ((q : R) * q) ^ k • (zetaB q ^ j * zetaB q ^ k * ((α q * γ q) * (β q * δ q))) := by
          rw [alphaGamma_zeta_pow, mul_smul_comm, smul_mul_assoc]; simp only [mul_assoc]
      _ = ((q : R) * q) ^ k •
            (((q : R) * q) • zetaB q ^ (j + k + 1) +
              ((q : R) * q * q) • zetaB q ^ (j + k + 2)) := by
          rw [alphaGamma_betaDelta, ← pow_add, mul_add, mul_smul_comm, mul_smul_comm,
            ← pow_succ, ← mul_assoc, ← pow_succ, ← pow_succ]
  rw [hprod, smul_smul, smul_add, smul_smul, smul_smul, smul_add, smul_smul, smul_smul]
  congr 2
  · linear_combination (((q⁻¹ : Rˣ) : R)) * jk ((q : R) * q) (j + 1) * (q : R) * q * hrev +
      jk ((q : R) * q) (j + 1) * jk ((q : R) * q) (k + 1) * q * hq1
  · linear_combination (((q⁻¹ : Rˣ) : R)) * jk ((q : R) * q) (j + 1) * (q : R) * q * q * hrev +
      jk ((q : R) * q) (j + 1) * jk ((q : R) * q) (k + 1) * q * q * hq1

/-- At `x = 1`, `[n]_x = n`. -/
theorem jk_one_eq (n : ℕ) : jk (1 : R) n = n := by
  induction n with
  | zero => simp
  | succ n ih => rw [jk_succ, ih, one_pow]; push_cast; ring

end Ring

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

theorem jk_ge {x : K} (hx : 1 ≤ x) (n : ℕ) : (n : K) ≤ jk x n := by
  induction n with
  | zero => simp
  | succ n ih => rw [jk_succ]; push_cast; linarith [one_le_pow₀ (n := n) hx]

/-- **The coupling does not degenerate.** For `1 ≤ q`, both coefficients of
`pair_zetaB_pow` are at least `(j+1)(k+1)`. -/
theorem pair_coeff_ge (q : Kˣ) (hq : 1 ≤ (q : K)) (j k : ℕ) :
    ((j : K) + 1) * ((k : K) + 1) ≤
        jk ((q : K) * q) (j + 1) * jk ((q : K) * q) (k + 1) * q ∧
      ((j : K) + 1) * ((k : K) + 1) ≤
        jk ((q : K) * q) (j + 1) * jk ((q : K) * q) (k + 1) * (q * q) := by
  have hx : (1 : K) ≤ (q : K) * q := by nlinarith
  have hj := jk_ge hx (j + 1)
  have hk := jk_ge hx (k + 1)
  push_cast at hj hk
  have h0j : (0 : K) ≤ (j : K) + 1 := by positivity
  have h0k : (0 : K) ≤ (k : K) + 1 := by positivity
  have hprod : ((j : K) + 1) * ((k : K) + 1) ≤
      jk ((q : K) * q) (j + 1) * jk ((q : K) * q) (k + 1) :=
    mul_le_mul hj hk h0k (le_trans h0j hj)
  have hP : (0 : K) ≤ jk ((q : K) * q) (j + 1) * jk ((q : K) * q) (k + 1) :=
    le_trans (mul_nonneg h0j h0k) hprod
  constructor
  · nlinarith
  · nlinarith

end Ordered

end QOU.FluidDynamics.BlockPairCascade
