/-
  The ratio of two Faddeev solutions is doubly periodic — the algebraic core of
  `hper`, and a reduction of `hibinv` to `hratio`.

  WHERE THIS SITS. `QOU.MathlibExt.DoublyPeriodicLiouville` reduces
  `PentagonRigidity.uniqueUpToScalar` to two open inputs and proves the
  Liouville-elliptic step:

      ratio_const_of_entire_ratio
        (hr   : Differentiable ℂ (fun z => Ψ z / Φ z))          -- `hratio`, bean qou-cons
        (hper : ∀ i z, Ψ (z + b i) / Φ (z + b i) = Ψ z / Φ z)   -- `hibinv`, bean qou-rp5f
        : ∃ c, ∀ z, Ψ z / Φ z = c

  Both beans are title-only stubs, so this file first pins down what `hper`
  actually is.

  WHAT IS PROVED HERE.

  1. `hper` IS ALGEBRA, off the prefactor zeros. If `Φ` and `Ψ` both satisfy
     `FaddeevPhi b`, both shift equations have the SAME prefactor, and the
     prefactor cancels out of the ratio. No analysis, no growth, no
     factorization — one `mul_div_mul_left`. That gives `ib`- and
     `i/b`-periodicity of the ratio at every `z` where the corresponding
     prefactor is nonzero.

  2. THE PREFACTOR ZERO SETS ARE NOWHERE DENSE. `1 + exp(2πbz)` is entire and
     equals `2` at `z = 0`, so by the identity theorem its zero set has empty
     interior, hence dense complement.

  3. THEREFORE `hibinv` IS NOT INDEPENDENT OF `hratio`. Given that the ratio is
     entire — hence continuous — periodicity on a dense set extends to
     periodicity everywhere. `periodic_b_of_continuous` and
     `periodic_binv_of_continuous` do exactly that.

  CONSEQUENCE FOR THE WORK PLAN. `uniqueUpToScalar` was carried as TWO open
  inputs. It is one: discharge `hratio` (bean qou-cons — the two solutions share
  their divisor) and `hibinv` follows, by the lemmas here, with no further
  analytic input. Bean qou-rp5f's own title names the intended mechanism
  ("identity theorem off dual pole lattice"); this supplies it.

  WHAT IS STILL OPEN: `hratio` itself. That two `FaddeevPhi` solutions share
  their divisor is a genuine fact about `Φ_b`, not algebra, and nothing here
  touches it.

  -- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
-/
import QOU.MathlibExt.FaddeevQuantumDilogarithm
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

namespace QOU.Mathlib.FaddeevRatioPeriodic

open Complex QOU.MathlibExt.FaddeevQuantumDilogarithm

variable {b : ℂ} {Φ Ψ : ℂ → ℂ}

/-! ### 1. The prefactor cancels: `hper` is algebra off the prefactor zeros -/

/-- The ratio of two `FaddeevPhi b` solutions is invariant under the compact
`ib`-shift wherever the shared prefactor is nonzero.

The whole content is that both shift equations carry the SAME prefactor, so it
cancels from the ratio. Note this needs nothing about the zeros of `Φ`: at a
point where `Φ` vanishes both sides are `0`, and `mul_div_mul_left` covers it. -/
theorem ratio_shift_b (hΦ : FaddeevPhi b Φ) (hΨ : FaddeevPhi b Ψ) (z : ℂ)
    (hA : 1 + Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0) :
    Ψ (z - I * (b / 2)) / Φ (z - I * (b / 2))
      = Ψ (z + I * (b / 2)) / Φ (z + I * (b / 2)) := by
  rw [hΦ.shift_b z, hΨ.shift_b z]
  exact mul_div_mul_left _ _ hA

/-- The modular-dual half. The guard is already in the `FaddeevPhi` axiom. -/
theorem ratio_shift_binv (hΦ : FaddeevPhi b Φ) (hΨ : FaddeevPhi b Ψ) (z : ℂ)
    (hA : 1 + Complex.exp (2 * (Real.pi : ℂ) * z / b) ≠ 0) :
    Ψ (z - I / (2 * b)) / Φ (z - I / (2 * b))
      = Ψ (z + I / (2 * b)) / Φ (z + I / (2 * b)) := by
  rw [hΦ.shift_binv z hA, hΨ.shift_binv z hA]
  exact mul_div_mul_left _ _ hA

/-- Period form of `ratio_shift_b`: the ratio is `ib`-periodic off the prefactor
zeros. (Re-centred at `w = z + ib/2`, so the two shifted arguments become `w` and
`w - ib`.) -/
theorem ratio_periodic_b (hΦ : FaddeevPhi b Φ) (hΨ : FaddeevPhi b Ψ) (w : ℂ)
    (hA : 1 + Complex.exp (2 * (Real.pi : ℂ) * b * (w - I * (b / 2))) ≠ 0) :
    Ψ (w - I * b) / Φ (w - I * b) = Ψ w / Φ w := by
  have h := ratio_shift_b hΦ hΨ (w - I * (b / 2)) hA
  have e1 : w - I * (b / 2) - I * (b / 2) = w - I * b := by ring
  have e2 : w - I * (b / 2) + I * (b / 2) = w := by ring
  rwa [e1, e2] at h

/-- Period form of `ratio_shift_binv`. -/
theorem ratio_periodic_binv (hΦ : FaddeevPhi b Φ) (hΨ : FaddeevPhi b Ψ) (w : ℂ)
    (hA : 1 + Complex.exp (2 * (Real.pi : ℂ) * (w - I / (2 * b)) / b) ≠ 0) :
    Ψ (w - I / b) / Φ (w - I / b) = Ψ w / Φ w := by
  have h := ratio_shift_binv hΦ hΨ (w - I / (2 * b)) hA
  have e1 : w - I / (2 * b) - I / (2 * b) = w - I / b := by ring
  have e2 : w - I / (2 * b) + I / (2 * b) = w := by ring
  rwa [e1, e2] at h

/-! ### 2. The prefactor zero sets are nowhere dense -/

/-- An entire `g` that is nonzero somewhere has a zero set with DENSE COMPLEMENT.

Identity theorem: if the zero set had interior, `g` would vanish on a
neighbourhood, hence identically on the (preconnected) plane. -/
theorem dense_compl_zeros {g : ℂ → ℂ} (hg : Differentiable ℂ g)
    {z₀ : ℂ} (hz₀ : g z₀ ≠ 0) : Dense {z | g z = 0}ᶜ := by
  rw [← interior_eq_empty_iff_dense_compl]
  by_contra hne
  obtain ⟨x, hx⟩ := Set.nonempty_iff_ne_empty.mpr hne
  have hana : AnalyticOnNhd ℂ g Set.univ := fun z _ => hg.analyticAt z
  have hev : g =ᶠ[nhds x] 0 := by
    filter_upwards [isOpen_interior.mem_nhds hx] with y hy
    simpa using interior_subset hy
  have := hana.eqOn_zero_of_preconnected_of_eventuallyEq_zero
    (isPreconnected_univ) (Set.mem_univ x) hev
  exact hz₀ (this (Set.mem_univ z₀))

/-- The compact prefactor `1 + e^{2πbz}` has a nowhere-dense zero set: it takes
the value `2` at `z = 0`. -/
theorem dense_compl_prefactor_b :
    Dense {z : ℂ | 1 + Complex.exp (2 * (Real.pi : ℂ) * b * z) = 0}ᶜ := by
  refine dense_compl_zeros (g := fun z => 1 + Complex.exp (2 * (Real.pi : ℂ) * b * z))
    ((differentiable_const 1).add (Complex.differentiable_exp.comp (by fun_prop)))
    (z₀ := 0) ?_
  simp

/-- The dual prefactor `1 + e^{2πz/b}` likewise. -/
theorem dense_compl_prefactor_binv :
    Dense {z : ℂ | 1 + Complex.exp (2 * (Real.pi : ℂ) * z / b) = 0}ᶜ := by
  refine dense_compl_zeros (g := fun z => 1 + Complex.exp (2 * (Real.pi : ℂ) * z / b))
    ((differentiable_const 1).add (Complex.differentiable_exp.comp (by fun_prop)))
    (z₀ := 0) ?_
  simp

/-! ### 3. `hibinv` follows from `hratio` -/

/-- **Given that the ratio is entire, `ib`-periodicity holds EVERYWHERE.**

The algebra gives it off the prefactor zeros; those are nowhere dense; a
continuous function is determined by its values on a dense set. So the open input
`hibinv` (bean qou-rp5f) is not independent of `hratio` (bean qou-cons) — it
follows from it. -/
theorem periodic_b_of_continuous (hΦ : FaddeevPhi b Φ) (hΨ : FaddeevPhi b Ψ)
    (hcont : Continuous (fun z => Ψ z / Φ z)) (w : ℂ) :
    Ψ (w - I * b) / Φ (w - I * b) = Ψ w / Φ w := by
  have hdense : Dense {x : ℂ |
      1 + Complex.exp (2 * (Real.pi : ℂ) * b * (x - I * (b / 2))) = 0}ᶜ := by
    refine dense_compl_zeros
      (g := fun x => 1 + Complex.exp (2 * (Real.pi : ℂ) * b * (x - I * (b / 2))))
      ((differentiable_const 1).add (Complex.differentiable_exp.comp (by fun_prop)))
      (z₀ := I * (b / 2)) ?_
    simp
  have hshift : Continuous (fun z => Ψ (z - I * b) / Φ (z - I * b)) :=
    hcont.comp (by fun_prop)
  have heq : Set.EqOn (fun z => Ψ (z - I * b) / Φ (z - I * b)) (fun z => Ψ z / Φ z)
      {x : ℂ | 1 + Complex.exp (2 * (Real.pi : ℂ) * b * (x - I * (b / 2))) = 0}ᶜ :=
    fun x hx => ratio_periodic_b hΦ hΨ x hx
  exact congrFun (Continuous.ext_on hdense hshift hcont heq) w

/-- The modular-dual half, same argument. -/
theorem periodic_binv_of_continuous (hΦ : FaddeevPhi b Φ) (hΨ : FaddeevPhi b Ψ)
    (hcont : Continuous (fun z => Ψ z / Φ z)) (w : ℂ) :
    Ψ (w - I / b) / Φ (w - I / b) = Ψ w / Φ w := by
  have hdense : Dense {x : ℂ |
      1 + Complex.exp (2 * (Real.pi : ℂ) * (x - I / (2 * b)) / b) = 0}ᶜ := by
    refine dense_compl_zeros
      (g := fun x => 1 + Complex.exp (2 * (Real.pi : ℂ) * (x - I / (2 * b)) / b))
      ((differentiable_const 1).add (Complex.differentiable_exp.comp (by fun_prop)))
      (z₀ := I / (2 * b)) ?_
    simp
  have hshift : Continuous (fun z => Ψ (z - I / b) / Φ (z - I / b)) :=
    hcont.comp (by fun_prop)
  have heq : Set.EqOn (fun z => Ψ (z - I / b) / Φ (z - I / b)) (fun z => Ψ z / Φ z)
      {x : ℂ | 1 + Complex.exp (2 * (Real.pi : ℂ) * (x - I / (2 * b)) / b) = 0}ᶜ :=
    fun x hx => ratio_periodic_binv hΦ hΨ x hx
  exact congrFun (Continuous.ext_on hdense hshift hcont heq) w

end QOU.Mathlib.FaddeevRatioPeriodic
