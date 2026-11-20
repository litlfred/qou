---
# qou-o3so
title: 'PROVE(lean): pair_skein_mass_formula — theorem pair_skein_mass_formula : ∀ a b : ℕ, S_ab a b = (q * μ a + q⁻¹ * μ b) / (Real.sqrt [cited jones1987,manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-jones1987
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-11-20T09:30:00Z
parent: qou-aabg
---

**File:** `QOU/HadronicMass/pair_skein_mass_formula.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/HadronicMass/pair_skein_mass_formula.lean

### `pair_skein_mass_formula`  —  line 64  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem pair_skein_mass_formula : ∀ a b : ℕ, S_ab a b = (q * μ a + q⁻¹ * μ b) / (Real.sqrt q + 1 / Real.sqrt q) `
- **Cited:** `[jones1987]`, `[manuscript]`, `[jones1987]`
  - [jones1987] Jones (1987), *Hecke algebra representations of braid groups and link polynomials* — https://doi.org/10.2307/1971403
  - [manuscript] quantum-observable-universe/observations/pair-skein-mass-formula.md
- **Tractability:** S_ab = (q·μ_a+q⁻¹·μ_b)/(√q+1/√q) skein mass formula; repo compute identity (Real.sqrt present).
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## Round 69 Update (lane-e667)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/DescendedTraceNormCentralChannelSplitPairSkeinChiralityLinkingVolumePerturbation.lean`
- 80-dps mpmath probe: `computations/probes/descended_trace_norm_central_channel_split_pair_skein_chirality_linking_volume_perturbation_probe.py`
- Witness: `computations/probes/descended-trace-norm-central-channel-split-pair-skein-chirality-linking-volume-perturbation.witness.json` (`scriptHash = 95d51dea43d2`, `scriptCommitSha = 64331862e639c45c7af4076683d01a06c6112e41`)
- PR: https://github.com/litlfred/qou/pull/8377 (`395a22d2b9a8d9ca11ced0eeab9414dd76df1c20`)

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

Claim released (stalled since 2026-10-04). The PROVE task cannot be done as titled. `pair_skein_mass_formula` is now a Prop-valued definition over caller data. With `S_ab` free the identity is refutable (`not_pair_skein_mass_formula_of_free_data`). Its normaliser `1/(q^{1/2}+q^{-1/2})` is z_C, so it is convention C; disposition by `qou-z9ws`. Re-derivation under D is `qou-cds1`'s, not a z-swap. Open batch PR #8377 (W4's queue) claims this bean but adds only Int ring identities on a cleared-denominator numerator. That does not prove the formula. Not closed: the D-frame pair-Skein mass is open (rule 13a).
