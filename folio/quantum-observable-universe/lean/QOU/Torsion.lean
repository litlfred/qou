-- Chapter 4 — Lifting of Quantum Torsion
--
-- Split into section-based modules for parallel build and progress tracking.
-- Each file corresponds to one or more §-sections of the manuscript.

import QOU.Torsion.JetProlongation
import QOU.Torsion.BraneTower
import QOU.Torsion.MassIdentity
import QOU.Torsion.ArchimedeanMassIdentity
import QOU.Torsion.MassTraceIdentity
import QOU.Torsion.MassTraceMarkov
import QOU.Torsion.YekutielijTriple  -- AUDIT: typo variant; YekutieliTriple.lean is the canonical spelling
import QOU.Torsion.YekutieliTriple
import QOU.Torsion.Descent
import QOU.Torsion.DescentCondition
import QOU.Torsion.GlobalGluing
import QOU.Torsion.TopologicalMass
import QOU.Torsion.TopologicalMassEquality
import QOU.Torsion.MassGap
import QOU.Torsion.quantum_dilogarithm
import QOU.Torsion.skein_generation
import QOU.Torsion.brane_boundary_structure
-- Sibling-import cluster wire-in (2026-06-01): content-tree extract
-- migrated into the Lake build (see
-- docs/audits/2026-06-01-sibling-import-cluster-wire-in-plan.md).
-- Module path is QOU.Torsion.HeckeMassElement; its declarations live in
-- the QOU.Braiding namespace (module path ≠ namespace), so the block's
-- lean.ref qou:QOU.Braiding.HeckeMassElement is unchanged. COMPILE-PENDING.
import QOU.Torsion.HeckeMassElement
