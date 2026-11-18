---
# qou-0w3s
title: 'Descent inputs of CatDescendedInputs (cat_descended_is_base_mass.lean): no sorries remain, two open inputs'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:08Z
updated_at: 2026-10-10T07:01:01Z
parent: qou-aabg
---

**File:** `QOU/TopologicalMass/cat_descended_is_base_mass.lean` (QOU)  ·  2 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/TopologicalMass/cat_descended_is_base_mass.lean

### `descended_trace_is_base_trace`  —  line 79  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem descended_trace_is_base_trace : trFrob (tauHat alpha) = baseTrace `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.md
- **Tractability:** trFrob(τ̂ α) = baseTrace descent identity; repo categorical-trace infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `base_mass_is_norm_of_base_trace`  —  line 89  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem base_mass_is_norm_of_base_trace : mnorm baseTrace = baseMass `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.md
- **Tractability:** mnorm(baseTrace) = baseMass; repo mass-norm identity.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.


## 2026-10-10 — status update (title changed; survey for epic `qou-d8c7`, issue #7547)

Former title: 'PROVE(lean): cat_descended_is_base_mass.lean — 2 cited sorries [cited manuscript]'.

The body above describes a file that no longer exists in that form. Checked on `main` 2026-10-10: `QOU/TopologicalMass/cat_descended_is_base_mass.lean` has **no `sorry`**. The two identities are now fields of `class CatDescendedInputs : Prop` (documented as "Open input 1" and "Open input 2"), and the two theorems project them (`ctx.trace_compat` and its sibling). So the open item is the two class inputs, not two sorries. `qou-50p7` recorded the structural wall: as stated the inputs relate independent opaque constants, so nothing in the repo forces them.

Tracked under carrier M2 (`tmvac`) of epic `qou-d8c7`. Stays open: the inputs are conjectural (rule 13a).

## Round 69 Update (lane-e667)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/DescendedTraceNormCentralChannelSplitPairSkeinChiralityLinkingVolumePerturbation.lean`
- 80-dps mpmath probe: `computations/probes/descended_trace_norm_central_channel_split_pair_skein_chirality_linking_volume_perturbation_probe.py`
- Witness: `computations/probes/descended-trace-norm-central-channel-split-pair-skein-chirality-linking-volume-perturbation.witness.json` (`scriptHash = 95d51dea43d2`, `scriptCommitSha = 64331862e639c45c7af4076683d01a06c6112e41`)
- PR: https://github.com/litlfred/qou/pull/8377 (`395a22d2b9a8d9ca11ced0eeab9414dd76df1c20`)
