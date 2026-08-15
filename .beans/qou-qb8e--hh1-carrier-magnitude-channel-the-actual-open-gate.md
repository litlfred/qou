---
# qou-qb8e
title: 'HH^1 carrier: the MAGNITUDE channel — the actual open gate for c_3'
status: todo
type: task
priority: high
created_at: 2026-08-08T10:15:00Z
updated_at: 2026-08-08T10:15:00Z
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
location `q*_S`**, not a magnitude. This also fits `q*_S`'s independent standing
as the third, decay-sector determination of q0.

`qou-qb8g`'s third correction (PR #5061) restores "c_3's bar-parity is
undetermined" and names the live route: parity read off the FIBRE object, not
inferred from two archimedean anchors that cannot see it. **qb8e and qb8g close
together or not at all — but the target is the zero.**

**Standing prohibition, now with its real justification:** do NOT open another
magnitude-matching probe on `|S_leak|` at an anchor. Not because it is hard, but
because the quantity has no scale content to match.

Still in force, unchanged: do NOT open another Borel/Leroy/Stokes/Ecalle probe
on this ladder; do NOT fit a normalisation to land on -2.0202.
