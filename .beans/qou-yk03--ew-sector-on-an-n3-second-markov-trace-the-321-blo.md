---
# qou-yk03
title: 'EW sector on an N=3 SECOND Markov trace: the (3,2,1) block is occupied there, and every piece of the route is already in the corpus unconnected'
status: todo
type: task
priority: normal
created_at: 2026-09-05T12:51:20Z
updated_at: 2026-09-05T12:51:58Z
---

Opened 2026-09-05 from `qou-wapd`. Not started.

## The route

The corpus already holds every piece and has not connected them:

- **The flavour sector REQUIRES N=3.** `y_lambda_su_n.py` says so;
  `RowCapObstruction.lean` proves sorry-free that N=2 cannot host the
  decuplet (the alternating channel `dim V_{(1^3)} = C(N,3)` vanishes iff N<3).
- **The mass channel CANNOT be retuned to N=3.** `ocneanu_N_lockin_probe.py`
  — moving N re-weights channels the mass pipeline already evaluates.
- **Therefore flavour needs a SECOND trace on the same H_n(q)**, not a modified
  first one — and `HnMarkovTrace.lean` already types the Markov parameter as a
  free class field, so two instances are typeable TODAY.

## Why this bears on the electroweak sector specifically

`appendix-standard-model/sm-params-gauge-couplings.md` rules that the
lambda=(3,2,1) block 'carries no states' because l(lambda)=3 > N=2, and that
therefore 'every route from such a block to a physical number is either a Markov
trace, which the row cap sends to zero, or a spectrum, which has no states to
act on'. **That ruling is scoped to N=2.** At N=3 the block is occupied
(l(lambda)=3 <= N) and its Ocneanu weight is nonzero, measured
0.0103939752433 at q0. So the row-cap objection does not exclude an N=3 reading
of the EW sector; it excludes the N=2 one.

## First measurement, already done

`probes/beta_ew_n3_second_trace_probe.py` — characters exact through the
consumers' own Hoefsmit path:

    N=2: tr_M = 4.83789085692050323822   occupied 4/11   y_(3,2,1) = 0
    N=3: tr_M = 2.90062956640672874659   occupied 7/11   y_(3,2,1) = 0.01039...
    N=4: tr_M = 2.19236562357645905376   occupied 9/11   y_(3,2,1) = 0.01480...

**Read neither as confirmation nor refutation.** A Markov trace is normalised
and is not dimensionally a cotangent; the EW consumers build cot(theta_W) from
RATIOS of weighted quantities, not from a bare trace. The row exists so the
route can later be judged on a number.

## What would actually close or kill this

1. Is the EW sector's carrier the N=3 trace, or is that flavour-only? This is
   the load-bearing question and it is NOT settled by the arithmetic above.
2. If N=3: what RATIO of N=3-weighted quantities is the cot(theta_W) reading,
   and does it land near 1.82306787 WITHOUT a proximity search over candidate
   residual factors? The N=2 construction's factor was selected as closest of 74
   — that is the fit signature the anti-fit discipline exists to catch, and an
   N=3 redo that repeats it has gained nothing.
3. The corpus's own preferred lever is DIFFERENT: the Milnor triple linking
   mu-bar_123, which separates the two U(1)s that theta_W mixes. It is gated on
   the open SU(3) sector. If mu-bar_123 lands first this route may be moot.

## NOT claimed

That N=3 is the right reading of the EW sector. This bean records that the
row-cap objection is N=2-scoped and that the N=3 door is structurally open, not
that it should be walked through.
