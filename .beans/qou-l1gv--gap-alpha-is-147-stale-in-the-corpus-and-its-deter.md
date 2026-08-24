---
# qou-l1gv
title: 'GAP: alpha* is 14.7% stale in the corpus and its determining producer cannot run'
status: todo
type: task
priority: normal
created_at: 2026-08-24T13:05:13Z
updated_at: 2026-08-24T13:06:10Z
---

Found while triaging the last convention-C sites (`qou-cds1`, PR #5622).
`computations/alpha/alpha_high_precision.py` was on my list only because it
carries a C-frame `z`; it turned out to have **three** independent defects, and
the convention is the least important of them.

## 1. The documented α* is stale by +14.7 % — in its OWN convention

    docs/canonicalization-review.md:21,136     alpha* ~= 0.305807
    measured now, convention C (unchanged)     alpha* == 0.350886411466
                                               +14.7411 %

Both numbers are convention C, so **this drift is not the excision**. Something
upstream moved — the q₀ re-pin and/or a mass constant are the obvious
candidates — and nobody noticed, because the producer stopped being able to
report it (see 3).

## 2. Under the canonical convention D it is different again

    convention C   alpha* = 0.350886411466
    convention D   alpha* = 0.283762164005      (-19.13 % vs C)
    corpus         alpha* ~ 0.305807            (stale C)

The corpus value sits **between** the two live roots, which is how the staleness
stayed invisible: it looks like a plausible number from either side.

## 3. The producer cannot run, and has not been able to for some time

    $ python3 computations/alpha/alpha_high_precision.py
      Bracket: err(0.3) = +1.074673%, err(0.32) = +0.649811%
      ERROR: no sign change in bracket            -> exit 1

`a_lo/a_hi` are hardcoded `0.3 / 0.32`, a window built around the stale
0.305807. **Both live roots are outside it, on opposite sides** — C's 0.3509 is
above `a_hi`, D's 0.2838 is below `a_lo`. So converting the convention does not
fix it and does not break it further; it flips the sign of the whole error curve
(all-positive over the window under C, all-negative under D) without ever
crossing zero inside it.

## 4. It is also muon-pinned, against the standing directive

The run prints `q_0 = 1.1099785955573347` — the **muon** pin. The 2026-08-07
owner directive (reaffirmed 2026-08-15 R2) says compute defaults to proton.
That is a third, separate defect, and fixing it will move α* again.

## What this contaminates

`docs/alpha-blend-derivation.md:772` records **`alpha* = G/3` as "falsified by
PSLQ"**, citing this producer, and §5 discusses a "0.16 % match between α* and
G/3". `G/3 = 0.30532`, which is 0.16 % from the stale **0.305807** — and 13 %
from the live C root. So the falsification's *verdict* survives (it is further
away, not nearer) but its *reasoning* was against the wrong target, and any
other closed-form search run against 0.305807 was searching for a number that
is not α*.

The docstring calls α* *"the BLOCKING input for formal derivation: we need to
know exactly what α* equals before we can prove it."* It has been emitting
nothing.

## Why this is filed rather than fixed

Three entangled defects, each of which moves the answer: convention, bracket,
pin. Fixing any subset produces a number that is neither the old frame nor a
correct new one, and it would land in a witness where a reader could take it as
the new α*. That is the "defined residual != derived" hazard: publish it only
once all three are right.

Suggested order: (i) proton pin, (ii) convention D, (iii) re-derive the bracket
from a scan rather than hardcoding a window — the hardcoded window is what let
a 14.7 % drift go unreported for months. Then re-run the closed-form/PSLQ
search against the new α* and correct `alpha-blend-derivation.md` §5 + line 772.

Blast radius is small: the only importers are two audit scanners
(`witness_environment_split_audit`, `canonical_script_input_audit`), neither of
which consumes the math.
