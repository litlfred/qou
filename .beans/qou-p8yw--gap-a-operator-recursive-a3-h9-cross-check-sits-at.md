---
# qou-p8yw
title: 'GAP: a-operator-recursive-a3-h9 cross-check sits at the float64 floor in the committed witness but at 50 dps on a fresh run'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:43:04Z
updated_at: 2026-08-30T14:43:37Z
---

Found 2026-08-30 while draining the `qou-cds2` producer-importability backlog.
**Not attributed, deliberately not committed** — the fresh values were restored,
not swept into an unrelated commit.

## What moved

`computations/a_operator/a-operator-recursive-a3-h9.witness.json` is a SIBLING
witness: it was rewritten as a side effect of running
`computations/probes/eigenbasis_structural_lemmas_probe.py` /
`chi_content_eigenbasis_probe.py` after fixing their bootstrap order. Its own
`scriptFile` is `a_operator_recursive_a3_crosscheck.py`.

Two assertion `source` strings moved, both on the ³H (triton) row:

| | committed | fresh run |
|---|---|---|
| `max\|χ_comb − χ_young\|` | `5.9119161e-48` | `2.619456e-48` |
| `tr_M combiner vs transfer rel` | `1.9515091e-16` | `1.0198718e-50` |
| `max\|χ_comb − χ_transfer\|` | `1.5407722e-15` | `6.6599317e-49` |

The second row is the one that matters: **~34 orders of magnitude**, and the
committed value sits exactly at the float64 floor (`1e-16`) while the fresh one
sits at the 50-dps serialization floor. The assertion's own text names the
threshold it was tested against — *"< 1e-12 float64 word-constant floor"* — so
the committed run was float64-limited by something in its path and the fresh
one was not.

## Why this is NOT claimed as a fix

I cannot attribute the change, and AGENTS.md requires attribution before
claiming a movement. Three candidate causes, none measured:

1. **The bootstrap fix changed module resolution.** The two probes now put
   `computations/` on `sys.path` before their imports; a different
   `_precision` / `hoefsmit_symbolic` may now resolve than did under the
   documented `PYTHONPATH=computations:computations/hecke:...` invocation, and
   an exact-arithmetic path may have replaced a float64 one.
2. **Environment.** The committed run may predate an `mpmath`/`pyhecke_native`
   change.
3. **A genuinely different code path** in the cross-check, unrelated to either.

Cause 1 is the interesting one and would be a finding in its own right: it
would mean the documented `PYTHONPATH` invocation was silently selecting a
float64 module, i.e. the masking bug degrading a NUMBER rather than merely
hiding a crash. That is a stronger claim than anything `qou-0e1t` or `qou-cds2`
has established and it needs measuring, not asserting.

## Next step

Run `a_operator_recursive_a3_crosscheck.py` directly, both ways — under the
documented `PYTHONPATH=...` and under `env -u PYTHONPATH` with the bootstrap —
and diff the two witnesses. If they differ, cause 1 is confirmed and the whole
`PYTHONPATH`-documented population needs re-examining for float64 selection,
not just for runnability. If they agree, check the environment block against
the committed witness.

**Do not "refresh" this witness to the better numbers before that measurement.**
A value improving is not evidence about why, and committing it would launder an
unexplained change as a precision win.
