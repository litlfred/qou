---
# qou-a0j7
title: 'qou-mass vendored _internal has no sync tooling: 15 hand-copied files, canonical_braid_crossings confirmed stale'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T14:18:01Z
updated_at: 2026-10-04T15:23:05Z
parent: qou-5vkl
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

This is the seventh instance of *a private copy cannot learn what the
canonical one learns*, and the only one that ships to PyPI.

*(Revised 2026-08-15.)* This paragraph originally read "the published package
raises on any word carrying a p-n interface — deuteron and up — the same way
`canonical_tr_m_via_rust` did before `qou-8zjd`". Both halves were wrong: it
raises on **every** input, proton included, and for an unrelated reason
(`ModuleNotFoundError`, missing vendored deps — see the correction below), not
because of the narrow vocabulary. The stale vocabulary is real but currently
unreachable.

## Why it was not fixed alongside qou-8zjd

Not a copy job, and the decision is not the agent's to make.

**Missing dependencies.** The fixed module needs `flavor_split_leading`
(`_li_2_q_util`) for δ and `atom_braid_word_3A` (`mass_at_3A_proper`) for the
triples. Neither is vendored, nor is `hecke_core` or `_path_bridge`:

    _li_2_q_util.py      : False
    mass_at_3A_proper.py : False
    hecke_core.py        : False
    _path_bridge.py      : False

**~~It changes published numbers.~~** ⚠ **RETRACTED — see the 2026-08-15
correction below.** This paragraph originally asserted, in the present tense,
that syncing "makes `qou-mass` compute the colour-weighted p-n interface
`-h(1/2 - δ/4)` where today it computes the colour-blind `-h/2` — a 6.88e-4
shift ... for every `Z >= 1, N >= 1` nuclide."

It computes neither. The vendored path raises `ModuleNotFoundError` on every
input, so there is no current output for a sync to shift. The 6.88e-4 figure
would apply only **conditionally** — *if* the vendor were completed (P3) and
the path became runnable *and* the classifier were left stale. As a statement
about today's package it is simply false.

## The decision needed

1. **Does `qou-mass` ship the colour-weighted convention?** If yes, vendor
   the four missing deps and sync. If no, the package should *say* it is
   colour-blind rather than raise. Note this is conditional on P3 landing
   first: until the path is runnable at all, neither answer changes any
   number the package currently reports, because it reports none.
2. **What replaces hand-copying?** A sync script with a drift check in CI, or
   a real dependency on `qou-substrate` / `pyhecke` instead of a snapshot.
   Whichever — 15 files with no provenance will drift again, and the next
   drift will be found the same way this one was: by accident.

Until then the package is alpha (`v0.1.0a1`) with one in-repo importer, so
the blast radius is small — but the staleness is real and is now recorded
rather than latent.

## CORRECTION (2026-08-15): there is no output to change — it cannot run

I twice described this as an owner decision because "syncing would change what
the published facade reports by 6.88e-4 for every `Z >= 1, N >= 1` nuclide."
**That was wrong.** Measured:

    import qou_mass                                    -> OK
    vendored atom_canonical_crossings(1,1)  [deuteron] -> ModuleNotFoundError: mass_at_3A_proper
    vendored atom_canonical_crossings(1,0)  [proton]   -> ModuleNotFoundError: mass_at_3A_proper

It fails for **every** input, proton included — not just the words carrying a
p-n interface. There is no 6.88e-4 shift to weigh because there is no output.
The stale classifier inside it is unreachable.

The package already knows this. `api.py` says so in two places:

    line 319:  "path which is P3 work (vendoring the canonical_braid_crossings
                ...)"
    line 342:  "Live computation via canonical_braid_crossings has deep deps"

So the vendored `canonical_braid_crossings.py` is a **partial, aspirational
vendor for a path the package documents as unfinished**, not a live component
serving wrong numbers. `mass_at_3A_proper` is not vendored, and neither is
`_li_2_q_util` (which the fixed classifier needs for δ), so a straight sync is
not possible either — it would import two more absent modules.

### Revised disposition

Not "sync it and change the numbers", and not an owner call on output. The
real options are:

1. **Leave it, documented** — it is dead code behind a documented-as-P3 path.
   Cheapest, and honest, provided the staleness is recorded where the next
   person doing P3 will see it.
2. **Finish the vendor** — pull in `mass_at_3A_proper` + `_li_2_q_util` +
   their transitive deps, then sync. That is the P3 work itself, not a fix
   to it.
3. **Delete the partial vendor** — remove a file nothing can call, so P3
   starts from the canonical source rather than a stale snapshot.

The systemic finding in the original entry **stands**: 15 hand-copied files
with no sync tooling and no provenance. That is still real and still wants
addressing. What changes is the urgency and the framing of this one file —
it is not shipping wrong physics, it is unreachable.

**Lesson for my own reporting:** I asserted a specific numerical consequence
(6.88e-4, every mixed nuclide) for a code path I had never executed. The
grep showed a stale classifier and I inferred the rest. One import would have
corrected it, and I escalated to the owner twice instead.

In-progress in Round 98 PR litlfred/qou#8442.
