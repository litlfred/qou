import QOU.BringsSurface.KernelGrowthBound
import QOU.BringsSurface.PolyhedralDomination
import QOU.BringsSurface.OhtsukiKappaFormal
import QOU.BringsSurface.DominationTowers
import QOU.BringsSurface.DominationSqueeze
import QOU.BringsSurface.TwoFiltrationBridgeGeneral
import QOU.BringsSurface.TwoFiltrationBridgeSmallCases
import QOU.BringsSurface.JointGaloisBraidFigure8
import QOU.BringsSurface.JointGaloisBraidDischarged
import QOU.BringsSurface.AdelicSubstrate
import QOU.BringsSurface.MotivicSubstrate
-- `MotivicSubstrateTrivial` deliberately NOT aggregated here:
-- the trivial `MotivicSubstrate ℤ ℤ trivialTarget` instance
-- would otherwise pollute typeclass search anywhere
-- `QOU.AlgebraicSubstrate` (and thus `QOU`) is imported.
-- Modules that need the witness must opt in explicitly with
-- `import QOU.AlgebraicSubstrate.MotivicSubstrateTrivial`.
-- Cf. copilot-pull-request-reviewer review on PR #541.
import QOU.BringsSurface.ReebEpsilon
import QOU.BringsSurface.CartanContraction
import QOU.BringsSurface.QFromEpsilon
import QOU.BringsSurface.SurrealRateCalculus
import QOU.BringsSurface.SurrealSqueeze
import QOU.BringsSurface.PvsNPQou
import QOU.BringsSurface.MetallicHierarchy
import QOU.BringsSurface.WignerAxiom

/-!
# QOU.AlgebraicSubstrate — Chapter 8 aggregator

Aggregator module for the algebraic-substrate chapter:

- **Adelic substrate** (`AdelicSubstrate.lean`) — the rational adele
  ring `𝔸_ℚ` interface used for Tate-thesis factorisations.
- **Reeb infinitesimal** (`ReebEpsilon.lean`) — the categorical
  primitive `ε = d/dt|_{t=0} Φ_t` of the Reeb flow.
- **`q = 1 + ε`** (`QFromEpsilon.lean`) — the substrate parameter
  as a derived surreal-valued scalar.
- **Surreal rate calculus** (`SurrealRateCalculus.lean`) — the
  four classical-limit rate laws.
- **Surreal squeeze** (`SurrealSqueeze.lean`) — the common
  punchline `δ² · ε⁻¹ > ε³`.
- **P vs NP conjecture** (`PvsNPQou.lean`) — the QOU-framework
  complexity-theoretic squeeze instance.
-/
