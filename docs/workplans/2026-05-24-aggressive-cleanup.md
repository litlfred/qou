# Aggressive cleanup workplan — cut non-canonical probes + thimble + negatives

**Date:** 2026-05-24
**Branch:** `claude/aggressive-cleanup-2026-05-24`
**Owner direction:** "remove all from compute infrastructure in the paper.
we don't need these non canonical probes littering paper and compute.
aggressive audit on what we can cut. paper is way too long and
disorganized with these empirical fittings, probes, numerology.
also we don't need any of the negative findings that are internal
to the paper. the only reason to keep in negative finding is if it
is a negative finding about an external conjecture from another paper"

## Scope summary

| Category | Compute | Paper | Est |
|----------|--------:|------:|-----|
| Thimble/PL/SW (CI + blocks) | 29 scripts | 64 blocks | Batch 1 |
| CI pipeline cleanup | 6 steps | — | Batch 1 |
| Probes (`probe_*`) | 158 scripts, 66 witnesses | 63 blocks | Batch 2 |
| DEPRECATED/SUPERSEDED | 63 scripts | — | Batch 2 |
| Internal negative findings | — | ~114 blocks | Batch 3 |
| Empirical fits/numerology | — | ~93 blocks | Batch 3 |
| Spike/explore | 5 scripts | — | Batch 2 |

## Batch 1: Thimble + CI (highest impact — fixes CI)

- [ ] **1a.** Remove 6 thimble steps from `witness-pipeline.yml`
  - `picard_lefschetz_thimble`
  - `mobius_limit_from_thimble`
  - `baryon_product_from_alt`
  - `sw_period_thimble_equivalence`
  - `residue_algebraic_verification`
  - `jet_gb_pl_correspondence`
- [ ] **1b.** Move 29 thimble-dependent `.py` scripts to `_deprecated/`
- [ ] **1c.** Remove 64 thimble/PL/SW content blocks from paper
  - Remove `.ts` + `.md` triples
  - Update chapter manifests to drop references
  - Keep `.lean` siblings if they have non-thimble value
- [ ] **1d.** Remove thimble drift exclusions from `witness-pipeline.yml`
  (no longer needed once the steps are gone)
- [ ] **1e.** Run `bun run validate` — fix broken cross-refs
- [ ] **1f.** Commit, push, PR

## Batch 2: Probes + deprecated scripts

- [ ] **2a.** Move 158 `probe_*.py` scripts to `_deprecated/probes/`
- [ ] **2b.** Move 66 `probe-*.witness.json` to `_deprecated/probes/`
- [ ] **2c.** Move 63 DEPRECATED/SUPERSEDED scripts to `_deprecated/`
- [ ] **2d.** Move 5 `spike_*` / `explore_*` scripts to `_deprecated/`
- [ ] **2e.** Remove 63 content blocks wired to probes
  - Update chapter manifests
  - Fix broken `uses[]` references
- [ ] **2f.** Run audits — fix any regressions
- [ ] **2g.** Commit, push, PR

## Batch 3: Internal negatives + empirical fits (paper content)

- [ ] **3a.** Audit 114 blocks with negative-finding language
  - KEEP if the negative is about an external conjecture
  - REMOVE if the negative is about an internal failed attempt
- [ ] **3b.** Audit 93 blocks with empirical/numerical/probe language
  - KEEP if it's a proved result with empirical verification
  - REMOVE if it's an empirical fit / numerology / coincidence
- [ ] **3c.** Review chapter structure post-removal
  - Re-flow section intros
  - Update chapter manifests
  - Fix dangling `uses[]` / `interprets`
- [ ] **3d.** One-voice sweep on surviving blocks
- [ ] **3e.** Commit, push, PR

## Batch 4: Verification + dashboard refresh

- [ ] **4a.** `bun run validate` clean
- [ ] **4b.** Refresh per-observable-100x-status dashboard
- [ ] **4c.** Refresh canonical-derivation-cheat-sheet
- [ ] **4d.** CI green (the actual test — thimble steps gone)
- [ ] **4e.** Final PR + merge

## Rules

- **Move, don't delete.** Scripts go to `_deprecated/` (gitignored
  or separate directory). Git history preserves everything.
- **Keep external-conjecture negatives.** E.g. "Bożejko-Speicher
  does not apply at q > 1" stays because it's about an external
  paper's claim.
- **Remove internal negatives.** E.g. "Bring-Bloch PSLQ negative"
  goes because it's about our own conjecture's failed search.
- **Keep proved results.** Family A, flavor split, Borromean κ=3/16
  are PROVED — they stay regardless of how they were discovered.
- **No empirical fits in production.** Any `= CODATA` (not `≈`)
  without a derivation chain goes.
