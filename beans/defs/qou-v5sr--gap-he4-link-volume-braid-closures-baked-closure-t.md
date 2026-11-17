---
# qou-v5sr
title: 'GAP: he4_link_volume_braid_closure''s baked CLOSURE table is stale for the NUCLEON rows, and its own comment is now false'
status: in-progress
pr: 8350
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T16:32:52Z
updated_at: 2026-10-04T15:20:05Z
parent: qou-5vkl
---

Found as a by-product of answering the carrier question for `qou-o6ml`
(bean `qou-mbbf`, PR #7322), while checking whether the arc's closing
measurement is stale. NOT caused by that branch.

## What is stale

`computations/he4_link_volume_braid_closure.py` carries a baked `CLOSURE` dict
(lines 62-69) transcribing a live run, plus a comment reading

    Every mode (avg -> +sigma / -sigma / drop) gives the same non-geometric
    outcome; +sigma tabulated.

Measured 2026-09-13 with `snappy 3.3.2` / `spherogram 2.4.1` (both `pip install`
cleanly), calibrated against `Vol(4_1) = 2.0298832128`:

| case | baked | live `borromean`, +sigma / -sigma / drop |
|---|---|---|
| proton | `geometric False, vol 0.0` | **True**, 9.966512 / 11.942872 / 10.215606 |
| neutron | `geometric False, vol 0.0` | **True**, 16.191143 / 8.195703 / 11.942872 |
| 3H | `False, 0.0` | False, 0.0 (all 3) — **unchanged** |
| 3He | `False, 0.0` | False, 0.0 (all 3) — **unchanged** |
| 4He | `False, 0.0` | False, 0.0 (all 3) — **unchanged** |

So only the two NUCLEON rows moved, and the quoted comment is now **false for
them** — it holds under `"grouped"`, the word it was measured on, and fails
under `"borromean"` in all three modes.

## Root cause, established rather than guessed

`atom_canonical_crossings` forwards `intra_order` to
`mass_at_3A_proper.atom_braid_word_3A`, whose default became `"borromean"` in
`7db032fb48` (2026-09-05) — each nucleon's confinement core became the
alternating `(s0 s1^-1)^3`. Re-running with `intra_order="grouped"` reproduces
the baked table exactly, all five rows, all three modes. That is the
discriminator: the table is not wrong-as-written, it is **stale**, and by the
same commit as `qou-sikd`'s 45 %/52 % trace move.

## 🛑 DO NOT read 9.966512 as the proton's volume

It varies by up to **2x** across the averaging mode (9.966512 / 11.942872 /
10.215606), and that mode is an unresolved *rendering* convention — how an
`"averaged"` crossing becomes a braid letter — not a categorical input. A
quantity that moves 2x under a convention nobody has fixed is not derived, and
picking the mode whose number one prefers is exactly the selection-against-the-
target the anti-fit rule forbids. **What is established is the qualitative flip**
(non-geometric -> geometric), which IS mode-independent. The magnitude is not.

## NOT FIXED, deliberately

Correcting the table means either re-running with `--live` and re-committing the
witness, or hand-editing the baked dict. Both are changes to a producer's
recorded output under AGENTS.md "ASK THE OWNER BEFORE CHANGING THINGS"
(2026-09-07), and neither exemption applies: it does not increase precision, and
which word is canonical for THIS producer's purpose is not settled by any single
corpus artifact — the same open question `qou-sikd` raises for the tr_M
consumers. Same commit, same decision, and they should be decided together.

Note the baked table is `CLOSURE`, consulted when `--live` is absent, i.e. the
default path. Anyone reading proton/neutron geometricity off this producer
without `--live` gets the pre-2026-09-05 answer with no signal.

## Reproduce

    pip install snappy spherogram
    PYTHONPATH=computations python3 -u computations/probes/atom_closure_geometry_probe.py

5/5; skips cleanly with a message when SnapPy is absent, since a bare container
is the default here.

Cross-links: `qou-mbbf` (the A+1 component law and the carrier question),
`qou-sikd` (the same commit, on the trace side), `qou-o6ml` (the arc).


## Round 57 Implementation (PR #8350)
- Implemented on branch `claude/round57-trd0-9nnz-fixes` (commit `35175f892e4827e826a23a3d007073dd800ff733`, https://github.com/litlfred/qou/pull/8350).
