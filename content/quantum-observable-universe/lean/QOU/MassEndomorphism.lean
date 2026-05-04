import QOU.MassEndomorphism.DeltaMaxUniformBound
import QOU.MassEndomorphism.MassEndomorphismConjecture
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

The pre-Arch tier of the mass-endomorphism tower lives in
co-located stubs at
`braids-and-knots/mass-endomorphism-tower.lean` (`Pre` and `Arch`
namespaces); a formal-chain port is a follow-up.

Per `QOU.GroundRingAnnotations`, the contents of this aggregator
include both pre-Arch and Arch tiers — the namespace separation
in each module makes the tier explicit.
-/
