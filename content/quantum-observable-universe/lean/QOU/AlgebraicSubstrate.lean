import QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral
import QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases
import QOU.AlgebraicSubstrate.JointGaloisBraidFigure8
import QOU.AlgebraicSubstrate.JointGaloisBraidDischarged
import QOU.AlgebraicSubstrate.AdelicSubstrate
import QOU.AlgebraicSubstrate.MotivicSubstrate
-- `MotivicSubstrateTrivial` deliberately NOT aggregated here:
-- the trivial `MotivicSubstrate ℤ ℤ trivialTarget` instance
-- would otherwise pollute typeclass search anywhere
-- `QOU.AlgebraicSubstrate` (and thus `QOU`) is imported.
-- Modules that need the witness must opt in explicitly with
-- `import QOU.AlgebraicSubstrate.MotivicSubstrateTrivial`.
-- Cf. copilot-pull-request-reviewer review on PR #541.
import QOU.AlgebraicSubstrate.ReebEpsilon
import QOU.AlgebraicSubstrate.QFromEpsilon
import QOU.AlgebraicSubstrate.SurrealRateCalculus
import QOU.AlgebraicSubstrate.SurrealSqueeze
import QOU.AlgebraicSubstrate.PvsNPQou
import QOU.AlgebraicSubstrate.MetallicHierarchy

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
