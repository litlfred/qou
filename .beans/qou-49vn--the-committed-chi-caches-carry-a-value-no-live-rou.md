---
# qou-49vn
title: 'The committed chi caches carry a value no live route reproduces: cached 0.5751722439 vs --fresh AND markov-peel 0.1519683392'
status: todo
type: task
priority: normal
created_at: 2026-09-05T19:13:20Z
updated_at: 2026-09-05T19:14:14Z
---


Found 2026-09-05 while re-verifying a claim I had **asserted without measuring**
in PR #6861 — *"re-running the chi producer today reproduces them"*. It does
not, and the discrepancy is a factor of 3.78.

## The measurement

Same container, same commit (`main` at `14c798b93c` + 2), same `mpmath 1.3.0`.
`computations/chi_at_q0_via_hoefsmit_mpfr.py deuteron`, differing **only** by
the `--fresh` flag:

| run | `tr_M_at_q0` |
|---|---|
| cached (resume: 11 partitions already cached) | `0.57517224391777187082653534398618088915249435289286` |
| `--fresh` | `0.15196833920423160759266569775106614127124096465527` |

The cached run reproduces the **committed** witness value to all 50 digits.

Independent corroboration, same day, different script —
`QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py --anchor
proton`:

    [peel]  tr_M(q_0) = 0.15196833920423160759266569775106614127124096465526   (deuteron)
    |bridge - peel|   = 1.15e-51

So the **markov-peel** and the **Hoefsmit+Wenzl bridge** agree with each other
at 1e-51 and with `--fresh` chi to **49 of 50 digits**. Three routes today give
`0.1519683392…`; the cache alone gives `0.5751722439…`.

The `--fresh` help text describes this exact failure: *"Use when a cache may
already have been stamped with the CURRENT q0 while holding values computed at
a different one — the resume check compares stored-vs-current q0, so it cannot
see that."*

## What moved, and what did not

Comparing the fresh witness against the committed one per partition: the
`y_lambda` are **unchanged**; **9 of 11 `chi_lambda` differ substantially**,
with sign flips — e.g. `λ=(5,1)`: `3.2163173422…` → `-0.6822850128…`. So this
is a **χ** change, the mirror of the 2026-08-10 move analysed in `qou-brkp`,
which was a **y** change.

The committed chi witness is also **self-stale**: `scriptHash c36a8a393fcd`
predates two producer fixes —

  * `41f517bf17` (2026-08-23) *"fix(qou-8chw): my own unblock turned a crash
    into silent cache poisoning — guarded"*
  * `d151898dd6` (2026-08-30) *"fix(L1): pin-specific numerical chi caches —
    5/6 atoms certified 1 ppQ (T + ³He recovered)"*

Both are about exactly this cache. `d151898dd6` is the leading candidate and is
**not** confirmed here.

## Scope: all three atoms, and the arbiter itself

The arbiter's committed witness (`atomic-tr-m-mpfr-50dps-proton.witness.json`,
computed **2026-08-19**) disagrees with a re-run today on **every** atom:

| atom | committed 2026-08-19 | today |
|---|---|---|
| proton  | `1.14575969245730086968…` | `0.62932840220292191816…` |
| neutron | `0.98774368811580957163…` | `0.47513351715568221250…` |
| deuteron | (chi cache) `0.5751722439…` | `0.15196833920423160759…` |
| tritium | (chi cache) `0.2293101021…` | `0.02914404236097206535…` |
| ³He | (chi cache) `0.4037670368…` | `0.05859625365443638021…` |

## 🛑 TWO CONFOUNDS — this does NOT establish which value is correct

1. **The Rust kernel was unavailable in today's run** — the arbiter printed
   `[rust] hecke-canonical-chi unavailable; falling back to Hoefsmit+Wenzl
   bridge`. The committed run may have used `canonical-rust`. The fallback is
   the documented graceful one, but it means today's "two routes" are closer
   kin than they look.
2. **The arbiter's own source drifted**: `scriptHash 7c63fadfb8d0 →
   db23b7ba36cb`.

The deuteron result survives both confounds, because `--fresh` chi is a
*different script* that also gives `0.1519683392…`. The proton/neutron rows do
not, and are recorded as observations, not verdicts.

**Nothing here says `0.152…` is right and `0.575…` wrong.** What it says is
that **no live route reproduces `0.575…` except the cache**, and that the cache
is the thing two producer fixes were written to distrust.

## What this retracts

`qou-brkp` item 1 was closed earlier today as *"answered — four routes, one
number (`0.5751722439…`)"*, on the strength of `qou-r9dv` / `aeb31dfb41`
(2026-08-23), which reports three independent methods agreeing exactly. **That
closure is retracted.** `aeb31dfb41` predates `d151898dd6` (2026-08-30), and
the arbiter it names now gives a different number. I closed a question on a
**baseline** instead of a fresh measurement — the precise trap this repo's own
agent-memory doctrine names (*"a BASELINE tells you what to measure, never the
current answer"*), in the same session in which I wrote that entry.

## Next, in order

1. **Build `hecke-canonical-chi` / restore the Rust kernel** and re-run the
   arbiter, to remove confound 1. Until then no verdict.
2. `git diff c36a8a393fcd..HEAD -- computations/chi_at_q0_via_hoefsmit_mpfr.py`
   and read `d151898dd6` — it claims a 1 ppQ certification for 5/6 atoms and
   may already contain the answer.
3. If `0.152…` is right, the blast radius is wide: `option_e_multi_isotope_
   delta_lambda_probe_v3` and every other reader of `chi-*-at-q0-50dps.witness
   .json` carries the superseded value, and `qou-r9dv`'s three-method
   certification needs re-running.
4. **Do not mass-regenerate.** One atom, with the Rust kernel present, decided
   first.
