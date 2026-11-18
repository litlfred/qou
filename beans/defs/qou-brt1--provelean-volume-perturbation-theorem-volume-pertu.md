---
# qou-brt1
title: 'PROVE(lean): volume_perturbation — theorem volume_perturbation [ctx : VolumePerturbationContext] : ∀ k : ℕ, 4 ≤ k → ctx.δΦ k  [cited manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:04Z
updated_at: 2026-10-04T15:22:48Z
parent: qou-t5uj
---

**File:** `QOU/BraidKnot/volume_perturbation.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/BraidKnot/volume_perturbation.lean

### `volume_perturbation`  —  line 81  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem volume_perturbation [ctx : VolumePerturbationContext] : ∀ k : ℕ, 4 ≤ k → ctx.δΦ k = ctx.z ^ 2 * ctx.Vol_41 * qIntSym ctx.q ((k : ℤ) - 3) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-theory/volume-perturbation-formula.md
- **Tractability:** δΦ_k = z²·Vol(4₁)·qIntSym identity over a context class; repo compute identity.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## Round 69 Update (lane-e667)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/DescendedTraceNormCentralChannelSplitPairSkeinChiralityLinkingVolumePerturbation.lean`
- 80-dps mpmath probe: `computations/probes/descended_trace_norm_central_channel_split_pair_skein_chirality_linking_volume_perturbation_probe.py`
- Witness: `computations/probes/descended-trace-norm-central-channel-split-pair-skein-chirality-linking-volume-perturbation.witness.json` (`scriptHash = 95d51dea43d2`, `scriptCommitSha = 64331862e639c45c7af4076683d01a06c6112e41`)
- PR: https://github.com/litlfred/qou/pull/8377 (`395a22d2b9a8d9ca11ced0eeab9414dd76df1c20`)
