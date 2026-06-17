import QOU.MassEndomorphism.DeltaMaxUniformBound
import QOU.MassEndomorphism.MassEndomorphismConjecture
import QOU.MassEndomorphism.PhiQConvergence
import QOU.MassEndomorphism.ZHabiroCauchy
-- `MassEndomorphismTrivial` deliberately NOT aggregated here:
-- the zero-data `MassEndomorphism ℤ β` instance would otherwise
-- satisfy `MassEndomorphism` typeclass searches in unrelated
-- developments.  Opt in explicitly with
-- `import QOU.MassEndomorphism.MassEndomorphismTrivial`.
-- Cf. copilot-pull-request-reviewer review on PR #541.

/-!
# QOU.MassEndomorphism — Mass-endomorphism tower aggregator

Aggregator for the mass-endomorphism tower modules:

- `DeltaMaxUniformBound` — the Archimedean / rank-1 SDP closure of
  the per-level residual bound (`prop:delta-max-uniform-bound`),
  with `OperatorNormBound` discharging the
  `JetTowerUniformDeltaMax` conjectural class on its rank-1 leaf.
- `PhiQConvergence` — the analytic convergence prerequisite of the
  brane-tower conjecture: `Φ_q(z)` is `Multipliable` for `1 < q`,
  `|z| < q` (`quantumDilog_multipliable`).
- `ZHabiroCauchy` — the algebraic Cauchy-limit half of
  `conj:brane-tower-z-habiro`: the z-Habiro filtration descending
  chain, the increment-coherence Cauchy core, and the conditional
  inverse-limit thread (all sorry-free; the brane-tower-specific
  increment input + the completion-ring packaging remain open — see
  the module header).

The pre-Arch tier of the mass-endomorphism tower lives in
co-located stubs at
`braids-and-knots/mass-endomorphism-tower.lean` (`Pre` and `Arch`
namespaces); a formal-chain port is a follow-up.

Per `QOU.GroundRingAnnotations`, the contents of this aggregator
include both pre-Arch and Arch tiers — the namespace separation
in each module makes the tier explicit.
-/
