/-
# The ladder phase is not a constant-residue holonomy angle — by the logarithm's
# functional equation, not by transcendence

Bean `qou-pdix` (child of `qou-cds1`), route 5.

Route 5 is the surviving route: derive `α` as the holonomy angle of a connection
whose monodromy reproduces the `H₃(q)` braiding.  Kohno–Drinfeld **fixes the
scale** rather than leaving it free — braiding is `P exp(ħt/2)` with `t`
eigenvalues `±1`, matching the Hecke eigenvalues `{q, −q⁻¹}` exactly when
`q = e^{ħ/2}` — so `ħ = 2 ln q` and a **constant-residue** holonomy angle is
`c · ln q` for some constant `c`.

The obvious objection is transcendence: `α` is an algebraic function of `q`
(a rational function of `√q` under convention C, of `q` under D) while `c ln q`
is transcendental.  That argument is correct but needs transcendence theory.
**This file uses an elementary substitute that needs none.**

`ln` satisfies `ln (q²) = 2 ln q`, so **every** function of the form `c · ln`
satisfies `f (q²) = 2 f q`, whatever `c` is.  That is an algebraic identity, and
`α` fails it:

  `α_C (q²) − 2 α_C q  =  −(2q^{7/2} − 2q^{3/2} + q⁵ − 2q⁴ − 3q³ + 3q² + 2q − 1) / (2q²(q+1))`
  `α_D (q²) − 2 α_D q  =  (q−1)²(q+1)(q⁹+q⁸+2q⁶+q⁵+3q⁴−q³+q²−q+1) / (2q²(q²+1)(q⁴+1))`

both nonzero.  Witnesses at a single point suffice and are what is proved below.

**Scope — scope-(b), invariant named.**  This excludes `α = c · ln q` for every
constant `c`, in both conventions, hence every **constant-residue** Kohno–Drinfeld
holonomy angle.  It does **not** exclude a connection whose residues depend on
`q`, nor a non-flat or genuinely `q`-dependent-parameter construction; those
remain route 5's live space.  What it removes is precisely the class the
branch-3 acceptance test was built around.

**Consequence for that acceptance test.**  Together with
`BarEvenForcesStationarity` (part 1 is a bar-symmetry test in disguise, hence
vacuous) and the measurement that entry (7)'s *"EXACT: target / Re(log-gap) =
−1/4"* is a **0.32 %** approximation for `α_C` (22 % for `α_D`, 8.5 % for the
required phase) and provably cannot be exact, **both discriminating parts of the
test are defective**.  The `−1/4` is not an identity to be accounted for.

Companion probe:
`computations/qbeta/qbeta_phase_fails_log_functional_equation_probe.py`.
-/
import Mathlib.Tactic

namespace QOU.QBeta.LogFunEq

/-- **Any constant multiple of an additive function satisfies `f (q*q) = 2 f q`.**

`ln` is the case at hand (`ln (q²) = 2 ln q`), and a constant-residue
Kohno–Drinfeld holonomy angle is `c · ln q`.  The hypothesis is only additivity
on the diagonal, so the lemma applies to any logarithm-like scale, and `c` is
arbitrary — which is what makes the exclusion below hold for *every* `c` at
once. -/
theorem const_mul_additive_doubles {L : ℝ → ℝ}
    (hL : ∀ x : ℝ, L (x * x) = L x + L x) (c : ℝ) (q : ℝ) :
    (fun x => c * L x) (q * q) = 2 * (fun x => c * L x) q := by
  simp only [hL q]
  ring

/-- The ladder phase under **convention D**, `α_D = (z_D − 1)·h/2` with
`z_D = q³/(q²+1)` and `h = q − q⁻¹`. -/
noncomputable def alphaD (q : ℝ) : ℝ :=
  (q ^ 3 / (q ^ 2 + 1) - 1) * (q - q⁻¹) / 2

/-- The ladder phase under **convention C**, in the square-root variable
`u = √q`: `z_C = u/(u²+1)` and `h = u² − u⁻²`.  Writing it in `u` keeps the
statement algebraic; `q ↦ q²` corresponds to `u ↦ u²`. -/
noncomputable def alphaC (u : ℝ) : ℝ :=
  (u / (u ^ 2 + 1) - 1) * (u ^ 2 - (u ^ 2)⁻¹) / 2

/-- `α_D (2) = 9/20`. -/
theorem alphaD_two : alphaD 2 = 9 / 20 := by
  unfold alphaD; norm_num

/-- `α_D (4) = 705/136`. -/
theorem alphaD_four : alphaD 4 = 705 / 136 := by
  unfold alphaD; norm_num

/-- **`α_D` fails the doubling identity at `q = 2`**: `α_D(2·2) = 705/136`
while `2·α_D(2) = 9/10`. -/
theorem alphaD_fails_doubling : alphaD (2 * 2) ≠ 2 * alphaD 2 := by
  rw [show (2 : ℝ) * 2 = 4 by norm_num, alphaD_four, alphaD_two]
  norm_num

/-- `α_C (2) = −9/8`. -/
theorem alphaC_two : alphaC 2 = -(9 / 8) := by
  unfold alphaC; norm_num

/-- `α_C (4) = −195/32`. -/
theorem alphaC_four : alphaC 4 = -(195 / 32) := by
  unfold alphaC; norm_num

/-- **`α_C` fails the doubling identity at `u = 2`**: `α_C(2·2) = −195/32`
while `2·α_C(2) = −9/4 = −72/32`. -/
theorem alphaC_fails_doubling : alphaC (2 * 2) ≠ 2 * alphaC 2 := by
  rw [show (2 : ℝ) * 2 = 4 by norm_num, alphaC_four, alphaC_two]
  norm_num

/-- **The exclusion, convention D.**  For no constant `c` and no additive `L`
is `α_D` equal to `c · L` — in particular `α_D ≠ c · ln`, so `α_D` is not a
constant-residue Kohno–Drinfeld holonomy angle. -/
theorem alphaD_not_const_mul_additive :
    ¬ ∃ (L : ℝ → ℝ) (c : ℝ), (∀ x : ℝ, L (x * x) = L x + L x) ∧
        ∀ x : ℝ, alphaD x = c * L x := by
  rintro ⟨L, c, hL, hEq⟩
  have h4 : alphaD (2 * 2) = 2 * alphaD 2 := by
    rw [hEq, hEq]
    have := const_mul_additive_doubles hL c 2
    simpa using this
  exact alphaD_fails_doubling h4

/-- **The exclusion, convention C.**  Same statement in the square-root
variable, where `q ↦ q²` is `u ↦ u²`. -/
theorem alphaC_not_const_mul_additive :
    ¬ ∃ (L : ℝ → ℝ) (c : ℝ), (∀ x : ℝ, L (x * x) = L x + L x) ∧
        ∀ x : ℝ, alphaC x = c * L x := by
  rintro ⟨L, c, hL, hEq⟩
  have h4 : alphaC (2 * 2) = 2 * alphaC 2 := by
    rw [hEq, hEq]
    have := const_mul_additive_doubles hL c 2
    simpa using this
  exact alphaC_fails_doubling h4

end QOU.QBeta.LogFunEq
