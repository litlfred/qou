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
