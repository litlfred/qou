---
# qou-a0j7
title: 'qou-mass vendored _internal has no sync tooling: 15 hand-copied files, canonical_braid_crossings confirmed stale'
status: todo
type: task
priority: normal
---

## The finding

`qou-mass/src/qou_mass/_internal/` holds **15 hand-copied files** from
`computations/`. There is no sync script, no drift check, and no recorded
provenance for any of them. It is a snapshot that nothing keeps current.

One of them is confirmed stale. `canonical_braid_crossings.py` is the
**pre-fix** file verbatim — the narrow `{0, -h, -h/2}` vocabulary, no
`classify_crossing`, no `d_for_ctype`:

    vendored has classify_crossing   : False
    vendored has d_for_ctype         : False
    vendored has averaged_weighted   : False
    vendored has sign_for_ctype      : False
    vendored has CTYPES              : False

So the published package raises on any word carrying a p-n interface —
deuteron and up — the same way `canonical_tr_m_via_rust` did before
`qou-8zjd`. This is the seventh instance of *a private copy cannot learn
what the canonical one learns*, and the only one that ships to PyPI.

## Why it was not fixed alongside qou-8zjd

Not a copy job, and the decision is not the agent's to make.

**Missing dependencies.** The fixed module needs `flavor_split_leading`
(`_li_2_q_util`) for δ and `atom_braid_word_3A` (`mass_at_3A_proper`) for the
triples. Neither is vendored, nor is `hecke_core` or `_path_bridge`:

    _li_2_q_util.py      : False
    mass_at_3A_proper.py : False
    hecke_core.py        : False
    _path_bridge.py      : False

**It changes published numbers.** Syncing makes `qou-mass` compute the
colour-weighted p-n interface `-h(1/2 - δ/4)` where today it computes the
colour-blind `-h/2` — a 6.88e-4 shift on the interface crossing, for every
`Z >= 1, N >= 1` nuclide. That is a deliberate change to what an
external-researcher facade reports, not a bug fix to be slipped in.

## The decision needed

1. **Does `qou-mass` ship the colour-weighted convention?** If yes, vendor
   the four missing deps and sync. If no, the package should *say* it is
   colour-blind rather than raise.
2. **What replaces hand-copying?** A sync script with a drift check in CI, or
   a real dependency on `qou-substrate` / `pyhecke` instead of a snapshot.
   Whichever — 15 files with no provenance will drift again, and the next
   drift will be found the same way this one was: by accident.

Until then the package is alpha (`v0.1.0a1`) with one in-repo importer, so
the blast radius is small — but the staleness is real and is now recorded
rather than latent.
