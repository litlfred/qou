import QOU.MassTheory.BorelProperTimeMoment
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.PSeries

/-!
# Borel variable ↔ proper time: the analytic face

The moment integral `∫₀^∞ s^{n+1}·e^{−s}·ds/s = n!`, the Carleman minorant and divergence for
`{k!}`, and the instance-free conjecture carrier `BindingKernelSchwingerRepresentation` with its
conditional reduction `kernel_moments_eq_schwinger`. Split out of
`QOU.MassTheory.BorelProperTimeMoment`, which keeps the unit-forcing identity and the
generic-field bar-covariance falsifier outside the transcendental boundary. Namespace and
declaration names are unchanged; the full discussion and references are in that file's header.

-- Ref: [leitner2026] mass-theory, conj:qdifference-kernel-prolongation-symbol;
--      classical determinacy: B. Simon, Adv. Math. 137 (1998) 82–203.
-/

namespace QOU.Archimedean.BorelProperTimeMoment

open MeasureTheory

/-! ## Attack A — the provable moment core (wall-side, ℝ) -/

/-- **The moment identity.** The `(n+1)`-st `ds/s`-moment of the unit
(`c = 1`) Schwinger kernel is exactly `n!`:
`∫₀^∞ s^{n+1}·e^{−s}·ds/s = Γ(n+1) = n!`. Unshifted this is
`∫ s^n e^{−s} ds/s = (n−1)!` for `n ≥ 1` — the keystone-forced binding
normalizer `N(n) = (n−1)!` (`KeystoneBridgeC1Binding`) IS the moment data
of the loop's proper-time kernel. Index shifted by 1 so ℕ-arithmetic stays
subtraction-free. -/
theorem moment_eq_factorial (n : ℕ) :
    ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Real.exp (-s) / s
      = (n.factorial : ℝ) := by
  have h1 : ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Real.exp (-s) / s
      = ∫ s in Set.Ioi (0:ℝ), Real.exp (-s) * s ^ (((n:ℝ) + 1) - 1) := by
    refine setIntegral_congr_fun measurableSet_Ioi ?_
    intro s hs
    have hs0 : (0:ℝ) < s := hs
    have he : ((n:ℝ) + 1) - 1 = ((n : ℕ) : ℝ) := by ring
    simp only [he, Real.rpow_natCast, pow_succ]
    field_simp [hs0.ne']
  rw [h1, ← Real.Gamma_eq_integral (by positivity : (0:ℝ) < (n:ℝ) + 1)]
  exact_mod_cast Real.Gamma_nat_eq_factorial n

/-- **The Carleman minorant.** The Carleman term of the shifted moment
sequence `{k!}` dominates the harmonic term: `1/k ≤ (k!)^{−1/(2k)}`, from
the exact bound `k! ≤ k^{2k}`. This is the quantitative heart of
Carleman's condition for `{k!}`. -/
theorem carleman_minorant (k : ℕ) (hk : 1 ≤ k) :
    (1 : ℝ) / k ≤ (k.factorial : ℝ) ^ (-(1 / (2 * (k : ℝ)))) := by
  have hk0 : (0:ℝ) < k := by exact_mod_cast hk
  have hfac0 : (0:ℝ) ≤ (k.factorial : ℝ) := by positivity
  have hx : (0:ℝ) ≤ 1 / (2 * (k:ℝ)) := by positivity
  have hnat : k.factorial ≤ k ^ (2 * k) :=
    le_trans (Nat.factorial_le_pow k) (Nat.pow_le_pow_right hk (by omega))
  have hle : (k.factorial : ℝ) ≤ (k:ℝ) ^ (2 * k) := by exact_mod_cast hnat
  have hax : (k.factorial : ℝ) ^ (1 / (2 * (k:ℝ))) ≤ (k:ℝ) := by
    have h1 : (k.factorial : ℝ) ^ (1 / (2 * (k:ℝ)))
        ≤ ((k:ℝ) ^ (2 * k)) ^ (1 / (2 * (k:ℝ))) :=
      Real.rpow_le_rpow hfac0 hle hx
    have h2 : ((k:ℝ) ^ (2 * k) : ℝ) = (k:ℝ) ^ ((2 * k : ℕ) : ℝ) :=
      (Real.rpow_natCast _ _).symm
    have h3 : ((k:ℝ) ^ ((2 * k : ℕ) : ℝ)) ^ (1 / (2 * (k:ℝ)))
        = (k:ℝ) ^ (((2 * k : ℕ) : ℝ) * (1 / (2 * (k:ℝ)))) :=
      (Real.rpow_mul (le_of_lt hk0) _ _).symm
    have h4 : ((2 * k : ℕ) : ℝ) * (1 / (2 * (k:ℝ))) = 1 := by
      have hne : (2 * (k:ℝ)) ≠ 0 := by positivity
      push_cast
      field_simp
    rw [h2, h3, h4, Real.rpow_one] at h1
    exact h1
  have haxpos : (0:ℝ) < (k.factorial : ℝ) ^ (1 / (2 * (k:ℝ))) :=
    Real.rpow_pos_of_pos (by positivity) _
  have hdiv := one_div_le_one_div_of_le haxpos hax
  rw [Real.rpow_neg hfac0, ← one_div]
  exact hdiv

/-- **Carleman divergence.** `Σ_k (k!)^{−1/(2k)} = ∞` (stated as
non-summability): the Carleman condition for the Stieltjes moment problem
of `{k!}` HOLDS. By the classical Carleman–Stieltjes determinacy theorem
(Simon 1998; NOT formalized in Mathlib — this lemma proves its exact
hypothesis) the problem is determinate: `e^{−s}·ds` is the UNIQUE positive
measure on `(0,∞)` with moments `{k!}`. -/
theorem carleman_divergence :
    ¬ Summable (fun k : ℕ => (k.factorial : ℝ) ^ (-(1 / (2 * (k : ℝ))))) := by
  intro hsum
  have h : Summable (fun k : ℕ => (1:ℝ) / k) := by
    refine Summable.of_nonneg_of_le (fun k => by positivity)
      (fun k => ?_) hsum
    rcases Nat.eq_zero_or_pos k with hk | hk
    · subst hk
      simp
    · exact carleman_minorant k hk
  exact Real.not_summable_one_div_natCast h

/-! ## The conditional reduction class (§3b-tax; content-bearing; NO
instance — the fields are the conjecture's two open hypotheses) -/

/-- **Conjecture carrier (primary; no instance exists or may be created).**
The binding Borel resummation kernel — the weight `K_b(s)·ds` realizing the
keystone-forced normalizer as `N(n+1) = n! = ∫ s^{n+1}·K_b(s)·ds/s` — is a
positive measure on `(0,∞)` with exactly the factorial `ds/s`-moments.
These fields are the two OPEN hypotheses that Attack A reduces the
conjecture "binding Borel variable = loop proper time" to:

* `positive` + `integrable` — the substrate resummation weight is a genuine
  positive measure (open: no corpus result establishes it; the C1 carrier
  coefficients `I(n)/n!` are NOT themselves a Stieltjes moment sequence —
  log-convexity fails at `m = 2` — so this is a statement about the
  kernel, not the coefficients);
* `moments` — its moments are the keystone-forced factorials (open: the
  keystone forces the NORMALIZER values `(n−1)!`, not that they arise as
  the moments of the substrate's own kernel).

Given both, `kernel_moments_eq_schwinger` below (proved) plus classical
Carleman–Stieltjes determinacy (`carleman_divergence` proves its
hypothesis; the theorem itself is classical, unformalized) force
`K_b(s)·ds = e^{−s}·ds` — the identification. Creating an `instance` of
this class would launder the conjecture (§Axiomatization is NOT a Proof);
none exists. -/
class BindingKernelSchwingerRepresentation (Kb : ℝ → ℝ) : Prop where
  positive : ∀ s : ℝ, 0 < s → 0 ≤ Kb s
  integrable : ∀ n : ℕ,
    IntegrableOn (fun s : ℝ => s ^ (n + 1) * Kb s / s) (Set.Ioi 0)
  moments : ∀ n : ℕ,
    ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Kb s / s = (n.factorial : ℝ)

/-- **The reduction, proved conditionally.** Any kernel satisfying the
hypothesis class is moment-indistinguishable from the unit Schwinger
kernel: every `ds/s`-moment agrees. The remaining gap to
`K_b = e^{−s}` (a.e.) is exactly the classical determinacy step whose
Carleman hypothesis `carleman_divergence` proves — so the conjecture is
reduced to the class's two named hypotheses, nothing else. -/
theorem kernel_moments_eq_schwinger (Kb : ℝ → ℝ)
    [BindingKernelSchwingerRepresentation Kb] (n : ℕ) :
    ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Kb s / s
      = ∫ s in Set.Ioi (0:ℝ), s ^ (n + 1) * Real.exp (-s) / s := by
  rw [BindingKernelSchwingerRepresentation.moments (Kb := Kb) n,
    moment_eq_factorial]

end QOU.Archimedean.BorelProperTimeMoment
