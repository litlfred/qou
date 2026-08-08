import QOU.Machinery.HeckeH3AlgebraInstance
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH3BlockRep — the (2,1) two-dimensional block of H₃(q)

Wenzl-bridge **stage 2c-2** (bean `qou-vndn`, epic `qou-otbb`): the
two-dimensional Hoefsmit seminormal representation of `H3A`, completing
the block *data* of the rank-3 Wedderburn picture
$H_3(q) \cong K \times K \times M_2(K)$ (the two characters are
`HeckeH3Characters`; this file supplies the $M_2$ block).

Convention: base field $K$, $q \neq 0$, Hecke parameter
$h = q - q^{-1}$ (eigenvalues $q$ and $-q^{-1}$).  The genericity
denominator is $[2]_q$-type: $q^2 + 1 \neq 0$ (equivalently the two
eigenvalues are distinct, $q \neq -q^{-1}$).  The seminormal matrices

$$ S_0 = \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
   \qquad
   S_1 = \begin{pmatrix}
     -\dfrac{1}{q(q^2+1)} & 1 \\[2mm]
     \dfrac{q^4+q^2+1}{(q^2+1)^2} & \dfrac{q^3}{q^2+1}
   \end{pmatrix} $$

satisfy the Hecke quadratic and the braid relation (proved below as
matrix identities), and the induced map on NF coordinates is an
algebra homomorphism `blockRep : H3A K (q - q⁻¹) →ₐ[K] M₂(K)` —
multiplicativity by the same structured route as the characters
(right-action intertwiners + right-linearity of `mulNF`).

Over $\mathbb{R}$ the hypotheses hold for **every** $q \neq 0$
($q^2 + 1 > 0$), so the real block is unconditional — same pattern as
`HeckeH2WedderburnReal`.  What remains for the full rank-3 Wedderburn
*isomorphism* is bijectivity of the assembled map
$(\chi_+, \chi_-, \rho)$ — the six-dimensional linear inversion —
tracked in bean `qou-vndn`.

Base ring (§7c): generic `[Field K]` — inverses are genuinely used;
no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Machinery.H3

variable {K : Type*} [Field K]

/-- The diagonal seminormal generator: $S_0 = \mathrm{diag}(q, -q^{-1})$. -/
noncomputable def S0 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  Matrix.of ![![q, 0], ![0, -q⁻¹]]

/-- The mixing seminormal generator $S_1$ (entries rational in $q$ over
    the genericity denominator $q^2+1$). -/
noncomputable def S1 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  Matrix.of ![![-(1 / (q * (q ^ 2 + 1))), 1],
              ![(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1)]]

/-- $S_0$ satisfies the Hecke quadratic $S^2 = (q - q^{-1})S + 1$
    (sorry-free). -/
theorem S0_hecke (q : K) (hq : q ≠ 0) :
    S0 q * S0 q = (q - q⁻¹) • S0 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]
  all_goals try field_simp
  all_goals try ring

/-- $S_1$ satisfies the Hecke quadratic (sorry-free). -/
theorem S1_hecke (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S1 q * S1 q = (q - q⁻¹) • S1 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]
  all_goals try field_simp
  all_goals try ring

/-- The braid relation $S_0 S_1 S_0 = S_1 S_0 S_1$ (sorry-free). -/
theorem S0_S1_braid (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    S0 q * S1 q * S0 q = S1 q * S0 q * S1 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [S0, S1, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals try field_simp
  all_goals try ring

/-- The block map on NF coordinates: each basis word goes to the
    corresponding word in $S_0, S_1$ (basis
    `[γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`). -/
noncomputable def blockOf (q : K) (v : Fin 6 → K) :
    Matrix (Fin 2) (Fin 2) K :=
  v 0 • 1 + v 1 • S0 q + v 2 • S1 q + v 3 • (S1 q * S0 q)
    + v 4 • (S0 q * S1 q) + v 5 • (S0 q * S1 q * S0 q)

/-- The block map intertwines the right `σ₀`-action with right
    multiplication by $S_0$ (sorry-free). -/
theorem blockOf_mulσ₀ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (u : Fin 6 → K) :
    blockOf q (mulσ₀ (q - q⁻¹) u) = blockOf q u * S0 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [blockOf, S0, S1, mulσ₀, Matrix.mul_apply, Fin.sum_univ_two,
        Matrix.one_apply]
  all_goals try field_simp
  all_goals try ring

/-- The block map intertwines the right `σ₁`-action with right
    multiplication by $S_1$ (sorry-free). -/
theorem blockOf_mulσ₁ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (u : Fin 6 → K) :
    blockOf q (mulσ₁ (q - q⁻¹) u) = blockOf q u * S1 q := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [blockOf, S0, S1, mulσ₁, Matrix.mul_apply, Fin.sum_univ_two,
        Matrix.one_apply]
  all_goals try field_simp
  all_goals try ring

/-- **Multiplicativity of the block map on the full NF product
    (sorry-free)** — expand `mulNF` by right-linearity, reduce each
    basis-word action with the two intertwiners (the same structured
    route as `chiNF_mulNF`). -/
theorem blockOf_mulNF (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (u v : Fin 6 → K) :
    blockOf q (mulNF (q - q⁻¹) u v) = blockOf q u * blockOf q v := by
  have e : blockOf q (mulNF (q - q⁻¹) u v) =
      v 0 • blockOf q u
      + v 1 • blockOf q (mulσ₀ (q - q⁻¹) u)
      + v 2 • blockOf q (mulσ₁ (q - q⁻¹) u)
      + v 3 • blockOf q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u))
      + v 4 • blockOf q (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u))
      + v 5 • blockOf q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u))) := by
    ext i j
    fin_cases i <;> fin_cases j
    all_goals simp [blockOf, mulNF, Matrix.one_apply]
    all_goals try ring
  rw [e]
  simp only [blockOf_mulσ₀ q hq h2, blockOf_mulσ₁ q hq h2]
  simp only [blockOf, Matrix.mul_add, Matrix.mul_smul, Matrix.mul_one]
  simp only [Matrix.mul_assoc]

namespace H3A

/-- **The (2,1) two-dimensional block representation (sorry-free).**
    The algebra homomorphism `H₃(q) →ₐ M₂(K)` induced by the seminormal
    matrices; with the two characters of `HeckeH3Characters` this
    completes the block *data* of
    $H_3(q) \cong K \times K \times M_2(K)$. -/
noncomputable def blockRep (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    H3A K (q - q⁻¹) →ₐ[K] Matrix (Fin 2) (Fin 2) K where
  toFun x := blockOf q x.v
  map_one' := by
    show blockOf q unitNF = 1
    simp [blockOf, unitNF]
  map_mul' x y := blockOf_mulNF q hq h2 x.v y.v
  map_zero' := by
    show blockOf q 0 = 0
    simp [blockOf]
  map_add' x y := by
    show blockOf q (x.v + y.v) = blockOf q x.v + blockOf q y.v
    ext i j
    fin_cases i <;> fin_cases j
    all_goals simp [blockOf, Matrix.one_apply]
    all_goals try ring
  commutes' c := by
    show blockOf q ((c • (1 : H3A K (q - q⁻¹))).v) = _
    rw [smul_v, one_v]
    ext i j
    fin_cases i <;> fin_cases j
    all_goals simp [blockOf, unitNF, Matrix.algebraMap_matrix_apply, Matrix.one_apply, Algebra.algebraMap_self_apply]

end H3A

end QOU.Machinery.H3
