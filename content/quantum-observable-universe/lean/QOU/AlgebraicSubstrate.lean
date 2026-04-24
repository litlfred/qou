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

import QOU.AlgebraicSubstrate.AdelicSubstrate
import QOU.AlgebraicSubstrate.ReebEpsilon
import QOU.AlgebraicSubstrate.QFromEpsilon
import QOU.AlgebraicSubstrate.SurrealRateCalculus
import QOU.AlgebraicSubstrate.SurrealSqueeze
import QOU.AlgebraicSubstrate.PvsNPQou
