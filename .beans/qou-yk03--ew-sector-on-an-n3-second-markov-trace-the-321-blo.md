---
# qou-yk03
title: 'EW sector on an N=3 SECOND Markov trace: the (3,2,1) block is occupied there, and every piece of the route is already in the corpus unconnected'
status: todo
type: task
priority: normal
created_at: 2026-09-05T12:51:20Z
updated_at: 2026-09-05T15:10:35Z
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


## 2026-09-05 — BOTH SIDES ANALYSED. Recommendation: flavour-only (Side B).

Write-up: `docs/audits/2026-09-05-ew-carrier-n3-trace-or-flavour-only.md`.

**The reframing that matters: N IS the Ocneanu trace parameter**, a = q^{N-1}
(a=q -> Jones/gl_2, the mass pipeline; a=q^2 -> gl_3, the eightfold). All the
N-dependence sits in the weights y_lam ~ s_lam(1,q,...,q^{N-1}), so 'choose N'
and 'choose the trace' are one act, and the row cap is arithmetic rather than an
imposed rule.

**Lock-in verified independently at q0** against the corpus's y_lambda_su_n:

    y_(2,1)/y_(3) = [2][N-1]/[N+2]   (balanced)
      N=2 0.48930712047797097   N=3 0.774590881357880918   N=4 0.958124031288484858

Exact agreement at all three. Different rational functions of q, so N=3
RE-WEIGHTS surviving channels by 58% — an N=3 channel must be a SEPARATE trace,
never a re-tuning. (My first pass read a mismatch against the probe's stated
q[2][N-1]/[N+2]; that formula is in the ASYMMETRIC convention while the module
is balanced — off by exactly 1/q = 0.90091828. Both are right in their own
convention.)

**Side A (EW on N=3) is not refuted but is nearly empty.** The trace exists
arithmetically (2.9006, computed) and the row-cap objection IS scoped to N=2 so
it genuinely does not reach. But the N=3 CARRIER — a 3-dim fibre object — has
FOUR independent sorry-free proofs of non-existence in the single-fibre setting:
row cap, Sym2GateMultiplicity (dim must be even, 3 is odd),
SU2EmergenceRankForced (Lambda^2 V = 1 forces N=2), and
FibreFunctorDimensionNotCategorical (3-dim fibre functors EXIST and don't help —
monoidal, so Clebsch-Gordan is preserved and the needed singlet is absent by
parity). The required property is itself proved: NON-SELF-DUALITY.

**Two gates stay shut even granting N=3:** flavour/colour is not separable by
ANY object-level gate (no_object_gate_separates, scope-(b) — equal dim, equal FS
type, equal triality), and HYPERCHARGE is open and is theta_W's actual blocker
(writhe->Y falsified; the twist battery proved vacuous). The hypercharge gate is
INDEPENDENT OF N.

**The eightfold implication that decides it:** its N=3 is SU(3)_FLAVOUR, and its
own ledger marks the construction open. EW is SU(2)xU(1), not SU(3) — putting it
on an N=3 trace asserts a gl_3 carrier and nothing argues for that. The pull
comes from the label (3,2,1) reading like the SM 3-2-1; but (3,2,1) is selected
STRUCTURALLY as the UNIQUE self-conjugate partition of 6 (verified: 11
partitions, exactly one self-conjugate). Reading its parts as gauge factors
would be numerology. Real consequences of the self-conjugacy: kappa = 0 so
Molien's q^{-kappa} is exactly 1 on this block, and the block is bar-ODD.

**The objection that survives BOTH sides**, and is stronger than the row cap:
the 1.8208 residual factor was selected as closest of 74 enumerated candidates,
witness records 'neither supported at 1e-3 nor falsified at 1e-2'. An N=3 redo
running the same search on re-weighted numbers gains nothing.

**RE-SCOPE THIS BEAN.** 'Is the EW carrier the N=3 trace' is answerable now: no,
on present evidence. The question worth keeping is the FLAVOUR one it was
standing in for — build the non-self-dual 3-dim object, already reduced by the
eightfold chapter to one checkable property.
