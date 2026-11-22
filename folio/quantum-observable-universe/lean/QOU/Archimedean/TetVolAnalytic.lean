/-
  The Λ-sum volume chart is real-analytic on the open angle simplex — the
  RHS half of the obtuse ideal-tetrahedron continuation (bean `qou-w3eg`).

  WHAT THIS IS.  The obtuse case of Milnor's identity
  `Vol(α,β,γ) = Λ(α) + Λ(β) + Λ(γ)` is being closed by analytic continuation
  off the acute region.  An identity theorem needs BOTH sides analytic on a
  preconnected open set.  This file supplies the **right-hand side** — the
  Λ-sum `tetVol (α,β) = Λ(α) + Λ(β) + Λ(π−α−β)` — together with the
  topological hypotheses the identity theorem consumes:

    * `isOpen_tetSimplex`         — the angle simplex is open
    * `isPreconnected_tetSimplex` — and preconnected (via its proved convexity)
    * `analyticOnNhd_tetVol`      — the Λ-sum is analytic on it

  It composes `QOU.Archimedean.analyticOnNhd_Lob` (`LobAnalytic.lean`) with the
  analytic coordinate maps.  Each of the three arguments stays inside `(0, π)`
  on the simplex: `α` and `β` by `α, β > 0` and `α + β < π`, and the third
  angle `π − α − β` by the same two facts read the other way round.

  WHAT THIS DOES NOT DO — read this before citing the file.  It says nothing
  about the hyperbolic volume.  `tetVol` is *defined* as the Λ-sum (see
  `IdealTetrahedronVolumeConcavity.volChart`'s docstring: "A definition, not the
  geometric volume"), so analyticity of `tetVol` is analyticity of the identity's
  RHS only.  The LHS — the geometric volume as a function of the angles — is
  **not** treated here and is the open half.  In particular:

  * The corpus's base integral is an `ℝ≥0∞`-valued `lintegral` whose angle
    dependence sits **wholly in the domain of integration**
    (`hypVolume_chimney_of_ae_lt`, `HyperbolicVolumeFubini.lean`; the integrand
    is parameter-free).  Mathlib's parametric-integral family
    (`Analysis/Calculus/ParametricIntegral.lean`) requires the parameter in the
    *integrand*, so "differentiate under the integral sign" does not apply to it
    as it stands, and there is as yet no real-valued carrier to state LHS
    analyticity about.
  * The obtuse case was closed WITHOUT this file, by direct geometry
    (`ObtuseTiling.idealTetVolume_of_vertices_obtuse`).  This bullet used to say
    that even a complete LHS-analyticity result would not finish it, because
    `IdealTetEqChimney.idealTet_eq_chimney` carries `α, β, γ < π/2` and is a set
    equality.  Those hypotheses turned out to be unused and were dropped, so the
    claim is retracted — but the conclusion for THIS file is unchanged and if
    anything sharper: the continuation route did not close the obtuse case, and
    the results here address the identity's RHS only.

  Both points are recorded in bean `qou-w3eg`.

  Archimedean (ℝ): `Real.pi`, ordering — §7c.

  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
  -- Ref: [leitner2026] beans qou-w3eg (H4-5 obtuse), qou-idvt
-/
import QOU.Archimedean.LobAnalytic
import QOU.Archimedean.IdealTetrahedronVolumeConcave

namespace QOU.Archimedean

open Real Set

/-- **The open angle simplex is open.**  It is the intersection of three
preimages of open half-lines under continuous coordinate maps. -/
theorem isOpen_tetSimplex : IsOpen tetSimplex := by
  have h : tetSimplex
      = {p : ℝ × ℝ | 0 < p.1} ∩ {p : ℝ × ℝ | 0 < p.2}
        ∩ {p : ℝ × ℝ | p.1 + p.2 < Real.pi} := by
    ext p; simp [tetSimplex, and_assoc]
  rw [h]
  exact ((isOpen_lt continuous_const continuous_fst).inter
      (isOpen_lt continuous_const continuous_snd)).inter
    (isOpen_lt (continuous_fst.add continuous_snd) continuous_const)

/-- **The open angle simplex is preconnected** — the hypothesis the identity
theorem (`AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`) consumes.
Immediate from its proved convexity. -/
theorem isPreconnected_tetSimplex : IsPreconnected tetSimplex :=
  convex_tetSimplex.isPreconnected

/-- On the simplex the first angle lies in `(0, π)`. -/
theorem tetSimplex_fst_mem_Ioo {p : ℝ × ℝ} (hp : p ∈ tetSimplex) :
    p.1 ∈ Ioo 0 π :=
  ⟨hp.1, by linarith [hp.2.1, hp.2.2]⟩

/-- On the simplex the second angle lies in `(0, π)`. -/
theorem tetSimplex_snd_mem_Ioo {p : ℝ × ℝ} (hp : p ∈ tetSimplex) :
    p.2 ∈ Ioo 0 π :=
  ⟨hp.2.1, by linarith [hp.1, hp.2.2]⟩

/-- On the simplex the third angle `π − α − β` lies in `(0, π)`. -/
theorem tetSimplex_third_mem_Ioo {p : ℝ × ℝ} (hp : p ∈ tetSimplex) :
    Real.pi - p.1 - p.2 ∈ Ioo 0 π :=
  ⟨by linarith [hp.2.2], by linarith [hp.1, hp.2.1]⟩

/-- **The Λ-sum volume chart is real-analytic at every interior angle pair.**
Each summand is `Λ` composed with an analytic coordinate map, and each of the
three angles stays inside `(0, π)` where `Λ` is analytic. -/
theorem analyticAt_tetVol {p : ℝ × ℝ} (hp : p ∈ tetSimplex) :
    AnalyticAt ℝ tetVol p := by
  have h1 : AnalyticAt ℝ (fun r : ℝ × ℝ => Lob r.1) p := by
    have hf : AnalyticAt ℝ (fun r : ℝ × ℝ => r.1) p := analyticAt_fst
    have := AnalyticAt.comp (g := Lob) (f := fun r : ℝ × ℝ => r.1) (x := p)
      (analyticAt_Lob (tetSimplex_fst_mem_Ioo hp).1 (tetSimplex_fst_mem_Ioo hp).2) hf
    simpa [Function.comp] using this
  have h2 : AnalyticAt ℝ (fun r : ℝ × ℝ => Lob r.2) p := by
    have hf : AnalyticAt ℝ (fun r : ℝ × ℝ => r.2) p := analyticAt_snd
    have := AnalyticAt.comp (g := Lob) (f := fun r : ℝ × ℝ => r.2) (x := p)
      (analyticAt_Lob (tetSimplex_snd_mem_Ioo hp).1 (tetSimplex_snd_mem_Ioo hp).2) hf
    simpa [Function.comp] using this
  have h3 : AnalyticAt ℝ (fun r : ℝ × ℝ => Lob (Real.pi - r.1 - r.2)) p := by
    have hf : AnalyticAt ℝ (fun r : ℝ × ℝ => Real.pi - r.1 - r.2) p :=
      (analyticAt_const.sub analyticAt_fst).sub analyticAt_snd
    have := AnalyticAt.comp (g := Lob)
      (f := fun r : ℝ × ℝ => Real.pi - r.1 - r.2) (x := p)
      (analyticAt_Lob (tetSimplex_third_mem_Ioo hp).1 (tetSimplex_third_mem_Ioo hp).2) hf
    simpa [Function.comp] using this
  simpa [tetVol] using (h1.add h2).add h3

/-- **The Λ-sum volume chart is real-analytic on the whole open angle
simplex** — the `AnalyticOnNhd` form the identity theorem consumes. -/
theorem analyticOnNhd_tetVol : AnalyticOnNhd ℝ tetVol tetSimplex :=
  fun _ hp => analyticAt_tetVol hp

end QOU.Archimedean
