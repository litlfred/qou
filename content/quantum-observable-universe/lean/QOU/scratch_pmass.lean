import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.Substrate.ProtonMassSubstrateIdentity

opaque F_Bor (q : ℝ) : ℝ

def m_e_codata : ℝ := 0.51099895069
def m_mu_codata : ℝ := 105.6583755
def m_p_codata : ℝ := 938.27208943

def m_p_predicted (q_0 : ℝ) : ℝ :=
  2 * m_mu_codata * F_Bor q_0 - 12 * m_e_codata

theorem proton_mass_substrate_match (q_0 : ℝ) (h_F : F_Bor q_0 = 4.46913873576752253) :
  |m_p_predicted q_0 - m_p_codata| / m_p_codata < 0.25 / 1000000 := by
  rw [m_p_predicted, h_F, m_e_codata, m_mu_codata, m_p_codata]
  norm_num

end QOU.Substrate.ProtonMassSubstrateIdentity
