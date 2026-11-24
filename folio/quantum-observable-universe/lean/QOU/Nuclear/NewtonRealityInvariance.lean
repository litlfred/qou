import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

set_option autoImplicit false

/-!
# QOU.QBeta.NewtonRealityInvariance — real seeds cannot reach the cusp

The structural invariant behind the pole→cusp negative of
`computations/qbeta/qbeta_c3_barodd_pole_seed_newton_probe.py` (finding A:
a literal real Φ_q-pole seed flows to the golden branch, never the cusp) and
`computations/qbeta/qbeta_c3_pole_sign_complexification_probe.py` (the pole's
own sign, phase π, does not help): **a Newton iteration whose numerator and
denominator commute with complex conjugation, started at a real seed of either
sign, has all-real iterates; a convergent all-real sequence has a real limit;
so it can never converge to the cusp shape `e^{iπ/3}` (imaginary part
`√3/2 ≠ 0`).**

This upgrades the computed per-`k` negatives to a scope-(b) exclusion of the
whole real-seed class, per AGENTS.md §Before declaring "refuted" — the proved
invariant is conjugation equivariance plus closedness of the real axis.

## Honesty (hypothesis-carrying, conditional-proved ≠ premise-established)

`ConjEquivariant` is an explicit hypothesis. Real-coefficient rational maps —
in particular the 4₁ gluing polynomial `z(z−1)·w(w−1) − 1` at real meridian
and its derivative — satisfy it, and the concrete polynomial instance is
provided (`conjEquivariant_realPolynomial`). Nothing here claims which map
the substrate assigns; the open link `u(q₀)` is untouched.

## References

- [neumann-zagier1985] Neumann & Zagier, "Volumes of hyperbolic
  three-manifolds," Topology 24 (1985). https://doi.org/10.1016/0040-9383(85)90004-7
- [leitner2026] docs/audits/2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md
-/

namespace QOU.QBeta.NewtonRealityInvariance

open Complex Filter Function

local notation "conj'" => (starRingEnd ℂ)

/-- A map `ℂ → ℂ` that commutes with complex conjugation. Real-coefficient
polynomials and their ratios satisfy this. -/
def ConjEquivariant (f : ℂ → ℂ) : Prop :=
  ∀ z, conj' (f z) = f (conj' z)

/-- The Newton step `z ↦ z − f z / g z` (with `g` the derivative in the
intended reading — kept abstract; division by zero is junk-total as usual). -/
noncomputable def newtonStep (f g : ℂ → ℂ) (z : ℂ) : ℂ :=
  z - f z / g z

/-- The Newton step of conjugation-equivariant maps is conjugation-equivariant. -/
theorem conjEquivariant_newtonStep {f g : ℂ → ℂ}
    (hf : ConjEquivariant f) (hg : ConjEquivariant g) :
    ConjEquivariant (newtonStep f g) := by
  intro z
  simp only [newtonStep, map_sub, map_div₀, hf z, hg z]

/-- A conjugation-equivariant map sends real points to real points. -/
theorem conjEquivariant_maps_real {f : ℂ → ℂ} (hf : ConjEquivariant f)
    {z : ℂ} (hz : conj' z = z) : conj' (f z) = f z := by
  rw [hf z, hz]

/-- All Newton iterates of a real seed are real (conjugation-fixed). -/
theorem iterate_real {f g : ℂ → ℂ}
    (hf : ConjEquivariant f) (hg : ConjEquivariant g)
    {z₀ : ℂ} (hz : conj' z₀ = z₀) (n : ℕ) :
    conj' ((newtonStep f g)^[n] z₀) = (newtonStep f g)^[n] z₀ := by
  induction n with
  | zero => simpa using hz
  | succ n ih =>
      rw [iterate_succ_apply']
      exact conjEquivariant_maps_real
        (conjEquivariant_newtonStep hf hg) ih

/-- The limit of a convergent sequence of real (conjugation-fixed) complex
numbers is real: conjugation is continuous, so both `conj ∘ u` and `u` tend
to `conj L` and `L`, and they are equal. -/
theorem limit_real {u : ℕ → ℂ} (hu : ∀ n, conj' (u n) = u n)
    {L : ℂ} (hL : Tendsto u atTop (nhds L)) : conj' L = L := by
  have h₁ : Tendsto (fun n => conj' (u n)) atTop (nhds (conj' L)) :=
    (Complex.continuous_conj.tendsto L).comp hL
  have h₂ : Tendsto (fun n => conj' (u n)) atTop (nhds L) := by
    simpa only [hu] using hL
  exact tendsto_nhds_unique h₁ h₂

/-- **Real seeds cannot reach a non-real target.** If a Newton iteration with
conjugation-equivariant data starts at a real seed (either sign) and
converges, its limit is real — in particular it is not any point with
non-zero imaginary part, such as the 4₁ cusp shape `e^{iπ/3}`
(`Im = √3/2`). -/
theorem real_seed_limit_ne_of_im_ne {f g : ℂ → ℂ}
    (hf : ConjEquivariant f) (hg : ConjEquivariant g)
    {z₀ : ℂ} (hz : z₀.im = 0) {L w : ℂ}
    (hL : Tendsto (fun n => (newtonStep f g)^[n] z₀) atTop (nhds L))
    (hw : w.im ≠ 0) : L ≠ w := by
  have hz' : conj' z₀ = z₀ := Complex.conj_eq_iff_im.mpr hz
  have hlim : conj' L = L :=
    limit_real (fun n => iterate_real hf hg hz' n) hL
  have hLim : L.im = 0 := Complex.conj_eq_iff_im.mp hlim
  intro h
  exact hw (h ▸ hLim)

/-- Concrete instance: a real-coefficient polynomial, evaluated over `ℂ`, is
conjugation-equivariant — so the gluing polynomial and its derivative at real
meridian qualify, and the exclusion applies to the literal pole-seed Newton. -/
theorem conjEquivariant_realPolynomial (p : Polynomial ℝ) :
    ConjEquivariant fun z => (p.map (algebraMap ℝ ℂ)).eval z := by
  intro z
  induction p using Polynomial.induction_on' with
  | add p q hp hq =>
      simp only [Polynomial.map_add, Polynomial.eval_add, map_add, hp, hq]
  | monomial n a =>
      simp [Polynomial.map_monomial, Polynomial.eval_monomial, map_mul,
        map_pow, Complex.conj_ofReal]

end QOU.QBeta.NewtonRealityInvariance
