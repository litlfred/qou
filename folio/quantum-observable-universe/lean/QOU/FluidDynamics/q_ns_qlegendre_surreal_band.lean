import QOU.FluidDynamics.q_ns_qlegendre_classical_limit
import QOU.FluidDynamics.surreal_enstrophy_finite_modes

/-!
# QOU.FluidDynamics.q_ns_qlegendre_surreal_band — the coupled band at an infinitesimal `q − 1`

Work over a linearly ordered field `K` that may be non-archimedean (a surreal line), with
`q = 1 + δ` and `δ` a positive infinitesimal in the sense of
`QOU.FluidDynamics.Infinitesimal` (`n·|δ| < 1` for every natural `n`).

**Main result** (`Rc_ge_of_infinitesimal`). For **every** mode `s : ℕ`,
`Rc q s ≥ (s+1)²/32`. So no standard mode is decoupled: the normalised squared raising
coupling at `q = 1 + δ` is bounded below, mode by mode, by half of the bound that holds at
`q = 1` (`Rc_one_ge`), and in particular it is never infinitesimal
(`Rc_not_infinitesimal`) and is unbounded in `s`.

**What this means for the surreal blowup picture.** Over the standard indices `s : ℕ` the
`q = 1 + δ` coupling behaves classically. Any cutoff of the coupled band (where the coupling
becomes infinitesimal) therefore sits at an *infinite* index, of order `log(1/δ)/δ`; that index
is not a natural number and is not reachable by `s : ℕ`. Locating it needs hypernatural
indices, which this file does not introduce. The file asserts nothing about the
`N → ∞` limit, about energy transfer, or about the classical PDE.

On an archimedean `K` (e.g. `ℝ`) the only infinitesimal is `0`, so `q = 1` and the theorem
reduces to a weakening of `Rc_one_ge`.

## References
- [leitner2026] fluid-dynamics/regularity-breakdown (Part A); appendix-surreals/
  surreal-blowup-calculus; QOU/FluidDynamics/q_ns_qlegendre_classical_limit (`Rc_ge`);
  QOU/FluidDynamics/surreal_enstrophy_finite_modes (infinitesimal calculus).
-/

namespace QOU.FluidDynamics.QLegendreClassical

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

open QOU.FluidDynamics

/-- Powers of `1 + δ` deviate from `1` by an infinitesimal (fixed exponent). -/
theorem pow_one_add_infinitesimal {δ : K} (hδ : Infinitesimal δ) (j : ℕ) :
    Infinitesimal ((1 + δ) ^ j - 1) := by
  have h := pow_one_sub_infinitesimal hδ.neg j
  simpa [sub_neg_eq_add] using h

omit [IsStrictOrderedRing K] in
/-- An infinitesimal is below `1` in absolute value. -/
theorem abs_lt_one_of_infinitesimal {x : K} (hx : Infinitesimal x) : |x| < 1 := by
  simpa using hx 1

/-- **Every standard mode stays coupled at `q = 1 + δ`.** If `q − 1` is infinitesimal and
`q ≥ 1`, then `Rc q s ≥ (s+1)²/32` for every `s : ℕ`. -/
theorem Rc_ge_of_infinitesimal (q : Kˣ) (hq : 1 ≤ (q : K))
    (hδ : Infinitesimal ((q : K) - 1)) (s : ℕ) :
    ((s : K) + 1) ^ 2 / 32 ≤ Rc q s := by
  have h := Rc_ge q hq s
  set X : K := ((q : K) * q) ^ (10 * s + 14) with hX
  have hXeq : X = (1 + ((q : K) - 1)) ^ (2 * (10 * s + 14)) := by
    rw [hX, ← sq, ← pow_mul]; ring_nf
  have hX1 : |X - 1| < 1 := by
    rw [hXeq]; exact abs_lt_one_of_infinitesimal (pow_one_add_infinitesimal hδ _)
  have hXlt : X < 2 := by linarith [le_abs_self (X - 1)]
  have hP : 1 ≤ (q : K) * q := one_le_mul_of_one_le_of_one_le hq hq
  have hXpos : 0 < X := by rw [hX]; exact pow_pos (by linarith) _
  have hpos : 0 < ((s : K) + 1) ^ 2 / 16 := by positivity
  have hRpos : 0 < Rc q s := by
    by_contra hc
    push_neg at hc
    have : Rc q s * X ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hc hXpos.le
    linarith
  have : Rc q s * X ≤ Rc q s * 2 := mul_le_mul_of_nonneg_left hXlt.le hRpos.le
  have h2 : ((s : K) + 1) ^ 2 / 32 = (((s : K) + 1) ^ 2 / 16) / 2 := by ring
  rw [h2, div_le_iff₀ (by norm_num : (0 : K) < 2)]
  linarith

/-- **No standard mode is infinitesimally coupled.** Under the same hypotheses, `Rc q s` is
not infinitesimal for any `s : ℕ`. -/
theorem Rc_not_infinitesimal (q : Kˣ) (hq : 1 ≤ (q : K))
    (hδ : Infinitesimal ((q : K) - 1)) (s : ℕ) : ¬ Infinitesimal (Rc q s) := by
  intro hR
  have hge := Rc_ge_of_infinitesimal q hq hδ s
  have hs : (1 : K) / 32 ≤ ((s : K) + 1) ^ 2 / 32 := by
    have : (1 : K) ≤ ((s : K) + 1) ^ 2 := by
      have : (1 : K) ≤ (s : K) + 1 := by linarith [(Nat.cast_nonneg s : (0 : K) ≤ s)]
      nlinarith
    linarith
  have h32 := hR 32
  have hab : Rc q s ≤ |Rc q s| := le_abs_self _
  push_cast at h32
  nlinarith

end QOU.FluidDynamics.QLegendreClassical
