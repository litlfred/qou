---
# qou-po7i
title: q0 anchor is selected by sys.argv[0] — 2384 of 2785 producers undeclared, 1887 witnesses carry no anchor
status: in-progress
type: task
priority: normal
created_at: 2026-08-10T02:20:19Z
updated_at: 2026-08-10T02:21:04Z
---


## Opened retroactively — this work was done UNCLAIMED

Found while investigating `a-K-via-lp-dual-hecke-basis`, the last invalid-JSON
witness on bean `qou-mnrd`. The a-K fix itself was in that bean's scope; **this
finding is not**, and it was diagnosed, fixed and committed (`0a5b2b6c7`) before
a bean existed for it. Recording that here rather than leaving it implied.

## The finding

`computations/substrate/q_parameter.py:92-100` resolves the q₀ anchor as:

    _anchor = os.environ.get("QOU_Q0_ANCHOR", "").strip().lower()
    # else:
    _stem = Path(sys.argv[0]).stem
    if _stem in manifest["ideal_muon"]:  →  muon
    # anything else                       →  proton

So with the env var unset, **the anchor is chosen by the name of the invoked
script**, not by the producer that computes the value. Consequences:

  * a producer imported by a differently-named driver gets the driver's anchor;
  * a producer run under a wrapper, a test runner, or `python -c` gets no stem
    match at all and silently takes proton;
  * the same producer therefore yields 11.5-ppb-different numbers depending on
    how it was invoked, with nothing in the witness recording which.

## The size of it

    producers under computations/ (non-deprecated)   2785
    declared in q0_anchor_manifest.json               403
    UNDECLARED → fall through to proton by argv[0]   2384

    witness anchor audit buckets:
      Q0_OK               581
      Q0_ANCHOR_MISSING  1887     ← no q0Anchor field at all
      Q0_AMBIGUOUS         17
      Q0_VALUE_MISSING      1
      Q0_FLIP               0     ← no *contradictions*, which is why it is quiet

`Q0_FLIP = 0` is exactly why this has stayed invisible: the audit can only catch
a witness whose recorded anchor disagrees with its recorded value. A witness with
NO anchor recorded is classified `Q0_ANCHOR_MISSING`, which the audit's own
header calls "pre-backfill; not a failure". 1887 of them cannot flip because
they never declared anything to flip from.

## Worked example — how it bites

`a-K-via-lp-dual-hecke-basis.witness.json` was computed under muon and carried no
`q0Anchor`. Re-running it today took proton, because its stem is in no list. The
LP inputs `t_i` moved 3.0e-10 (z at the two anchors, verified to f64 epsilon) and
the LP amplified that to ~4.2e-7 in `x_star`.

I first mis-diagnosed that as a solver/precision difference and wrote it up that
way on PR #4895 — a wrong published claim that cost a round trip. **An anchor
that is not recorded gets attributed to whatever else changed.** That is the real
cost of `Q0_ANCHOR_MISSING`, not the ppb.

## Fix applied so far (one producer only)

Declaring the stem under `ideal_muon` does BOTH halves at once, which is the
argument for using the manifest rather than an env var at each call site:

  * pins the anchor independently of invocation — re-running with no env var is
    now bit-identical (244/244 fields) to `QOU_Q0_ANCHOR=ideal`;
  * `q0_anchor_is_declared()` starts returning true, so `WitnessBuilder` stamps
    `q0Anchor` + `q0Value` (witness.py:1014-1022). Q0_ANCHOR_MISSING → Q0_OK.

## What to do — and what NOT to do

**Do not bulk-backfill 2384 stems.** Guessing an anchor per producer asserts a
pin nobody established, which is precisely what witness.py:1010-1013 refuses to
do by default ("defaulting one in would assert a pin nobody established"). A
wrong declaration is worse than a missing one: it turns a known-unknown into a
confident lie, and it would move `Q0_FLIP` off zero for the wrong reason.

Suggested order:

  1. **Stop the bleed.** Make `WitnessBuilder.save` refuse to write a witness
     whose producer is undeclared — warn-by-default like
     `QOU_WITNESS_STRICT_FLOAT64`, with `QOU_WITNESS_STRICT_ANCHOR=raise` for
     new work. Same ratchet shape that took raw-float64 to green.
  2. **Declare on touch.** Any producer an agent re-runs gets its stem declared
     in the same commit, from the evidence of the committed witness's own value
     (the a-K method: compare against z or q₀ at both anchors — it is decisive
     to f64 epsilon). 2384 is a background drain, not a sweep.
  3. **Only then** consider making the fall-through explicit rather than
     silently proton.

Related: bean `tnjb` holds the muon→proton migration posture and the owner's
2026-08-07 note that the target end state is proton everywhere in compute but
that this does **not** authorise a bulk rewrite. This bean is the *recording*
problem, not the *migration* problem — a witness should say which anchor it used
whichever anchor that is. Keep them separate.
