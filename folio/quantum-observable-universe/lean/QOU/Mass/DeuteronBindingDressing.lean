import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import QOU.ParticleInteractions.neutron_qvalue_symbolic

/-!
# QOU.Mass.DeuteronBindingDressing

**Proposition (conditional on `conj:borromean-quark`)** for content block
[`prop:deuteron-binding-dressing-proton-net`](../../../quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md):
*The deuteron binding dressing `(1 − h/2)` is the proton single-wrap
normal-form net coefficient `net(p)`.*

Empirically (probe `probe_d_qbeta_h_invariant` / `probe_d_dressing_is_proton_net`)
the trace-canonical deuteron binding is reproduced to `+0.12 %` of AME2020
by `B_D = E₀ · (1 − h/2) · Δtr` with `E₀ = m_e / (q(q−1))` and `Δtr` the
free−bound Markov-trace difference.  This file shows the dressing factor
`(1 − h/2)` is **not a new object**: it is exactly `net(p) = 1 − h/2`, the
proton `[u,u,d]` single-wrap NF net coefficient carried by
`conj:borromean-quark` (the same conjecture the neutron `Q`-value already
assumes — see `QOU.ParticleInteractions.neutron_qvalue_symbolic`).

The load-bearing algebra (all exact in a field, derived from the same class
inputs — no new hypothesis, no fit):

  * `Δ(net) = net(n) − net(p) = −h · net(p)`         (division-free)
  * `|Δ(net)| = h · net(p)`                          (`0 < h < 2` regime)
  * `Q_β = E₀ · h · net(p)`                          (from the `Q`-value ansatz)
  * `E₀ · net(p) · Δtr = Q_β · Δtr / h`              (`h ≠ 0`)

so the **bar-even binding dressing `net(p)`** and the **bar-odd `Q`-value**
are the same categorical object separated by the single Hecke factor `h`
(`h = q − q⁻¹`, bar-odd).  This *identifies* the dressing structurally; the
magnitude match to AME remains observation-tier and conditional on
`conj:borromean-quark` (NOT wired — the Δ_λ gate stands).

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md
-/

namespace QOU.Mass

open QOU.ParticleInteractions

/-- **`Δ(net) = −h · net(p)` (division-free).**  The neutron−proton NF net
    difference is exactly `−h` times the proton NF net coefficient — the
    identity that ties the deuteron binding dressing to the `Q`-value. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md
theorem delta_net_eq_neg_h_net_p [inst : BorromeanQuark] :
    inst.net_n - inst.net_p = - inst.h * inst.net_p := by
  rw [inst.proton_net, inst.neutron_net]; ring

/-- **`Q_β = E₀ · h · net(p)`.**  Substituting `|Δ(net)| = h · net(p)`
    (from `delta_net_eq_neg_h_net_p` and `0 < h < 2`) into the `Q`-value
    ansatz gives the `Q`-value as `E₀` times `h · net(p)`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md
theorem qbeta_eq_E0_h_net_p [inst : BorromeanQuark] :
    inst.Q_β = inst.h * inst.net_p * (inst.m_e / (inst.q * (inst.q - 1))) := by
  -- net(p) = 1 − h/2 > 0 (since h < 2), and h > 0, so h·net(p) ≥ 0.
  have hp : 0 < inst.net_p := by
    rw [inst.proton_net]; have := inst.h_lt_two; linarith
  have hh : 0 < inst.h := inst.h_pos
  have hprod : 0 ≤ inst.h * inst.net_p := le_of_lt (mul_pos hh hp)
  have hdelta : inst.net_n - inst.net_p = - inst.h * inst.net_p :=
    delta_net_eq_neg_h_net_p
  have habs : |inst.net_n - inst.net_p| = inst.h * inst.net_p := by
    rw [hdelta, abs_of_nonpos (by rw [neg_mul]; linarith)]; ring
  rw [inst.qvalue_ansatz, habs]

/-- **The deuteron binding dressing is the proton NF net coefficient.**
    The candidate binding functional `E₀ · net(p) · Δtr` equals the
    `Q_β`-scaled trace difference `Q_β · Δtr / h` for any `Δtr`, i.e. the
    `(1 − h/2)` dressing on the `E₀` route is exactly `net(p)`, the
    bar-even partner of `Q_β` under the single Hecke factor `h`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md
theorem binding_dressing_eq_qbeta_over_h [inst : BorromeanQuark]
    (Dtr : ℝ) :
    (inst.m_e / (inst.q * (inst.q - 1))) * inst.net_p * Dtr
      = inst.Q_β * Dtr / inst.h := by
  have hh : inst.h ≠ 0 := ne_of_gt inst.h_pos
  have hden : inst.q * (inst.q - 1) ≠ 0 := borromeanQuark_denom_ne_zero
  rw [qbeta_eq_E0_h_net_p]
  field_simp

end QOU.Mass
