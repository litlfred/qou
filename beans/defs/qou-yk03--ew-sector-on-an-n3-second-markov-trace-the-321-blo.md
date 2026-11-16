---
# qou-yk03
title: 'RESCOPED: does H_n(q) admit a SECOND Markov trace at N=3 — the Ocneanu-parameter question, NOT the fibre-dimension one (that is qou-8p1x)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T12:51:20Z
updated_at: 2026-11-16T21:54:00Z
parent: qou-rtxm
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

## RESCOPED 2026-09-05 on owner instruction — and the rescope I RECOMMENDED was wrong

**What I told the owner to rescope this to:** "build the non-self-dual 3-dim
object in the multi-fibre groupoid whose Sym^2 is irreducible." **That
recommendation was wrong, and the corpus-grep that should have preceded it
catches it in one command** (`grep -rln "non-self-dual" .beans/`, path 6):

- **`qou-e2j8` is COMPLETED and already holds a non-self-dual 3.** Its own
  title is "the live non-self-dual 3 (7 = 1+3+3bar)" and its body says it
  "SUPERSEDES the 'no such object' claim": octonion `G_2 = Aut(O)`,
  Gunaydin-Gursey `7 = 1 + 3 + 3bar`, the `3`/`3bar` are complex conjugates,
  therefore non-self-dual, therefore **PASSES the Sym^2 gate**. Discrete
  skeleton machine-checked (`det3_cyclic_invariant`, `PSL(2,7) = GL(3,F_2)`).
  What is missing is a **MATHLIB GAP** — no `Octonion`, no `G_2` Lie group —
  explicitly "not a structural obstruction".
- **`qou-8p1x` is a LIVE EPIC** ("routes to a 3-dimensional fibre / colour
  SU(3) — assessed and roasted") carrying a seven-route scoreboard for exactly
  this question. It rates the multi-fibre groupoid route I named as route #1,
  "weakest content", and roasts it: *"It is a NAME, not a construction. Nobody
  has exhibited the inequivalent fibre objects or shown their interaction space
  is three-dimensional. It relocates 'why is dim V = 3' to 'why are there
  exactly 3 inequivalent fibres' — the same question wearing a hat."* Its bean
  `qou-8p1i` is **SCRAPPED**.

So the recommendation would have re-opened a solved requirement via the route
its own epic rates worst. **Do not rescope this bean to the fibre-dimension
question. That question is `qou-8p1x`, and it has an owner.**

### What this bean uniquely holds, and what it is now scoped to

The fibre-dimension question ("where does a 3-dim `V` come from") and the
trace question ("given `N`, does `H_n(q)` carry a SECOND Markov trace, and what
forbids re-tuning the first") are DIFFERENT, and only the second is unclaimed.
The reframing that separates them is this bean's own contribution:

**N IS the Ocneanu trace parameter**, `a = q^{N-1}` — `a = q` is Jones/`gl_2`
(the mass pipeline), `a = q^2` is `gl_3` (the eightfold). ALL the N-dependence
sits in the weights `y_lam ~ s_lam(1,q,...,q^{N-1})`, so "choose N" and "choose
the trace" are ONE ACT, and the Schur-Weyl row cap is arithmetic rather than an
imposed rule. Verified independently at q0 against `y_lambda_su_n`:

    y_(2,1)/y_(3) = [2][N-1]/[N+2]   (balanced convention)
      N=2 0.48930712047797097
      N=3 0.774590881357880918
      N=4 0.958124031288484858

Exact at all three. These are different rational functions of q, so N=3
RE-WEIGHTS the surviving channels by 58 % — an N=3 channel must be a SEPARATE
trace, never a re-tuning of the mass one. `HnMarkovTrace.lean` already makes two
instances typeable by carrying the Markov parameter as a free class field, so
the object is statable today.

**Scoped question, one sentence:** is there a second Markov trace on `H_n(q)` at
`a = q^2`, consistent with `ocneanu_N_lockin_probe`'s result that the mass
channel cannot move, and what does the corpus's own trace-convention registry
say about registering it?

### CLOSED under the old scope — do not re-ask

"Is the EW sector's carrier the N=3 trace?" **No, on present evidence**
(analysis: `docs/audits/2026-09-05-ew-carrier-n3-trace-or-flavour-only.md`). EW
is SU(2)xU(1), not SU(3); putting it on an N=3 trace asserts a `gl_3` carrier
and nothing argues for one. The pull came from `(3,2,1)` reading like the SM
3-2-1, but `(3,2,1)` is selected STRUCTURALLY as the unique self-conjugate
partition of 6 (verified: 11 partitions, exactly one self-conjugate) — reading
its parts as gauge factors is numerology. The measured N=3 trace of the EW word
(2.90062956640672874659) stays on file and is judged neither way.

### Two gates that stay shut regardless, and are NOT this bean's

- **Flavour/colour separation is PROVED unreachable** by the corpus's two tools
  (`gate_does_not_separate_two_triples`, `identification_invisible_to_selection_rule`);
  `qou-e2j8`'s 2026-08-29 note makes it its own open item under
  eightfold-open-problems item 4.
- **Hypercharge is open and is theta_W's actual blocker** (writhe->Y falsified,
  twist battery vacuous), and it is INDEPENDENT OF N.

### The objection that survives every version of this

The 1.8208 residual factor was selected as the closest of **74** enumerated
candidates, and its witness records the ansatz as neither supported at 1e-3 nor
falsified at 1e-2. An N=3 redo that runs the same proximity search over
re-weighted numbers gains nothing — that is the fit signature the anti-fit
discipline exists to catch.

## 2026-09-05 — ANSWERED, and my own rescope of five hours ago was partly stale

The rescoped question was: "is there a second Markov trace on H_n(q) at a = q^2
(N=3), and what does the trace-convention registry say about registering it?"

**YES, AND ITS PARAMETER IS ALREADY DERIVED IN CLOSED FORM.** The corpus holds
it and I framed it as open. `computations/ocneanu_param_from_fibre_dimension.py`
(6/6 PASS, re-run today) and its Lean companion
`QOU/BraidsAndKnots/FibreDimensionForcesTL.lean` give

    z_N = q^N / [N]_q     with  z * [N]_q = q^N  proved DIVISION-FREE over a
                          generic commutative domain

so the Ocneanu parameter is a FUNCTION OF THE FIBRE DIMENSION, and every N has
its trace. Measured at the proton q0:

    z(N=2) = 0.6126880371464652436505  -> N = 2.0   (== convention D, exactly:
                                                     q^2/[2]_q = q^3/(q^2+1))
    z(N=3) = 0.4493048090902078521850  -> N = 3.0
    z_C    = 0.4993203341836944525024  -> N = 2.5995155364  (NOT an integer)

Three consequences, none of which the bean had:

1. The second trace is not a construction problem. It is the N=3 member of a
   one-parameter family whose parameter is a closed form in N.
2. The probe's check C2 establishes that y_(1^3) = 0 **iff N = 2** -- so the
   Schur-Weyl row cap is visible AS A STATEMENT ABOUT THE TRACE, not only about
   the fibre. That is the same fact the bean's own lock-in measured, reached
   from the other side.
3. C5 is the strong one and is independent of everything above: convention C
   corresponds to a fibre dimension of **2.5995**, not an integer. So C was
   never any fibre's trace at all -- an argument for the D ruling that does not
   depend on any anchor or any comparison to data.

**SO THIS BEAN'S REMAINING SCOPE IS NARROWER AGAIN.** Not "does a second trace
exist" (it does, derived) but: what would REGISTERING the N=3 channel require,
given that its support differs from N=2's (C2), so every consumer that switched
would sum over different blocks? That is a registry-and-consumers question, not
a mathematics one.

**Method note, and it is the second time today.** I recommended rescoping this
bean to "build the non-self-dual 3-object" and the corpus-grep showed
`qou-e2j8` had already built it. I then rescoped it to the second-trace
question and the corpus-grep shows that is derived too. Both times the framing
was mine and the answer was on disk. The rule that keeps catching it is path 6
(grep .beans/) plus reading the probe rather than its bean summary.

## Found while doing this: the documented z_3 grep trap names the wrong quantity

`docs/audits/2026-08-16-colour-level-and-tln-compute.md` and bean `qou-d7h1`
both warn that "the literal 0.44930482320583087 in many witnesses is h_q, NOT
z_3 -- they differ at the 8th decimal". Measured at 65 dps
(probes/z3_muon_pin_vs_hq_misidentification_probe.py, 2/2), that literal is
**z_3 at the MUON anchor** (rel 2.17e-10, the literal's own truncation), while
h_q = q - 1/q is **53 % away** -- off by a factor of two, so the claim is not a
small slip inside a true statement.

The two numbers are ONE quantity at TWO ANCHORS: a layer straddle, not a
lookalike. Extent measured and small: 0 live producers (3 deprecated, 2 doc
sites carrying the misidentification itself). Both sites corrected.

## 2026-11-16 — N=3 Second Markov Trace Channel-Ratio Separation (`QOU.Foundations.ConventionDKeystoneTraceTower`, PR #8214)
- Formalized `ocneanuN2N3ChannelDet` and `ocneanu_n2_vs_n3_channel_ratio_det` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDKeystoneTraceTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `7cc3c04b0719e92286ff6279855cbf3f0b9a7826` | PR: `https://github.com/litlfred/qou/pull/8214`
- Kept at `status: in-progress` per merge-manager protocol.
