---
# qou-tnrz
title: 'Three path sites that need a decision, not a count fix: a dead chi cache, a lowercase-only vendor scraper, and a no-op check-all'
status: todo
type: task
created_at: 2026-08-23T19:24:34Z
updated_at: 2026-08-23T19:24:34Z
---

Three genuinely-wrong path sites found during the qou-rug0 sweep and deliberately
left alone, because each needs a decision rather than a path fix.

## 1. `computations/hecke/hecke_character_symbolic.py:283` — a cache that has been dead since Phase-6

    here = Path(__file__).parent
    here.glob("chi-{atom}-h*.witness.json")

All 50 `chi-*.witness.json` live in flat `computations/`. Phase-6 moved this
module into `computations/hecke/`, so the glob has matched **zero** files ever
since and `_load_chi_witness` silently returns `{}`.

**Why it was not just repointed.** Fixing the path ACTIVATES a dormant symbolic
cache — the module starts using witness data it has not touched in weeks. And the
glob is convention-ambiguous: `chi-deuteron-h*.witness.json` matches five files,
and sorted order picks `chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json` over the
`-at-q0-50dps` one. That is a numeric/convention decision with corpus-wide blast
radius, not a path fix.

## 2. `scripts/sync-qou-mass-vendor.py::required_witnesses` — a lowercase-only scraper

The regex `[a-z0-9][a-z0-9._-]*\.witness\.json` cannot match a capital, so
`sublemma-2-1-A-operator-extract.witness.json` never enters the vendored set. A
silent hole in the sync script's own promise that "a rename upstream should be
loud".

## 3. `tools/qou-substrate/python/qou_substrate/witness.py:2063` — `check-all` checks nothing

    comp_dir = Path(__file__).resolve().parent
    comp_dir.glob("*.witness.json")

The name says `computations/`, but since this was promoted out of
`computations/witness_base.py` it globs the INSTALLED PACKAGE directory, so the
`check-all` CLI reports nothing. The right target differs between an in-repo
checkout and a pip-installed package, so it needs a deliberate choice rather than
a count adjustment.

## Context

These came out of a scan of 5,204 `__file__`-rooted path sites. The rest were
either fixed under qou-rug0 or judged correct with a stated reason. The sweep also
found that `codata_2022_source.MASS_RATIO_P_E` was silently `None` in the shipped
wheel and that `wedderburn_jones_markov`'s y_lambda fast path never fired there —
both from the same fixed-count bug class, both now fixed.
