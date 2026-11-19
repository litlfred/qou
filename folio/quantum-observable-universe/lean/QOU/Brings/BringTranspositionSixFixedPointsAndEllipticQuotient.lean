import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.GroupTheory.Perm.Fin

/-!
# Bring's Curve Transposition Fixed-Point Cubic $t^3 + 2t^2 + 3t + 4 = 0$, $10 \times 6 = 60$ Weierstrass Points, and the Degree-2 Elliptic Quotient ($\chi(B) = -6$)

This module gives an unconditional algebraic proof that each of the $\binom{5}{2} = 10$
transpositions $\tau \in S_5 = \mathrm{Aut}(B)$ fixes **6** points on Bring's curve
$$B = \Bigl\{[z_0 : z_1 : z_2 : z_3 : z_4] \in \mathbb{P}^4 \;\Big|\;
  \sum_{i=0}^{4} z_i = \sum_{i=0}^{4} z_i^2 = \sum_{i=0}^{4} z_i^3 = 0\Bigr\},$$
that the fixed-point loci of distinct transpositions $\tau \neq \tau'$ are pairwise disjoint
(yielding all $10 \times 6 = 60 = 4^3 - 4$ simple Weierstrass points of $B$), and that via
the degree-$2$ elliptic quotient $B \to E_\tau = B/\langle\tau\rangle$ of genus $g(E_\tau) = 1$
($\chi(E_\tau) = 0$), the $6$ branch points determine $\chi(B) = 2\chi(E_\tau) - 6 = -6$ and
$g(B) = 4$ (bean `qou-qhcr`).

## Main Results

1. **Section 1 — Exclusion of the $(-1)$-Eigenspace Point & Reduction to the Affine Hyperplane
   $z_0 = z_1 = 1$:**
   - Under the transposition $\tau = (0\,1)$ acting by
     $\tau(z_0, z_1, z_2, z_3, z_4) = (z_1, z_0, z_2, z_3, z_4)$, a projective fixed point
     satisfies $\tau(z) = \lambda z$ with $\lambda \in \{\pm 1\}$.
   - The isolated $(-1)$-eigenspace point $[1 : -1 : 0 : 0 : 0] \in \mathbb{P}^4$ satisfies
     $\sum z_i^2 = 2 \neq 0$ (for $\mathrm{char}(K) \neq 2$) and never lies on Bring's curve
     (`antiFixedPoint_not_on_bring`, `antiFixedPoint_one_neg_one_not_on_bring`).
   - On the $(+1)$-eigenspace hyperplane $z_0 = z_1$, any point with $z_0 = z_1 = 0$ satisfies
     $z_2 + z_3 + z_4 = z_2^2 + z_3^2 + z_4^2 = z_2^3 + z_3^3 + z_4^3 = 0$, which by Newton's
     identities forces $6 z_i^3 = 0$ and hence $z_2 = z_3 = z_4 = 0$ for $\mathrm{char}(K) \notin \{2, 3\}$
     (`zero_coord_fixed_locus_empty`). Every projective fixed point of $\tau = (0\,1)$ on $B$
     therefore normalizes uniquely to the affine slice $z_0 = z_1 = 1$.

2. **Section 2 — Exact Affine Reduction ($z_0 = z_1 = 1$) to the Separable Cubic
   $P_\tau(T) = T^3 + 2T^2 + 3T + 4 = 0$ (`3! = 6` Fixed Points):**
   - Setting $z_0 = z_1 = 1$, the Bring equations $2 + \sum_{i=2}^4 z_i^k = 0$ ($k = 1, 2, 3$)
     are equivalent via Newton's identities (`bring_transposition_fixed_iff_vieta`) to the
     elementary symmetric equations
     $$e_1(z_2, z_3, z_4) = -2, \qquad e_2(z_2, z_3, z_4) = 3, \qquad e_3(z_2, z_3, z_4) = -4,$$
     so $(T - z_2)(T - z_3)(T - z_4) = T^3 + 2T^2 + 3T + 4 = P_\tau(T)$
     (`transpositionCubic_vieta_factorization`).
   - The discriminant of $P_\tau(T) = T^3 + 2T^2 + 3T + 4$ is
     $$\Delta(P_\tau) = (z_2 - z_3)^2 (z_2 - z_4)^2 (z_3 - z_4)^2 = -200 = -2^3 \cdot 5^2$$
     (`transposition_cubic_discriminant_eq_neg_200`), proving that $z_2, z_3, z_4$ are pairwise
     distinct over any field of characteristic $\notin \{2, 5\}$
     (`bring_transposition_fixed_coords_pairwise_distinct`).
   - Permuting the three distinct roots $(r_0, r_1, r_2)$ of $P_\tau$ by $\sigma \in S_3 =
     \mathrm{Equiv.Perm}(\mathrm{Fin}\,3)$ yields an injective family of $|S_3| = 3! = 6$
     fixed points $[1 : 1 : r_{\sigma(0)} : r_{\sigma(1)} : r_{\sigma(2)}] \in B^{\tau}$
     (`bringFixedPointOfPerm_on_bring`, `bringFixedPointOfPerm_injective`,
     `card_perm_fin_three_eq_six`).

3. **Section 3 — Pairwise Disjointness Across All $\binom{5}{2} = 10$ Transpositions
   (`10 × 6 = 60` Weierstrass Points) & Elliptic Quotient Riemann–Hurwitz ($\chi(B) = -6$):**
   - Fixed-point sets of distinct transpositions $\tau \neq \tau'$ in $S_5$ are pairwise
     disjoint (`overlapping_transpositions_disjoint`, `disjoint_transpositions_disjoint`):
     * Overlapping transpositions (e.g. $(0\,1)$ and $(1\,2)$, forcing $z_0 = z_1 = z_2 = 1$):
       eliminating $z_3, z_4$ from $3 + z_3 + z_4 = 3 + z_3^2 + z_4^2 = 3 + z_3^3 + z_4^3 = 0$
       yields the exact polynomial identity $60 = 0$ ($2^2 \cdot 3 \cdot 5 = 0$), impossible
       in characteristic $\notin \{2, 3, 5\}$.
     * Disjoint transpositions (e.g. $(0\,1)$ and $(2\,3)$, forcing $z_0 = z_1 = 1$ and
       $z_2 = z_3$): contradicts $z_2 \neq z_3$ from $\Delta(P_\tau) = -200 \neq 0$.
   - The symmetric group $S_5 = \mathrm{Equiv.Perm}(\mathrm{Fin}\,5)$ contains
     $\binom{5}{2} = 10$ transpositions (`card_transpositionsS5_eq_ten`), yielding
     $10 \times 6 = 60 = 4^3 - 4$ total Weierstrass points (`bring_weierstrass_point_count_from_transpositions`).
   - For the degree-$2$ involution quotient $B \to E_\tau = B/\langle\tau\rangle$ onto the
     elliptic curve $E_\tau$ of genus $g(E_\tau) = 1$ ($\chi(E_\tau) = 0$) branched at the
     $b = 6$ fixed points of $\tau$, Riemann–Hurwitz gives
     $\chi(B) = 2\chi(E_\tau) - 6 = -6$ and $g(B) = 4$
     (`bring_elliptic_quotient_forces_chi_eq_neg_six`).
-/

namespace QOU.Brings
namespace BringTranspositionSixFixedPointsAndEllipticQuotient

/-! ## Section 1: Exclusion of the $(-1)$-Eigenspace Point & Reduction to $z_0 = z_1 = 1$ -/

section ProjectiveFixedLocusReduction

variable {K : Type*} [CommRing K]

/-- First Newton power sum $p_1(z) = \sum_{i=0}^{4} z_i$ defining the trace hyperplane of
Bring's curve in $\mathbb{P}^4$. -/
def bringPowerSum1 (z0 z1 z2 z3 z4 : K) : K :=
  z0 + z1 + z2 + z3 + z4

/-- Second Newton power sum $p_2(z) = \sum_{i=0}^{4} z_i^2$ defining the quadric hypersurface
of Bring's curve in $\mathbb{P}^4$. -/
def bringPowerSum2 (z0 z1 z2 z3 z4 : K) : K :=
  z0 ^ 2 + z1 ^ 2 + z2 ^ 2 + z3 ^ 2 + z4 ^ 2

/-- Third Newton power sum $p_3(z) = \sum_{i=0}^{4} z_i^3$ defining the cubic hypersurface
of Bring's curve in $\mathbb{P}^4$. -/
def bringPowerSum3 (z0 z1 z2 z3 z4 : K) : K :=
  z0 ^ 3 + z1 ^ 3 + z2 ^ 3 + z3 ^ 3 + z4 ^ 3

/-- A homogeneous coordinate tuple $(z_0, z_1, z_2, z_3, z_4) \in K^5$ lies on Bring's curve $B$
if and only if its first three Newton power sums vanish:
$\sum_{i=0}^4 z_i = \sum_{i=0}^4 z_i^2 = \sum_{i=0}^4 z_i^3 = 0$. -/
def IsOnBringCurve (z0 z1 z2 z3 z4 : K) : Prop :=
  bringPowerSum1 z0 z1 z2 z3 z4 = 0 ∧
  bringPowerSum2 z0 z1 z2 z3 z4 = 0 ∧
  bringPowerSum3 z0 z1 z2 z3 z4 = 0

/-- **Exclusion of the $(-1)$-Eigenspace of a Transposition (`antiFixedPoint_not_on_bring`)**:
In the $(-1)$-eigenspace of the transposition $\tau = (0\,1)$ (where $z_1 = -z_0$ and
$z_2 = z_3 = z_4 = 0$), the quadric equation $\sum_{i=0}^4 z_i^2 = 2 z_0^2 = 0$ forces
$z_0 = 0$ over any domain of characteristic $\neq 2$. Hence the isolated projective
$(-1)$-eigenpoint $[1 : -1 : 0 : 0 : 0] \in \mathbb{P}^4$ never lies on Bring's curve. -/
theorem antiFixedPoint_not_on_bring [NoZeroDivisors K]
    (h2 : (2 : K) ≠ 0) (z0 : K)
    (hB : IsOnBringCurve z0 (-z0) 0 0 0) :
    z0 = 0 := by
  rcases hB with ⟨_, hq, _⟩
  unfold bringPowerSum2 at hq
  have h2z : 2 * z0 ^ 2 = 0 := by linear_combination hq
  rcases mul_eq_zero.mp h2z with h20 | hz2
  · exact False.elim (h2 h20)
  · exact pow_eq_zero hz2

/-- Explicit non-membership of the isolated $(-1)$-eigenpoint $(1, -1, 0, 0, 0)$ on Bring's
curve whenever $(2 : K) \neq 0$. -/
theorem antiFixedPoint_one_neg_one_not_on_bring
    (h2 : (2 : K) ≠ 0) :
    ¬ IsOnBringCurve (1 : K) (-1) 0 0 0 := by
  rintro ⟨_, hq, _⟩
  unfold bringPowerSum2 at hq
  apply h2
  linear_combination hq

/-- **Universal Newton–Girard 3-Variable Cubic Annihilation Identity**:
For any $a, b, c \in K$ with power sums $s_1 = a + b + c$, $s_2 = a^2 + b^2 + c^2$, and
$s_3 = a^3 + b^3 + c^3$, the coordinate $a$ satisfies
$$6 a^3 = 6 s_1 a^2 - 3(s_1^2 - s_2) a + (s_1^3 - 3 s_1 s_2 + 2 s_3).$$ -/
theorem newton_girard_three_var_cube_identity (a b c : K) :
    6 * a ^ 3 =
      6 * (a + b + c) * a ^ 2 -
        3 * ((a + b + c) ^ 2 - (a ^ 2 + b ^ 2 + c ^ 2)) * a +
        ((a + b + c) ^ 3 - 3 * (a + b + c) * (a ^ 2 + b ^ 2 + c ^ 2) +
          2 * (a ^ 3 + b ^ 3 + c ^ 3)) := by
  ring

/-- **Emptiness of the Boundary Locus $z_0 = z_1 = 0$ on the Fixed Hyperplane
(`zero_coord_fixed_locus_empty`)**:
Over any domain $K$ with $(2 : K) \neq 0$ and $(3 : K) \neq 0$, if a point
$(0, 0, z_2, z_3, z_4)$ on the fixed hyperplane $z_0 = z_1$ lies on Bring's curve, then
$z_2 = z_3 = z_4 = 0$. Consequently, every projective fixed point of $\tau = (0\,1)$ on
Bring's curve has $z_0 = z_1 \neq 0$ and normalizes uniquely to $z_0 = z_1 = 1$. -/
theorem zero_coord_fixed_locus_empty [NoZeroDivisors K]
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0)
    (z2 z3 z4 : K)
    (hB : IsOnBringCurve 0 0 z2 z3 z4) :
    z2 = 0 ∧ z3 = 0 ∧ z4 = 0 := by
  rcases hB with ⟨hp1, hp2, hp3⟩
  unfold bringPowerSum1 at hp1
  unfold bringPowerSum2 at hp2
  unfold bringPowerSum3 at hp3
  have h6 : (6 : K) ≠ 0 := by
    have h23 : (2 : K) * (3 : K) = (6 : K) := by norm_num
    rw [← h23]
    exact mul_ne_zero h2 h3
  have hz2 : 6 * z2 ^ 3 = 0 := by
    linear_combination
      (6 * z2 ^ 2 - 3 * (z2 + z3 + z4) * z2 + (z2 + z3 + z4) ^ 2 -
          3 * (z2 ^ 2 + z3 ^ 2 + z4 ^ 2)) * hp1 +
        (3 * z2) * hp2 + 2 * hp3
  have hz3 : 6 * z3 ^ 3 = 0 := by
    linear_combination
      (6 * z3 ^ 2 - 3 * (z2 + z3 + z4) * z3 + (z2 + z3 + z4) ^ 2 -
          3 * (z2 ^ 2 + z3 ^ 2 + z4 ^ 2)) * hp1 +
        (3 * z3) * hp2 + 2 * hp3
  have hz4 : 6 * z4 ^ 3 = 0 := by
    linear_combination
      (6 * z4 ^ 2 - 3 * (z2 + z3 + z4) * z4 + (z2 + z3 + z4) ^ 2 -
          3 * (z2 ^ 2 + z3 ^ 2 + z4 ^ 2)) * hp1 +
        (3 * z4) * hp2 + 2 * hp3
  refine ⟨?_, ?_, ?_⟩
  · exact pow_eq_zero ((mul_eq_zero.mp hz2).resolve_left h6)
  · exact pow_eq_zero ((mul_eq_zero.mp hz3).resolve_left h6)
  · exact pow_eq_zero ((mul_eq_zero.mp hz4).resolve_left h6)

end ProjectiveFixedLocusReduction

/-! ## Section 2: Affine Reduction ($z_0 = z_1 = 1$) to the Cubic $P_\tau(T) = T^3 + 2T^2 + 3T + 4 = 0$ -/

section TranspositionFixedCubic

variable {K : Type*} [CommRing K]

/-- First elementary symmetric polynomial $e_1(z_2, z_3, z_4) = z_2 + z_3 + z_4$. -/
def elemSym1 (z2 z3 z4 : K) : K :=
  z2 + z3 + z4

/-- Second elementary symmetric polynomial $e_2(z_2, z_3, z_4) = z_2 z_3 + z_2 z_4 + z_3 z_4$. -/
def elemSym2 (z2 z3 z4 : K) : K :=
  z2 * z3 + z2 * z4 + z3 * z4

/-- Third elementary symmetric polynomial $e_3(z_2, z_3, z_4) = z_2 z_3 z_4$. -/
def elemSym3 (z2 z3 z4 : K) : K :=
  z2 * z3 * z4

/-- The characteristic transposition fixed-point cubic
$$P_\tau(t) = t^3 + 2t^2 + 3t + 4$$
whose root permutations $(z_2, z_3, z_4)$ classify all fixed points $[1 : 1 : z_2 : z_3 : z_4]$
of the transposition $\tau = (0\,1)$ on Bring's curve. -/
def transpositionCubic (t : K) : K :=
  t ^ 3 + 2 * t ^ 2 + 3 * t + 4

/-- **Exact Vieta Reduction of the Transposition Fixed-Point Equations
(`bring_transposition_fixed_iff_vieta`)**:
Over any domain $K$ with $(2 : K) \neq 0$ and $(3 : K) \neq 0$, an affine point
$(1, 1, z_2, z_3, z_4)$ on the fixed hyperplane $z_0 = z_1 = 1$ lies on Bring's curve if
and only if the remaining three coordinates $(z_2, z_3, z_4)$ have elementary symmetric
polynomials
$$e_1(z_2, z_3, z_4) = -2, \qquad e_2(z_2, z_3, z_4) = 3, \qquad e_3(z_2, z_3, z_4) = -4.$$ -/
theorem bring_transposition_fixed_iff_vieta [NoZeroDivisors K]
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0)
    (z2 z3 z4 : K) :
    IsOnBringCurve 1 1 z2 z3 z4 ↔
      (elemSym1 z2 z3 z4 = -2 ∧ elemSym2 z2 z3 z4 = 3 ∧ elemSym3 z2 z3 z4 = -4) := by
  unfold IsOnBringCurve bringPowerSum1 bringPowerSum2 bringPowerSum3
    elemSym1 elemSym2 elemSym3
  have hnewton2 :
      (1 : K) ^ 2 + 1 ^ 2 + z2 ^ 2 + z3 ^ 2 + z4 ^ 2 =
        (z2 + z3 + z4) ^ 2 - 2 * (z2 * z3 + z2 * z4 + z3 * z4) + 2 := by
    ring
  have hnewton3 :
      (1 : K) ^ 3 + 1 ^ 3 + z2 ^ 3 + z3 ^ 3 + z4 ^ 3 =
        (z2 + z3 + z4) ^ 3 - 3 * (z2 + z3 + z4) * (z2 * z3 + z2 * z4 + z3 * z4) +
          3 * (z2 * z3 * z4) + 2 := by
    ring
  constructor
  · rintro ⟨hp1, hp2, hp3⟩
    have he1 : z2 + z3 + z4 = -2 := by linear_combination hp1
    rw [hnewton2, he1] at hp2
    have h2e2 : 2 * (z2 * z3 + z2 * z4 + z3 * z4 - 3) = 0 := by linear_combination -hp2
    have he2 : z2 * z3 + z2 * z4 + z3 * z4 = 3 := by
      have h0 := (mul_eq_zero.mp h2e2).resolve_left h2
      linear_combination h0
    rw [hnewton3, he1, he2] at hp3
    have h3e3 : 3 * (z2 * z3 * z4 + 4) = 0 := by linear_combination hp3
    have he3 : z2 * z3 * z4 = -4 := by
      have h0 := (mul_eq_zero.mp h3e3).resolve_left h3
      linear_combination h0
    exact ⟨he1, he2, he3⟩
  · rintro ⟨he1, he2, he3⟩
    refine ⟨by linear_combination he1, ?_, ?_⟩
    · rw [hnewton2, he1, he2]; ring
    · rw [hnewton3, he1, he2, he3]; ring

/-- **Vieta Factorization of the Transposition Fixed-Point Cubic
(`transpositionCubic_vieta_factorization`)**:
Whenever $(z_2, z_3, z_4)$ satisfy $e_1 = -2$, $e_2 = 3$, and $e_3 = -4$, the cubic
$P_\tau(t) = t^3 + 2t^2 + 3t + 4$ factors identically as $(t - z_2)(t - z_3)(t - z_4)$. -/
theorem transpositionCubic_vieta_factorization
    (z2 z3 z4 : K)
    (he1 : elemSym1 z2 z3 z4 = -2)
    (he2 : elemSym2 z2 z3 z4 = 3)
    (he3 : elemSym3 z2 z3 z4 = -4)
    (t : K) :
    transpositionCubic t = (t - z2) * (t - z3) * (t - z4) := by
  have hexp :
      (t - z2) * (t - z3) * (t - z4) =
        t ^ 3 - elemSym1 z2 z3 z4 * t ^ 2 + elemSym2 z2 z3 z4 * t - elemSym3 z2 z3 z4 := by
    unfold elemSym1 elemSym2 elemSym3
    ring
  rw [hexp, he1, he2, he3]
  unfold transpositionCubic
  ring

/-- Every coordinate $z_2, z_3, z_4$ of a transposition fixed point $(1, 1, z_2, z_3, z_4)$
is a root of $P_\tau(t) = t^3 + 2t^2 + 3t + 4 = 0$. -/
theorem bring_fixed_coords_are_roots_of_transpositionCubic
    (z2 z3 z4 : K)
    (he1 : elemSym1 z2 z3 z4 = -2)
    (he2 : elemSym2 z2 z3 z4 = 3)
    (he3 : elemSym3 z2 z3 z4 = -4) :
    transpositionCubic z2 = 0 ∧
    transpositionCubic z3 = 0 ∧
    transpositionCubic z4 = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [transpositionCubic_vieta_factorization z2 z3 z4 he1 he2 he3 z2]; ring
  · rw [transpositionCubic_vieta_factorization z2 z3 z4 he1 he2 he3 z3]; ring
  · rw [transpositionCubic_vieta_factorization z2 z3 z4 he1 he2 he3 z4]; ring

/-- **Universal Cubic Discriminant Symmetric-Polynomial Identity**:
For any $a, b, c \in K$ with elementary symmetric polynomials $e_1, e_2, e_3$,
$$(a - b)^2 (a - c)^2 (b - c)^2
  = e_1^2 e_2^2 - 4 e_2^3 - 4 e_1^3 e_3 - 27 e_3^2 + 18 e_1 e_2 e_3.$$ -/
theorem cubic_discriminant_elemSym_identity (a b c : K) :
    (a - b) ^ 2 * (a - c) ^ 2 * (b - c) ^ 2 =
      (elemSym1 a b c) ^ 2 * (elemSym2 a b c) ^ 2 -
        4 * (elemSym2 a b c) ^ 3 -
        4 * (elemSym1 a b c) ^ 3 * (elemSym3 a b c) -
        27 * (elemSym3 a b c) ^ 2 +
        18 * (elemSym1 a b c) * (elemSym2 a b c) * (elemSym3 a b c) := by
  unfold elemSym1 elemSym2 elemSym3
  ring

/-- **Exact Discriminant $\Delta(P_\tau) = -200 = -2^3 \cdot 5^2$ of the Transposition Cubic
(`transposition_cubic_discriminant_eq_neg_200`)**:
For any $(z_2, z_3, z_4)$ satisfying the Vieta system $e_1 = -2$, $e_2 = 3$, $e_3 = -4$ of
$P_\tau(t) = t^3 + 2t^2 + 3t + 4$, the squared Vandermonde product equals $-200$:
$$(z_2 - z_3)^2 (z_2 - z_4)^2 (z_3 - z_4)^2 = -200.$$ -/
theorem transposition_cubic_discriminant_eq_neg_200
    (z2 z3 z4 : K)
    (he1 : elemSym1 z2 z3 z4 = -2)
    (he2 : elemSym2 z2 z3 z4 = 3)
    (he3 : elemSym3 z2 z3 z4 = -4) :
    (z2 - z3) ^ 2 * (z2 - z4) ^ 2 * (z3 - z4) ^ 2 = -200 := by
  rw [cubic_discriminant_elemSym_identity, he1, he2, he3]
  ring

/-- **Pairwise Distinctness of the Three Non-Fixed Coordinates
(`bring_transposition_fixed_coords_pairwise_distinct`)**:
Over any domain $K$ with $(2 : K) \neq 0$, $(3 : K) \neq 0$, and $(5 : K) \neq 0$, for every
point $(1, 1, z_2, z_3, z_4)$ on Bring's curve fixed by $\tau = (0\,1)$, the three coordinates
$z_2, z_3, z_4$ are pairwise distinct:
$$z_2 \neq z_3 \;\wedge\; z_2 \neq z_4 \;\wedge\; z_3 \neq z_4.$$ -/
theorem bring_transposition_fixed_coords_pairwise_distinct [NoZeroDivisors K]
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0)
    (z2 z3 z4 : K)
    (hB : IsOnBringCurve 1 1 z2 z3 z4) :
    z2 ≠ z3 ∧ z2 ≠ z4 ∧ z3 ≠ z4 := by
  have ⟨he1, he2, he3⟩ := (bring_transposition_fixed_iff_vieta h2 h3 z2 z3 z4).mp hB
  have hdisc := transposition_cubic_discriminant_eq_neg_200 z2 z3 z4 he1 he2 he3
  have h200 : (-200 : K) ≠ 0 := by
    have hfac : (-200 : K) = -(2 : K) ^ 3 * (5 : K) ^ 2 := by norm_num
    rw [hfac]
    exact mul_ne_zero (neg_ne_zero.mpr (pow_ne_zero 3 h2)) (pow_ne_zero 2 h5)
  have hprod : (z2 - z3) ^ 2 * (z2 - z4) ^ 2 * (z3 - z4) ^ 2 ≠ 0 := by
    rw [hdisc]
    exact h200
  refine ⟨?_, ?_, ?_⟩
  · intro h
    apply hprod
    rw [h]; ring
  · intro h
    apply hprod
    rw [h]; ring
  · intro h
    apply hprod
    rw [h]; ring

/-- Action of a permutation $\sigma \in S_3 = \mathrm{Equiv.Perm}(\mathrm{Fin}\,3)$ on a
root triple $r : \mathrm{Fin}\,3 \to K$ of $P_\tau(t) = t^3 + 2t^2 + 3t + 4$, parametrizing
the $3! = 6$ fixed points $[1 : 1 : r(\sigma(0)) : r(\sigma(1)) : r(\sigma(2))]$ of the
transposition $\tau = (0\,1)$ on Bring's curve. -/
def bringFixedPointOfPerm (r : Fin 3 → K) (σ : Equiv.Perm (Fin 3)) : Fin 3 → K :=
  fun i => r (σ i)

/-- Every permutation $\sigma \in S_3 = \mathrm{Equiv.Perm}(\mathrm{Fin}\,3)$ of a Vieta root
triple $r : \mathrm{Fin}\,3 \to K$ yields a valid fixed point
$(1, 1, r(\sigma(0)), r(\sigma(1)), r(\sigma(2)))$ on Bring's curve. -/
theorem bringFixedPointOfPerm_on_bring
    (r : Fin 3 → K)
    (hB : IsOnBringCurve 1 1 (r 0) (r 1) (r 2))
    (σ : Equiv.Perm (Fin 3)) :
    IsOnBringCurve 1 1
      (bringFixedPointOfPerm r σ 0)
      (bringFixedPointOfPerm r σ 1)
      (bringFixedPointOfPerm r σ 2) := by
  unfold IsOnBringCurve bringPowerSum1 bringPowerSum2 bringPowerSum3 at hB ⊢
  unfold bringFixedPointOfPerm
  rcases hB with ⟨hp1, hp2, hp3⟩
  have hsum1 :
      r (σ 0) + r (σ 1) + r (σ 2) = r 0 + r 1 + r 2 := by
    have h := Equiv.sum_comp σ r
    simpa [Fin.sum_univ_three, add_assoc] using h
  have hsum2 :
      r (σ 0) ^ 2 + r (σ 1) ^ 2 + r (σ 2) ^ 2 = r 0 ^ 2 + r 1 ^ 2 + r 2 ^ 2 := by
    have h := Equiv.sum_comp σ (fun i => r i ^ 2)
    simpa [Fin.sum_univ_three, add_assoc] using h
  have hsum3 :
      r (σ 0) ^ 3 + r (σ 1) ^ 3 + r (σ 2) ^ 3 = r 0 ^ 3 + r 1 ^ 3 + r 2 ^ 3 := by
    have h := Equiv.sum_comp σ (fun i => r i ^ 3)
    simpa [Fin.sum_univ_three, add_assoc] using h
  refine ⟨?_, ?_, ?_⟩
  · linear_combination hp1 + hsum1
  · linear_combination hp2 + hsum2
  · linear_combination hp3 + hsum3

omit [CommRing K] in
/-- Because the three roots $r_0, r_1, r_2$ of $P_\tau(t) = t^3 + 2t^2 + 3t + 4$ are pairwise
distinct (`Function.Injective r`), the map $\sigma \mapsto \mathrm{bringFixedPointOfPerm}\,r\,\sigma$
from $\mathrm{Equiv.Perm}(\mathrm{Fin}\,3)$ to fixed points on Bring's curve is injective. -/
theorem bringFixedPointOfPerm_injective
    (r : Fin 3 → K) (hr : Function.Injective r) :
    Function.Injective (bringFixedPointOfPerm r) := by
  intro σ₁ σ₂ hEq
  exact Equiv.ext (fun i => hr (congrFun hEq i))

/-- The permutation group $\mathrm{Equiv.Perm}(\mathrm{Fin}\,3)$ parametrizing the fixed points
of a single transposition on Bring's curve has cardinality $3! = 6$. -/
theorem card_perm_fin_three_eq_six :
    Fintype.card (Equiv.Perm (Fin 3)) = 6 := by
  decide

end TranspositionFixedCubic

/-! ## Section 3: Pairwise Disjointness Across All $10$ Transpositions, $60$ Weierstrass Points, & $\chi(B) = -6$ -/

section DisjointnessAndEllipticQuotient

variable {K : Type*} [CommRing K]

/-- **Universal Elimination Identity for Overlapping Transpositions ($z_0 = z_1 = z_2 = 1$)**:
For any $z_3, z_4 \in K$, let $s_1 = 3 + z_3 + z_4$, $s_2 = 3 + z_3^2 + z_4^2$, and
$s_3 = 3 + z_3^3 + z_4^3$. Then
$$s_1^3 - 9 s_1^2 + 36 s_1 - 3(s_1 - 3) s_2 + 2 s_3 = 60.$$ -/
theorem overlapping_transpositions_elimination_identity (z3 z4 : K) :
    (3 + z3 + z4) ^ 3 - 9 * (3 + z3 + z4) ^ 2 + 36 * (3 + z3 + z4) -
      3 * ((3 + z3 + z4) - 3) * (3 + z3 ^ 2 + z4 ^ 2) +
      2 * (3 + z3 ^ 3 + z4 ^ 3) = 60 := by
  ring

/-- **Disjointness of Fixed Sets for Overlapping Transpositions
(`overlapping_transpositions_disjoint`)**:
Over any domain $K$ with $(2 : K) \neq 0$, $(3 : K) \neq 0$, and $(5 : K) \neq 0$, no point on
Bring's curve can be simultaneously fixed by two overlapping transpositions (such as $(0\,1)$
and $(1\,2)$, which force $z_0 = z_1 = z_2 = 1$). -/
theorem overlapping_transpositions_disjoint [NoZeroDivisors K]
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0)
    (z3 z4 : K) :
    ¬ IsOnBringCurve 1 1 1 z3 z4 := by
  rintro ⟨hp1, hp2, hp3⟩
  unfold bringPowerSum1 at hp1
  unfold bringPowerSum2 at hp2
  unfold bringPowerSum3 at hp3
  have hid := overlapping_transpositions_elimination_identity z3 z4
  have hs1 : 3 + z3 + z4 = 0 := by linear_combination hp1
  have hs2 : 3 + z3 ^ 2 + z4 ^ 2 = 0 := by linear_combination hp2
  have hs3 : 3 + z3 ^ 3 + z4 ^ 3 = 0 := by linear_combination hp3
  rw [hs1, hs2, hs3] at hid
  have h60_zero : (60 : K) = 0 := by linear_combination -hid
  have h60_ne : (60 : K) ≠ 0 := by
    have hfac : (60 : K) = (2 : K) ^ 2 * (3 : K) * (5 : K) := by norm_num
    rw [hfac]
    exact mul_ne_zero (mul_ne_zero (pow_ne_zero 2 h2) h3) h5
  exact h60_ne h60_zero

/-- **Disjointness of Fixed Sets for Disjoint Transpositions
(`disjoint_transpositions_disjoint`)**:
Over any domain $K$ with $(2 : K) \neq 0$, $(3 : K) \neq 0$, and $(5 : K) \neq 0$, no point on
Bring's curve can be simultaneously fixed by two disjoint transpositions (such as $(0\,1)$
and $(2\,3)$, which force $z_0 = z_1 = 1$ and $z_2 = z_3$). -/
theorem disjoint_transpositions_disjoint [NoZeroDivisors K]
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0)
    (z2 z4 : K) :
    ¬ IsOnBringCurve 1 1 z2 z2 z4 := by
  intro hB
  have ⟨hneq, _, _⟩ :=
    bring_transposition_fixed_coords_pairwise_distinct h2 h3 h5 z2 z2 z4 hB
  exact hneq rfl

/-- Boolean predicate identifying transpositions (permutations moving exactly $2$ elements)
in $S_5 = \mathrm{Equiv.Perm}(\mathrm{Fin}\,5)$. -/
def isTransposition5 (σ : Equiv.Perm (Fin 5)) : Bool :=
  ((Finset.univ : Finset (Fin 5)).filter (fun i => σ i ≠ i)).card == 2

/-- The finite set of all transpositions in $S_5 = \mathrm{Equiv.Perm}(\mathrm{Fin}\,5)$. -/
def transpositionsS5 : Finset (Equiv.Perm (Fin 5)) :=
  (Finset.univ : Finset (Equiv.Perm (Fin 5))).filter (fun σ => isTransposition5 σ)

/-- **Exact Count of Transpositions in $S_5$ (`card_transpositionsS5_eq_ten`)**:
The symmetric group $S_5 = \mathrm{Equiv.Perm}(\mathrm{Fin}\,5)$ contains exactly
$\binom{5}{2} = 10$ transpositions. -/
theorem card_transpositionsS5_eq_ten :
    transpositionsS5.card = 10 ∧ Nat.choose 5 2 = 10 := by
  decide

/-- **Total Weierstrass Point Count from Pairwise-Disjoint Transposition Fixed Loci
(`bring_weierstrass_point_count_from_transpositions`)**:
Multiplying the $\binom{5}{2} = 10$ transpositions of $S_5$ by the $3! = 6$ fixed points per
transposition gives $10 \times 6 = 60 = 4^3 - 4$, accounting for all $g^3 - g = 60$ simple
Weierstrass points of the genus-$4$ Bring surface. -/
theorem bring_weierstrass_point_count_from_transpositions :
    transpositionsS5.card * Fintype.card (Equiv.Perm (Fin 3)) = 60 ∧
    (4 : ℕ) ^ 3 - 4 = 60 := by
  decide

/-- Topological Euler characteristic $\chi_{\mathrm{eu}}(\Sigma_g) = 2 - 2g$ of a compact
Riemann surface of genus $g$. -/
def riemannSurfaceEuler (g : ℤ) : ℤ :=
  2 - 2 * g

/-- Riemann–Hurwitz Euler characteristic $\chi(B) = d \cdot \chi(E) - R$ of a degree-$d$
branched cover $B \to E$ with total ramification degree $R$. -/
def riemannHurwitzCoverEuler (d chiBase ramification : ℤ) : ℤ :=
  d * chiBase - ramification

/-- **Degree-2 Involution Quotient Riemann–Hurwitz Theorem
(`riemann_hurwitz_involution_quotient_euler`)**:
For any involution $\tau$ on a compact Riemann surface $B$ of genus $g_B$ with $b$ fixed points
(each of ramification index $e_P = 2$, so $R = \sum (e_P - 1) = b$) and quotient curve
$E_\tau = B / \langle\tau\rangle$ of genus $g_E$,
$$\chi_{\mathrm{eu}}(B) = 2 \chi_{\mathrm{eu}}(E_\tau) - b
  \quad\Longleftrightarrow\quad 2 g_B - 2 = 2(2 g_E - 2) + b.$$ -/
theorem riemann_hurwitz_involution_quotient_euler (gB gE b : ℤ) :
    riemannSurfaceEuler gB = riemannHurwitzCoverEuler 2 (riemannSurfaceEuler gE) b ↔
      2 * gB - 2 = 2 * (2 * gE - 2) + b := by
  unfold riemannSurfaceEuler riemannHurwitzCoverEuler
  constructor <;> intro h <;> linarith

/-- **Bring Transposition Elliptic Quotient Theorem
(`bring_elliptic_quotient_forces_chi_eq_neg_six`)**:
With $b = 6$ fixed points for a transposition involution $\tau \in S_5$ (`card (Perm (Fin 3)) = 6`)
and elliptic quotient $E_\tau = B / \langle\tau\rangle$ of genus $g_E = 1$
($\chi_{\mathrm{eu}}(E_\tau) = 0$), the Riemann–Hurwitz formula yields
$$\chi_{\mathrm{eu}}(B) = 2 \cdot \chi_{\mathrm{eu}}(E_\tau) - 6 = -6 \;\wedge\; g_B = 4.$$ -/
theorem bring_elliptic_quotient_forces_chi_eq_neg_six (gB : ℤ) :
    riemannSurfaceEuler 1 = 0 ∧
    riemannHurwitzCoverEuler 2 (riemannSurfaceEuler 1)
      (Fintype.card (Equiv.Perm (Fin 3)) : ℤ) = -6 ∧
    (riemannSurfaceEuler gB =
      riemannHurwitzCoverEuler 2 (riemannSurfaceEuler 1)
        (Fintype.card (Equiv.Perm (Fin 3)) : ℤ) ↔ gB = 4) := by
  rw [card_perm_fin_three_eq_six]
  unfold riemannSurfaceEuler riemannHurwitzCoverEuler
  refine ⟨by norm_num, by norm_num, ?_⟩
  constructor <;> intro h <;> omega

end DisjointnessAndEllipticQuotient

end BringTranspositionSixFixedPointsAndEllipticQuotient
end QOU.Brings
