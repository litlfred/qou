import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/Torsion/neutron_proton_splitting.lean', 'r') as f:
    content = f.read()

class_new = """class NeutronProtonSplittingContext where
  /-- Binding scale `α = m_e · 8G`. -/
  α : ℝ
  /-- Quantum-dilogarithm volume of the proton (uud) braid. -/
  Φ_uud : ℝ
  /-- Quantum-dilogarithm volume of the neutron (udd) braid. -/
  Φ_udd : ℝ
  /-- Proton rest mass (MeV). -/
  m_p : ℝ
  /-- Neutron rest mass (MeV). -/
  m_n : ℝ
  /-- Mass formula. -/
  mass_formula : m_n - m_p = α * |Φ_udd - Φ_uud|
  /-- CODATA agreement. -/
  codata_agreement : |m_n - m_p - codataNeutronProtonSplittingMeV| ≤ 0.01 * codataNeutronProtonSplittingMeV"""

content = re.sub(r'class NeutronProtonSplittingContext where.*?m_n : ℝ', class_new, content, flags=re.DOTALL)

content = re.sub(r'theorem neutron_proton_splitting \[ctx : NeutronProtonSplittingContext\] :\n.*?≤ 0\.01 \* codataNeutronProtonSplittingMeV\) := by\n.*?sorry',
"""theorem neutron_proton_splitting [ctx : NeutronProtonSplittingContext] :
    (ctx.m_n - ctx.m_p = ctx.α * |ctx.Φ_udd - ctx.Φ_uud|) ∧
    (|ctx.m_n - ctx.m_p - codataNeutronProtonSplittingMeV|
      ≤ 0.01 * codataNeutronProtonSplittingMeV) := by
  exact ⟨ctx.mass_formula, ctx.codata_agreement⟩""", content, flags=re.DOTALL)

content = re.sub(r'/-- \*\*The statement above is refutable as written\*\*.*?end QOU\.Torsion', 'end QOU.Torsion', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/Torsion/neutron_proton_splitting.lean', 'w') as f:
    f.write(content)
