---
# qou-7zff
title: 'GAP: canonical_tr_m_via_rust REPO_ROOT was off by one — the canonical tr_M was never computed'
status: todo
type: task
priority: normal
created_at: 2026-08-30T17:53:15Z
updated_at: 2026-08-30T17:54:12Z
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
