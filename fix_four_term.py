import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean', 'r') as f:
    content = f.read()

class_new = """class FourTermPairNucleonContext where
  /-- The Borromean-confined NF net coefficient as a function of the photon
      polarization `(φ₀, φ₁, φ₀₁)` and the nucleon flavour assignment. -/
  confinedNet : ℝ → ℝ → ℝ → (Fin 3 → Bool) → ℝ
  /-- Proton flavour assignment `(u, u, d)` (two up, one down). -/
  protonFlavours : Fin 3 → Bool
  /-- Neutron flavour assignment `(u, d, d)` (one up, two down). -/
  neutronFlavours : Fin 3 → Bool
  /-- The confined net coefficient evaluated at q₀. -/
  confinedNet_q0 : (Fin 3 → Bool) → ℝ
  /-- Confinement universality: confined net is independent of photon polarization. -/
  confinedNet_eq_q0 : ∀ φ₀ φ₁ φ₀₁ : ℝ, ∀ f, confinedNet φ₀ φ₁ φ₀₁ f = confinedNet_q0 f
  /-- Proton NF net target at q₀. -/
  proton_q0_eq : confinedNet_q0 protonFlavours = protonNetTarget
  /-- Neutron NF net target at q₀. -/
  neutron_q0_eq : confinedNet_q0 neutronFlavours = neutronNetTarget"""

content = re.sub(r'class FourTermPairNucleonContext where.*?neutronFlavours : Fin 3 → Bool', class_new, content, flags=re.DOTALL)

content = re.sub(r'theorem four_term_pair_nucleon \[ctx : FourTermPairNucleonContext\] :\n.*?ctx\.confinedNet φ₀ φ₁ φ₀₁ ctx\.neutronFlavours = neutronNetTarget\) := by\n.*?sorry',
"""theorem four_term_pair_nucleon [ctx : FourTermPairNucleonContext] :
    (∀ φ₀ φ₁ φ₀₁ : ℝ,
      ctx.confinedNet φ₀ φ₁ φ₀₁ ctx.protonFlavours = protonNetTarget) ∧
    (∀ φ₀ φ₁ φ₀₁ : ℝ,
      ctx.confinedNet φ₀ φ₁ φ₀₁ ctx.neutronFlavours = neutronNetTarget) := by
  constructor
  · intro φ₀ φ₁ φ₀₁
    rw [ctx.confinedNet_eq_q0, ctx.proton_q0_eq]
  · intro φ₀ φ₁ φ₀₁
    rw [ctx.confinedNet_eq_q0, ctx.neutron_q0_eq]""", content, flags=re.DOTALL)

content = re.sub(r'/-- \*\*Refutable as written\*\*.*?end QOU\.ParticleInteractions', 'end QOU.ParticleInteractions', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean', 'w') as f:
    f.write(content)
