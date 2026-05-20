-- Quantum Observable Universe — Lean 4 Formalization
--
-- This project formalizes the mathematical content of the QOU manuscript.
-- Each chapter has a corresponding Lean file.
--
-- Status tracking:
--   - Unproved goals are marked with placeholder tactics
--   - `proof-objects.json` in the repo root tracks formalization status
--   - LeanBlueprint macros in the LaTeX source link to declarations here

-- NOTE: Fred2005 has moved to content/fred2005-formal-groups/lean/
-- import Fred2005

import QOU.Basic
import QOU.MathlibExt
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.MathlibExt.SDPRealUniqueness
-- Per Copilot review: `QOU.MathlibExt.SDPRankEquality` is kept
-- OUT of the top-level umbrella while it still has `sorry`
-- placeholders (rank-nullity Mathlib API + Goldman-Tucker
-- categorical axiom).  Downstream code that needs the full
-- rank-equality chain can import it directly:
--   `import QOU.MathlibExt.SDPRankEquality`
-- This keeps QOU's baseline dependency surface clean for
-- consumers who only need the closed (interior + active-empty)
-- cases via `SDPRealUniqueness`.
import QOU.MathlibExt.PosSemidefTraceZero
import QOU.MathlibExt.PosSemidefDiagZero
import QOU.MathlibExt.FrobeniusInnerProduct
import QOU.MathlibExt.QPlancherel
import QOU.MathlibExt.MonoidalCalcVar
import QOU.HeckeAlgebra
import QOU.Glossary
import QOU.KnotTheory
import QOU.KnotRegistry
import QOU.MassDerivation
import QOU.Calculations
import QOU.HadronicMass
import QOU.AtomicMass
import QOU.QuantumObservableUniverse
import QOU.Elaboration
import QOU.PathIntegrals
import QOU.MobiusEnergy
import QOU.Torsion
import QOU.BringsSurface
import QOU.DescartesUniverse
import QOU.PAdicQuantumGroups
import QOU.GaugeFieldFluidDynamics
import QOU.InformationTheory
import QOU.LightningPath
import QOU.RepresentationTheory
import QOU.GradedFrobeniusHopf
import QOU.ChannelSeparation
import QOU.Descartes
import QOU.Interactions
import QOU.Encounter
import QOU.BraidKnot
import QOU.FlavorDressing
import QOU.ArchimedeanMassFormula
import QOU.CODATAChain
import QOU.ClassicalLimitObstruction
import QOU.FeynmanPathIntegrals
import QOU.MathConstants
import QOU.PhotonThreading
import QOU.QBirchSwinnertonDyer
import QOU.QCollatz
import QOU.QGeometricLanglands
import QOU.AppendixSurreals
import QOU.AlgebraicSubstrate
import QOU.LiftingDescent
import QOU.LiftingDescent.HomologicalCondensation
import QOU.LiftingDescent.BBStratification
import QOU.MotivesArchimedean
import QOU.MassEndomorphism
import QOU.PhiQPiece
import QOU.Kashaev
import QOU.PhiQJSJ
import QOU.Infra
import QOU.Observations.AlgebraicGnsEmbedding
import QOU.Observations.QCltNonCommutative
import QOU.Observations.TraceLocalityMeetsGsNonLocality
import QOU.MathlibExt.RpowAlgebra
import QOU.Braiding.HnMarkovTrace
import QOU.Braiding.TrMHopfSigma1SqClosedForm
import QOU.Information.HeckeLogDecomposition
import QOU.JetHorizon
import QOU.MagicShell.DeltaCouplingSubstrateForm
-- Migrated from content-tree extract
-- (`quantum-observable-universes/categorical-dq-squared-proof.lean`).
-- See `AUDIT-REPORT.md §P3` for the open non-vanishing direction.
import QOU.CategoricalDqSquared
import QOU.frobenius_relation
import QOU.dq_squared
import QOU.emergence_to_quantum_flat
import QOU.su2_emergence_dagger_unitarity
import QOU.su2_emergence_volume_determinant
import QOU.frobenius_dagger_positive_definite
import QOU.volume_from_rigidity
import QOU.substrate_radial_coordinate
import QOU.Braiding.non_self_intersection
import QOU.Information.p_bandwidth_bound
