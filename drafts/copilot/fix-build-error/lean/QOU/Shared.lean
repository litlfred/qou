/-!
# QOU.Shared — index of shared typeclass roots

Re-exports the four shared typeclass roots used to factor out
common context across ~70 Lean blocks:

| Typeclass | Used by | Manuscript theme |
|-----------|---------|------------------|
| `QOU.Shared.MarkovTraceContext` | ~40 blocks | Hecke + Markov trace |
| `QOU.Shared.OperatorSelectionLPContext` | ~10 blocks | LP primal/dual |
| `QOU.Shared.WedderburnBlockDecompositionContext` | ~15 blocks | Wedderburn / Plancherel |
| `QOU.Shared.SobolevHkRegularityContext` | ~5 blocks | q-NS Sobolev regularity |

Each typeclass bundles the manuscript-shared structure (coefficient
ring, substrate parameter, etc.) so per-block classes only have to
specify the substantive claim.

See `.claude/skills/local/lean-substantive-pass.md` for usage
patterns.
-/

import QOU.Shared.MarkovTraceClaim
import QOU.Shared.OperatorSelectionLP
import QOU.Shared.WedderburnBlockDecomposition
import QOU.Shared.SobolevHkRegularity
