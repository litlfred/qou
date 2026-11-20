# Pre-registration: the lepton-strand premise and the physical passage of #8638

Bean `qou-99qc` (N1 thread), also `qou-g0jn`. Owner (Carl), 2026-11-20 ~20:15: *derive, don't choose*.
Written 2026-11-20 before the Lean file. One exploratory sympy run (the all-weak-vertex passage, Q3c below)
was made BEFORE this file was written; it is marked as such.

## The object under test

`ChargedCurrentW.lean` (#8638): `n ⊗ ν → e⁻ ⊗ p` through the leftward positive passage `σ₁σ₂σ₃` is
`(h·q)·T⁺`; through the rightward negative passage `σ₃⁻¹σ₂⁻¹σ₁⁻¹` it is `−(h/q)·T⁺`. It rests on
ASSUMPTION L (the lepton is one more strand carrying the same doublet `V`, with `ν = u`, `e⁻ = d`) and on an
open CHOICE (which passage). #8636 (N2) used the same choice, labelled C-lep.

## Questions and predictions (stated before proving)

* **Q1 (assignment inside L).** If the lepton is a `V`-strand, is `ν = u, e⁻ = d` forced? Prediction: yes,
  by conservation of total weight (`Ř` commutes with `K ⊗ K`), and the opposite assignment and a singlet lepton
  are both excluded, scope (b), invariant = total `T³`. Also consistent with `Q = T³ + Y/2` with one `Y` per
  doublet: `Q(ν) − Q(e⁻) = 1` forces the same order.
* **Q2 (L itself).** Does any corpus definition imply L? Prediction: no. `def:electron-knot` (trefoil
  `T(2,3)`), `def:neutrino-knot` (unknot), `def:antineutrino-knot` (β⁻ as the `L₀⁻` skein smoothing) define
  leptons as knot types / smoothing products, not as a strand colour. Underdetermined; alternatives enumerated.
* **Q3 (passage).** Does the owner-ruled left line select one passage? Prediction: NO, for three reasons to
  be proved: (a) `σ` and `σ⁻¹` act as scalars on the same left line; (b) the weak vertex `W_L = q⁻¹J`,
  strand-tracked, has a β entry in BOTH strand orientations, equal magnitude `q⁻¹h/[2]`, so it is blind to
  the direction of passage; (c) the passages are bar/mirror images. **Q3c (run before this file):** with every
  lepton crossing replaced by `W_L`, the β block is not proportional to `T⁺` and the reverse block is nonzero.
* **Q3′ (a corpus convention that does select).** Among the four single-sign passages (left/right × ±) only
  leftward-positive and rightward-negative have a nonzero β block. The corpus draws `e⁻` as the positive braid
  `σ³` (solid, forward time) and `ν̄` with negative orientation (so the incoming `ν` is positive). Transferring
  that orientation to the lepton strand selects leftward-positive (`hq`, C-lep). Prediction: this is a
  conditional selection — it needs a bridge (knot chirality ⇒ strand crossing sign), not a theorem of the corpus.
* **Q4.** `e⁻ = σ₀σ₁σ₀` (γγ normal-form coordinate) closes to a 2-component link; `T(2,3)` closes to 1
  component. Prediction: different objects; and neither is the strand-colour electron of L.

Nothing is fitted; no experimental number enters.

## RESULTS (2026-11-20, `LeptonStrandPremise.lean`, 28 declarations, lean-direct exit 0, no `sorryAx`)

* **Q1 held.** `lepton_assignment_forced`, `singlet_lepton_excluded`, `gmn_forces_order`,
  `lepton_hypercharge` (`Y = −1`), with the conservation law `Rc_commute_Kt` +
  `entry_eq_zero_of_commute_diagonal` + `zpow_ne_of_ne`. Inside L, `ν = u, e⁻ = d` is DERIVED and the
  opposite labelling / a singlet lepton are EXCLUDED (scope (b), invariant total `T³`).
  **This derivation uses the lepton strand INSIDE the `K`-grading.** Sibling #8661
  (`CartanEnergyTransport.lean`) proves that with the lepton inside the grading every `K`-weighted split of
  the energy is 0; the scored `Q_β = 0.3254 MeV` cell (#8586) is nonzero only because the lepton is kept
  outside the grading. So the amplitude `(q²−1)·T⁺` (lepton inside) and the scored `Q_β` (lepton outside)
  rest on incompatible readings of the same strand.
* **Q2 held.** No corpus definition implies L (grep of `def:electron-knot`, `def:neutrino-knot`,
  `def:antineutrino-knot`, `def:lepton-number-categorical`, `def:up-quark`, `def:down-quark`). Underdetermined.
* **Q3 held.** `sigma_on_left` / `sigmaInv_on_left`: both crossings are scalars on one left line.
  `WL_beta_both`: `W_L` flips flavour in both strand orientations, magnitude `(q²−1)/(q(q²+1))`.
  `WR_beta_ratio`: `W_R` is `q²` times `W_L` (the same `q²` as `hq` vs `h/q`). Q3c (probe, exact sympy):
  the all-`W_L` passage block is not proportional to `T⁺` and its reverse block is nonzero (output below).
  The left line does not select the passage.
* **Q3′ held, conditionally.** `beta_left_pos = (q²−1)·T⁺`, `beta_right_neg = −((q²−1)/q²)·T⁺`,
  `beta_left_neg = beta_right_pos = 0`, `passage_nonzero_iff`, `positive_selects_left`. With the bridge
  "the electron's positive braid `σ₁³` fixes the sign of the lepton strand's crossings" the C-lep passage is
  selected. The bridge is not a theorem.
* **Q4 held.** `perm_e_gg` (`σ₀σ₁σ₀ ↦ (0 2)`), `e_gg_fixed_strand`, `trefoil_one_component`.
