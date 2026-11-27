import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum

/-!
# Iterated Confinement Layer Tower, Adiabatic Gap Stability & Toric Chemical Stoichiometry

Formalizes `Q-Gap-0` (`qou-5lct`):

1. **Iterative `ConfinementLayer` and `promoteLayer` Functorial Step:**
   Each physical layer `L_k` (`k = 0, …, 4`) is modeled by an integer conserved-charge matrix
   `A : Matrix (Fin d) (Fin m) ℤ`, an unperturbed column cost vector `c : Fin m → K`, and an
   admissibility predicate (e.g. Reading-3 Frobenius positivity or Pauli `2n²` shell capacity).
   We prove exact LP reduced-cost decomposition, conservation-fiber cost-difference invariance,
   LP weak/strong duality certificates, strict binding-gap positivity for `IsConfinedMotif`, and
   functorial charge conservation under `promoteLayer` (Dantzig–Wolfe column generation).

2. **Adiabatic Confinement Gap Stability & Cross-Layer Deconfinement Flip:**
   If every intra-layer break-up move `g` has unperturbed cost `configCost c_k g ≥ Δ_k > 0` and
   residual Layer-`(k+1)` couplings perturb the move cost by `|δ_V| < Δ_k` (adiabatic ratio
   `η_k = |δ_V| / Δ_k < 1`), then `configCost c_k g + δ_V > 0`: no Layer-`k` bound motif breaks
   apart inside Layer `k+1`. Conversely, when an external chemical potential or Fermi sea drives
   `-δ_V > Δ_k`, the total move cost flips sign (`< 0`), triggering cross-layer transmutation
   (instantiated on neutron-star crust inverse beta capture `p + e⁻ → n + ν_e` at
   `E_{F,e} > m_n - m_p`).

3. **Layer-3 Atomic Shadow Prices = Mulliken Electronegativity & Parr–Pearson Hardness:**
   Right and left discrete electron-count shadow slopes `μ₊(N) = E(N+1) - E(N) = -A_ea(N)` and
   `μ₋(N) = E(N) - E(N-1) = -I(N)` satisfy `η_PP(N) = I(N) - A_ea(N) = μ₊(N) - μ₋(N)`,
   `η_PP(N) ≥ 0 ↔ 2 E(N) ≤ E(N-1) + E(N+1)` (Perdew–Parr–Levy–Balduz discrete convexity),
   `2 χ_Mulliken(N) = -(μ₊(N) + μ₋(N))`, and cumulative Pauli `2n²` period closures produce the
   noble-gas magic numbers `[2, 10, 18, 36, 54, 86]`.

4. **Layer-4 Chemical Stoichiometry, Toric Binomials & Canonical Diophantine Circuits:**
   Atom-count conservation holds iff the signed stoichiometric vector `ν₊ - ν₋` lies in the
   homogeneous integer kernel `Matrix.mulVec A_chem v = 0`, which closes under `ℤ`-linear
   combinations (Hess's law), preserves nuclear elemental inventories along arbitrary reaction
   trajectories, maps every kernel vector to a pure binomial `x^{ν₊} - x^{ν₋}` vanishing on the
   toric parameterization `(Rˣ)^E → R^M`, and yields exact 1D primitive circuits (`gcd = 1`)
   for water synthesis, methane combustion, Haber–Bosch ammonia synthesis, and glucose
   respiration, together with the 4D C–H–O reaction network circuits.

## Base-ring discipline (AGENTS.md §7c)

All algebraic identities are stated over generic `[CommRing K]` (`ℝ`-free); order bounds ask only
for `[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]` (and `[Field K]` solely where division
by `2` or `Δ_k` appears explicitly).

-- Ref: [dantzig-wolfe1960] https://doi.org/10.1287/opre.8.1.101
-- Ref: [benders1962] https://doi.org/10.1007/BF01386316
-- Ref: [deloera-hemmecke-koeppe2013] https://doi.org/10.1137/1.9781611972443
-- Ref: [bloch-horowitz1958] https://doi.org/10.1016/0029-5582(58)90136-6
-- Ref: [schrieffer-wolff1966] https://doi.org/10.1103/PhysRev.149.491
-- Ref: [mulliken1934] https://doi.org/10.1063/1.1749394
-- Ref: [perdew-parr-levy-balduz1982] https://doi.org/10.1103/PhysRevLett.49.1691
-- Ref: [parr-pearson1983] https://doi.org/10.1021/ja00364a005
-- Ref: [horn-jackson1972] https://doi.org/10.1007/BF00251225
-- Ref: [feinberg1972] https://doi.org/10.1007/BF00255665
-- Ref: [craciun-dickenstein-shiu-sturmfels2009] https://doi.org/10.1016/j.jsc.2008.08.006
-/

namespace QOU.MathlibInfra.ConfinementLayerTower

open scoped BigOperators

/-! ## §1. `ConfinementLayer`, Reduced Costs, LP Fiber Invariance & `promoteLayer` -/

/-- A discrete confinement layer over `d` conserved charges and `m` candidate motif columns,
    with integer charge matrix `A`, column cost `c`, and multiplicity admissibility predicate. -/
structure ConfinementLayer (d m : ℕ) (K : Type*) where
  /-- Conserved-charge / stoichiometry matrix `A ∈ ℤ^{d × m}`. -/
  A : Matrix (Fin d) (Fin m) ℤ
  /-- Column cost / unperturbed motif energy vector `c ∈ K^m`. -/
  c : Fin m → K
  /-- Layer admissibility predicate on nonnegative column multiplicities. -/
  admissible : (Fin m → ℕ) → Prop

/-- Cast a nonnegative multiplicity configuration `u : Fin m → ℕ` to `Fin m → ℤ`. -/
def natConfigToInt {m : ℕ} (u : Fin m → ℕ) : Fin m → ℤ :=
  fun j => (u j : ℤ)

/-- Linear cost functional `∑_j z_j · c_j` of a signed integer configuration `z : Fin m → ℤ`. -/
def configCost {m : ℕ} {K : Type*} [CommRing K] (c : Fin m → K) (z : Fin m → ℤ) : K :=
  ∑ j : Fin m, (z j : K) * c j

/-- Dual objective `∑_i b_i · y_i` at conserved charge inventory `b : Fin d → ℤ` and
    shadow-price vector `y : Fin d → K`. -/
def dualObj {d : ℕ} {K : Type*} [CommRing K] (b : Fin d → ℤ) (y : Fin d → K) : K :=
  ∑ i : Fin d, (b i : K) * y i

/-- LP reduced cost `c̄_j(y) := c_j - ∑_i A_{i,j} y_i` of column `j` under shadow prices `y`. -/
def reducedCost {d m : ℕ} {K : Type*} [CommRing K]
    (A : Matrix (Fin d) (Fin m) ℤ) (c : Fin m → K) (y : Fin d → K) (j : Fin m) : K :=
  c j - ∑ i : Fin d, (A i j : K) * y i

theorem configCost_zero {m : ℕ} {K : Type*} [CommRing K] (c : Fin m → K) :
    configCost c (0 : Fin m → ℤ) = 0 := by
  simp [configCost]

theorem configCost_add {m : ℕ} {K : Type*} [CommRing K]
    (c : Fin m → K) (z₁ z₂ : Fin m → ℤ) :
    configCost c (z₁ + z₂) = configCost c z₁ + configCost c z₂ := by
  simp only [configCost, Pi.add_apply, Int.cast_add, add_mul, Finset.sum_add_distrib]

theorem configCost_sub {m : ℕ} {K : Type*} [CommRing K]
    (c : Fin m → K) (z₁ z₂ : Fin m → ℤ) :
    configCost c (z₁ - z₂) = configCost c z₁ - configCost c z₂ := by
  simp only [configCost, Pi.sub_apply, Int.cast_sub, sub_mul, Finset.sum_sub_distrib]

theorem configCost_zsmul {m : ℕ} {K : Type*} [CommRing K]
    (c : Fin m → K) (a : ℤ) (z : Fin m → ℤ) :
    configCost c (a • z) = (a : K) * configCost c z := by
  simp only [configCost, Pi.smul_apply, smul_eq_mul, Int.cast_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl ?_
  intro j _
  ring

theorem configCost_cost_add {m : ℕ} {K : Type*} [CommRing K]
    (c₁ c₂ : Fin m → K) (z : Fin m → ℤ) :
    configCost (c₁ + c₂) z = configCost c₁ z + configCost c₂ z := by
  simp only [configCost, Pi.add_apply, mul_add, Finset.sum_add_distrib]

/-- **LP Lagrangian / reduced-cost decomposition** over any commutative ring `K`:
    `∑_j z_j c̄_j(y) = ∑_j z_j c_j - ∑_i (A z)_i y_i`. -/
theorem reduced_cost_decomposition {d m : ℕ} {K : Type*} [CommRing K]
    (A : Matrix (Fin d) (Fin m) ℤ) (c : Fin m → K) (y : Fin d → K) (z : Fin m → ℤ) :
    configCost (reducedCost A c y) z =
      configCost c z - dualObj (Matrix.mulVec A z) y := by
  simp only [configCost, reducedCost, dualObj, Matrix.mulVec, dotProduct]
  have hsub :
      (∑ j : Fin m, (z j : K) * (c j - ∑ i : Fin d, (A i j : K) * y i)) =
        (∑ j : Fin m, (z j : K) * c j) -
          ∑ j : Fin m, ∑ i : Fin d, (z j : K) * ((A i j : K) * y i) := by
    rw [← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl ?_
    intro j _
    rw [mul_sub, Finset.mul_sum]
  rw [hsub]
  congr 1
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl ?_
  intro i _
  push_cast
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl ?_
  intro j _
  ring

/-- **Kernel reduced-cost invariance**: on any charge-neutral move `g ∈ ker_ℤ(A)`,
    reduced cost and bare cost coincide identically for all shadow prices `y`. -/
theorem reduced_cost_eq_cost_on_kernel {d m : ℕ} {K : Type*} [CommRing K]
    (A : Matrix (Fin d) (Fin m) ℤ) (c : Fin m → K) (y : Fin d → K)
    {g : Fin m → ℤ} (hg : Matrix.mulVec A g = 0) :
    configCost (reducedCost A c y) g = configCost c g := by
  rw [reduced_cost_decomposition, hg]
  simp [dualObj]

/-- **Conservation-fiber cost-difference invariance**: two configurations `u, v` in the same
    charge fiber `A u = A v` have identical bare-cost and reduced-cost differences
    `c · (u - v) = c̄(y) · (u - v)`. -/
theorem reduced_cost_fiber_invariance {d m : ℕ} {K : Type*} [CommRing K]
    (A : Matrix (Fin d) (Fin m) ℤ) (c : Fin m → K) (y : Fin d → K)
    {u v : Fin m → ℤ} (huv : Matrix.mulVec A u = Matrix.mulVec A v) :
    configCost (reducedCost A c y) (u - v) = configCost c (u - v) := by
  apply reduced_cost_eq_cost_on_kernel
  rw [Matrix.mulVec_sub, huv, sub_self]

/-- **LP weak duality**: if `u : Fin m → ℕ` satisfies `A u = b` and every column has
    nonnegative reduced cost `0 ≤ c̄_j(y)`, then `b · y ≤ c · u`. -/
theorem lp_weak_duality {d m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (A : Matrix (Fin d) (Fin m) ℤ) (c : Fin m → K) (b : Fin d → ℤ)
    (u : Fin m → ℕ) (y : Fin d → K)
    (hfeas : Matrix.mulVec A (natConfigToInt u) = b)
    (hd : ∀ j : Fin m, 0 ≤ reducedCost A c y j) :
    dualObj b y ≤ configCost c (natConfigToInt u) := by
  have hdec := reduced_cost_decomposition A c y (natConfigToInt u)
  rw [hfeas] at hdec
  have hnn : 0 ≤ configCost (reducedCost A c y) (natConfigToInt u) := by
    unfold configCost natConfigToInt
    refine Finset.sum_nonneg ?_
    intro j _
    rw [Int.cast_natCast]
    exact mul_nonneg (Nat.cast_nonneg (u j)) (hd j)
  linarith

/-- **LP strong-duality / complementary-slackness optimality certificate**: if `u*` and `y*`
    are primal-dual feasible and satisfy complementary slackness `u*_j · c̄_j(y*) = 0`, then
    `c · u* = b · y*` and `u*` minimizes `c · u` over all `u : Fin m → ℕ` in the fiber `A u = b`. -/
theorem lp_optimality_of_complementary_slackness {d m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (A : Matrix (Fin d) (Fin m) ℤ) (c : Fin m → K) (b : Fin d → ℤ)
    (u_star : Fin m → ℕ) (y_star : Fin d → K)
    (hfeas_star : Matrix.mulVec A (natConfigToInt u_star) = b)
    (hd_star : ∀ j : Fin m, 0 ≤ reducedCost A c y_star j)
    (hcs : ∀ j : Fin m, (u_star j : K) * reducedCost A c y_star j = 0) :
    configCost c (natConfigToInt u_star) = dualObj b y_star ∧
      ∀ u : Fin m → ℕ, Matrix.mulVec A (natConfigToInt u) = b →
        configCost c (natConfigToInt u_star) ≤ configCost c (natConfigToInt u) := by
  have hdec := reduced_cost_decomposition A c y_star (natConfigToInt u_star)
  rw [hfeas_star] at hdec
  have hzero : configCost (reducedCost A c y_star) (natConfigToInt u_star) = 0 := by
    unfold configCost natConfigToInt
    refine Finset.sum_eq_zero ?_
    intro j _
    simpa using hcs j
  have heq : configCost c (natConfigToInt u_star) = dualObj b y_star := by
    linarith
  refine ⟨heq, ?_⟩
  intro u hu
  rw [heq]
  exact lp_weak_duality A c b u y_star hu hd_star

/-- `w` is a **confined motif** of layer `L` if it is nonzero, admissible, and strictly
    lower in cost than every nontrivial conserved admissible decomposition `u₁ + u₂`. -/
def ConfinementLayer.IsConfinedMotif {d m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] (L : ConfinementLayer d m K) (w : Fin m → ℕ) : Prop :=
  w ≠ 0 ∧ L.admissible w ∧
    ∀ u₁ u₂ : Fin m → ℕ, u₁ ≠ 0 → u₂ ≠ 0 → L.admissible u₁ → L.admissible u₂ →
      Matrix.mulVec L.A (natConfigToInt w) =
        Matrix.mulVec L.A (natConfigToInt u₁) + Matrix.mulVec L.A (natConfigToInt u₂) →
      configCost L.c (natConfigToInt w) <
        configCost L.c (natConfigToInt u₁) + configCost L.c (natConfigToInt u₂)

/-- Every confined motif has a strictly positive binding gap against any nontrivial admissible
    fission channel `w → u₁ + u₂`. -/
theorem confined_motif_pos_binding_gap {d m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (L : ConfinementLayer d m K) {w u₁ u₂ : Fin m → ℕ}
    (hw : L.IsConfinedMotif w) (hu₁ : u₁ ≠ 0) (hu₂ : u₂ ≠ 0)
    (hadm₁ : L.admissible u₁) (hadm₂ : L.admissible u₂)
    (hcharge : Matrix.mulVec L.A (natConfigToInt w) =
      Matrix.mulVec L.A (natConfigToInt u₁) + Matrix.mulVec L.A (natConfigToInt u₂)) :
    0 < configCost L.c (natConfigToInt u₁ + natConfigToInt u₂) -
          configCost L.c (natConfigToInt w) := by
  have hlt := hw.2.2 u₁ u₂ hu₁ hu₂ hadm₁ hadm₂ hcharge
  rw [configCost_add]
  linarith

/-- Constituent expansion map sending a Layer-`(k+1)` signed motif vector `v : Fin m' → ℤ`
    to its underlying Layer-`k` column vector `∑_α v_α · motifs(α)`. -/
def expandMotifs {m m' : ℕ} (motifs : Fin m' → (Fin m → ℕ)) (v : Fin m' → ℤ) : Fin m → ℤ :=
  fun j => ∑ α : Fin m', v α * (motifs α j : ℤ)

/-- **Functorial Dantzig–Wolfe promotion (`promoteLayer`)**: promote a selected family of
    Layer-`k` motifs `motifs : Fin m' → (Fin m → ℕ)` into the elementary columns of Layer `k+1`,
    inheriting each motif's exact conserved charge vector `A_k (motifs α)` and unperturbed cost
    plus residual inter-motif cost shift `δc`. -/
def promoteLayer {d m m' : ℕ} {K : Type*} [CommRing K]
    (L : ConfinementLayer d m K)
    (motifs : Fin m' → (Fin m → ℕ))
    (δc : Fin m' → K)
    (adm' : (Fin m' → ℕ) → Prop) : ConfinementLayer d m' K where
  A := fun i α => Matrix.mulVec L.A (natConfigToInt (motifs α)) i
  c := fun α => configCost L.c (natConfigToInt (motifs α)) + δc α
  admissible := adm'

/-- **Functorial charge conservation**: the Layer-`(k+1)` charge of `v` equals the Layer-`k`
    charge of its expanded constituent vector `expandMotifs motifs v`. -/
theorem promoteLayer_charge_conservation {d m m' : ℕ} {K : Type*} [CommRing K]
    (L : ConfinementLayer d m K) (motifs : Fin m' → (Fin m → ℕ))
    (δc : Fin m' → K) (adm' : (Fin m' → ℕ) → Prop) (v : Fin m' → ℤ) :
    Matrix.mulVec (promoteLayer L motifs δc adm').A v =
      Matrix.mulVec L.A (expandMotifs motifs v) := by
  ext i
  simp only [promoteLayer, expandMotifs, natConfigToInt, Matrix.mulVec, dotProduct]
  calc
    (∑ α : Fin m', (∑ j : Fin m, L.A i j * (motifs α j : ℤ)) * v α)
        = ∑ α : Fin m', ∑ j : Fin m, L.A i j * (v α * (motifs α j : ℤ)) := by
          refine Finset.sum_congr rfl ?_
          intro α _
          rw [Finset.sum_mul]
          refine Finset.sum_congr rfl ?_
          intro j _
          ring
    _ = ∑ j : Fin m, ∑ α : Fin m', L.A i j * (v α * (motifs α j : ℤ)) := Finset.sum_comm
    _ = ∑ j : Fin m, L.A i j * ∑ α : Fin m', v α * (motifs α j : ℤ) := by
          refine Finset.sum_congr rfl ?_
          intro j _
          rw [← Finset.mul_sum]

/-- **Kernel lifting**: every balanced Layer-`(k+1)` move `v ∈ ker_ℤ(A_{k+1})` expands to an
    exact charge-conserving move `expandMotifs motifs v ∈ ker_ℤ(A_k)` at Layer `k`. -/
theorem promoteLayer_kernel_lifts_to_base_kernel {d m m' : ℕ} {K : Type*} [CommRing K]
    (L : ConfinementLayer d m K) (motifs : Fin m' → (Fin m → ℕ))
    (δc : Fin m' → K) (adm' : (Fin m' → ℕ) → Prop) {v : Fin m' → ℤ}
    (hv : Matrix.mulVec (promoteLayer L motifs δc adm').A v = 0) :
    Matrix.mulVec L.A (expandMotifs motifs v) = 0 := by
  rw [← promoteLayer_charge_conservation L motifs δc adm' v, hv]

/-- At zero cross-motif residual shift (`δc = 0`), Layer-`(k+1)` cost equals the exact
    constituent Layer-`k` cost of `expandMotifs motifs v`. -/
theorem promoteLayer_unperturbed_cost {d m m' : ℕ} {K : Type*} [CommRing K]
    (L : ConfinementLayer d m K) (motifs : Fin m' → (Fin m → ℕ))
    (adm' : (Fin m' → ℕ) → Prop) (v : Fin m' → ℤ) :
    configCost (promoteLayer L motifs 0 adm').c v =
      configCost L.c (expandMotifs motifs v) := by
  simp only [promoteLayer, expandMotifs, natConfigToInt, configCost, Pi.zero_apply, add_zero,
    Int.cast_natCast]
  calc
    (∑ α : Fin m', (v α : K) * ∑ j : Fin m, (motifs α j : K) * L.c j)
        = ∑ α : Fin m', ∑ j : Fin m, ((v α : K) * (motifs α j : K)) * L.c j := by
          refine Finset.sum_congr rfl ?_
          intro α _
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl ?_
          intro j _
          ring
    _ = ∑ j : Fin m, ∑ α : Fin m', ((v α : K) * (motifs α j : K)) * L.c j := Finset.sum_comm
    _ = ∑ j : Fin m, (↑(∑ α : Fin m', v α * (motifs α j : ℤ)) : K) * L.c j := by
          refine Finset.sum_congr rfl ?_
          intro j _
          push_cast
          rw [Finset.sum_mul]


/-! ## §2. Adiabatic Gap Stability & Cross-Layer Deconfinement Flip -/

/-- **Adiabatic confinement gap stability (`η_k < 1`)**: if an intra-layer break-up move `g`
    has unperturbed Layer-`k` cost `configCost c_k g ≥ Δ_k > 0` and Layer-`(k+1)` residual
    coupling perturbs the move cost by `|δ_V| < Δ_k`, then the total move cost remains
    strictly endothermic (`configCost c_k g + δ_V > 0`), preventing cross-layer motif breakup. -/
theorem hierarchical_confinement_of_gap_gt_perturbation {m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (c_k : Fin m → K) (g : Fin m → ℤ) (Δ_k δ_V : K)
    (hgap_pos : 0 < Δ_k)
    (hmove_gap : Δ_k ≤ configCost c_k g)
    (hpert : |δ_V| < Δ_k) :
    0 < configCost c_k g + δ_V := by
  have hneg : -Δ_k < δ_V := (abs_lt.mp hpert).1
  have _ := hgap_pos
  linarith

/-- Vector-perturbation form of adiabatic confinement stability: if `|δc · g| < Δ_k` and
    `Δ_k ≤ c_k · g`, then `(c_k + δc) · g > 0`. -/
theorem hierarchical_confinement_vec {m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (c_k δc : Fin m → K) (g : Fin m → ℤ) (Δ_k : K)
    (hgap_pos : 0 < Δ_k)
    (hmove_gap : Δ_k ≤ configCost c_k g)
    (hpert : |configCost δc g| < Δ_k) :
    0 < configCost (c_k + δc) g := by
  rw [configCost_cost_add]
  exact hierarchical_confinement_of_gap_gt_perturbation c_k g Δ_k (configCost δc g)
    hgap_pos hmove_gap hpert

/-- Ordered-field adiabatic ratio criterion: if `Δ_k > 0`, `Δ_k ≤ c_k · g`, and the
    dimensionless adiabatic ratio `η_k := |δ_V| / Δ_k < 1`, then `c_k · g + δ_V > 0` with
    explicit positive margin `Δ_k * (1 - |δ_V| / Δ_k) ≤ c_k · g + δ_V`. -/
theorem hierarchical_confinement_of_adiabatic_ratio_lt_one {m : ℕ} {K : Type*}
    [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (c_k : Fin m → K) (g : Fin m → ℤ) (Δ_k δ_V : K)
    (hgap_pos : 0 < Δ_k)
    (hmove_gap : Δ_k ≤ configCost c_k g)
    (hratio : |δ_V| / Δ_k < 1) :
    0 < configCost c_k g + δ_V ∧
      Δ_k * (1 - |δ_V| / Δ_k) ≤ configCost c_k g + δ_V := by
  have hne : Δ_k ≠ 0 := ne_of_gt hgap_pos
  have habs : |δ_V| < Δ_k := by
    have hmul : (|δ_V| / Δ_k) * Δ_k < 1 * Δ_k :=
      mul_lt_mul_of_pos_right hratio hgap_pos
    rwa [div_mul_cancel₀ |δ_V| hne, one_mul] at hmul
  have hpos := hierarchical_confinement_of_gap_gt_perturbation c_k g Δ_k δ_V
    hgap_pos hmove_gap habs
  refine ⟨hpos, ?_⟩
  have hmargin : Δ_k * (1 - |δ_V| / Δ_k) = Δ_k - |δ_V| := by
    field_simp [hne]
  rw [hmargin]
  have hle : -|δ_V| ≤ δ_V := neg_abs_le δ_V
  linarith

/-- **Cross-layer deconfinement / transmutation flip (`η_k > 1`)**: when an external chemical
    potential or Fermi-sea pressure drives `-δ_V > Δ_k ≥ configCost c_k g`, the total move
    cost flips sign (`configCost c_k g + δ_V < 0`), making the cross-layer binomial rewrite
    exothermically favorable. -/
theorem cross_layer_flip_of_perturbation_gt_gap {m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (c_k : Fin m → K) (g : Fin m → ℤ) (Δ_k δ_V : K)
    (hmove_le : configCost c_k g ≤ Δ_k)
    (hdriven : Δ_k < -δ_V) :
    configCost c_k g + δ_V < 0 := by
  linarith

/-- Vector-perturbation form of the cross-layer deconfinement flip. -/
theorem cross_layer_flip_vec {m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (c_k δc : Fin m → K) (g : Fin m → ℤ)
    (hdriven : configCost c_k g < -configCost δc g) :
    configCost (c_k + δc) g < 0 := by
  rw [configCost_cost_add]
  linarith

/-- **Neutron-star crust inverse beta capture (`L_3 → L_2` flip)**: for baryon mass gap
    `Δ_np = m_n - m_p` and electron Fermi energy `E_Fe` (`δ_V = -E_Fe`), the cross-layer
    capture `p + e⁻ → n + ν_e` has net cost `(m_n - m_p) - E_Fe`, which is strictly exothermic
    iff `m_n - m_p < E_Fe` and strictly suppressed iff `E_Fe < m_n - m_p`. -/
theorem neutron_star_electron_capture_threshold {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (m_p m_n E_Fe : K) :
    ((m_n - m_p) - E_Fe < 0 ↔ m_n - m_p < E_Fe) ∧
      (0 < (m_n - m_p) - E_Fe ↔ E_Fe < m_n - m_p) := by
  constructor <;> constructor <;> intro h <;> linarith


/-! ## §3. Layer-3 Atomic Shadow Prices: Mulliken Electronegativity & Parr–Pearson Hardness -/

/-- Vertical ionization energy `I(N) := E(N - 1) - E(N)` of an `N`-electron species. -/
def ionizationEnergy {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) : K :=
  E (N - 1) - E N

/-- Electron affinity `A_ea(N) := E(N) - E(N + 1)` of an `N`-electron species. -/
def electronAffinity {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) : K :=
  E N - E (N + 1)

/-- Right discrete LP shadow slope `μ₊(N) := E(N + 1) - E(N)` (electron addition chemical potential). -/
def shadowSlopePlus {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) : K :=
  E (N + 1) - E N

/-- Left discrete LP shadow slope `μ₋(N) := E(N) - E(N - 1)` (electron removal chemical potential). -/
def shadowSlopeMinus {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) : K :=
  E N - E (N - 1)

/-- Parr–Pearson chemical hardness jump `η_PP(N) := I(N) - A_ea(N)`
    (unhalved Perdew–Parr–Levy–Balduz derivative discontinuity `μ₊ - μ₋`; Parr & Pearson 1983
    also tabulate `(I - A_ea) / 2`, differing by an overall factor of `2`). -/
def parrPearsonHardness {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) : K :=
  ionizationEnergy E N - electronAffinity E N

/-- Mulliken absolute electronegativity `χ_M(N) := (I(N) + A_ea(N)) / 2`. -/
def mullikenElectronegativity {K : Type*} [Field K] (E : ℕ → K) (N : ℕ) : K :=
  (ionizationEnergy E N + electronAffinity E N) / 2

theorem shadowSlopePlus_eq_neg_electronAffinity {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) :
    shadowSlopePlus E N = -electronAffinity E N := by
  simp only [shadowSlopePlus, electronAffinity]
  ring

theorem shadowSlopeMinus_eq_neg_ionizationEnergy {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) :
    shadowSlopeMinus E N = -ionizationEnergy E N := by
  simp only [shadowSlopeMinus, ionizationEnergy]
  ring

/-- **Parr–Pearson hardness equals the LP shadow-price discontinuity**:
    `η_PP(N) = I(N) - A_ea(N) = μ₊(N) - μ₋(N)`. -/
theorem parr_pearson_hardness_eq_shadow_jump {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) :
    parrPearsonHardness E N = shadowSlopePlus E N - shadowSlopeMinus E N := by
  simp only [parrPearsonHardness, ionizationEnergy, electronAffinity,
    shadowSlopePlus, shadowSlopeMinus]
  ring

/-- Second-difference expansion of Parr–Pearson hardness:
    `η_PP(N) = E(N - 1) + E(N + 1) - 2 E(N)`. -/
theorem parr_pearson_hardness_eq_second_diff {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) :
    parrPearsonHardness E N = E (N - 1) + E (N + 1) - 2 * E N := by
  simp only [parrPearsonHardness, ionizationEnergy, electronAffinity]
  ring

/-- **Division-free Mulliken shadow-price identity** over any `[CommRing K]`:
    `I(N) + A_ea(N) = -(μ₊(N) + μ₋(N)) = E(N - 1) - E(N + 1)`. -/
theorem neg_shadow_sum_eq_ionization_add_affinity {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) :
    -(shadowSlopePlus E N + shadowSlopeMinus E N) =
      ionizationEnergy E N + electronAffinity E N := by
  simp only [shadowSlopePlus, shadowSlopeMinus, ionizationEnergy, electronAffinity]
  ring

/-- **Mulliken electronegativity equals minus the midpoint of right/left shadow slopes**:
    `2 * χ_Mulliken(N) = -(μ₊(N) + μ₋(N))`. -/
theorem two_mul_mulliken_eq_neg_shadow_sum {K : Type*} [Field K]
    (E : ℕ → K) (N : ℕ) (h2 : (2 : K) ≠ 0) :
    2 * mullikenElectronegativity E N = -(shadowSlopePlus E N + shadowSlopeMinus E N) := by
  unfold mullikenElectronegativity
  rw [mul_div_cancel₀ _ h2, neg_shadow_sum_eq_ionization_add_affinity]

/-- **Perdew–Parr–Levy–Balduz discrete convexity equivalence**:
    `0 ≤ η_PP(N) ↔ 2 * E(N) ≤ E(N - 1) + E(N + 1)`. -/
theorem parr_pearson_hardness_nonneg_iff_convex {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (E : ℕ → K) (N : ℕ) :
    0 ≤ parrPearsonHardness E N ↔ 2 * E N ≤ E (N - 1) + E (N + 1) := by
  rw [parr_pearson_hardness_eq_second_diff]
  constructor <;> intro h <;> linarith

/-- **Strict shell-closure kink**: `0 < η_PP(N) ↔ 2 * E(N) < E(N - 1) + E(N + 1)`, ensuring
    disproportionation stability `2 X(N) → X(N-1) + X(N+1)` at closed shells. -/
theorem parr_pearson_hardness_pos_iff_strict_convex {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (E : ℕ → K) (N : ℕ) :
    0 < parrPearsonHardness E N ↔ 2 * E N < E (N - 1) + E (N + 1) := by
  rw [parr_pearson_hardness_eq_second_diff]
  constructor <;> intro h <;> linarith

/-- Pauli principal-shell capacity `2 n²`. -/
def pauliShellCap (n : ℕ) : ℕ := 2 * n ^ 2

/-- Madelung period capacity `2 ⌈(p + 2) / 2⌉² = 2 * ((p + 1) / 2 + 1)²` (`p = 0, 1, 2, …` giving
    `2, 8, 8, 18, 18, 32, …`). -/
def madelungPeriodCap (p : ℕ) : ℕ := pauliShellCap ((p + 1) / 2 + 1)

/-- Cumulative noble-gas electron count after closing `P` Madelung periods. -/
def cumulativeNobleGasClosure (P : ℕ) : ℕ :=
  (List.range P).foldl (fun acc p => acc + madelungPeriodCap p) 0

/-- First four principal Pauli shell capacities `[2, 8, 18, 32]`. -/
theorem pauli_shell_capacities_1_to_4 :
    [1, 2, 3, 4].map pauliShellCap = [2, 8, 18, 32] := by
  decide

/-- Cumulative noble-gas magic closures `[2, 10, 18, 36, 54, 86]` (`He, Ne, Ar, Kr, Xe, Rn`)
    from `2n²` period capacities `[2, 8, 8, 18, 18, 32]`. -/
theorem noble_gas_magic_closures_eq :
    [1, 2, 3, 4, 5, 6].map cumulativeNobleGasClosure = [2, 10, 18, 36, 54, 86] := by
  decide


/-! ## §4. Layer-4 Chemical Stoichiometry, Toric Binomials & Canonical Diophantine Circuits -/

/-- Signed stoichiometric reaction vector `v_j := ν_{+,j} - ν_{-,j}` from unsigned reactant
    and product multiplicities `ν_minus, ν_plus : Fin M → ℕ`. -/
def stoichVec {M : ℕ} (ν_minus ν_plus : Fin M → ℕ) : Fin M → ℤ :=
  fun j => (ν_plus j : ℤ) - (ν_minus j : ℤ)

/-- **Fundamental theorem of chemical equation balancing**: every element `e : Fin E` has equal
    reactant and product atom counts iff the signed stoichiometric vector `stoichVec ν_minus ν_plus`
    lies in the homogeneous linear Diophantine kernel `Matrix.mulVec A_chem v = 0`. -/
theorem atom_conservation_iff_stoich_in_kernel {E M : ℕ}
    (A_chem : Matrix (Fin E) (Fin M) ℤ) (ν_minus ν_plus : Fin M → ℕ) :
    (∀ e : Fin E,
      ∑ j : Fin M, A_chem e j * (ν_minus j : ℤ) =
        ∑ j : Fin M, A_chem e j * (ν_plus j : ℤ)) ↔
      Matrix.mulVec A_chem (stoichVec ν_minus ν_plus) = 0 := by
  constructor
  · intro h
    ext e
    simp only [Matrix.mulVec, dotProduct, stoichVec, Pi.zero_apply]
    have he := h e
    have hsub :
        (∑ j : Fin M, A_chem e j * ((ν_plus j : ℤ) - (ν_minus j : ℤ))) =
          (∑ j : Fin M, A_chem e j * (ν_plus j : ℤ)) -
            ∑ j : Fin M, A_chem e j * (ν_minus j : ℤ) := by
      rw [← Finset.sum_sub_distrib]
      refine Finset.sum_congr rfl ?_
      intro j _
      ring
    rw [hsub, he, sub_self]
  · intro h e
    have he : Matrix.mulVec A_chem (stoichVec ν_minus ν_plus) e = 0 := by
      rw [h]; rfl
    simp only [Matrix.mulVec, dotProduct, stoichVec] at he
    have hsub :
        (∑ j : Fin M, A_chem e j * ((ν_plus j : ℤ) - (ν_minus j : ℤ))) =
          (∑ j : Fin M, A_chem e j * (ν_plus j : ℤ)) -
            ∑ j : Fin M, A_chem e j * (ν_minus j : ℤ) := by
      rw [← Finset.sum_sub_distrib]
      refine Finset.sum_congr rfl ?_
      intro j _
      ring
    rw [hsub] at he
    omega

/-- **Lattice subgroup closure of balanced reactions**: any `ℤ`-linear combination `a • v₁ + b • v₂`
    of balanced chemical reactions remains balanced (`∈ ker_ℤ(A_chem)`). -/
theorem stoich_kernel_linear_comb {E M : ℕ}
    (A_chem : Matrix (Fin E) (Fin M) ℤ) {v₁ v₂ : Fin M → ℤ}
    (hv₁ : Matrix.mulVec A_chem v₁ = 0) (hv₂ : Matrix.mulVec A_chem v₂ = 0)
    (a b : ℤ) :
    Matrix.mulVec A_chem (a • v₁ + b • v₂) = 0 := by
  rw [Matrix.mulVec_add, Matrix.mulVec_smul, Matrix.mulVec_smul, hv₁, hv₂]
  simp

/-- **Hess's law (linearity + elemental reference-potential invariance)**:
    reaction enthalpy `ΔH(v) := configCost h_f v` is `ℤ`-linear on reaction vectors and
    strictly invariant under arbitrary shifts of elemental reference zero-points
    `h_f' j = h_f j - ∑_e A_{e,j} y_e` on every balanced reaction `v ∈ ker_ℤ(A_chem)`. -/
theorem hess_law_linear_and_reference_invariant {E M : ℕ} {K : Type*} [CommRing K]
    (A_chem : Matrix (Fin E) (Fin M) ℤ) (h_f : Fin M → K) (y : Fin E → K)
    {v₁ v₂ : Fin M → ℤ}
    (hv₁ : Matrix.mulVec A_chem v₁ = 0) (hv₂ : Matrix.mulVec A_chem v₂ = 0)
    (a b : ℤ) :
    configCost h_f (a • v₁ + b • v₂) =
        (a : K) * configCost h_f v₁ + (b : K) * configCost h_f v₂ ∧
      configCost (reducedCost A_chem h_f y) (a • v₁ + b • v₂) =
        configCost h_f (a • v₁ + b • v₂) := by
  refine ⟨?_, ?_⟩
  · rw [configCost_add, configCost_zsmul, configCost_zsmul]
  · exact reduced_cost_eq_cost_on_kernel A_chem h_f y
      (stoich_kernel_linear_comb A_chem hv₁ hv₂ a b)

/-- Apply a finite sequence of reaction extents `(ξ_r, v_r)` to an initial molecular state `n₀`. -/
def applyReactions {M : ℕ} (n₀ : Fin M → ℤ) (steps : List (ℤ × (Fin M → ℤ))) : Fin M → ℤ :=
  steps.foldl (fun n step => n + step.1 • step.2) n₀

/-- **Exact nuclear-element invariance across arbitrary reaction networks**:
    if every reaction step `v_r` in `steps` lies in `ker_ℤ(A_chem)`, then the elemental atom
    inventory `A_chem (applyReactions n₀ steps) = A_chem n₀` is strictly conserved. -/
theorem element_inventory_invariant_along_reactions {E M : ℕ}
    (A_chem : Matrix (Fin E) (Fin M) ℤ) (n₀ : Fin M → ℤ)
    (steps : List (ℤ × (Fin M → ℤ)))
    (hsteps : ∀ step ∈ steps, Matrix.mulVec A_chem step.2 = 0) :
    Matrix.mulVec A_chem (applyReactions n₀ steps) = Matrix.mulVec A_chem n₀ := by
  induction steps generalizing n₀ with
  | nil => rfl
  | cons hd tl ih =>
      simp only [applyReactions, List.foldl_cons] at ih ⊢
      have hhd : Matrix.mulVec A_chem hd.2 = 0 := hsteps hd (List.mem_cons_self ..)
      have htl : ∀ step ∈ tl, Matrix.mulVec A_chem step.2 = 0 :=
        fun step hmem => hsteps step (List.mem_cons_of_mem hd hmem)
      rw [ih (n₀ + hd.1 • hd.2) htl, Matrix.mulVec_add, Matrix.mulVec_smul, hhd, smul_zero,
        add_zero]

/-- Monomial evaluation `x^ν := ∏_j x_j^{ν_j}` in any commutative ring `R`. -/
def evalMonomial {M : ℕ} {R : Type*} [CommRing R] (x : Fin M → R) (ν : Fin M → ℕ) : R :=
  ∏ j : Fin M, x j ^ ν j

/-- Toric parameterization `(Rˣ)^E → R^M` sending elemental fugacity units `t : Fin E → Rˣ`
    to `x_j(t) := ∏_e t_e^{A_{e,j}}`. -/
def toricSpecMap {E M : ℕ} {R : Type*} [CommRing R]
    (A_chem : Matrix (Fin E) (Fin M) ℤ) (t : Fin E → Rˣ) (j : Fin M) : R :=
  ((∏ e : Fin E, t e ^ A_chem e j : Rˣ) : R)

private lemma finset_prod_zpow_sum {ι G : Type*} [CommGroup G]
    (s : Finset ι) (u : G) (f : ι → ℤ) :
    (∏ i ∈ s, u ^ f i) = u ^ (∑ i ∈ s, f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih =>
      rw [Finset.prod_insert ha, Finset.sum_insert ha, zpow_add, ih]

private lemma toric_unit_monomial_eq {E M : ℕ} {R : Type*} [CommRing R]
    (A_chem : Matrix (Fin E) (Fin M) ℤ) (t : Fin E → Rˣ) (ν : Fin M → ℕ) :
    (∏ j : Fin M, (∏ e : Fin E, t e ^ A_chem e j) ^ ν j) =
      ∏ e : Fin E, t e ^ (∑ j : Fin M, A_chem e j * (ν j : ℤ)) := by
  calc
    (∏ j : Fin M, (∏ e : Fin E, t e ^ A_chem e j) ^ ν j)
        = ∏ j : Fin M, ∏ e : Fin E, t e ^ (A_chem e j * (ν j : ℤ)) := by
          refine Finset.prod_congr rfl ?_
          intro j _
          rw [← Finset.prod_pow]
          refine Finset.prod_congr rfl ?_
          intro e _
          rw [← zpow_natCast, ← zpow_mul]
    _ = ∏ e : Fin E, ∏ j : Fin M, t e ^ (A_chem e j * (ν j : ℤ)) := Finset.prod_comm
    _ = ∏ e : Fin E, t e ^ (∑ j : Fin M, A_chem e j * (ν j : ℤ)) := by
          refine Finset.prod_congr rfl ?_
          intro e _
          exact finset_prod_zpow_sum Finset.univ (t e) (fun j => A_chem e j * (ν j : ℤ))

/-- **Toric binomial vanishing theorem**: every balanced chemical reaction
    `stoichVec ν_minus ν_plus ∈ ker_ℤ(A_chem)` defines a pure toric binomial
    `x^{ν_plus} - x^{ν_minus}` that vanishes identically on the toric image `toricSpecMap A_chem t`
    over any commutative ring `R`. -/
theorem toric_hom_vanishes_on_binomial_of_kernel {E M : ℕ} {R : Type*} [CommRing R]
    (A_chem : Matrix (Fin E) (Fin M) ℤ) (t : Fin E → Rˣ)
    {ν_minus ν_plus : Fin M → ℕ}
    (hker : Matrix.mulVec A_chem (stoichVec ν_minus ν_plus) = 0) :
    evalMonomial (toricSpecMap A_chem t) ν_plus -
      evalMonomial (toricSpecMap A_chem t) ν_minus = 0 := by
  have hcons := (atom_conservation_iff_stoich_in_kernel A_chem ν_minus ν_plus).mpr hker
  have hunit :
      (∏ j : Fin M, (∏ e : Fin E, t e ^ A_chem e j) ^ ν_plus j) =
        ∏ j : Fin M, (∏ e : Fin E, t e ^ A_chem e j) ^ ν_minus j := by
    rw [toric_unit_monomial_eq, toric_unit_monomial_eq]
    refine Finset.prod_congr rfl ?_
    intro e _
    rw [hcons e]
  have hval :
      evalMonomial (toricSpecMap A_chem t) ν_plus =
        evalMonomial (toricSpecMap A_chem t) ν_minus := by
    unfold evalMonomial toricSpecMap
    have hcast : ∀ ν : Fin M → ℕ,
        (∏ j : Fin M, ((∏ e : Fin E, t e ^ A_chem e j : Rˣ) : R) ^ ν j) =
          (((∏ j : Fin M, (∏ e : Fin E, t e ^ A_chem e j) ^ ν j : Rˣ)) : R) := by
      intro ν
      push_cast
      rfl
    rw [hcast ν_plus, hcast ν_minus, hunit]
  rw [hval, sub_self]

/-- Greatest common divisor of the entries of an integer stoichiometric vector `v : Fin M → ℤ`
    (`vecGcd v = 1` certifies that `v` is a primitive lattice vector). -/
def vecGcd {M : ℕ} (v : Fin M → ℤ) : ℕ :=
  (List.finRange M).foldl (fun g j => Nat.gcd g (v j).natAbs) 0


/-! ### §4a. Four Canonical 1D-Kernel Chemical Systems (Exact `ker_ℤ` & Primitivity) -/

/-- **1. Water synthesis** `(H₂, O₂, H₂O)` over `(H, O)`: `A_H2O = [[2, 0, 2], [0, 2, 1]]`. -/
def A_H2O : Matrix (Fin 2) (Fin 3) ℤ := ![![2, 0, 2], ![0, 2, 1]]

/-- Primitive water-synthesis circuit `2 H₂ + O₂ → 2 H₂O`: `v_H2O = (-2, -1, 2)`. -/
def v_H2O : Fin 3 → ℤ := ![-2, -1, 2]

theorem v_H2O_in_kernel_and_primitive :
    Matrix.mulVec A_H2O v_H2O = 0 ∧ vecGcd v_H2O = 1 := by
  refine ⟨?_, by decide⟩
  funext i; fin_cases i <;> decide

/-- Complete 1D integer kernel of water synthesis: `ker_ℤ(A_H2O) = ℤ · (-2, -1, 2)`. -/
theorem ker_A_H2O_iff (w : Fin 3 → ℤ) :
    Matrix.mulVec A_H2O w = 0 ↔ ∃ k : ℤ, w = k • v_H2O := by
  constructor
  · intro hw
    have h0 : (Matrix.mulVec A_H2O w) 0 = 0 := by rw [hw]; rfl
    have h1 : (Matrix.mulVec A_H2O w) 1 = 0 := by rw [hw]; rfl
    rw [Matrix.mulVec, dotProduct, Fin.sum_univ_three] at h0 h1
    change 2 * w 0 + 0 * w 1 + 2 * w 2 = 0 at h0
    change 0 * w 0 + 2 * w 1 + 1 * w 2 = 0 at h1
    refine ⟨-w 1, ?_⟩
    funext i
    fin_cases i
    · change w 0 = -w 1 * (-2); omega
    · change w 1 = -w 1 * (-1); omega
    · change w 2 = -w 1 * 2; omega
  · rintro ⟨k, rfl⟩
    rw [Matrix.mulVec_smul, v_H2O_in_kernel_and_primitive.1, smul_zero]

/-- **2. Methane combustion** `(CH₄, O₂, CO₂, H₂O)` over `(C, H, O)`:
    `A_CH4 = [[1, 0, 1, 0], [4, 0, 0, 2], [0, 2, 2, 1]]`. -/
def A_CH4 : Matrix (Fin 3) (Fin 4) ℤ := ![![1, 0, 1, 0], ![4, 0, 0, 2], ![0, 2, 2, 1]]

/-- Primitive methane-combustion circuit `CH₄ + 2 O₂ → CO₂ + 2 H₂O`: `v_CH4 = (-1, -2, 1, 2)`. -/
def v_CH4 : Fin 4 → ℤ := ![-1, -2, 1, 2]

theorem v_CH4_in_kernel_and_primitive :
    Matrix.mulVec A_CH4 v_CH4 = 0 ∧ vecGcd v_CH4 = 1 := by
  refine ⟨?_, by decide⟩
  funext i; fin_cases i <;> decide

/-- Complete 1D integer kernel of methane combustion: `ker_ℤ(A_CH4) = ℤ · (-1, -2, 1, 2)`. -/
theorem ker_A_CH4_iff (w : Fin 4 → ℤ) :
    Matrix.mulVec A_CH4 w = 0 ↔ ∃ k : ℤ, w = k • v_CH4 := by
  constructor
  · intro hw
    have h0 : (Matrix.mulVec A_CH4 w) 0 = 0 := by rw [hw]; rfl
    have h1 : (Matrix.mulVec A_CH4 w) 1 = 0 := by rw [hw]; rfl
    have h2 : (Matrix.mulVec A_CH4 w) 2 = 0 := by rw [hw]; rfl
    rw [Matrix.mulVec, dotProduct, Fin.sum_univ_four] at h0 h1 h2
    change 1 * w 0 + 0 * w 1 + 1 * w 2 + 0 * w 3 = 0 at h0
    change 4 * w 0 + 0 * w 1 + 0 * w 2 + 2 * w 3 = 0 at h1
    change 0 * w 0 + 2 * w 1 + 2 * w 2 + 1 * w 3 = 0 at h2
    refine ⟨w 2, ?_⟩
    funext i
    fin_cases i
    · change w 0 = w 2 * (-1); omega
    · change w 1 = w 2 * (-2); omega
    · change w 2 = w 2 * 1; omega
    · change w 3 = w 2 * 2; omega
  · rintro ⟨k, rfl⟩
    rw [Matrix.mulVec_smul, v_CH4_in_kernel_and_primitive.1, smul_zero]

/-- **3. Haber–Bosch ammonia synthesis** `(N₂, H₂, NH₃)` over `(N, H)`:
    `A_NH3 = [[2, 0, 1], [0, 2, 3]]`. -/
def A_NH3 : Matrix (Fin 2) (Fin 3) ℤ := ![![2, 0, 1], ![0, 2, 3]]

/-- Primitive Haber–Bosch circuit `N₂ + 3 H₂ → 2 NH₃`: `v_NH3 = (-1, -3, 2)`. -/
def v_NH3 : Fin 3 → ℤ := ![-1, -3, 2]

theorem v_NH3_in_kernel_and_primitive :
    Matrix.mulVec A_NH3 v_NH3 = 0 ∧ vecGcd v_NH3 = 1 := by
  refine ⟨?_, by decide⟩
  funext i; fin_cases i <;> decide

/-- Complete 1D integer kernel of Haber–Bosch synthesis: `ker_ℤ(A_NH3) = ℤ · (-1, -3, 2)`. -/
theorem ker_A_NH3_iff (w : Fin 3 → ℤ) :
    Matrix.mulVec A_NH3 w = 0 ↔ ∃ k : ℤ, w = k • v_NH3 := by
  constructor
  · intro hw
    have h0 : (Matrix.mulVec A_NH3 w) 0 = 0 := by rw [hw]; rfl
    have h1 : (Matrix.mulVec A_NH3 w) 1 = 0 := by rw [hw]; rfl
    rw [Matrix.mulVec, dotProduct, Fin.sum_univ_three] at h0 h1
    change 2 * w 0 + 0 * w 1 + 1 * w 2 = 0 at h0
    change 0 * w 0 + 2 * w 1 + 3 * w 2 = 0 at h1
    refine ⟨-w 0, ?_⟩
    funext i
    fin_cases i
    · change w 0 = -w 0 * (-1); omega
    · change w 1 = -w 0 * (-3); omega
    · change w 2 = -w 0 * 2; omega
  · rintro ⟨k, rfl⟩
    rw [Matrix.mulVec_smul, v_NH3_in_kernel_and_primitive.1, smul_zero]

/-- **4. Glucose respiration / photosynthesis** `(C₆H₁₂O₆, O₂, CO₂, H₂O)` over `(C, H, O)`:
    `A_gluc = [[6, 0, 1, 0], [12, 0, 0, 2], [6, 2, 2, 1]]`. -/
def A_gluc : Matrix (Fin 3) (Fin 4) ℤ := ![![6, 0, 1, 0], ![12, 0, 0, 2], ![6, 2, 2, 1]]

/-- Primitive glucose-respiration circuit `C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O`:
    `v_gluc = (-1, -6, 6, 6)`. -/
def v_gluc : Fin 4 → ℤ := ![-1, -6, 6, 6]

theorem v_gluc_in_kernel_and_primitive :
    Matrix.mulVec A_gluc v_gluc = 0 ∧ vecGcd v_gluc = 1 := by
  refine ⟨?_, by decide⟩
  funext i; fin_cases i <;> decide

/-- Complete 1D integer kernel of glucose respiration: `ker_ℤ(A_gluc) = ℤ · (-1, -6, 6, 6)`. -/
theorem ker_A_gluc_iff (w : Fin 4 → ℤ) :
    Matrix.mulVec A_gluc w = 0 ↔ ∃ k : ℤ, w = k • v_gluc := by
  constructor
  · intro hw
    have h0 : (Matrix.mulVec A_gluc w) 0 = 0 := by rw [hw]; rfl
    have h1 : (Matrix.mulVec A_gluc w) 1 = 0 := by rw [hw]; rfl
    have h2 : (Matrix.mulVec A_gluc w) 2 = 0 := by rw [hw]; rfl
    rw [Matrix.mulVec, dotProduct, Fin.sum_univ_four] at h0 h1 h2
    change 6 * w 0 + 0 * w 1 + 1 * w 2 + 0 * w 3 = 0 at h0
    change 12 * w 0 + 0 * w 1 + 0 * w 2 + 2 * w 3 = 0 at h1
    change 6 * w 0 + 2 * w 1 + 2 * w 2 + 1 * w 3 = 0 at h2
    refine ⟨-w 0, ?_⟩
    funext i
    fin_cases i
    · change w 0 = -w 0 * (-1); omega
    · change w 1 = -w 0 * (-6); omega
    · change w 2 = -w 0 * 6; omega
    · change w 3 = -w 0 * 6; omega
  · rintro ⟨k, rfl⟩
    rw [Matrix.mulVec_smul, v_gluc_in_kernel_and_primitive.1, smul_zero]


/-! ### §4b. Multi-Reaction `3 × 7` C–H–O Network `(C, H₂, O₂, CO, CO₂, H₂O, CH₄)` -/

/-- Stoichiometric matrix of `(C, H₂, O₂, CO, CO₂, H₂O, CH₄)` over `(C, H, O)`. -/
def A_CHO : Matrix (Fin 3) (Fin 7) ℤ :=
  ![![1, 0, 0, 1, 1, 0, 1],
    ![0, 2, 0, 0, 0, 2, 4],
    ![0, 0, 2, 1, 2, 1, 0]]

/-- Water–gas shift `CO + H₂O → CO₂ + H₂`. -/
def v_WGS : Fin 7 → ℤ := ![0, 1, 0, -1, 1, -1, 0]

/-- Boudouard disproportionation `2 CO → C + CO₂`. -/
def v_Boudouard : Fin 7 → ℤ := ![1, 0, 0, -2, 1, 0, 0]

/-- Carbon-monoxide methanation `CO + 3 H₂ → CH₄ + H₂O`. -/
def v_Methanation : Fin 7 → ℤ := ![0, -3, 0, -1, 0, 1, 1]

/-- Complete carbon oxidation `C + O₂ → CO₂`. -/
def v_CarbonOx : Fin 7 → ℤ := ![-1, 0, -1, 0, 1, 0, 0]

theorem cho_canonical_circuits_valid_and_primitive :
    Matrix.mulVec A_CHO v_WGS = 0 ∧ vecGcd v_WGS = 1 ∧
    Matrix.mulVec A_CHO v_Boudouard = 0 ∧ vecGcd v_Boudouard = 1 ∧
    Matrix.mulVec A_CHO v_Methanation = 0 ∧ vecGcd v_Methanation = 1 ∧
    Matrix.mulVec A_CHO v_CarbonOx = 0 ∧ vecGcd v_CarbonOx = 1 := by
  refine ⟨by funext i; fin_cases i <;> decide, by decide,
          by funext i; fin_cases i <;> decide, by decide,
          by funext i; fin_cases i <;> decide, by decide,
          by funext i; fin_cases i <;> decide, by decide⟩

end QOU.MathlibInfra.ConfinementLayerTower
