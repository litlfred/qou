import QOU.Archimedean.HeckeRep
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# Concrete Representations of H₃(q)

Explicit matrices for the three irreducible representations of the
Iwahori–Hecke algebra H₃(q):

1. **Symmetric** (trivial), dim 1: `σ_i ↦ q`
2. **Standard**, dim 2: explicit 2×2 matrices (Young seminormal form)
3. **Alternating** (sign), dim 1: `σ_i ↦ −q⁻¹`

## The standard representation

The 2D standard representation (partition (2,1)) is the key
ingredient for computing the axial coupling g_A.  The matrices
are in the Young seminormal form:

```
σ₀ = ⎡ q   1  ⎤     σ₁ = ⎡ −q⁻¹   0 ⎤
     ⎣ 0  −q⁻¹ ⎦          ⎣  1      q ⎦
```

These satisfy:
- Hecke relation: `σ² = (q − q⁻¹)σ + I`
- Braid relation: `σ₀σ₁σ₀ = σ₁σ₀σ₁`

## References

- [jones1987] V. Jones, Hecke algebra representations of braid groups
  and link polynomials.
- [wenzl1988] H. Wenzl, Hecke algebras of type A_n and subfactors.
-/

namespace QOU.Archimedean

open Matrix

/-! ## §1  Standard representation matrices -/

/-- Generator σ₀ in the standard (2,1) representation of H₃(q).

    ```
    σ₀ = ⎡ q   1  ⎤
         ⎣ 0  −q⁻¹ ⎦
    ```

    Eigenvalues: q (top-left) and −q⁻¹ (bottom-right). -/
noncomputable def stdRep3_gen0 : TMatrix :=
  Matrix.of !![q_from_t, 1; 0, -q_inv_from_t]

/-- Generator σ₁ in the standard (2,1) representation of H₃(q).

    ```
    σ₁ = ⎡ −q⁻¹   0 ⎤
         ⎣  1      q ⎦
    ```

    Eigenvalues: q (bottom-right) and −q⁻¹ (top-left). -/
noncomputable def stdRep3_gen1 : TMatrix :=
  Matrix.of !![-q_inv_from_t, 0; 1, q_from_t]

/-- Generator inverse σ₀⁻¹ in the standard (2,1) representation.

    `σ₀⁻¹ = σ₀ − HA · I = ⎡ q⁻¹   1  ⎤`
                            `⎣ 0    −q  ⎦` -/
noncomputable def stdRep3_genInv0 : TMatrix :=
  stdRep3_gen0 - HA_t • 1

/-- Generator inverse σ₁⁻¹ in the standard (2,1) representation.

    `σ₁⁻¹ = σ₁ − HA · I = ⎡ −q     0  ⎤`
                            `⎣  1    q⁻¹ ⎦` -/
noncomputable def stdRep3_genInv1 : TMatrix :=
  stdRep3_gen1 - HA_t • 1

/-! ## §1a  Laurent-`T` arithmetic closers

  The per-entry goals below live in `R_t = ℤ[t, t⁻¹] = AddMonoidAlgebra ℤ ℤ`,
  where `t · t⁻¹ = 1` is `T 1 * T (-1) = T 0` — an `AddMonoidAlgebra`
  fact, **not** a `ring` fact (`ring` treats `T 1` and `T (-1)` as
  independent atoms and cannot use the relation).  The closers below
  therefore unfold all scalars to `T`-monomials, distribute, fold every
  product with `← LaurentPolynomial.T_add` (so `T m * T n` becomes
  `T (m + n)` with a *literal* exponent), and let `norm_num` evaluate
  the exponent arithmetic; the surviving goal is ℤ-linear in distinct
  `T k` atoms, which the ring-normalising core of `norm_num` closes. -/

/-- `q − HA = q⁻¹` in `R_t` (pure ring identity, no `t·t⁻¹` relation). -/
lemma q_from_t_sub_HA_t : q_from_t - HA_t = q_inv_from_t := by
  unfold HA_t
  ring

/-! ## §2  Hecke relation verification -/

/-- σ₀ satisfies the Hecke relation in the standard representation. -/
-- Ref: [jones1987]
theorem stdRep3_hecke0 :
    stdRep3_gen0 * stdRep3_gen0 = HA_t • stdRep3_gen0 + 1 := by
  ext i j : 1
  fin_cases i <;> fin_cases j <;>
    simp [stdRep3_gen0, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply] <;>
    simp only [HA_t, q_from_t, q_inv_from_t, t, t_inv, sub_mul,
               ← LaurentPolynomial.T_add, Int.reduceAdd, Int.reduceNeg,
               LaurentPolynomial.T_zero] <;>
    ring1

/-- σ₁ satisfies the Hecke relation in the standard representation. -/
-- Ref: [jones1987]
theorem stdRep3_hecke1 :
    stdRep3_gen1 * stdRep3_gen1 = HA_t • stdRep3_gen1 + 1 := by
  ext i j : 1
  fin_cases i <;> fin_cases j <;>
    simp [stdRep3_gen1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply] <;>
    simp only [HA_t, q_from_t, q_inv_from_t, t, t_inv, sub_mul,
               ← LaurentPolynomial.T_add, Int.reduceAdd, Int.reduceNeg,
               LaurentPolynomial.T_zero] <;>
    ring1

/-! ## §3  Braid relation verification -/

/-- The braid relation σ₀σ₁σ₀ = σ₁σ₀σ₁ in the standard representation. -/
-- Ref: [jones1987]
theorem stdRep3_braid :
    stdRep3_gen0 * stdRep3_gen1 * stdRep3_gen0 =
    stdRep3_gen1 * stdRep3_gen0 * stdRep3_gen1 := by
  ext i j : 1
  fin_cases i <;> fin_cases j <;>
    simp [stdRep3_gen0, stdRep3_gen1, Matrix.mul_apply, Fin.sum_univ_two,
          Matrix.of_apply] <;>
    simp only [q_from_t, q_inv_from_t, t, t_inv, add_mul, neg_mul, one_mul,
               ← LaurentPolynomial.T_add, Int.reduceAdd, Int.reduceNeg,
               LaurentPolynomial.T_zero] <;>
    ring1

/-! ## §3a  T(3, n) center: (σ₀ σ₁)^3 = I in (2,1) — q-independent -/

/-- **Structural identity** (PR derivation 2026-05-24): in the standard
    (2,1) representation of H₃(q), the cube of σ₀σ₁ is the identity
    matrix, exactly, for all q.

    Direct consequence: the matrix M = σ₀σ₁ has minimal polynomial
    X² + X + 1, whose roots are the primitive cube roots of unity
    e^{±2πi/3} = −1/2 ± i√3/2.  These eigenvalues are q-independent.

    **Corollary for T(3, n) torus knots.**  The braid word for the
    T(3, n) torus knot family is (σ₀σ₁)^n in B₃.  The (2,1) character
    is therefore
        χ^{(2,1)}((σ₀σ₁)^n)  =  2 cos(2πn/3)  ∈  {−1, −1, +2}
    cyclically with n mod 3 — **q-independent**.

    This means the Fibonacci/Chebyshev-of-second-kind h-polynomial
    pattern proved for T(2, 2m) in H₂(q) (PR #1165) does NOT extend
    to T(3, n) via the (2,1) channel of H₃(q): the (2,1) contribution
    is a pure 3-cycle character with no h-dependence.

    The non-trivial q-dependence of J_{T(3, n)}(q) lives entirely in
    the trivial (q^{2n}) and sign (q^{-2n}) Wedderburn channels.

    **Computational provenance**: sympy-verified at q symbolic in
    [`folio-assistant/computations/probes/t3n_binomial_pattern_probe.py`]. -/
-- Ref: [jones1987]
theorem stdRep3_M_cubed_eq_one :
    (stdRep3_gen0 * stdRep3_gen1) ^ 3 = (1 : TMatrix) := by
  -- Unfold M^3 into an explicit triple product so `simp` can chew it
  -- with `Matrix.mul_apply` + `Fin.sum_univ_two`.
  rw [show (3 : ℕ) = 2 + 1 from rfl, pow_succ, sq]
  ext i j : 1
  fin_cases i <;> fin_cases j <;>
    simp [stdRep3_gen0, stdRep3_gen1, Matrix.mul_apply, Fin.sum_univ_two,
          Matrix.of_apply] <;>
    simp only [q_from_t, q_inv_from_t, t, t_inv, mul_add, add_mul, neg_mul,
               mul_neg, mul_one, one_mul, ← LaurentPolynomial.T_add,
               Int.reduceAdd, Int.reduceNeg, LaurentPolynomial.T_zero] <;>
    ring1

/-! ## §3b  Borromean (2,1) character — named definition + structural properties

  This section names χ^{(2,1)}(β_Bor) for the standard 6-crossing
  Borromean braid β_Bor = (σ₀ σ₁⁻¹)^3 ∈ B₃ and proves the basic
  algebraic structure (it's the trace of a specific matrix product).

  The EXPLICIT POLYNOMIAL FORM in q is
      χ^{(2,1)}(β_Bor)  =  −q⁶ + 3q⁴ − 3q² + 4 − 3/q² + 3/q⁴ − 1/q⁶
  which expands in h = q − q⁻¹ to
      χ^{(2,1)}(β_Bor)(h)  =  2 − 3h⁴ − h⁶  (exact, finite-degree 6 polynomial)

  Sympy-verified in `folio-assistant/computations/crystal_yekutieli_probes_abcd.py`
  (PR #1233 probe B). The Lean theorem stating this polynomial equality
  would require the q-form to be written in the t-parameter algebra
  (HA_t / q_from_t machinery), which is non-trivial; this section just
  names the character as a `noncomputable def` and proves basic
  structural facts that don't require the polynomial RHS.

  **Wedderburn context**: combined with χ^{(3)}(β_Bor) = 1 (trivial rep)
  and χ^{(1,1,1)}(β_Bor) = 1 (sign rep), this gives the per-irrep
  decomposition of the Borromean Markov trace at H_3(q). -/

/-- The (2,1) Wedderburn character of the Borromean braid β_Bor =
    (σ₀ σ₁⁻¹)^3 ∈ B₃.

    Computed by: forming the matrix M = σ₀ · σ₁⁻¹ in (2,1), cubing it,
    and taking the trace. -/
noncomputable def stdRep3_chi_borromean : R_t :=
  ((stdRep3_gen0 * stdRep3_genInv1) ^ 3).trace

/-- The (2,1) Borromean character is the trace of an explicit triple
    product of 2×2 matrices in the standard rep — a finite expression
    in the t-parameter algebra (no `sorry` needed for the definition). -/
theorem stdRep3_chi_borromean_eq_trace :
    stdRep3_chi_borromean =
      ((stdRep3_gen0 * stdRep3_genInv1) *
       (stdRep3_gen0 * stdRep3_genInv1) *
       (stdRep3_gen0 * stdRep3_genInv1)).trace := by
  unfold stdRep3_chi_borromean
  rw [show (3 : ℕ) = 2 + 1 from rfl, pow_succ, sq]

/-! ## §4  HeckeRep instance -/

/-- The standard (2,1) representation of H₃(q) as a `HeckeRep` instance. -/
noncomputable def stdRep3 : HeckeRep 3 2 where
  gen i := match i with
    | ⟨0, _⟩ => stdRep3_gen0
    | ⟨1, _⟩ => stdRep3_gen1
  hecke_rel i := by
    match i with
    | ⟨0, _⟩ => exact stdRep3_hecke0
    | ⟨1, _⟩ => exact stdRep3_hecke1
  braid_adj i hi₀ hi₁ := by
    -- Only case: i = 0, i + 1 = 1
    have : i = 0 := by omega
    subst this
    simp only
    exact stdRep3_braid
  braid_far i j hij := by
    -- For H₃(q), no pair (i, j) in Fin 2 has distance ≥ 2
    exact absurd hij (by omega)

/-! ## §5  Half-Borromean matrices -/

/-- The three color-tube half-Borromean matrices in the standard
    representation.

    Each half-Borromean corresponds to one of the 3 color tubes
    of the exceptional divisor on Σ₄:

    - h₀₁ = σ₀⁻¹ σ₁ σ₀ σ₁⁻¹   (adjacent pair, standard)
    - h₁₂ = σ₁⁻¹ σ₀ σ₁ σ₀⁻¹   (adjacent pair, swapped)
    - h₀₂ = σ₀⁻¹ σ₁⁻¹ σ₀ σ₁   (non-adjacent pair, conjugated) -/
inductive ColorTube where
  | rg : ColorTube  -- red-green (strands 0-1)
  | gb : ColorTube  -- green-blue (strands 1-2)
  | rb : ColorTube  -- red-blue (strands 0-2, non-adjacent)
deriving DecidableEq, Repr

/-- The half-Borromean matrix for each color tube. -/
noncomputable def halfBorromeanStd : ColorTube → TMatrix
  | .rg => stdRep3_genInv0 * stdRep3_gen1 * stdRep3_gen0 * stdRep3_genInv1
  | .gb => stdRep3_genInv1 * stdRep3_gen0 * stdRep3_gen1 * stdRep3_genInv0
  | .rb => stdRep3_genInv0 * stdRep3_genInv1 * stdRep3_gen0 * stdRep3_gen1

/-- The Borromean color average in the standard representation:
    `β_color = ⅓(h₀₁ + h₁₂ + h₀₂)`.

    Since we work over ℤ[t, t⁻¹] (no division by 3), we store
    the UN-AVERAGED sum.  The factor of 3 is handled in the ratio
    computation (it cancels between numerator and denominator when
    both channels use the same average). -/
noncomputable def borromeanColorSum : TMatrix :=
  halfBorromeanStd .rg + halfBorromeanStd .gb + halfBorromeanStd .rb

/-! ## §6  Symmetric representation traces -/

/-- Every half-Borromean evaluates to the identity in the trivial representation.

    In the trivial rep, σ_i ↦ q · I, σ_i⁻¹ ↦ q⁻¹ · I.
    So h_{ij} = σ_i⁻¹ σ_j σ_i σ_j⁻¹ ↦ q⁻¹ · q · q · q⁻¹ · I = I.

    This holds because every half-Borromean is a commutator, and
    any commutator is trivial in a 1-dimensional (abelian)
    representation. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem halfBorromean_trivial_eval (n : ℕ) (i j : Fin (n - 1)) :
    (trivRep n).halfBorromeanMat i j = 1 := by
  -- Scalar identity first: (q − HA)·q·q·(q − HA) = q⁻¹·q·q·q⁻¹ = 1,
  -- closed by `linear_combination` against `q·q⁻¹ = 1` (NOT by `ring`:
  -- the relation `t·t⁻¹ = 1` is an `AddMonoidAlgebra` fact, see §1a).
  have hscalar : (q_from_t - HA_t) * (q_from_t * (q_from_t * (q_from_t - HA_t)))
      = (1 : R_t) := by
    rw [q_from_t_sub_HA_t]
    linear_combination (q_from_t * q_inv_from_t + 1) * q_from_t_mul_q_inv_from_t
  simp [HeckeRep.halfBorromeanMat, HeckeRep.genInv, trivRep, ← sub_smul]
  -- Goal: (q − HA) • q • q • (q − HA) • 1 = 1.  Fold the smul chain
  -- into one scalar, then discharge it with `hscalar`.
  simp only [smul_smul]
  rw [hscalar, one_smul]

/-- Every conjugated half-Borromean also evaluates to the identity
    in the trivial representation (same reasoning: commutator in
    abelian rep). -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem halfBorromeanConj_trivial_eval (n : ℕ) (i j : Fin (n - 1)) :
    (trivRep n).halfBorromeanConjMat i j = 1 := by
  -- Scalar identity: q·q·(q − HA)·(q − HA) = q·q·q⁻¹·q⁻¹ = 1 (see §1a);
  -- stated in the operand order simp produces in the smul chain below.
  have hscalar : q_from_t * (q_from_t * ((q_from_t - HA_t) * (q_from_t - HA_t)))
      = (1 : R_t) := by
    rw [q_from_t_sub_HA_t]
    linear_combination (q_from_t * q_inv_from_t + 1) * q_from_t_mul_q_inv_from_t
  simp [HeckeRep.halfBorromeanConjMat, HeckeRep.genInv, trivRep, ← sub_smul]
  -- Goal: q • q • (q − HA) • (q − HA) • 1 = 1.
  simp only [smul_smul]
  rw [hscalar, one_smul]

/-! ## §7  Axial coupling ratio (symbolic) -/

/-- The standard representation trace of the Borromean color sum.

    `tr_std(h₀₁ + h₁₂ + h₀₂)` as an element of `ℤ[t, t⁻¹]`. -/
noncomputable def borromeanColorSum_stdTrace : R_t :=
  borromeanColorSum.trace

/-- The trivial representation trace of the Borromean color sum.

    Each half-Borromean evaluates to 1 in the trivial rep,
    so the sum is 3. -/
noncomputable def borromeanColorSum_trivTrace : R_t := 3

/-- The axial coupling ratio (over the fraction field):

    `g_A / g_V = (5/3) × |tr_std(β_color)| / |tr_sym(β_color)|`

    In the fraction field of `ℤ[t, t⁻¹]`, the ratio
    `tr_std / (3)` is computed exactly.

    The 5/3 prefactor (naive quark model) and absolute value
    are applied in the numerical evaluation (Chapter 7).

    Here we compute the algebraic ratio:
    `r(q) = tr_std(h₀₁ + h₁₂ + h₀₂) / 3`

    which is an element of the fraction field. -/
noncomputable def axialCouplingAlgebraic : FractionRing R_t :=
  algebraMap R_t (FractionRing R_t) borromeanColorSum_stdTrace /
    algebraMap R_t (FractionRing R_t) borromeanColorSum_trivTrace

end QOU.Archimedean
