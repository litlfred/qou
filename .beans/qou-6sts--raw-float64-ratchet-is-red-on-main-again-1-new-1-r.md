---
# qou-6sts
title: 'raw-float64 ratchet is RED on main again: 1 new + 1 regressed (2026-08-31)'
status: completed
type: bug
priority: normal
created_at: 2026-08-31T03:49:09Z
updated_at: 2026-09-03T11:06:59Z
---

MEASURED on `main` `83f5e6482e`, 2026-08-31T03:5xZ, by running
`computations/witness_raw_float64_audit.py` directly (the committed audit
witness on main said `new_not_baselined: 0`, so do not trust it -- same
staleness family as `qou-82ur`).

    dirty_witnesses      1045
    new_not_baselined       1
    regressed               1
    drained_files         168

NEW (4 raw float64 fields):
    computations/probes/arc-count-diagnostic-degeneracy.witness.json
    last touched a4f54a3127 "research(qou-0c19): the R^2=0.83 arc-count
    diagnostic is not in the witness it cites"  -> owning arc is qou-0c19

REGRESSED (89 -> 91):
    computations/audits/braid-encoding-audit.witness.json
    last touched 89f1137463 "fix(qou-soj6): all three routes tried -- route 1
    lands, and it catches a 43% disagreement"  -> owning arc is qou-soj6

NOT MINE, and I am not fixing them from the Toffoli branch (#6341) -- different
domain, different producers, and the "ride on the active PR" rule is for
ADJACENT code. Handing them to the owning arcs instead.

FIX AT THE PRODUCER, per the standing rule: carry the value as `mpmath.mpf`
from its source and serialize with `_precision.fmt`, then re-run. Do NOT add
either file to `raw-float64-baseline.json`, do NOT `--rebaseline`, and do NOT
hand-edit a number. Baselines drain, never grow.

WHY THIS KEEPS HAPPENING, and why this bean is about two names rather than the
mechanism: `qou-mnrd` (completed) already established the durable finding --
nothing runs the ratchet on a push, because CI is `workflow_dispatch`-only under
the 2026-06-30 Actions-billing directive, and the owner reaffirmed that
dispatch-only choice on 2026-08-09 with this exact failure cost on the table.
So the enforcement gap is settled policy, not an open item, and re-proposing a
push trigger is out of scope. `qou-mnrd`'s own conclusion is that WHICH files
are dirty is transient and cheap to drain; this bean exists only to name the
current two so the arcs that produced them can drain them, and should be closed
when they are -- not held open as a tracker for the class.

A TRAP I walked into while measuring this. I first ran the ratchet on a tree
**146 commits behind main** and got a different `dirty_witnesses` (1049) and
`drained_files` (165) with the SAME two offenders. The offenders happened to be
stable; the counts were not. Re-measure on the tip before quoting any figure
from this family.

A SECOND TRAP, in the harness rather than the corpus. `precision-gates.sh`
prints `NEW dirty witnesses : 0` for the padding-family ratchets, and a grep
that matches that phrase reads as an all-clear while the raw-float64 ratchet is
red one line further down under a DIFFERENT phrase (`NEW witnesses carrying raw
float64`). I misread it that way for one turn. The gate to read is the `RED:`
summary line, or the per-audit witness's `new_not_baselined` / `regressed`
fields -- never a phrase match on one ratchet's wording.


---

## UPDATE 2026-08-31T07:3xZ — a THIRD offender, and it landed after this bean was written

Re-measured on current `main` (`e8f5a64a81`), same command:

    new_not_baselined       2      (this bean recorded 1)
    regressed               1

The two NEW are `probes/arc-count-diagnostic-degeneracy` (4 fields, already
named here) and:

    computations/probes/bpp-higher-a-sparse.witness.json     (2 fields)
    computedAt 2026-08-31T03:45:36Z
    landed in 241985c108 "research(qou-gcmn) ANSWERED: B_pp DECLINES with A"
    -> owning arc is qou-gcmn

This bean's measurement was taken at `83f5e6482e` at 03:49Z, four minutes
after that witness was written, so the two do not conflict — it simply was
not on the tip yet. Which is this bean's own "re-measure on the tip" trap
firing on the bean itself, four minutes wide.

**The disposition stands unchanged**: hand it to `qou-gcmn`, fix at the
producer, do not baseline it. Close this bean when all three drain.

## A THIRD TRAP, and it is worse than the two recorded above

Both traps in this bean are about **misreading the output**. There is a
third, one level down: **the bare invocation cannot fail at all.**

    computations/witness_raw_float64_audit.py:1027
        return 1 if (args.strict and (new_files or grew)) else 0

Measured just now on the same tree, same offenders:

| invocation | exit |
|---|---|
| `python3 computations/witness_raw_float64_audit.py` | **0** |
| `python3 computations/witness_raw_float64_audit.py --strict` | **1** |

So `$?` is not a signal without the flag. The documented paths are fine —
`scripts/precision-gates.sh` passes `--strict`, and so does
`witness-staleness.yml` — but a hand-run of the bare form exits 0 over an
arbitrarily red corpus.

**I did exactly that, on six PRs.** Every `qou-srvu` slice verification I ran
this session (#6241, #6245, #6250, #6255, #6259) plus the `qou-wc8f`
follow-through (#6385) used the bare form and reported the gate as passed.
The *counts* I quoted were read correctly off stdout and the conclusions
happen to hold — `NEW dirty 0` really was 0 on those branches — but I was
reading a number and calling it a gate, which is precisely the distinction
this bean's second trap is about. Recorded here rather than in a bean of its
own because it belongs to the same family: three ways to believe this ratchet
is green when it is not, and only one of them involves the corpus at all.

## 2026-09-03 — ratchet GREEN (NEW 0 / REGRESSED 0), exit 0 (session cool-johnson-t1wveh)

Drained at the producers (compute-precision-auditor sub-agent, verified). The
list had drifted: 174 of the originally-listed witnesses were already drained on
this branch; the live dirty set was **2 NEW + 3 REGRESSED**, all handled. No
`--rebaseline`, no baseline additions, no hand-edited numbers; git status
confirmed no sibling witnesses collaterally written.

| Witness | before -> after | disposition |
|---|---|---|
| probes/arc-count-diagnostic-degeneracy | 4 -> 0 | float(Fraction) -> exact rational to mpf, fmt |
| probes/bpp-higher-a-sparse | 2 -> 0 | per-row wall-clock renamed to reserved `elapsed_sec` |
| meson-spectrum-predictions | 20 -> 0 | full mpmath rewrite of the Markov-trace path (was float64 numpy) |
| delta-n2-lp-dual-extraction | 22 -> 0 | float64-seeded mp.mpf(Q0_FLOAT) -> full-precision Q_MP; 7/7 assertions pass |
| audits/braid-encoding-audit | 91 -> 6 | regression cleared (6 << baseline 89); residual is UPSTREAM float64 |

Commits: 9c8f0ca112, 0f546a2c93, 4228812c59, c80524fc70.

**Honest residual (NOT papered over):** braid-encoding-audit retains 6 float64
fields it cannot drain downstream — they echo float64 stored in the UPSTREAM
witnesses `option-b-proton-mass-full-chain.witness.json` and
`markov-trace-assembly-proton.derivation.json`, plus a hardcoded content-block
quote. This is the 'float64 input poisons the result' case. Draining to 0 needs
the upstream producers fixed -> follow-up bean (see below). The sub-agent
deliberately did NOT stringify the upstream floats to fake a pass.
