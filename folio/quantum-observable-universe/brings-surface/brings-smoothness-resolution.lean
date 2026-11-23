import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.BringsSurface.brings_smoothness_resolution — Smoothness and intrinsic resolution of Bring's surface

Let $\mathcal{S} \subset \mathbb{P}^4(\mathbb{C})$ be Bring's curve/surface
([`def:brings-surface`](#def:brings-surface)), cut out in homogeneous coordinates
$x = (x_0, x_1, x_2, x_3, x_4) \in \mathbb{C}^5 \setminus \{0\}$ by the first three
Newton power sums
$$p_1(x) = \sum_{i=0}^4 x_i = 0, \qquad
  p_2(x) = \sum_{i=0}^4 x_i^2 = 0, \qquad
  p_3(x) = \sum_{i=0}^4 x_i^3 = 0.$$

This module formalises and proves (`0` `sorry`, `0` `: True` placeholders) the three
claims of [`prop:brings-smoothness-resolution`](#prop:brings-smoothness-resolution):

1. **Transversality in $\mathbb{P}^4(\mathbb{C})$ (`bring_transverse_in_P4`).**
   For any three coordinate columns $(i, j, k)$, the $3 \times 3$ minor of the
   $3 \times 5$ Jacobian matrix $\partial(p_1, p_2, p_3)/\partial(x_0,\dots,x_4)$
   factors as the Vandermonde product
   $$\det J_{i,j,k}(x) = 6 (x_j - x_i)(x_k - x_i)(x_k - x_j).$$
   Every non-zero solution $x \in \mathbb{C}^5 \setminus \{0\}$ of
   $p_1(x) = p_2(x) = p_3(x) = 0$ assumes at least three pairwise-distinct coordinate
   values, hence admits a non-vanishing $3 \times 3$ Jacobian minor
   $\det J_{i,j,k}(x) \neq 0$.

2. **Intrinsic branch-point resolution (`bring_intrinsic_resolution`).**
   When two color sheets $x_i, x_j$ collide at midpoint $x_c = (x_i + x_j)/2$, the
   local color-difference coordinate $\delta = x_i - x_j$ satisfies the exact
   quadratic perturbation identity
   $$x_i^2 + x_j^2 - 2 x_c^2 = \frac{\delta^2}{2}, \qquad \delta = 0 \iff x_i = x_j,$$
   embedding the quadratic ramification $z - z_c \sim \delta^2$ directly in the
   ambient color coordinates.

3. **Regular $C_5$ foliation (`bring_regular_c5_foliation`).**
   For any non-trivial fifth root of unity $\zeta \in \mathbb{C}$ ($\zeta^5 = 1$,
   $\zeta \neq 1$) and any non-zero resolvent coordinate $w_1 \neq 0$, the cyclic
   action $w_1 \mapsto \zeta w_1$ is fixed-point-free ($\zeta w_1 \neq w_1$).
-/
namespace QOU.BringsSurface

-- Ref: [leitner2026] Ch. 6, §1 (prop:brings-smoothness-resolution)
-- Ref: [bring1786] Bring, "Meletemata quaedam mathematica circa transformationem aequationum algebraicarum," Lund 1786
-- Ref: [edge1978] Edge, "Bring's curve," J. London Math. Soc. (2) 18 (1978), 539–545

/-- First Newton power sum $p_1(x) = \sum_{r=0}^4 x_r$ on $\mathbb{C}^5$. -/
def bringPowerSum1 (x : Fin 5 → ℂ) : ℂ :=
  x 0 + x 1 + x 2 + x 3 + x 4

/-- Second Newton power sum $p_2(x) = \sum_{r=0}^4 x_r^2$ on $\mathbb{C}^5$. -/
def bringPowerSum2 (x : Fin 5 → ℂ) : ℂ :=
  x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 + x 4 ^ 2

/-- Third Newton power sum $p_3(x) = \sum_{r=0}^4 x_r^3$ on $\mathbb{C}^5$. -/
def bringPowerSum3 (x : Fin 5 → ℂ) : ℂ :=
  x 0 ^ 3 + x 1 ^ 3 + x 2 ^ 3 + x 3 ^ 3 + x 4 ^ 3

/-- The affine cone over Bring's surface in $\mathbb{C}^5$, cut out by the
    three power-sum equations $p_1(x) = p_2(x) = p_3(x) = 0$. -/
def OnBringSurfaceLocus (x : Fin 5 → ℂ) : Prop :=
  bringPowerSum1 x = 0 ∧ bringPowerSum2 x = 0 ∧ bringPowerSum3 x = 0

/-- The $3 \times 3$ minor of the $3 \times 5$ Jacobian matrix
    $\partial(p_1, p_2, p_3)/\partial(x_0, \dots, x_4)$ on columns $(i, j, k)$:
    $$\det \begin{pmatrix} 1 & 1 & 1 \\ 2 x_i & 2 x_j & 2 x_k \\ 3 x_i^2 & 3 x_j^2 & 3 x_k^2 \end{pmatrix}.$$ -/
def bringJacobianMinor (x : Fin 5 → ℂ) (i j k : Fin 5) : ℂ :=
  1 * (2 * x j * (3 * x k ^ 2) - 2 * x k * (3 * x j ^ 2)) -
  1 * (2 * x i * (3 * x k ^ 2) - 2 * x k * (3 * x i ^ 2)) +
  1 * (2 * x i * (3 * x j ^ 2) - 2 * x j * (3 * x i ^ 2))

/-- **Vandermonde factorisation of the Bring Jacobian minor.**
    Every $3 \times 3$ minor of $\partial(p_1, p_2, p_3)/\partial x$ equals
    $6 (x_j - x_i)(x_k - x_i)(x_k - x_j)$. -/
theorem bringJacobianMinor_eq_six_vandermonde (x : Fin 5 → ℂ) (i j k : Fin 5) :
    bringJacobianMinor x i j k = 6 * (x j - x i) * (x k - x i) * (x k - x j) := by
  unfold bringJacobianMinor
  ring

/-- Any three pairwise-distinct coordinates $(x_i, x_j, x_k)$ give a non-vanishing
    $3 \times 3$ Jacobian minor. -/
theorem bringJacobianMinor_ne_zero (x : Fin 5 → ℂ) (i j k : Fin 5)
    (hij : x i ≠ x j) (hik : x i ≠ x k) (hjk : x j ≠ x k) :
    bringJacobianMinor x i j k ≠ 0 := by
  rw [bringJacobianMinor_eq_six_vandermonde]
  have h6 : (6 : ℂ) ≠ 0 := by norm_num
  exact mul_ne_zero
    (mul_ne_zero (mul_ne_zero h6 (sub_ne_zero.mpr hij.symm)) (sub_ne_zero.mpr hik.symm))
    (sub_ne_zero.mpr hjk.symm)

/-- Algebraic identity expressing $\sum_{r=0}^4 (x_r - a)(x_r - b)$ in terms of
    $p_1(x)$, $p_2(x)$, and $5ab$. -/
theorem two_value_sum_identity (x : Fin 5 → ℂ) (a b : ℂ) :
    (x 0 - a) * (x 0 - b) + (x 1 - a) * (x 1 - b) + (x 2 - a) * (x 2 - b) +
    (x 3 - a) * (x 3 - b) + (x 4 - a) * (x 4 - b) =
    bringPowerSum2 x - (a + b) * bringPowerSum1 x + 5 * a * b := by
  unfold bringPowerSum1 bringPowerSum2
  ring

/-- If every coordinate $x_r$ takes values in $\{0, b\}$ and $p_1(x) = 0$, then either
    $b = 0$ or all five coordinates vanish. -/
theorem eq_zero_of_mem_zero_pair (x : Fin 5 → ℂ) (b : ℂ)
    (hp1 : bringPowerSum1 x = 0)
    (h0 : x 0 = 0 ∨ x 0 = b) (h1 : x 1 = 0 ∨ x 1 = b)
    (h2 : x 2 = 0 ∨ x 2 = b) (h3 : x 3 = 0 ∨ x 3 = b)
    (h4 : x 4 = 0 ∨ x 4 = b) :
    b = 0 ∨ (x 0 = 0 ∧ x 1 = 0 ∧ x 2 = 0 ∧ x 3 = 0 ∧ x 4 = 0) := by
  unfold bringPowerSum1 at hp1
  rcases h0 with h0 | h0 <;> rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2 <;>
    rcases h3 with h3 | h3 <;> rcases h4 with h4 | h4
  · right
    exact ⟨h0, h1, h2, h3, h4⟩
  all_goals
    left
    rw [h0, h1, h2, h3, h4] at hp1
    first
    | linear_combination hp1
    | linear_combination hp1 / 2
    | linear_combination hp1 / 3
    | linear_combination hp1 / 4
    | linear_combination hp1 / 5

/-- Consequently, if every coordinate $x_r \in \{0, b\}$ and $p_1(x) = 0$, then every
    coordinate $x_r = 0$. -/
theorem all_zero_of_mem_zero_pair (x : Fin 5 → ℂ) (b : ℂ)
    (hp1 : bringPowerSum1 x = 0)
    (hall : ∀ r : Fin 5, x r = 0 ∨ x r = b) :
    ∀ r : Fin 5, x r = 0 := by
  rcases eq_zero_of_mem_zero_pair x b hp1 (hall 0) (hall 1) (hall 2) (hall 3) (hall 4) with
    hb | ⟨z0, z1, z2, z3, z4⟩
  · intro r
    rcases hall r with hr | hr
    · exact hr
    · exact hr.trans hb
  · intro r
    match r with
    | ⟨0, _⟩ => exact z0
    | ⟨1, _⟩ => exact z1
    | ⟨2, _⟩ => exact z2
    | ⟨3, _⟩ => exact z3
    | ⟨4, _⟩ => exact z4
    | ⟨n + 5, h⟩ => omega

/-- If every coordinate $x_r$ takes values in $\{a, b\}$ and $p_1(x) = p_2(x) = 0$,
    then every coordinate $x_r = 0$. -/
theorem all_zero_of_two_values (x : Fin 5 → ℂ) (a b : ℂ)
    (hp1 : bringPowerSum1 x = 0) (hp2 : bringPowerSum2 x = 0)
    (hall : ∀ r : Fin 5, x r = a ∨ x r = b) :
    ∀ r : Fin 5, x r = 0 := by
  have hprod : ∀ r : Fin 5, (x r - a) * (x r - b) = 0 := by
    intro r
    rcases hall r with hr | hr
    · rw [hr, sub_self, zero_mul]
    · rw [hr, sub_self, mul_zero]
  have hsum : 5 * a * b = 0 := by
    have hid := two_value_sum_identity x a b
    rw [hprod 0, hprod 1, hprod 2, hprod 3, hprod 4, hp1, hp2] at hid
    linear_combination -hid
  have hab : a = 0 ∨ b = 0 := by
    have h5 : (5 : ℂ) ≠ 0 := by norm_num
    have hab' : a * b = 0 := by
      rcases mul_eq_zero.mp (by linear_combination hsum : (5 : ℂ) * (a * b) = 0) with h50 | hab0
      · exact False.elim (h5 h50)
      · exact hab0
    exact mul_eq_zero.mp hab'
  rcases hab with ha | hb
  · apply all_zero_of_mem_zero_pair x b hp1
    intro r
    rcases hall r with hr | hr
    · left; exact hr.trans ha
    · right; exact hr
  · apply all_zero_of_mem_zero_pair x a hp1
    intro r
    rcases hall r with hr | hr
    · right; exact hr
    · left; exact hr.trans hb

/-- **Claim 1 (Smoothness / Transversality in $\mathbb{P}^4(\mathbb{C})$).**
    Every non-zero point $x \in \mathbb{C}^5 \setminus \{0\}$ on the Bring surface
    locus $p_1(x) = p_2(x) = p_3(x) = 0$ has at least one non-vanishing $3 \times 3$
    Jacobian minor. -/
def BringTransverseInP4 : Prop :=
  ∀ x : Fin 5 → ℂ, OnBringSurfaceLocus x → (∃ r : Fin 5, x r ≠ 0) →
    ∃ i j k : Fin 5, bringJacobianMinor x i j k ≠ 0

/-- **Proof of Claim 1 (`BringTransverseInP4`).** -/
theorem bring_transverse_in_P4 : BringTransverseInP4 := by
  intro x ⟨hp1, hp2, _hp3⟩ ⟨r₀, hr₀⟩
  by_contra hno
  push_neg at hno
  have hall_two : ∀ i j k : Fin 5, x i = x j ∨ x k = x i ∨ x k = x j := by
    intro i j k
    by_contra hne
    push_neg at hne
    exact bringJacobianMinor_ne_zero x i j k hne.1 hne.2.1.symm hne.2.2.symm (hno i j k)
  have hzero : ∀ r : Fin 5, x r = 0 := by
    by_cases hall0 : ∀ s : Fin 5, x s = x 0
    · apply all_zero_of_two_values x (x 0) (x 0) hp1 hp2
      intro r
      exact Or.inl (hall0 r)
    · push_neg at hall0
      rcases hall0 with ⟨s, hs⟩
      apply all_zero_of_two_values x (x 0) (x s) hp1 hp2
      intro r
      rcases hall_two 0 s r with h0s | hr0 | hrs
      · exact False.elim (hs h0s.symm)
      · exact Or.inl hr0
      · exact Or.inr hrs
  exact hr₀ (hzero r₀)

/-- **Claim 2 (Intrinsic quadratic branch-point resolution).**
    At any sheet collision with midpoint $x_c = (x_i + x_j)/2$ and local color-difference
    coordinate $\delta = x_i - x_j$, the quadratic perturbation satisfies
    $x_i^2 + x_j^2 - 2 x_c^2 = \delta^2 / 2$ and $\delta = 0 \iff x_i = x_j$. -/
def BringIntrinsicResolution : Prop :=
  ∀ x : Fin 5 → ℂ, ∀ i j : Fin 5,
    x i ^ 2 + x j ^ 2 - 2 * ((x i + x j) / 2) ^ 2 = (x i - x j) ^ 2 / 2 ∧
    (x i - x j = 0 ↔ x i = x j)

/-- **Proof of Claim 2 (`BringIntrinsicResolution`).** -/
theorem bring_intrinsic_resolution : BringIntrinsicResolution := by
  intro x i j
  refine ⟨by ring, sub_eq_zero⟩

/-- **Claim 3 (Regular $C_5$ foliation without fixed points).**
    For any non-trivial fifth root of unity $\zeta \in \mathbb{C}$ ($\zeta^5 = 1$,
    $\zeta \neq 1$) and any non-zero resolvent coordinate $w_1 \neq 0$, the cyclic
    action $w_1 \mapsto \zeta w_1$ has no fixed points ($\zeta w_1 \neq w_1$). -/
def BringRegularC5Foliation : Prop :=
  ∀ ζ w₁ : ℂ, ζ ^ 5 = 1 → ζ ≠ 1 → w₁ ≠ 0 → ζ * w₁ ≠ w₁

/-- **Proof of Claim 3 (`BringRegularC5Foliation`).** -/
theorem bring_regular_c5_foliation : BringRegularC5Foliation := by
  intro ζ w₁ _hζ5 hζ1 hw₁ hfix
  apply hζ1
  have hsub : (ζ - 1) * w₁ = 0 := by linear_combination hfix
  rcases mul_eq_zero.mp hsub with hζ0 | hw0
  · exact sub_eq_zero.mp hζ0
  · exact False.elim (hw₁ hw0)

/-- **Carrier for the three smoothness and resolution conditions**, parameterised by
    the three propositions. -/
structure BringSurfaceSmoothness
    (Transverse IntrinsicResolution RegularFoliation : Prop) : Prop where
  /-- The three power-sum constraints are transverse (Jacobian has full rank). -/
  transverse : Transverse
  /-- At each branch point $z_c$, the local color coordinate $\delta = x_i - x_j$
      satisfies the quadratic perturbation identity $x_i^2 + x_j^2 - 2 x_c^2 = \delta^2 / 2$. -/
  intrinsic_resolution : IntrinsicResolution
  /-- The $C_5$ orbits $w_1 \mapsto \zeta w_1$ act without fixed points on $w_1 \neq 0$. -/
  regular_foliation : RegularFoliation

/-- Concrete proved inhabitant of `BringSurfaceSmoothness` for the three Bring surface
    smoothness, intrinsic-resolution, and regular-foliation propositions. -/
def bringSurfaceSmoothnessWitness :
    BringSurfaceSmoothness
      BringTransverseInP4 BringIntrinsicResolution BringRegularC5Foliation :=
  ⟨bring_transverse_in_P4, bring_intrinsic_resolution, bring_regular_c5_foliation⟩

/-- **Unconditional proof of `prop:brings-smoothness-resolution`.**
    Establishes (1) transversality of the three power-sum constraints in
    $\mathbb{P}^4(\mathbb{C})$ via the $3 \times 3$ Vandermonde Jacobian minors,
    (2) the intrinsic quadratic branch-point resolution in the local difference
    coordinate $\delta = x_i - x_j$, and (3) fixed-point-freeness of the non-trivial
    $C_5$ phase action on $w_1 \neq 0$. -/
theorem brings_smoothness_resolution :
    BringTransverseInP4 ∧ BringIntrinsicResolution ∧ BringRegularC5Foliation :=
  ⟨bring_transverse_in_P4, bring_intrinsic_resolution, bring_regular_c5_foliation⟩

end QOU.BringsSurface
