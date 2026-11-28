import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The Gibbs nucleon split with the Coulomb pair term in the weight (route 1 of item C1)

Owner card 2026-11-27, option 1: "Derive c_em and E (Gibbs)". Bean `qou-myts`.

`NucleonSplitSingleElement` inserted the all-pairs charge term linearly, `K + c·Q_pair`. In a
Gibbs (free-energy) reading the energy enters the weight as an exponential, `e^{−H/E}`, with
`E = k_BT_q`. Route T fixes that temperature: `k_BT_q = E₀` (`SpectatorEnergyMap.kT_eq_e0`), so
`E` is derived. On a nucleon weight space `Q_pair` is a scalar (`0` on `W_p`, `−1/3` on `W_n`),
so the Coulomb factor `exp(−λ·Q_pair/E)` is a scalar too and the free energy is exact, not
linearised:

    m_N = −E·log(q^{±1}·t) + λ·Q_pair,N + c₀,
    m_n − m_p = 2E·log q + λ·(Q_pair,n − Q_pair,p) = 2E·log q − λ/3.

`λ` is the Coulomb energy per unit charge product. The temperature cancels from the Coulomb
part. Sign: repulsion is `λ > 0`, and then the Coulomb term **lowers** `m_n − m_p`
(`gibbs_coulomb_split_lt_cell`). This matches the sign of the electromagnetic part of the
physical split and `NucleonChargeTerms.adopted_selfenergy_sign` for the self-energy form.

Correction to `NucleonSplitSingleElement` (sign convention, not a change to any theorem there):
the linear coupling `c` in `K + c·Q_pair` that corresponds to Coulomb repulsion is `c < 0`, so
the remark "for `c ≥ 0` the Gibbs cell can only grow" covers the attractive sign only.

What is not derived here: the value of `λ`. The corpus's on-record candidate is
`λ = α_em(q₀)·E₀^{tower}` (`computations/crossing_covariant_qed_probe.py`, conditional on the
unproved CS Gram-ratio identification, bean `qou-wkgp`; the old Witten-κ Gram `sorry` was
refuted and removed 2026-11-20). Numbers are in
`computations/probes/nucleon_split_gibbs_coulomb_probe.py`.

-- Ref: [leitner2026] docs/audits/2026-11-27-nucleon-split-gibbs-coulomb.md
-- Ref: [leitner2026] docs/audits/2026-11-21-qbeta-energy-map-spectator.md
-/

namespace QOU.QBeta.NucleonSplitGibbsCoulomb

/-- Gibbs mass of a nucleon: `−E·log(K-weight · t) + λ·Q_pair + c₀`. -/
noncomputable def gibbsMass (E lam c₀ k t Qpair : ℝ) : ℝ :=
  -E * Real.log (k * t) + lam * Qpair + c₀

/-- **The exact Gibbs split with the Coulomb pair term.** Proton weight `q`, pair charge `0`;
neutron weight `q⁻¹`, pair charge `−1/3`; same common trace `t > 0`. -/
theorem gibbs_coulomb_split_eq {q E lam c₀ t : ℝ} (hq : 0 < q) (ht : 0 < t) :
    gibbsMass E lam c₀ q⁻¹ t (-1 / 3) - gibbsMass E lam c₀ q t 0 =
      2 * E * Real.log q - lam / 3 := by
  unfold gibbsMass
  rw [Real.log_mul (inv_pos.mpr hq).ne' ht.ne', Real.log_mul hq.ne' ht.ne', Real.log_inv]
  ring

/-- Repulsion (`λ > 0`) lowers the split below the route-T cell `2E·log q`. -/
theorem gibbs_coulomb_split_lt_cell {q E lam c₀ t : ℝ} (hq : 0 < q) (ht : 0 < t)
    (hlam : 0 < lam) :
    gibbsMass E lam c₀ q⁻¹ t (-1 / 3) - gibbsMass E lam c₀ q t 0 < 2 * E * Real.log q := by
  rw [gibbs_coulomb_split_eq hq ht]
  linarith

/-- The split stays positive while `λ < 6E·log q`. -/
theorem gibbs_coulomb_split_pos {q E lam c₀ t : ℝ} (hq : 0 < q) (ht : 0 < t)
    (hlam : lam < 6 * E * Real.log q) :
    0 < gibbsMass E lam c₀ q⁻¹ t (-1 / 3) - gibbsMass E lam c₀ q t 0 := by
  rw [gibbs_coulomb_split_eq hq ht]
  linarith

/-- **What `λ` must be for a given target split `Δ`**: `λ = 3·(2E·log q − Δ)`. Stated so the
required value can be compared with a derived one; it selects nothing. -/
theorem gibbs_coulomb_lambda_of_split {q E lam c₀ t Δ : ℝ} (hq : 0 < q) (ht : 0 < t)
    (h : gibbsMass E lam c₀ q⁻¹ t (-1 / 3) - gibbsMass E lam c₀ q t 0 = Δ) :
    lam = 3 * (2 * E * Real.log q - Δ) := by
  rw [gibbs_coulomb_split_eq hq ht] at h
  linarith

end QOU.QBeta.NucleonSplitGibbsCoulomb
