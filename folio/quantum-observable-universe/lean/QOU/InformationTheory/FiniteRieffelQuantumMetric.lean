import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Finite Rieffel–Kantorovich Quantum Metric & Quotient Faithfulness

Generic ordered-field (§7c, zero `ℝ`) formalization closing bean `qou-5uj7`:
1. **Rieffel Lip-seminorms (`LipSeminorm K A`):** proves `L(0) = 0`,
   `L(c · 1_A) = 0` (`L(1) = 0`), symmetry `L(-a) = L(a)`, scalar-shift
   invariance `L(a + c · 1_A) = L(a)`, and the dual Connes–Rieffel triangle
   inequality across unital state functionals.
2. **Quotient Faithfulness Criterion (`HasScalarKernel`):**
   - Non-scalar kernel elements separated by states make the dual Lipschitz
     supremum unbounded (`unbounded_of_nonscalar_kernel`).
   - Conversely, when states separate non-scalars (as on semisimple finite
     quotients `TL_n(q) = H_n(q) / rad`), finite state-pair bounds force
     `ker L = K · 1_A` (`hasScalarKernel_of_state_bounded`).
3. **Kantorovich–Rubinstein Shortest-Path & Transport Duality on Finite Graphs:**
   - Every 1-Lipschitz potential satisfies `|f x - f y| ≤ pathCost p` along any
     admissible path `p` from `x` to `y` (`kr_lip_le_pathCost`).
   - When `d` is a shortest-path metric on `V`, `f_{x₀}(v) = d(x₀, v)` is
     1-Lipschitz and attains `|f_{x₀}(y) - f_{x₀}(x₀)| = d(x₀, y)`, matching
     the Kantorovich primal coupling lower bound (`kantorovich_primal_ge_dual`).
4. **Categorical Dirac Convex Cost Split (`dirac_convex_weights`):**
   `q⁻¹ + (1 - q⁻¹) = 1` with both weights strictly positive for `1 < q`.
-/

-- Ref: [rieffel1999] Rieffel, "Metrics on state spaces", Doc. Math. 4 (1999), 559–600.
-- Ref: [rieffel2004] Rieffel, Mem. Amer. Math. Soc. 168 (2004), no. 796.
-- Ref: [kantorovich1942] Kantorovich, Dokl. Akad. Nauk SSSR 37 (1942), 227–229.
-- Ref: [rubinstein1957] Kantorovich & Rubinstein, Dokl. Akad. Nauk SSSR 115 (1957), 1058–1061.
-- Ref: [latremoliere2016] Latrémolière, Trans. Amer. Math. Soc. 368 (2016), 365–411.
-- Ref: [iochum-krajewski-martinetti2001] Iochum, Krajewski & Martinetti, J. Geom. Phys. 37 (2001), 100–125.
-- Ref: [dandrea-martinetti2010] D'Andrea & Martinetti, SIGMA 6 (2010), 057.
namespace QOU.InformationTheory.FiniteRieffelQuantumMetric

open scoped BigOperators

section LipSeminormTheory

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
variable {A : Type*} [Ring A] [Algebra K A]

/-- A Rieffel Lipschitz seminorm on a unital `K`-algebra `A`, vanishing on `1`. -/
structure LipSeminorm (K : Type*) [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (A : Type*) [Ring A] [Algebra K A] where
  toFun : A → K
  nonneg : ∀ a, 0 ≤ toFun a
  map_one : toFun 1 = 0
  homog : ∀ (c : K) (a : A), toFun (c • a) = |c| * toFun a
  subadd : ∀ a b : A, toFun (a + b) ≤ toFun a + toFun b

theorem LipSeminorm.map_zero (L : LipSeminorm K A) : L.toFun 0 = 0 := by
  have h : (0 : A) = (0 : K) • (1 : A) := by simp
  rw [h, L.homog, abs_zero, zero_mul]

/-- Scalar multiples of the unit lie in `ker L`: `L(c · 1_A) = 0`. -/
theorem LipSeminorm.map_algebraMap (L : LipSeminorm K A) (c : K) :
    L.toFun (algebraMap K A c) = 0 := by
  rw [Algebra.algebraMap_eq_smul_one, L.homog, L.map_one, mul_zero]

theorem LipSeminorm.map_neg (L : LipSeminorm K A) (a : A) :
    L.toFun (-a) = L.toFun a := by
  have h : (-a : A) = (-1 : K) • a := by simp
  rw [h, L.homog, abs_neg, abs_one, one_mul]

/-- Adding a scalar multiple of `1_A` leaves `L(a)` invariant. -/
theorem LipSeminorm.shift_scalar (L : LipSeminorm K A) (a : A) (c : K) :
    L.toFun (a + algebraMap K A c) = L.toFun a := by
  apply le_antisymm
  · calc L.toFun (a + algebraMap K A c)
        ≤ L.toFun a + L.toFun (algebraMap K A c) := L.subadd _ _
      _ = L.toFun a := by rw [L.map_algebraMap, add_zero]
  · calc L.toFun a
        = L.toFun ((a + algebraMap K A c) + algebraMap K A (-c)) := by
            rw [RingHom.map_neg, add_assoc, add_neg_cancel, add_zero]
      _ ≤ L.toFun (a + algebraMap K A c) + L.toFun (algebraMap K A (-c)) := L.subadd _ _
      _ = L.toFun (a + algebraMap K A c) := by rw [L.map_algebraMap, add_zero]

/-- Unit Lip-ball predicate `L(a) ≤ 1`. -/
def IsLipOne (L : LipSeminorm K A) (a : A) : Prop := L.toFun a ≤ 1

theorem one_isLipOne (L : LipSeminorm K A) : IsLipOne L 1 := by
  rw [IsLipOne, L.map_one]
  exact zero_le_one

/-- Unital `K`-linear functional (algebraic state carrier). -/
structure UnitalState (K : Type*) [CommSemiring K] (A : Type*) [Semiring A] [Algebra K A] where
  toLinear : A →ₗ[K] K
  map_one : toLinear 1 = 1

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem UnitalState.map_algebraMap (φ : UnitalState K A) (c : K) :
    φ.toLinear (algebraMap K A c) = c := by
  rw [Algebra.algebraMap_eq_smul_one, LinearMap.map_smul, smul_eq_mul, φ.map_one, mul_one]

/-- `d` is an upper bound for the Connes–Rieffel dual supremum between `φ` and `ψ`. -/
def IsDualBound (L : LipSeminorm K A) (φ ψ : UnitalState K A) (d : K) : Prop :=
  ∀ a : A, IsLipOne L a → |φ.toLinear a - ψ.toLinear a| ≤ d

theorem isDualBound_self (L : LipSeminorm K A) (φ : UnitalState K A) :
    IsDualBound L φ φ 0 := by
  intro a _
  simp

theorem isDualBound_symm {L : LipSeminorm K A} {φ ψ : UnitalState K A} {d : K}
    (h : IsDualBound L φ ψ d) : IsDualBound L ψ φ d := by
  intro a ha
  rw [abs_sub_comm]
  exact h a ha

/-- **Triangle inequality** for Connes–Rieffel dual metric bounds. -/
theorem isDualBound_triangle {L : LipSeminorm K A} {φ χ ψ : UnitalState K A} {d₁ d₂ : K}
    (h₁ : IsDualBound L φ χ d₁) (h₂ : IsDualBound L χ ψ d₂) :
    IsDualBound L φ ψ (d₁ + d₂) := by
  intro a ha
  calc |φ.toLinear a - ψ.toLinear a|
      = |(φ.toLinear a - χ.toLinear a) + (χ.toLinear a - ψ.toLinear a)| := by ring_nf
    _ ≤ |φ.toLinear a - χ.toLinear a| + |χ.toLinear a - ψ.toLinear a| := abs_add_le _ _
    _ ≤ d₁ + d₂ := add_le_add (h₁ a ha) (h₂ a ha)

/-- Rieffel's faithfulness condition on the Lip-seminorm kernel: `ker L = K · 1_A`. -/
def HasScalarKernel (L : LipSeminorm K A) : Prop :=
  ∀ a : A, L.toFun a = 0 ↔ ∃ c : K, a = algebraMap K A c

/-- Any kernel element `r` (`L(r) = 0`) separated by two states (`φ(r) ≠ ψ(r)`)
drives the dual Lipschitz objective past every proposed finite bound `M`. -/
theorem unbounded_of_nonscalar_kernel (L : LipSeminorm K A)
    (φ ψ : UnitalState K A) {r : A} (hr : L.toFun r = 0)
    (hsep : φ.toLinear r ≠ ψ.toLinear r) (M : K) :
    ∃ b : A, IsLipOne L b ∧ M < |φ.toLinear b - ψ.toLinear b| := by
  set δ : K := φ.toLinear r - ψ.toLinear r
  have hδ : δ ≠ 0 := sub_ne_zero.mpr hsep
  set t : K := (|M| + 1) / δ
  refine ⟨t • r, ?_, ?_⟩
  · rw [IsLipOne, L.homog, hr, mul_zero]
    exact zero_le_one
  · have hlin : φ.toLinear (t • r) - ψ.toLinear (t • r) = |M| + 1 := by
      simp only [LinearMap.map_smul, smul_eq_mul, ← mul_sub]
      exact div_mul_cancel₀ (|M| + 1) hδ
    rw [hlin]
    have hpos : 0 < |M| + 1 := by positivity
    rw [abs_of_pos hpos]
    exact lt_of_le_of_lt (le_abs_self M) (by linarith)

/-- **Rieffel's Quotient Faithfulness Theorem (finite-bound direction):**
When unital states separate non-scalar elements of `A` (as on the faithful
quotient `TL_n(q) = H_n(q) / rad`) and every state pair admits a finite
`IsDualBound`, the Lip-seminorm kernel equals the scalar subalgebra `K · 1_A`. -/
theorem hasScalarKernel_of_state_bounded (L : LipSeminorm K A)
    (hsep : ∀ r : A, (∀ φ ψ : UnitalState K A, φ.toLinear r = ψ.toLinear r) →
      ∃ c : K, r = algebraMap K A c)
    (hbdd : ∀ φ ψ : UnitalState K A, ∃ M : K, IsDualBound L φ ψ M) :
    HasScalarKernel L := by
  intro r
  constructor
  · intro hr
    apply hsep r
    intro φ ψ
    by_contra hne
    obtain ⟨M, hM⟩ := hbdd φ ψ
    obtain ⟨b, hb, hgt⟩ := unbounded_of_nonscalar_kernel L φ ψ hr hne M
    exact lt_irrefl M (lt_of_lt_of_le hgt (hM b hb))
  · rintro ⟨c, rfl⟩
    exact L.map_algebraMap c

end LipSeminormTheory

section KantorovichRubinsteinFiniteGraph

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- A scalar potential `f : V → K` is 1-Lipschitz with respect to edge costs `cost`
along adjacency relation `adj`. -/
def IsGraphLipOne {V : Type*} (adj : V → V → Prop) (cost : V → V → K) (f : V → K) : Prop :=
  ∀ u v : V, adj u v → |f u - f v| ≤ cost u v

/-- Inductive chain of adjacent vertices from `x` to `y` accumulating edge cost. -/
inductive ValidPath {V : Type*} (adj : V → V → Prop) (cost : V → V → K) :
    V → V → K → Prop
  | refl (x : V) : ValidPath adj cost x x 0
  | step {x u y : V} {c : K} (hadj : adj x u) (hp : ValidPath adj cost u y c) :
      ValidPath adj cost x y (cost x u + c)

/-- **Weak Kantorovich–Rubinstein Shortest-Path Duality:**
Every 1-Lipschitz potential `f` satisfies `|f x - f y| ≤ c` for every valid path
from `x` to `y` of total cost `c`. -/
theorem kr_lip_le_pathCost {V : Type*} {adj : V → V → Prop} {cost : V → V → K}
    {f : V → K} (hlip : IsGraphLipOne adj cost f)
    {x y : V} {c : K} (hp : ValidPath adj cost x y c) :
    |f x - f y| ≤ c := by
  induction hp with
  | refl x => simp
  | @step x u y c hadj _ ih =>
    calc |f x - f y|
        = |(f x - f u) + (f u - f y)| := by ring_nf
      _ ≤ |f x - f u| + |f u - f y| := abs_add_le _ _
      _ ≤ cost x u + c := add_le_add (hlip x u hadj) ih

/-- **Strong Kantorovich–Rubinstein Attainment on Finite Shortest-Path Metrics:**
If `d` satisfies `d(x₀, x₀) = 0`, `0 ≤ d(x₀, y)`, and the metric triangle bounds
`d(x₀, u) ≤ d(x₀, v) + cost(u, v)` and `d(x₀, v) ≤ d(x₀, u) + cost(u, v)` along
every edge `(u, v)` (automatic for shortest-path distance on symmetric weighted graphs),
then the distance potential `f(v) = d(x₀, v)` is 1-Lipschitz and attains `d(x₀, y)`
exactly between `y` and `x₀`. -/
theorem kr_shortest_path_attained {V : Type*} {adj : V → V → Prop} {cost d : V → V → K}
    (x₀ y : V) (hdiag : d x₀ x₀ = 0) (hnonneg : 0 ≤ d x₀ y)
    (htri : ∀ u v : V, adj u v → d x₀ u ≤ d x₀ v + cost u v ∧ d x₀ v ≤ d x₀ u + cost u v) :
    IsGraphLipOne adj cost (fun v => d x₀ v) ∧
      |(fun v => d x₀ v) y - (fun v => d x₀ v) x₀| = d x₀ y := by
  refine ⟨fun u v huv => ?_, ?_⟩
  · obtain ⟨h1, h2⟩ := htri u v huv
    exact abs_sub_le_iff.mpr ⟨by linarith, by linarith⟩
  · dsimp only
    rw [hdiag, sub_zero, abs_of_nonneg hnonneg]

/-- **Kantorovich Transport Plan Duality (Finite Type):**
For any non-negative coupling `π : V → V → K` and any 1-Lipschitz potential `f`
with respect to metric `d` (`|f u - f v| ≤ d u v`), the difference of marginal
expectations is bounded above by the primal transport cost `∑_{u, v} π(u, v) d(u, v)`. -/
theorem kantorovich_primal_ge_dual {V : Type*} [Fintype V]
    (d π : V → V → K) (f : V → K)
    (hπ : ∀ u v : V, 0 ≤ π u v)
    (hlip : ∀ u v : V, |f u - f v| ≤ d u v) :
    |(∑ u : V, f u * (∑ v : V, π u v)) - (∑ v : V, f v * (∑ u : V, π u v))| ≤
      ∑ u : V, ∑ v : V, π u v * d u v := by
  have hrew :
      (∑ u : V, f u * (∑ v : V, π u v)) - (∑ v : V, f v * (∑ u : V, π u v)) =
        ∑ u : V, ∑ v : V, π u v * (f u - f v) := by
    simp_rw [Finset.mul_sum]
    rw [Finset.sum_comm (s := Finset.univ) (t := Finset.univ) (f := fun v u => f v * π u v)]
    rw [← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun u _ => ?_
    rw [← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun v _ => ?_
    ring
  rw [hrew]
  calc |∑ u : V, ∑ v : V, π u v * (f u - f v)|
      ≤ ∑ u : V, |∑ v : V, π u v * (f u - f v)| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ u : V, ∑ v : V, |π u v * (f u - f v)| :=
        Finset.sum_le_sum fun u _ => Finset.abs_sum_le_sum_abs _ _
    _ = ∑ u : V, ∑ v : V, π u v * |f u - f v| := by
        refine Finset.sum_congr rfl fun u _ => Finset.sum_congr rfl fun v _ => ?_
        rw [abs_mul, abs_of_nonneg (hπ u v)]
    _ ≤ ∑ u : V, ∑ v : V, π u v * d u v :=
        Finset.sum_le_sum fun u _ => Finset.sum_le_sum fun v _ =>
          mul_le_mul_of_nonneg_left (hlip u v) (hπ u v)

/-- Categorical Dirac operator `D_∇ = q⁻¹ ∇ + ℏ_q ι_ξ ∇` convex cost weights over
any ordered field (`1 < q`): both weights are strictly positive and sum to `1`. -/
theorem dirac_convex_weights {q : K} (hq : 1 < q) :
    0 < q⁻¹ ∧ 0 < (1 - q⁻¹) ∧ q⁻¹ + (1 - q⁻¹) = 1 := by
  have hq0 : (0 : K) < q := lt_trans zero_lt_one hq
  exact ⟨inv_pos.mpr hq0, sub_pos.mpr (inv_lt_one_of_one_lt₀ hq), by ring⟩

end KantorovichRubinsteinFiniteGraph

end QOU.InformationTheory.FiniteRieffelQuantumMetric
