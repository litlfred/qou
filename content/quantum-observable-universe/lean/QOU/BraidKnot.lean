import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.ConfinementCategory
import QOU.BraidKnot.ElectronShell
import QOU.BraidKnot.DressedParticle
import QOU.BraidKnot.LevelSufficiency
import QOU.BraidKnot.ShellClosureStability
import QOU.BraidKnot.ShellNeutrality
import QOU.BraidKnot.MathlibBridge
import QOU.BraidKnot.ConfinementPhaseStratification
import QOU.BraidKnot.ThreeCalibrationInputs
import QOU.BraidKnot.ConfinementLevel
import QOU.BraidKnot.ChiralityWritheRibbon
import QOU.BraidKnot.GradedMarkovTraceFromGSFiltration
import QOU.BraidKnot.ResidueAtRoot
import QOU.BraidKnot.GBSpectralSequence
import QOU.BraidKnot.GradedTraceResidueSplit
import QOU.BraidKnot.GBResidueSpectralSum
import QOU.BraidKnot.JetTowerUniformDeltaMax
import QOU.BraidKnot.PhiQTowerAlgebraicStratification

/-!
# BraidKnot — Module Index

Re-exports all formalization modules for the confinement framework:
confined particles, the confinement category, electron shells,
dressing morphisms, level sufficiency, shell-closure stability,
and phase stratification.

## Modules

- ConfinedParticle: (name, level, Markov class, coarse strand count)
- ConfinementCategory: Conf with {unfold, fold, dress} morphisms
- ElectronShell: cabled-strand shell with SDP binding subword
- DressedParticle: codomain of a dressing morphism
- LevelSufficiency: Markov-trace preservation under unfolding
- ShellClosureStability: σ_F monotone, noble-gas terminality
- ShellNeutrality: full-twist θ_n = 1 ↔ κ_λ = 0 ↔ self-conjugate λ
- MathlibBridge: fromMathlib bridge to Mathlib.Combinatorics.Young.YoungDiagram
- ConfinementPhaseStratification: Ω(P) open, local μ constancy
- ChiralityWritheRibbon: a_K = 1 + w·h + O(h²) from ribbon-twist framing
-/
