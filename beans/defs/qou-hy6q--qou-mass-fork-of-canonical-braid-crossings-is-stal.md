---
# qou-hy6q
title: qou-mass fork of canonical_braid_crossings is stale — no averaged_weighted
status: completed
type: task
priority: normal
created_at: 2026-08-14T19:41:56Z
updated_at: 2026-08-15T00:37:10Z
parent: qou-1295
---

Confirmed against current main: qou-mass/src/qou_mass/_internal/canonical_braid_crossings.py is ~95 lines behind computations/ -- no _avg_color_delta, no averaged_weighted, no CTYPES, no d_for_ctype delta= kwarg. Its siblings hoefsmit_symbolic / markov_weights_symbolic / isotope_record_schema carry the same stale {sigma, sigma_inv, averaged} vocabulary. Not touched in PR #5029: qou-mass is a published PyPI facade and a version bump is a release decision, not a sweep. Scope when picked up: decide fork-vs-vendor first.



## RE-SCOPED 2026-08-15 after actually reading the package — the defect is in the DATA, not the code

My earlier note said the vendored module is '~95 lines behind' and framed this as a code-staleness / fork-vs-vendor decision. Both halves were wrong, in opposite directions.

### The vendored CODE is unreachable, so its staleness costs nothing today

qou-mass/src/qou_mass/_internal/canonical_braid_crossings.py is 95 lines vs 251 in computations/ — not a drifted copy but an EARLIER GENERATION. It predates classify_crossing entirely: grep counts are 0 for classify_crossing, d_for_ctype, sign_for_ctype, CTYPES, averaged_weighted, _avg_color_delta. It carries an inline {0, -h, -h/2} classifier with a raise on anything else, i.e. exactly the narrow vocabulary the whole qou-gdtb/qou-8zjd arc removed.

But it CANNOT RUN. Its body does `from mass_at_3A_proper import atom_braid_word_3A` and `from hecke_core import h`, and NEITHER is vendored — the _internal dir has 16 files and no mass_at_3A_proper.py, no hecke_core.py. Any call raises ImportError before reaching the classifier. api.canonical_braid() does not call it; it reads a bundled witness and falls back to empty generators, with the live path documented as 'P3 work (vendoring the canonical_braid_crossings transitive dependency chain)' and test_canonical_braid_4he pytest.mark.skip for the same reason.

So: no user of the published package can reach the stale classifier. Refreshing that file is cosmetic.

### The shipped DATA carries the pre-split vocabulary, and that IS the public API's answer

qou-mass/src/qou_mass/data/canonical-mass-table-extended.witness.json is what api.canonical_braid() actually returns, via BraidWord.crossing_types. Its 8 rows were generated before the label split, so every multi-nucleon row collapses the colour-weighted p-n interface into 'averaged':

    atom  shipped avg  true avg  true avgW  status
    p               2         2          0  ok
    n               2         2          0  ok
    2H              5         4          1  COLLAPSED
    3H              7         6          1  COLLAPSED
    3He             7         6          1  COLLAPSED
    4He             9         8          1  COLLAPSED
    5Li            11        10          1  COLLAPSED
    6Li            13        12          1  COLLAPSED

2H's 'averaged: 5' is the SAME wrong number as the build_atomic_braid_recipe_d_chain literal fixed on PR #5029, in a second medium. p and n are correct for the usual reason: no p-n bond.

### What this changes about the disposition

The fork-vs-vendor question is real but it is NOT what gates this, and it is not urgent: the code path it governs is dead. What is live is that an external researcher calling qou_mass.canonical_braid(2, 2) is told the 4He word has 9 averaged crossings and no colour-weighted interface. Regenerating the bundled shard against the current classifier is a data refresh plus a version bump — smaller than a vendoring decision, and it is the part with a user on the other end.

Still an owner call because it is a published-package release, not because the choice is hard.



## CLOSED 2026-08-15 — shard regenerated, v1.0.0, and the shard was hiding a bigger change than the labels

Owner picks: regenerate 8 rows properly / 1.0.0 / full vendor.

The shard's row set (p, n, D, T, 3He, 4He, 5Li, 6Li) is reproducible with '--method auto --atoms ...', once auto can route A<2 without Rust. It could not: laurent_q_rust raised ImportError on the missing pyhecke_native with no fallback. Added a narrow fallback to the sympy laurent_q path in auto ONLY, recording the substitution in method_used. This does not reopen the PR #886 decision, which declined a chain out of Case C -- a MATHEMATICAL condition. A missing extension is an environment capability. p and n agree exactly between markov_peel and laurent_q.

THE ACTUAL FINDING: the shard was not merely label-stale. It was a 2026-05-19 CONVENTION C artifact, and the corpus moved to convention D in #4928. Every tr_M value moves:

  p    1.0653 -> 1.1458  (+7.6%)      4He  0.05535 -> 0.16097  (+191%)
  n    0.9232 -> 0.9877  (+7.0%)      5Li  0.02944 -> 0.11300  (+284%)
  2H   0.3883 -> 0.5751  (+48%)       6Li  0.00789 -> 0.04505  (+471%)
  3H   0.1041 -> 0.2293  (+120%)
  3He  0.2065 -> 0.4038  (+95%)

Nucleon predictions move only ~0.25 ppm (938.2718526 -> 938.2720894 MeV), the convention being largely absorbed downstream. So the MAJOR bump is right for a reason beyond the policy's letter: recorded tr_M values from 0.1.0a1 are a different object, not a less precise one.

BUG FOUND AND FIXED WHILE HERE: predict() raised TypeError for EVERY atom in 0.1.0a1 -- 'Decimal * float' at api.py:210, because the witness loads with parse_float=Decimal. The package's headline function was dead on arrival. Fixed with Decimal(10_000), preserving exactness. 5 of 8 test failures were this, and they fail identically on the OLD shard, so it is pre-existing and unrelated to the data change.

Tests: 19 passed, 1 skipped (the P3 vendoring skip). Two hardcoded convention-C tr_M expectations updated with a note not to widen tolerances -- C and D are different traces, not different precisions. test_version_string pinned the alpha SERIES ('0.'), so it had to fail on leaving alpha; now asserts the version SHAPE and additionally cross-checks pyproject.toml against __version__, which nothing did before -- pyproject carries a STATIC version while _version.py claims to be the single source of truth.

REMAINING: the vendored _internal modules are still stale. That is qou-elb0, and the drift measurement there (14 of 14 modules drifted) is the reason it needs a sync script rather than 22 more hand copies.
