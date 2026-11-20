import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Order.Filter.AtTopBot.Basic
import Mathlib.MeasureTheory.Integral.CircleIntegral
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

/-!
# QOU.BraidKnot.terms_2_6_higher_operations — conjecture carrier

Content block
[`conj:terms-2-6-higher-operations`](../../../quantum-observable-universe/mass-theory/terms-2-6-higher-operations.md).

**Conjecture, not a proposition (owner, 2026-11-20, bean `qou-6qbv`).** The
block reads Term 2 of the unified knot-mass formula as the `k → ∞` limit of
the level-`k` Jones–Wenzl traces, and Term 6 as the sum over `ℓ ≥ 2` of the
root-of-unity residues `Res_{q = ζ_ℓ}[Φ_q · tr_{M,ℓ}(T_w)] / (q₀ − ζ_ℓ)`.

## What changed

Until 2026-11-20 this file carried a context class whose fields were
`target_page_term_2 = 1 ∧ hochschild_arity_term_2 = 2` (and the same for
term 6) on free `ℕ` fields, and a `def` that projected them back. Any instance
picked the numbers, so it asserted nothing. It also encoded the Hochschild
higher-operation route, which the block's own author note records as **closed**
(`HH¹(H₃(R, q)) = 0` at generic `q`).

## What is stated now

`Terms26HigherOperations q₀ term2 levelTrace integrand residue term6` is the
conjecture about the named quantities: the level traces converge to Term 2;
for each `ℓ ≥ 2`, `residue ℓ` is the residue of `integrand ℓ` at the primitive
root `ζ_ℓ = exp(2πi/ℓ)`; and `Σ_{ℓ≥2} residue ℓ / (q₀ − ζ_ℓ)` sums to Term 6.
It is a `Prop`-valued class with no instance — the open state. The quantities
are parameters, so a witness has to be about these particular numbers, not
ones the instance chooses.

**2026-11-20 correction (W8b, owner-approved item 1).** The first version of
this class summed real `residue (ℓ + 2)` with no denominator. The block's
formula has the factor `1/(q₀ − ζ_ℓ)`, and the `ζ_ℓ` are complex, so that
version stated a different series. The residues, the summands and Term 6 are
now complex, `ζ_ℓ` is concrete, and the residue is tied to its integrand.
The residue is defined without a simple-pole assumption, as
`(2πi)⁻¹ ∮_{|z − ζ| = ε} F` for every sufficiently small `ε > 0`.

**Not encoded.** The integrands `Φ_q · tr_{M,ℓ}(T_w)`, the level traces and
Term 2 are parameters, not constructed from a braid word; the Habiro
cyclotomic-basis clause of the block is not encoded.

`ℝ` / `ℂ` are deliberate (§7c): both readings are limits, a contour integral
and an infinite sum at the archimedean substrate point.

## What is proved

`term2_eq_of_conj` and `term6_eq_of_conj`: under the conjecture, Term 2 and
Term 6 are *determined* by the level traces and the residues (limits and sums
are unique). `not_conj_of_divergent`: the conjecture is not automatic.
`cyclotomicRoot_ne_substrate`: for `q₀ > 1` no denominator `q₀ − ζ_ℓ`
vanishes, so the Term-6 series is well formed.
-/

namespace QOU.BraidKnot

open Filter Topology

/-- The primitive `ℓ`-th root of unity `ζ_ℓ = exp(2πi/ℓ)`. -/
noncomputable def cyclotomicRoot (ℓ : ℕ) : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / ℓ)

/-- `r` is the residue of `F` at `ζ`: for every sufficiently small `ε > 0`,
`(2πi)⁻¹ ∮_{|z − ζ| = ε} F z dz = r`. No simple-pole assumption. -/
def IsResidueAt (F : ℂ → ℂ) (ζ r : ℂ) : Prop :=
  ∀ᶠ ε in 𝓝[>] (0 : ℝ), (2 * Real.pi * Complex.I)⁻¹ * (∮ z in C(ζ, ε), F z) = r

/-- `‖ζ_ℓ‖ = 1`. -/
theorem norm_cyclotomicRoot (ℓ : ℕ) : ‖cyclotomicRoot ℓ‖ = 1 := by
  unfold cyclotomicRoot
  have h : (2 * Real.pi * Complex.I / ℓ : ℂ) = ((2 * Real.pi / ℓ : ℝ) : ℂ) * Complex.I := by
    push_cast; ring
  rw [h, Complex.norm_exp_ofReal_mul_I]

/-- For a substrate point `q₀ > 1`, no denominator `q₀ − ζ_ℓ` of the Term-6
series vanishes: `‖q₀‖ = q₀ > 1 = ‖ζ_ℓ‖`. -/
theorem cyclotomicRoot_ne_substrate {q₀ : ℝ} (hq : 1 < q₀) (ℓ : ℕ) :
    (q₀ : ℂ) - cyclotomicRoot ℓ ≠ 0 := by
  intro h
  have h' : (q₀ : ℂ) = cyclotomicRoot ℓ := sub_eq_zero.mp h
  have hn := congrArg (‖·‖) h'
  simp only [norm_cyclotomicRoot, Complex.norm_real, Real.norm_eq_abs] at hn
  rw [abs_of_pos (by linarith)] at hn
  linarith

/-- **Conjecture (Terms 2 and 6).** `levelTrace k` is the level-`k`
Jones–Wenzl trace contributing to Term 2, and Term 2 is its `k → ∞` limit.
`integrand ℓ` is `Φ_q · tr_{M,ℓ}(T_w)` as a function of `q`, `residue ℓ` is
its residue at `ζ_ℓ`, and Term 6 is `Σ_{ℓ ≥ 2} residue ℓ / (q₀ − ζ_ℓ)`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/terms-2-6-higher-operations
-- Ref: [habiro2004] Habiro, "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
class Terms26HigherOperations (q₀ term2 : ℝ) (levelTrace : ℕ → ℝ)
    (integrand : ℕ → ℂ → ℂ) (residue : ℕ → ℂ) (term6 : ℂ) : Prop where
  /-- Term 2 is the infinite-level Wedderburn limit. -/
  term2_wedderburn_limit : Tendsto levelTrace atTop (𝓝 term2)
  /-- `residue ℓ` is the residue of the level-`ℓ` integrand at `ζ_ℓ`, `ℓ ≥ 2`. -/
  residue_spec :
    ∀ ℓ : ℕ, 2 ≤ ℓ → IsResidueAt (integrand ℓ) (cyclotomicRoot ℓ) (residue ℓ)
  /-- Term 6 is the root-of-unity residue sum
  `Σ_{ℓ ≥ 2} Res_{q = ζ_ℓ}[Φ_q · tr_{M,ℓ}(T_w)] / (q₀ − ζ_ℓ)`. -/
  term6_residue_sum :
    HasSum (fun ℓ : ℕ => residue (ℓ + 2) / ((q₀ : ℂ) - cyclotomicRoot (ℓ + 2))) term6

/-- Under the conjecture, Term 2 is determined by the level traces. -/
theorem term2_eq_of_conj {q₀ t2 t2' : ℝ} {t6 t6' : ℂ} {levelTrace : ℕ → ℝ}
    {integrand : ℕ → ℂ → ℂ} {residue : ℕ → ℂ}
    (h : Terms26HigherOperations q₀ t2 levelTrace integrand residue t6)
    (h' : Terms26HigherOperations q₀ t2' levelTrace integrand residue t6') : t2 = t2' :=
  tendsto_nhds_unique h.term2_wedderburn_limit h'.term2_wedderburn_limit

/-- Under the conjecture, Term 6 is determined by the residues. -/
theorem term6_eq_of_conj {q₀ t2 t2' : ℝ} {t6 t6' : ℂ} {levelTrace : ℕ → ℝ}
    {integrand : ℕ → ℂ → ℂ} {residue : ℕ → ℂ}
    (h : Terms26HigherOperations q₀ t2 levelTrace integrand residue t6)
    (h' : Terms26HigherOperations q₀ t2' levelTrace integrand residue t6') : t6 = t6' :=
  h.term6_residue_sum.unique h'.term6_residue_sum

/-- The conjecture is not automatic: a divergent level-trace sequence admits no
Term 2 at all, so `Terms26HigherOperations` fails for every candidate value. -/
theorem not_conj_of_divergent {q₀ t2 : ℝ} {t6 : ℂ} {integrand : ℕ → ℂ → ℂ}
    {residue : ℕ → ℂ} :
    ¬ Terms26HigherOperations q₀ t2 (fun k => (k : ℝ)) integrand residue t6 := by
  intro h
  exact not_tendsto_nhds_of_tendsto_atTop tendsto_natCast_atTop_atTop t2
    h.term2_wedderburn_limit

end QOU.BraidKnot
