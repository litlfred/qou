import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Tactic.Ring

/-!
# QOU.Glossary — index of where each glossary term is formalised

This file used to hold 21 axiom-free `structure`s and two numeric `def`s,
generated on 2026-04-01 by the since-deleted `ontologist.py`.  None of them had
a consumer: 45 files imported this module and no file used any of its names.
Each structure carried bare fields with no axioms, so it asserted nothing
(issue #8012).  They are removed.  This index records where each term is
formalised now.

The imports above are kept on purpose: removing them could break an importer
that relies on them transitively.

## Superseded by a live declaration

| Old glossary name | Live declaration |
|---|---|
| `KahlerDifferentials` | `QOU.MathlibExt.UniversalDifferentials.Ω1` (the noncommutative universal calculus `ker μ`), and the field `QuantumUniverse.differentialForms` |
| `FrobeniusHopfObject` | `QOU.FrobeniusHopfData` (`QOU/QuantumObservableUniverse/CategoricalFoundations.lean`) |
| `FibreFunctor` | `QOU.BraidsKnots.FibreFunctor` (`QOU/MotivesArchimedean.lean`), and the `fibreFunctor` field of `QOU.QuantumUniverse` |
| `QuantumGaugeGroup` | `QOU.QuantumGaugeGroup` (`QOU/QuantumObservableUniverse/SubstrateParameter.lean`) |
| `BringsSurface` | `QOU.BringsSurface.BringsSurface` (`QOU/BringsSurface.lean`) |
| `JetProlongation` | `QOU.Torsion.JetProlongation` (`QOU/Torsion/JetProlongation.lean`) |
| `BraidGroup` | `QOU.MathlibExt.Braid.BraidGroup` (`QOU/MathlibExt/BraidGroup.lean`) |
| `quantumParameter`, `substrateParameter` | `QOU/QuantumObservableUniverse/SubstrateParameter.lean`.  The removed `quantumParameter` hard-coded `1.1097`, a numerical value that does not belong in a library definition. |

## Available in Mathlib

| Old glossary name | Mathlib declaration |
|---|---|
| `BinaryDihedralGroup` | `QuaternionGroup n`, the dicyclic group of order `4n`.  The binary dihedral group of order 12 is `QuaternionGroup 3`. |
| `FIsocrystal` | `WittVector.Isocrystal` (`Mathlib/RingTheory/WittVector/Isocrystal.lean`) |

These are pointers, not aliases.  An `abbrev` would make all 45 importers load
those Mathlib modules for a name nothing uses.

## Removed with no counterpart

`PrincipalBundle`, `LusztigIntegralForm`, `AdjointObject`, `CRManifold`,
`LeviForm`, `WebsterMetric`, `ReebVectorField`, `HodgeStarH`,
`YangMillsFunctional`, `SelfDualCurvature`, `StateBundle`, `QLaplacian`.  A
future formalisation should state the term's defining axioms where it is used,
not here.
-/

namespace QOU.Glossary

end QOU.Glossary
