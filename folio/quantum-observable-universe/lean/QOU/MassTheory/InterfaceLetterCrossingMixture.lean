/-
# Every production interface letter is a convex mixture of a crossing and its inverse

The production words (`pyhecke.atom.nucleon_gen_chains`, `atom_per_generator_volumes`;
`computations/_exact_trace_engine.py::nucleon_word` / `bond_d`) are built from letters
`c·σ_i + d·1` with `c = 1` and `d ∈ {0, −h·b, −h·(1 − δ/2)/2, −h}`, `b ∈ {0, ½, 1}`,
`h = q − q⁻¹`. Under the Hecke relation `σ² = h σ + 1` (the corpus's
`(σ − q)(σ + q⁻¹) = 0`) the inverse crossing is `σ⁻¹ = σ − h·1`, so every such letter is

    σ − e h·1 = (1 − e)·σ + e·σ⁻¹,     e = −d/h ∈ [0, 1],

a **Bernoulli mixture** of the positive crossing (weight `1 − e`) and the inverse crossing
(weight `e`). Under any linear trace with `t(1) = 1`, `t(σ) = z` its trace is
`(1 − e) z + e (z − h) = z − e h` — the corpus's bond factor `z_D + d`.

This is the algebra behind the owner's 2026-09-16 reading that entanglement is
"weighted fully in the negative coefficients": the only negative coefficient a production
letter carries is `d = −e h`, the weight of the inverse crossing. Corpus values at `q₀`
(`pyhecke.constants.pn_interface_offset`, convention `bring_color_weighted`,
`δ = (q − 1)²(1 − q⁻⁴)/3`): interfaces `e_pp = 0`, `e_pn = (1 − δ/2)/2`, `e_nn = 1`;
intra-nucleon quark pairs `e_uu = 0`, `e_ud = ½`, `e_dd = 1`. Measured in
`relative_reeb_datum_trace_angle_probe.py`.

What this does NOT say: nothing here selects `e`, and reading `e` as an entanglement
grade makes the like-nucleon pairs the extremes (`pp` unentangled, `nn` fully entangled)
while the two-body spectrum needs the *unlike* pair singled out (bean `qou-q8vl`). Beans
`qou-1x56`, `qou-8r6b`.

-- Ref: [leitner2026] def:hecke-skein-convention; prop:hecke-markov-transition
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring

namespace QOU.MassTheory.InterfaceLetter

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The interface letter `σ + d·1`, written through its inverse-crossing weight
`e = −d/h`: `σ − (e h)·1`. -/
def interfaceLetter (σ : A) (h e : R) : A := σ - (e * h) • (1 : A)

/-- **Under the Hecke relation `σ² = h σ + 1`, `σ − h·1` is a two-sided inverse of `σ`.**
This is the identification `σ⁻¹ = σ − h·1` the corpus writes as `T_i⁻¹ = T_i − A`. -/
theorem mul_sub_smul_one_eq_one (σ : A) (h : R) (hσ : σ * σ = h • σ + 1) :
    σ * (σ - h • (1 : A)) = 1 ∧ (σ - h • (1 : A)) * σ = 1 := by
  constructor
  · rw [mul_sub, hσ, Algebra.mul_smul_comm, mul_one]
    abel
  · rw [sub_mul, hσ, Algebra.smul_mul_assoc, one_mul]
    abel

/-- **The interface letter is the `e`-mixture of the crossing and its inverse.** -/
theorem interfaceLetter_eq_mix (σ : A) (h e : R) :
    interfaceLetter σ h e = (1 - e) • σ + e • (σ - h • (1 : A)) := by
  unfold interfaceLetter
  rw [smul_sub, sub_smul, one_smul, smul_smul]
  abel

/-- Under a linear trace `t` with `t 1 = 1` and `t σ = z`, the letter's trace is the
mixture of the two crossing traces, `(1 − e) z + e (z − h) = z − e h` — the corpus's bond
factor `z_D + d`. -/
theorem trace_interfaceLetter (t : A →ₗ[R] R) (σ : A) (h e z : R)
    (h1 : t 1 = 1) (hz : t σ = z) :
    t (interfaceLetter σ h e) = (1 - e) * z + e * (z - h) := by
  unfold interfaceLetter
  rw [map_sub, map_smul, h1, hz, smul_eq_mul, mul_one]
  ring

end QOU.MassTheory.InterfaceLetter
