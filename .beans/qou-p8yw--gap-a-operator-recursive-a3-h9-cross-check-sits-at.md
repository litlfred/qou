---
# qou-p8yw
title: 'GAP: a-operator-recursive-a3-h9 cross-check sits at the float64 floor in the committed witness but at 50 dps on a fresh run'
status: completed
type: task
priority: normal
created_at: 2026-08-30T14:43:04Z
updated_at: 2026-08-30T15:12:04Z
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


## 2026-08-30 — MEASURED. Cause 1 is REFUTED; the interesting hypothesis is dead

Ran `a_operator_recursive_a3_crosscheck.py` both ways, as this bean prescribed.

    run (a)  PYTHONPATH=computations:computations/a_operator:...   exit 0
    run (b)  env -u PYTHONPATH, from repo root                     exit 0

**Every non-ephemeral field is byte-identical between the two.** The witness
writer itself said so on the second run — *"[unchanged — kept on-disk commitSha
for staleness]"*.

So the documented `PYTHONPATH` invocation does **not** select a float64 module.
The speculation that the masking bug was degrading a *number* rather than
merely hiding a crash is **wrong**, and the corollary I floated — that the whole
`PYTHONPATH`-documented population needs re-examining for silently degraded
numbers — does not follow from anything. Withdrawn.

## What the movement actually is: an ordinary two-month-stale witness

    committed   2026-06-28T17:11:53Z   mpmath 1.3.0   scriptHash 8db718c4294d
    fresh       2026-08-30             mpmath 1.4.1   scriptHash 8db718c4294d

**The producer's own source is unchanged** — identical `scriptHash`. Both fresh
runs agree with each other and differ from a witness nobody has regenerated in
two months.

## Remaining candidates, and why I cannot close it here

- **Import-cone drift** — the likelier one. The stale value `rel = 1.9515091e-16`
  sits exactly at the float64 floor, and no `mpmath` version bump turns a double
  into 50 correct digits; something in the cone stopped laundering an f64. The
  transfer reference (`reduced_block_kernel.chi_all_lambda_reduced_block`,
  `dps=50`) carries no `float(` today.
- **Environment** — `mpmath 1.3.0 -> 1.4.1`. Cannot explain a 1e-16 -> 1e-50
  move on its own, for the reason above.

**Dating it is not possible in this clone, and that is a finding in itself.**
The repo is shallow (`git rev-parse --is-shallow-repository` -> true). The
witness's `commitSha 406489450c9b…` does not resolve, and `git log -- <file>`
attributes everything predating the graft to `cdb64587b8`, which has **no
parents** (`git rev-list --count` -> 1) and reports "41473 files changed,
14448426 insertions" — the graft artifact, not a diff.

## Next step (unchanged in aim, narrowed in method)

Run `computations/audits/witness_import_cone_staleness_audit.py` against this
producer to identify which cone member moved. Do NOT date anything with
`git log` in a shallow clone.

**Still do not refresh this witness to the better numbers** until the cone
member is named. Two reproducible runs agreeing is evidence the value is
*right*; it is not evidence about *why it changed*, and committing it without
that is the laundering this bean was opened to avoid.


## 2026-08-30 — CLOSED. The cone member is `canonical_trm_reference.py`

**Import-cone drift, as narrowed.** The audit's own transitive walk on this
producer: **63 cone modules, 21 datable, and all 21 post-date the witness**
(newest 2026-08-30 vs `computedAt` 2026-06-28). `canonical_trm_reference.py` is
among them; so is `markov_weights_symbolic.py`, which imports it.

**The mechanism is arithmetic, not a coincidence.** `06788fd463` (today) created
`canonical_trm_reference.py`, replacing the tr_M reference that *fifteen files*
had hardcoded as `mp.mpf("1.0653062286131670…")` with a value read from
`atomic-tr-m-mpfr-50dps*.witness.json`, selected by anchor stamp. `654c1a2a46`
added a `mp.dps < 60` guard because *"parsing it at mpmath's default dps=15
would silently round it"*.

That literal is **17 significant figures**. A comparison against it cannot show
agreement better than ~1e-16 however exact both sides are. So the committed
`rel = 1.9515091e-16` was never a disagreement between the combiner and the
transfer — **it was the truncation of the constant they were compared against.**
Against the 50-dps reference the real agreement shows: `1.0198718e-50`.

**Refreshed** in `e4d5fb5b7b`, which is now safe where it was not: producer
source unchanged (`scriptHash 8db718c4294d` both), both fresh runs byte-identical,
cause named. 4/4 assertions; the verdict is unchanged and now rests on an exact
reference rather than a truncated one.

**Not traced:** the exact cone edge carrying the reference into the
`chi_all_lambda_reduced_block` transfer comparison. Attribution is by three
converging measurements (in-cone, moved after, magnitude matches its documented
effect), not by a dataflow trace. Stated so the next reader knows which part is
proved.

## Two corrections to my own reasoning, both worth keeping

1. **"PYTHONPATH selects a float64 module"** — refuted by measurement; the two
   invocations are byte-identical. The corollary I drew from it (re-examine
   every PYTHONPATH-documented producer for degraded numbers) died with it.
2. **"The import-cone audit will report a vacuous clean in a shallow clone"** —
   also wrong. It reports **1,799 of 3,267** cone-stale, prints an explicit
   `⚠ SHALLOW CLONE` banner, and calls its own count a LOWER BOUND covering
   only post-graft commits. It returns `None` for pre-graft modules *by design*
   — a correct refusal to date what it cannot see, and better handling of the
   shallow hazard than the two audits I had to annotate.

Top movers corpus-wide, for whoever drains this: `pyhecke/constants.py` (1470
witnesses), `canonical_trm_reference.py` (137), `substrate/hecke_core_symbolic.py`
(121), `qbeta/qbeta_utils.py` (49).
