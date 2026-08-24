---
# qou-2zjp
title: 'GAP: alpha_high_precision is broken on main — bisection bracket no longer contains a root'
status: todo
type: task
priority: normal
created_at: 2026-08-24T14:53:43Z
updated_at: 2026-08-24T17:52:15Z
---

## What happens

    $ QOU_Q0_ANCHOR=proton python3 computations/alpha/alpha_high_precision.py
    HIGH-PRECISION alpha* DETERMINATION (dps=50)
      q_0 = 1.1099785827513808
      M_p = 938.27208943,  M_n = 939.56542179
      Bracket: err(0.3) = +1.074673%, err(0.32) = +0.649810%
      ERROR: no sign change in bracket
    (exit 1)

The mpmath bisection is hardcoded to the bracket [0.3, 0.32]. Both endpoints
now give a POSITIVE error, so there is no root inside it and the script exits
before writing anything.

## Not caused by the q0 migration

It fails identically at BOTH anchors -- the decomposition harness records
`FAIL(m=1,p=1)`, i.e. the muon leg (its own declared anchor, the state on
main) fails too. So this is pre-existing breakage on main, surfaced by the
migration sweep rather than introduced by it. Its witness cannot be migrated
until the producer runs at all.

## Why it looked silent

It reports the error on STDOUT, not stderr, so a harness capturing only stderr
records rc=1 with an empty message. Worth knowing for any other sweep.

## Next honest step

Someone who knows what alpha* is supposed to be needs to decide whether the
bracket is stale (widen/re-derive it) or whether the root genuinely left the
interval because an upstream constant moved -- in which case the interesting
question is which one, and the committed witness is asserting a value the
current code can no longer reproduce. Do NOT just widen the bracket until it
finds something; that would fit a number rather than derive it.


## DIAGNOSED 2026-08-24 — not a stale bracket. The root MOVED, and convention C→D is why.

The original entry said "someone needs to decide whether the bracket is stale
or the root left the interval". It is the second, and the cause is identifiable.

**The root exists and is well-defined.** `err_n_mp(alpha)` is smooth and
monotonically decreasing; scanning alpha in exact 1/50 steps puts the zero
between 0.34 and 0.36. Bisected: **alpha* = 0.35088642931861095442**.

**The committed witness says alpha_star = 0.3058074307438076264762** — which is
INSIDE the old bracket [0.30, 0.32]. So the bracket was correct when written.
The root has since moved **+14.741 %**.

**It is NOT the q0 anchor.** Measured at both:

    manifest-resolved   alpha* = 0.35088642931861095442
    forced MUON         alpha* = 0.35088642931861095442
    forced PROTON       alpha* = 0.35088641146608020901

The two anchors differ in the 8th decimal — that is the 11.54 ppb separation.
The 14.741 % shift is anchor-independent, so the q0 migration neither caused
nor can fix it.

**It is NOT the producer.** `alpha_high_precision.py` has ZERO commits since the
witness was last regenerated (2026-06-22). Byte-identical source, headline
result moved 14.7 %: textbook import-cone drift.

**It is convention C→D.** The only `hecke_core` commit in the window is
`6086572c4e` (2026-08-15), the owner-approved convention migration, whose own
message records:

    z   0.4993203341836945 -> 0.6126880371464652   (C -> D, +22.70 %)

z feeds the Hecke traces, which feed `V_blend`/`tower`, which is what the
bisection roots. **So the committed alpha* = 0.30580743 is a CONVENTION-C
VALUE**, and the "broken bracket" is a symptom: [0.30, 0.32] brackets the
C-frame root, not the D-frame one.

## What to do, and what NOT to do

Re-centring the bracket on the D-frame root is legitimate and is NOT fitting —
the root is a well-defined zero of a monotone function and its location is
measured above, not chosen to hit a target. But do **not** just widen it and
regenerate: that would silently replace a published alpha* with a value 14.7 %
away under a different convention, with nothing in the witness saying so. The
regenerated witness must record that it is D-frame.

This is the same class as the AGENTS.md standing note that the Q_beta c_k ladder
is C-frame throughout and needs re-derivation under D (bean `qou-cds1`).
alpha* is another C-frame quantity that nobody had flagged.

## Scope: alpha* is probably not alone

112 producers import `hecke_core`. **30 of their witnesses were computed before
2026-08-15** and so may carry C-frame values. That is an UPPER BOUND, not a
count — importing `hecke_core` does not prove the value depends on z, and
`computedAt` is a proxy for the code version rather than proof of it. alpha* is
the one confirmed instance, measured at 14.741 %. Worth converting the bound
into a real number before anyone regenerates in bulk.
