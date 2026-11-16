---
# qou-7zff
title: 'GAP: canonical_tr_m_via_rust REPO_ROOT was off by one — the canonical tr_M was never computed'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T17:53:15Z
updated_at: 2026-11-16T19:29:47Z
parent: qou-trd0
---

## A one-line off-by-one hid the canonical Markov trace entirely

`computations/canonical_tr_m_via_rust.py`:

    HERE      = Path(__file__).parent          # <repo>/computations
    REPO_ROOT = HERE.parent.parent             # -> /home/user   *** WRONG ***

`HERE.parent.parent` is the directory **above** the repository, so every
`BIN_CANDIDATES` entry pointed at `/home/user/tools/hecke-engine/...` instead of
`<repo>/tools/hecke-engine/...`.

**The failure was silent and total.** `find_binary()` always returned `None`;
`compute_tr_m` always short-circuited to
`tr_M_q0_unavail_reason = "hecke-canonical-chi binary not built"` — **even on a
tree where the binary HAD been built.** I built it (`cargo build --release
--bin hecke-canonical-chi`, 39 s, exit 0), confirmed the file on disk, and the
producer still said it was missing. Fixed to `REPO_ROOT = HERE.parent`.

## What it was hiding — a SIXTH value for tr_M(p, q₀)

With the fix and the binary built:

    tr_M(p, q_0) = 1.1457596924573008693524177451617664911309013015621
    tr_M(n, q_0) = 0.98774368811580957144294046174148798302020471873882

**This is the canonical computation** — on the canonical word *with its averaged
crossings* (`sigma: 6, sigma_inv: 3, averaged: 2` for the proton), which is what
`markov_trace_symbolic` and the whole canonical convention mean.

**It matches none of the five values catalogued in `qou-soj6`:**

| value | source | vs canonical 1.145760 |
|---|---|---|
| 1.884319467254976 | option-b full chain | **+64.5 %** |
| 1.88432 | axiomatic content block | +64.5 % |
| 1.6331535640480814 | `TR_M_AT_Q0["p"]` (LIVE) | **+42.6 %** |
| 1.0653062285923893 | assembly-chain derivation | −7.0 % (closest) |
| 2.12258 | deprecated producer docstring | +85.3 % |

And `TR_M_AT_Q0["n"] = 1.2482482717…` against canonical **0.987744** — **+26.4 %**.

## This RETRACTS my verdict in qou-soj6 / PR #6289

I computed `Σ y_λ·χ^λ` on `σ₁⁷σ₂⁴` — **eleven all-positive crossings** — and
called the option-b value canonical because it agreed to 5.17e-16. That
agreement means option-b was computed **on the same all-positive word I used**,
not that either is canonical. The canonical word has three inverse and two
averaged crossings.

**And it inverts the action I was about to take.** I proposed "correct
`TR_M_AT_Q0["p"]` to 1.884319…". That would have moved it **further** from the
canonical value — 42.6 % off becomes 64.5 % off.

## Scope — what is NOT claimed

That 1.145760 should be written into `TR_M_AT_Q0`. Six values now exist and only
this one is reproducible from the canonical engine on the canonical word, but
**every one of the five has consumers**, and the two that are live feed the
neutron assembly chain and the phase-5 proton diagnostic. Reconciling them is a
real tranche with real number movement, not a constant edit.

What this bean fixes is only the bug that made the canonical value unobtainable.


## A SEVENTH value, and it is the canonical cache — measured 2026-09-06

`tr_M(p, q₀)` now has a seventh claimant, and unlike the five in the census it
is the value the **canonical chi cache actually holds today**:

    0.62932840220292191816534574677848592760021940063436   (proton)
    0.47513351715568221250609023267500579955840763470875   (neutron)

`computations/chi-{proton,neutron}-h3-at-q0-50dps.witness.json`, producer
`chi_at_q0_via_hoefsmit_mpfr.py`, `computedAt` 2026-09-06T03:15:55.

### Where it came from — the intra-ordering ruling, not a new route

The sixth value this bean records — `1.14575969245730086935…` from
`hecke-canonical-chi`, once the `REPO_ROOT` path bug was fixed — **was** the
cache value as recently as 2026-08-29. `atom_braid_word_3A`'s per-nucleon
confinement core then changed from GROUPED to alternating on the 2026-09-05
owner ruling (bean `qou-hu1f`) and the caches were regenerated under the
follow-up ruling (`qou-92u9`). Measured cache-before against cache-after:

| | 2026-08-29 | 2026-09-06 | before / after |
|---|---|---|---|
| proton | 1.14575969245730086968… | 0.62932840220292191817… | **1.82060** |
| neutron | 0.98774368811580957163… | 0.47513351715568221251… | **2.07887** |

Those are the single-nucleon analogues of the `R_quark` factors recorded for the
bound atoms (²H 3.785, ³H 7.868, ³He 6.891, ⁴He 14.325).

### 🛑 A figure I reported in chat and am correcting here

I first reported the move as **1.6928× (proton) / 1.9431× (neutron)**. Those are
wrong. They are `documented / regenerated` — I divided the new cache value by the
`1.0653` / `0.9232` figures from a failing assertion's `expected` field, which
were **never the cache value**. The regeneration move is the table above.

### The failure that surfaced this was ALREADY RED — do not "fix" it

`gap_a4_T2_per_knot_vol_probe_perknot_rerun.py` asserts
`proton_chi_cache_tr_M_matches_documented` against `1.0653062380758782`, and
`neutron…` against `0.9232333051498377`. Both fail today. **Both failed before
the regeneration too**, at the 2026-08-29 values — verified with
`git show 3cc4b2aab1~1:<witness>`. The regeneration widened the gap; it did not
open it.

So the assertion is **reporting the truth** and should stay red. Updating
`expected` to `0.62932840…` would pin it to a value whose relationship to the
other six is exactly what this bean says is unestablished — the laundering
AGENTS.md §"Axiomatization is NOT a Proof" forbids, one level down.

### 🛑 And there is NO drain here — a measurement that would have been misread

A line-level grep over tracked source and content (excluding `.beans/`,
`_deprecated/` and `.work/`) finds `1.0653` on a trace-naming line in **85
files** and `0.9232` in **38**, overwhelmingly `docs/audits/`. That is **not** a
blast radius of stale values:

- `1.0653062285923893` is claimant **#4** in this bean's own census and has
  carried status **UNEXPLAINED** since 2026-08-30 — it was not made stale by
  anything I did.
- The canonical cache has not matched it since at least 2026-08-29.
- Note the census spells it `…62285923893` while the live assertion expects
  `…62380758782`. **Even the "1.0653" family has two spellings**, differing at
  the 8th significant digit — consistent with this bean's own warning.

An agent reading "85 files carry a superseded value" would sweep them onto
`0.62932840…`, which would replace one unexplained number with another and
destroy the record of the disagreement. Recorded so that does not happen.

### What would actually settle it

Not a sweep. The open question is unchanged and is this bean's subject: **which
of the seven is `tr_M(p, q₀)`, and by what derivation.** The seventh at least
has a named, reproducible producer and a dated owner ruling behind its braid
word, which none of claimants #3–#5 do — but "has a provenance" is not "is
canonical", and this note does not claim it is.

## Progress Update (Round 49 — PR #8170)

- Added `--self-test` to `computations/canonical_tr_m_via_rust.py` locking in `REPO_ROOT == HERE.parent`, `(REPO_ROOT / 'tools' / 'hecke-engine' / 'Cargo.toml').is_file()`, and `canonical_word_for(1, 0)` / `canonical_word_for(1, 1)` wire-format encoding.
- PR: https://github.com/litlfred/qou/pull/8170 (`8b83507c7e14547848b5b991bdd3396fc7f3a703`)
