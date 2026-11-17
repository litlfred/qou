---
# qou-qb8e
title: 'HH^1 carrier: the MAGNITUDE channel — the actual open gate for c_3'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T10:15:00Z
updated_at: 2026-11-15T17:33:13Z
parent: qou-avtq
blocked_by:
    - qou-cds1
---

Successor to qou-qb8b + qou-qb8d, which between them settled the PARITY channel
for the HH^1 fibre-level c_3 carrier:

- qou-qb8b: bar-parity of the outer CLASS is normalization-dependent
  (Hilbert 90 over Q(zeta)/Q(zeta)^+) -- carries no information.
- qou-qb8d: bar-parity of the tr_M-PAIRED NUMBER is well defined against
  structural pins (He-Nie generator + Ocneanu trace), is NOT trace-blind, and
  is MIXED with a NONZERO bar-ODD component.

Net: the bar-parity obstruction that closed every real-q0 route does NOT close
the HH^1 route. The parity screen is PASSED. That was the cheap channel.

THE ACTUAL GATE IS MAGNITUDE, and it is untouched. Nothing so far reproduces
c_3's value (-2.0202 at the cache q0) or, more importantly, its ANCHOR SWING
-- the cross-anchor variation that is the whole reason c_3 is tier
'cal-anchored' rather than 'derived'
(docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).

What a real attack needs, in order:

1. **A map from the outer class to a NUMBER at the substrate anchor.** The
   n=3 pairing gives numbers in Q(zeta)[z]. c_3 is evaluated at real q0 ~
   1.10998, which is NOT a root of unity. Per AGENTS.md §"Im(q) at fibre vs
   observable level" the correct target is a HABIRO-RING element whose
   archimedean evaluation at q0 reproduces c_3 at THAT anchor. So the
   root-of-unity values must ASSEMBLE (over all zeta) into a Habiro element --
   that assembly is the real content and is not started.

2. **The Bring case.** n=3 is the mechanism; the Bring fibre is H_5 at zeta_5
   (bean qou-jcmw, for the DIMENSION count -- explicitly NOT its parity leg,
   see qou-qb8b).

3. **A falsifiable magnitude prediction BEFORE looking at the target.**
   Formalize-first: state what the construction predicts, then compare. Fitting
   a normalization to land on -2.0202 is a FIT, is the seventh-ansatz failure
   mode the corpus already names, and must not be wired.

ANTI-FIT GUARDRAIL (load-bearing): the parity result is NECESSARY, NOT
SUFFICIENT. Do not let "the parity works" license a magnitude fit. A derived
c_3 must come out of the construction with its normalization pinned in advance.

---

# FRONT-STATE CORRECTION (2026-08-08) — this bean was STALE; read before probing

I attacked this bean and generated four "findings", ALL of which were already in
the corpus. Recording the accurate front state so the next agent does not repeat
it. **The c_3 front is ~20 probes deep. Read the ledger + the capstone FIRST.**

## What this bean got wrong

It says "Nothing so far reproduces c_3's value or, more importantly, its ANCHOR
SWING". That framing is superseded. The swing is UNDERSTOOD:

 - the extractor is c_3 = (Q_beta/Q_N2 - 1)/u^3; S'(q*) = 2.37 x (1/u^3) is a
   SMOOTH O(1) prefactor over a tiny u^3 (2026-07-12 capstone result 3, #3636)
 - capstone verdict: "the wall was never physical". It has an explicit
   "what NOT to re-chase" section.
 - the swing is the 1/u^3 extractor acting on experimental Q_beta -- it is NOT
   a property of any fibre-level u-tilde function.

## The ACTUAL open gate (replaces items 1-3 above)

log R = E(u~) + h*D(u~) HOLDS exactly (h = q - 1/q, u~ = q*u, verified to
ORD 19 with 9 over-determining orders zero; d_1..d_9 exact in Q(sqrt3);
extended to k=31 at ORD 63).

The D-ladder is DIVERGENT -- Gevrey class exp(Bk + Ck*log k), triple-confirmed.
So closing S needs RESUMMATION, and that is the open front:

 - NO instanton action identified (Borel-plane singularity unlocated)
 - Leroy estimator gate FAILS at every scanned s at k=21; parity-split branches
   0/9 and 0/9; the k=21 dlog-Pade/root-test inconsistency persists
 - fixed-base Jackson q-Borel REFUTED (over/under-accelerates; only the Q->1
   Leroy boundary matches the growth class)
 - D is SMOOTH through q*; the S=0 zero lives in the h*D -> S BRIDGE, not in D
 - the k=31 extension exists and the carrier SATURATES there
   (|O_31 - O_21| ~ 6.94e-29), so more terms alone will not move it

## Do NOT re-derive these (I did; all four were already known)

 1. "the hypersensitivity is an artifact not structure" -> capstone result 3
 2. the Skein bar-odd factorisation (q - q^-1) x bar-even -> KC21's S = h*D
 3. "h*D is anchor-blind and cannot be the swinging S" -> stated verbatim in
    qbeta-c3-qstar-k31-repin.witness.json: "the carrier is anchor-blind
    (spread 1.23e-9) and is NOT the swinging empirical S, so 'S=h*D(u)' is
    schematic, not a tight identity"
 4. "S_leak is a ~200x cancellation" -> the 1/u^3 ladder inversion, same result 3

## Where a real contribution could come from

The resummation arm, specifically: identify the Borel-plane instanton action for
the exp(Bk + Ck log k) class. Everything else is downstream of that. This is a
hard analysis problem, not a probe -- do not approach it by scanning.

Read first, in order:
  docs/coordination/ck-dk-canonical-registry.md  (KC21 row)
  docs/audits/2026-07-12-c3-wall-resolution-capstone.md  (+ its "do not re-chase")
  docs/audits/2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md
  computations/qbeta/qbeta-dladder-*.witness.json  (~20 arms, check before probing)

---

# SECOND FRONT-STATE CORRECTION (2026-08-09) — the resummation arm is DISSOLVED,
# not blocked. The premise was false.

I took the "ACTUAL open gate" above at face value ("identify the Borel-plane
instanton action for the exp(Bk + Ck log k) class") and went at it analytically
rather than by scanning, as instructed. There is no such class.

**The D-ladder is CONVERGENT.** Radius

    rho  = u~(q*) = 0.14279999664468968890572088577932032058109273315046...
    1/rho          = 7.0028012849899955047002755670642702546578912740699...

where q* = 1.4898947996883652482253115227781736826531279179281... is the unique
real root > 1 of the irreducible degree-12 factor of the Delta_net numerator --
i.e. **a zero of Q_b**, at which log R has a plain logarithmic branch point.

    d_k = -(1/(2h*)) * rho^-k / k * (1 + O(1/k)),   h* = q* - 1/q* = 0.8187064713519...
    1/(2h*) = 0.61071949165658530740674396151590239...

Amplitude predicted from the residue BEFORE looking at any d_k. Measured
k|d_k|rho^k / (1/(2h*)) = 0.9763 (k=21), 0.9874 (k=41), 0.9950 (k=101),
0.9975 (k=201), correction -0.51/k, no oscillation. Ladder extended to k=201
(the k=41 block was sympy `radsimp∘cancel∘together` per coefficient plus two
O(ORD^3) steps -- purely computational; a numeric-coefficient rebuild of the
same pipeline does ORD 403 in 53 s and matches the exact Q(sqrt3) ladder to
200+ digits for every k <= 41).

**What the 2026-07-12 divergence correction missed:** its singularity search
covered the sqrt branch points, the u~'=0 folds, the Q_A zeros and the
cos(alpha_eff) zeros -- but not the zeros of **Q_b**. The three nearest
singularities in the u~ plane are all Q_b zeros (0.14280, 0.25754, 0.25754).
The original PR #3716 Domb-Sykes "rho ~ 0.143" was RIGHT.

Every published diagnostic reproduces exactly and is re-explained by the
convergent law -- root test 5.91@21 / 6.08@27, log|d|/(k log k)=0.4963972525@41,
log|d|/k^2=0.04496114563@41, C=0.077/0.062/0.048 (the SAME C comes out of
fitting A+Bk+Ck log k to the exact convergent law: 0.084/0.072/0.051), and
|O_31 - O_21| = 6.94484e-29 which is not saturation but geometric convergence
(next increments 7.79e-41, 9.63e-53, 7.56e-124).

Cheap discriminator nobody ran: **k^2 * Delta^2 log|d_k| -> 1** (measured 0.960,
0.975, 0.987, 0.990 at k=20,40,80,99) while **k * Delta^2 -> 0** => Gevrey index
kappa = 0. The single-instanton probe fit Delta^2 = m/k + b and read b->0 as
"ordinary Gevrey", but both hypotheses give b->0; 1/k vs 1/k^2 is the test.

**Named invariant / falsifier** (so this negative is reusable): any claim of
Gevrey growth, a nonzero instanton action, or a Stokes ambiguity in D must first
exhibit a singularity of log R(q) - log R(1/q) strictly inside |u~| < rho. The
complete singular set is enumerated in the audit; none is.

**Payoff, and its limit.** At the CAL-2/muon pin u~(q0) = 0.00945395003124 is
15.10x INSIDE rho, so h*D(u~0) = -0.003486063636129187405605313929674524979867
is already pinned to 38 digits by the committed k<=41 ladder with a rigorous
tail bound. But this does NOT derive c_3, does NOT change its cal-anchored tier,
and does NOT close L2: the mu-p anchor swing on Q_beta is 29.96 ppb = 3.84x the
7.797 ppb target, and this bean's own earlier note stands -- the carrier is
anchor-BLIND (spread 1.23e-9) and is therefore not the swinging empirical S.

**So: the resummation arm was never the gate; it was an artifact.** The gate is
still the map from a bar-odd, anchor-blind fibre-level object to an
anchor-DEPENDENT number. Do not open another Borel/Leroy/Stokes/Ecalle probe on
this ladder.

Full write-up, with the singularity inventory, the exact minimal polynomials,
the reproduction recipe, and the corrections owed to registry row KC22 and
docs/precision-goals.md §"Open compute levers" (i):
  docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md

## OWED CORRECTIONS: 2 of 3 LANDED (foreground session, 2026-08-09)

Independently re-verified the reversal before acting on it. Decisive check, on
the CONVERGENT closed form with zero free parameters (|d_k| = AMP*rho^-k/k),
against the committed witness values as targets:

    diagnostic                    witness         convergent law    rel.err
    log|d|/(k log k) @k=41        0.4963972525    0.4964783325      1.6e-4
    log|d|/k^2       @k=41        0.04496114563   0.04496848945     1.6e-4
    root test |d|^(1/k) @21       5.9103783       5.917128064       1.1e-3
    root test |d|^(1/k) @27       6.0817125       6.085924273       6.9e-4

A purely convergent law reproduces ALL FOUR published "Gevrey" diagnostics to
~1e-4 with NO fitted parameter. Those diagnostics never discriminated convergent
from divergent -- they measured geometric growth against the wrong yardstick.
Curvature discriminator on the closed form: k^2 D^2 log|d_k| = 1.0011 (k=21),
1.0003 (41), 1.00005 (101) -> 1, while k D^2 -> 0. kappa = 0. CONFIRMED.

LANDED:
  1. docs/precision-goals.md "Open compute levers" (i) -- lever WITHDRAWN.
     Replaced with rho, q*, the Q_b-zero explanation, the closed form, the
     clause-by-clause supersession of the old text, and the 38-digit pinned
     h*D(u~0). Explicitly restates that this does NOT derive c_3, does NOT
     change its tier, and does NOT close L2.
  2. registry row KC22 -- exact non-holonomicity, 2-adic parity grading and
     Lean anchors kept VERBATIM; "super-exponentially divergent (q-Gevrey,
     radius -> 0; the ~0.143 ratio is the (k!)^C shadow, not a radius)" and the
     "=> transcendental/resurgent (Ecalle acceleration class)" inference struck.
     Added a note that non-holonomicity is UNAFFECTED by the radius correction.

STILL OWED (3rd item), now enumerated but NOT executed:
  3. Re-tier the resummation witnesses. Audit section 6 (appended) is the ledger
     of all 29: 6 UNAFFECTED (arithmetic/holonomicity/2-adic), 11 ILL-POSED
     (divergent-series estimators on a convergent series), 1 PARTIAL
     (extension-singularity: the exact k=31 data stands, its "Divergence-class C
     0.07737->0.06134" reading is the spurious 1/log k decay), 4 NOT ASSESSED
     (the deformed-meridian / odd-channel-Stokes family -- DIFFERENT OBJECT, the
     radius result does NOT automatically transfer, no claim made).

     The 11 should move from scope-(a) NEGATIVE to scope-(b) CLOSED/ILL-POSED so
     nobody reads "gate fails, needs more terms" as an open lever. Do NOT delete
     them -- they are the evidence the arm was exhausted properly, and their
     input (the exact ladder) is live. NO witness file was edited; all 29 still
     report allPassed:true, which is exactly why a bulk re-run would not have
     caught this.

---

# ITEM 3 EXECUTED 2026-08-15 — registry section 9d

The owed re-tier is landed: `ck-dk-canonical-registry.md` section **9d**. Group
B is re-tiered scope-(a) NEGATIVE -> scope-(b) CLOSED/ILL-POSED, nothing
deleted, with the reusable falsifier restated (any Gevrey / instanton / Stokes
claim on this ladder must FIRST exhibit a singularity of
`log R(q) - log R(1/q)` strictly inside `|u~| < rho`).

## Correction to the enumeration above: B is 12, D is 3

The 2026-08-09 note put `qbeta-odd-channel-stokes-borel` in group D ("different
object ... not `D(u~)`"). **Wrong, and checkable in one line** -- the probe
imports the D-ladder producer and calls it:

    import qbeta_dladder_generating_function_structure_probe as P   # line 87
    dk, KMAX, valid_top, odd_ok = P.build_d_ladder()                # line 136

Same `d_k`, so the radius result DOES transfer; it belongs in B. Verified by
reference count: the three genuine group-D probes (deformed-meridian,
deformed-rungs, borel-pade-resummation) have **0** refs to `build_d_ladder`;
this one has **4**.

That also settles whether its re-scope in PR #5050 over-reached: it did not.
Its own data corroborates convergence (Gevrey order drifts DOWN 0.08->0.05;
Borel-Leroy pole 0.147 at s=0.02, ~3% from rho, trending toward it as s->0).
Scope-(a): consistency with the radius, NOT a derivation of rho. Its method
negative -- plain-Borel does not transfer, G3 needs the true q-Borel chain --
survives intact.

Sharpest of the twelve: `qbeta-dladder-fibre-branch-stokes-ambiguity`, whose
`r* = 0.147` was recorded as an ambiguity scale and is in fact a ratio estimate
of `rho = 0.1428`. That arm was measuring the radius while reporting a Stokes
datum.

## THIS BEAN STAYS OPEN — the gate is untouched

Item 3 was the owed bookkeeping, not the gate.

**CORRECTED 2026-08-15 — the gate is a ZERO LOCATION, not a magnitude.** An
earlier revision of this section stated the gate as *"the map from a bar-odd,
anchor-BLIND fibre-level object to an anchor-DEPENDENT number"*, with the Phi_b
deficit and the h*D carrier as two objects failing the same test. **That framing
is circular and is withdrawn.** Measured over the same anchor gap
`dq = 1.28e-8`:

    carrier h*D   moves 1.23e-9   => slope ~ 0.096    (an ORDINARY smooth function)
    S_leak        moves 0.0491    => slope ~ 3.84e6   (within 17.7% of dc_3/dq ~ 4.66e6)

"anchor-blind" = ordinary derivative; "anchor-dependent" = the `1/u^3` ladder
inversion, which the 2026-07-12 capstone closed ("the wall was never physical").
A smooth function failing to track a quantity with a 4e7x larger slope is
arithmetic, not an obstruction.

**What is actually true.** `S_leak`'s zero `q*_S` lies BETWEEN the anchors
(80.28% from proton to muon); `S_leak` is linear through it (lever arm 4.0700 vs
measured ratio 4.0751 — 0.12%). This is **Route A** (2026-08-01), Lean-proved
sorry-free in `SLeakMagnitudeOffsetRatio.lean`. So `|S_leak|` at an anchor is
`slope x (distance to the zero)` and carries **no scale content** — which is why
this bean's own ~20 magnitude probes failed. They were matching the wrong thing.

The carrier `h*D(u~0) = -0.003486` is a nonzero near-constant while `S_leak`
crosses zero. A nonzero constant cannot equal a function crossing zero — that,
and not any magnitude comparison, is the real content of "S = h*D(u~) is
schematic, not a tight identity".

**RESTATED GATE (checkable):** the fibre carrier must reproduce the **zero
location `q*_S`**, not a magnitude.

**CORRECTION 2026-08-15 (`qou-kh7e`, PR #5074).** An earlier revision of this
paragraph closed with *"This also fits `q*_S`'s independent standing as the
third, decay-sector determination of q0."* **Withdraw that sentence.** `q*_S` is
root-found on `S = c_3 + Vol(4_1)` where `c_3 = (Q_beta^exp/Q_N2 - 1)/u^3` is
extracted from experimental Q_beta, so locating `q*_S` presupposes (H1). It has
no independent standing; the substrate rests on **two** pins. Registry section
**9f**; five other sites re-scoped in the same PR.

**The gate itself survives the withdrawal, and is sharper for it.** `q*_S` is a
determination of q0 *conditional on (H1)*, so a fibre carrier that reproduced it
would be deriving an experimentally-anchored quantity from the fibre — which is
exactly what "derive `c_3`" means. What the withdrawal removes is any reading in
which hitting `q*_S` is corroborated by an *independent* decay-sector pin: there
is no such pin, so hitting it is the whole claim, not a cross-check on it.

Two consequences for anyone attacking this:

  - Do NOT cite `q*_S` as evidence for (H1) on the way to the gate. That is the
    circularity, and it is what section 9f removes.
  - The genericity window is the calibration: **every** constant `V` in
    `(-c_3(mu), -c_3(p)) = (2.02020024, 2.06934258)`, width `0.0491423`, puts a
    zero between the anchors (7/7 unrelated constants tested). A carrier that
    lands *somewhere between the anchors* has therefore achieved nothing. The
    bar to clear is `q*_S` to a precision better than the window sweeps —
    `Vol(4_1)` sits 80.2961% from the proton end, so an in-window hit is the
    null result, not the signal.

`qou-qb8g`'s third correction (PR #5061) restores "c_3's bar-parity is
undetermined" and names the live route: parity read off the FIBRE object, not
inferred from two archimedean anchors that cannot see it. **qb8e and qb8g close
together or not at all — but the target is the zero.**

**Standing prohibition, now with its real justification:** do NOT open another
magnitude-matching probe on `|S_leak|` at an anchor. Not because it is hard, but
because the quantity has no scale content to match.

Still in force, unchanged: do NOT open another Borel/Leroy/Stokes/Ecalle probe
on this ladder; do NOT fit a normalisation to land on -2.0202.

---

# ITEM 1 IS ILL-POSED AT q0 — and the restated gate has no test power yet
# (2026-08-15, PR #5084; formalize-first, no scan run)

Item 1 above asks for "a HABIRO-RING element whose archimedean evaluation at
q0 ~ 1.10998 reproduces c_3 at THAT anchor". Two structural facts settle it
before any assembly is attempted. Neither needed a search.

## FACT A — a Habiro element has no value at q0

A Habiro element is `sum_n a_n(q) (q;q)_n`, convergent in the cyclotomic
completion BECAUSE `(q;q)_n -> 0` there. So a continuous evaluation at q0
requires `(q0;q0)_n -> 0`. The EXACT reflection identity

    (q;q)_n = (-1)^n * q^(n(n+1)/2) * (1/q;1/q)_n        every n, every q != 0

(termwise, from `1 - q^k = -q^k(1 - q^-k)`) shows the q > 1 branch carries an
explicit `q^(n(n+1)/2)` blow-up over the |q| < 1 branch. Hence

    |q| > 1  -> diverges super-exponentially
    |q| < 1  -> tends to a NONZERO limit
    q^N = 1  -> exactly 0 for n >= N

**Roots of unity are the only points admitting the evaluation, and q0 > 1 is not
one.** Item 1 is ill-posed AS WRITTEN — not merely hard. Same species as the
2026-08-09 finding that the resummation arm was an artifact: the premise is
malformed.

Lean, sorry-free, axioms `[propext, Classical.choice, Quot.sound]` on all 8
declarations:
`folio/quantum-observable-universe/lean/QOU/QBeta/HabiroEvaluationTrichotomy.lean`
  - `qPoch_reflection`                     the identity, GENERIC (any field)
  - `qPoch_eq_zero_of_pow_eq_one`          roots of unity, GENERIC (CommRing)
  - `qPoch_not_tendsto_zero_of_one_lt`     real q > 1, archimedean
  - `no_continuous_evaluation_of_one_lt`   the contrapositive punchline

## It is a DICHOTOMY, not a blanket prune

The closed-braid Markov trace is the one-variable Jones polynomial, so ITS
`(q;q)_m` expansion TERMINATES (2026-05-30 Habiro-PDE audit, stage 2, citing
Habiro 2000 Thm 1.1). A finite expansion is a Laurent polynomial and evaluates
at q0 fine. So:

    finite branch    -> evaluable; but then an INTEGER Laurent polynomial, and
                        FACT B applies to it
    infinite branch  -> not evaluable at q0 at all; needs an ANALYTIC
                        representative, and 1/q0 = 0.9009182839557415 is the
                        ONLY member of the bar-pair inside the unit disc

That last point inverts the framing and is the actionable part: the bar
involution `q -> 1/q` that qou-qb8g needs for the parity read-off is not an
extra step to arrange, it IS the map between the two convergence regimes.
**Evaluate the carrier at 1/q0, not q0.**

## FACT B — neither channel of the gate currently resolves anything

    magnitude       c_3's absolute value carries +/-1.262 propagated CAL-3
                    against a central value ~ -2.02 (registry 9e; the
                    aomega_o2 probe fires O1-remove on exactly this)
    zero location   sigma(q*_S) = 3.2876883e-7, while the genericity window's
                    IMAGE in q* is the anchor interval, width 1.28028e-8

Ratio **25.679447**. The ENTIRE set of constants that "put a zero between the
anchors" sits inside ONE error bar of q*_S. So "reproduce the zero" cannot
presently separate Vol(4_1) from the 7/7 unrelated constants that already pass.
Cross-checks to 1e-5 against the independently-computed factor in the qstar
experimental-budget witness — two routes, one number.

**So the restated gate is the right TARGET but not yet a decidable TEST.** It
becomes one after a ~26x sharper neutron Q_beta, and not before. That is the
honest state: the zero is the resolved channel and the magnitude is not, but
"resolved" here means 296 ppb against a 11.5 ppb structure.

## Standing prohibitions, updated

Still in force: no Borel/Leroy/Stokes/Ecalle probe on this ladder; no
magnitude-matching on |S_leak| at an anchor; no fitting a normalisation to land
on -2.0202.

**Added:** do NOT open a root-of-unity ASSEMBLY probe aimed at evaluating the
result at q0. The object has no value there and the Lean proves it. If the
assembly is pursued, its evaluation point is 1/q0 and its representative must be
analytic (state integral / convergent q-series), not the formal Habiro series.

**Added:** do NOT report a carrier candidate as a hit on the strength of landing
between the anchors. That is the null result — 7/7 unrelated constants do it,
and the whole window is narrower than one error bar on q*_S.

Probe: `computations/qbeta/qbeta_habiro_evaluation_dichotomy_and_test_power.py`
(exit 0, 7/7 assertions, experimental/proton pin).


---

# FRONT (a) — `1/q0` DOES NOT RESCUE THE CARRIER (2026-08-15, PR #5096)
# This CORRECTS the closing framing of PR #5084, written hours earlier.

#5084 concluded: *"1/q0 = 0.9009 is the only member of the bar-pair inside the
unit disc, which is exactly where a state integral / q-series converges.
Evaluate the carrier at 1/q0, not q0."* Right for a GENERIC q-series. **Wrong
for the object actually wanted.**

The figure-eight's cyclotomic (Habiro / Kashaev) expansion is

    J(4_1; q) = sum_n (q;q)_n (1/q;1/q)_n = sum_n prod_{j=1..n} (1-q^j)(1-q^-j)

Each term carries BOTH q and 1/q, so the bar involution merely swaps the two
brackets of each factor: **T_n(1/q) = T_n(q) EXACTLY**, every n, every q, any
field. Lean-proved sorry-free, `QOU.QBeta.Fig8CyclotomicBarInvariance` (6
declarations, axioms clean). Measured at the substrate pair: max relative
|T_n(q0)/T_n(1/q0) - 1| = **5.9e-49** over n=1..40; closed form
`-(q^j-1)^2/q^j` matches to **1.6e-50**; growth root |T_n|^(2/(n(n+1))) rises
monotonically toward q0 (0.766 -> 0.985 -> 1.048 -> 1.074).

## Why this is a correction, not a restatement

`HabiroEvaluationTrichotomy` (#5084) showed the BUILDING BLOCK `(q;q)_n` is
asymmetric — diverges above 1, tends to a nonzero limit below.
`BarInvolutionDomainObstruction` (#5093) showed the unit ball is not bar-stable.
Both are true and both survive. But `J(4_1)` MULTIPLIES the two branches, and
the asymmetry **cancels exactly**. So the substrate pair is not "one good side
and one bad side" for the figure-eight invariant — it is two equally bad sides.

## Net effect on front (a)

A **state integral** — an integral, convergent on `C \ R`, not a series in q —
is not one route among several. It is the **ONLY** route. The corpus already has
`computations/qbeta/phi_b_evaluator.py`, so the machinery exists.

**Standing prohibition, added:** do NOT attempt to make `J(4_1)`'s series
converge by choosing an evaluation point. No point in a bar-pair is better than
its partner; the invariant is bar-symmetric by construction.

## And read this with front (e)

Even a successful state-integral carrier **cannot be validated at present
precision**. Per PR #5093: sigma(c_3) = +/-1.262 (61% of |c_3|), so the magnitude
channel is 0.03-sigma — no evidence either way; and per #5084 the zero-location
channel is 25.7x short of separating Vol(4_1) from 7/7 unrelated constants.
Build it because it is the right mathematics, not because it can be tested yet.

Scope-(b) for the SERIES route (invariant: the involution fixes each factor).
Nothing here touches (H1) or argues against the state integral.

---

# CONVENTION PROVENANCE (2026-08-15, owner redirect — read before any carrier work)

The owner-redirect validity audit
(docs/audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md)
found the Q_beta ladder consumes the CONVENTION-C Markov parameter end-to-end
(alpha = (z-1)h/2, z = sqrt(q)/(1+q); qbeta_utils.py:124-125), and the
Q_beta channel is UNREGISTERED in trace-convention-registry.json. For this
bean's gate:

- **The target `q*_S` is a C-frame number.** Re-extraction under convention D
  moves c_3 to ~ -974; there is no ~ -2 value and no S-zero between the
  anchors in the D frame of the same ladder shape. A fibre carrier "hitting
  q*_S" is hitting a convention-C-conditional target — say so when reporting.
- **The gate's structural walls are convention-immune** (swing D/C = 1.0052;
  the 1/u^3 result, the entropy bound, and the (q;q)_n domain trichotomy do
  not involve z).
- Settle-the-convention is bean qou-b3nk; until it lands, carrier work should
  state "C-frame" on every value-level comparison.


## 2026-08-29 — workflow (both lenses survive): OPEN, blocked upstream on cds1; convention-agnostic braid-exclusion handle
|c3| gate untouched; -974 is a z-swap artifact not a D target (blocked on cds1). CONVENTION-AGNOSTIC scope-(b) prune: the magnitude carrier CANNOT be a braid-word image -- alpha is unbounded/non-constant in BOTH frames (alpha_C->-inf, alpha_D->+inf), so any polynomial relation forces all coeffs zero (BraidImageEigenphase{Exclusion,Algebraic}.lean, sorry-free, char + eigenvalue-pair; the proof never reads z). This is the |c3| analog of the avt1 affine-transport convention-agnostic handle. Sole surviving carrier = branch (3) KZ/Kohno-Drinfeld holonomy on V_(2,1), hbar=2ln q -- but red-team flags qou-pdix precision obstruction (0.579% NF ambiguity > 0.160% target effect, 3.6x). Also: D residual N2/N1~0.89 = NO rung convergence, so c3 may not be a convergent-ladder coeff under D. Audit 2026-08-29-convention-d-qbeta-front.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: BLOCKED.** Blocked on qou-cds1. Even if it unblocks, the zero-location gate is about 26× short of experimental resolution (C-frame). The prohibitions (no Borel/Stokes on the D-ladder, no q0 Habiro assembly, no magnitude matching) are backed by sorry-free Lean and stand.

Evidence: Blocked on `qou-cds1` (in-progress): the gate target q*_S is C-frame, and there is no S-zero between the anchors under D (`qou-iax1`). `qbeta_habiro_evaluation_dichotomy_and_test_power.py` re-run exits 0, 7/7 (σ(q*_S)=3.29e-7, ratio 25.679). Lean, all sorry-free by grep: `HabiroEvaluationTrichotomy`, `Fig8CyclotomicBarInvariance`, `BraidImageEigenphaseExclusion`/`Algebraic`. The D-ladder convergence (ρ=0.14280) is recorded in `docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`. That was not re-run here.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Progress Update (Round 65 — PR #8267)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8267`](https://github.com/litlfred/qou/pull/8267) (branch `feat/round65-radical-branching-bond-habiro-cusp-43c1`, Commit 1 `20143712c434683951cbe6f568953fd4a98454bc`, Commit 2 / Head `1ee46ede72413597113d706dd733554a25e327d5`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/QBeta/HabiroEvaluationTrichotomy.lean (`qPoch_one_two_and_eval_one`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/radical_branching_bond_habiro_cusp_probe.py` (`scriptHash: 949a90321cd5`) + `test/results/witnesses/radical-branching-bond-habiro-cusp.witness.json` (`allPassed: true`).
