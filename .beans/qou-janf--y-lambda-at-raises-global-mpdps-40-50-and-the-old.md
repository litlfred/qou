---
# qou-janf
title: y_lambda_at's FIRST call raises global mp.dps 40->50 via a lazy module-scope import (y_lambda_su_n:269, deliberate) — cache-served straddle since RESOLVED
status: todo
type: task
priority: normal
created_at: 2026-08-11T11:09:11Z
updated_at: 2026-08-18T20:48:38Z
---

## Corrected finding (3rd measurement — supersedes the body this bean had)

The 40 → 50 shift is real, but **both my earlier accounts of the cause were
wrong, in opposite directions**, and this one is traced rather than inferred.

### What is actually true

Traced with a watcher on every write to `mp.mp.dps`:

```
first write -> dps=50
    <frozen importlib._bootstrap> _find_and_load_unlocked
    y_lambda_su_n.py:269 <module>
    precision.py:125 set_compute_dps
```

1. **It is a LAZY IMPORT, not the call's arithmetic.** The first
   `y_lambda_at(...)` pulls `y_lambda_su_n`, whose **module scope** runs
   `set_compute_dps(50)`.
2. **It is first-call-only.** Measured: `n=6` first call → 50; `n=6` again →
   stays 40; `n=3` → stays 40. Once-per-process, not per-call.
3. **The `set_compute_dps(50)` is DELIBERATE AND CORRECT — do not remove it.**
   Its own comment says why: it must precede the `mpf()` registry literals or
   `REG_ZC` / `REG_ZD` are parsed at mpmath's default 15 dps, rounded to 53
   bits, and are **already wrong when built**. It names
   `module_const_precision_audit --strict`, which flags exactly those two.
   This is a **fix** for the `qou-j6gb` module-const defect class, not an
   instance of it.

### Correction history — three passes, and read this before trusting any of them

| where | claim | verdict |
|---|---|---|
| commit `40b89a61d` | 40→50 because importing `q_parameter` pulls `set_compute_dps` | **mechanism right, module wrong** — it is module-scope `set_compute_dps` on import, but in `y_lambda_su_n`, not `q_parameter` |
| PR #4975 body | "the effect **does not occur**" | **wrong** — measured `mp.dps` across an import of the *innocent* module |
| this bean, 1st body | "it is the **call**, on the live path — not any import" | **wrong the other way** — it IS an import, a *lazy* one fired by the first call |
| this body | lazy import of `y_lambda_su_n`, module-scope, first-call-only | **traced** (stack above) |

My first bisect missed it because I called `_load_y_lambda_at_q0_witness()`
explicitly as step one, which consumed the one-time effect; every later step
then showed 40 and looked innocent. A once-per-process side effect is invisible
to exactly the probe you would reach for first.

### The cache-served straddle has been RESOLVED at the source

The original body's larger claim — that the cached witness is muon-built and was
being served to proton-anchored callers — **no longer holds**. Measured now:

```
_Y_LAMBDA_AT_Q0_WITNESS_Q0 = 1.1099785827513808   (PROTON pin)
gate hit for Q_MP          = True
```

The witness has since been regenerated at the proton pin, so the gate hits and
serves *experimental*-layer data to an *experimental*-layer caller. No straddle.
The guard fix (gating on the witness's own recorded q₀ rather than
`q_parameter.Q`) plus the re-pinned witness together closed it.

## Landed in this bean

Documentation only — nothing behavioural, because nothing here is broken:

- `wedderburn_jones_markov.y_lambda_at` docstring: the first-call dps side
  effect, its real cause, why the cause must not be removed, and the concrete
  consequence (a producer declaring 40 records `compute_dps: 50`).
- `substrate/_precision` docstring: **importing it does not set `mp.dps`** —
  measured, it stays at mpmath's default 15. Requested twice by the #5023
  sibling; closes their half. Both directions noted together, since they
  present identically ("the number looks fine, at the wrong precision").

## Not done here

**Making `y_lambda_at` restore the caller's dps.** Tempting, but it is a
behavioural change with witness churn: producers that currently finish at 50
would drop to 40 and their recorded values would move. That deserves its own
scoped change, not a drive-by on a documentation bean.

## Item 2 (audit which witnesses were cache-served) — downgraded, with the reason

I called this "the one with reach". It is worth less than I said:

- The straddle it was chasing is **resolved at the source** (above), so the
  ideal-layer-under-experimental-heading hazard is closed going forward.
- `qou-j6gb` has since landed a **gate** for the causally-related defect
  (module-scope `mpf` built before precision is raised, now in
  `precision-gates.sh`'s `GATES` array).
- My proposed tell — "recorded `compute_dps` differs from declared `mp.dps`" —
  returned **74** witnesses on a raw pass. That is high-recall: as this very
  bean shows, a deliberate module-scope raise produces the mismatch with
  nothing wrong. Publishing 74 as a defect count would repeat the error this
  bean is about.
- The #5022 sibling adds a real refinement: `qbeta-c3-phib-saddle-state-integral`
  and `qbeta-c3-qstar-k31-repin` record both anchors in `data` with **no
  top-level `q0Anchor`**, so an anchor-key scan misses them. Any formalised
  audit needs that second tell too.

Honest next step if anyone picks it up: intersect the 74 against `qou-j6gb`'s
coverage and against the top-level-`q0Anchor` scan, and triage the residue by
hand. Do not report the raw count.
