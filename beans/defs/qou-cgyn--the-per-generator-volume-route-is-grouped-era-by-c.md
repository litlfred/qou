---
# qou-cgyn
title: The per-generator volume route is grouped-era by construction and cannot express the borromean ordering
status: in-progress
pr: 8321
branch: feat/qou-ai7v-cgyn-k12x-u8ji-y2np
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T19:38:09Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
---


## What was measured

`computations/terms-2-3-atom-per-gen-mpfr-50dps.witness.json` stores
`wedderburn_vols` per atom. Their product is exactly the GROUPED |tr_M|:

    atom      channel   |Π wedderburn_vols|
    proton    std       1.14575969245730086968908     ← grouped proton, 24 digits
    neutron   std       0.98774368811580957163402     ← grouped neutron
    proton    full      1.02289598443797884083137
    neutron   full      0.887544546479944725313742

`T1_descended = |Π_i V̂_i|` in `derive_m_p_hecke_full_tower_50dps.py:271`, so
**T1 of the mass formula is a grouped-era quantity**, and it propagates to the
whole vhat cluster (`vhat_std_vs_full_tower_compare`, `vhat_tower_im_cancellation`,
`vhat_per_crossing_chain`).

## Why this is NOT a stale artifact, and not a mirror that drifted

Re-running the producer reports **unchanged** — it recomputes the same volumes
today. The reason is in the construction:

`terms_2_3_atom_per_gen_mpfr_50dps._nucleon_gen_chains_mpfr` builds

    # B₃ confinement: (σ₀ · σ₁⁻¹)³
    g0 = [(1, 0)]  * 3        # three σ₀
    g1 = [(1, -h)] * 3        # three σ₁⁻¹

— two SEPARATE per-generator chains. That is the grouped word: all σ₀ letters in
one list, all σ₁ letters in another. The comment names the alternating
`(σ₀·σ₁⁻¹)³` while the code cannot express it.

**And it is not a stale mirror of a fixed original.** The thing it mirrors,
`tools/pyhecke/python/pyhecke/atom.py::nucleon_gen_chains`, does the same:

    # B₃ confinement: (σ₀·σ₁⁻¹)³
    g0 = [(1, _d_sigma)] * 3
    g1 = [(1, _d_inv)]   * 3

So both are grouped, consistently. A per-generator factorisation is
**order-blind within a generator by construction** — that is what "per
generator" means — and the 2026-09-05 ruling (`qou-hu1f`) says the interleaving
is exactly what matters, with only the 2-dimensional (2,1) block moving.

## Why no symptom-keyed sweep could have found it

Neither file calls `atom_braid_word_3A`. A sweep looking for callers of the word
builder, or for producers that "use the ordering", finds nothing here. This is
precisely the case `qou-4383` was created for — keying on the VALUE — and it was
found by a 24-digit fingerprint match on a product, not on any stored field.

## What the work is, and what it is NOT

**NOT** "add `intra_order` to `_nucleon_gen_chains_mpfr`". The return type is
`(g0_chain, g1_chain)`; there is no place to put an interleaving in it. Changing
the ordering means changing what the function RETURNS, and then everything
downstream that consumes a per-generator decomposition.

The real questions, in order:

1. **Does the per-generator volume decomposition survive the ruling at all?**
   If |tr_M| under the borromean word does not factorise per generator, then
   T1 = |Π V̂_i| has no canonical counterpart and the tower's first term needs
   re-deriving rather than re-ordering.
2. If it does not, **what replaces T1** in `derive_m_p_hecke_full_tower_50dps`?
   `canonical_trm_reference.tr_m_nucleon` gives the canonical |tr_M| directly —
   but T1 is a *product of volumes*, and the tower's T2/T3 are built from the
   same `vols`, so substituting the total does not obviously preserve the
   decomposition the other terms rely on.
3. Only then, the mechanical part.

This is an owner-facing question about the mass formula's first term, not a
frame fix. Flagged, not attempted.

## Related

`qou-4383` (found it), `qou-hu1f` (the ruling), `qou-y4gi` (the ordering guard
that would have caught it had this route read a witness — it does not; it
computes).

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`FallbackTierWindowZeroingAndPerGeneratorGroupedVolume.lean`, `CanonicalBraidLinkingNonUniformityAndMirrorSlopeFlip.lean`, `SymmetryEnergyBarBranchContinuumAndBetaBlindness.lean`) and verified at 50 dps in `computations/probes/fallback_tier_grouped_volume_braid_linking_mirror_slope_symmetry_branch_probe.py` (`computations/probes/fallback-tier-grouped-volume-braid-linking-mirror-slope-symmetry-branch-probe.witness.json`, `allPassed = true`). Opened PR #8321 (`ready: cde173d67efbd687c4f51cce6847a870b6c300f4`).
