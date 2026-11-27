import QOU.FluidDynamics.q_ns_block_ladder

/-!
# QOU.FluidDynamics.q_ns_block_weight_lap — `L = X₊X₋` on the weight blocks `(αγ)^s · K[ζ]`

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), part (a): the operator
`L = X₊ ∘ X₋` of `OqSU2BudgetLittleQJacobi` on a general weight block, not only on the
Cartan block `K[ζ]`. Part (b), the coupling between blocks, is `q_ns_block_ladder`.

Write `A = αγ`, `ζ = βγ`, `B_s = A^s · K[ζ]`, and `[n]_x = 1 + x + ⋯ + x^{n-1}` (`jk x n`).
`X₊` maps `B_{s-1}` to `B_s` (`fieldPlus_ladder`). This file shows that `X₋` maps `B_s`
back to `B_{s-1}`, so `L` preserves every `B_s`, and computes `L` there.

## Results (over a commutative ring `R`, `q : Rˣ`)

* `tw_alphaGamma`: the twist scales `A` by `q⁻²`.
* `fieldMinus_alphaGamma_pow`: `X₋(A^{s}) = A^{s-1} ([s]_{q⁻²} + (q + q⁻¹)[s]_{q⁻⁴} ζ)`,
  for `s = r + 1 ≥ 1`.
* `fieldMinus_block`: `X₋(A^{s} ζ^{k+1}) = A^{s-1} (a_k ζ^{k+1} + b_k ζ^{k+2})`. `X₋` lowers
  the block index by one and raises the `ζ`-degree by at most one.
* `lap_alphaGamma_pow`: `L(A^s) = q⁻¹ (q + q⁻¹)[s]_{q⁻⁴} · A^s`. The lowest element of
  each block is an eigenvector.
* `lap_block`: `L(A^s ζ^{k+1}) = c_k · A^s ζ^k + D_{k+1} · A^s ζ^{k+1}`. So `L` is lower
  bidiagonal on `B_s` in the basis `A^s ζ^m`, as it is on `B_0` (`lap_zeta_pow`).
* `blockDiag`: the diagonal entry,
  `D_m(s) = q⁻¹ [m+1]_{q⁻²} ((q + q⁻¹)[s]_{q⁻⁴} + q³ [m]_{q²})`, and `lap_block_diag`
  restates `lap_block` with it.
* `blockDiag_strictMono`: for `0 < q` over an ordered field, `D_m(s)` strictly increases
  in `m`. So the diagonal entries on each block are distinct, which is what triangularity
  needs for an eigenbasis.

At `q = 1`, `D_m(s) = (m + 1)(m + 2s)`. With `l = s + m` and weight `s`, that is
`(l + s)(l − s + 1)`, the classical value of `L₊L₋` on spin `l`, weight `s`.

## Not established

* The eigenpolynomials themselves, and that they are the little q-Jacobi polynomials
  `p_m(ζ; q^{2s}, ·; q²)`. The diagonal fixes the spectrum; the identification of the
  polynomials is a separate computation.
* The Haar pairing on `B_s`. The Haar state is zero on `B_s` for `s ≠ 0` (nonzero
  weight), so an integration-by-parts identity on `B_s` pairs it with the opposite block
  `(βδ)^s K[ζ]`. That needs `X₊` and `X₋` on `(βδ)^s K[ζ]`, or the invariance
  `h ∘ X₊ = 0`, and neither is in the corpus yet.
* That `L` on these blocks is the q-NS viscous term. See `q_ns_block_viscous_dissipation`.

Everything is algebraic, so the file stays out of `QOU/Transcendental/`. No empirical
value enters any proof.

-- Ref: [woronowicz1987-twisted-su2] (the relations of `S_μU(2)`)
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.BlockLadder

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

section Ring

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))

/-- `tw(αγ) = q⁻² αγ`. -/
theorem tw_alphaGamma :
    torusScaleAlgHom (R := R) q q⁻¹ q⁻¹⁻¹ (α q * γ q) = (qi * qi) • (α q * γ q) := by
  obtain ⟨ha, -, hg, -⟩ := field_twist_generators (R := R) q
  rw [map_mul, ha, hg, smul_mul_smul_comm]

theorem tw_zetaB_pow (k : ℕ) :
    torusScaleAlgHom (R := R) q q⁻¹ q⁻¹⁻¹ (zetaB q ^ k) = zetaB q ^ k := by
  rw [map_pow, tw_zeta]

/-- `ζ αγ = q⁻² αγ ζ`. -/
theorem zetaB_alphaGamma :
    zetaB (R := R) q * (α q * γ q) = (qi * qi) • ((α q * γ q) * zetaB q) := by
  simpa using zetaB_pow_alphaGamma q 1

/-- **`X₋` on `(αγ)^{r+1}`.** `X₋(A^{r+1}) = [r+1]_{q⁻²} A^r + (q + q⁻¹)[r+1]_{q⁻⁴} A^r ζ`. -/
theorem fieldMinus_alphaGamma_pow (r : ℕ) :
    fieldMinus q ((α (R := R) q * γ q) ^ (r + 1)) =
      jk (qi * qi) (r + 1) • (α q * γ q) ^ r +
        (((q : R) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1)) •
          ((α q * γ q) ^ r * zetaB q) := by
  induction r with
  | zero => simp [fieldMinus_alphaGamma]
  | succ r ih =>
    have h1 : (α (R := R) q * γ q) ^ r * ((qi * qi) • (α q * γ q)) =
        (qi * qi) • (α q * γ q) ^ (r + 1) := by
      rw [mul_smul_comm, ← pow_succ]
    have h2 : ((α (R := R) q * γ q) ^ r * zetaB q) * ((qi * qi) • (α q * γ q)) =
        ((qi * qi) * (qi * qi)) • ((α q * γ q) ^ (r + 1) * zetaB q) := by
      rw [mul_smul_comm, mul_assoc, zetaB_alphaGamma, mul_smul_comm, smul_smul, pow_succ]
      simp only [mul_assoc]
    have h3 : (α (R := R) q * γ q) ^ (r + 1) * (1 + ((q : R) + qi) • zetaB q) =
        (α q * γ q) ^ (r + 1) + ((q : R) + qi) • ((α q * γ q) ^ (r + 1) * zetaB q) := by
      rw [mul_add, mul_one, mul_smul_comm]
    rw [pow_succ (α q * γ q) (r + 1), field_leibniz, ih, tw_alphaGamma, fieldMinus_alphaGamma,
      add_mul, smul_mul_assoc, smul_mul_assoc, h1, h2, h3, jk_succ' (qi * qi) (r + 1),
      jk_succ' ((qi * qi) * (qi * qi)) (r + 1)]
    module

/-- `A^{r+1} ζ^k βδ = q^{2k} q² A^r ζ^{k+1} + q^{2k} q³ A^r ζ^{k+2}`. -/
theorem alphaGamma_pow_zeta_pow_betaDelta (r k : ℕ) :
    (α (R := R) q * γ q) ^ (r + 1) * (zetaB q ^ k * (β q * δ q)) =
      (((q : R) * q) ^ k * ((q : R) * q)) • ((α q * γ q) ^ r * zetaB q ^ (k + 1)) +
        (((q : R) * q) ^ k * ((q : R) * q * q)) • ((α q * γ q) ^ r * zetaB q ^ (k + 2)) := by
  have e1 : (α (R := R) q * γ q) ^ r * (zetaB q ^ k * zetaB q) =
      (α q * γ q) ^ r * zetaB q ^ (k + 1) := by rw [← pow_succ]
  have e2 : (α (R := R) q * γ q) ^ r * (zetaB q ^ k * (zetaB q * zetaB q)) =
      (α q * γ q) ^ r * zetaB q ^ (k + 2) := by
    rw [show k + 2 = k + 1 + 1 from rfl, pow_succ, pow_succ]; simp only [mul_assoc]
  calc (α (R := R) q * γ q) ^ (r + 1) * (zetaB q ^ k * (β q * δ q))
      = (α q * γ q) ^ r * (((α q * γ q) * zetaB q ^ k) * (β q * δ q)) := by
        rw [pow_succ]; simp only [mul_assoc]
    _ = ((q : R) * q) ^ k • ((α q * γ q) ^ r * (zetaB q ^ k * ((α q * γ q) * (β q * δ q)))) := by
        rw [alphaGamma_zeta_pow, smul_mul_assoc, mul_smul_comm]; simp only [mul_assoc]
    _ = _ := by
        rw [alphaGamma_betaDelta, mul_add, mul_smul_comm, mul_smul_comm, mul_add, mul_smul_comm,
          mul_smul_comm, e1, e2]
        module

/-- **`X₋` on the block `B_{r+1}`.** `X₋(A^{r+1} ζ^{k+1}) = a_k A^r ζ^{k+1} + b_k A^r ζ^{k+2}`,
with `a_k = [r+1]_{q⁻²} + [k+1]_{q⁻²} q^{2k} q²` and
`b_k = (q + q⁻¹)[r+1]_{q⁻⁴} + [k+1]_{q⁻²} q^{2k} q³`. -/
theorem fieldMinus_block (r k : ℕ) :
    fieldMinus q ((α (R := R) q * γ q) ^ (r + 1) * zetaB q ^ (k + 1)) =
      (jk (qi * qi) (r + 1) + jk (qi * qi) (k + 1) * (((q : R) * q) ^ k * ((q : R) * q))) •
          ((α q * γ q) ^ r * zetaB q ^ (k + 1)) +
        (((q : R) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1) +
            jk (qi * qi) (k + 1) * (((q : R) * q) ^ k * ((q : R) * q * q))) •
          ((α q * γ q) ^ r * zetaB q ^ (k + 2)) := by
  have e3 : ((α (R := R) q * γ q) ^ r * zetaB q) * zetaB q ^ (k + 1) =
      (α q * γ q) ^ r * zetaB q ^ (k + 2) := by rw [mul_assoc, ← pow_succ']
  have e4 : (α (R := R) q * γ q) ^ r * zetaB q ^ (k + 1) =
      (α q * γ q) ^ r * zetaB q ^ (k + 1) := rfl
  rw [field_leibniz, fieldMinus_alphaGamma_pow, tw_zetaB_pow, fieldMinus_zeta_pow, mul_smul_comm,
    alphaGamma_pow_zeta_pow_betaDelta, add_mul, smul_mul_assoc, smul_mul_assoc, e3, e4]
  module

/-- **`L` on the lowest element of a block.** `L(A^{r+1}) = q⁻¹(q + q⁻¹)[r+1]_{q⁻⁴} A^{r+1}`. -/
theorem lap_alphaGamma_pow (r : ℕ) :
    lap q ((α (R := R) q * γ q) ^ (r + 1)) =
      (qi * (((q : R) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1))) • (α q * γ q) ^ (r + 1) := by
  have hl := fieldPlus_ladder q r 0
  rw [zero_add, pow_one, pow_zero, mul_one] at hl
  rw [lap_apply, fieldMinus_alphaGamma_pow, map_add, map_smul, map_smul,
    fieldPlus_alphaGamma_pow, hl]
  simp only [jk_one]
  module

/-- **`L` on the block `B_{r+1}`.** `L(A^{r+1} ζ^{k+1}) = c · A^{r+1} ζ^k + D · A^{r+1} ζ^{k+1}`:
lower bidiagonal. -/
theorem lap_block (r k : ℕ) :
    lap q ((α (R := R) q * γ q) ^ (r + 1) * zetaB q ^ (k + 1)) =
      ((jk (qi * qi) (r + 1) + jk (qi * qi) (k + 1) * (((q : R) * q) ^ k * ((q : R) * q))) *
          (qi * jk (qi * qi) (k + 1))) • ((α q * γ q) ^ (r + 1) * zetaB q ^ k) +
        ((((q : R) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1) +
            jk (qi * qi) (k + 1) * (((q : R) * q) ^ k * ((q : R) * q * q))) *
          (qi * jk (qi * qi) (k + 2))) • ((α q * γ q) ^ (r + 1) * zetaB q ^ (k + 1)) := by
  have hl1 := fieldPlus_ladder q r k
  have hl2 := fieldPlus_ladder q r (k + 1)
  rw [show k + 1 + 1 = k + 2 from rfl] at hl2
  rw [lap_apply, fieldMinus_block, map_add, map_smul, map_smul, hl1, hl2, smul_smul, smul_smul]

end Ring

section Diag

variable {K : Type*} [Field K] (q : Kˣ)

/-- The diagonal entry of `L` on `B_s` at `ζ`-degree `m`:
`D_m(s) = q⁻¹ [m+1]_{q⁻²} ((q + q⁻¹)[s]_{q⁻⁴} + q³ [m]_{q²})`. -/
noncomputable def blockDiag (s m : ℕ) : K :=
  (q : K)⁻¹ * jk ((q : K)⁻¹ * (q : K)⁻¹) (m + 1) *
    (((q : K) + (q : K)⁻¹) * jk (((q : K)⁻¹ * (q : K)⁻¹) * ((q : K)⁻¹ * (q : K)⁻¹)) s +
      (q : K) ^ 3 * jk ((q : K) * q) m)

/-- `[k+1]_{q⁻²} q^{2k} = [k+1]_{q²}`. -/
theorem jk_inv_mul_pow (k : ℕ) :
    jk ((q : K)⁻¹ * (q : K)⁻¹) (k + 1) * ((q : K) * q) ^ k = jk ((q : K) * q) (k + 1) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  rw [mul_comm]
  exact jk_reverse (S := K) (y := (q : K) * q) (z := (q : K)⁻¹ * (q : K)⁻¹) (by field_simp) k

/-- `lap_block`, with the diagonal entry written as `blockDiag`. -/
theorem lap_block_diag (r k : ℕ) : ∃ c : K,
    lap q ((α (R := K) q * γ q) ^ (r + 1) * zetaB q ^ (k + 1)) =
      c • ((α q * γ q) ^ (r + 1) * zetaB q ^ k) +
        blockDiag q (r + 1) (k + 1) • ((α q * γ q) ^ (r + 1) * zetaB q ^ (k + 1)) := by
  refine ⟨(jk (((q⁻¹ : Kˣ) : K) * ((q⁻¹ : Kˣ) : K)) (r + 1) +
      jk (((q⁻¹ : Kˣ) : K) * ((q⁻¹ : Kˣ) : K)) (k + 1) * (((q : K) * q) ^ k * ((q : K) * q))) *
      (((q⁻¹ : Kˣ) : K) * jk (((q⁻¹ : Kˣ) : K) * ((q⁻¹ : Kˣ) : K)) (k + 1)), ?_⟩
  rw [lap_block]
  congr 2
  have hk := jk_inv_mul_pow q k
  rw [blockDiag, qi_eq_inv, show k + 1 + 1 = k + 2 from rfl]
  linear_combination ((q : K)⁻¹ * jk ((q : K)⁻¹ * (q : K)⁻¹) (k + 2) *
    ((q : K) * q * q)) * hk

end Diag

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

theorem jk_nonneg {x : K} (hx : 0 ≤ x) (n : ℕ) : 0 ≤ jk x n := by
  unfold jk; exact Finset.sum_nonneg fun i _ => pow_nonneg hx i

theorem jk_strictMono {x : K} (hx : 0 < x) : StrictMono (jk x) :=
  strictMono_nat_of_lt_succ fun n => by rw [jk_succ]; exact lt_add_of_pos_right _ (pow_pos hx n)

/-- **The diagonal entries on each block are distinct.** For `0 < q`, `D_m(s)` strictly
increases in `m`. -/
theorem blockDiag_strictMono (q : Kˣ) (hq : 0 < (q : K)) (s : ℕ) :
    StrictMono (blockDiag q s) := by
  have hi : 0 < (q : K)⁻¹ := inv_pos.2 hq
  have hx : 0 < (q : K)⁻¹ * (q : K)⁻¹ := mul_pos hi hi
  have hy : 0 < (q : K) * q := mul_pos hq hq
  have hc : 0 ≤ ((q : K) + (q : K)⁻¹) * jk (((q : K)⁻¹ * (q : K)⁻¹) * ((q : K)⁻¹ * (q : K)⁻¹)) s :=
    mul_nonneg (by positivity) (jk_nonneg (by positivity) s)
  intro m n hmn
  unfold blockDiag
  have h1 : jk ((q : K)⁻¹ * (q : K)⁻¹) (m + 1) < jk ((q : K)⁻¹ * (q : K)⁻¹) (n + 1) :=
    jk_strictMono hx (by omega)
  have h1p : 0 < jk ((q : K)⁻¹ * (q : K)⁻¹) (m + 1) := by
    rw [jk_succ']; have := jk_nonneg hx.le m; positivity
  have h2 : jk ((q : K) * q) m < jk ((q : K) * q) n := jk_strictMono hy hmn
  have h2p : 0 ≤ jk ((q : K) * q) m := jk_nonneg hy.le m
  have hq3 : 0 < (q : K) ^ 3 := pow_pos hq 3
  have hA : 0 ≤ ((q : K) + (q : K)⁻¹) *
      jk (((q : K)⁻¹ * (q : K)⁻¹) * ((q : K)⁻¹ * (q : K)⁻¹)) s + (q : K) ^ 3 * jk ((q : K) * q) m :=
    add_nonneg hc (mul_nonneg hq3.le h2p)
  have hB : ((q : K) + (q : K)⁻¹) *
      jk (((q : K)⁻¹ * (q : K)⁻¹) * ((q : K)⁻¹ * (q : K)⁻¹)) s + (q : K) ^ 3 * jk ((q : K) * q) m <
      ((q : K) + (q : K)⁻¹) *
      jk (((q : K)⁻¹ * (q : K)⁻¹) * ((q : K)⁻¹ * (q : K)⁻¹)) s + (q : K) ^ 3 * jk ((q : K) * q) n := by
    have := mul_lt_mul_of_pos_left h2 hq3; linarith
  have := mul_lt_mul'' h1 hB h1p.le hA
  calc (q : K)⁻¹ * jk ((q : K)⁻¹ * (q : K)⁻¹) (m + 1) * _ =
      (q : K)⁻¹ * (jk ((q : K)⁻¹ * (q : K)⁻¹) (m + 1) * _) := by ring
    _ < (q : K)⁻¹ * (jk ((q : K)⁻¹ * (q : K)⁻¹) (n + 1) * _) := mul_lt_mul_of_pos_left this hi
    _ = _ := by ring

end Ordered

end QOU.FluidDynamics.BlockLadder
