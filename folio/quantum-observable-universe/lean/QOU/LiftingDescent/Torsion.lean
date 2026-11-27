-- Chapter 4 — Lifting of Quantum Torsion
--
-- Split into section-based modules for parallel build and progress tracking.
-- Each file corresponds to one or more §-sections of the manuscript.

import QOU.LiftingDescent.Torsion.JetProlongation
import QOU.LiftingDescent.BraneTower
import QOU.LiftingDescent.MassIdentity
import QOU.LiftingDescent.ArchimedeanMassIdentity
import QOU.LiftingDescent.MassTraceIdentity
import BraidKnotOctonion.MassTraceMarkov
import QOU.LiftingDescent.YekutielijTriple  -- AUDIT: typo variant; YekutieliTriple.lean is the canonical spelling
import QOU.LiftingDescent.YekutieliTriple
import QOU.LiftingDescent.Descent
import QOU.LiftingDescent.DescentCondition
import QOU.LiftingDescent.GlobalGluing
import QOU.LiftingDescent.TopologicalMass
import QOU.LiftingDescent.TopologicalMassEquality
import QOU.LiftingDescent.MassGap
import QOU.LiftingDescent.quantum_dilogarithm
import QOU.LiftingDescent.skein_generation
import QOU.LiftingDescent.brane_boundary_structure
-- Sibling-import cluster wire-in (2026-06-01): content-tree extract
-- migrated into the Lake build (see
-- docs/audits/2026-06-01-sibling-import-cluster-wire-in-plan.md).
-- Module path is QOU.Torsion.HeckeMassElement; its declarations live in
-- the QOU.Braiding namespace (module path ≠ namespace), so the block's
-- lean.ref qou:QOU.Braiding.HeckeMassElement is unchanged. COMPILE-PENDING.
import HeckeTemperleyLieb.HeckeMassElement
import QOU.LiftingDescent.MultiplicativeIntegralCurvature
