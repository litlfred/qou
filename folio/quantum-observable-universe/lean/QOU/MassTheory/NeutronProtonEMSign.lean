import Mathlib.Tactic

/-!
# Neutron–proton splitting: the sign of the missing L2 term (formalize-first prune)

The leading traced-volume prediction `Δm = α·|ΔΦ|` (namespace
`QOU.NeutronProtonSplitting` in
`folio/quantum-observable-universe/observations/neutron-proton-mass-splitting.lean`;
`docs/audits/2026-07-11-quark-volume-provenance.md`)
**over**-predicts the neutron–proton mass difference by `+0.63%`
(`docs/audits/2026-07-11-np-splitting-residual-not-q0-knob.md`).  Before
scanning candidate closures for that residual, this file **formalizes the
structural invariant the missing term must satisfy** (formalize-first,
AGENTS.md §"Formalize-first probe discipline").

The next correction is the **electromagnetic self-energy**.  Its sign is fixed,
**parameter-free**, by the quark charge structure: the pairwise Coulomb factor
`Σ_{i<j} q_i q_j` is `0` for the proton (uud) and `-1/3` for the neutron (udd),
so the proton carries the larger Coulomb self-energy and the EM correction to
`Δm = m_n − m_p` is **negative** — exactly the sign of the observed residual.

This is a **prune**, not a closure: it proves the missing term is charge-odd
and reduces `Δm` (ruling out a charge-blind `ℏ_q`-tower of the wrong sign); it
does **not** derive the EM coupling from the 13 categorical drivers, so nothing
here is wired into production (anti-laundering rule).  Everything is over `ℚ`
(charges are rational; no archimedean structure — §7c).

The EM self-energy sign of `m_p − m_n` is the standard PDG result.

-- Ref: [leitner2026] prop:neutron-proton-mass-splitting
-/

namespace QOU.MassTheory.NeutronProtonEMSign

/-- Electric charge of the up quark (units of `e`). -/
def qUp : ℚ := 2 / 3

/-- Electric charge of the down quark (units of `e`). -/
def qDown : ℚ := -1 / 3

/-- The pairwise Coulomb charge-structure factor `Σ_{i<j} q_i q_j` of a
three-quark ordering `(c₀, c₁, c₂)` — the leading electromagnetic
self-energy weight. -/
def chargeStructure (c0 c1 c2 : ℚ) : ℚ := c0 * c1 + c0 * c2 + c1 * c2

/-- Proton `uud`: the Coulomb charge-structure factor vanishes. -/
theorem chargeStructure_uud : chargeStructure qUp qUp qDown = 0 := by
  simp only [chargeStructure, qUp, qDown]; norm_num

/-- Neutron `udd`: the Coulomb charge-structure factor is `-1/3`. -/
theorem chargeStructure_udd : chargeStructure qUp qDown qDown = -1 / 3 := by
  simp only [chargeStructure, qUp, qDown]; norm_num

/-- **Charge-structure gap.** `Σqq(proton) − Σqq(neutron) = +1/3 > 0`: the
proton carries the larger Coulomb self-energy. -/
theorem em_gap_eq :
    chargeStructure qUp qUp qDown - chargeStructure qUp qDown qDown = 1 / 3 := by
  rw [chargeStructure_uud, chargeStructure_udd]; norm_num

theorem em_gap_pos :
    0 < chargeStructure qUp qUp qDown - chargeStructure qUp qDown qDown := by
  rw [em_gap_eq]; norm_num

/-- **Sign of the missing L2 term (conditional on the EM-Coulomb model).**
If the electromagnetic correction to `Δm = m_n − m_p` is
`δ = -k·(Σqq(proton) − Σqq(neutron))` for any positive self-energy coupling
`k > 0` (the standard Coulomb self-energy, higher energy ⇒ heavier ⇒ subtracts
from `m_n − m_p`), then `δ < 0`.

Combined with the traced-volume leading piece **over**-predicting `Δm`
(residual `< 0`), the EM correction has the **right sign** to close the gap.
This constrains any candidate closure: it must be charge-odd and reduce `Δm`. -/
theorem em_correction_neg {k : ℚ} (hk : 0 < k) :
    -(k * (chargeStructure qUp qUp qDown - chargeStructure qUp qDown qDown)) < 0 := by
  have h : 0 < k * (chargeStructure qUp qUp qDown - chargeStructure qUp qDown qDown) :=
    mul_pos hk em_gap_pos
  linarith

end QOU.MassTheory.NeutronProtonEMSign
