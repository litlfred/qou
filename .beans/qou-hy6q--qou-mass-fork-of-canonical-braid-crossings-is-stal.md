---
# qou-hy6q
title: qou-mass fork of canonical_braid_crossings is stale — no averaged_weighted
status: todo
type: task
priority: normal
created_at: 2026-08-14T19:41:56Z
updated_at: 2026-08-15T00:07:22Z
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
