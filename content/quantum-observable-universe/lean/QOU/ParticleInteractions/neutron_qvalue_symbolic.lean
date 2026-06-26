import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-!
# QOU.ParticleInteractions.neutron_qvalue_symbolic

**Proposition (conditional on `conj:borromean-quark`)** for content block
[`prop:neutron-qvalue-symbolic`](../../../quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md):
*Symbolic $Q$-value of free neutron $\beta^-$-decay.*

The single-wrap normal-form (NF) net coefficients of the proton `[u,u,d]`
and neutron `[u,d,d]` in `H_3(q)` are the **conjectural categorical inputs**
(`conj:borromean-quark`), carried here as class hypotheses:

  net(p) = 1 − h/2,          net(n) = 1 − 3h/2 + h²/2,      h = q − q⁻¹.

The closed-form `Q`-value additionally assumes the energy-scale *ansatz*
`Q_β = |Δ(net)| · E₀` with `E₀ = m_e / (q(q−1))`, stated "by construction"
in the manuscript (`pre-archimedean-derivation-chain.md`), not derived from
the canonical per-braid mass formula.  This too is carried as a hypothesis.

Given these inputs, the symbolic difference `Δ(net) = (h² − 2h)/2` and the
closed form `Q_β = m_e·(2−h)·h / (2q(q−1))` are **derived by algebra** —
this is a rigorous §3b-cond conditional, not a self-projection.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md
-/

namespace QOU.ParticleInteractions

/-- §3b-cond conjecture class for `conj:borromean-quark` (non-degenerate per
    AGENTS.md §3b-cond item 5): carries the conjectural categorical *inputs*
    — the single-wrap NF net coefficients and the energy-scale ansatz — as
    hypotheses, NOT the conclusion (`Δ(net)` and the `Q`-value are derived
    from them below). -/
class BorromeanQuark where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Hecke differential `h = q − q⁻¹`. -/
  h : ℝ
  h_eq : h = q - q⁻¹
  /-- Electron mass `m_e : ℝ`. -/
  m_e : ℝ
  /-- Proton single-wrap NF net coefficient. -/
  net_p : ℝ
  /-- Neutron single-wrap NF net coefficient. -/
  net_n : ℝ
  /-- The Q-value `Q_β : ℝ`. -/
  Q_β : ℝ
  /-- Substrate-regime bound on the Hecke differential: `0 < h`. Holds at
      the substrate `q₀ ≈ 1.11` (`h ≈ 0.21`); carried as an explicit input
      so the `|Δ(net)|` resolution is rigorous, not assumed silently. -/
  h_pos : 0 < h
  /-- Substrate-regime bound: `h < 2`. Holds at `q₀ ≈ 1.11`; needed to
      resolve the absolute value `|h² − 2h| = 2h − h²`. -/
  h_lt_two : h < 2
  /-- Conjectural input (i): proton NF net `= 1 − h/2`. -/
  proton_net : net_p = 1 - h / 2
  /-- Conjectural input (ii): neutron NF net `= 1 − 3h/2 + h²/2`. -/
  neutron_net : net_n = 1 - 3 * h / 2 + h ^ 2 / 2
  /-- Ansatz input (iii): the `Q`-value is the **absolute** NF difference
      `|Δ(net)|` scaled by the energy scale `E₀ = m_e / (q(q−1))`. This
      `Q_β = |Δ(net)| · E₀` relation is stated "by construction" in the
      manuscript, not derived from the per-braid mass formula. -/
  qvalue_ansatz : Q_β = |net_n - net_p| * (m_e / (q * (q - 1)))

/-- Auxiliary positivity: under `1 < q`, the denominator `q(q−1) ≠ 0`. -/
theorem borromeanQuark_denom_ne_zero [inst : BorromeanQuark] :
    inst.q * (inst.q - 1) ≠ 0 := by
  have hq : 1 < inst.q := inst.q_gt_one
  have h1 : (0 : ℝ) < inst.q := by linarith
  have h2 : (0 : ℝ) < inst.q - 1 := by linarith
  have : (0 : ℝ) < inst.q * (inst.q - 1) := mul_pos h1 h2
  linarith

/-- **Symbolic `Δ(net)` (derived).**  The NF difference
    `net(n) − net(p) = (h² − 2h)/2` follows from the conjectural single-wrap
    NF nets by ring algebra — not a projection of a class field. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md
theorem neutron_delta_net [inst : BorromeanQuark] :
    inst.net_n - inst.net_p = (inst.h ^ 2 - 2 * inst.h) / 2 := by
  rw [inst.proton_net, inst.neutron_net]; ring

/-- **Symbolic `Q`-value closed form (conditional on `conj:borromean-quark`).**

    Given the conjectural NF nets and the energy-scale ansatz, the neutron
    `β⁻`-decay `Q`-value has the closed form

      Q_β = m_e · (2 − h) · h / (2 q (q − 1)),     h = q − q⁻¹.

    The proof *derives* this from `qvalue_ansatz` by substituting the NF nets
    (via `neutron_delta_net`) and clearing the denominator — it is NOT a
    read-back of a stored conclusion. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md
theorem neutron_qvalue_symbolic [inst : BorromeanQuark] :
    inst.Q_β = inst.m_e * (2 - inst.h) * inst.h / (2 * inst.q * (inst.q - 1)) := by
  have hden : inst.q * (inst.q - 1) ≠ 0 := borromeanQuark_denom_ne_zero
  -- Resolve |Δ(net)| = (2h − h²)/2 using 0 < h < 2 (substrate regime).
  have hdelta : inst.net_n - inst.net_p = (inst.h ^ 2 - 2 * inst.h) / 2 :=
    neutron_delta_net
  have hneg : (inst.h ^ 2 - 2 * inst.h) / 2 ≤ 0 := by
    have hh0 : 0 < inst.h := inst.h_pos
    have hh2 : inst.h < 2 := inst.h_lt_two
    nlinarith [mul_pos hh0 (by linarith : (0:ℝ) < 2 - inst.h)]
  have habs : |inst.net_n - inst.net_p| = (2 * inst.h - inst.h ^ 2) / 2 := by
    rw [hdelta, abs_of_nonpos hneg]; ring
  rw [inst.qvalue_ansatz, habs]
  field_simp

end QOU.ParticleInteractions
