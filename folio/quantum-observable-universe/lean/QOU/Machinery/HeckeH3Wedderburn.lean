import QOU.Machinery.HeckeH3Characters
import QOU.Machinery.HeckeH3BlockRep

/-!
# QOU.Machinery.HeckeH3Wedderburn — the full rank-3 Wedderburn isomorphism

Wenzl-bridge **stage 2c-3** (bean `qou-vndn`, epic `qou-otbb`): the
assembled explicit isomorphism

$$ H_3(q) \;\cong\; K \times K \times M_2(K) $$

from the two characters (`HeckeH3Characters`) and the $(2,1)$ block
(`HeckeH3BlockRep`).  The inverse was computed symbolically (sympy,
6×6 inversion over $\mathbb{Q}(q)$) and is **verified here by Lean**
— nothing is trusted from the computation; the determinant of the
coordinate map is

$$ \det = \frac{(q^2+1)\,(q^2-q+1)^3\,(q^2+q+1)^3}{q^7}, $$

so the degeneracy locus is exactly the Wenzl genericity condition at
rank 3: the hypotheses are $q \neq 0$, $q^2 + 1 \neq 0$ ($[2]$-type)
and $q^4 + q^2 + 1 = (q^2+q+1)(q^2-q+1) \neq 0$ ($[3]$-type).  Over
$\mathbb{R}$ all three hold for every $q \notin \{0, \pm 1\}$… indeed
$q^2+1 > 0$ and $q^4+q^2+1 > 0$ always, so only $q \neq 0$ remains.

**Semisimplicity note (honest):** Mathlib currently lists
`IsSemisimpleRing (Matrix ι ι R)` as `proof_wanted`
(`RingTheory/SimpleModule/Basic.lean`), so the `IsSemisimpleRing`
Prop for $H_3(q)$ cannot yet be obtained by transfer.  The explicit
isomorphism below *is* the Wedderburn decomposition — strictly more
informative — and the Prop-level corollary lands the day the Mathlib
gap closes.

Base ring (§7c): generic `[Field K]`; no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU.Machinery.H3

variable {K : Type*} [Field K]

/-- `q` is a root of the Hecke quadratic at `h = q - q⁻¹` (sorry-free). -/
theorem root_q (q : K) (hq : q ≠ 0) : q * q = (q - q⁻¹) * q + 1 := by
  field_simp
  all_goals ring

/-- `-q⁻¹` is the other root (sorry-free). -/
theorem root_negInv (q : K) (hq : q ≠ 0) :
    (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by
  field_simp
  all_goals ring

/-- **The assembled Wedderburn homomorphism**
    $(\chi_+, \chi_-, \rho) : H_3(q) \to K \times K \times M_2(K)$
    (sorry-free). -/
noncomputable def wedderburnHom (q : K) (hq : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) :
    H3A K (q - q⁻¹) →ₐ[K] K × K × Matrix (Fin 2) (Fin 2) K where
  toFun x := (chiNF q x.v, chiNF (-q⁻¹) x.v, blockOf q x.v)
  map_one' := by
    refine Prod.ext ?_ (Prod.ext ?_ ?_)
    · show chiNF q (unitNF (R := K)) = 1
      simp
    · show chiNF (-q⁻¹) (unitNF (R := K)) = 1
      simp
    · show blockOf q (unitNF (R := K)) = 1
      simp [blockOf, unitNF]
  map_mul' x y := by
    refine Prod.ext ?_ (Prod.ext ?_ ?_)
    · exact chiNF_mulNF (q - q⁻¹) q (root_q q hq) x.v y.v
    · exact chiNF_mulNF (q - q⁻¹) (-q⁻¹) (root_negInv q hq) x.v y.v
    · exact blockOf_mulNF q hq h2 x.v y.v
  map_zero' := by
    refine Prod.ext ?_ (Prod.ext ?_ ?_)
    · show chiNF q (0 : Fin 6 → K) = 0
      simp [chiNF]
    · show chiNF (-q⁻¹) (0 : Fin 6 → K) = 0
      simp [chiNF]
    · show blockOf q (0 : Fin 6 → K) = 0
      simp [blockOf]
  map_add' x y := by
    refine Prod.ext ?_ (Prod.ext ?_ ?_)
    · show chiNF q (x.v + y.v) = chiNF q x.v + chiNF q y.v
      simp [chiNF]
      ring
    · show chiNF (-q⁻¹) (x.v + y.v) = _
      simp [chiNF]
      ring
    · show blockOf q (x.v + y.v) = blockOf q x.v + blockOf q y.v
      ext i j
      fin_cases i <;> fin_cases j
      all_goals simp [blockOf, Matrix.one_apply]
      all_goals try ring
  commutes' c := by
    show (chiNF q ((c • (1 : H3A K (q - q⁻¹))).v),
          chiNF (-q⁻¹) ((c • (1 : H3A K (q - q⁻¹))).v),
          blockOf q ((c • (1 : H3A K (q - q⁻¹))).v)) = _
    rw [H3A.smul_v, H3A.one_v, Algebra.algebraMap_eq_smul_one]
    refine Prod.ext ?_ (Prod.ext ?_ ?_)
    · show chiNF q (c • unitNF) = c • (1 : K)
      simp [chiNF, unitNF]
    · show chiNF (-q⁻¹) (c • unitNF) = c • (1 : K)
      simp [chiNF, unitNF]
    · show blockOf q (c • unitNF) = c • (1 : Matrix (Fin 2) (Fin 2) K)
      ext i j
      fin_cases i <;> fin_cases j
      all_goals simp [blockOf, unitNF, Matrix.one_apply]

/-- The inverse coordinate map, computed symbolically over
    $\mathbb{Q}(q)$ and verified by the inverse lemmas below. -/
noncomputable def wedderburnInvV (q s t : K)
    (M : Matrix (Fin 2) (Fin 2) K) : Fin 6 → K :=
  ![ (s + q ^ 6 * t) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
       + q ^ 2 * (M 0 0 + M 1 1) / (q ^ 4 + q ^ 2 + 1),
     (q * s - q ^ 5 * t) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
       + (q ^ 3 * M 0 0 - q * M 1 1) / (q ^ 4 + q ^ 2 + 1),
     (q * s - q ^ 5 * t - q * M 0 0 + q ^ 5 * M 1 1) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
       + q ^ 2 * M 0 1 / (q ^ 2 + 1) ^ 2 + q ^ 2 * M 1 0 / (q ^ 4 + q ^ 2 + 1),
     (q ^ 2 * s + q ^ 4 * t - q ^ 2 * M 0 0 - q ^ 4 * M 1 1) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
       - q * M 0 1 / (q ^ 2 + 1) ^ 2 + q ^ 3 * M 1 0 / (q ^ 4 + q ^ 2 + 1),
     (q ^ 2 * s + q ^ 4 * t - q ^ 2 * M 0 0 - q ^ 4 * M 1 1) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
       + q ^ 3 * M 0 1 / (q ^ 2 + 1) ^ 2 - q * M 1 0 / (q ^ 4 + q ^ 2 + 1),
     (q ^ 3 * s - q ^ 3 * t - q ^ 3 * M 0 0 + q ^ 3 * M 1 1) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
       - q ^ 2 * M 0 1 / (q ^ 2 + 1) ^ 2 - q ^ 2 * M 1 0 / (q ^ 4 + q ^ 2 + 1) ]

/-- Explicit entry formulas for the block map (sorry-free; proved once
    so the inverse lemmas below stay purely scalar). -/
theorem blockOf_apply₀₀ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (v : Fin 6 → K) :
    blockOf q v 0 0 = v 0 + q * v 1 - v 2 / (q * (q ^ 2 + 1))
      - v 3 / (q ^ 2 + 1) - v 4 / (q ^ 2 + 1) - q * v 5 / (q ^ 2 + 1) := by
  simp [blockOf, S0, S1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]
  field_simp
  ring

theorem blockOf_apply₀₁ (q : K) (hq : q ≠ 0) (v : Fin 6 → K) :
    blockOf q v 0 1 = v 2 - v 3 / q + q * v 4 - v 5 := by
  simp [blockOf, S0, S1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]
  field_simp
  ring

theorem blockOf_apply₁₀ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (v : Fin 6 → K) :
    blockOf q v 1 0 = (q ^ 4 + q ^ 2 + 1) * (v 2 + q * v 3) / (q ^ 2 + 1) ^ 2
      - (q ^ 4 + q ^ 2 + 1) * v 4 / (q * (q ^ 2 + 1) ^ 2)
      - (q ^ 4 + q ^ 2 + 1) * v 5 / (q ^ 2 + 1) ^ 2 := by
  simp [blockOf, S0, S1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]
  field_simp
  ring

theorem blockOf_apply₁₁ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (v : Fin 6 → K) :
    blockOf q v 1 1 = v 0 - v 1 / q + q ^ 3 * v 2 / (q ^ 2 + 1)
      - q ^ 2 * v 3 / (q ^ 2 + 1) - q ^ 2 * v 4 / (q ^ 2 + 1)
      + q * v 5 / (q ^ 2 + 1) := by
  simp [blockOf, S0, S1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]
  field_simp
  ring

/-- **Left inverse on coordinates (sorry-free):** the inverse formulas
    recover every NF coordinate from the character/block triple. -/
theorem wedderburnInvV_left (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (v : Fin 6 → K) :
    wedderburnInvV q (chiNF q v) (chiNF (-q⁻¹) v) (blockOf q v) = v := by
  have h2' : (1 : K) + q ^ 2 ≠ 0 := fun h => h2 (by linear_combination h)
  have h3' : (1 : K) + q ^ 2 + q ^ 4 ≠ 0 := fun h => h3 (by linear_combination h)
  have h00 := blockOf_apply₀₀ q hq h2 v
  have h01 := blockOf_apply₀₁ q hq v
  have h10 := blockOf_apply₁₀ q hq h2 v
  have h11 := blockOf_apply₁₁ q hq h2 v
  have hA := mul_inv_cancel₀ h3'
  funext i
  fin_cases i
  all_goals simp [wedderburnInvV, chiNF, h00, h01, h10, h11]
  all_goals field_simp [hq, h2', h3']
  · linear_combination (v 0 + v 0 * q ^ 2) * hA
  · linear_combination (v 1 + v 1 * q ^ 2) * hA
  · linear_combination (v 2 + q * v 3 + v 2 * q ^ 2 + v 2 * q ^ 4 + v 5 * q ^ 2 - v 4 * q ^ 3) * hA
  · linear_combination (q * v 2 + v 3 * q ^ 4 + v 4 * q ^ 2 - q * v 5 + 2 * v 3 * q ^ 2) * hA
  · linear_combination (v 4 + v 3 * q ^ 2 + v 5 * q ^ 3 - v 2 * q ^ 3 + 2 * v 4 * q ^ 2) * hA
  · linear_combination (v 5 + v 2 * q ^ 2 + v 4 * q ^ 3 + v 5 * q ^ 2 + v 5 * q ^ 4 - q * v 3) * hA

/-- **Right inverse, first character (sorry-free).** -/
theorem chiNF_wedderburnInvV_plus (q : K) (hq : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (s t : K)
    (M : Matrix (Fin 2) (Fin 2) K) :
    chiNF q (wedderburnInvV q s t M) = s := by
  have h2' : (1 : K) + q ^ 2 ≠ 0 := fun h => h2 (by linear_combination h)
  have h3' : (1 : K) + q ^ 2 + q ^ 4 ≠ 0 := fun h => h3 (by linear_combination h)
  simp [wedderburnInvV, chiNF]
  field_simp [hq, h2', h3']
  linear_combination (s * (1 + 2 * q ^ 2 + q ^ 4)) * mul_inv_cancel₀ h3'

/-- **Right inverse, second character (sorry-free).** -/
theorem chiNF_wedderburnInvV_minus (q : K) (hq : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (s t : K)
    (M : Matrix (Fin 2) (Fin 2) K) :
    chiNF (-q⁻¹) (wedderburnInvV q s t M) = t := by
  have h2' : (1 : K) + q ^ 2 ≠ 0 := fun h => h2 (by linear_combination h)
  have h3' : (1 : K) + q ^ 2 + q ^ 4 ≠ 0 := fun h => h3 (by linear_combination h)
  simp [wedderburnInvV, chiNF]
  field_simp [hq, h2', h3']
  linear_combination (t * q * (1 + 2 * q ^ 2 + q ^ 4)) * mul_inv_cancel₀ h3'

/-- **Right inverse, matrix block (sorry-free).** -/
theorem blockOf_wedderburnInvV (q : K) (hq : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (s t : K)
    (M : Matrix (Fin 2) (Fin 2) K) :
    blockOf q (wedderburnInvV q s t M) = M := by
  have h2' : (1 : K) + q ^ 2 ≠ 0 := fun h => h2 (by linear_combination h)
  have h3' : (1 : K) + q ^ 2 + q ^ 4 ≠ 0 := fun h => h3 (by linear_combination h)
  have hA := mul_inv_cancel₀ h3'
  ext i j
  fin_cases i <;> fin_cases j
  · show blockOf q (wedderburnInvV q s t M) 0 0 = M 0 0
    rw [blockOf_apply₀₀ q hq h2]
    simp [wedderburnInvV]
    field_simp [hq, h2', h3']
    linear_combination (M 0 0 * (1 + 3 * q ^ 2 + 3 * q ^ 4 + q ^ 6)) * hA
  · show blockOf q (wedderburnInvV q s t M) 0 1 = M 0 1
    rw [blockOf_apply₀₁ q hq]
    simp [wedderburnInvV]
    field_simp [hq, h2', h3']
    ring
  · show blockOf q (wedderburnInvV q s t M) 1 0 = M 1 0
    rw [blockOf_apply₁₀ q hq h2]
    simp [wedderburnInvV]
    field_simp [hq, h2', h3']
    linear_combination (M 1 0 * (1 + 4 * q ^ 2 + 6 * q ^ 4 + 4 * q ^ 6 + q ^ 8)) * hA
  · show blockOf q (wedderburnInvV q s t M) 1 1 = M 1 1
    rw [blockOf_apply₁₁ q hq h2]
    simp [wedderburnInvV]
    field_simp [hq, h2', h3']
    linear_combination (M 1 1 * (1 + 3 * q ^ 2 + 3 * q ^ 4 + q ^ 6)) * hA

/-- **The rank-3 Wedderburn isomorphism (sorry-free):**
    $H_3(q) \cong K \times K \times M_2(K)$ whenever $q \neq 0$,
    $q^2+1 \neq 0$ and $q^4+q^2+1 \neq 0$ — exactly the Wenzl
    genericity locus at rank 3, read off the determinant. -/
noncomputable def wedderburn₃ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    H3A K (q - q⁻¹) ≃ₐ[K] K × K × Matrix (Fin 2) (Fin 2) K :=
  AlgEquiv.ofBijective (wedderburnHom q hq h2) <| by
    constructor
    · -- injective via the coordinate left inverse
      intro x y hxy
      apply H3A.ext
      calc x.v = wedderburnInvV q (chiNF q x.v) (chiNF (-q⁻¹) x.v)
                  (blockOf q x.v) := (wedderburnInvV_left q hq h2 h3 x.v).symm
        _ = wedderburnInvV q (chiNF q y.v) (chiNF (-q⁻¹) y.v)
              (blockOf q y.v) := by
              have h1 : chiNF q x.v = chiNF q y.v := congrArg Prod.fst hxy
              have h2' : chiNF (-q⁻¹) x.v = chiNF (-q⁻¹) y.v :=
                congrArg (fun p => p.2.1) hxy
              have h3' : blockOf q x.v = blockOf q y.v :=
                congrArg (fun p => p.2.2) hxy
              rw [h1, h2', h3']
        _ = y.v := wedderburnInvV_left q hq h2 h3 y.v
    · -- surjective via the explicit inverse
      rintro ⟨s, t, M⟩
      refine ⟨⟨wedderburnInvV q s t M⟩, ?_⟩
      refine Prod.ext ?_ (Prod.ext ?_ ?_)
      · exact chiNF_wedderburnInvV_plus q hq h2 h3 s t M
      · exact chiNF_wedderburnInvV_minus q hq h2 h3 s t M
      · exact blockOf_wedderburnInvV q hq h2 h3 s t M

end QOU.Machinery.H3
