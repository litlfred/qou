---
# qou-7tr2
title: 'Import-cone staleness backlog: 1799 flags triaged to 7 module questions — one real class'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T16:19:30Z
updated_at: 2026-10-04T15:20:48Z
parent: qou-5vkl
---

Measured 2026-08-30 on `claude/convention-c-migration-tranche-1-2026-08-30`
(436 behind main, so branch-local). Method is `qou-a2q5`'s, applied at the
granularity that bean actually specifies and that I got wrong first: **which
SYMBOL changed, and who imports that symbol** — not merely which module moved.

    witnesses scanned            3,267
    SELF-stale (excluded)          595
    IMPORT-CONE STALE            1,799   <- collapses to SEVEN module questions

## The seven, each read at symbol level

| module | flagged | verdict |
|---|---|---|
| `tools/pyhecke/python/pyhecke/constants.py` | 1470 | **mostly false** |
| `computations/canonical_trm_reference.py` | 137 | **REAL** |
| `computations/substrate/hecke_core_symbolic.py` | 121 | **false** |
| `computations/qbeta/qbeta_utils.py` | 49 | **false** |
| `computations/probes/_gap_a4_qsafe.py` | 17 | **false** |
| `computations/derivation_chain.py` | 4 | **real but sub-44th-digit** |
| `computations/nucleus_real_sdp.py` | 1 | **false** |

**`pyhecke/constants.py` — 1470.** `d2c80cccc9` excised a float64 alpha_EM
CS-tower. Two public symbols: the diff's own comment states
`ALPHA_EM_INV_DERIVED` **is unchanged** (implementation moved to mp with a
back-compat downcast); only `E_HARTREE_EV` moved (`511000.0 * alpha_em**2`, a
rounded electron mass, → `float(e_hartree_ev_mp())`). **12 producers reference
`E_HARTREE`**, not 1470. Direct-reference grep, so 12 is a floor; the ceiling is
nowhere near 1470.

**`canonical_trm_reference.py` — 137. The one real class.** `06788fd463`
replaced a tr_M reference that fifteen files hardcoded as
`mp.mpf("1.0653062286131670…")` — **17 significant figures** — with a 50-dps
witness value. Any comparison against the old literal was capped at ~1e-16
regardless of how exact both sides were. Confirmed on one:
`a-operator-recursive-a3-h9` moved `rel 1.9515091e-16 → 1.0198718e-50`
(bean `qou-p8yw`, refreshed). **The other 136 are the live backlog.**

**`hecke_core_symbolic.py` — 121.** `TR_M_SYM` is the only changed symbol (1
code line + 5 comment lines); exactly one of 11 importers references it
(`shift_from_nf_basis.py`); and that one was re-run *inside* the same commit
(witness `computedAt` 09:19:53, commit 09:21:41). Re-ran to confirm — 4/4, no
non-ephemeral field moved.

**`qbeta_utils.py` — 49.** Three commits, none of which moves a value:
`98f6bfecb1` renames `markov_parameter` → `markov_parameter_convention_C` and
adds a guard that **raises** on withheld `z`/`alpha` rather than returning a
wrong number; `b10782af64` **adds** a symbolic branch that did not previously
exist (the function was mpmath-only); `d552593dbc` fixes that branch's
predicate (`hasattr` → `getattr(..., None)`, because sympy numerics carry an
empty `free_symbols`), routing numerics back to the pre-existing mpmath arm.
Net for any pre-2026-08-30 witness: **identical**. For a genuine `Symbol`: it
previously raised `TypeError`, so no witness can exist.

**`_gap_a4_qsafe.py` — 17.** My own 3-line `sys.path` bootstrap (`cf3bf07ed6`).
Cannot move a number.

**`derivation_chain.py` — 4. The only nuance.** `TR_M_AT_Q0_50DPS["D"]` was
extended from 43 to 60 significant digits, **same prefix**
(`0.5751722439177718708265353439861808891524943…`). So nothing moves above the
43rd digit; at 50-dps serialization only digits 44–50 can. Real, and bounded to
a size no assertion in this corpus tests.

**`nucleus_real_sdp.py` — 1.** Provenance only: `q0_anchor=False` →
`q0_anchor="proton"` plus a reason string. No arithmetic. Notable that the
audit's own `PROVENANCE_ONLY` filter did not catch it.

## What this means for anyone reaching for this backlog

**Do not treat 1,799 as a work queue.** The real population is the 136
un-refreshed `canonical_trm_reference` consumers plus a bounded slice of the 12
`E_HARTREE` producers. Everything else is a module mtime.

## The trap, recorded because I fell into it

`qou-a2q5` says to read the module diff. I did, saw a genuine constant change in
`hecke_core_symbolic.py`, and wrote *"the false-positive argument does not apply
here"* — publishing "121 witnesses this PR has not re-run" on PR #6144. That
conflates **the module changed** with **the changed symbol reaches these
consumers**. The module diff is half the test; the other half is the symbol's
importers. Withdrawn same day.

- **Round 96 (`litlfred/qou#8428`)**: Advanced in `feat/round96-milnororder-signrep-mirrorsplit-multibond-moebius-43c1` (Commit 1 `22d991a251c6bf1bcf86f7ea08f935c2c280b7b3`, Commit 2 `391eb320415cc99c2e005cd0ffab67710cb6bc1d`, probe sha256 `94f6f6be6af6f9daa73f3911e2df79962cba2a56eed95434d4d929e3d5348851`).
