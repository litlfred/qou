import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Tactic

/-!
# Neumann–Zagier parity: the deformation potential is even, so there is no u³ rung

For a one-cusped hyperbolic manifold under Dehn-surgery deformation with
meridian log-holonomy `u`, Neumann–Zagier prove the longitude log-holonomy
`v(u)` is an ODD function of `u`; consequently the NZ potential `Φ(u)`
(with `v = ∂Φ/∂u` up to normalisation) and the complex-volume expansion
`CVol(u) = Vol(0) − (τ/4)u² + …` are EVEN in `u`.

-- Ref: [neumann-zagier1985] Volumes of hyperbolic three-manifolds — see content/schema/references.ts

**Physical consequence (the prune this file certifies):** the geometric NZ
series contains NO odd-order term — in particular no `u³` rung.  Any
identification of the Q_β bar-odd target `r = S·u_ladder³` with a *geometric
NZ coefficient* is therefore structurally excluded (scope-(b), invariant =
parity, proved below); the odd object must come from OUTSIDE the classical
NZ potential (1-loop torsion / higher-loop / Φ_b phase accumulation), or
from the distinction between the ladder variable `u_ladder = b·ℏ_q²` and the
NZ deformation variable `u_NZ = log-holonomy` (two different `u`'s — the
2026-07-11 #3562 NZ-u³ proposal conflated them and is corrected by this
file).

We carry the potential as a polynomial truncation `Φ ∈ R[X]` (any finite
NZ-series truncation); evenness as a function is `Φ.comp (−X) = Φ`, which
over an infinite integral domain is equivalent to pointwise evenness.  The
algebra is generic (§7c): `[CommRing R]`, with two-torsion-freeness exactly
where the parity cancellation needs it.
-/

namespace QOU.Knot.NeumannZagierParity

open Polynomial

variable {R : Type*} [CommRing R]

/-- Coefficient of the reflected polynomial: `(p.comp (−X)).coeff n = (−1)ⁿ · p.coeff n`. -/
theorem coeff_comp_neg_X (p : R[X]) (n : ℕ) :
    (p.comp (-X)).coeff n = (-1) ^ n * p.coeff n := by
  induction p using Polynomial.induction_on' with
  | add p q hp hq => simp [add_comp, coeff_add, hp, hq, mul_add]
  | monomial k a =>
    have hC : ((-X : R[X]) ^ k) = C ((-1 : R) ^ k) * X ^ k := by
      rw [neg_pow, map_pow, map_neg, map_one]
    simp only [monomial_comp, hC, ← mul_assoc, ← C_mul, coeff_C_mul, coeff_X_pow,
      coeff_monomial]
    by_cases h : n = k
    · subst h; simp [mul_comm]
    · have h' : ¬k = n := fun hk => h hk.symm
      simp [h, h']

/-- An even polynomial (as a function: `p(−X) = p`) has vanishing odd
    coefficients, provided `R` has no 2-torsion. -/
theorem coeff_odd_eq_zero_of_comp_neg_eq (p : R[X])
    (heven : p.comp (-X) = p) (h2 : ∀ r : R, 2 * r = 0 → r = 0)
    {n : ℕ} (hn : Odd n) : p.coeff n = 0 := by
  have h : (p.comp (-X)).coeff n = p.coeff n := by rw [heven]
  rw [coeff_comp_neg_X, hn.neg_one_pow] at h
  have : (2 : R) * p.coeff n = 0 := by linear_combination -h
  exact h2 _ this

/-- Two-torsion-freeness from the standard typeclasses: in a ring with no
    zero divisors where `2 ≠ 0`, `2·r = 0` forces `r = 0`. -/
theorem two_torsion_free_of_noZeroDivisors [NoZeroDivisors R] [NeZero (2 : R)]
    (r : R) (h : 2 * r = 0) : r = 0 :=
  (mul_eq_zero.mp h).resolve_left (NeZero.ne (2 : R))

/-- **Neumann–Zagier even-potential data (§3b-cond hypothesis class).**

    The single field is NZ85's parity result for the chosen truncation: the
    potential is even as a function.  An instance for a specific manifold is
    supplied by the NZ theorem (v(u) odd); we do not fabricate one here. -/
-- Ref: [neumann-zagier1985] (v(u) is odd in u; the potential is even)
class NeumannZagierEvenPotential (R : Type*) [CommRing R] where
  /-- A finite truncation of the NZ potential series in the deformation
      variable `u`. -/
  potential : R[X]
  /-- NZ parity: the potential is even as a function of `u`. -/
  even_potential : potential.comp (-X) = potential

/-- **No cubic rung (derived).**  The geometric NZ series has no `u³` term:
    parity kills every odd order.  This is the proved invariant behind the
    scope-(b) exclusion of "S·u³ as a geometric NZ coefficient". -/
theorem no_cubic_rung (R : Type*) [CommRing R] [NoZeroDivisors R] [NeZero (2 : R)]
    [nz : NeumannZagierEvenPotential R] :
    nz.potential.coeff 3 = 0 :=
  coeff_odd_eq_zero_of_comp_neg_eq nz.potential nz.even_potential
    two_torsion_free_of_noZeroDivisors (by norm_num)

/-- Every odd order vanishes, not just the cubic. -/
theorem no_odd_rung (R : Type*) [CommRing R] [NoZeroDivisors R] [NeZero (2 : R)]
    [nz : NeumannZagierEvenPotential R] {n : ℕ} (hn : Odd n) :
    nz.potential.coeff n = 0 :=
  coeff_odd_eq_zero_of_comp_neg_eq nz.potential nz.even_potential
    two_torsion_free_of_noZeroDivisors hn

end QOU.Knot.NeumannZagierParity
