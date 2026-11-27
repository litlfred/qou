import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

/-!
# A continuous function periodic on a dense set is periodic everywhere

The identity-theorem-free core of the `hibinv` input of
`QOU.QBeta.FaddeevRigidityReduction` (bean `qou-q95i`). The dual-shift
periodicity of the `Φ_b` ratio (`CyclicDilogPentagon.ratio_ibinv_periodic`) is
proved only **off** the discrete dual pole lattice (the `shift_binv` guard). To
promote it to the everywhere-periodicity the reduction consumes, one does **not**
need the full complex-analytic identity theorem: the dual pole lattice is
discrete, so its complement is **dense**, and a *continuous* function agreeing
with its shift on a dense set agrees everywhere. This isolates the remaining two
inputs cleanly: the ratio is continuous (from the entireness endowment,
`qou-2cvs`) and the dual-lattice complement is dense (a discreteness fact).

Verified `lean`-direct against pinned Mathlib (exit 0).
-/

open Complex

namespace QOU.Common

/-- A continuous `r : ℂ → ℂ` that is `c`-periodic on a **dense** set is
`c`-periodic everywhere: `r(·+c)` and `r` are continuous and agree on a dense
set, so they agree. -/
theorem periodic_of_continuous_of_eqOn_dense
    {r : ℂ → ℂ} {c : ℂ} {S : Set ℂ}
    (hcont : Continuous r) (hS : Dense S)
    (hper : ∀ z ∈ S, r (z + c) = r z) :
    ∀ z, r (z + c) = r z := by
  have hg : Continuous (fun z => r (z + c)) :=
    hcont.comp (continuous_id.add continuous_const)
  have hfun : (fun z => r (z + c)) = r :=
    Continuous.ext_on hS hg hcont (fun z hz => hper z hz)
  intro z
  exact congrFun hfun z

/-- **A countable subset of `ℂ` has dense complement.** `sᶜ = ⋂_{x ∈ s} {x}ᶜ`, a
countable intersection of dense open sets, so it is dense by Baire (`ℂ` is a
complete metric — hence Baire — perfect space). -/
theorem dense_compl_of_countable {s : Set ℂ} (hs : s.Countable) : Dense sᶜ := by
  have hset : sᶜ = ⋂ x ∈ s, ({x}ᶜ : Set ℂ) := by
    ext y
    simp only [Set.mem_compl_iff, Set.mem_iInter, Set.mem_singleton_iff]
    constructor
    · intro hy x hx; rintro rfl; exact hy hx
    · intro h hy; exact h y hy rfl
  rw [hset]
  exact dense_biInter_of_isOpen (fun x _ => isOpen_compl_singleton) hs
    (fun x _ => dense_compl_singleton x)

/-- **The dual pole lattice complement is dense** (the `hibinv` discreteness
input, bean `qou-q95i`). The zero set of the dual quasi-period prefactor
`1 + exp(2π(z + i/2b)/b)` is exactly where `exp(2π(z + i/2b)/b) = -1`; by
`Complex.exp_eq_exp_iff_exists_int` this pins `z` to the discrete lattice
`{ (πi + n·2πi)·b/(2π) − i/2b : n ∈ ℤ }`, so the zero set is **countable** and its
complement — the set on which `CyclicDilogPentagon.ratio_ibinv_periodic`'s guard
`hpre` holds — is **dense** in `ℂ`. Combined with `periodic_of_continuous_of_eqOn_dense`
(and the `qou-2cvs` continuity endowment) this discharges the `hibinv` input of
`FaddeevRigidityReduction` from the everywhere-periodicity side. -/
theorem dense_dualPole_compl {b : ℂ} (hb : b ≠ 0) :
    Dense {z : ℂ |
      (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0} := by
  have hπ : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  have h2pi : (2 : ℂ) * (Real.pi : ℂ) ≠ 0 := by simp [hπ]
  -- The zero set injects into the discrete lattice `f '' ℤ`, hence is countable.
  have hsub :
      {z : ℂ | (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) = 0}
        ⊆ Set.range (fun n : ℤ =>
            ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)) * b
              / (2 * (Real.pi : ℂ)) - I / (2 * b)) := by
    intro z hz
    simp only [Set.mem_setOf_eq] at hz
    have hexp : Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) = -1 := by
      linear_combination hz
    rw [← Complex.exp_pi_mul_I, Complex.exp_eq_exp_iff_exists_int] at hexp
    obtain ⟨n, hn⟩ := hexp
    refine ⟨n, ?_⟩
    show ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)) * b
        / (2 * (Real.pi : ℂ)) - I / (2 * b) = z
    rw [div_eq_iff hb] at hn
    have hz2 : z + I / (2 * b)
        = ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)) * b
            / (2 * (Real.pi : ℂ)) := by
      rw [eq_div_iff h2pi]; linear_combination hn
    rw [← hz2]; ring
  have hcount := (Set.countable_range _).mono hsub
  have hgoal :
      {z : ℂ | (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0}
        = {z : ℂ | (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) = 0}ᶜ := by
    ext z; simp only [Set.mem_setOf_eq, Set.mem_compl_iff, ne_eq]
  rw [hgoal]
  exact dense_compl_of_countable hcount

/-- **The primary pole lattice complement is dense** (the `ib`-period companion of
`dense_dualPole_compl`, for the `hib` discreteness input). The zero set of the
primary quasi-period prefactor `1 + exp(iπb²)·exp(2πbz)` is where
`exp(iπb² + 2πbz) = -1`; by `Complex.exp_eq_exp_iff_exists_int` this pins `z` to a
discrete `ℤ`-lattice, so the zero set is countable and its complement — the guard
domain of `CyclicDilogPentagon.ratio_ib_periodic` — is dense in `ℂ`. -/
theorem dense_primaryPole_compl {b : ℂ} (hb : b ≠ 0) :
    Dense {z : ℂ | (1 : ℂ)
      + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0} := by
  have hπ : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  have h2pib : (2 : ℂ) * (Real.pi : ℂ) * b ≠ 0 :=
    mul_ne_zero (mul_ne_zero two_ne_zero hπ) hb
  have hsub :
      {z : ℂ | (1 : ℂ)
          + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) = 0}
        ⊆ Set.range (fun n : ℤ =>
            ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I) - I * (Real.pi : ℂ) * b ^ 2)
              / (2 * (Real.pi : ℂ) * b)) := by
    intro z hz
    simp only [Set.mem_setOf_eq] at hz
    have hexp : Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z)
        = -1 := by linear_combination hz
    rw [← Complex.exp_add, ← Complex.exp_pi_mul_I, Complex.exp_eq_exp_iff_exists_int] at hexp
    obtain ⟨n, hn⟩ := hexp
    refine ⟨n, ?_⟩
    show ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I) - I * (Real.pi : ℂ) * b ^ 2)
        / (2 * (Real.pi : ℂ) * b) = z
    rw [div_eq_iff h2pib]
    linear_combination -hn
  have hcount := (Set.countable_range _).mono hsub
  have hgoal :
      {z : ℂ | (1 : ℂ)
          + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0}
        = {z : ℂ | (1 : ℂ)
          + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) = 0}ᶜ := by
    ext z; simp only [Set.mem_setOf_eq, Set.mem_compl_iff, ne_eq]
  rw [hgoal]
  exact dense_compl_of_countable hcount

end QOU.Common
