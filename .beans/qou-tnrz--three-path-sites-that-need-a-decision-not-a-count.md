---
# qou-tnrz
title: 'Three path sites that need a decision, not a count fix: a dead chi cache, a lowercase-only vendor scraper, and a no-op check-all'
status: completed
type: task
priority: normal
created_at: 2026-08-23T19:24:34Z
updated_at: 2026-08-23T22:16:04Z
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


---

## RESOLVED — all three decided and landed (93e24e23d)

**1. The dead chi cache — REMOVED, not repaired (option A).**
`_load_chi_witness` in `hecke/hecke_character_symbolic.py` globbed
`Path(__file__).parent` for `chi-*.witness.json`. After the Phase-6 refactor
moved the file into `hecke/`, that directory holds no chi witnesses, so the
cache had been missing on every call — silently, since a miss just means
recompute. Repairing the path would have switched on a cache nobody had
exercised in months and changed what the producers compute; removing it
preserves the behaviour everything has actually been running.

Removed: `_load_chi_witness`, `_CHI_WITNESS_STRINGS`, the call site, and the
now-unused `atom_cache_label` parameter of `q_character_on_braid_word` —
signature is now `q_character_on_braid_word(shape, braid_crossings, q)` — plus
the `chi_cache_label` lookup and keyword in
`habiro/habiro_coefficients_atomic.py`. A comment at
`hecke_character_symbolic.py:275` records what was there and why it went.

**2. The lowercase-only vendor scraper — FIXED.**
`scripts/sync-qou-mass-vendor.py:217` matched witness filenames with
`[a-z0-9][a-z0-9._-]*`. On any name containing a capital the class matched a
TRUNCATED FRAGMENT after it rather than failing outright, so the scraper
recorded a name that resolves to nothing. Widened to
`[A-Za-z0-9][A-Za-z0-9._-]*`. The failure mode is the dangerous kind: not an
error, a wrong answer that looks like an answer.

**3. The no-op `check-all` — FIXED.**
`witness.py`'s `check-all` used `Path(__file__).parent` to find
`computations/`. The CLI was promoted out of `computations/witness_base.py`
into the installed package, and the path followed it, so `check-all` had been
globbing the package directory and reporting **0 witnesses** — a staleness
checker returning "nothing to report" because it was looking in an empty
place. Now searches upward for a real `computations/` tree and falls back to
the module directory only when there is no repo around it (the one case where
globbing beside the module is right). Scans **2717** witnesses;
`_deprecated/` excluded, matching every other consumer.

Each of the three is the same shape: a path that stopped being right when a
file moved, failing quietly rather than loudly. None was a count to fix.
